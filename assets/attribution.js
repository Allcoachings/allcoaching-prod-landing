/* AllCoaching ad attribution — keeps ad click IDs and UTMs from the landing URL
   and passes them to studio.allcoaching.in so sign-ups and purchases can be
   matched to the ad that brought the educator.

   - Reads utm_*, gclid, gbraid, wbraid, fbclid, twclid, msclkid from the URL.
   - Stores first touch and last touch in a 90-day cookie on .allcoaching.in
     (`ac_attr`), readable by the studio on the same parent domain.
   - Sets `_fbc` (Meta click ID format) when an fbclid arrives, so the studio
     and the Conversions API can send it even before the pixel loads.
   - Appends the last-touch params to every studio.allcoaching.in link.
   - Pushes them to dataLayer as `ac_attribution` for GTM. */
(function () {
  var KEYS = /^(utm_[a-z_]+|gclid|gbraid|wbraid|fbclid|twclid|msclkid)$/;
  var DOMAIN = /allcoaching\.in$/.test(location.hostname) ? '; domain=.allcoaching.in' : '';
  var MAX = 60 * 60 * 24 * 90;

  function readCookie(name) {
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }
  function writeCookie(name, value) {
    document.cookie = name + '=' + encodeURIComponent(value) + '; path=/; max-age=' + MAX + DOMAIN + '; SameSite=Lax' + (location.protocol === 'https:' ? '; Secure' : '');
  }

  var now = {}, has = false;
  try {
    new URLSearchParams(location.search).forEach(function (v, k) {
      if (KEYS.test(k) && v) { now[k] = v.slice(0, 200); has = true; }
    });
  } catch (e) {}

  var store = {};
  try { store = JSON.parse(readCookie('ac_attr') || '{}') || {}; } catch (e) { store = {}; }
  if (has) {
    now.ts = Date.now();
    now.lp = location.pathname;
    if (document.referrer) now.ref = document.referrer.slice(0, 200);
    if (!store.first) store.first = now;
    store.last = now;
    try { writeCookie('ac_attr', JSON.stringify(store)); } catch (e) {}
    if (now.fbclid && !readCookie('_fbc')) writeCookie('_fbc', 'fb.1.' + now.ts + '.' + now.fbclid);
  }

  var last = store.last || {};
  var qs = new URLSearchParams();
  Object.keys(last).forEach(function (k) { if (KEYS.test(k)) qs.set(k, last[k]); });
  var q = qs.toString();

  var dl = window.dataLayer = window.dataLayer || [];
  if (q) dl.push({ event: 'ac_attribution', ac_first: store.first || null, ac_last: last });

  function tag() {
    if (!q) return;
    var links = document.querySelectorAll('a[href*="studio.allcoaching.in"]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (a.getAttribute('data-attr') === '1') continue;
      try {
        var u = new URL(a.href);
        qs.forEach(function (v, k) { if (!u.searchParams.has(k)) u.searchParams.set(k, v); });
        a.href = u.toString();
        a.setAttribute('data-attr', '1');
      } catch (e) {}
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tag); else tag();
})();
