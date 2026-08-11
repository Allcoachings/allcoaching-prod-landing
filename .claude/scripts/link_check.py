# -*- coding: utf-8 -*-
"""Check broken internal links + canonical correctness across all pages. Read-only."""
import re, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Every directory that publishes pages. `vs` and `institute` were missing until
# 2026-08-07, which made real pages such as /vs/classplus report as broken links.
PAGE_DIRS = ['blog', 'blogs', 'blogs/en', 'blogs/hi', 'blogs/hinglish',
             'author', 'vs', 'institute']


def pages():
    out = glob.glob(os.path.join(ROOT, '*.html'))
    for d in PAGE_DIRS:
        out += glob.glob(os.path.join(ROOT, d, '*.html'))
        out += glob.glob(os.path.join(ROOT, d, '*', '*.html'))
    return sorted(set(out))

P = pages()
valid = {'/', '/index.html'}
valid.update('/' + d for d in PAGE_DIRS)
for p in P:
    rp = '/' + os.path.relpath(p, ROOT).replace(os.sep, '/')
    valid.add(rp)            # /about.html
    valid.add(rp[:-5])       # /about
    if rp.endswith('/index.html'):
        valid.add(rp[:-10].rstrip('/'))   # /blog

SKIP_PREFIX = ('/assets', '/dist', '/styles', '/brand', '/manifest', '/sw', '/feed', '/sitemap', '/robots', '/llms')
SKIP_EXT = ('.css', '.js', '.xml', '.txt', '.webmanifest', '.png', '.webp', '.svg', '.ico', '.jpg')

broken = {}; canon_issues = []
for p in P:
    c = open(p, encoding='utf-8').read()
    m = re.search(r'rel="canonical"[^>]*href="([^"]+)"', c)
    can = m.group(1) if m else None
    if can and not can.startswith('https://allcoaching.in'):
        canon_issues.append((os.path.relpath(p, ROOT), can))
    for href in re.findall(r'href="(/[^"#]*)"', c):
        h = href.split('?')[0].split('#')[0].rstrip('/')
        if h == '': h = '/'
        if any(h.startswith(x) for x in SKIP_PREFIX): continue
        if h.endswith(SKIP_EXT): continue
        if h in valid or (h + '.html') in valid or (h + '/index.html') in valid:
            continue
        broken.setdefault(href, set()).add(os.path.basename(p))

print('canonical not on https://allcoaching.in:', canon_issues or 'none')
print('distinct broken internal link targets:', len(broken))
for href, ps in sorted(broken.items()):
    print(f'  {href}   <- {len(ps)} pages e.g. {sorted(ps)[:3]}')
