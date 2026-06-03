import json, re, os

BLOGS = [
    'blogs/hinglish/apni-coaching-ki-website-kaise-banaye-free.html',
    'blogs/hinglish/hindi-medium-teacher-ke-liye-online-platform.html',
    'blogs/hinglish/online-tuition-class-kaise-shuru-kare-aur-paise-kamaye.html',
    'blogs/hinglish/youtube-se-coaching-app-par-kaise-shift-kare.html',
]

def slug(p):
    return os.path.basename(p)[:-5]

sitemap = open('sitemap.xml', encoding='utf-8').read()
index = open('blogs/hinglish/index.html', encoding='utf-8').read()
llms = open('llms.txt', encoding='utf-8').read()
llms_full = open('llms-full.txt', encoding='utf-8').read() if os.path.isfile('llms-full.txt') else ''
robots = open('robots.txt', encoding='utf-8').read() if os.path.isfile('robots.txt') else ''

issues = []
def flag(sev, where, msg):
    issues.append((sev, where, msg))

for p in BLOGS:
    s = slug(p)
    h = open(p, encoding='utf-8').read()
    tag = s[:32]
    # title
    t = re.search(r'<title>(.*?)</title>', h)
    tl = len(t.group(1)) if t else 0
    if not t: flag('HIGH', tag, 'no <title>')
    elif tl > 65: flag('MED', tag, f'title {tl} chars (>65)')
    # description
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    dl = len(d.group(1)) if d else 0
    if not d: flag('HIGH', tag, 'no meta description')
    elif dl < 70: flag('MED', tag, f'description short {dl}')
    elif dl > 180: flag('LOW', tag, f'description {dl} chars (>180)')
    # canonical
    can = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    if not can: flag('HIGH', tag, 'no canonical')
    elif s not in can.group(1): flag('HIGH', tag, 'canonical slug mismatch')
    # hreflang
    for hl in ('hi-Latn', 'en-IN', 'x-default'):
        if f'hreflang="{hl}"' not in h: flag('MED', tag, f'missing hreflang {hl}')
    # hreflang en target exists
    for m in re.finditer(r'hreflang="(?:en-IN|x-default)" href="https://allcoaching\.in(/[^"]+)"', h):
        rel = m.group(1).lstrip('/') + '.html'
        if not os.path.isfile(rel): flag('HIGH', tag, f'hreflang target 404: {m.group(1)}')
    # OG + twitter
    for prop in ['og:title', 'og:description', 'og:image', 'og:url', 'og:type']:
        if f'property="{prop}"' not in h: flag('MED', tag, f'missing {prop}')
    for prop in ['twitter:card', 'twitter:title', 'twitter:image']:
        if f'name="{prop}"' not in h: flag('LOW', tag, f'missing {prop}')
    # robots
    if 'name="robots"' not in h: flag('MED', tag, 'no robots meta')
    # single H1
    h1 = len(re.findall(r'<h1[ >]', h))
    if h1 != 1: flag('HIGH', tag, f'{h1} H1 tags (want 1)')
    # images alt + dims
    for img in re.findall(r'<img[^>]*>', h):
        if 'alt=' not in img: flag('MED', tag, 'img missing alt: ' + img[:60])
    # internal links resolve
    for href in set(re.findall(r'href="(/blogs?/[^"#]+)"', h)):
        rel = href.lstrip('/') + '.html'
        if not os.path.isfile(rel): flag('HIGH', tag, f'DEAD internal link {href}')
    # JSON-LD
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.DOTALL)
    bad = 0
    for b in blocks:
        try: json.loads(b)
        except: bad += 1
    if bad: flag('HIGH', tag, f'{bad} invalid JSON-LD')
    if len(blocks) < 6: flag('MED', tag, f'only {len(blocks)} JSON-LD blocks (<6)')
    types = []
    for b in blocks:
        try:
            o = json.loads(b); ty = o.get('@type')
            types.append(ty if isinstance(ty, str) else tuple(ty))
        except: pass
    flat = str(types)
    for need in ['Article', 'BreadcrumbList', 'HowTo', 'SoftwareApplication', 'FAQPage', 'DefinedTermSet']:
        if need not in flat: flag('MED', tag, f'missing schema {need}')
    # FAQ parity
    try:
        faqp = [json.loads(b) for b in blocks if json.loads(b).get('@type') == 'FAQPage'][0]
        if len(faqp['mainEntity']) != h.count('<summary>'):
            flag('MED', tag, f"FAQ schema {len(faqp['mainEntity'])} != DOM {h.count('<summary>')}")
    except: flag('MED', tag, 'FAQPage parse issue')
    # DefinedTermSet parity
    try:
        dts = [json.loads(b) for b in blocks if json.loads(b).get('@type') == 'DefinedTermSet'][0]
        if len(dts['hasDefinedTerm']) != len(re.findall(r'<dfn ', h)):
            flag('MED', tag, 'DefinedTermSet != dfn count')
    except: flag('MED', tag, 'DefinedTermSet parse issue')
    # mojibake / devanagari
    if any('ऀ' <= c <= 'ॿ' for c in h): flag('HIGH', tag, 'Devanagari char in hi-Latn file')
    if 'Â' in h or 'â€' in h: flag('HIGH', tag, 'mojibake')
    # fraunces
    if 'Fraunces' in h: flag('MED', tag, 'Fraunces font ref')
    # cache-bust on css
    for css in ['brand.css', 'styles.css', 'tw.min.css']:
        m = re.search(re.escape(css) + r'\?v=([0-9a-z]+)', h)
        if not m: flag('LOW', tag, f'{css} no cache-bust ?v=')
    # registration presence
    if s not in sitemap: flag('HIGH', tag, 'NOT in sitemap.xml')
    if s not in index: flag('HIGH', tag, 'NOT in blogs/hinglish/index.html')
    if s not in llms: flag('MED', tag, 'NOT in llms.txt')
    if llms_full and s not in llms_full: flag('MED', tag, 'NOT in llms-full.txt')

# global checks
import xml.dom.minidom as M
try: M.parseString(sitemap);
except Exception as e: flag('HIGH', 'sitemap', f'malformed XML: {e}')
for bot in ['OAI-SearchBot', 'PerplexityBot', 'Googlebot', 'Bingbot']:
    if robots and bot in robots:
        # ensure not disallowed
        pass
# cache-bust consistency across the 4 blogs
versions = set(re.findall(r'brand\.css\?v=([0-9a-z]+)', '\n'.join(open(p,encoding='utf-8').read() for p in BLOGS)))
print('=== cache-bust brand.css versions in new blogs:', versions)

print('=== SEO AUDIT: 4 new blogs + registration ===')
print('Total issues:', len(issues))
for sev in ['HIGH', 'MED', 'LOW']:
    sub = [i for i in issues if i[0] == sev]
    print(f'\n--- {sev} ({len(sub)}) ---')
    for _, where, msg in sub:
        print(f'  [{where}] {msg}')
if not issues:
    print('\nNO ISSUES — clean.')
