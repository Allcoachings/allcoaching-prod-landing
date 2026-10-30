"""Branded replacement covers for legacy posts whose CDN hero image shows outdated pricing claims.

Run:  python .claude/skills/academy-guide-blog/graphics/legacy_covers.py <slug> [<slug> ...]
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/<slug>
The headline comes from the post's <title>; no prices other than the current plan facts appear.
"""
import os, re, sys, html as H
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))


def post_path(slug):
    for d in ('blog', 'blogs/en', 'blogs/hinglish'):
        p = os.path.join(ROOT, d, slug + '.html')
        if os.path.exists(p):
            return d, p
    sys.exit('no post for ' + slug)


def wrap(t, n=19):
    out, cur = [], ''
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out


def cover(slug):
    d, p = post_path(slug)
    src = open(p, encoding='utf-8').read()
    t = H.unescape(re.search(r'<title>(.*?)</title>', src, re.S).group(1))
    t = re.split(r'\s+[|—–]\s+(?=AllCoaching|All Coaching)', t)[0].strip()
    t = re.sub(r'\s*\((19|20)\d\d\)\s*$', '', t)
    # The cover never repeats a "free" claim: there is a 7-day trial, not a free plan.
    t = re.sub(r'\s*\(Free in (19|20)\d\d\)', '', t)
    t = re.sub(r'^Free\s+', '', t)
    t = re.sub(r'\s+Free(?=[:\s(]|$)', '', t)
    t = re.sub(r'\s*\((?:(?:19|20)\d\d\s*)?Guide\)', '', t)
    t = re.sub(r'\s*\b(?:19|20)\d\d\b', '', t)
    t = re.sub(r'\s*[—:–-]\s*$', '', t)
    t = re.sub(r'\s+(?:in|for|of)$', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    rows = wrap(t, 17)
    if len(rows) > 4:
        rows = wrap(t, 24)[:4]
        rows[-1] = rows[-1].rstrip(',:;') + '…' if len(wrap(t, 24)) > 4 else rows[-1]
    size = 76 if len(rows) <= 3 and max(len(r) for r in rows) <= 17 else 64
    rows[-1] = '*' + rows[-1] + '*'
    hing = d == 'blogs/hinglish'
    sub = 'Monthly plans par 0% commission · 7 din free trial' if hing else '0% commission on monthly plans · 7-day free trial'
    checks = (['Apni website, apna domain', 'Apna Android app', 'Courses, tests aur live classes'] if hing
              else ['Your website on your own domain', 'Your own Android app', 'Courses, tests and live classes'])
    b = lockup(72, 60, 1.0)
    y0 = 250
    b += headline(80, y0, rows, size)
    y = y0 + int(size * 1.02) * len(rows) + 24
    b += lines(84, y, [sub], 26, BLUE, weight=600) if 'weight' in lines.__code__.co_varnames else lines(84, y, [sub], 26, BLUE)
    for i, c in enumerate(checks):
        b += check_row(84, y + 70 + i * 54, c, 24)
    b += laptop(900, 210, 560, 'studio-desktop.jpg')
    b += phone(1380, 330, 150, 'studio-mobile.jpg')
    b += text(900, 190, 'Studio preview · sample data', 15, MUTED)
    out = os.path.join(ROOT, 'assets', 'blog', slug)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'cover.svg'), 'w', encoding='utf-8') as f:
        f.write(svg(1600, 900, b, t))
    print('wrote', slug, rows)


if __name__ == '__main__':
    for s in sys.argv[1:]:
        cover(s)
