#!/usr/bin/env python3
"""Write assets/x/footer.html (shared X footer) and append its CSS to assets/x/x.css.
Social icons are taken from the current homepage footer. The registered address line is NOT in the
shared footer: apply_x_header.py adds it on the homepage only (CLAUDE.md rule)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

idx = open('index.html', encoding='utf-8').read()
foot = idx[idx.index('<footer'):idx.index('</footer>') + 9]
soc = re.search(r'<div class="foot-soc">.*?</div>', foot, re.S).group(0).replace('class="foot-soc"', 'class="xft-soc"')
reg = re.search(r'<div class="foot-reg".*?</div>', foot, re.S)
if reg and not os.path.exists('assets/x/footer-reg.html'):
    open('assets/x/footer-reg.html', 'w', encoding='utf-8').write(reg.group(0).replace('class="foot-reg"', 'class="xft-reg"').replace(' style="margin-top:14px;font-size:12px;line-height:1.6;color:rgba(255,255,255,.45)"', '') + '\n')

FOOTER = '''<!-- X FOOTER (source: assets/x/footer.html) -->
<footer class="xft">
  <div class="xft-in">
    <div class="xft-top">
      <div class="xft-brand">
        <a href="/" class="xft-logo" aria-label="AllCoaching home"><img src="/assets/logo/allcoaching-logo.webp?v=20260707" alt="" width="64" height="64" loading="lazy"/><span>AllCoaching</span></a>
        <p>Build your own LMS in a few clicks: your website, your app, your courses and your payments, under your own brand.</p>
        <a class="xft-cta" href="https://studio.allcoaching.in/">Start free trial</a>
        <div class="xft-ct">
          <a href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener">WhatsApp +91 98899 77262</a>
          <a href="mailto:contact@allcoaching.in">contact@allcoaching.in</a>
        </div>
      </div>
      <nav class="xft-cols" aria-label="Footer">
        <div><h4>Product</h4><a href="/features/">All features</a><a href="/pricing">Pricing</a><a href="/start">Get started</a><a href="/vs/">Compare</a><a href="https://studio.allcoaching.in/login">Log in</a></div>
        <div><h4>Features</h4><a href="/features/academy-website">Academy website</a><a href="/features/mobile-app">Your own app</a><a href="/features/courses">Courses</a><a href="/features/test-series">Test series</a><a href="/features/live-classes">Live classes</a><a href="/features/payments">Payments</a></div>
        <div><h4>Resources</h4><a href="/blog/">Blog</a><a href="/tutorials">Studio tutorials</a><a href="/faq">Help and FAQ</a><a href="/press">Press</a><a href="/brand">Brand</a></div>
        <div><h4>Company</h4><a href="/about">About</a><a href="/manifesto">Manifesto</a><a href="/author/amit-ratan">Founder</a><a href="/contact">Contact</a></div>
        <div><h4>Legal</h4><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="/refund-policy">Refund and cancellation</a><a href="/delivery-policy">Delivery policy</a><a href="/educator-agreement">Educator agreement</a></div>
      </nav>
    </div>
    <div class="xft-mid">
      <div class="xft-follow"><span>Follow AllCoaching</span>
        SOCIALS
      </div>
      <div class="xft-apps"><span>Student app</span><a href="https://play.google.com/store/apps/details?id=org.student.allcoaching" target="_blank" rel="noopener">Android</a><a href="https://apps.apple.com/in/app/allcoaching-exam-prep-app/id6758305866" target="_blank" rel="noopener">iOS</a></div>
    </div>
    <div class="xft-bot">
      <div>© <span id="yr">2026</span> AllCoaching Technology · Made in India</div>
      <div class="xft-tag">The Operating System of Education</div>
    </div>
    <!--REG-->
  </div>
</footer>
<!-- /X FOOTER -->
'''.replace('SOCIALS', soc)
open('assets/x/footer.html', 'w', encoding='utf-8').write(FOOTER)

CSS = r'''
/* ---------- shared footer ---------- */
.xft{background:#111;color:rgba(242,242,242,.78);font-family:'Inter',system-ui,sans-serif;font-size:15px;line-height:1.5;border-top:1px solid rgba(255,255,255,.07);position:relative;z-index:3}
.xft *{box-sizing:border-box}
.xft a{color:inherit;text-decoration:none}
.xft-in{max-width:1440px;margin:0 auto;padding:80px 90px 40px}
.xft-top{display:grid;grid-template-columns:1.1fr 2.4fr;gap:72px}
.xft-logo{display:inline-flex;align-items:center;gap:10px;color:#fff}
.xft-logo img{width:34px;height:34px;border-radius:50%}
.xft-logo span{font-family:'Instrument Serif',serif;font-style:italic;font-size:27px;letter-spacing:-.3px}
.xft-brand p{margin-top:18px;max-width:34ch;color:rgba(242,242,242,.6)}
.xft-cta{display:inline-block;margin-top:24px;background:#fff;color:#151515!important;font-weight:600;padding:11px 22px;border-radius:999px;transition:transform .2s}
.xft-cta:hover{transform:translateY(-1px)}
.xft-ct{display:grid;gap:6px;margin-top:22px;font-size:14px}
.xft-ct a:hover,.xft-cols a:hover,.xft-apps a:hover{color:#fff}
.xft-cols{display:grid;grid-template-columns:repeat(5,1fr);gap:28px}
.xft-cols h4{margin:0 0 16px;font-family:'JetBrains Mono',monospace;font-size:11.5px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:#A9B6FF}
.xft-cols a{display:block;padding:5px 0;font-size:14.5px;color:rgba(242,242,242,.72)}
.xft-mid{margin-top:56px;padding-top:28px;border-top:1px solid rgba(255,255,255,.08);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.xft-follow,.xft-apps{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.xft-follow>span,.xft-apps>span{font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:rgba(242,242,242,.45)}
.xft-soc{display:flex;gap:8px;flex-wrap:wrap}
.xft-soc a{width:38px;height:38px;border-radius:12px;background:#1f1f1f;border:1px solid rgba(255,255,255,.08);display:grid;place-items:center;transition:background .2s,transform .2s}
.xft-soc a:hover{background:#2b44ff;transform:translateY(-2px)}
.xft-soc svg{width:17px;height:17px;fill:#f2f2f2}
.xft-apps a{padding:8px 14px;border-radius:10px;background:#1f1f1f;border:1px solid rgba(255,255,255,.08);font-size:14px}
.xft-bot{margin-top:28px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:13px;color:rgba(242,242,242,.45)}
.xft-tag{font-family:'Instrument Serif',serif;font-style:italic;font-size:16px;color:rgba(242,242,242,.6)}
.xft-reg{margin-top:14px;font-size:12px;line-height:1.6;color:rgba(242,242,242,.4)}
.xft-reg a{color:inherit}
@media (max-width:1180px){.xft-in{padding:64px 40px 36px}.xft-top{grid-template-columns:1fr;gap:44px}}
@media (max-width:760px){.xft-in{padding:56px 20px 110px}.xft-cols{grid-template-columns:1fr 1fr;gap:24px 20px}.xft-mid{flex-direction:column;align-items:flex-start}}
'''
c = open('assets/x/x.css', encoding='utf-8').read()
if '/* ---------- shared footer' not in c:
    a = c.index('/* responsive */')
    c = c[:a] + CSS.strip() + '\n\n' + c[a:]
    open('assets/x/x.css', 'w', encoding='utf-8').write(c)
print('footer.html written; css', 'ok')
