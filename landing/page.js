/* /landing v2 pages: funnel events, scroll reveal, sticky mobile button.
   <script src="/landing/page.js" data-page="lp_xxx" defer></script> */
(function () {
  var me = document.currentScript;
  var PAGE = (me && me.getAttribute('data-page')) || 'lp';
  document.documentElement.classList.add('js');
  var dl = window.dataLayer = window.dataLayer || [];
  function eid() { return 'ob.' + Date.now().toString(36) + '.' + Math.random().toString(36).slice(2, 10); }
  function push(ev, x) { var o = { event: ev, event_id: eid(), page: PAGE, page_variant: 'v2', currency: 'INR' }; for (var k in x) o[k] = x[k]; dl.push(o); }
  push('ob_view', {});
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-ev]');
    if (a) push(a.getAttribute('data-ev'), { where: a.getAttribute('data-where') || '', plan: a.getAttribute('data-plan') || '' });
  });
  var sent = {};
  addEventListener('scroll', function () {
    var h = document.documentElement, p = (scrollY + innerHeight) / h.scrollHeight * 100;
    [50, 90].forEach(function (d) { if (p >= d && !sent[d]) { sent[d] = 1; push('ob_scroll', { depth: d }); } });
  }, { passive: true });
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }); }, { threshold: .2 });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
  // background sketches: draw when they come into view, drift a little slower than the page
  var sk = document.querySelectorAll('.bgsk .d');
  if ('IntersectionObserver' in window) {
    var so = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); so.unobserve(x.target); } }); }, { rootMargin: '0px 0px -10% 0px' });
    sk.forEach(function (el) { so.observe(el); });
  } else sk.forEach(function (el) { el.classList.add('in'); });
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches, ticking = false;
  function px() { ticking = false; var y = scrollY; sk.forEach(function (el) { el.style.transform = 'translate3d(0,' + (y * (+el.getAttribute('data-d') || 0)).toFixed(1) + 'px,0)'; }); }
  if (!still && sk.length) addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(px); } }, { passive: true });
  var bar = document.getElementById('bar'), hc = document.getElementById('hero-cta'), fin = document.querySelector('.final');
  function sc() { if (bar && hc) bar.classList.toggle('on', hc.getBoundingClientRect().bottom < 0 && (!fin || fin.getBoundingClientRect().top > innerHeight * .6)); }
  sc(); addEventListener('scroll', sc, { passive: true });
})();
