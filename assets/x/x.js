/* AllCoaching X layer: mega-menu header, mobile drawer, hero word rotator, in-view video playback,
   floating studio-tour pill and video modal. No dependencies. */
(function () {
  var d = document, reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var h = d.querySelector('header.xh');

  /* ---------- header ---------- */
  if (h) {
    var trig = [].slice.call(h.querySelectorAll('.xh-t')), scrim = d.getElementById('xh-scrim'), cur = null, tOpen = 0, tClose = 0;
    var desk = matchMedia('(min-width: 981px)');
    // transparent over any dark hero (homepage video hero or an inner-page dark hero)
    var firstHero = d.querySelector('#main-content > .xhero:first-child, #main-content > .xphero:first-child, main > .xhero:first-child, main > .xphero:first-child, #main-content > .xdark:first-child > .xhero:first-child');
    if (firstHero) { h.classList.add('over'); d.body.classList.add('xover'); }
    function solid() { h.classList.toggle('solid', scrollY > 40 || !h.classList.contains('over')); }
    function show(b) {
      if (cur === b) return; hide(true);
      var p = d.getElementById(b.getAttribute('aria-controls')); if (!p) return;
      cur = b; b.setAttribute('aria-expanded', 'true'); p.hidden = false;
      requestAnimationFrame(function () { p.classList.add('on'); });
      h.classList.add('open'); if (scrim) scrim.classList.add('on');
    }
    function hide(fast) {
      if (!cur) return;
      var p = d.getElementById(cur.getAttribute('aria-controls'));
      cur.setAttribute('aria-expanded', 'false'); cur = null;
      if (p) { p.classList.remove('on'); if (fast) p.hidden = true; else setTimeout(function () { if (!p.classList.contains('on')) p.hidden = true; }, 220); }
      h.classList.remove('open'); if (scrim) scrim.classList.remove('on');
    }
    trig.forEach(function (b) {
      b.addEventListener('click', function () { cur === b ? hide() : show(b); });
      b.addEventListener('mouseenter', function () { if (!desk.matches) return; clearTimeout(tClose); clearTimeout(tOpen); tOpen = setTimeout(function () { show(b); }, cur ? 0 : 110); });
      b.addEventListener('keydown', function (e) { if (e.key === 'ArrowDown') { e.preventDefault(); show(b); var f = d.getElementById(b.getAttribute('aria-controls')).querySelector('a'); if (f) f.focus(); } });
    });
    h.addEventListener('mouseleave', function () { clearTimeout(tOpen); tClose = setTimeout(function () { hide(); }, 180); });
    h.addEventListener('mouseenter', function () { clearTimeout(tClose); });
    h.querySelectorAll('.xh-nav > a, .xh-pill, .xh-logo').forEach(function (a) { a.addEventListener('mouseenter', function () { if (desk.matches) { clearTimeout(tOpen); hide(); } }); });
    if (scrim) scrim.addEventListener('click', function () { hide(); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') { if (cur) { var b = cur; hide(); b.focus(); } closeDrawer(); } });
    d.addEventListener('click', function (e) { if (cur && !h.contains(e.target)) hide(); });
    addEventListener('scroll', solid, {passive: true}); solid();

    /* mobile drawer */
    var burger = h.querySelector('.xh-burger'), drawer = d.getElementById('xh-drawer');
    function closeDrawer() { if (!drawer || drawer.hidden) return; drawer.hidden = true; burger.setAttribute('aria-expanded', 'false'); d.documentElement.style.overflow = ''; h.classList.remove('open'); burger.innerHTML = burger.getAttribute('data-open'); }
    if (burger && drawer) {
      burger.setAttribute('data-open', burger.innerHTML);
      burger.addEventListener('click', function () {
        if (!drawer.hidden) return closeDrawer();
        drawer.hidden = false; burger.setAttribute('aria-expanded', 'true'); d.documentElement.style.overflow = 'hidden'; h.classList.add('open');
        burger.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>';
      });
      drawer.addEventListener('click', function (e) { if (e.target.closest('a')) closeDrawer(); });
      desk.addEventListener('change', function () { if (desk.matches) closeDrawer(); else hide(true); });
    }
  }

  /* ---------- hero word rotator ---------- */
  var rot = d.querySelector('.xrot');
  if (rot && !reduce) {
    var words = rot.getAttribute('data-words').split('|'), w = rot.querySelector('.w'), k = 0;
    setInterval(function () {
      if (d.hidden) return;
      w.classList.add('out');
      setTimeout(function () {
        k = (k + 1) % words.length; w.textContent = words[k];
        w.classList.remove('out'); w.classList.add('pre'); void w.offsetWidth; w.classList.remove('pre');
      }, 420);
    }, 2600);
  }

  /* ---------- reveal on scroll ---------- */
  var rv = [].slice.call(d.querySelectorAll('.xrv'));
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, {threshold: .12, rootMargin: '0px 0px -6% 0px'});
    rv.forEach(function (el) { io.observe(el); });
  } else rv.forEach(function (el) { el.classList.add('in'); });

  /* ---------- background videos: play only while on screen ---------- */
  var vids = [].slice.call(d.querySelectorAll('video[data-bg]'));
  function load(v) { if (!v.src && v.getAttribute('data-src')) { v.src = v.getAttribute('data-src'); } }
  if (reduce) vids.forEach(function (v) { v.removeAttribute('autoplay'); v.pause && v.pause(); });
  else if ('IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function (es) {
      es.forEach(function (e) { var v = e.target; if (e.isIntersecting) { load(v); var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause(); });
    }, {threshold: .15});
    vids.forEach(function (v) { vo.observe(v); });
  } else vids.forEach(function (v) { load(v); });

  /* ---------- video modal ---------- */
  var modal = d.getElementById('xmodal'), mv = modal && modal.querySelector('video'), last = null;
  function openModal(src, from) {
    if (!modal) return; last = from || null;
    if (mv.getAttribute('src') !== src) mv.src = src;
    modal.hidden = false; d.documentElement.style.overflow = 'hidden';
    try { mv.currentTime = 0; } catch (e) {}
    var p = mv.play(); if (p && p.catch) p.catch(function () {});
    modal.querySelector('.close').focus();
  }
  function closeModal() { if (!modal || modal.hidden) return; mv.pause(); modal.hidden = true; d.documentElement.style.overflow = ''; if (last) last.focus(); }
  if (modal) {
    modal.addEventListener('click', function (e) { if (e.target === modal || e.target.closest('.close')) closeModal(); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });
  }
  d.addEventListener('click', function (e) {
    var t = e.target.closest('[data-xvideo]'); if (!t) return;
    if (e.target.closest('.x')) return;
    e.preventDefault(); openModal(t.getAttribute('data-xvideo'), t);
  });

  /* ---------- YouTube lite embed: <button class="xyt" data-yt="ID"> -> iframe on click ---------- */
  d.addEventListener('click', function (e) {
    var b = e.target.closest('.xyt'); if (!b || b.classList.contains('on')) return;
    e.preventDefault();
    var f = d.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-yt') + '?autoplay=1&rel=0&playsinline=1&modestbranding=1';
    f.title = b.getAttribute('aria-label') || 'AllCoaching studio tutorial';
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.allowFullscreen = true;
    b.classList.add('on'); b.appendChild(f);
  });
  /* tutorial switcher: [data-ytpick="ID"] swaps the main player */
  d.addEventListener('click', function (e) {
    var t = e.target.closest('[data-ytpick]'); if (!t) return;
    var main = d.querySelector('.xyt'); if (!main) return;
    e.preventDefault();
    var fr = main.querySelector('iframe'); if (fr) fr.remove(); main.classList.remove('on');
    main.setAttribute('data-yt', t.getAttribute('data-ytpick'));
    var img = main.querySelector('img'); if (img && t.getAttribute('data-thumb')) img.src = t.getAttribute('data-thumb');
    var cap = d.querySelector('.xf-vcap b'); if (cap && t.getAttribute('data-title')) cap.textContent = t.getAttribute('data-title');
    [].forEach.call(d.querySelectorAll('[data-ytpick]'), function (x) { x.classList.toggle('on', x === t); });
  });

  /* ---------- floating studio-tour pill ---------- */
  var pill = d.getElementById('xvpill');
  if (pill) {
    try { if (sessionStorage.getItem('xvp') === '0') pill.classList.add('gone'); } catch (e) {}
    pill.querySelector('.x').addEventListener('click', function (e) { e.stopPropagation(); e.preventDefault(); pill.classList.add('gone'); try { sessionStorage.setItem('xvp', '0'); } catch (er) {} });
    var foot = d.querySelector('footer');
    if (foot && 'IntersectionObserver' in window) new IntersectionObserver(function (es) { pill.style.opacity = es[0].isIntersecting ? '0' : ''; pill.style.pointerEvents = es[0].isIntersecting ? 'none' : ''; }).observe(foot);
  }
})();
