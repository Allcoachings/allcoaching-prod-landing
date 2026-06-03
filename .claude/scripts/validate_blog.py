import json, re, os, sys

f = sys.argv[1] if len(sys.argv) > 1 else 'blogs/hinglish/apni-coaching-ki-website-kaise-banaye-free.html'
h = open(f, encoding='utf-8').read()
blocks = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.DOTALL)
for b in blocks:
    json.loads(b)
types = [json.loads(b).get('@type') for b in blocks]
print('JSON-LD blocks:', len(blocks), '->', types)
print('Devanagari chars:', len([c for c in h if 'ऀ' <= c <= 'ॿ']))
print('mojibake:', ('Â' in h or 'â' in h), '| Fraunces:', 'Fraunces' in h, '| CRLF:', '\r' in h)
print('"creators":', h.count('creators'))
print('title len:', len(re.search(r'<title>(.*?)</title>', h).group(1)))
faqp = [json.loads(b) for b in blocks if json.loads(b).get('@type') == 'FAQPage'][0]
print('FAQ dom:', h.count('<summary>'), '| schema:', len(faqp['mainEntity']))
dts = [json.loads(b) for b in blocks if json.loads(b).get('@type') == 'DefinedTermSet'][0]
print('dfn dom:', len(re.findall(r'<dfn ', h)), '| DefinedTermSet:', len(dts['hasDefinedTerm']))
print('step-card:', h.count('"step-card'), '| step-num:', h.count('step-num'))
print('cover-shell before main:', 'cover-shell' in h and h.index('cover-shell') < h.index('<main'))
print('cover==og==preload:',
      re.search(r'cover-figure.*?<img src="([^"]+)"', h, re.DOTALL).group(1)
      == re.search(r'og:image" content="([^"]+)"', h).group(1)
      == re.search(r'preload" as="image" href="([^"]+)"', h).group(1))
print('divs balanced:', h.count('<div') == h.count('</div>'))
print('words approx:', len(re.sub(r'<[^>]+>', ' ', h).split()))
hrefs = set(re.findall(r'href="(/blogs?/[^"#]+)"', h))
print('--- internal link existence ---')
bad = 0
for href in sorted(hrefs):
    rel = href.lstrip('/') + '.html'
    exists = os.path.isfile(rel)
    if not exists:
        bad += 1
    print(('OK  ' if exists else 'DEAD'), href)
print('DEAD links:', bad)
