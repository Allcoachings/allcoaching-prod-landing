# -*- coding: utf-8 -*-
"""Apply the shared index.html header + footer chrome to all root sub-pages.
Idempotent: re-running is safe (gated on id="topbar"). Run:
  python .claude/scripts/apply_chrome.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGES = ['404.html','about.html','contact.html','faq.html','manifesto.html',
         'press.html','pricing.html','privacy.html','terms.html']

WA = ('M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07'
      '-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5'
      '.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57a1.1 1.1 0 00-.8.37c-.27.3-1.04 1.02-1.04 2.48'
      ' 0 1.46 1.07 2.87 1.22 3.07.15.2 2.1 3.2 5.08 4.49.7.3 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.42'
      '.25-.69.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35m-5.42 7.4c-1.76 0-3.49-.47-5.03-1.37l-.36-.22-3.74.99 1-3.65-.24-.38'
      'a9.86 9.86 0 01-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88a9.83 9.83 0 019.88 9.89c0 5.45-4.44 9.88-9.89 9.88m8.41-18.3'
      'A11.82 11.82 0 0012.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 005.69 1.45'
      'c6.55 0 11.89-5.34 11.89-11.89a11.82 11.82 0 00-3.48-8.41z')
YT = 'M23.5 6.2a3 3 0 00-2.1-2.1C19.6 3.6 12 3.6 12 3.6s-7.6 0-9.4.5A3 3 0 00.5 6.2C0 8 0 12 0 12s0 4 .5 5.8a3 3 0 002.1 2.1c1.8.5 9.4.5 9.4.5s7.6 0 9.4-.5a3 3 0 002.1-2.1c.5-1.8.5-5.8.5-5.8s0-4-.5-5.8zM9.6 15.6V8.4l6.3 3.6z'
TG = 'M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.56 8.2-1.86 8.77c-.14.62-.51.77-1.03.48l-2.85-2.1-1.37 1.32c-.15.15-.28.28-.57.28l.2-2.9 5.27-4.77c.23-.2-.05-.32-.36-.12l-6.52 4.1-2.81-.88c-.61-.19-.62-.61.13-.9l10.99-4.24c.51-.19.96.12.78.96z'
IG = 'M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.43.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.43.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 01-1.38-.9 3.7 3.7 0 01-.9-1.38c-.16-.43-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.43-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63a5.8 5.8 0 00-2.1 1.37A5.8 5.8 0 00.63 4.14C.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.31.79.72 1.46 1.37 2.1.64.65 1.31 1.06 2.1 1.37.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56a5.8 5.8 0 002.1-1.37 5.8 5.8 0 001.37-2.1c.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91a5.8 5.8 0 00-1.37-2.1A5.8 5.8 0 0019.86.63c-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0zm0 5.84A6.16 6.16 0 1018.16 12 6.16 6.16 0 0012 5.84zm0 10.16A4 4 0 1116 12a4 4 0 01-4 4zm6.41-11.85a1.44 1.44 0 101.44 1.44 1.44 1.44 0 00-1.44-1.44z'
FB = 'M24 12a12 12 0 10-13.88 11.86v-8.39H7.08V12h3.04V9.36c0-3 1.79-4.67 4.53-4.67 1.31 0 2.68.24 2.68.24v2.95h-1.51c-1.49 0-1.96.93-1.96 1.87V12h3.33l-.53 3.47h-2.8v8.39A12 12 0 0024 12z'
XX = 'M18.244 2h3.308l-7.227 8.26L22.5 22h-6.8l-5.31-6.96L4.3 22H.99l7.73-8.83L1.5 2h6.97l4.8 6.34L18.244 2zm-1.16 18h1.83L7.02 3.9H5.06l12.02 16.1z'

HEADER = '''<header class="topbar" id="topbar">
  <a href="/" class="lockup"><img src="/assets/fevicon.webp" alt="AllCoaching"/><span class="word">AllCoaching</span><span class="dem-tag">Democratizing&nbsp;Education</span></a>
  <nav>
    <a href="/#trap">The trap</a><a href="/#studio">Studio</a><a href="/#students">Students</a><a href="/#calc">Earnings</a><a href="/pricing">Pricing</a><a href="/faq">FAQ</a>
  </nav>
  <div class="actions">
    <a href="https://studio.allcoaching.in/" class="login">Log in</a>
    <a href="https://studio.allcoaching.in/" class="btn btn-accent">Join now</a>
  </div>
  <button class="burger" id="burger" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</header>
<div class="mobnav" id="mobnav"><div class="panel">
  <button class="close" id="mobclose" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  <a href="/#trap">The trap</a><a href="/#studio">Studio</a><a href="/#students">Students</a><a href="/#calc">Earnings</a><a href="/pricing">Pricing</a><a href="/faq">FAQ</a>
  <a href="https://studio.allcoaching.in/" class="btn btn-accent" style="margin-top:14px;">Join now</a>
</div></div>'''

FOOTER = '''<footer>
  <div class="foot-wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="/" class="lockup"><img src="/assets/fevicon.webp" alt="AllCoaching"/><span class="word">AllCoaching</span></a>
        <div class="dem-tag-foot">Democratizing Education</div>
        <div style="font-family:var(--display); font-style:italic; font-size:23px; letter-spacing:-.3px; color:var(--accent-deep); margin:12px 0 0; line-height:1.25;">Reclaiming education for the people who <span style="color:var(--accent-light);">teach it.</span></div>
        <p>This was never about software. It's a quiet revolution for the people who taught us everything &mdash; built so the <em style="font-style:italic;font-family:var(--display);color:var(--accent-deep);">best teacher</em>, not the biggest budget, is the one who gets found.</p>
        <div class="foot-follow">Follow us</div>
        <div class="foot-soc">
          <a class="wa" href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24"><path d="%(WA)s"/></svg></a>
          <a class="yt" href="https://www.youtube.com/@Allcoaching" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="%(YT)s"/></svg></a>
          <a class="tg" href="https://t.me/allcoaching" target="_blank" rel="noopener" aria-label="Telegram"><svg viewBox="0 0 24 24"><path d="%(TG)s"/></svg></a>
          <a class="ig" href="https://www.instagram.com/allcoachings/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="%(IG)s"/></svg></a>
          <a class="fb" href="https://www.facebook.com/allcoaching.in" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="%(FB)s"/></svg></a>
          <a class="x" href="https://x.com/allcoachings" target="_blank" rel="noopener" aria-label="X"><svg viewBox="0 0 24 24"><path d="%(XX)s"/></svg></a>
        </div>
      </div>
      <div class="foot-col"><h4>Product</h4><a href="/#features">Features</a><a href="/#students">Marketplace</a><a href="/#calc">Calculator</a><a href="/pricing">Pricing</a></div>
      <div class="foot-col"><h4>Company</h4><a href="/manifesto">Manifesto</a><a href="/blog/">Blog</a><a href="/about">About</a><a href="/contact">Contact</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a></div>
      <div class="foot-col"><h4>Educators</h4><a href="https://studio.allcoaching.in/">Login</a><a href="https://studio.allcoaching.in/">Join Now</a><a href="/faq">FAQ</a><a href="https://api.whatsapp.com/send/?phone=919889977262">WhatsApp</a></div>
      <div class="foot-col"><h4>Students</h4><a href="https://play.google.com/store/apps/details?id=org.student.allcoaching">Android App</a><a href="/#students">Find Educators</a><a href="https://t.me/allcoaching">Telegram</a></div>
    </div>
    <div class="foot-bottom">
      <div>&copy; <span id="yr">2026</span> AllCoaching Technologies Pvt. Ltd. &middot; Made in India</div>
      <div>The Operating System of Education &middot; One educator at a time.</div>
    </div>
  </div>
</footer>''' % {'WA':WA,'YT':YT,'TG':TG,'IG':IG,'FB':FB,'XX':XX}

PROGRESS = '<div class="progress" id="progress"></div>'

FAB = ('<a href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener" '
       'class="fab-wa" aria-label="Chat on WhatsApp"><svg viewBox="0 0 24 24"><path d="%s"/></svg></a>') % WA

JS = '''<script>
(function(){
  var y=document.getElementById('yr'); if(y) y.textContent=new Date().getFullYear();
  var tb=document.getElementById('topbar'), pr=document.getElementById('progress');
  function onScroll(){ var h=document.documentElement, st=h.scrollTop||document.body.scrollTop, max=h.scrollHeight-h.clientHeight; if(pr) pr.style.width=(max>0?(st/max*100):0)+'%'; if(tb) tb.classList.toggle('scrolled', st>8); }
  document.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  var bg=document.getElementById('burger'), mn=document.getElementById('mobnav'), mc=document.getElementById('mobclose');
  if(bg&&mn) bg.addEventListener('click',function(){mn.classList.add('open');});
  if(mc&&mn) mc.addEventListener('click',function(){mn.classList.remove('open');});
  if(mn) mn.addEventListener('click',function(e){ if(e.target===mn||e.target.tagName==='A') mn.classList.remove('open'); });
})();
</script>'''

CSS_MARKER = '/* @CHROME-SHARED */'
CHROME_CSS = CSS_MARKER + '''
:root{--hair:#E5DDD0;}
.foot-wrap{max-width:1160px; margin:0 auto; padding:0 32px;}
.progress{position:fixed; top:0; left:0; height:3px; width:0%; z-index:100; background:var(--accent-grad); box-shadow:0 0 12px rgba(197,139,67,.6);}
.topbar{position:sticky; top:0; z-index:80; display:flex; align-items:center; gap:16px; padding:13px 32px; background:rgba(250,248,244,.82); -webkit-backdrop-filter:saturate(180%) blur(16px); backdrop-filter:saturate(180%) blur(16px); border-bottom:1px solid var(--line); transition:box-shadow .3s var(--ease);}
.topbar.scrolled{box-shadow:0 10px 30px -16px rgba(38,28,14,.16);}
.topbar .lockup{display:flex; align-items:center; gap:11px; text-decoration:none;}
.topbar .lockup img{width:32px; height:32px; border-radius:9px; box-shadow:0 4px 12px rgba(197,139,67,.28), inset 0 1px 0 rgba(255,255,255,.22);}
.topbar .word{font-family:var(--display); font-style:italic; font-weight:400; font-size:21px; letter-spacing:-0.3px; line-height:1; color:var(--ink-1);}
.topbar nav{display:flex; gap:22px; margin-left:auto; align-items:center;}
.topbar nav a{font-size:13px; font-weight:600; color:var(--ink-2); padding:5px 0; position:relative; text-decoration:none;}
.topbar nav a::after{content:''; position:absolute; left:0; bottom:0; width:0; height:2px; background:var(--accent); transition:width .25s var(--ease);}
.topbar nav a:hover{color:var(--ink-1);} .topbar nav a:hover::after{width:100%;}
.topbar .actions{display:flex; align-items:center; gap:10px; margin-left:8px;}
.topbar .login{font-size:13px; font-weight:600; color:var(--ink-2); text-decoration:none;}
.burger{display:none; margin-left:auto; width:42px; height:42px; border-radius:11px; border:1px solid var(--line-2); background:var(--surface); align-items:center; justify-content:center; cursor:pointer;}
.burger svg{width:20px; height:20px; stroke:var(--ink-1); fill:none;}
.dem-tag,.dem-tag-foot{font-family:var(--mono); font-weight:700; text-transform:uppercase; background:linear-gradient(90deg,#9C6A2E,#E0A95C,#C58B43,#E0A95C,#9C6A2E); background-size:200% auto; -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; color:transparent; animation:demShine 5s linear infinite;}
.dem-tag{display:inline-flex; align-items:center; margin-left:12px; padding-left:13px; border-left:1px solid var(--line-2); font-size:9px; letter-spacing:.16em; white-space:nowrap;}
.dem-tag-foot{display:inline-block; font-size:11px; letter-spacing:.26em; margin-top:12px;}
@keyframes demShine{to{background-position:-200% center;}}
.mobnav{display:none; position:fixed; inset:0; z-index:90; background:rgba(21,17,13,.5);}
.mobnav.open{display:block;}
.mobnav .panel{position:absolute; top:0; right:0; width:min(82vw,340px); height:100%; background:var(--bg); padding:24px; display:flex; flex-direction:column; gap:4px; box-shadow:var(--sh-3);}
.mobnav .panel a{padding:14px 8px; font-size:16px; font-weight:600; border-bottom:1px solid var(--line); color:var(--ink-1); text-decoration:none;}
.mobnav .close{align-self:flex-end; width:42px; height:42px; border-radius:11px; border:1px solid var(--line-2); background:var(--surface); display:grid; place-items:center; margin-bottom:8px; cursor:pointer;}
.mobnav .close svg{width:20px; height:20px; stroke:var(--ink-1); fill:none;}
footer{background:#EEE7DA; border-top:1px solid #E5DDD0; padding:64px 0 32px;}
.foot-grid{display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr; gap:40px;}
.foot-brand .lockup{display:flex; align-items:center; gap:11px; text-decoration:none;}
.foot-brand .lockup img{width:34px; height:34px; border-radius:9px;}
.foot-brand .word{font-family:var(--display); font-style:italic; font-size:24px; color:var(--ink-1);}
.foot-brand p{font-size:13.5px; color:var(--ink-2); line-height:1.65; max-width:300px; margin-top:18px;}
.foot-follow{font-family:var(--mono); font-size:11px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--ink-3); margin:24px 0 12px;}
.foot-soc{display:flex; gap:8px; flex-wrap:wrap;}
.foot-soc a{width:38px; height:38px; border-radius:10px; background:#FFFFFF; border:1px solid #E5DDD0; display:grid; place-items:center; color:var(--ink-2); transition:transform .2s var(--ease), background .2s var(--ease), color .2s var(--ease), border-color .2s var(--ease);}
.foot-soc a svg{width:18px; height:18px; fill:currentColor;}
.foot-soc a:hover{transform:translateY(-3px); color:#fff; border-color:transparent;}
.foot-soc a.wa:hover{background:#25D366;} .foot-soc a.yt:hover{background:#FF0000;} .foot-soc a.tg:hover{background:#229ED9;} .foot-soc a.ig:hover{background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF);} .foot-soc a.fb:hover{background:#1877F2;} .foot-soc a.x:hover{background:#15110D;}
.foot-col h4{font-size:14px; font-weight:600; color:var(--ink-1); margin:0 0 16px;}
.foot-col a{display:block; font-size:13.5px; color:var(--ink-2); padding:5px 0; transition:color .15s var(--ease); text-decoration:none;}
.foot-col a:hover{color:var(--ink-1);}
.foot-bottom{display:flex; justify-content:space-between; gap:12px; margin-top:48px; padding-top:24px; border-top:1px solid #E5DDD0; flex-wrap:wrap; font-size:12px; color:var(--ink-3);}
@media (max-width:980px){.dem-tag{display:none;} .foot-grid{grid-template-columns:repeat(4,1fr); gap:28px 24px;} .foot-brand{grid-column:1 / -1; max-width:560px;}}
@media (max-width:760px){.topbar{padding:11px 20px;} .topbar nav,.topbar .actions{display:none;} .burger{display:flex;} .foot-grid{grid-template-columns:1fr 1fr; gap:26px 20px;}}
'''

def patch_brand():
    p = os.path.join(ROOT, 'brand.css')
    css = open(p, encoding='utf-8').read()
    if CSS_MARKER in css:
        print('brand.css: chrome CSS already present (skip)')
        return
    with open(p, 'a', encoding='utf-8') as fp:
        fp.write('\n\n' + CHROME_CSS)
    print('brand.css: appended chrome CSS')

def process(fn):
    p = os.path.join(ROOT, fn)
    c = open(p, encoding='utf-8').read()
    if 'id="topbar"' in c:
        print(f'{fn}: already has topbar (skip)')
        return
    orig = c
    # 1. replace FIRST <header>...</header> with new header+mobnav
    c, n_h = re.subn(r'<header\b.*?</header>', lambda m: HEADER, c, count=1, flags=re.DOTALL)
    # 2. replace the (single) <footer>...</footer>
    c, n_f = re.subn(r'<footer\b.*?</footer>', lambda m: FOOTER, c, count=1, flags=re.DOTALL)
    # 3. progress bar right after <body ...>
    c, n_b = re.subn(r'(<body\b[^>]*>)', lambda m: m.group(1) + '\n' + PROGRESS, c, count=1)
    # 4. before </body>: fab (only if missing) + chrome JS
    add = (('' if 'fab-wa' in c else FAB + '\n')) + JS + '\n'
    c = c.replace('</body>', add + '</body>', 1)
    if c == orig:
        print(f'{fn}: NO CHANGE (pattern miss!)')
        return
    open(p, 'w', encoding='utf-8', newline='\n').write(c)
    print(f'{fn}: header={n_h} footer={n_f} progress={n_b} fab={"kept" if "fab-wa" in orig else "added"}')

if __name__ == '__main__':
    patch_brand()
    import sys
    targets = sys.argv[1:] or PAGES
    for fn in targets:
        process(fn)
