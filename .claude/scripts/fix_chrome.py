# -*- coding: utf-8 -*-
"""Fix chrome: (1) header/footer wordmark -> Instrument Serif (brand-consistent),
(2) repair the WhatsApp SVG path (a space was dropped), (3) simplify sub-page
header to logo + Log in + Join. Idempotent. Run:
  python .claude/scripts/fix_chrome.py
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGES = ['404.html','about.html','contact.html','faq.html','manifesto.html',
         'press.html','pricing.html','privacy.html','terms.html']

OLD_HEADER = '''<header class="topbar" id="topbar">
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

NEW_HEADER = '''<header class="topbar simple" id="topbar">
  <a href="/" class="lockup"><img src="/assets/fevicon.webp" alt="AllCoaching"/><span class="word">AllCoaching</span><span class="dem-tag">Democratizing&nbsp;Education</span></a>
  <div class="actions">
    <a href="https://studio.allcoaching.in/" class="login">Log in</a>
    <a href="https://studio.allcoaching.in/" class="btn btn-accent">Join now</a>
  </div>
</header>'''

SIMPLE_CSS_MARKER = '/* @CHROME-SIMPLE */'
SIMPLE_CSS = '''
''' + SIMPLE_CSS_MARKER + '''
.topbar.simple .actions{margin-left:auto;}
@media (max-width:760px){.topbar.simple{padding:11px 20px;} .topbar.simple .actions{display:flex;}}
'''

def fix_brand():
    p = os.path.join(ROOT, 'brand.css')
    css = open(p, encoding='utf-8').read()
    before = css
    # wordmark -> Instrument Serif (chrome must match index regardless of --display)
    css = css.replace('.topbar .word{font-family:var(--display);',
                      ".topbar .word{font-family:'Instrument Serif','Times New Roman',serif;")
    css = css.replace('.foot-brand .word{font-family:var(--display);',
                      ".foot-brand .word{font-family:'Instrument Serif','Times New Roman',serif;")
    if SIMPLE_CSS_MARKER not in css:
        css += SIMPLE_CSS
    if css != before:
        open(p, 'w', encoding='utf-8', newline='\n').write(css)
        print('brand.css: wordmark->Instrument Serif + simple-header CSS')
    else:
        print('brand.css: already fixed')

def fix_page(fn):
    p = os.path.join(ROOT, fn)
    c = open(p, encoding='utf-8').read()
    before = c
    notes = []
    # 1. repair WhatsApp path (dropped space)
    if '2.480 1.46 1.07 2.87' in c:
        c = c.replace('2.480 1.46 1.07 2.87', '2.48 0 1.46 1.07 2.87')
        notes.append('whatsapp-path')
    # 2. simplify header (only if the full nav header is present)
    if OLD_HEADER in c:
        c = c.replace(OLD_HEADER, NEW_HEADER)
        notes.append('header-simplified')
    if c != before:
        open(p, 'w', encoding='utf-8', newline='\n').write(c)
        print(f'{fn}: ' + ', '.join(notes))
    else:
        print(f'{fn}: no change')

if __name__ == '__main__':
    fix_brand()
    for fn in PAGES:
        fix_page(fn)
