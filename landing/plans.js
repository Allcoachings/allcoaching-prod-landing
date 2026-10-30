/*!
 * Plans for /landing pages (the studio's live pricing, owner 29 Oct 2026):
 *   <div data-plans></div>        → filled with one card per plan (CTA opens the checkout)
 *   <span data-from></span>       → "₹3,999" (Starter, per month)
 *   <span data-keep-range></span> → "100% on monthly plans (90–95% on yearly)"
 * Same three plans, two ways to pay: monthly at 0% commission (card price; the button carries
 * data-plan="<key>_m", which checkout.js leaves as a plain link to studio, where monthly autopay is
 * bought), or yearly for a lower fixed fee plus a small fee per sale (the "Or pay yearly" link opens
 * the on-page checkout, which sells the three yearly plans).
 * The plans are static on purpose; the checkout in the studio still shows the live price
 * before the educator pays.
 */
(function () {
  'use strict';
  var PLANS = [
    { key: 'starter', label: 'Starter', price: '₹3,999', per: '/month + GST', keep: 100,
      pts: ['<span><b>0% commission</b> · keep 100% of every sale</span>', '512 GB video storage · 512 GB streaming a month', '20 hours a month of built-in live classroom', '3 team seats · any 6 landing pages · any 2 premium themes', 'Your own Android app'], yr: '₹6,999 a year + 10% per sale' },
    { key: 'growth', label: 'Growth', price: '₹5,999', per: '/month + GST', keep: 100,
      pts: ['<span><b>0% commission</b> · keep 100% of every sale</span>', '1 TB video storage · 1 TB streaming a month', '50 hours a month of built-in live classroom', '5 team seats · any 12 landing pages · any 5 premium themes', 'Your own Android app'], yr: '₹12,999 a year + 7.5% per sale' },
    { key: 'pro', label: 'Pro', price: '₹7,999', per: '/month + GST', keep: 100,
      pts: ['<span><b>0% commission</b> · keep 100% of every sale</span>', '2 TB video storage · 2 TB streaming a month · 4K', '90 hours a month of built-in live classroom', '7 team seats · all 16 landing pages · all premium themes', 'Your own Android &amp; iOS app'], yr: '₹24,999 a year + 5% per sale (3 TB, premium theme)' }
  ];
  // On every plan.
  var ALL = ['Unlimited YouTube video &amp; live classes on YouTube Live or Zoom', 'Own domain, Zoom, Razorpay, Pixel &amp; GTM', 'No setup fee · no sales limit'];

  function card(p, featured) {
    var tag = p.key === 'growth' ? '<span class="tag">Most popular</span>' : p.key === 'pro' ? '<span class="tag bv">Best value · Recommended</span>' : '';
    var pts = p.pts.concat(ALL);
    return '<div class="plan' + (featured ? ' ft' : '') + '">' + tag +
      '<span class="pn">' + p.label + '</span>' +
      '<div class="pp"><b>' + p.price + '</b><span>' + p.per + '</span></div>' +
      '<ul>' + pts.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' +
      '<a class="btn' + (featured ? '' : ' ghost') + '" href="https://studio.allcoaching.in/" data-checkout data-plan="' + p.key + '_m" data-ev="ob_cta_click" data-where="plan-' + p.key + '-monthly">Start free with ' + p.label + '</a>' +
      '<p class="yr" style="margin:10px 0 0;font-size:13px;line-height:1.5;text-align:center">Or pay yearly: <a href="https://studio.allcoaching.in/" data-checkout data-plan="' + p.key + '" data-ev="ob_cta_click" data-where="plan-' + p.key + '-yearly" style="color:inherit;text-decoration:underline">' + p.yr + '</a>, with your own Android &amp; iOS app</p></div>';
  }
  function render() {
    document.querySelectorAll('[data-from]').forEach(function (el) { el.textContent = '₹3,999'; });
    document.querySelectorAll('[data-keep-range]').forEach(function (el) { el.textContent = '100% on monthly plans (90–95% on yearly)'; });
    document.querySelectorAll('[data-plans]').forEach(function (box) {
      var feat = box.getAttribute('data-featured') || 'growth';
      box.innerHTML = PLANS.map(function (p) { return card(p, p.key === feat); }).join('');
      box.classList.add('ready');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render); else render();
})();
