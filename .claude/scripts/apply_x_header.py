#!/usr/bin/env python3
"""Apply the shared X header (assets/x/header.html: dark mega-menu header + mobile drawer) to every
site page. Idempotent: pages that already carry it are refreshed from the source file.
Skips ad landing pages (landing/), theme demos, redirects, dist/ and templates/.
Usage: python .claude/scripts/apply_x_header.py [--check]
"""
import re, glob, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
VER = '44'
HDR = open('assets/x/header.html', encoding='utf-8').read().strip()
FTR = open('assets/x/footer.html', encoding='utf-8').read().strip()
REG = open('assets/x/footer-reg.html', encoding='utf-8').read().strip()
FCUR = re.compile(r'<!-- X FOOTER.*?<!-- /X FOOTER -->', re.S)
FOLD = re.compile(r'<footer[^>]*>.*?</footer>', re.S)
MODAL = ('<div class="xmodal" id="xmodal" role="dialog" aria-modal="true" aria-label="AllCoaching studio tour" hidden>\n'
         '  <div class="box"><button type="button" class="close" aria-label="Close video">×</button>'
         '<video controls playsinline preload="none" poster="/assets/x/tour-poster.webp"></video></div>\n</div>\n')
CSS = '<link rel="stylesheet" href="/assets/x/x.css?v=%s"/>' % VER
JS = '<script src="/assets/x/x.js?v=%s" defer></script>' % VER
OLD = re.compile(r'<header class="(?:topbar simple|v3-head|nav)"[^>]*>.*?</header>', re.S)
CUR = re.compile(r'<!-- X HEADER.*?<!-- /X HEADER -->', re.S)
SKIP = ('dist/', 'templates/', 'assets/', 'node_modules/', 'landing/', 'demo/')

def header_for(path, had_topbar):
    h = HDR
    cls = 'xh over' if path == 'index.html' else 'xh'
    ident = 'topbar' if had_topbar else 'xh'   # legacy inline scripts toggle a class on #topbar
    return h.replace('<header class="xh" id="xh">', '<header class="%s" id="%s">' % (cls, ident), 1)

def process(path, check=False):
    s = open(path, encoding='utf-8').read()
    if 'http-equiv="refresh"' in s[:3000]:
        return 'skip'
    o = s
    had_topbar = "getElementById('topbar')" in s or 'id="topbar"' in s
    new = header_for(path, had_topbar)
    if CUR.search(s):
        s = CUR.sub(lambda m: new, s, 1)
    elif OLD.search(s):
        s = OLD.sub(lambda m: new, s, 1)
    else:
        return 'noheader'
    # shared footer (registered address only on the homepage)
    ftr = FTR.replace('<!--REG-->', '')  # owner 2026-11-25: no registered address in any footer
    if FCUR.search(s):
        s = FCUR.sub(lambda m: ftr, s, 1)
    elif FOLD.search(s):
        s = FOLD.sub(lambda m: ftr, s, 1)
    s = re.sub(r'<link rel="stylesheet" href="/assets/x/x\.css\?v=\d+"/>', CSS, s)
    # owner 2026-11-25: Inter (Shopify's font); any leftover Inter Tight link becomes the Inter variable font
    s = re.sub(r'family=Inter\+Tight:(?:ital,)?wght@[0-9.,;]+', 'family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900', s)
    if '/assets/x/x.css' not in s:
        s = s.replace('</head>', CSS + '\n</head>', 1)
    s = re.sub(r'<script src="/assets/x/x\.js\?v=\d+" defer></script>', JS, s)
    if '/assets/x/x.js' not in s:
        i = s.rindex('</body>')
        s = s[:i] + ('' if 'id="xmodal"' in s else MODAL) + JS + '\n' + s[i:]
    if s != o and not check:
        open(path, 'w', encoding='utf-8', newline='').write(s)
    return 'changed' if s != o else 'same'

if __name__ == '__main__':
    check = '--check' in sys.argv
    files = sorted(f.replace(os.sep, '/') for f in glob.glob('**/*.html', recursive=True))
    files = [f for f in files if not f.startswith(SKIP)]
    out = {}
    for f in files:
        out.setdefault(process(f, check), []).append(f)
    for k, v in out.items():
        print(k, len(v), v[:6] if k != 'changed' else '')
