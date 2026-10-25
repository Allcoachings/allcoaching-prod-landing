"""Refresh the site-wide registrations of rewritten v3 posts (same URL, new content).

Usage: python .claude/scripts/refresh_v3_registrations.py blog/<slug>.html blogs/en/<slug>.html ...

For each post it updates, in place:
  - sitemap.xml: <lastmod>, <image:loc> (new local cover), <image:title>
  - llms.txt: the "- [Title](url): ..." line -> new title + description + key takeaways (plain text)
  - blog/index.html, blogs/index.html, blogs/en/index.html, blogs/hinglish/index.html:
      blog-card image, alt, tag, h3, text, read time; JSON-LD BlogPosting headline and ItemList name
Run build_llms_full.py and build_feed_xml.py afterwards.
"""
import html as H, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDEXES = ['blog/index.html', 'blogs/index.html', 'blogs/en/index.html', 'blogs/hinglish/index.html']
TODAY = '2026-10-24'


def clean(t):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()


def info(path):
    s = open(os.path.join(ROOT, path), encoding='utf-8').read()
    rel = path[:-5]
    slug = rel.split('/')[-1]
    title = H.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    desc = H.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    alt = H.unescape(re.search(r'<meta property="og:image:alt" content="([^"]*)"', s).group(1))
    sec = re.search(r'"articleSection":"([^"]+)"', s)
    rt = re.search(r'<span class="rt">([^<]+)</span>', s)
    keys = re.search(r'<div class="v3-keys" id="tldr">.*?<ul>(.*?)</ul>', s, re.S)
    facts = [clean(x) for x in re.findall(r'<li>(.*?)</li>', keys.group(1), re.S)] if keys else []
    return {'path': path, 'rel': rel, 'slug': slug, 'url': f'https://allcoaching.in/{rel}', 'title': title, 'desc': desc, 'alt': alt,
            'tag': (sec.group(1) if sec else 'Guide') + ' &middot; 2026', 'read': rt.group(1) if rt else '', 'facts': facts,
            'cover_rel': f'/assets/blog/{slug}/cover.webp', 'cover_abs': f'https://allcoaching.in/assets/blog/{slug}/cover.webp'}


def esc(t):
    return H.escape(t, quote=True)


def do_sitemap(p, log):
    f = os.path.join(ROOT, 'sitemap.xml')
    s = open(f, encoding='utf-8').read()
    m = re.search(r'  <url>\n    <loc>' + re.escape(p['url']) + r'</loc>.*?</url>\n', s, re.S)
    if not m:
        log.append('sitemap: NOT FOUND')
        return
    b = m.group(0)
    b2 = re.sub(r'<lastmod>[^<]*</lastmod>', f'<lastmod>{TODAY}T09:00:00+05:30</lastmod>', b)
    b2 = re.sub(r'<image:loc>[^<]*</image:loc>', f'<image:loc>{p["cover_abs"]}</image:loc>', b2)
    b2 = re.sub(r'<image:title>[^<]*</image:title>', f'<image:title>{esc(p["title"])}</image:title>', b2)
    open(f, 'w', encoding='utf-8').write(s.replace(b, b2, 1))
    log.append('sitemap ok')


def do_llms(p, log):
    f = os.path.join(ROOT, 'llms.txt')
    s = open(f, encoding='utf-8').read()
    pat = re.compile(r'^- \[[^\n]*?\]\(' + re.escape(p['url']) + r'\):[^\n]*$', re.M)
    entry = f'- [{p["title"]}]({p["url"]}): {p["desc"]} ' + ' '.join(p['facts']) + ' Updated 24 Oct 2026; competitor figures from official sites with dates.'
    if pat.search(s):
        s = pat.sub(lambda m: entry, s, count=1)
        log.append('llms ok')
    else:
        log.append('llms: NOT FOUND')
    open(f, 'w', encoding='utf-8').write(s)


def do_index(p, idx, log):
    f = os.path.join(ROOT, idx)
    if not os.path.exists(f):
        return
    s = open(f, encoding='utf-8').read()
    href = '/' + p['rel']
    n = 0
    for m in list(re.finditer(r'<a href="' + re.escape(href) + r'" class="blog-card"[^>]*>.*?</a>', s, re.S)):
        card = m.group(0)
        c2 = re.sub(r'aria-label="[^"]*"', f'aria-label="Read: {esc(p["title"])}"', card, count=1)
        c2 = re.sub(r'<img src="[^"]*" alt="[^"]*"', f'<img src="{p["cover_rel"]}" alt="{esc(p["alt"])}"', c2, count=1)
        c2 = re.sub(r'<span class="blog-card-tag">.*?</span>', f'<span class="blog-card-tag">{p["tag"]}</span>', c2, count=1, flags=re.S)
        c2 = re.sub(r'<h3>.*?</h3>', f'<h3>{esc(p["title"])}</h3>', c2, count=1, flags=re.S)
        c2 = re.sub(r'<p>.*?</p>', f'<p>{esc(p["desc"])}</p>', c2, count=1, flags=re.S)
        if p['read']:
            c2 = re.sub(r'<span>\d+ min read</span>', f'<span>{p["read"]}</span>', c2, count=1)
        s = s.replace(card, c2, 1)
        n += 1
    hl = json.dumps(p['title'], ensure_ascii=False)
    s, k1 = re.subn(r'("headline":)"(?:[^"\\]|\\.)*"(,"url":"' + re.escape(p['url']) + r'")', lambda m: m.group(1) + hl + m.group(2), s)
    s, k2 = re.subn(r'("url":"' + re.escape(p['url']) + r'","name":)"(?:[^"\\]|\\.)*"', lambda m: m.group(1) + hl, s)
    open(f, 'w', encoding='utf-8').write(s)
    log.append(f'{idx}: cards {n}, headline {k1}, itemlist {k2}')


def main(paths):
    for path in paths:
        p = info(path)
        log = []
        do_sitemap(p, log)
        do_llms(p, log)
        for idx in INDEXES:
            do_index(p, idx, log)
        print(p['rel'], '|', '; '.join(log))
    for f in INDEXES:
        s = open(os.path.join(ROOT, f), encoding='utf-8').read()
        for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', s, re.S):
            json.loads(x)
    print('index JSON-LD valid')


if __name__ == '__main__':
    main(sys.argv[1:])
