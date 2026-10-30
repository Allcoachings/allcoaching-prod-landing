/*!
 * AllCoaching studio walkthrough: the real studio's Own branding screens (Templates → Themes →
 * Domain → App → Marketing tools), shown one after another inside a browser frame. Each screen
 * eases in on the part that matters and a click lands where the educator would click.
 * Screens are screenshots of studio.allcoaching.in (landing/img/studio-*.webp), not mock-ups.
 *
 *   <div data-studio-anim></div>
 *   window.ACStudioAnim.mount(el, { compact: true })   // smaller version, used by the checkout
 *
 * Decorative: aria-hidden, and it pauses when off screen.
 */
(function () {
  'use strict';
  if (window.ACStudioAnim) return;

  var IMG = '/landing/img/studio-';
  var V = '?v=2';
  // key, label, image, zoom origin x/y (%), zoom, click x/y (%)
  var STEPS = [
    ['templates', 'Templates', 52, 80, 1.55, 33, 82],
    ['themes', 'Themes', 56, 68, 1.5, 70, 86],
    ['domain', 'Domain', 44, 44, 1.6, 70, 53],
    ['app', 'App', 50, 54, 1.5, 42, 75],
    ['marketing', 'Marketing tools', 62, 80, 1.55, 94, 88]
  ];
  var DUR = 3600;

  var CSS = [
    '.sa{position:relative;width:100%;max-width:580px;background:#fff;border:1px solid #E3E7F0;border-radius:18px;overflow:hidden;box-shadow:0 1px 2px rgba(15,18,32,.05),0 50px 90px -46px rgba(15,25,120,.5);font-family:"Inter Tight",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#14161F;user-select:none}',
    '.sa *{box-sizing:border-box}',
    '.sa-top{display:flex;align-items:center;gap:6px;padding:9px 12px;border-bottom:1px solid #EEF0F6;background:#FBFCFE}',
    '.sa-top i{width:9px;height:9px;border-radius:50%;background:#E3E6EE}',
    '.sa-top span{margin:0 auto;font:500 11px/1 "JetBrains Mono",ui-monospace,monospace;color:#7A8094;background:#F1F3F8;border-radius:7px;padding:5px 12px}',
    '.sa-view{position:relative;aspect-ratio:1.6;overflow:hidden;background:#F6F8FC}',
    '.sa-sl{position:absolute;inset:0;opacity:0;transition:opacity .7s ease}',
    '.sa-sl.on{opacity:1}',
    '.sa-z{position:absolute;inset:0;transform-origin:var(--ox) var(--oy);transition:transform 3.4s cubic-bezier(.45,0,.2,1)}',
    '.sa-sl.go .sa-z{transform:scale(var(--s))}',
    '.sa-z img{display:block;width:100%;height:100%;object-fit:cover}',
    '.sa-tap{position:absolute;left:var(--tx);top:var(--ty);width:0;height:0}',
    '.sa-tap svg{position:absolute;left:-3px;top:-2px;width:20px;height:20px;opacity:0;transform:translate(26px,22px);filter:drop-shadow(0 2px 3px rgba(0,0,0,.3))}',
    '.sa-tap:before{content:"";position:absolute;left:-14px;top:-14px;width:28px;height:28px;border-radius:50%;border:2px solid #2B44FF;background:rgba(43,68,255,.18);opacity:0}',
    '.sa-sl.go .sa-tap svg{animation:sacur 1.6s .9s cubic-bezier(.45,0,.2,1) forwards}',
    '.sa-sl.go .sa-tap:before{animation:satap .7s 2.25s ease-out forwards}',
    '@keyframes sacur{0%{opacity:0;transform:translate(26px,22px)}35%{opacity:1}75%,100%{opacity:1;transform:none}}',
    '@keyframes satap{0%{opacity:1;transform:scale(.4)}100%{opacity:0;transform:scale(1.7)}}',
    '.sa-steps{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;padding:11px 12px 12px;border-top:1px solid #EEF0F6}',
    '.sa-st{font-size:11.5px;font-weight:600;color:#9AA0B4;transition:color .3s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
    '.sa-st i{display:block;height:3px;border-radius:99px;background:#EEF0F6;margin-bottom:7px;overflow:hidden}',
    '.sa-st i b{display:block;height:100%;width:0;background:#2B44FF;border-radius:99px}',
    '.sa-st.done{color:#4A5063}.sa-st.done i b{width:100%}',
    '.sa-st.on{color:#14161F}.sa-st.on i b{width:100%;transition:width var(--d) linear}',
    // compact
    '.sa.sa-c{max-width:none;border-radius:14px}',
    '.sa-c .sa-top{padding:7px 10px}.sa-c .sa-top i{width:7px;height:7px}.sa-c .sa-top span{font-size:10px;padding:4px 9px}',
    '.sa-c .sa-steps{padding:8px 10px 9px;gap:4px}.sa-c .sa-st{font-size:10px}.sa-c .sa-st i{margin-bottom:5px}',
    '@media (max-width:560px){.sa-st{font-size:10px}}',
    '@media (prefers-reduced-motion:reduce){.sa *{transition:none!important;animation:none!important}}'
  ].join('');

  var cssDone = false;
  function injectCSS() {
    if (cssDone) return;
    cssDone = true;
    var st = document.createElement('style');
    st.textContent = CSS;
    document.head.appendChild(st);
  }
  var CUR = '<svg viewBox="0 0 24 24"><path d="M5 3l14 8-6 1.5L10 19z" fill="#14161F" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/></svg>';

  function mount(el, opts) {
    if (!el || el.__sa) return el && el.__sa;
    injectCSS();
    opts = opts || {};
    var compact = !!(opts.compact || (el.dataset && el.dataset.compact === '1'));
    el.classList.add('sa');
    if (compact) el.classList.add('sa-c');
    el.setAttribute('aria-hidden', 'true');
    el.style.setProperty('--d', DUR + 'ms');

    el.innerHTML =
      '<div class="sa-top"><i></i><i></i><i></i><span>studio.allcoaching.in</span></div>' +
      '<div class="sa-view">' + STEPS.map(function (s, i) {
        return '<div class="sa-sl" style="--ox:' + s[2] + '%;--oy:' + s[3] + '%;--s:' + s[4] + ';--tx:' + s[5] + '%;--ty:' + s[6] + '%">' +
          '<div class="sa-z"><img src="' + IMG + s[0] + '.webp' + V + '" alt="" width="1440" height="900"' + (i ? ' loading="lazy"' : '') + ' decoding="async"/>' +
          '<span class="sa-tap">' + CUR + '</span></div></div>';
      }).join('') + '</div>' +
      '<div class="sa-steps">' + STEPS.map(function (s) { return '<span class="sa-st"><i><b></b></i>' + s[1] + '</span>'; }).join('') + '</div>';

    var slides = el.querySelectorAll('.sa-sl'), labels = el.querySelectorAll('.sa-st');
    var idx = -1, timer = null, running = false;
    function show(n) {
      idx = n;
      for (var i = 0; i < slides.length; i++) {
        var on = i === n;
        slides[i].classList.toggle('on', on);
        if (!on) (function (sl) { setTimeout(function () { if (!sl.classList.contains('on')) sl.classList.remove('go'); }, 750); })(slides[i]);
        labels[i].classList.toggle('done', i < n);
        labels[i].classList.remove('on');
      }
      // restart the zoom, click and progress bar on the next frame so the transitions replay
      requestAnimationFrame(function () { requestAnimationFrame(function () {
        if (idx !== n) return;
        slides[n].classList.add('go');
        labels[n].classList.add('on');
      }); });
    }
    function next() {
      if (!running) return;
      show((idx + 1) % STEPS.length);
      timer = setTimeout(next, DUR);
    }
    function start() { if (running) return; running = true; if (idx < 0) next(); else timer = setTimeout(next, 900); }
    function stop() { running = false; clearTimeout(timer); }

    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    if (still) show(0);
    else if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) start(); else stop(); }); }, { threshold: .15 }).observe(el);
    } else start();

    el.__sa = { start: start, stop: stop };
    return el.__sa;
  }

  window.ACStudioAnim = { mount: mount };
  function auto() { document.querySelectorAll('[data-studio-anim]').forEach(function (el) { mount(el); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', auto); else auto();
})();
