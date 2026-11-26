/* /journey: stage tabs inside each step, and the sticky stage index */
(function () {
  var d = document;
  // tabs: one screenshot + one text pane per part
  [].forEach.call(d.querySelectorAll('[data-jr]'), function (f) {
    var tabs = f.querySelectorAll('.jr-tab');
    function show(i) {
      [].forEach.call(f.querySelectorAll('.jr-tab,.jr-pane,.jr-shot'), function (el) {
        var on = el.getAttribute('data-i') === String(i);
        el.classList.toggle('on', on);
        if (el.classList.contains('jr-tab')) el.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
    }
    [].forEach.call(tabs, function (t) { t.addEventListener('click', function () { show(t.getAttribute('data-i')); }); });
    // clicking the screenshot moves to the next part
    var scr = f.querySelector('.jr-screen');
    if (scr) scr.addEventListener('click', function () {
      var cur = f.querySelector('.jr-tab.on'); var n = (Number(cur ? cur.getAttribute('data-i') : 0) + 1) % tabs.length; show(n);
    });
  });
  // sticky index: mark the stage on screen
  var links = d.querySelectorAll('.jr-idx a');
  if (links.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        var k = en.target.getAttribute('data-ch');
        [].forEach.call(links, function (a) { a.classList.toggle('on', a.getAttribute('data-ch') === k); });
      });
    }, {rootMargin: '-45% 0px -45% 0px'});
    [].forEach.call(d.querySelectorAll('.jr-ch'), function (s) { io.observe(s); });
  }
})();

