/*!
 * Plans for /landing pages (owner-approved pricing, 28 Oct 2026):
 *   <div data-plans></div>        → filled with one card per plan (CTA opens the checkout)
 *   <span data-from></span>       → "₹6,999" (Starter, per year)
 *   <span data-keep-range></span> → "100% on Growth and Pro (90% on Starter)"
 * The plans are static on purpose. The pricing API (login/onboarding/pricing) used to drive these
 * cards and labelled every price "/year" with a commission (the old per-sale fee plans); Growth and
 * Pro are now monthly with 0% commission, so live backend figures are no longer shown here. The
 * checkout in the studio still shows the live price before the educator pays.
 */
(function () {
  'use strict';
  var PLANS = [
    { key: 'starter', label: 'Starter', price: '₹6,999', per: '/year + GST', keep: 90,
      pts: ['Keep <b>90%</b> of every sale (10% per sale)', '512 GB video storage · 100 GB streaming a month', 'Your own Android app'] },
    { key: 'growth', label: 'Growth', price: '₹7,999', per: '/month + GST', keep: 100,
      pts: ['<b>0% commission</b> · keep 100% of every sale', '1 TB video storage · 1 TB streaming a month', 'Your own Android app', 'Or ₹79,990 a year (2 months free)'] },
    { key: 'pro', label: 'Pro', price: '₹14,999', per: '/month + GST', keep: 100,
      pts: ['<b>0% commission</b> · keep 100% of every sale', '2 TB video storage · 2 TB streaming a month · 4K', 'Your own Android &amp; iOS app', 'Premium theme', 'Or ₹1,49,990 a year (2 months free)'] }
  ];
  // On every plan.
  var ALL = ['Unlimited live classes &amp; YouTube videos', 'Domain, themes, Zoom, Razorpay, Pixel &amp; GTM', 'No launch fee · no sales limit'];

  function card(p, featured) {
    var tag = p.key === 'growth' ? '<span class="tag">Most popular</span>' : p.key === 'pro' ? '<span class="tag bv">Best value · Recommended</span>' : '';
    var pts = p.pts.concat(ALL);
    return '<div class="plan' + (featured ? ' ft' : '') + '">' + tag +
      '<span class="pn">' + p.label + '</span>' +
      '<div class="pp"><b>' + p.price + '</b><span>' + p.per + '</span></div>' +
      '<ul>' + pts.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' +
      '<a class="btn' + (featured ? '' : ' ghost') + '" href="https://studio.allcoaching.in/" data-checkout data-plan="' + p.key + '" data-ev="ob_cta_click" data-where="plan-' + p.key + '">Start free with ' + p.label + '</a></div>';
  }
  function render() {
    document.querySelectorAll('[data-from]').forEach(function (el) { el.textContent = '₹6,999'; });
    document.querySelectorAll('[data-keep-range]').forEach(function (el) { el.textContent = '100% on Growth and Pro (90% on Starter)'; });
    document.querySelectorAll('[data-plans]').forEach(function (box) {
      var feat = box.getAttribute('data-featured') || 'growth';
      box.innerHTML = PLANS.map(function (p) { return card(p, p.key === feat); }).join('');
      box.classList.add('ready');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render); else render();
})();
