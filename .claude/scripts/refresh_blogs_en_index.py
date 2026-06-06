import re, glob, html, os

IDX = 'blogs/en/index.html'
H = open(IDX, encoding='utf-8').read()

m_bp = re.search(r'"blogPost":\[(.*?)\]\}', H, re.DOTALL)
existing = set(re.findall(r'"url":"(https://allcoaching\.in/[^"]+)"', m_bp.group(1)))
print('existing blogPost entries:', len(existing))

def date_of(fp):
    s = open(fp, encoding='utf-8').read()
    mm = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"', s)
    return mm.group(1) if mm else '0000-00-00'

posts = []
for folder in ['blog', 'blogs/en']:  # English posts only
    for fp in sorted(glob.glob(folder + '/*.html')):
        fp2 = fp.replace('\\', '/')
        if fp2.endswith('/index.html'):
            continue
        slug = fp2.split('/')[-1][:-5]
        urlpath = '/' + folder + '/' + slug
        posts.append({'folder': folder, 'slug': slug, 'urlpath': urlpath,
                      'url': 'https://allcoaching.in' + urlpath, 'date': date_of(fp2)})
print('total English posts:', len(posts))

missing = [p for p in posts if p['url'] not in existing]
missing.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
print('MISSING (newest-first):', len(missing))
for p in missing:
    print('  ', p['date'], p['urlpath'])

SRC = {'blog': 'blog/index.html', 'blogs/en': 'blogs/en/index.html'}
cache = {f: open(f, encoding='utf-8').read() for f in set(SRC.values())}
cards, bp_entries = [], []
for p in missing:
    src = cache[SRC[p['folder']]]
    cm = re.search(r'<a href="%s" class="blog-card".*?</a>' % re.escape(p['urlpath']), src, re.DOTALL)
    assert cm, 'NO CARD FOUND for ' + p['urlpath']
    card = cm.group(0).strip()
    h3 = re.search(r'<h3>(.*?)</h3>', card, re.DOTALL).group(1)
    headline = html.unescape(re.sub(r'<[^>]+>', '', h3)).strip().replace('\\', '\\\\').replace('"', '\\"')
    cards.append('    ' + card)
    bp_entries.append('{"@type":"BlogPosting","headline":"%s","url":"%s","datePublished":"%s","inLanguage":"en-IN"}'
                      % (headline, p['url'], p['date']))

grid_open = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert H.count(grid_open) == 1
H = H.replace(grid_open, grid_open + '\n' + '\n\n'.join(cards) + '\n\n', 1)
bp_open = '"blogPost":['
assert H.count(bp_open) == 1
H = H.replace(bp_open, bp_open + ','.join(bp_entries) + ',', 1)
H = re.sub(r'("dateModified":")\d{4}-\d{2}-\d{2}(")', r'\g<1>2026-06-06\g<2>', H, count=1)
open(IDX, 'w', encoding='utf-8', newline='').write(H)
print('WROTE. cards:', H.count('class="blog-card"'), '| blogPost:', H.count('"@type":"BlogPosting"'))
