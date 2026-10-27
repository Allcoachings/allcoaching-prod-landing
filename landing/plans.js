/*!
 * Live plans for /landing pages. Plans change on the server, so no page hardcodes a price:
 *   <div data-plans></div>        → filled with one card per plan (CTA opens the checkout)
 *   <span data-from></span>       → "₹6,999" (cheapest plan today)
 *   <span data-keep-range></span> → "90–100%"
 * Reads GET login/onboarding/pricing through the same-origin proxy (/acapi/proxy.php).
 * If the call fails, plan cards are replaced by one button that opens the checkout, where the
 * educator still sees live prices.
 */
(function () {
  'use strict';
  var URL_ = '/acapi/proxy.php?p=' + encodeURIComponent('login/onboarding/pricing');
  var KEY = 'ac_plans_v1';
  var ORDER = ['starter', 'growth', 'pro'];

  function rs(paise) { return '₹' + Math.round(paise / 100).toLocaleString('en-IN'); }
  function gb(b) { var g = b / 1073741824; return g >= 1024 ? (Math.round(g / 102.4) / 10) + ' TB' : Math.round(g) + ' GB'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function cached() {
    try { var c = JSON.parse(sessionStorage.getItem(KEY) || 'null'); if (c && Date.now() - c.t < 6e5) return c.plans; } catch (e) {}
    return null;
  }
  function load() {
    var c = cached();
    if (c) return Promise.resolve(c);
    return fetch(URL_, { headers: { Accept: 'application/json' }, cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        var plans = ((j && j.data && j.data.plans) || []).filter(function (p) { return p && p.key; });
        plans.sort(function (a, b) { return ORDER.indexOf(a.key) - ORDER.indexOf(b.key); });
        if (!plans.length) throw new Error('no plans');
        try { sessionStorage.setItem(KEY, JSON.stringify({ t: Date.now(), plans: plans })); } catch (e) {}
        return plans;
      });
  }
  function fee(p) { return p.signup_paise || p.fee_paise || 0; }
  function card(p, featured) {
    var keep = typeof p.commission_pct === 'number' ? (100 - p.commission_pct) : null;
    var pts = [];
    if (keep != null) pts.push('Keep <b>' + keep + '%</b> of every sale');
    if (p.storage_bytes) pts.push(gb(p.storage_bytes) + ' storage · ' + (/4k/i.test(p.video_max || '') ? '4K' : esc(p.video_max || '1080p')));
    if (p.premium_template) pts.push('Premium theme (₹10,000 value)');
    // On every plan (pricing truth 2026-10-20).
    pts.push('Unlimited live classes &amp; videos', p.key === 'pro' ? 'Your own Android &amp; iOS app' : 'Your own Android app', 'Domain, themes, Zoom, Razorpay, Pixel &amp; GTM');
    var tag = featured ? '<span class="tag">Most popular</span>' : p.key === 'pro' ? '<span class="tag bv">Best value</span>' : '';
    return '<div class="plan' + (featured ? ' ft' : '') + '">' + tag +
      '<span class="pn">' + esc(p.label || p.key) + '</span>' +
      '<div class="pp"><b>' + rs(fee(p)) + '</b><span>/year + GST</span></div>' +
      '<ul>' + pts.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' +
      '<a class="btn' + (featured ? '' : ' ghost') + '" href="https://studio.allcoaching.in/" data-checkout data-plan="' + esc(p.key) + '" data-ev="ob_cta_click" data-where="plan-' + esc(p.key) + '">Choose ' + esc(p.label || p.key) + '</a></div>';
  }
  function render(plans) {
    var min = Math.min.apply(null, plans.map(fee));
    var keeps = plans.filter(function (p) { return typeof p.commission_pct === 'number'; }).map(function (p) { return 100 - p.commission_pct; });
    document.querySelectorAll('[data-from]').forEach(function (el) { el.textContent = rs(min); });
    if (keeps.length) document.querySelectorAll('[data-keep-range]').forEach(function (el) {
      var lo = Math.min.apply(null, keeps), hi = Math.max.apply(null, keeps);
      el.textContent = lo === hi ? lo + '%' : lo + '–' + hi + '%';
    });
    document.querySelectorAll('[data-plans]').forEach(function (box) {
      var feat = box.getAttribute('data-featured') || 'growth';
      box.innerHTML = plans.map(function (p) { return card(p, p.key === feat); }).join('');
      box.classList.add('ready');
    });
  }
  function fallback() {
    document.querySelectorAll('[data-from-wrap]').forEach(function (el) { el.style.display = 'none'; });
    document.querySelectorAll('[data-plans]').forEach(function (box) {
      box.innerHTML = '<a class="btn" href="https://studio.allcoaching.in/" data-checkout data-ev="ob_cta_click" data-where="plans">See plans and start</a>';
      box.classList.add('ready', 'fallback');
    });
  }
  function go() { load().then(render, fallback); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();
