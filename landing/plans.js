/*!
 * Plans for /landing pages. Figures copied from the studio's plan picker
 * (.claude/scripts/x_plans.py, owner 22 Nov 2026; marketing leads with yearly, owner 25 Nov 2026):
 *   <div data-plans></div>        → a Yearly | Monthly toggle (opens on Yearly) and one card per plan
 *   <span data-from></span>       → "₹3,999" (Starter, per month)
 *   <span data-keep-range></span> → "100% on monthly plans (90–95% on yearly)"
 * Yearly cards open the on-page checkout (data-plan="<key>"), which sells the three yearly plans
 * and offers the 7-day trial. Monthly cards carry data-plan="<key>_m", which checkout.js leaves as a
 * plain link to studio, where monthly autopay is bought.
 * Static on purpose; the studio checkout still shows the live price before the educator pays.
 */
(function () {
  'use strict';
  var YEARLY = [
    { key: 'starter', label: 'Starter', price: '₹6,999', per: '/year + GST', fee: '+ 10% per sale', keep: '90%', storage: '512 GB', video: '1080p', live: 5, seats: '1 team seat', pages: 'any 6 landing pages', ios: false },
    { key: 'growth', label: 'Growth', price: '₹12,999', per: '/year + GST', fee: '+ 7.5% per sale', keep: '92.5%', storage: '1 TB', video: '1080p', live: 10, seats: '3 team seats', pages: 'any 12 landing pages', ios: true },
    { key: 'pro', label: 'Pro', price: '₹24,999', per: '/year + GST', fee: '+ 5% per sale', keep: '95%', storage: '3 TB', video: '4K', live: 15, seats: '5 team seats', pages: 'every landing page', ios: true }
  ];
  var MONTHLY = [
    { key: 'starter', label: 'Starter', price: '₹3,999', per: '/month + GST', fee: '0% commission', keep: '100%', storage: '512 GB', video: '1080p', live: 20, seats: '5 team seats', pages: 'any 6 landing pages', ios: false },
    { key: 'growth', label: 'Growth', price: '₹5,999', per: '/month + GST', fee: '0% commission', keep: '100%', storage: '1 TB', video: '1080p', live: 50, seats: '10 team seats', pages: 'any 12 landing pages', ios: true },
    { key: 'pro', label: 'Pro', price: '₹7,999', per: '/month + GST', fee: '0% commission', keep: '100%', storage: '2 TB', video: '4K', live: 90, seats: '20 team seats', pages: 'every landing page', ios: true }
  ];
  // On every plan.
  var ALL = ['Unlimited YouTube video &amp; live classes on YouTube Live or Zoom', 'Own domain, Zoom, Razorpay, Pixel &amp; GTM', 'Classic theme included', 'No setup fee · no sales limit'];

  var CSS = '.ptog{display:flex;justify-content:center;gap:4px;margin:28px auto 0;padding:4px;border-radius:99px;background:rgba(20,22,31,.06);width:max-content;max-width:100%}' +
    '.ptog button{font:inherit;font-size:14px;font-weight:600;border:0;background:transparent;color:inherit;padding:8px 18px;border-radius:99px;cursor:pointer}' +
    '.ptog button[aria-pressed="true"]{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.12);color:#14161F}' +
    '.ptog button:focus-visible{outline:2px solid #2B44FF;outline-offset:2px}' +
    '.pfee{display:block;font-size:13px;font-weight:600;margin-top:2px;opacity:.8}';

  function card(p, mode, featured) {
    var tag = p.key === 'growth' ? '<span class="tag">Most popular</span>' : p.key === 'pro' ? '<span class="tag bv">Best value · Recommended</span>' : '';
    var keepLine = mode === 'm'
      ? '<span><b>0% commission</b> · keep 100% of every sale</span>'
      : '<span>Keep <b>' + p.keep + '</b> of every sale</span>';
    var pts = [keepLine,
      p.storage + ' video storage · ' + p.video,
      p.live + ' hours a month of built-in live classroom',
      p.seats + ' · ' + p.pages,
      p.ios ? 'Your own Android &amp; iOS app (iOS after 30 days)' : 'Your own Android app'].concat(ALL);
    var plan = mode === 'm' ? p.key + '_m' : p.key;
    var where = 'plan-' + p.key + (mode === 'm' ? '-monthly' : '-yearly');
    return '<div class="plan' + (featured ? ' ft' : '') + '">' + tag +
      '<span class="pn">' + p.label + '</span>' +
      '<div class="pp"><b>' + p.price + '</b><span>' + p.per + '</span></div>' +
      '<span class="pfee">' + p.fee + '</span>' +
      '<ul>' + pts.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' +
      '<a class="btn' + (featured ? '' : ' ghost') + '" href="https://studio.allcoaching.in/" data-checkout data-plan="' + plan + '" data-ev="ob_cta_click" data-where="' + where + '">Start 7-day free trial</a></div>';
  }
  function fill(box, mode) {
    var feat = box.getAttribute('data-featured') || 'growth';
    var list = mode === 'm' ? MONTHLY : YEARLY;
    box.querySelector('.pcards').innerHTML = list.map(function (p) { return card(p, mode, p.key === feat); }).join('');
    box.querySelectorAll('.ptog button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === mode)); });
  }
  function render() {
    if (!document.getElementById('ptog-css')) {
      var st = document.createElement('style'); st.id = 'ptog-css'; st.textContent = CSS; document.head.appendChild(st);
    }
    document.querySelectorAll('[data-from]').forEach(function (el) { el.textContent = '₹3,999'; });
    document.querySelectorAll('[data-keep-range]').forEach(function (el) { el.textContent = '100% on monthly plans (90–95% on yearly)'; });
    document.querySelectorAll('[data-plans]').forEach(function (box, i) {
      // The toggle sits above the grid, so the box keeps its .plans grid class only on the cards.
      var wrap = document.createElement('div');
      wrap.innerHTML = '<div class="ptog" role="group" aria-label="Billing"><button type="button" id="ptog-y-' + i + '" data-mode="y">Yearly</button><button type="button" id="ptog-m-' + i + '" data-mode="m">Monthly · 0% commission</button></div>';
      box.parentNode.insertBefore(wrap.firstChild, box);
      box.innerHTML = '<div class="pcards" style="display:contents"></div>';
      var tog = box.previousSibling;
      tog.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return;
        fill(box, b.getAttribute('data-mode'));
        tog.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      });
      fill(box, 'y');
      tog.querySelector('[data-mode="y"]').setAttribute('aria-pressed', 'true');
      tog.querySelector('[data-mode="m"]').setAttribute('aria-pressed', 'false');
      box.classList.add('ready');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render); else render();
})();
