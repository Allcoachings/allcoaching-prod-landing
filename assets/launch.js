/* Launch simulator — scripted walkthrough of the self-serve flow.
   Choose a plan → create a course → connect a domain → start selling.
   All names and figures are illustrative sample data. */
(function(){
  var root = document.getElementById('lx');
  if(!root) return;

  var vp = root.querySelector('.lx-viewport'),
      stage = root.querySelector('.lx-stage'),
      view = root.querySelector('.lx-view'),
      learn = root.querySelector('.lx-learn'),
      urlBox = root.querySelector('.lx-url'),
      urlTxt = root.querySelector('.lx-url-t'),
      cur = root.querySelector('.lx-cursor'),
      toasts = root.querySelector('.lx-toasts'),
      endCard = root.querySelector('.lx-end'),
      cap = root.querySelector('.lx-cap'),
      plan = root.querySelector('.lx-plan'),
      playBtn = root.querySelector('.lx-play'),
      chs = [].slice.call(root.querySelectorAll('.lx-ch')),
      bars = chs.map(function(c){ return c.querySelector('.bar i'); }),
      navs = [].slice.call(root.querySelectorAll('.lx-nav[data-k]'));

  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CANCEL = {};
  var run = 0, idx = 0, userPaused = false, vis = false, started = false;
  var active = false, elapsed = 0, est = 1, scale = 1, mode = '';

  /* ── icons ─────────────────────────────────────────────── */
  var P = {
    check:'<path d="M5 12.5l4.2 4.2L19 7"/>',
    video:'<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10.5l5-3v9l-5-3"/>',
    file:'<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h7M9 17h5"/>',
    upload:'<path d="M12 15V4M7.5 8.5L12 4l4.5 4.5M4 15v4a1 1 0 001 1h14a1 1 0 001-1v-4"/>',
    lock:'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
    globe:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 010 18M12 3a14 14 0 000 18"/>',
    bag:'<path d="M5 8h14l-1.2 12H6.2z"/><path d="M9 8V6.5a3 3 0 016 0V8"/>',
    card:'<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19"/>',
    play:'<path d="M8 5.5v13l11-6.5z" fill="currentColor" stroke="none"/>',
    home:'<path d="M4 11l8-7 8 7v9H4z"/>',
    compass:'<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    live:'<circle cx="12" cy="12" r="2"/><path d="M8 8a5.7 5.7 0 000 8M16 8a5.7 5.7 0 010 8"/>',
    book:'<path d="M5 4.5A1.5 1.5 0 016.5 3H19v15H6.5A1.5 1.5 0 005 19.5z"/><path d="M5 19.5A1.5 1.5 0 006.5 21H19"/>',
    test:'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 11l2 2 4-4"/>',
    search:'<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    rupee:'<path d="M7 5h10M7 9.5h10M9.5 5c3 0 5 1.6 5 4.5S12.5 14 9.5 14H8l7 6"/>',
    user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>'
  };
  function ic(k){ return '<svg class="i" viewBox="0 0 24 24" aria-hidden="true">' + P[k] + '</svg>'; }
  function q(s){ return stage.querySelector(s); }
  function inr(n){ return '₹' + n.toLocaleString('en-IN', {minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2}); }

  /* ── fit the fixed-size stage into the page ────────────── */
  function fit(){
    var w = vp.clientWidth; if(!w) return;
    var m = w < 740 ? 'compact' : 'wide';
    if(m !== mode){ mode = m; root.setAttribute('data-mode', m); }
    /* A narrower design width means a bigger zoom: on a 1260px hero the
       studio renders ~1.25x, so every label reads clearly at a glance. */
    var W = m === 'compact' ? Math.min(Math.max(w, 340), 460) : 1000;
    var H = m === 'compact' ? 700 : 640;
    scale = w / W;
    stage.style.width = W + 'px'; stage.style.height = H + 'px';
    stage.style.transform = 'scale(' + scale + ')';
    vp.style.height = Math.round(H * scale) + 'px';
  }
  fit();
  if(window.ResizeObserver) new ResizeObserver(fit).observe(vp); else window.addEventListener('resize', fit);

  /* ── helpers bound to one run (cancel-safe, pause-aware) ─ */
  function helpers(id, fast){
    var xy = [0, 0], hovEl = null;
    function alive(){ if(id !== run) throw CANCEL; }
    function wait(ms){
      if(fast) return Promise.resolve().then(alive);
      return new Promise(function(res, rej){
        var left = ms, last = performance.now();
        (function tick(now){
          if(id !== run) return rej(CANCEL);
          if(!userPaused && vis) left -= (now - last);
          last = now;
          if(left <= 0) res(); else requestAnimationFrame(tick);
        })(last);
      });
    }
    function pos(el){
      var s = stage.getBoundingClientRect(), r = el.getBoundingClientRect();
      return [(r.left - s.left) / scale + Math.min(r.width * .55, 70), (r.top - s.top) / scale + r.height * .58];
    }
    function hover(el){
      if(hovEl && hovEl !== el) hovEl.classList.remove('hov');
      hovEl = el; if(el) el.classList.add('hov');
    }
    async function move(el, ms){
      if(fast || !el) return;
      ms = ms || 720;
      xy = pos(el);
      cur.classList.add('show');
      cur.style.transitionDuration = ms + 'ms, .3s';
      cur.style.transform = 'translate(' + xy[0] + 'px,' + xy[1] + 'px)';
      await wait(ms + 30);
      hover(el);
    }
    async function click(el, ms){
      await move(el, ms);
      alive();
      if(fast) return;
      cur.classList.add('dn'); el.classList.add('press');
      var r = document.createElement('span'); r.className = 'lx-rip';
      r.style.left = xy[0] + 'px'; r.style.top = xy[1] + 'px';
      stage.appendChild(r); setTimeout(function(){ r.remove(); }, 650);
      await wait(130);
      cur.classList.remove('dn'); el.classList.remove('press');
      await wait(170);
    }
    async function type(el, text, cb, sp){
      el.classList.remove('ph'); el.classList.add('caret');
      if(fast){ el.textContent = text; if(cb) cb(text); }
      else for(var i = 1; i <= text.length; i++){
        el.textContent = text.slice(0, i); if(cb) cb(el.textContent);
        await wait((sp || 46) + Math.random() * 42);
      }
      el.classList.remove('caret'); alive();
    }
    async function count(el, a, b, ms, f){
      if(fast){ el.textContent = f(b); return; }
      var n = Math.max(10, Math.round(ms / 32));
      for(var i = 1; i <= n; i++){
        var t = i / n, e = 1 - Math.pow(1 - t, 3);
        el.textContent = f(a + (b - a) * e);
        await wait(ms / n);
      }
      el.textContent = f(b);
    }
    function focus(el){
      [].forEach.call(stage.querySelectorAll('.lx-in.focus'), function(x){ x.classList.remove('focus'); });
      if(el) el.classList.add('focus');
    }
    function toast(title, sub, icon, good){
      if(fast) return;
      var t = document.createElement('div');
      t.className = 'lx-toast' + (good ? ' g' : '');
      t.innerHTML = '<span class="ti">' + ic(icon || 'check') + '</span><div><b>' + title + '</b><span>' + sub + '</span></div>';
      toasts.appendChild(t);
      while(toasts.children.length > 2) toasts.firstChild.remove();
      setTimeout(function(){ t.classList.add('out'); setTimeout(function(){ t.remove(); }, 420); }, 3400);
    }
    return {wait:wait, move:move, click:click, type:type, count:count, focus:focus, toast:toast, hover:hover, alive:alive, fast:fast};
  }

  /* ── shell state ───────────────────────────────────────── */
  function setUrl(u){
    if(urlTxt.textContent === u) return;
    urlTxt.textContent = u;
    urlBox.classList.remove('chg'); void urlBox.offsetWidth; urlBox.classList.add('chg');
  }
  function studio(k, u){
    learn.classList.remove('on');
    navs.forEach(function(n){ n.classList.toggle('on', n.getAttribute('data-k') === k); });
    setUrl(u);
  }
  function mount(html){
    view.innerHTML = html;
    view.classList.remove('in'); void view.offsetWidth; view.classList.add('in');
  }
  function setPlan(on){
    plan.classList.toggle('on', !!on);
    plan.querySelector('.k').textContent = on ? 'Growth · active' : 'No plan yet';
    plan.querySelector('.v').textContent = on ? 'Renews in 12 months · 10 live hrs/month' : 'Choose a plan to publish your academy';
  }
  function resetShell(){
    toasts.innerHTML = '';
    endCard.classList.remove('on');
    cur.classList.remove('show', 'dn');
    [].forEach.call(stage.querySelectorAll('.lx-rip'), function(r){ r.remove(); });
  }

  /* ── Scene 1 · choose a plan ───────────────────────────── */
  var PLANS = [
    {n:'Starter', p:'6,999', f:'10', k:'90', l:['Your own domain', 'Live classes · 5 hrs/month', 'Marketplace discovery']},
    {n:'Growth', p:'12,999', f:'7.5', k:'92.5', l:['Your own domain', 'Live classes · 10 hrs/month', 'Marketplace discovery']},
    {n:'Pro', p:'24,999', f:'5', k:'95', l:['Your own domain', 'Live classes · 15 hrs/month', 'Premium website template']}
  ];
  async function scPlan(h){
    studio('billing', 'studio.allcoaching.in/billing'); setPlan(0);
    mount(
      '<div class="lx-eb">Billing</div><h3 class="lx-h">Choose your plan.</h3>' +
      '<p class="lx-p">Annual plans · prices exclude GST · every plan includes your own domain</p>' +
      '<div class="lx-plans">' + PLANS.map(function(p, i){
        return '<div class="lx-pl" data-i="' + i + '"><div class="n">' + p.n + (i === 2 ? '<span>Premium template</span>' : '') + '</div>' +
          '<div class="pr">₹' + p.p + '<small> /year</small></div><span class="fee">' + p.f + '% fee · you keep ' + p.k + '%</span>' +
          '<ul>' + p.l.map(function(x){ return '<li>' + ic('check') + x + '</li>'; }).join('') + '</ul>' +
          '<div class="lx-btn' + (i === 1 ? ' dark' : '') + '">Choose ' + p.n + '</div></div>';
      }).join('') + '</div>' +
      '<div class="lx-scrim"></div>' +
      '<div class="lx-drawer"><div class="lx-dw">' +
        '<div class="lx-eb">Checkout</div><h4 class="lx-h4">Growth · annual</h4>' +
        '<div class="lx-row"><span>Growth plan · 12 months</span><b>₹12,999.00</b></div>' +
        '<div class="lx-row"><span>GST (18%)</span><b>₹2,339.82</b></div>' +
        '<div class="lx-row tot"><span>Total today</span><b>₹15,338.82</b></div>' +
        '<span class="lx-lbl mt">Pay with</span>' +
        '<div class="lx-pm"><span class="on">UPI</span><span>Card</span><span>Netbanking</span></div>' +
        '<div class="lx-in mt" id="pUpi"><span class="v ph">yourname@upi</span></div>' +
        '<div class="lx-btn acc lx-pay mt">Pay ₹15,338.82</div>' +
        '<p class="lx-fine">Renews yearly · upgrade anytime, unused value is credited</p>' +
      '</div></div>'
    );
    var cards = view.querySelectorAll('.lx-pl'), g = cards[1];
    await h.wait(900);
    await h.move(cards[0], 900); await h.wait(350);
    await h.move(cards[2], 700); await h.wait(350);
    await h.move(g, 600); await h.wait(250);
    var gb = g.querySelector('.lx-btn');
    await h.click(gb, 500);
    g.classList.add('sel'); h.hover(null);
    await h.wait(250);
    q('.lx-view .lx-scrim').classList.add('on'); q('.lx-drawer').classList.add('on');
    await h.wait(900);
    var upi = q('#pUpi');
    await h.click(upi, 700); h.focus(upi);
    await h.type(upi.querySelector('.v'), 'neha.sharma@upi');
    h.focus(null);
    var pay = q('.lx-pay');
    await h.click(pay, 600);
    pay.innerHTML = '<span class="lx-spin"></span>Confirming payment';
    await h.wait(1500);
    q('.lx-dw').innerHTML =
      '<div class="lx-okw"><div class="lx-okc"><svg class="i" viewBox="0 0 24 24">' + P.check + '</svg></div>' +
      '<h4 class="lx-h4">Growth plan active.</h4><p class="lx-p">Receipt emailed · renews in 12 months</p>' +
      '<div class="lx-row mt"><span>Platform fee on your sales</span><b>7.5%</b></div>' +
      '<div class="lx-row"><span>You keep on every sale</span><b>92.5%</b></div>' +
      '<div class="lx-row"><span>Live classes</span><b>10 hrs/month</b></div></div>';
    setPlan(1);
    h.toast('Payment received', 'Growth plan is active on your studio', 'card', true);
    await h.wait(2300);
  }

  /* ── Scene 2 · create a course ─────────────────────────── */
  var TITLE = 'JEE Physics — Complete Mechanics';
  var FILES = [
    ['video', '01 · Kinematics in one dimension.mp4', '486 MB'],
    ['video', '02 · Newton’s laws, every exam pattern.mp4', '612 MB'],
    ['file', '03 · Mechanics formula sheet.pdf', '4 MB']
  ];
  async function scCourse(h){
    studio('courses', 'studio.allcoaching.in/courses/new'); setPlan(1);
    mount(
      '<div class="lx-head"><div><div class="lx-eb">Courses · New</div><h3 class="lx-h">Create a course.</h3></div><span class="lx-status" id="cSt">Draft</span></div>' +
      '<div class="lx-cgrid"><div class="lx-card lx-form">' +
        '<span class="lx-lbl">Course title</span><div class="lx-in" id="cT"><span class="v ph">e.g. Complete Mechanics for JEE</span></div>' +
        '<span class="lx-lbl mt">Exam</span><div class="lx-chips"><span class="lx-chip">NEET</span><span class="lx-chip" id="cJ">JEE Main</span><span class="lx-chip">JEE Advanced</span><span class="lx-chip">Boards</span></div>' +
        '<span class="lx-lbl mt">Lessons</span><div class="lx-drop" id="cD"><div class="lx-dropz">' + ic('upload') + 'Drop videos &amp; PDFs, or <u>browse</u></div><div id="cF"></div></div>' +
        '<div class="lx-2"><div><span class="lx-lbl mt">Price</span><div class="lx-in" id="cP"><span class="cur">₹</span><span class="v ph">0</span></div></div>' +
        '<div><span class="lx-lbl mt">Access</span><div class="lx-in">12 months</div></div></div>' +
        '<div class="lx-tg mt"><span>List on the AllCoaching marketplace</span><span class="lx-sw" id="cS"></span></div>' +
        '<div class="lx-btn acc lx-cpub">Publish course</div>' +
      '</div>' +
      '<div class="lx-card lx-pvcard"><span class="lx-lbl">Student preview</span>' +
        '<div class="lx-pv"><div class="th"><span class="tg" id="pvG">Course</span><div class="tt" id="pvT"></div></div>' +
        '<div class="bd"><b id="pvB">Untitled course</b><span>Neha Sharma · Sharma Physics</span>' +
        '<div class="prr"><span id="pvL">0 lessons</span><b id="pvP">₹0</b></div></div></div>' +
        '<div class="lx-btn acc" id="cPub">Publish course</div>' +
      '</div></div>'
    );
    var t = q('#cT'), pvT = q('#pvT'), pvB = q('#pvB');
    await h.wait(700);
    await h.click(t, 800); h.focus(t);
    await h.type(t.querySelector('.v'), TITLE, function(s){ pvT.textContent = s; pvB.textContent = s; }, 38);
    h.focus(null);
    var j = q('#cJ');
    await h.click(j, 600); j.classList.add('on'); q('#pvG').textContent = 'JEE Main';
    var d = q('#cD'), list = q('#cF');
    await h.click(d, 650);
    d.classList.add('hov');
    await h.wait(300);
    q('.lx-dropz').remove();
    var rows = FILES.map(function(f){
      var r = document.createElement('div'); r.className = 'lx-file';
      r.innerHTML = '<span class="ic">' + ic(f[0]) + '</span><div><div class="nm">' + f[1] + '</div><div class="pb"><i></i></div></div><span class="st">' + f[2] + '</span>';
      list.appendChild(r); return r;
    });
    d.classList.remove('hov'); h.hover(null);
    await h.wait(60);
    rows.forEach(function(r, i){ setTimeout(function(){ r.querySelector('.pb i').style.width = '100%'; }, h.fast ? 0 : i * 380); });
    for(var i = 0; i < rows.length; i++){
      await h.wait(i ? 380 : 1100);
      var st = rows[i].querySelector('.st'); st.textContent = 'Uploaded'; st.classList.add('ok');
      q('#pvL').textContent = (i + 1) + (i ? ' lessons' : ' lesson');
    }
    var p = q('#cP');
    await h.click(p, 700); h.focus(p);
    var pv = p.querySelector('.v');
    await h.type(pv, '4,999', function(s){ q('#pvP').textContent = '₹' + s; }, 90);
    h.focus(null);
    var sw = q('#cS');
    await h.click(sw, 650); sw.classList.add('on');
    await h.wait(350);
    var pubs = [q('#cPub'), q('.lx-cpub')];
    var pub = mode === 'compact' ? pubs[1] : pubs[0];
    await h.click(pub, 700);
    pubs.forEach(function(b){ b.innerHTML = '<span class="lx-spin"></span>Publishing'; });
    await h.wait(1100);
    pubs.forEach(function(b){ b.className = b.className.replace('acc', 'ok'); b.innerHTML = ic('check') + 'Published'; });
    var s = q('#cSt'); s.textContent = 'Published'; s.classList.add('ok');
    h.toast('Course published', 'Live in your studio and on the marketplace', 'book', true);
    await h.wait(2200);
  }

  /* ── Scene 3 · connect a domain ────────────────────────── */
  async function scDomain(h){
    studio('website', 'studio.allcoaching.in/website/domain'); setPlan(1);
    mount(
      '<div class="lx-eb">Website · Domain</div><h3 class="lx-h">Connect your domain.</h3>' +
      '<p class="lx-p">Included on every plan. Move your academy to a domain you own.</p>' +
      '<div class="lx-dgrid"><div class="lx-card">' +
        '<span class="lx-lbl">Your domain</span>' +
        '<div class="lx-dom"><div class="lx-in" id="dI"><span class="pre">https://</span><span class="v ph">yourdomain.in</span></div><div class="lx-btn dark" id="dG">Connect</div></div>' +
        '<div class="lx-cks">' +
          '<div class="lx-ck" id="k1"><span class="o"></span><div><b>Domain ownership verified</b><span>DNS records checked</span></div></div>' +
          '<div class="lx-ck" id="k2"><span class="o"></span><div><b>HTTPS certificate issued</b><span>Secure padlock for every student</span></div></div>' +
          '<div class="lx-ck" id="k3"><span class="o"></span><div><b>Academy website live</b><span id="k3s">Waiting</span></div></div>' +
        '</div></div>' +
      '<div class="lx-card lx-mini"><div class="lx-mbar"><i></i><i></i><i></i><span class="lx-murl" id="mU">' + ic('lock') + '<span>sharma-physics.allcoaching.in</span></span></div>' +
        '<div class="lx-msite"><div class="lx-mhd"><span class="m">S</span>Sharma Physics<nav><span>Courses</span><span>Live</span><span>Tests</span></nav></div>' +
        '<div class="lx-mhero">Physics that finally <em>clicks.</em></div><div class="lx-msub">JEE Main &amp; Advanced · taught by Neha Sharma</div>' +
        '<div class="lx-mcard"><span class="t"></span><div><b>JEE Physics — Complete Mechanics</b><span>3 lessons · 12 months access</span></div><span class="p">₹4,999</span></div>' +
      '</div></div></div>'
    );
    var inp = q('#dI');
    await h.wait(700);
    await h.click(inp, 800); h.focus(inp);
    await h.type(inp.querySelector('.v'), 'sharmaphysics.in', null, 60);
    h.focus(null);
    var go = q('#dG');
    await h.click(go, 600);
    go.innerHTML = '<span class="lx-spin"></span>Checking';
    var ks = ['#k1', '#k2', '#k3'];
    for(var i = 0; i < 3; i++){
      var k = q(ks[i]), o = k.querySelector('.o');
      k.classList.add('run'); o.innerHTML = '<span class="lx-spin"></span>';
      await h.wait(i === 1 ? 1200 : 950);
      k.classList.remove('run'); k.classList.add('ok');
      o.innerHTML = '<svg class="i" viewBox="0 0 24 24">' + P.check + '</svg>';
    }
    q('#k3s').textContent = 'https://sharmaphysics.in';
    var mu = q('#mU'); mu.querySelector('span').textContent = 'sharmaphysics.in'; mu.classList.add('ok');
    go.className = 'lx-btn ok'; go.innerHTML = ic('check') + 'Connected';
    h.toast('sharmaphysics.in is live', 'Your academy, on your own domain', 'globe', true);
    await h.wait(2300);
  }

  /* ── Scene 4 · a student buys, the sale lands in the studio ─ */
  var BUYERS = [['RK', 'Rohan K.', 'Kota'], ['IP', 'Ishita P.', 'Jaipur'], ['AS', 'Aman S.', 'Patna'], ['KR', 'Kavya R.', 'Pune']];
  var PRICE = 4999;
  async function scSell(h){
    setPlan(1);
    navs.forEach(function(n){ n.classList.toggle('on', n.getAttribute('data-k') === 'dash'); });
    learn.innerHTML =
      '<aside class="lx-lside"><div class="lx-lbrand"><span class="lx-lmono">S</span><b>Sharma Physics</b></div>' +
        '<div class="lx-lnav">' + ic('home') + 'Home</div><div class="lx-lnav">' + ic('compass') + 'Explore</div>' +
        '<div class="lx-lnav">' + ic('live') + 'Live class</div><div class="lx-lhr"></div>' +
        '<div class="lx-lnav on">' + ic('book') + 'Courses</div><div class="lx-lnav">' + ic('test') + 'Test series</div>' +
        '<div class="lx-lnav">' + ic('file') + 'Notes &amp; PDFs</div>' +
        '<div class="lx-lmentor"><span class="lx-av">NS</span><div><b>Neha Sharma</b><span>Physics · JEE mentor</span></div></div>' +
      '</aside>' +
      '<div class="lx-lmain"><div class="lx-ltop"><div class="lx-lbrand lx-lbrandm" style="padding:0"><span class="lx-lmono">S</span><b>Sharma Physics</b></div>' +
        '<div class="lx-search">' + ic('search') + 'Search courses, tests, notes…</div><div class="lx-grow"></div>' +
        '<span class="lx-lchip">' + ic('live') + 'Live</span><span class="lx-av" style="background:var(--surface-3);color:var(--ink-2)">RK</span></div>' +
        '<div class="lx-lbody"><div class="lx-tabs"><span>For you</span><span>Live</span><span class="on">Courses</span><span>Test series</span><span>Notes &amp; PDFs</span></div>' +
          '<div class="lx-lhero"><div><span class="lx-leb">Course · JEE Main</span><h4>' + TITLE + '</h4>' +
            '<div class="lx-lby"><span class="lx-av">NS</span><div><b>Neha Sharma</b><span>Physics · Sharma Physics</span></div></div>' +
            '<div class="lx-lmeta"><span>3 lessons</span><span>Formula sheet</span><span>12 months access</span></div></div>' +
            '<div class="lx-buy"><div class="pr">₹4,999</div><span class="s">12 months access · watch on web and app</span>' +
            '<div class="lx-btn acc" id="lB">Enrol now</div><span class="s2">' + ic('lock') + 'Secure checkout · UPI &amp; cards</span></div></div>' +
          '<div class="lx-lsec"><span class="lx-lbl">Course content</span>' +
            FILES.map(function(f, i){ return '<div class="lx-less"><span class="pl">' + ic(i < 2 ? 'play' : 'file') + '</span><b>' + f[1].replace(/\.(mp4|pdf)$/, '') + '</b><span>' + (i < 2 ? ['42:10', '55:36'][i] : 'PDF') + '</span></div>'; }).join('') +
          '</div></div></div>' +
      '<div class="lx-scrim" id="lS"></div>' +
      '<div class="lx-modal" id="lM"><div class="lx-eb">Pay Sharma Physics</div><div class="lx-mamt">₹4,999</div>' +
        '<p class="lx-p">' + TITLE + '</p>' +
        '<div class="lx-pm mt"><span class="on">UPI</span><span>Card</span><span>Netbanking</span></div>' +
        '<div class="lx-in mt" id="lU"><span class="v ph">yourname@upi</span></div>' +
        '<div class="lx-btn acc mt" id="lP">Pay ₹4,999</div></div>';
    setUrl('sharmaphysics.in/courses/jee-physics-mechanics');
    learn.classList.add('on');
    await h.wait(1300);
    var buy = learn.querySelector('#lB');
    var less = learn.querySelectorAll('.lx-less');
    if(mode !== 'compact' && less.length){ await h.move(less[1], 900); await h.wait(400); }
    await h.click(buy, 800);
    learn.querySelector('#lS').classList.add('on'); learn.querySelector('#lM').classList.add('on');
    await h.wait(800);
    var u = learn.querySelector('#lU');
    await h.click(u, 650); h.focus(u);
    await h.type(u.querySelector('.v'), 'rohan.k@upi', null, 55);
    h.focus(null);
    var pb = learn.querySelector('#lP');
    await h.click(pb, 600);
    pb.innerHTML = '<span class="lx-spin"></span>Waiting for UPI approval';
    await h.wait(1500);
    learn.querySelector('#lM').innerHTML =
      '<div class="lx-okw"><div class="lx-okc"><svg class="i" viewBox="0 0 24 24">' + P.check + '</svg></div>' +
      '<h4 class="lx-h4">You’re enrolled, Rohan.</h4><p class="lx-p">' + TITLE + ' is in your library.</p>' +
      '<div class="lx-btn dark mt" style="width:100%">Start lesson 1</div></div>';
    await h.wait(1900);

    /* back in the educator's studio */
    studio('dash', 'studio.allcoaching.in');
    mount(
      '<div class="lx-head"><div><div class="lx-eb">Today</div><h3 class="lx-h">Good evening, Neha.</h3>' +
      '<p class="lx-p">Sharma Physics is live on sharmaphysics.in</p></div><div class="lx-seg"><span>Today</span><span>7d</span><span class="on">30d</span></div></div>' +
      '<div class="lx-kpis">' +
        '<div class="lx-kpi" id="q1"><div class="k">Sales</div><div class="v" id="v1">₹0</div><span class="d" id="d1">no sales yet</span></div>' +
        '<div class="lx-kpi" id="q2"><div class="k">Enrolments</div><div class="v" id="v2">0</div><span class="d" id="d2">—</span></div>' +
        '<div class="lx-kpi acc" id="q3"><div class="k">You keep · 92.5%</div><div class="v" id="v3">₹0</div><span class="d">to your bank, T+3</span></div>' +
        '<div class="lx-kpi" id="q4"><div class="k">Platform fee · 7.5%</div><div class="v" id="v4">₹0</div><span class="d">flat, per sale</span></div>' +
      '</div>' +
      '<div class="lx-dg2"><div class="lx-card lx-chart"><div class="hd"><b>Sales</b><span>sharmaphysics.in</span></div>' +
        '<svg viewBox="0 0 400 180" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="lxGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C58B43" stop-opacity=".28"/><stop offset="1" stop-color="#C58B43" stop-opacity="0"/></linearGradient></defs>' +
        '<line class="gl" x1="0" y1="45" x2="400" y2="45"/><line class="gl" x1="0" y1="90" x2="400" y2="90"/><line class="gl" x1="0" y1="135" x2="400" y2="135"/>' +
        '<path class="ar" d="M0 172 L60 168 L110 150 L160 138 L210 112 L260 96 L310 62 L360 44 L400 22 L400 180 L0 180Z"/>' +
        '<path class="ln" pathLength="1" d="M0 172 L60 168 L110 150 L160 138 L210 112 L260 96 L310 62 L360 44 L400 22"/></svg></div>' +
      '<div class="lx-card lx-ords"><div class="hd"><b>Recent enrolments</b><span class="lx-livep">Live</span></div><div id="oL"><div class="lx-empty">Waiting for your first student</div></div></div></div>'
    );
    await h.wait(1000);
    var ln = q('.lx-chart .ln'), ar = q('.lx-chart .ar'), oL = q('#oL');
    for(var i = 0; i < BUYERS.length; i++){
      var b = BUYERS[i], n = i + 1, prev = i * PRICE, now = n * PRICE;
      if(i === 0) oL.innerHTML = '';
      var row = document.createElement('div'); row.className = 'lx-ord';
      row.innerHTML = '<span class="lx-av">' + b[0] + '</span><div><b>' + b[1] + ' · ' + b[2] + '</b><span>' + TITLE + ' · UPI</span></div><span class="a">+' + inr(PRICE) + '</span>';
      oL.insertBefore(row, oL.firstChild);
      if(oL.children.length > 4) oL.lastChild.remove();
      ['#q1', '#q2', '#q3'].forEach(function(s){ q(s).classList.add('hl'); });
      q('#d1').textContent = '+' + inr(PRICE) + ' just now';
      q('#d2').textContent = '+1 just now';
      q('#v2').textContent = n;
      ln.style.strokeDashoffset = String(1 - n / BUYERS.length); if(n === BUYERS.length) ar.style.opacity = '1';
      if(i === 0) h.toast('New enrolment · ' + inr(PRICE), b[1] + ' bought ' + TITLE, 'bag');
      if(i === BUYERS.length - 1) h.toast(n + ' students enrolled', 'Every sale lands in your studio', 'rupee', true);
      await Promise.all([
        h.count(q('#v1'), prev, now, 900, inr),
        h.count(q('#v3'), prev * .925, now * .925, 900, inr),
        h.count(q('#v4'), prev * .075, now * .075, 900, inr)
      ]);
      await h.wait(i === 0 ? 1100 : 650);
      ['#q1', '#q2', '#q3'].forEach(function(s){ q(s).classList.remove('hl'); });
    }
    await h.wait(1600);
  }

  var SC = [
    {t:12500, run:scPlan, cap:'<b>Choose a plan.</b> Pick the annual plan that fits and pay by UPI or card. It is active the moment the payment clears.'},
    {t:15500, run:scCourse, cap:'<b>Create your course.</b> Name it, upload lessons, set your price and publish. The student preview updates as you type.'},
    {t:10500, run:scDomain, cap:'<b>Connect your domain.</b> Type a domain you own. Verification and the HTTPS certificate are tracked right in the studio.'},
    {t:21000, run:scSell, cap:'<b>Start selling.</b> A student finds the course on your domain and pays by UPI. The sale lands in your studio, with your share shown upfront.'}
  ];

  /* ── chapters / progress ───────────────────────────────── */
  function markCh(k){
    chs.forEach(function(c, j){
      c.classList.toggle('on', j === k); c.classList.toggle('done', j < k);
      c.setAttribute('aria-selected', j === k ? 'true' : 'false');
      bars[j].style.width = j < k ? '100%' : '0%';
    });
    cap.innerHTML = '<span>' + SC[k].cap + '</span>';
  }
  var last = performance.now();
  function loop(now){
    var dt = now - last; last = now;
    if(active && !userPaused && vis){ elapsed += dt; bars[idx].style.width = Math.min(elapsed / est * 100, 99) + '%'; }
    requestAnimationFrame(loop);
  }
  if(!RM) requestAnimationFrame(loop);

  async function play(from, auto){
    var id = ++run, fast = RM;
    resetShell();
    var h = helpers(id, fast);
    try{
      for(var k = from; k < SC.length; k++){
        idx = k; markCh(k); elapsed = 0; est = SC[k].t; active = !fast;
        await SC[k].run(h);
        active = false; bars[k].style.width = '100%';
        if(!auto) return;
      }
      chs.forEach(function(c){ c.classList.remove('on'); c.classList.add('done'); });
      cur.classList.remove('show'); h.hover(null);
      await h.wait(400);
      endCard.classList.add('on');
      await h.wait(9000);
      play(0, true);
    }catch(e){ if(e !== CANCEL) throw e; }
  }

  chs.forEach(function(c, k){
    c.addEventListener('click', function(){ userPaused = false; syncBtn(); play(k, !RM); });
  });
  root.querySelector('.lx-replay').addEventListener('click', function(){ userPaused = false; syncBtn(); play(0, !RM); });
  function syncBtn(){
    playBtn.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
    playBtn.setAttribute('aria-label', userPaused ? 'Play walkthrough' : 'Pause walkthrough');
  }
  playBtn.addEventListener('click', function(){
    if(RM){ play((idx + 1) % SC.length, false); return; }
    userPaused = !userPaused; syncBtn();
  });
  if(RM){ playBtn.setAttribute('aria-label', 'Next step'); }

  var io = new IntersectionObserver(function(es){
    vis = es[0].isIntersecting;
    if(vis && !started){ started = true; play(0, !RM); }
  }, {threshold:.2});
  io.observe(vp);
})();
