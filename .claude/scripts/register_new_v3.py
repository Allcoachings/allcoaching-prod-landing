"""Register NEW v3 posts (new URLs) in sitemap.xml, llms.txt and blog/index.html.

Usage: python .claude/scripts/register_new_v3.py blog/<slug>.html [blog/<slug2>.html ...]

Inserts each post at the top of the blog section (sitemap), the English blog list (llms.txt)
and the blog index (card + BlogPosting + ItemList). Idempotent: skips anything already present.
Then run refresh_v3_registrations.py on the same paths, build_llms_full.py and build_feed_xml.py.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refresh_v3_registrations import info, esc, ROOT  # noqa: E402

os.chdir(ROOT)
SITEMAP_ANCHOR = '  <url>\n    <loc>https://allcoaching.in/blog/seo-for-online-academy-beginners-guide</loc>'
LLMS_ANCHOR = '- [Online Academy SEO: The Beginner'
CARD_ANCHOR = '    <!-- Online Academy SEO guide (Oct 24) -->'


def published(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'"datePublished":"(\d{4}-\d{2}-\d{2})', s)
    return m.group(1) if m else '2026-10-25'


def register(path):
    p = info(path)
    url, date = p['url'], published(path)
    log = []

    sm = open('sitemap.xml', encoding='utf-8').read()
    if url + '</loc>' not in sm:
        assert sm.count(SITEMAP_ANCHOR) == 1, 'sitemap anchor'
        block = ("  <url>\n"
                 f"    <loc>{url}</loc>\n"
                 f"    <lastmod>{date}T09:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.95</priority>\n"
                 f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"{url}\" />\n"
                 f"    <image:image>\n      <image:loc>{p['cover_abs']}</image:loc>\n      <image:title>{esc(p['title'])}</image:title>\n    </image:image>\n  </url>\n")
        open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(SITEMAP_ANCHOR, block + SITEMAP_ANCHOR, 1))
        log.append('sitemap added')

    lt = open('llms.txt', encoding='utf-8').read()
    if f"]({url})" not in lt:
        assert lt.count(LLMS_ANCHOR) == 1, 'llms anchor'
        line = f"- [{p['title']}]({url}): {p['desc']} " + ' '.join(p['facts'])
        open('llms.txt', 'w', encoding='utf-8').write(lt.replace(LLMS_ANCHOR, line.strip() + "\n" + LLMS_ANCHOR, 1))
        log.append('llms added')

    h = open('blog/index.html', encoding='utf-8').read()
    if f'/{p["rel"]}" class="blog-card"' not in h:
        bp_anchor = '"blogPost":[\n'
        assert h.count(bp_anchor) == 1
        h = h.replace(bp_anchor, bp_anchor + f'      {{"@type":"BlogPosting","headline":{json.dumps(p["title"], ensure_ascii=False)},"url":"{url}","datePublished":"{date}"}},\n', 1)
        idx = h.find('"@type":"ItemList"')
        m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
        arr = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1)) + 1}', m.group(2))
        new = f'\n      {{"@type":"ListItem","position":1,"url":"{url}","name":{json.dumps(p["title"], ensure_ascii=False)}}},'
        h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + new + arr + m.group(3), 1)
        n = int(re.search(r'"numberOfItems":(\d+),', h).group(1))
        h = h.replace(f'"numberOfItems":{n},', f'"numberOfItems":{n + 1},', 1)
        assert h.count(CARD_ANCHOR) == 1, 'card anchor'
        card = (f'    <!-- {esc(p["title"])} ({date}) -->\n'
                f'    <a href="/{p["rel"]}" class="blog-card" aria-label="Read: {esc(p["title"])}">\n'
                '      <div class="blog-card-img">\n'
                f'        <img src="{p["cover_rel"]}" alt="{esc(p["alt"])}" width="1600" height="900" decoding="async" loading="lazy" />\n'
                '      </div>\n      <div class="blog-card-body">\n'
                f'        <span class="blog-card-tag">{p["tag"]}</span>\n        <h3>{esc(p["title"])}</h3>\n        <p>{esc(p["desc"])}</p>\n'
                f'        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span><span>{p["read"]}</span>\n        </div>\n'
                '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n\n')
        h = h.replace(CARD_ANCHOR, card + CARD_ANCHOR, 1)
        for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S):
            json.loads(x)
        open('blog/index.html', 'w', encoding='utf-8').write(h)
        log.append('index added')
    print(path, '|', ', '.join(log) or 'already registered')


if __name__ == '__main__':
    for a in sys.argv[1:]:
        register(a)
