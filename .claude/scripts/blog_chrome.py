# -*- coding: utf-8 -*-
"""Apply the shared site chrome (simple topbar header + footer + progress + chrome JS)
and CSS cache-bust to all blog files. Reuses the EXACT verified chrome from terms.html.
Idempotent (skips files that already have the topbar). Preserves the article masthead
(<header class="mast-dark">), all JSON-LD, and article content.

Run:  python .claude/scripts/blog_chrome.py            # all blog files
      python .claude/scripts/blog_chrome.py <file ...>  # specific files (test)
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE_V = '20260603a'

# ---- extract canonical chrome from an already-correct root page ----
SRC = os.path.join(ROOT, 'terms.html')
s = open(SRC, encoding='utf-8').read()

def grab(pattern, name):
    m = re.search(pattern, s, re.DOTALL)
    if not m:
        raise SystemExit(f'FATAL: could not extract {name} from terms.html')
    return m.group(0)

HEADER = grab(r'<header class="topbar simple"[^>]*>.*?</header>', 'header')
FOOTER = grab(r'<footer>.*?</footer>', 'footer')
JS     = grab(r"<script>\s*\(function\(\)\{\s*var y=document\.getElementById\('yr'\).*?</script>", 'chrome JS')
PROGRESS = '<div class="progress" id="progress"></div>'

# sanity: chrome must be well-formed and root-relative
assert HEADER.count('<header') == 1 and HEADER.count('</header>') == 1, 'bad header'
assert FOOTER.count('<footer') == 1 and FOOTER.count('</footer>') == 1, 'bad footer'
assert 'id="yr"' in FOOTER and 'foot-wrap' in FOOTER, 'footer missing pieces'
assert "getElementById('topbar')" in JS, 'JS missing topbar'

def cachebust(c):
    for ref in ['brand.css', 'styles.css', 'tw.min.css']:
        # add ?v= only where missing
        c = re.sub(r'(' + re.escape(ref) + r')"', r'\1?v=' + CACHE_V + '"', c)
        # collapse accidental double-version
        c = c.replace('?v=' + CACHE_V + '?v=' + CACHE_V, '?v=' + CACHE_V)
    return c

def process(path):
    c = open(path, encoding='utf-8').read()
    if 'class="topbar simple"' in c or 'id="topbar"' in c:
        return (path, 'skip (already has chrome)')
    orig = c
    # 1. replace FIRST <header> (the nav-shell) -> chrome header. header[1] mast-dark is preserved.
    c, nh = re.subn(r'<header\b.*?</header>', lambda m: HEADER, c, count=1, flags=re.DOTALL)
    # 2. replace the single <footer> -> chrome footer
    c, nf = re.subn(r'<footer\b.*?</footer>', lambda m: FOOTER, c, count=1, flags=re.DOTALL)
    # 3. progress bar right after <body ...> (only if absent)
    if 'id="progress"' not in c:
        c, nb = re.subn(r'(<body\b[^>]*>)', lambda m: m.group(1) + '\n' + PROGRESS, c, count=1)
    # 4. chrome JS before </body> (drives yr/topbar/progress; blogs already have a fab)
    c = c.replace('</body>', JS + '\n</body>', 1)
    # 5. cache-bust CSS links
    c = cachebust(c)
    if nh != 1 or nf != 1:
        return (path, f'WARN header={nh} footer={nf} (NOT written)')
    if c == orig:
        return (path, 'no change')
    open(path, 'w', encoding='utf-8', newline='\n').write(c)
    return (path, f'OK header={nh} footer={nf}')

if __name__ == '__main__':
    targets = sys.argv[1:]
    if not targets:
        for d in ['blog', 'blogs/en', 'blogs/hinglish', 'blogs/hi']:
            targets += sorted(glob.glob(os.path.join(ROOT, d, '*.html')))
    for t in targets:
        p = t if os.path.isabs(t) else os.path.join(ROOT, t)
        path, msg = process(p)
        print(f'{os.path.relpath(path, ROOT):60} {msg}')