/* /journey: build your academy. Everything stays in this page; nothing is sent anywhere. */
(function () {
  var ab = document.querySelector('[data-ab]');
  if (!ab) return;
  var $ = function (s) { return ab.querySelector(s); }, $$ = function (s) { return [].slice.call(ab.querySelectorAll(s)); };
  var name = $('#ab-name'), dom = $('#ab-dom'), course = $('#ab-course'), price = $('#ab-price');
  var st = {step: 1, max: 1, subj: '', cat: '', connected: false, published: false, built: false, sold: false, domTouched: false, courseTouched: false};
  var timers = [];
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function bind(k, v) { $$('[data-b="' + k + '"]').forEach(function (e) { e.textContent = v; }); }
  function nm() { return (name.value.trim() || 'Your Academy').replace(/\s+/g, ' '); }
  function slug(s) { return (s || '').toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 24); }
  function ini(s) { var w = s.split(' ').filter(Boolean); return ((w[0] || 'Y')[0] + (w[1] ? w[1][0] : (w[0] || 'A')[1] || '')).toUpperCase(); }
  function inr(v) { var n = parseInt(String(v).replace(/\D/g, ''), 10); return isNaN(n) ? '0' : n.toLocaleString('en-IN'); }
  function host() { var s = slug(dom.value) || slug(nm()) || 'youracademy'; return st.connected ? s + '.in' : s + '.allcoaching.in'; }
  function render() {
    var n = nm();
    bind('name', n); bind('ini', ini(n)); bind('short', n.length > 12 ? n.slice(0, 11) + '…' : n);
    bind('subj', st.subj || 'live'); bind('cat', st.cat || 'Your subject'); bind('count', st.published ? '1 course' : '0 courses');
    bind('course', course.value.trim() || (st.cat ? st.cat + ' Complete Course' : 'Your first course'));
    bind('price', inr(price.value)); bind('url', host()); bind('link', host() + '/courses');
    ['dom', 'course', 'installed', 'sold'].forEach(function () {});
    ab.classList.toggle('s-dom', st.connected); ab.classList.toggle('s-course', st.published);
    var sum = {1: name.value.trim() ? n : '', 2: st.subj, 3: st.connected ? host() : '', 4: st.published ? '₹' + inr(price.value) : '', 5: st.built ? 'Ready' : '', 6: st.sold ? '1 sale (example)' : ''};
    $$('[data-sum]').forEach(function (e) { e.textContent = sum[e.getAttribute('data-sum')] || ''; });
    var g1 = $('[data-next="2"]'); g1.disabled = !name.value.trim();
    var g2 = $('[data-next="3"]'); g2.disabled = !st.subj;
  }
  function go(n) {
    st.step = n; st.max = Math.max(st.max, n); ab.setAttribute('data-step', n);
    $$('.ab-st').forEach(function (li) { var s = +li.getAttribute('data-s'); li.classList.toggle('on', s === n); li.classList.toggle('done', s < st.max || (s === 6 && st.sold)); });
    var li = $('.ab-st[data-s="' + n + '"]'); var inp = li && li.querySelector('input');
    if (inp && window.innerWidth > 1100) later(function () { inp.focus({preventScroll: true}); }, 350);
  }
  name.addEventListener('input', function () { if (!st.domTouched) dom.value = slug(name.value); render(); });
  name.addEventListener('keydown', function (e) { if (e.key === 'Enter' && name.value.trim()) go(2); });
  dom.addEventListener('input', function () { st.domTouched = true; dom.value = dom.value.toLowerCase().replace(/[^a-z0-9-]/g, ''); render(); });
  course.addEventListener('input', function () { st.courseTouched = true; render(); });
  price.addEventListener('input', function () { price.value = price.value.replace(/\D/g, ''); render(); });
  $$('[data-col] button').forEach(function (b) { b.addEventListener('click', function () {
    $$('[data-col] button').forEach(function (x) { x.classList.toggle('on', x === b); }); ab.style.setProperty('--b', b.getAttribute('data-v'));
  }); });
  $$('[data-subj] button').forEach(function (b) { b.addEventListener('click', function () {
    $$('[data-subj] button').forEach(function (x) { x.classList.toggle('on', x === b); });
    st.subj = b.getAttribute('data-v'); st.cat = b.getAttribute('data-cat');
    if (!st.courseTouched) course.value = st.cat + ' Complete Course';
    render();
  }); });
  $$('.ab-sh').forEach(function (h) { h.addEventListener('click', function () { var n = +h.parentNode.getAttribute('data-s'); if (n <= st.max) go(n); }); });
  function phone(cls) { ab.classList.remove('s-phone-home', 's-wa'); if (cls) ab.classList.add(cls); }
  ab.addEventListener('click', function (ev) {
    var t = ev.target.closest('[data-next],[data-act]'); if (!t || t.disabled) return;
    if (t.hasAttribute('data-next')) { go(+t.getAttribute('data-next')); return; }
    var a = t.getAttribute('data-act');
    if (a === 'connect') {
      if (!slug(dom.value)) { dom.focus(); return; }
      t.disabled = true; t.textContent = 'Checking DNS…';
      later(function () { t.textContent = 'Issuing HTTPS certificate…'; }, 700);
      later(function () { st.connected = true; render(); var em = $('.ab-bar em'); em.classList.remove('flip'); void em.offsetWidth; em.classList.add('flip'); t.disabled = false; t.textContent = 'Connected'; go(4); }, 1500);
    } else if (a === 'publish') {
      if (!course.value.trim()) { course.focus(); return; }
      st.published = true; render(); go(5);
    } else if (a === 'app') {
      t.disabled = true; t.textContent = 'Building your app…';
      phone('s-phone-home'); ab.classList.remove('s-installed'); ab.classList.add('s-building'); $('[data-inst]').textContent = 'Installing…';
      later(function () { ab.classList.add('s-installed'); $('[data-inst]').textContent = 'Installed · tap to open'; t.textContent = 'Opening your app…'; }, 2400);
      later(function () { phone(''); ab.classList.remove('s-building'); st.built = true; render(); t.disabled = false; t.textContent = 'App ready'; go(6); }, 3600);
    } else if (a === 'share') {
      t.disabled = true; phone('s-wa'); t.textContent = 'Sent to your students';
      later(function () { phone(''); ab.classList.add('s-sold'); st.sold = true; render(); go(6); }, 2200);
      later(function () { var d = $('.ab-done'); d.hidden = false; t.disabled = false; t.textContent = 'Share on WhatsApp'; d.scrollIntoView({behavior: 'smooth', block: 'center'}); }, 3600);
    } else if (a === 'reset') {
      timers.forEach(clearTimeout); timers = [];
      st = {step: 1, max: 1, subj: '', cat: '', connected: false, published: false, built: false, sold: false, domTouched: false, courseTouched: false};
      name.value = ''; dom.value = ''; course.value = ''; price.value = '1999';
      $$('[data-subj] button').forEach(function (x) { x.classList.remove('on'); });
      ab.classList.remove('s-sold', 's-installed', 's-building'); phone('');
      $('.ab-done').hidden = true; $('[data-act="connect"]').textContent = 'Connect domain'; $('[data-act="app"]').textContent = 'Build my app';
      render(); go(1); ab.scrollIntoView({behavior: 'smooth', block: 'start'});
    }
  });
  render(); go(1);
})();

