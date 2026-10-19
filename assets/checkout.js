/*!
 * AllCoaching on-page checkout — sign up and buy a studio plan without leaving allcoaching.in.
 *
 * Drop-in: any page that loads this file turns every element with [data-checkout] into a
 * button that opens the checkout sheet. Optional attributes on the button:
 *   data-plan="starter|growth|pro"   preselect a plan
 *   data-where="hero"                where the click came from (tracking)
 * Optional page config, set BEFORE this script:
 *   window.AC_CHECKOUT = {
 *     page: 'lp_competitive',   // tracking page name
 *     variant: 'v1',            // tracking variant
 *     vertical: 'competitive',  // studio vertical id (competitive|entrance|school|skills)
 *     plan: 'growth',           // default plan
 *     coupon: '',               // activation code applied automatically (campaign offers)
 *     trial: true               // offer the 14-day free trial next to buying
 *   };
 * URL overrides: ?plan=pro  ?code=OFFER50  ?ref=REFERRALCODE
 *
 * Flow: mobile + OTP → name + academy → plan → Razorpay → studio.
 * Every API call mirrors studio.allcoaching.in's own onboarding (same endpoints, same order,
 * same payloads), and every conversion event mirrors studio's dataLayer contract exactly:
 *   purchase_complete  (event_id = Razorpay payment id — the id the server CAPI Purchase uses)
 *   studio_signup_complete, sign_up, lead_complete (event_id = lead_id = educator id)
 *   start_trial, user_identified
 * so the GTM tags (Meta Pixel, Google Ads, GA4) keyed on them fire here unchanged.
 * Funnel steps go out as `lp_checkout` (step = open | otp_sent | otp_verified | details_saved |
 * payment_open | payment_dismissed | done | error).
 *
 * The page keeps working without this file: every [data-checkout] element is also a plain
 * link to studio.allcoaching.in.
 */
