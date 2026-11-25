#!/usr/bin/env python3
"""One-off: add the inner-page kit to assets/x/x.css and convert pricing.html to the X layout
(dark page hero + light content sheet + dark final). Safe to re-run: it skips what is already done."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

KIT = r'''
/* ---------- inner pages: dark page hero + light content sheet + dark final ---------- */
body.xin{background:var(--x-bg)}
.xphero{position:relative;overflow:hidden;background:var(--x-bg);color:#fff;font-family:var(--ui,'Inter',system-ui,sans-serif);padding:88px 0 150px;line-height:1.5}
.xphero:before{content:"";position:absolute;inset:0;background:radial-gradient(52% 70% at 82% 30%,rgba(43,68,255,.42),transparent 70%),radial-gradient(40% 55% at 6% 100%,rgba(43,68,255,.2),transparent 70%);pointer-events:none}
.xphero:after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:88px 88px;-webkit-mask-image:linear-gradient(180deg,#000,transparent 85%);mask-image:linear-gradient(180deg,#000,transparent 85%);pointer-events:none}
.xphero .xw{position:relative;z-index:1;display:grid;grid-template-columns:1.05fr .95fr;gap:64px;align-items:center}
.xphero.solo .xw{grid-template-columns:1fr}
.xphero.solo .tx{max-width:980px}
.xphero.center{text-align:center}.xphero.center .tx{margin:0 auto}.xphero.center .sub{margin-left:auto;margin-right:auto}.xphero.center .xcta,.xphero.center .xnote{justify-content:center}
.xphero h1{font-size:clamp(40px,5.2vw,80px);font-weight:300;letter-spacing:-.035em;line-height:1.04;color:#fff;margin:0}
.xphero h1 b,.xphero h1 .bd,.xphero h1 strong{font-weight:700}
.xphero .xh-eye{margin-bottom:22px}
.xphero .sub{margin-top:26px;font-size:clamp(17px,1.35vw,20px);line-height:1.55;color:var(--x-soft);max-width:60ch}
.xphero .sub a{color:#fff}
.xcta{margin-top:36px;display:flex;flex-wrap:wrap;gap:14px}
.xphero .xnote{margin-top:22px;font-size:14px;color:var(--x-dim);display:flex;gap:18px;flex-wrap:wrap}
.xphero .xnote span:before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:#22C55E;margin-right:8px;transform:translateY(-2px)}
.xphero .vis{position:relative}
.xphero .vis .xframe{transform:perspective(1800px) rotateY(-7deg) rotateX(2deg);transform-origin:left center}
.xphero .vis .xphone{position:absolute;right:-2%;bottom:-12%;font-size:clamp(6px,.6vw,8.4px)}
.xphero .meta{margin-top:22px;font-family:var(--mono,'JetBrains Mono','IBM Plex Mono',monospace);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--x-dim)}
.xkpis{position:relative;z-index:1;display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:64px;border-top:1px solid var(--x-line)}
.xkpis>div{padding:26px 28px 26px 0}
.xkpis>div+div{padding-left:28px;border-left:1px solid var(--x-line)}
.xkpis b{display:block;font-size:clamp(30px,3.2vw,48px);font-weight:300;letter-spacing:-.03em;color:#fff;line-height:1.05}
.xkpis small{display:block;font-family:var(--mono,'JetBrains Mono','IBM Plex Mono',monospace);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--x-blue-l);margin-bottom:10px}
.xkpis span{display:block;margin-top:8px;font-size:15px;color:var(--x-dim);line-height:1.45}
.xin .xlight{min-height:40vh}
.xin .xlight>section:first-child,.xin .xlight>div:first-child{padding-top:96px}
.xfinal.plain .xw{padding-top:120px;padding-bottom:120px}
.xfinal p.xlead{max-width:52ch}
@media (max-width:980px){.xphero{padding:56px 0 110px}.xphero .xw{grid-template-columns:1fr;gap:44px}.xphero .vis .xframe{transform:none}.xkpis{grid-template-columns:1fr;margin-top:44px}.xkpis>div,.xkpis>div+div{padding:20px 0;border-left:0;border-bottom:1px solid var(--x-line)}.xin .xlight>section:first-child,.xin .xlight>div:first-child{padding-top:64px}}
'''

p = 'assets/x/x.css'
s = open(p, encoding='utf-8').read()
if 'body.xin' not in s:
    a = s.index('/* responsive */')
    s = s[:a] + KIT.strip() + '\n\n' + s[a:]
    s = s.replace(".xhero .xcta{margin-top:40px;display:flex;flex-wrap:wrap;gap:14px}", ".xhero .xcta{margin-top:40px}")
    s = s.replace(".xhero .xcta .xbtn{flex:1 1 100%;justify-content:center}", ".xhero .xcta .xbtn,.xphero .xcta .xbtn{flex:1 1 100%;justify-content:center}")
    open(p, 'w', encoding='utf-8').write(s)
    print('kit added')

PHONE = open('assets/x/phone.html', encoding='utf-8').read().split('\n', 1)[1].strip()

HERO = '''<section class="xphero" id="top">
  <div class="xw">
    <div class="tx">
      <div class="xh-eye">Pricing · 0% commission plans from ₹3,999/month</div>
      <h1>Sign up. Upload.<br/><span class="bd">Start selling.</span></h1>
      <p class="sub">AllCoaching works the way Shopify works for an online store: sign up, choose a plan, upload your course, connect your domain and start selling. Unlimited YouTube video and live classes, your own white-label Android app, themes, plugins and marketing tools come with every plan; the iOS app comes with Growth and Pro, after 30 days. Pay monthly and keep 100% of every sale, or pay yearly with a small fee per sale. Try it all free for 7 days.</p>
      <div class="xcta">
        <a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start 7-day free trial</a>
        <a href="#plans" class="xbtn xbtn-o">See the plans</a>
      </div>
      <div class="xnote"><span>No card needed</span><span>No setup fee</span><span>No sales call</span></div>
    </div>
    <div class="vis">
      <div class="xframe"><img src="/assets/x/a-course.webp" alt="A course page on an AllCoaching academy with its price, Enroll now button and what the course includes" width="1600" height="900" fetchpriority="high"/></div>
      @@PHONE@@
    </div>
  </div>
  <div class="xw" style="display:block">
    <div class="xkpis" aria-label="How the free trial works">
      <div><small>Today</small><b>Start free</b><span>Sign up with Google, no card</span></div>
      <div><small>Days 1–7</small><b>Build &amp; brand</b><span>Add courses, connect your domain</span></div>
      <div><small>Day 7</small><b>Pick a plan</b><span>₹3,999/month at 0%, or ₹6,999/year, + GST</span></div>
    </div>
    <div class="xkpis" style="margin-top:0">
      <div><b>500+</b><span>educators already selling</span></div>
      <div><b>0%</b><span>commission on monthly plans</span></div>
      <div><b>Unlimited</b><span>YouTube video &amp; live classes</span></div>
    </div>
  </div>
</section>
<div class="xlight">
'''.replace('@@PHONE@@', PHONE.replace('IMG', '/assets/x/m-courses.webp').replace('ALT', 'Courses on an academy, on a phone'))

FINAL = '''</div>
<section class="xfinal plain">
  <div class="xw">
    <h2 class="xd" style="font-size:clamp(44px,6vw,96px);max-width:13ch">Build your LMS <b>tonight.</b></h2>
    <p class="xlead">Drag and drop your academy, put your brand on it and start selling. Free for 7 days.</p>
    <div class="xcta"><a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start 7-day free trial</a><a class="xbtn xbtn-o" href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
    <p class="xlead" style="font-size:14px;color:rgba(255,255,255,.52)">7 days free, then 0% commission from ₹3,999 a month, or from ₹6,999 a year · Prices exclude GST</p>
  </div>
</section>
'''

p = 'pricing.html'
s = open(p, encoding='utf-8').read()
if '<section class="px-hero' in s:
    a = s.index('<section class="px-hero'); b = s.index('</section>', a) + 10
    s = s[:a] + HERO + s[b:]
    a = s.index('<section class="px-final'); b = s.index('</section>', a) + 10
    s = s[:a] + FINAL + s[b:]
    s = s.replace('<body>', '<body class="xpage xin">', 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('pricing converted')