/* /journey hero map: a living network. Nodes drift, lean away from the cursor, light up their cluster on hover,
   pulses run along the lines, and hovering a step shows its real studio screen. Pauses off screen. */
(function () {
  var svg = document.querySelector('.jr-svg'); if (!svg) return;
  var map = svg.parentNode, tip = map.querySelector('.jr-tip');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nodes = {}, list = [];
  [].forEach.call(svg.querySelectorAll('[data-id]'), function (g, i) {
    var n = {el: g, id: g.getAttribute('data-id'), x0: +g.getAttribute('data-x'), y0: +g.getAttribute('data-y'), x: 0, y: 0, vx: 0, vy: 0,
      ph: i * 1.7, sp: .35 + (i % 7) * .06, amp: g.classList.contains('jr-dot') ? 7 : g.classList.contains('jr-hub') ? 3 : 5,
      c: g.getAttribute('data-c')};
    n.x = n.x0; n.y = n.y0; nodes[n.id] = n; list.push(n);
  });
  var lines = [].map.call(svg.querySelectorAll('.jr-edges line'), function (l) { return {el: l, a: nodes[l.getAttribute('data-a')], b: nodes[l.getAttribute('data-b')], c: l.getAttribute('data-c')}; });
  var pulsesG = svg.querySelector('.jr-pulses'), pulses = [];
  var NS = 'http://www.w3.org/2000/svg';
  var mouse = null, hot = null, running = false, t0 = performance.now();

  function toSvg(ev) {
    var pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY;
    var m = svg.getScreenCTM(); return m ? pt.matrixTransform(m.inverse()) : null;
  }
  function place() {
    list.forEach(function (n) { n.el.setAttribute('transform', 'translate(' + n.x.toFixed(1) + ' ' + n.y.toFixed(1) + ')'); });
    lines.forEach(function (l) {
      if (!l.a || !l.b) return;
      l.el.setAttribute('x1', l.a.x.toFixed(1)); l.el.setAttribute('y1', l.a.y.toFixed(1));
      l.el.setAttribute('x2', l.b.x.toFixed(1)); l.el.setAttribute('y2', l.b.y.toFixed(1));
    });
  }
  function spawnPulse() {
    var pool = hot != null ? lines.filter(function (l) { return l.c === hot; }) : lines.filter(function (l) { return !l.el.classList.contains('l3') || Math.random() < .25; });
    var l = pool[Math.floor(Math.random() * pool.length)]; if (!l) return;
    var c = document.createElementNS(NS, 'circle'); c.setAttribute('r', l.el.classList.contains('l1') ? 3.2 : 2.4); c.setAttribute('class', 'jr-pulse');
    pulsesG.appendChild(c);
    var out = Math.random() < .5;
    pulses.push({el: c, l: l, t: 0, dur: 900 + Math.random() * 900, out: out});
  }
  var lastPulse = 0;
  function frame(now) {
    if (!running) return;
    var t = (now - t0) / 1000, dt = Math.min(48, now - (frame.prev || now)); frame.prev = now;
    list.forEach(function (n) {
      var tx = n.x0 + Math.sin(t * n.sp + n.ph) * n.amp, ty = n.y0 + Math.cos(t * n.sp * .8 + n.ph) * n.amp;
      if (mouse && n.id !== 'h') {
        var dx = n.x - mouse.x, dy = n.y - mouse.y, d = Math.sqrt(dx * dx + dy * dy) || 1, R = 150;
        if (n.el.classList.contains('jr-dot')) { if (d < R) { var f = (1 - d / R) * 46; tx += dx / d * f; ty += dy / d * f; } }
        else if (d < 70) { var m = (1 - d / 70) * .35; tx -= dx * m; ty -= dy * m; }
      }
      n.vx = (n.vx + (tx - n.x) * .08) * .78; n.vy = (n.vy + (ty - n.y) * .08) * .78;
      n.x += n.vx; n.y += n.vy;
    });
    place();
    if (lastXY && (frame.n = (frame.n || 0) + 1) % 6 === 0) hitTest();
    if (now - lastPulse > (hot != null ? 160 : 420)) { spawnPulse(); lastPulse = now; }
    pulses = pulses.filter(function (p) {
      p.t += dt; var k = p.t / p.dur; if (k >= 1) { p.el.remove(); return false; }
      var a = p.out ? p.l.a : p.l.b, b = p.out ? p.l.b : p.l.a;
      p.el.setAttribute('cx', (a.x + (b.x - a.x) * k).toFixed(1)); p.el.setAttribute('cy', (a.y + (b.y - a.y) * k).toFixed(1));
      p.el.setAttribute('opacity', (Math.sin(k * Math.PI)).toFixed(2));
      return true;
    });
    requestAnimationFrame(frame);
  }
  function start() { if (running || reduce) return; running = true; frame.prev = null; requestAnimationFrame(frame); }
  function stop() { running = false; }

  function setHot(c, g) {
    hot = c;
    map.classList.toggle('jr-hot', c != null);
    [].forEach.call(svg.querySelectorAll('[data-c]'), function (el) { el.classList.toggle('lit', c != null && el.getAttribute('data-c') === c); });
    [].forEach.call(document.querySelectorAll('.jr-index a'), function (a, i) { a.classList.toggle('lit', c != null && String(i - 2) === c); });
    if (!tip) return;
    if (g && g.getAttribute('data-tip-title')) {
      var img = g.getAttribute('data-tip-img');
      tip.classList.toggle('noimg', !img);
      if (img) tip.querySelector('img').setAttribute('src', img);
      tip.querySelector('b').textContent = g.getAttribute('data-tip-title');
      tip.querySelector('small').textContent = g.getAttribute('data-tip-sub') || '';
      var r = g.getBoundingClientRect(), mr = map.getBoundingClientRect();
      var x = r.left + r.width / 2 - mr.left, y = r.top - mr.top;
      var w = 230, left = Math.min(Math.max(12, x - w / 2), mr.width - w - 12);
      tip.style.left = left + 'px'; tip.style.top = Math.max(12, y - (img ? 172 : 70)) + 'px';
      tip.classList.add('on');
    } else tip.classList.remove('on');
  }
  var lastXY = null, hovered = null;
  function hitTest() {
    if (!lastXY) return;
    var el = document.elementFromPoint(lastXY[0], lastXY[1]);
    var g = el && el.closest && el.closest('.jr-node,.jr-sat');
    if (g === hovered) return;
    hovered = g;
    setHot(g ? g.getAttribute('data-c') : null, g);
  }
  svg.addEventListener('pointermove', function (ev) {
    if (ev.pointerType === 'touch') return;
    mouse = toSvg(ev); lastXY = [ev.clientX, ev.clientY]; hitTest();
  });
  svg.addEventListener('pointerleave', function () { mouse = null; lastXY = null; hovered = null; setHot(null); });
  // the index list on the left lights up its stage on the map
  [].forEach.call(document.querySelectorAll('.jr-index a'), function (a, i) {
    if (i < 2) return;
    a.addEventListener('mouseenter', function () { var g = svg.querySelector('.jr-node[data-c="' + (i - 2) + '"]'); setHot(String(i - 2), g); });
    a.addEventListener('mouseleave', function () { setHot(null); });
  });
  // keep the cluster lit for a moment when a touch user taps a stage, before the page scrolls there
  svg.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a'); if (!a) return;
    var href = a.getAttribute('href'); if (!href || href[0] !== '#') return;
    var target = document.querySelector(href); if (!target) return;
    ev.preventDefault();
    var g = a.closest('[data-c]'); if (g) setHot(g.getAttribute('data-c'), null);
    setTimeout(function () { target.scrollIntoView({behavior: 'smooth', block: 'start'}); setHot(null); }, 260);
  });
  place();
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es[0].isIntersecting ? start() : stop(); }).observe(svg);
  else start();
})();
