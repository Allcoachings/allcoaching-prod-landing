(function () {
  'use strict';

  var WA_NUMBER = '919889977262';
  var WA_MSG = {
    studio: 'Hi AllCoaching, I saw the Studio demo and want to start my academy.',
    app: 'Hi AllCoaching, I saw the student app demo and want an app like this for my academy.',
    website: 'Hi AllCoaching, I saw the website demo and want a website like this for my academy.',
    general: 'Hi AllCoaching, I saw the live demo and have a few questions before I join.'
  };

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var dl = window.dataLayer = window.dataLayer || [];
  var track = function (event, data) { var o = { event: event }; for (var k in data) o[k] = data[k]; dl.push(o); };

  var yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();

  var topbar = $('#topbar');
  var onScroll = function () { topbar.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var mobnav = $('#mobnav'), burger = $('.burger');
  var setMenu = function (open) {
    mobnav.hidden = !open;
    burger.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('locked', open);
    if (open) $('.mobnav-close').focus();
  };
  burger.addEventListener('click', function () { setMenu(true); });
  mobnav.addEventListener('click', function (e) {
    if (e.target === mobnav || e.target.closest('.mobnav-close') || e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !mobnav.hidden) setMenu(false); });

  $$('[data-wa]').forEach(function (a) {
    var msg = WA_MSG[a.getAttribute('data-wa-product')] || WA_MSG.general;
    a.href = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg);
    a.target = '_blank';
    a.rel = 'noopener';
  });

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a) return;
    if (a.hasAttribute('data-wa')) track('whatsapp_click', { where: a.getAttribute('data-wa') });
    else if (a.hasAttribute('data-demo')) track('demo_open', { product: a.getAttribute('data-demo'), where: a.getAttribute('data-where') || '' });
    else if (a.hasAttribute('data-track')) track(a.getAttribute('data-track') + '_click', { where: a.getAttribute('data-where') || '' });
  });

  var bubble = $('#wabubble');
  try {
    if (!sessionStorage.getItem('ac-wa-bubble')) {
      setTimeout(function () {
        bubble.hidden = false;
        sessionStorage.setItem('ac-wa-bubble', '1');
        setTimeout(function () { bubble.hidden = true; }, 6000);
      }, 9000);
    }
  } catch (e) {}

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -6% 0px' });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('in'); });
  }
})();
