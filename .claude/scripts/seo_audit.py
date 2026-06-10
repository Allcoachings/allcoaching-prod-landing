# -*- coding: utf-8 -*-
"""Site-wide SEO + integrity audit across all root pages and blog pages.
Read-only. Reports actionable issues. Run: python .claude/scripts/seo_audit.py"""
import re, os, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def pages():
    out = [f for f in glob.glob(os.path.join(ROOT, '*.html'))]
    for d in ['blog', 'blogs', 'blogs/en', 'blogs/hi', 'blogs/hinglish', 'author']:
        out += glob.glob(os.path.join(ROOT, d, '*.html'))
    return sorted(set(out))

def rel(p): return os.path.relpath(p, ROOT).replace('\\', '/')

def meta(c, name, attr='name'):
    # NOTE: match the delimiter quote explicitly so apostrophes inside the value
    # (e.g. India's, isn't) don't truncate the captured content.
    pat = (r'<meta[^>]*' + attr + r'=(["\'])' + re.escape(name) +
           r'\1[^>]*content=(["\'])(.*?)\2')
    m = re.search(pat, c, re.I)
    if m:
        return m.group(3)
    pat2 = (r'<meta[^>]*content=(["\'])(.*?)\1[^>]*' + attr +
            r'=(["\'])' + re.escape(name) + r'\3')
    m = re.search(pat2, c, re.I)
    return m.group(2) if m else None

issues = {}
titles = {}; descs = {}
def add(p, msg): issues.setdefault(rel(p), []).append(msg)

P = pages()
for p in P:
    c = open(p, encoding='utf-8').read()
    r = rel(p)
    # title
    mt = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
    t = mt.group(1).strip() if mt else None
    if not t: add(p, 'NO <title>')
    else:
        if len(t) > 70: add(p, f'title {len(t)}c (>70)')
        if len(t) < 15: add(p, f'title {len(t)}c (short)')
        titles.setdefault(t, []).append(r)
    # description
    d = meta(c, 'description')
    if not d: add(p, 'NO meta description')
    else:
        if len(d) > 170: add(p, f'desc {len(d)}c (>170)')
        if len(d) < 70: add(p, f'desc {len(d)}c (short)')
        descs.setdefault(d, []).append(r)
    # canonical
    mc = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', c, re.I)
    if not mc: add(p, 'NO canonical')
    # og + twitter
    for og in ['og:title','og:description','og:image','og:url','og:type']:
        if not meta(c, og, 'property'): add(p, f'NO {og}')
    if not meta(c, 'twitter:card'): add(p, 'NO twitter:card')
    # viewport, lang, robots
    if 'width=device-width' not in c: add(p, 'NO viewport')
    if not re.search(r'<html[^>]*lang=', c): add(p, 'NO html lang')
    if not meta(c, 'robots'): add(p, 'NO meta robots')
    # H1
    h1 = re.findall(r'<h1\b', c)
    if len(h1) == 0: add(p, 'NO H1')
    elif len(h1) > 1: add(p, f'{len(h1)} H1s')
    # imgs missing alt
    imgs = re.findall(r'<img\b[^>]*>', c)
    noalt = [i for i in imgs if not re.search(r'\balt=', i)]
    if noalt: add(p, f'{len(noalt)} img w/o alt')
    # JSON-LD validity
    for b in re.findall(r'<script type=["\']application/ld\+json["\']>\s*(.+?)\s*</script>', c, re.DOTALL):
        try: json.loads(b)
        except Exception as e: add(p, f'INVALID JSON-LD: {str(e)[:40]}')

# duplicates
dup_t = {t: v for t, v in titles.items() if len(v) > 1}
dup_d = {d: v for d, v in descs.items() if len(v) > 1}

print(f'=== SEO AUDIT — {len(P)} pages ===')
print(f'pages with issues: {len(issues)} / {len(P)}')
# tally issue types
from collections import Counter
tally = Counter()
for v in issues.values():
    for m in v: tally[re.sub(r"\d+", "N", m)] += 1
print('\n-- issue tally --')
for k, n in tally.most_common(): print(f'  {n:4}  {k}')
print('\n-- duplicate titles:', len(dup_t), '| duplicate descriptions:', len(dup_d))
for t, v in list(dup_t.items())[:5]: print(f'   TITLE x{len(v)}: {t[:55]} -> {v[:3]}')
for d, v in list(dup_d.items())[:5]: print(f'   DESC x{len(v)}: {d[:45]} -> {v[:3]}')
print('\n-- per-page issues (first 30 pages with issues) --')
for r in sorted(issues)[:30]:
    print(f'  {r}: {issues[r]}')

# sitemap coverage
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT,'sitemap.xml')) else ''
sm_urls = set(re.findall(r'<loc>([^<]+)</loc>', sm))
print(f'\n-- sitemap.xml: {len(sm_urls)} URLs --')
missing_sm = []
for p in P:
    r = rel(p)
    if r.endswith('index.html'): slug = '/' + r[:-10]
    else: slug = '/' + r[:-5]
    slug = slug.rstrip('/') or '/'
    # check if any sitemap url ends with this path
    found = any(u.rstrip('/').endswith(slug.rstrip('/')) for u in sm_urls) or slug == '/'
    if not found and 'author' not in r: missing_sm.append(r)
print('pages possibly NOT in sitemap:', len(missing_sm))
for m in missing_sm[:25]: print('   ', m)