(function () {
  'use strict';
  if (window.__acCheckout) return;
  window.__acCheckout = 1;

  // ── config ──────────────────────────────────────────────────────────────
  // Set API_DIRECT to 'https://allcoaching-admin.b-cdn.net/v1/educator/' once the API allows
  // https://allcoaching.in in CORS; until then calls go through the same-origin PHP proxy.
  var API_DIRECT = '';
  var PROXY = '/acapi/proxy.php?p=';
  var STUDIO = 'https://studio.allcoaching.in/';
  // Loaded as a <script> from studio; it sets window.AC_HANDOFF_READY when studio can accept
  // a signed-in handoff. Until then the educator signs in to studio once more with an OTP.
  var HANDOFF_PROBE = 'https://studio.allcoaching.in/handoff-ready.js';
  var RZP_SRC = 'https://checkout.razorpay.com/v1/checkout.js';
  var SKEY = 'ac_ck_v1';

  var CFG = window.AC_CHECKOUT || {};
  var Q = new URLSearchParams(location.search);
  var PLANS = {
    starter: { key: 'starter', label: 'Starter', fee: 699900, keep: '90%', fee_pct: '10%', meta: '512 GB · 1080p · 5 live hrs/month' },
    growth:  { key: 'growth',  label: 'Growth',  fee: 1299900, keep: '92.5%', fee_pct: '7.5%', meta: '1 TB · 1080p · 10 live hrs/month' },
    pro:     { key: 'pro',     label: 'Pro',     fee: 2499900, keep: '95%', fee_pct: '5%', meta: '3 TB · 4K · 15 live hrs/month · premium template' }
  };
  var ORDER = ['starter', 'growth', 'pro'];
  var VERTICALS = ['competitive', 'entrance', 'school', 'skills'];
  function validPlan(p) { return PLANS[p] ? p : null; }

  var PAGE = CFG.page || ('lp' + location.pathname.replace(/[^a-z0-9]+/gi, '_'));
  var VARIANT = CFG.variant || 'v1';
  var VERTICAL = VERTICALS.indexOf(CFG.vertical) >= 0 ? CFG.vertical : '';
  var TRIAL_OK = CFG.trial !== false;
  var COUPON = (Q.get('code') || CFG.coupon || '').trim().toUpperCase().slice(0, 40);
  var REF = (Q.get('ref') || '').trim().slice(0, 60);
  try { if (REF) localStorage.setItem('ac_ref', REF); else REF = localStorage.getItem('ac_ref') || ''; } catch (e) {}

  // ── state ───────────────────────────────────────────────────────────────
  var S = load() || {};
  S.plan = validPlan(Q.get('plan')) || S.plan || validPlan(CFG.plan) || 'growth';
  var quote = null;          // server coupon quote for the selected plan
  var busy = false;
  var countdownTimer = null;

  function save() {
    try {
      sessionStorage.setItem(SKEY, JSON.stringify({
        step: S.step, phone: S.phone, token: S.token, auth: S.auth, isNew: S.isNew,
        name: S.name, academy: S.academy, plan: S.plan, saved: S.saved
      }));
    } catch (e) {}
  }
  function load() { try { return JSON.parse(sessionStorage.getItem(SKEY) || 'null'); } catch (e) { return null; } }
  function clearSaved() { try { sessionStorage.removeItem(SKEY); } catch (e) {} }

  // ── helpers ─────────────────────────────────────────────────────────────
  function rs(paise) { return '₹' + Math.round(paise / 100).toLocaleString('en-IN'); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function uuid() {
    if (window.crypto && crypto.randomUUID) return crypto.randomUUID();
    return 'id-' + Date.now() + '-' + Math.random().toString(16).slice(2);
  }
  function b64url(str) {
    var b = btoa(unescape(encodeURIComponent(str)));
    return b.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  }

  function msgOf(j, fallback) {
    if (!j || typeof j !== 'object') return fallback;
    if (typeof j.message === 'string' && j.message) return j.message;
    if (j.errors && typeof j.errors === 'object') {
      for (var k in j.errors) {
        var v = j.errors[k];
        if (Array.isArray(v) && v.length) return String(v[0]);
        if (typeof v === 'string' && v) return v;
      }
    }
    if (typeof j.detail === 'string' && j.detail) return j.detail;
    if (typeof j.error === 'string' && j.error) return j.error;
    return fallback;
  }

  // One request helper for every endpoint. Resolves with the parsed JSON, or throws an
  // Error carrying the server's own message and HTTP status.
  function api(path, body, fallbackMsg) {
    var direct = !!API_DIRECT;
    var url = direct ? API_DIRECT + path : PROXY + encodeURIComponent(path);
    var isGet = body === undefined;
    var method = isGet ? 'GET' : (direct && path === 'login/update' ? 'PATCH' : 'POST');
    var headers = { 'Accept': 'application/json' };
    var payload;
    if (!isGet) {
      if (direct && path === 'login/update') {
        payload = new FormData();
        Object.keys(body).forEach(function (k) {
          var v = body[k];
          if (v == null || v === '') return;
          payload.append(k, typeof v === 'object' ? JSON.stringify(v) : String(v));
        });
      } else {
        headers['Content-Type'] = 'application/json';
        payload = JSON.stringify(body || {});
      }
    }
    if (S.token) {
      if (direct) headers['Authorization'] = 'Token ' + S.token;
      else headers['X-AC-Token'] = S.token;
    }
    return fetch(url, { method: method, headers: headers, body: payload, credentials: 'same-origin', cache: 'no-store' })
      .then(function (r) {
        return r.text().then(function (t) {
          var j = null;
          try { j = t ? JSON.parse(t) : null; } catch (e) {}
          if (!r.ok || (j && j.status === 'false')) {
            var err = new Error(msgOf(j, fallbackMsg || 'Something went wrong. Please try again.'));
            err.status = r.status;
            err.code = j && j.code;
            throw err;
          }
          return j || {};
        });
      }, function () {
        throw new Error('Please check your internet connection and try again.');
      });
  }

  // studio's studioLock.ts, line for line
  function hasLockInfo(i) { return i != null && ('onboarding_unlocked' in i || 'onboarding_free' in i || 'onboarding_paid' in i); }
  function isUnlocked(i) {
    if (i == null) return false;
    if (typeof i.onboarding_unlocked === 'boolean') return i.onboarding_unlocked;
    return !!(i.onboarding_free || i.onboarding_paid);
  }
  function isOnboarded(i) {
    if (i == null) return true;
    if (!i.plan) return false;
    return !hasLockInfo(i) || isUnlocked(i);
  }

  // ── tracking ────────────────────────────────────────────────────────────
  var dl = window.dataLayer = window.dataLayer || [];
  function firedGet() { try { return JSON.parse(localStorage.getItem('ac_ck_fired') || '{}'); } catch (e) { return {}; } }
  function once(key) {
    var f = firedGet();
    if (f[key]) return false;
    f[key] = Date.now();
    try { localStorage.setItem('ac_ck_fired', JSON.stringify(f)); } catch (e) {}
    return true;
  }
  // Last-touch ad attribution saved by /assets/attribution.js (+ this URL), as studio sends it.
  function attribution() {
    var out = {};
    try {
      var m = document.cookie.match(/(?:^|; )ac_attr=([^;]*)/);
      var st = m ? JSON.parse(decodeURIComponent(m[1])) : {};
      var src = st.last || st.first || {};
      Object.keys(src).forEach(function (k) { if (/^(utm_[a-z_]+|gclid|gbraid|wbraid|fbclid|twclid|msclkid)$/.test(k)) out[k] = src[k]; });
      if (st.first && st.first.lp) out.landing_page = st.first.lp;
    } catch (e) {}
    Q.forEach(function (v, k) { if (/^(utm_[a-z_]+|gclid|gbraid|wbraid|fbclid|twclid|msclkid)$/.test(k) && v) out[k] = v.slice(0, 200); });
    if (!out.landing_page) out.landing_page = location.pathname;
    return out;
  }
  function push(ev, params) {
    var o = { event: ev };
    for (var k in params) if (params[k] !== undefined) o[k] = params[k];
    dl.push(o);
    return o;
  }
  function step(name, extra) {
    var p = { step: name, page: PAGE, page_variant: VARIANT, vertical: VERTICAL || undefined, plan: S.plan };
    for (var k in extra) p[k] = extra[k];
    push('lp_checkout', p);
  }
  function eduId() { var u = S.auth && S.auth.user; return u && u.id != null ? String(u.id) : (S.phone || undefined); }
  function eduEmail() { var u = S.auth && S.auth.user; return (u && u.email) || undefined; }
  function normPhone(raw) {
    var d = String(raw || '').replace(/\D/g, '');
    if (d.length === 10) d = '91' + d; else if (d.length === 11 && d.charAt(0) === '0') d = '91' + d.slice(1);
    return d;
  }
  // studio's acIdentify(): Meta Advanced Matching / Enhanced Conversions, pushed before conversions.
  var lastIdentity = '';
  function identify() {
    var u = (S.auth && S.auth.user) || {};
    var name = String(u.name || S.name || '').trim().split(/\s+/).filter(Boolean);
    var o = {
      external_id: u.id != null ? String(u.id) : '',
      em: u.email ? String(u.email).trim().toLowerCase() : '',
      ph: normPhone(u.phone || S.phone),
      fn: name.length ? name[0].toLowerCase() : '',
      ln: name.length > 1 ? name.slice(1).join(' ').toLowerCase() : '',
      country: 'in'
    };
    var out = {};
    Object.keys(o).forEach(function (k) { if (o[k]) out[k] = o[k]; });
    var key = JSON.stringify(out);
    if (key === lastIdentity) return;
    lastIdentity = key;
    out.event = 'user_identified';
    dl.push(out);
  }
  // Push the last conversion with a GTM callback so the redirect waits for the tags
  // (Meta Pixel, Ads, GA4) to send. Falls back to a timer if GTM is blocked or slow.
  function pushThen(ev, params, cb) {
    var done = false;
    function go() { if (!done) { done = true; cb(); } }
    var o = { event: ev, eventCallback: go, eventTimeout: 2500 };
    for (var k in params) if (params[k] !== undefined) o[k] = params[k];
    dl.push(o);
    setTimeout(go, window.google_tag_manager ? 3000 : 600);
  }

  // ── UI ──────────────────────────────────────────────────────────────────
  var CSS = '' +
    '.ck-ov{position:fixed;inset:0;z-index:1000;background:rgba(10,15,61,.55);-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);display:flex;align-items:center;justify-content:center;padding:20px;opacity:0;transition:opacity .2s}' +
    '.ck-ov.on{opacity:1}' +
    '.ck{position:relative;width:100%;max-width:460px;max-height:calc(100dvh - 40px);overflow:auto;background:#fff;border-radius:22px;box-shadow:0 40px 90px -30px rgba(10,15,61,.6);font-family:"Inter Tight",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#14161F;transform:translateY(14px);transition:transform .25s}' +
    '.ck-ov.on .ck{transform:none}' +
    '.ck-hd{position:sticky;top:0;z-index:2;display:flex;align-items:center;gap:10px;padding:14px 16px 12px 20px;background:#fff;border-bottom:1px solid #E6E8F0}' +
    '.ck-hd img{width:28px;height:28px;border-radius:50%}' +
    '.ck-hd b{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:21px;letter-spacing:-.3px}' +
    '.ck-hd .sp{flex:1}' +
    '.ck-x{width:38px;height:38px;border:0;border-radius:10px;background:#F6F8FC;color:#4A5063;font-size:22px;line-height:1;cursor:pointer}' +
    '.ck-x:hover{background:#E8F0FF;color:#2B44FF}' +
    '.ck-pr{display:flex;gap:6px;padding:14px 20px 0}' +
    '.ck-pr i{flex:1;height:4px;border-radius:99px;background:#E6E8F0}.ck-pr i.on{background:#2B44FF}' +
    '.ck-bd{padding:18px 20px 22px}' +
    '.ck h3{font-size:23px;line-height:1.2;letter-spacing:-.025em;margin:0 0 6px;font-weight:700}' +
    '.ck .sub{font-size:14.5px;color:#4A5063;margin:0 0 18px;line-height:1.5}' +
    '.ck-sum{display:flex;align-items:center;justify-content:space-between;gap:10px;background:#E8F0FF;border-radius:12px;padding:10px 14px;margin:0 0 18px;font-size:14px;color:#4A5063}' +
    '.ck-sum b{color:#14161F}.ck-sum button{border:0;background:none;color:#2B44FF;font:600 13.5px/1 \"Inter Tight\",system-ui,sans-serif;cursor:pointer;padding:4px}' +
    '.ck label.l{display:block;font-size:13.5px;font-weight:600;margin:0 0 7px}' +
    '.ck-in{display:flex;align-items:center;border:1.5px solid #D9DCE7;border-radius:12px;background:#fff;transition:border-color .15s,box-shadow .15s;margin-bottom:14px}' +
    '.ck-in:focus-within{border-color:#2B44FF;box-shadow:0 0 0 4px rgba(43,68,255,.14)}' +
    '.ck-in span{padding:0 4px 0 14px;font-weight:600;color:#4A5063}' +
    '.ck-in input{flex:1;min-width:0;border:0;outline:0;background:transparent;padding:14px;font:500 17px/1.2 \"Inter Tight\",system-ui,sans-serif;color:#14161F}' +
    '.ck-in input.otp{letter-spacing:.5em;font-size:22px;text-align:center;font-family:"JetBrains Mono",ui-monospace,monospace}' +
    '.ck-chk{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;color:#4A5063;margin:2px 0 16px;cursor:pointer;line-height:1.45}' +
    '.ck-chk input{width:18px;height:18px;margin:1px 0 0;accent-color:#2B44FF;flex:none}' +
    '.ck-chk a{color:#2B44FF}' +
    '.ck-btn{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;min-height:54px;border:0;border-radius:12px;background:#2B44FF;color:#fff;font:600 16.5px/1.2 \"Inter Tight\",system-ui,sans-serif;cursor:pointer;box-shadow:0 14px 30px -12px rgba(43,68,255,.6);transition:background .2s}' +
    '.ck-btn:hover{background:#1A2FD9}.ck-btn[disabled]{background:#A9B4FF;box-shadow:none;cursor:not-allowed}' +
    '.ck-btn.sec{background:#fff;color:#2B44FF;border:1px solid #2B44FF;box-shadow:none;min-height:48px;font-size:15px;margin-top:10px}' +
    '.ck-btn.sec:hover{background:#F4F6FF}' +
    '.ck-link{display:inline-block;border:0;background:none;color:#2B44FF;font:600 14px/1.4 \"Inter Tight\",system-ui,sans-serif;cursor:pointer;padding:6px 0}' +
    '.ck-link[disabled]{color:#A9AEBD;cursor:default}' +
    '.ck-row{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:10px;font-size:13.5px;color:#7A8094}' +
    '.ck-err{display:none;background:#FFF6F6;border:1px solid #F3CFCF;color:#9B2C2C;border-radius:10px;padding:10px 12px;font-size:14px;margin:0 0 14px;line-height:1.45}' +
    '.ck-err.on{display:block}' +
    '.ck-ok{background:#F2FBF5;border-color:#CDEFD9;color:#0F7A3A}' +
    '.ck-plans{display:grid;gap:10px;margin:0 0 14px}' +
    '.ck-pl{position:relative;display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:center;border:1.5px solid #E6E8F0;border-radius:14px;padding:13px 14px;cursor:pointer;transition:border-color .15s,background .15s}' +
    '.ck-pl:hover{border-color:#C9D1FF}' +
    '.ck-pl input{width:18px;height:18px;margin:0;accent-color:#2B44FF}' +
    '.ck-pl.on{border-color:#2B44FF;background:#F7F8FF}' +
    '.ck-pl b{display:block;font-size:15.5px}.ck-pl small{display:block;font-size:12.5px;color:#7A8094;line-height:1.4}' +
    '.ck-pl .p{text-align:right;font-weight:700;font-size:16px;white-space:nowrap}.ck-pl .p small{font-weight:500}' +
    '.ck-pl .tg{position:absolute;top:-9px;right:12px;background:#2B44FF;color:#fff;font-size:11px;font-weight:600;padding:2px 9px;border-radius:99px}' +
    '.ck-cp{margin:0 0 14px}.ck-cp .ck-in{margin:8px 0 0}.ck-cp .ck-in button{border:0;background:none;color:#2B44FF;font:600 14.5px/1 \"Inter Tight\",system-ui,sans-serif;padding:0 14px;cursor:pointer}' +
    '.ck-tot{display:flex;justify-content:space-between;align-items:baseline;gap:10px;border-top:1px dashed #D9DCE7;padding:14px 0 6px;font-size:15px}' +
    '.ck-tot b{font-size:22px;letter-spacing:-.02em}.ck-tot s{color:#A9AEBD;font-size:15px;margin-right:6px}' +
    '.ck-fine{font-size:12.5px;color:#7A8094;margin:2px 0 16px;line-height:1.5}' +
    '.ck-or{display:flex;align-items:center;gap:10px;margin:16px 0 0;color:#A9AEBD;font-size:12.5px}.ck-or:before,.ck-or:after{content:"";flex:1;height:1px;background:#E6E8F0}' +
    '.ck-trust{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:14px;font-size:12.5px;color:#7A8094}' +
    '.ck-trust span:before{content:"\\2713";color:#16A34A;font-weight:700;margin-right:5px}' +
    '.ck-wait{text-align:center;padding:28px 0 12px}' +
    '.ck-spin{width:42px;height:42px;margin:0 auto 16px;border-radius:50%;border:4px solid #E8F0FF;border-top-color:#2B44FF;animation:ckspin .8s linear infinite}' +
    '@keyframes ckspin{to{transform:rotate(360deg)}}' +
    '.ck-done{text-align:center;padding:10px 0 4px}' +
    '.ck-tick{width:64px;height:64px;margin:0 auto 16px;border-radius:50%;background:#E7F7EE;color:#16A34A;display:grid;place-items:center}' +
    '.ck-tick svg{width:32px;height:32px}' +
    '@media (max-width:560px){.ck-ov{align-items:flex-end;padding:0}.ck{max-width:none;border-radius:20px 20px 0 0;max-height:94dvh;padding-bottom:env(safe-area-inset-bottom)}.ck-ov .ck{transform:translateY(40px)}}' +
    '@media (prefers-reduced-motion:reduce){.ck-ov,.ck{transition:none}.ck-spin{animation-duration:2s}}';

  var ov, box, body, lastFocus;
  function mount() {
    if (ov) return;
    var st = document.createElement('style');
    st.textContent = CSS;
    document.head.appendChild(st);
    ov = document.createElement('div');
    ov.className = 'ck-ov';
    ov.innerHTML = '<div class="ck" role="dialog" aria-modal="true" aria-labelledby="ck-t">' +
      '<div class="ck-hd"><img src="/assets/logo/allcoaching-logo.webp?v=20260707" alt="" width="28" height="28"/><b>AllCoaching</b><span class="sp"></span>' +
      '<button type="button" class="ck-x" aria-label="Close">×</button></div>' +
      '<div class="ck-pr" aria-hidden="true"><i></i><i></i><i></i></div>' +
      '<div class="ck-bd" aria-live="polite"></div></div>';
    document.body.appendChild(ov);
    box = ov.querySelector('.ck');
    body = ov.querySelector('.ck-bd');
    ov.querySelector('.ck-x').addEventListener('click', close);
    ov.addEventListener('mousedown', function (e) { if (e.target === ov && !busy) close(); });
    document.addEventListener('keydown', function (e) {
      if (!ov.classList.contains('on')) return;
      if (e.key === 'Escape' && !busy) close();
      if (e.key === 'Tab') trapFocus(e);
    });
  }
  function trapFocus(e) {
    var f = box.querySelectorAll('button:not([disabled]),input:not([disabled]),a[href]');
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
  function progress(n) {
    var bars = ov.querySelectorAll('.ck-pr i');
    for (var i = 0; i < bars.length; i++) bars[i].classList.toggle('on', i < n);
  }
  var opened = false;
  function open(plan, where) {
    mount();
    if (validPlan(plan)) S.plan = plan;
    lastFocus = document.activeElement;
    document.documentElement.style.overflow = 'hidden';
    ov.style.display = 'flex';
    requestAnimationFrame(function () { ov.classList.add('on'); });
    step('open', { where: where || '' });
    // Meta InitiateCheckout / GA4 begin_checkout: once per page view, valued at the plan on screen.
    if (!opened) {
      opened = true;
      var p0 = PLANS[S.plan];
      push('begin_checkout', {
        event_id: 'ic_' + uuid(), value: p0.fee / 100, currency: 'INR',
        content_ids: [p0.key], content_name: p0.label + ' plan', content_type: 'product', num_items: 1,
        where: where || '', page: PAGE, vertical: VERTICAL || undefined
      });
    }
    loadPricing();
    if (S.token && S.step === 'plan') renderPlan();
    else if (S.token && S.step === 'details') renderDetails();
    else renderPhone();
  }
  function close() {
    if (!ov) return;
    // Never close while a payment is being confirmed or the studio is opening.
    if (busy && body.querySelector('.ck-wait')) return;
    ov.classList.remove('on');
    document.documentElement.style.overflow = '';
    clearInterval(countdownTimer);
    setTimeout(function () { ov.style.display = 'none'; }, 200);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  function setErr(text, ok) {
    var e = body.querySelector('.ck-err');
    if (!e) return;
    e.textContent = text || '';
    e.classList.toggle('on', !!text);
    e.classList.toggle('ck-ok', !!ok);
  }
  function setBusy(btn, on, label) {
    busy = on;
    if (!btn) return;
    if (on) { btn.setAttribute('data-l', btn.textContent); btn.textContent = label || 'Please wait…'; btn.disabled = true; }
    else { btn.textContent = btn.getAttribute('data-l') || btn.textContent; btn.disabled = false; }
  }
  function summary() {
    var p = PLANS[S.plan];
    return '<div class="ck-sum"><span><b>' + p.label + ' plan</b> · ' + rs(p.fee) + '/year</span>' +
      (S.step === 'plan' ? '' : '<button type="button" data-act="plans">Change</button>') + '</div>';
  }
  function bindPlansLink() {
    var b = body.querySelector('[data-act="plans"]');
    if (b) b.addEventListener('click', function () {
      if (S.token && S.saved) renderPlan();
      else setErr('You can change the plan in the last step.', true);
    });
  }

  // ── step 1: mobile number ─────────────────────────────────────────────
  function renderPhone() {
    S.step = 'phone'; progress(1);
    body.innerHTML = '<h3 id="ck-t">Start with your mobile number</h3>' +
      '<p class="sub">We’ll send a 6-digit code to verify it. Your studio is created on this number.</p>' +
      summary() +
      '<div class="ck-err" role="alert"></div>' +
      '<label class="l" for="ck-ph">Mobile number</label>' +
      '<div class="ck-in"><span>+91</span><input id="ck-ph" type="tel" inputmode="numeric" autocomplete="tel-national" maxlength="10" placeholder="10-digit mobile number" value="' + esc(S.phone || '') + '"/></div>' +
      '<p class="ck-fine" style="margin:0 0 14px">By continuing you agree to the <a href="/terms" target="_blank" rel="noopener" style="color:#2B44FF">Terms &amp; Conditions</a> and <a href="/privacy" target="_blank" rel="noopener" style="color:#2B44FF">Privacy Policy</a>.</p>' +
      '<button type="button" class="ck-btn" id="ck-go">Send OTP</button>' +
      '<div class="ck-trust"><span>No card needed to sign up</span><span>Secure payment by Razorpay</span></div>';
    bindPlansLink();
    var ph = body.querySelector('#ck-ph'), go = body.querySelector('#ck-go');
    ph.addEventListener('input', function () { ph.value = ph.value.replace(/\D/g, '').slice(0, 10); setErr(''); });
    ph.addEventListener('keydown', function (e) { if (e.key === 'Enter') go.click(); });
    go.addEventListener('click', function () {
      if (busy) return;
      var v = ph.value.replace(/\D/g, '');
      if (!/^[6-9]\d{9}$/.test(v)) { setErr('Enter a valid 10-digit mobile number.'); ph.focus(); return; }
      setErr('');
      sendOtp(v, go);
    });
    setTimeout(function () { ph.focus(); }, 60);
  }
  function sendOtp(phone, btn) {
    setBusy(btn, true, 'Sending code…');
    api('login/', { phone: phone }, 'Could not send the code. Please try again.').then(function () {
      setBusy(btn, false);
      S.phone = phone; save();
      step('otp_sent');
      renderOtp();
    }, function (e) {
      setBusy(btn, false);
      setErr(e.message);
      step('error', { at: 'otp_send', error: e.message.slice(0, 100) });
    });
  }

  // ── step 1b: OTP ──────────────────────────────────────────────────────
  function renderOtp() {
    S.step = 'otp'; progress(1);
    body.innerHTML = '<h3 id="ck-t">Enter the 6-digit code</h3>' +
      '<p class="sub">Sent by SMS to +91 ' + esc(S.phone.slice(0, 5) + ' ' + S.phone.slice(5)) + '. <button type="button" class="ck-link" data-act="chg">Change number</button></p>' +
      '<div class="ck-err" role="alert"></div>' +
      '<label class="l" for="ck-otp">Verification code</label>' +
      '<div class="ck-in"><input id="ck-otp" class="otp" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="••••••"/></div>' +
      '<button type="button" class="ck-btn" id="ck-go">Verify &amp; continue</button>' +
      '<div class="ck-row"><span>Didn’t get it?</span><button type="button" class="ck-link" id="ck-rs" disabled>Resend in 30s</button></div>';
    var otp = body.querySelector('#ck-otp'), go = body.querySelector('#ck-go'), rsb = body.querySelector('#ck-rs');
    body.querySelector('[data-act="chg"]').addEventListener('click', renderPhone);
    otp.addEventListener('input', function () {
      otp.value = otp.value.replace(/\D/g, '').slice(0, 6); setErr('');
      if (otp.value.length === 6) go.click();
    });
    otp.addEventListener('keydown', function (e) { if (e.key === 'Enter') go.click(); });
    go.addEventListener('click', function () {
      if (busy) return;
      if (otp.value.length !== 6) { setErr('Enter the 6-digit code from the SMS.'); otp.focus(); return; }
      verifyOtp(otp.value, go);
    });
    var left = 30;
    clearInterval(countdownTimer);
    countdownTimer = setInterval(function () {
      left--;
      if (left <= 0) { clearInterval(countdownTimer); rsb.disabled = false; rsb.textContent = 'Resend code'; }
      else rsb.textContent = 'Resend in ' + left + 's';
    }, 1000);
    rsb.addEventListener('click', function () {
      if (rsb.disabled || busy) return;
      rsb.disabled = true;
      api('login/', { phone: S.phone }, 'Could not resend the code.').then(function () {
        setErr('A new code has been sent.', true);
        step('otp_sent', { resend: true });
        left = 30; rsb.textContent = 'Resend in 30s';
        clearInterval(countdownTimer);
        countdownTimer = setInterval(function () {
          left--;
          if (left <= 0) { clearInterval(countdownTimer); rsb.disabled = false; rsb.textContent = 'Resend code'; }
          else rsb.textContent = 'Resend in ' + left + 's';
        }, 1000);
      }, function (e) { rsb.disabled = false; setErr(e.message); });
    });
    setTimeout(function () { otp.focus(); }, 60);
  }
  function verifyOtp(code, btn) {
    setBusy(btn, true, 'Verifying…');
    api('login/verify', { phone: S.phone, otp: code }, 'That code didn’t work. Please try again.').then(function (j) {
      setBusy(btn, false);
      clearInterval(countdownTimer);
      var d = j.data || {};
      if (!d.key) throw new Error('Could not sign you in. Please try again.');
      S.token = d.key;
      S.auth = { key: d.key, created: d.created, user: d.user, organizations: d.organizations };
      var u = d.user || {};
      // studio's rule: the server says whether this verify created the studio.
      S.isNew = d.new_studio === undefined ? !((u.name || '').trim() || (u.email || '').trim()) : !!d.new_studio;
      var inst = d.institute;
      S.name = S.name || (inst && inst.director_name) || u.name || '';
      save();
      identify();
      step('otp_verified', { new_studio: S.isNew });
      // Meta Lead: a new educator verified their number. event_id = user id, the same id the
      // server-side CAPI Lead (LoginVerifyView) and studio's own lead_complete send, so all
      // three collapse into one Lead in Meta.
      var lid = u.id != null ? String(u.id) : '';
      if (S.isNew && lid && once('lead|' + lid)) {
        push('lead_complete', {
          lead_id: lid, event_id: lid, content_category: 'General', content_name: 'Educator signup',
          vertical: VERTICAL || undefined, user_email: u.email || undefined, user_phone: S.phone,
          ac_attribution: attribution(), page: PAGE
        });
      }
      if (inst && isOnboarded(inst)) { loadExisting(false); return; }
      if (inst == null && d.organizations && d.organizations.length) { loadExisting(true); return; }
      renderDetails();
    }).catch(function (e) {
      setBusy(btn, false);
      setErr(e.message);
      step('error', { at: 'otp_verify', error: String(e.message).slice(0, 100) });
      var o = body.querySelector('#ck-otp'); if (o) { o.value = ''; o.focus(); }
    });
  }

  // ── already has a studio ──────────────────────────────────────────────
  // A studio on its free trial can buy a plan here; a paid one can move up a plan.
  // Reads the same /institute/usage/ studio's Settings ▸ Plan reads.
  var EXISTING = null;
  function loadExisting(teammate) {
    if (teammate) { renderExisting(null); return; }
    showWait('Checking your studio…', '');
    api('institute/usage/').then(function (j) {
      var u = (j && (j.data || j)) || {};
      EXISTING = {
        plan: validPlan(u.plan) || null,
        onTrial: !!(u.trial && u.trial.active),
        trialEnds: (u.trial && u.trial.ends_at) || u.plan_expires_at || null,
        daysLeft: typeof u.plan_days_left === 'number' ? u.plan_days_left : null
      };
      renderExisting(EXISTING);
    }, function (e) {
      if (e.status === 401) { expired(); return; }
      renderExisting(null);
    });
  }
  function niceDate(s) {
    try { return new Date(s).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }); } catch (e) { return ''; }
  }
  function renderExisting(ex) {
    S.step = 'existing'; progress(3);
    var cur = ex && ex.plan ? ORDER.indexOf(ex.plan) : -1;
    // On trial: every plan (the trial plan itself is a first purchase, sent as renew).
    // Paid: only plans above the current one; renewal is offered in the last 60 days.
    var offer = !ex ? [] : ex.onTrial ? ORDER.slice()
      : ORDER.filter(function (k, i) { return i > cur || (i === cur && ex.daysLeft != null && ex.daysLeft <= 60); });
    var tick = '<div class="ck-tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg></div>';
    var team = !ex && S.auth && S.auth.organizations && S.auth.organizations.length && S.auth.organizations[0].role !== 'owner'
      ? S.auth.organizations[0] : null;
    if (!offer.length) {
      body.innerHTML = '<div class="ck-done">' + tick +
        '<h3 id="ck-t">' + (team ? 'This number is a team login' : 'You already have a studio') + '</h3>' +
        '<p class="sub">' + (team
          ? 'It is a teacher login on ' + esc(team.name || 'another academy') + '. Plans are bought by the academy owner. To start your own academy, use a different mobile number.'
          : 'This number is already linked to an AllCoaching studio' + (ex && ex.plan ? ' on the ' + PLANS[ex.plan].label + ' plan' : '') + '. Open it to keep building.') + '</p>' +
        (team ? '<button type="button" class="ck-btn sec" id="ck-new" style="margin:0 0 10px">Use a different number</button>' : '') +
        '<button type="button" class="ck-btn" id="ck-go">Open my studio</button></div>';
      body.querySelector('#ck-go').addEventListener('click', function () { goStudio(true); });
      var nb = body.querySelector('#ck-new');
      if (nb) nb.addEventListener('click', function () { S.token = null; S.auth = null; S.phone = ''; EXISTING = null; save(); renderPhone(); });
      return;
    }
    if (offer.indexOf(S.plan) < 0) S.plan = offer.indexOf('growth') >= 0 ? 'growth' : offer[0];
    var rows = offer.map(function (k) {
      var p = PLANS[k], same = ex.plan === k;
      var tag = ex.onTrial && same ? 'Your trial plan' : (!ex.onTrial && same ? 'Renew' : (k === 'growth' ? 'Most popular' : ''));
      return '<label class="ck-pl' + (S.plan === k ? ' on' : '') + '">' + (tag ? '<span class="tg">' + tag + '</span>' : '') +
        '<input type="radio" name="ck-plan" value="' + k + '"' + (S.plan === k ? ' checked' : '') + '/>' +
        '<span><b>' + p.label + '</b><small>Keep ' + p.keep + ' of every sale · ' + p.meta + '</small></span>' +
        '<span class="p">' + rs(p.fee) + '<small>/yr</small></span></label>';
    }).join('');
    var title = ex.onTrial ? 'Your free trial is running' : ex.plan ? 'Move up a plan' : 'Choose your plan';
    var sub = ex.onTrial
      ? 'Pick a plan to keep your academy live' + (ex.trialEnds ? ' after ' + esc(niceDate(ex.trialEnds)) : '') + '. Your year starts today.'
      : ex.plan ? 'You’re on ' + PLANS[ex.plan].label + '. Upgrade now and what you already paid this year is credited.'
      : 'Pick a plan for your studio. Your year starts today.';
    body.innerHTML = '<h3 id="ck-t">' + title + '</h3><p class="sub">' + sub + '</p>' +
      '<div class="ck-err" role="alert"></div>' +
      '<div class="ck-plans" role="radiogroup" aria-label="Plan">' + rows + '</div>' +
      '<p class="ck-fine">You’ll see the final amount, including any tax and any credit, on the payment screen before you pay.</p>' +
      '<button type="button" class="ck-btn" id="ck-pay">Continue to secure payment</button>' +
      '<button type="button" class="ck-btn sec" id="ck-open">Open my studio instead</button>' +
      '<div class="ck-trust"><span>Razorpay: UPI, cards, netbanking</span><span>Same studio, nothing to set up again</span></div>';
    var radios = body.querySelectorAll('input[name="ck-plan"]');
    for (var i = 0; i < radios.length; i++) radios[i].addEventListener('change', function () {
      S.plan = this.value;
      var all = body.querySelectorAll('.ck-pl');
      for (var j = 0; j < all.length; j++) all[j].classList.toggle('on', all[j].querySelector('input').checked);
    });
    body.querySelector('#ck-open').addEventListener('click', function () { goStudio(true); });
    body.querySelector('#ck-pay').addEventListener('click', function () {
      if (busy) return;
      var btn = this, tier = S.plan;
      setErr('');
      setBusy(btn, true, 'Opening payment…');
      preloadRzp();
      payPlan(tier, ex.plan === tier, ex.onTrial).then(function (r) {
        if (!r.paid) {
          setBusy(btn, false);
          setErr('Payment not completed. You can pay whenever you’re ready.');
          step('payment_dismissed', { existing: true });
          return;
        }
        r.category = ex.onTrial ? 'Studio activation' : 'Studio upgrade';
        finish(r, false, tier);
      }).catch(function (e) {
        setBusy(btn, false);
        if (e.status === 401) { expired(); return; }
        setErr(e.message || 'Something went wrong. Please try again.');
        step('error', { at: 'plan_pay', error: String(e.message).slice(0, 100) });
      });
    });
  }

  // ── step 2: name + academy ────────────────────────────────────────────
  function renderDetails() {
    S.step = 'details'; progress(2); save();
    body.innerHTML = '<h3 id="ck-t">About you and your academy</h3>' +
      '<p class="sub">This goes on your studio, website and receipts. You can change it later.</p>' +
      summary() +
      '<div class="ck-err" role="alert"></div>' +
      '<label class="l" for="ck-nm">Your full name</label>' +
      '<div class="ck-in"><input id="ck-nm" type="text" autocomplete="name" maxlength="80" placeholder="e.g. Ritu Sharma" value="' + esc(S.name || '') + '"/></div>' +
      '<label class="l" for="ck-ac">Academy name</label>' +
      '<div class="ck-in"><input id="ck-ac" type="text" autocomplete="organization" maxlength="80" placeholder="e.g. Sharma Classes" value="' + esc(S.academy || '') + '"/></div>' +
      '<button type="button" class="ck-btn" id="ck-go">Continue</button>';
    bindPlansLink();
    var nm = body.querySelector('#ck-nm'), ac = body.querySelector('#ck-ac'), go = body.querySelector('#ck-go');
    [nm, ac].forEach(function (i) { i.addEventListener('keydown', function (e) { if (e.key === 'Enter') go.click(); }); i.addEventListener('input', function () { setErr(''); }); });
    go.addEventListener('click', function () {
      if (busy) return;
      var n = nm.value.trim(), a = ac.value.trim();
      if (n.length < 2) { setErr('Please enter your name.'); nm.focus(); return; }
      if (a.length < 2) { setErr('Please enter your academy name.'); ac.focus(); return; }
      S.name = n; S.academy = a; save();
      setBusy(go, true, 'Saving…');
      // Same fields studio writes on its identity + brand steps, in one patch.
      var patch = { director_name: n, name: a };
      if (VERTICAL) patch.vertical = VERTICAL;
      if (REF) patch.referral_code = REF;
      var at = attribution();
      if (Object.keys(at).length) patch.attribution = at;
      api('login/update', patch, 'Could not save your details.').then(function () {
        S.saved = true; save();
        step('details_saved');
        identify();
        // Meta CompleteRegistration: the new studio now has a name and an academy.
        var rid = eduId();
        if (S.isNew && rid && once('reg|' + rid)) {
          push('sign_up', {
            event_id: 'reg_' + rid, method: 'phone_otp', educator_id: rid, subject: VERTICAL || undefined,
            content_name: 'Studio created', status: 'registered', currency: 'INR', value: 0,
            user_data: { email: eduEmail(), phone: S.phone }, ac_attribution: attribution(), page: PAGE
          });
        }
        setBusy(go, false);
        renderPlan();
      }, function (e) {
        setBusy(go, false);
        if (e.status === 401) { expired(); return; }
        // studio does not block progress on a failed profile save, and neither do we:
        // the details are flushed again after payment.
        step('error', { at: 'details_save', error: String(e.message).slice(0, 100) });
        S.saved = false; save();
        renderPlan();
      });
    });
    setTimeout(function () { (nm.value ? ac : nm).focus(); }, 60);
  }

  // ── step 3: plan + payment ────────────────────────────────────────────
  function renderPlan() {
    S.step = 'plan'; progress(3); save();
    preloadRzp();
    var rows = ORDER.map(function (k) {
      var p = PLANS[k];
      return '<label class="ck-pl' + (S.plan === k ? ' on' : '') + '">' + (k === 'growth' ? '<span class="tg">Most popular</span>' : '') +
        '<input type="radio" name="ck-plan" value="' + k + '"' + (S.plan === k ? ' checked' : '') + '/>' +
        '<span><b>' + p.label + '</b><small>Keep ' + p.keep + ' of every sale · ' + p.meta + '</small></span>' +
        '<span class="p">' + rs(p.fee) + '<small>/yr</small></span></label>';
    }).join('');
    body.innerHTML = '<h3 id="ck-t">Choose your plan</h3>' +
      '<p class="sub">One yearly plan. Your studio opens the moment payment is confirmed.</p>' +
      '<div class="ck-err" role="alert"></div>' +
      '<div class="ck-plans" role="radiogroup" aria-label="Plan">' + rows + '</div>' +
      '<div class="ck-cp">' + (COUPON ? '' : '<button type="button" class="ck-link" id="ck-cpt">Have an activation code?</button>') +
      '<div class="ck-in" id="ck-cpw"' + (COUPON ? '' : ' hidden') + '><input id="ck-cp" type="text" autocomplete="off" maxlength="40" placeholder="Activation code" value="' + esc(COUPON) + '"/><button type="button" id="ck-cpa">Apply</button></div></div>' +
      '<div class="ck-tot"><span>Today</span><span id="ck-amt"></span></div>' +
      '<p class="ck-fine" id="ck-note">You’ll see the final amount, including any tax, on the payment screen before you pay.</p>' +
      '<button type="button" class="ck-btn" id="ck-pay">Continue to secure payment</button>' +
      (TRIAL_OK ? '<div class="ck-or">or</div><button type="button" class="ck-btn sec" id="ck-trial">Start 14-day free trial instead</button>' : '') +
      '<div class="ck-trust"><span>Razorpay: UPI, cards, netbanking</span><span>Upgrade any time, paid value credited</span></div>';
    var radios = body.querySelectorAll('input[name="ck-plan"]');
    for (var i = 0; i < radios.length; i++) radios[i].addEventListener('change', function () {
      S.plan = this.value; save();
      var all = body.querySelectorAll('.ck-pl');
      for (var j = 0; j < all.length; j++) all[j].classList.toggle('on', all[j].querySelector('input').checked);
      quote = null; paint();
      var c = body.querySelector('#ck-cp');
      if (c && c.value.trim()) applyCoupon(c.value.trim(), true);
    });
    var cpt = body.querySelector('#ck-cpt');
    if (cpt) cpt.addEventListener('click', function () { cpt.hidden = true; var w = body.querySelector('#ck-cpw'); w.hidden = false; w.querySelector('input').focus(); });
    var cpa = body.querySelector('#ck-cpa');
    cpa.addEventListener('click', function () { var v = body.querySelector('#ck-cp').value.trim(); if (v) applyCoupon(v); });
    body.querySelector('#ck-cp').addEventListener('keydown', function (e) { if (e.key === 'Enter') cpa.click(); });
    body.querySelector('#ck-pay').addEventListener('click', function () { if (!busy) launch(false, this); });
    var tb = body.querySelector('#ck-trial');
    if (tb) tb.addEventListener('click', function () { if (!busy) launch(true, this); });
    paint();
    if (COUPON) applyCoupon(COUPON, true);
  }
  function paint() {
    var el = body && body.querySelector('#ck-amt');
    if (!el) return;
    var p = PLANS[S.plan];
    if (quote && quote.tier === S.plan) {
      el.innerHTML = (quote.discount_paise ? '<s>' + rs(quote.fee_paise) + '</s>' : '') + '<b>' + rs(quote.payable_paise) + '</b>';
    } else {
      el.innerHTML = '<b>' + rs(p.fee) + '</b>';
    }
  }
  function applyCoupon(code, quiet) {
    var tier = S.plan;
    api('login/onboarding/coupon/check', { code: code, tier: tier }, 'Couldn’t check that code. Try again.').then(function (j) {
      var d = j.data || {};
      if (tier !== S.plan) return;
      quote = { code: d.code || code, label: d.label, fee_paise: d.fee_paise, discount_paise: d.discount_paise || 0, payable_paise: d.payable_paise, tier: tier };
      COUPON = quote.code;
      paint();
      setErr('Code applied' + (d.label ? ': ' + d.label : '') + '.', true);
      step('coupon_applied', { coupon: COUPON });
    }, function (e) {
      if (e.status === 401) { expired(); return; }
      quote = null; paint();
      if (!quiet || COUPON) setErr(e.message);
      COUPON = '';
    });
  }

  // studio's handleComplete(), step for step: claim → (trial | pay) → flush → conversions.
  function launch(trial, btn) {
    setErr('');
    setBusy(btn, true, trial ? 'Starting your trial…' : 'Confirming your plan…');
    var tier = trial ? 'starter' : S.plan;
    var paidResult = null, startedTrial = false;
    api('login/onboarding/claim', { tier: tier }, 'Couldn’t confirm your plan just now. Please try again.').then(function (j) {
      var claim = j.data;
      if (!claim) throw new Error('Couldn’t confirm your plan just now. Please try again.');
      if (!claim.must_pay) return 'open';
      if (trial) {
        if (!claim.trial_available) {
          var e = new Error('Your free trial has already been used. Choose a plan to open your studio.');
          e.keep = true;
          throw e;
        }
        return api('login/onboarding/trial', {}, 'Couldn’t start your free trial. Try again, or choose a plan.').then(function (t) {
          var d = t.data || {};
          if (!d.trial && !d.already_open) throw new Error('Couldn’t start your free trial. Try again, or choose a plan.');
          startedTrial = d.trial === true;
          return 'open';
        });
      }
      setBusy(btn, true, 'Opening payment…');
      return pay(tier, claim).then(function (r) {
        if (!r.paid) return 'dismissed';
        paidResult = r;
        return 'open';
      });
    }).then(function (res) {
      if (res === 'dismissed') {
        setBusy(btn, false);
        setErr('Payment not completed. Your details are saved — you can pay whenever you’re ready.');
        step('payment_dismissed');
        return;
      }
      finish(paidResult, startedTrial, tier);
    }).catch(function (e) {
      setBusy(btn, false);
      if (e.status === 401) { expired(); return; }
      setErr(e.message || 'Something went wrong. Please try again.');
      step('error', { at: trial ? 'trial' : 'pay', error: String(e.message).slice(0, 100) });
    });
  }

  var rzpLoading = null;
  function preloadRzp() {
    if (window.Razorpay) return Promise.resolve(true);
    if (!rzpLoading) {
      rzpLoading = new Promise(function (resolve) {
        var s = document.createElement('script');
        s.src = RZP_SRC; s.async = true;
        s.onload = function () { resolve(true); };
        s.onerror = function () { rzpLoading = null; resolve(false); };
        document.head.appendChild(s);
      });
    }
    return rzpLoading;
  }
  // New studio: studio's payOnboardingFee (order → Razorpay → verify).
  function pay(tier, claim) {
    var req = { tier: tier };
    if (COUPON) req.code = COUPON;
    return api('login/onboarding/pay/checkout', req, 'Couldn’t open the payment window. Please try again.').then(function (j) {
      var order = j.data || {};
      if (order.waived) return { paid: true, amountPaise: 0, waived: true };
      return openRazorpay(order, tier, claim.fee_paise, 'login/onboarding/pay/verify',
        function (d) { return !!d.paid; }, renderPlan,
        order.label ? order.label + ' plan · one year of studio' : 'Studio activation');
    });
  }

  // Studio that already exists (trial running, or a paid plan to upgrade or renew):
  // studio's own upgradeStudioPlan (institute/plan/checkout → Razorpay → institute/plan/verify).
  // The server prices it: full year for a trial conversion or renewal, credited difference
  // for an upgrade.
  function payPlan(tier, renew, onTrial) {
    return api('institute/plan/checkout/', { tier: tier, renew: !!renew }, 'Couldn’t open the payment window. Please try again.').then(function (j) {
      var order = j.data || {};
      var desc = onTrial ? (order.label || PLANS[tier].label) + ' — your first year'
        : renew ? 'Renew ' + (order.label || PLANS[tier].label) + ' — one more year'
        : 'Upgrade to ' + (order.label || PLANS[tier].label) + ' — one year';
      return openRazorpay(order, tier, PLANS[tier].fee, 'institute/plan/verify/',
        function (d) { return !!d.plan; }, function () { renderExisting(EXISTING); }, desc);
    });
  }

  function openRazorpay(order, tier, fallbackPaise, verifyPath, verified, onFail, description) {
    if (!order.order_id || !order.key_id) return Promise.reject(new Error('Couldn’t open the payment window. Please try again.'));
    return preloadRzp().then(function (ok) {
      if (!ok || !window.Razorpay) throw new Error('Couldn’t load the payment window. Check your connection and try again.');
      var value = (order.amount || fallbackPaise || 0) / 100;
      push('add_payment_info', {
        event_id: 'api_' + order.order_id, value: value, currency: 'INR',
        content_ids: [tier], content_name: PLANS[tier].label + ' plan', content_type: 'product', num_items: 1,
        page: PAGE, vertical: VERTICAL || undefined
      });
      step('payment_open', { value: value, existing: !!EXISTING });
      return new Promise(function (resolve, reject) {
        var rz = new window.Razorpay({
          key: order.key_id,
          order_id: order.order_id,
          amount: order.amount,
          currency: order.currency || 'INR',
          name: order.label ? 'AllCoaching · ' + order.label + ' plan' : 'AllCoaching Studio',
          description: description,
          prefill: { name: S.name || undefined, contact: S.phone || undefined, email: eduEmail() },
          theme: { color: '#2B44FF' },
          handler: function (resp) {
            showWait('Confirming your payment…', 'Please don’t close this window.');
            var stuck = 'We received your payment but could not confirm it yet. Please contact us on WhatsApp with your payment id ' + resp.razorpay_payment_id + '.';
            api(verifyPath, {
              razorpay_order_id: resp.razorpay_order_id,
              razorpay_payment_id: resp.razorpay_payment_id,
              razorpay_signature: resp.razorpay_signature
            }, stuck).then(function (v) {
              if (!verified(v.data || {})) { onFail(); reject(new Error(stuck)); return; }
              resolve({ paid: true, paymentId: resp.razorpay_payment_id, orderId: resp.razorpay_order_id, amountPaise: order.amount, tier: order.tier || (v.data && v.data.plan) || tier, label: order.label });
            }, function (e) { onFail(); reject(e); });
          },
          modal: { ondismiss: function () { resolve({ paid: false }); }, confirm_close: true }
        });
        rz.on && rz.on('payment.failed', function (r) {
          step('error', { at: 'razorpay', error: (r && r.error && r.error.description || 'payment failed').slice(0, 100) });
        });
        rz.open();
      });
    });
  }

  function showWait(title, sub) {
    progress(3);
    body.innerHTML = '<div class="ck-wait"><div class="ck-spin" aria-hidden="true"></div><h3 id="ck-t">' + esc(title) + '</h3><p class="sub">' + esc(sub || '') + '</p></div>';
  }

  function finish(paid, startedTrial, tier) {
    busy = true;
    showWait('Opening your studio…', '');
    // Final profile flush, as studio does after payment (best effort). Never for a studio
    // that already existed: its name and subject are the educator's, not this page's.
    var flush = {};
    if (!EXISTING && S.saved !== undefined) {
      if (S.name) flush.director_name = S.name;
      if (S.academy) flush.name = S.academy;
      if (VERTICAL) flush.vertical = VERTICAL;
    }
    var flushed = Object.keys(flush).length ? api('login/update', flush).catch(function () {}) : Promise.resolve();
    flushed.then(function () {
      identify();
      var id = eduId(), email = eduEmail();
      var attr = attribution();
      var userData = { email: email, phone: S.phone };
      var last = null;

      // Purchase — exactly studio's purchase_complete. event_id = Razorpay payment id,
      // the same id the server-side CAPI Purchase sends, so Meta counts it once.
      if (paid && !paid.waived) {
        var txn = paid.paymentId || paid.orderId;
        if (txn && once('purchase|' + txn)) {
          last = ['purchase_complete', {
            transaction_id: txn,
            event_id: txn,
            value: (paid.amountPaise || 0) / 100,
            currency: 'INR',
            content_category: paid.category || 'Studio activation',
            content_name: PLANS[paid.tier] ? PLANS[paid.tier].label + ' plan' : 'Studio plan',
            content_ids: [PLANS[paid.tier] ? paid.tier : 'plan'],
            content_type: 'product',
            num_items: 1,
            external_id: id,
            user_email: email,
            user_phone: S.phone,
            page: PAGE,
            page_variant: VARIANT,
            vertical: VERTICAL || undefined,
            ac_attribution: attr
          }];
        }
      }

      if (last) push(last[0], last[1]);   // purchase_complete leads, as in studio
      last = null;
      // Lead and CompleteRegistration already went out at OTP and at the details step.
      if (S.isNew && id && once('signup|' + id)) {
        push('studio_signup_complete', {
          educator_id: id, plan: paid ? (paid.tier || tier) : tier, subject: VERTICAL || undefined,
          trial: startedTrial, user_data: userData, event_id: uuid(), ac_attribution: attr, page: PAGE
        });
      }
      // Meta StartTrial: valued at zero, with the plan it converts to as predicted_ltv.
      if (startedTrial && id && once('trial|' + id)) {
        push('start_trial', {
          event_id: 'trial_' + id, educator_id: id, plan: 'starter', value: 0, currency: 'INR',
          predicted_ltv: PLANS.starter.fee / 100, content_ids: ['starter'], content_name: 'Starter plan trial',
          subject: VERTICAL || undefined, user_data: userData, ac_attribution: attr, page: PAGE
        });
      }

      // GTM fires tags in dataLayer order, so a callback on this LAST push runs only after
      // the conversion tags above have fired. The redirect waits for it.
      pushThen('lp_checkout', { step: 'done', page: PAGE, page_variant: VARIANT, vertical: VERTICAL || undefined, plan: paid ? (paid.tier || tier) : tier, trial: startedTrial, paid: !!paid }, function () {
        busy = false;
        renderDone(startedTrial, paid);
      });
    });
  }

  function renderDone(trial, paid) {
    progress(3);
    var realPay = paid && paid.paid && !paid.waived;
    var title = trial ? 'Your 14-day trial has started'
      : realPay ? 'Payment received. Your studio is open.'
      : 'Your studio is open';
    var sub = trial ? 'Nothing was charged. Taking you to your studio to add your first course.'
      : EXISTING ? 'Taking you to your studio.'
      : 'Taking you to your studio to add your first course.';
    body.innerHTML = '<div class="ck-done"><div class="ck-tick"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg></div>' +
      '<h3 id="ck-t">' + title + '</h3><p class="sub">' + sub + '</p>' +
      (paid && paid.paymentId ? '<p class="ck-fine">Payment id: ' + esc(paid.paymentId) + '</p>' : '') +
      '<button type="button" class="ck-btn" id="ck-go">Open my studio</button></div>';
    body.querySelector('#ck-go').addEventListener('click', function () { goStudio(true); });
    setTimeout(function () { goStudio(true); }, 2200);
  }

  var leaving = false;
  function goStudio(done) {
    if (leaving) return;
    leaving = true;
    var auth = S.auth;
    clearSaved();
    var ready = !!window.AC_HANDOFF_READY;
    var url;
    if (ready && auth && auth.key) {
      var env = { key: auth.key, created: auth.created, user: auth.user, organizations: auth.organizations, onboardingCompleted: !!done, launched: true };
      url = STUDIO + 'handoff#auth=' + b64url(JSON.stringify(env));
    } else {
      // Studio can't take the session yet: sign in there with the same number.
      url = STUDIO + 'login';
    }
    location.href = url;
  }

  function expired() {
    S.token = null; S.auth = null; S.step = 'phone'; EXISTING = null; save();
    renderPhone();
    setErr('Your session expired. Please verify your number again.');
  }

  // ── live prices (falls back to the built-in list) ─────────────────────
  var pricingLoaded = false;
  function loadPricing() {
    if (pricingLoaded) return;
    pricingLoaded = true;
    api('login/onboarding/pricing').then(function (j) {
      var d = j.data || {};
      (d.plans || []).forEach(function (p) {
        if (!PLANS[p.key]) return;
        if (p.signup_paise || p.fee_paise) PLANS[p.key].fee = p.signup_paise || p.fee_paise;
      });
      if (S.step === 'plan') paint();
      var sum = body && body.querySelector('.ck-sum span');
      if (sum) sum.innerHTML = '<b>' + PLANS[S.plan].label + ' plan</b> · ' + rs(PLANS[S.plan].fee) + '/year';
    }, function () { pricingLoaded = false; });
  }

  // ── studio handoff readiness probe ────────────────────────────────────
  function probeHandoff() {
    var s = document.createElement('script');
    s.src = HANDOFF_PROBE + '?t=' + Math.floor(Date.now() / 3.6e6);
    s.async = true;
    s.onerror = function () {};
    document.head.appendChild(s);
  }

  // ── wire up ───────────────────────────────────────────────────────────
  function bind() {
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('[data-checkout]');
      if (!a) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
      e.preventDefault();
      open(a.getAttribute('data-plan'), a.getAttribute('data-where'));
    });
    // Resume after a refresh mid-checkout (e.g. the OTP SMS took the educator away).
    if (S.token && (S.step === 'details' || S.step === 'plan') && Q.get('checkout') !== '0') {
      open(S.plan, 'resume');
    } else if (Q.get('checkout') === '1') {
      open(S.plan, 'url');
    }
  }
  probeHandoff();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bind); else bind();

  window.ACCheckout = { open: open, close: close };
})();
