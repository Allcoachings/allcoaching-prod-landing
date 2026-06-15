/*!
 * AllCoaching — client-side conversion-tracking layer (marketing site: allcoaching.in)
 * --------------------------------------------------------------------------------------
 * Pairs with GTM container GTM-T3KFKD3G (already installed on every page).
 * This file does ONLY the things that belong on the marketing site:
 *   1. Capture ad click-IDs (gclid/fbclid/wbraid/gbraid) + utm_* from the URL and
 *      persist them in a cookie scoped to the ROOT domain (.allcoaching.in) so the
 *      studio sub-domain can read them  ->  fixes the "all conversions look direct" risk.
 *   2. Decorate every studio.allcoaching.in link with those click-IDs so they survive
 *      the cross-domain hop even before GA4's _gl linker is configured in GTM (belt &
 *      braces; the GA linker, once enabled in GTM, adds _gl on top of this).
 *   3. Push the marketing-funnel dataLayer events GTM listens for:
 *        cta_signup_click, contact_click, view_pricing.
 *   4. Expose window.acGenerateUuid() (RFC-4122) for event_id generation/dedup.
 *
 * NOT here (by design — different surface): sign_up / start_trial / first_sale fire on
 * studio.allcoaching.in; GA4/Ads/Meta tag config lives in the GTM console; Meta CAPI /
 * offline-import are server-side. See the implementation report for those steps.
 *
 * No PII is read or sent here. No raw email/phone is touched. Hashing for Enhanced
 * Conversions / CAPI happens in the tag layer (GTM) or server, never in this file.
 */
(function () {
  'use strict';

  var ROOT_DOMAIN = '.allcoaching.in';
  // Click-IDs + campaign params worth preserving across the cross-domain hop.
  var ATTR_PARAMS = ['gclid', 'gbraid', 'wbraid', 'fbclid', 'msclkid',
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  var ATTR_COOKIE = 'ac_attribution';
  var FIRST_TOUCH_COOKIE = 'ac_first_touch';
  var COOKIE_DAYS = 90;

  window.dataLayer = window.dataLayer || [];
  var DL = window.dataLayer;

  /* ---------- cookie helpers (root-domain scoped, so studio.* can read) ---------- */
  function setCookie(name, value, days) {
    var exp = new Date(Date.now() + days * 864e5).toUTCString();
    var secure = location.protocol === 'https:' ? ';Secure' : '';
    document.cookie = name + '=' + encodeURIComponent(value) +
      ';expires=' + exp + ';path=/;domain=' + ROOT_DOMAIN + ';SameSite=Lax' + secure;
  }
  function getCookie(name) {
    var m = document.cookie.match('(?:^|;\\s*)' + name + '=([^;]*)');
    return m ? decodeURIComponent(m[1]) : '';
  }
  function readAttribution() {
    try { return JSON.parse(getCookie(ATTR_COOKIE) || '{}'); } catch (e) { return {}; }
  }

  /* ---------- RFC-4122 uuid (event_id for browser<->server dedup) ---------- */
  function generateUuid() {
    if (window.crypto && typeof crypto.randomUUID === 'function') return crypto.randomUUID();
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0, v = c === 'x' ? r : (r & 0x3) | 0x8;
      return v.toString(16);
    });
  }
  window.acGenerateUuid = generateUuid;

  /* ---------- 1. capture click-IDs / utm from URL -> cookie ---------- */
  function captureAttribution() {
    var qs;
    try { qs = new URLSearchParams(location.search); } catch (e) { return; }
    var found = {};
    ATTR_PARAMS.forEach(function (k) {
      var v = qs.get(k);
      if (v) found[k] = v;
    });
    if (!Object.keys(found).length) return;

    // Last-click wins for the live attribution cookie (new click-IDs override old).
    var merged = readAttribution();
    Object.keys(found).forEach(function (k) { merged[k] = found[k]; });
    merged._ts = Date.now();
    setCookie(ATTR_COOKIE, JSON.stringify(merged), COOKIE_DAYS);

    // First-touch is kept immutable for later offline-import / multi-touch analysis.
    if (!getCookie(FIRST_TOUCH_COOKIE)) {
      setCookie(FIRST_TOUCH_COOKIE,
        JSON.stringify({ p: found, lp: location.pathname, ts: Date.now() }), COOKIE_DAYS);
    }
  }

  /* ---------- 2. decorate studio links so click-IDs survive the hop ---------- */
  function decorateStudioLinks(root) {
    var attr = readAttribution();
    var keep = {};
    ATTR_PARAMS.forEach(function (k) { if (attr[k]) keep[k] = attr[k]; });
    if (!Object.keys(keep).length) return;
    var links = (root || document).querySelectorAll('a[href*="studio.allcoaching.in"]');
    Array.prototype.forEach.call(links, function (a) {
      try {
        var u = new URL(a.href);
        Object.keys(keep).forEach(function (k) {
          if (!u.searchParams.has(k)) u.searchParams.set(k, keep[k]);
        });
        a.href = u.toString();
      } catch (e) { /* skip malformed href */ }
    });
  }

  /* ---------- 3. dataLayer funnel events ---------- */
  function push(o) { DL.push(o); }

  // Coarse CTA location: hero | pricing | sticky | header | footer | body
  function ctaLocation(el) {
    var tagged = el.closest('[data-cta-location]');
    if (tagged) return tagged.getAttribute('data-cta-location');
    if (el.closest('[class*="sticky"],[class*="stk"]')) return 'sticky';
    if (el.closest('header,nav,[class*="nav"]')) return 'header';
    if (el.closest('footer,[class*="foot"]')) return 'footer';
    if (el.closest('[id*="pricing"],[class*="pricing"],[class*="plan"],[class*="earn"]')) return 'pricing';
    if (el.closest('[class*="hero"],[class*="mast"],[class*="lede"]')) return 'hero';
    return 'body';
  }
  function isSignupIntent(a) {
    // A studio link that is NOT an explicit "log in" link counts as signup intent.
    var cls = (a.className || '') + ' ' + (a.getAttribute('aria-label') || '');
    var txt = (a.textContent || '').toLowerCase();
    if (/log\s*in|login|sign\s*in/.test(cls.toLowerCase()) || /log\s*in|sign\s*in/.test(txt)) return false;
    return true;
  }

  function onClick(e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';

    if (href.indexOf('studio.allcoaching.in') > -1 && isSignupIntent(a)) {
      push({
        event: 'cta_signup_click',
        cta_location: ctaLocation(a),
        cta_text: (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80)
      });
    }

    var method = '';
    if (/919889977262|wa\.me|whatsapp/i.test(href)) method = 'whatsapp';
    else if (href.indexOf('tel:') === 0) method = 'phone';
    else if (href.indexOf('mailto:') === 0) method = 'email';
    if (method) push({ event: 'contact_click', method: method });
  }

  // view_pricing — fire once when the pricing/earnings section first becomes visible.
  function watchPricing() {
    var sec = document.querySelector('#pricing, [id*="pricing"], [class*="pricing"], #earnings, [class*="earning"]');
    if (!sec || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
          push({ event: 'view_pricing', section: 'pricing' });
          io.disconnect();
          return;
        }
      }
    }, { threshold: 0.4 });
    io.observe(sec);
  }

  /* ---------- init ---------- */
  function init() {
    captureAttribution();
    decorateStudioLinks(document);
    watchPricing();
    document.addEventListener('click', onClick, true);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
