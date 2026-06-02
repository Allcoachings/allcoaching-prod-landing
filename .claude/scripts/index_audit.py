"""Deep audit for index.html — structure, dead/broken CSS, JS DOM refs, links, images, SEO."""
import re, os, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FP = os.path.join(ROOT, 'index.html')
c = open(FP, encoding='utf-8').read()

def head(t): print('\n' + '='*70 + '\n' + t + '\n' + '='*70)

# split style / script / body
styles = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL))
scripts = '\n'.join(re.findall(r'<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', c, re.DOTALL))
# body = everything after </head>
body = c.split('</head>',1)[1] if '</head>' in c else c

# ---------- A. tag balance ----------
head('A. TAG BALANCE (open vs close)')
for tag in ['div','section','header','footer','nav','aside','main','ul','ol','li',
            'details','summary','table','thead','tbody','tr','td','th','a','button',
            'svg','g','defs','symbol','clipPath','figure','figcaption']:
    opens = len(re.findall(r'<'+tag+r'(?:\s|>|/)', body))
    # self-closing count
    selfc = len(re.findall(r'<'+tag+r'\b[^>]*/>', body))
    closes = len(re.findall(r'</'+tag+r'>', body))
    eff_open = opens - selfc
    flag = '' if eff_open == closes else '  <-- MISMATCH'
    if flag or tag in ('div','section','svg'):
        print(f'  {tag:10} open(non-self)={eff_open:4}  close={closes:4}  self-closed={selfc}{flag}')

# ---------- B. duplicate ids ----------
head('B. DUPLICATE IDs')
ids = re.findall(r'\sid="([^"]+)"', c)
seen={}; dups={}
for i in ids:
    seen[i]=seen.get(i,0)+1
for i,n in seen.items():
    if n>1: dups[i]=n
print('  total id attrs:', len(ids), '| unique:', len(seen))
print('  duplicates:', dups if dups else 'none')

# ---------- C. internal anchors ----------
head('C. INTERNAL ANCHORS (href="#id") -> target exists?')
anchors = set(re.findall(r'href="#([^"]+)"', c))
idset = set(seen.keys())
for a in sorted(anchors):
    if a in ('','top'):
        ok = a=='top' and 'top' in idset or a==''
    ok = a in idset or a=='top' and 'top' in idset
    if a not in idset and a!='':
        print(f'  MISSING target: #{a}')
print('  anchors checked:', len(anchors), '| all targets present:', all(a in idset for a in anchors if a))

# ---------- D. images exist ----------
head('D. IMAGE / ASSET SRC (local files exist?)')
srcs = re.findall(r'(?:src|href)="((?:assets|dist|styles)[^"]*)"', c)
srcs += re.findall(r'<image[^>]*href="(assets[^"]*)"', c)
for s in sorted(set(srcs)):
    p = os.path.join(ROOT, s)
    print(('  OK   ' if os.path.exists(p) else '  MISS ')+s)

# local css/js link/script
for m in re.findall(r'<link[^>]*href="([^"]+\.css)"', c) + re.findall(r'<script[^>]*src="([^"]+\.js)"', c):
    if not m.startswith('http'):
        p=os.path.join(ROOT, m.lstrip('/'))
        print(('  OK   ' if os.path.exists(p) else '  MISS ')+m)

# ---------- E. CSS classes used vs defined ----------
head('E. CSS CLASS USAGE')
defined = set(re.findall(r'\.([A-Za-z][\w-]*)', styles))
# remove things that look like property values? .digits already excluded by [A-Za-z]
used = set()
for cl in re.findall(r'class="([^"]+)"', c):
    for tok in cl.split():
        used.add(tok)
used_not_def = sorted(u for u in used if u not in defined)
def_not_used = sorted(d for d in defined if d not in used)
print('  defined classes:', len(defined), '| used classes:', len(used))
print('\n  USED-BUT-NOT-DEFINED (possible broken styling):')
print('   ', used_not_def if used_not_def else 'none')
print('\n  DEFINED-BUT-NOT-USED (possible dead CSS):')
print('   ', def_not_used if def_not_used else 'none')

# ---------- F. JS DOM refs ----------
head('F. JS DOM REFERENCES exist?')
for fn,pat in [('getElementById', r"getElementById\('([^']+)'\)"),
               ('getElementById', r'getElementById\("([^"]+)"\)')]:
    for tid in re.findall(pat, scripts):
        print(('  OK   ' if tid in idset else '  MISS ')+f'#{tid}')
# querySelector class/id
qs = re.findall(r"querySelector(?:All)?\(['\"]([^'\"]+)['\"]\)", scripts)
for sel in qs:
    # take simple leading token
    print('  QS   ', sel)

# ---------- G. SEO ----------
head('G. SEO / HEAD')
def meta(name, attr='name'):
    m=re.search(r'<meta[^>]*'+attr+'="'+re.escape(name)+r'"[^>]*content="([^"]*)"', c)
    if not m:
        m=re.search(r'<meta[^>]*content="([^"]*)"[^>]*'+attr+'="'+re.escape(name)+'"', c)
    return m.group(1) if m else None
title = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
title = title.group(1).strip() if title else None
desc = meta('description')
print('  <title>:', repr(title), f'({len(title)} chars)' if title else '')
print('  meta description:', f'({len(desc)} chars)' if desc else 'MISSING', '\n     ', repr(desc[:170]) if desc else '')
print('  meta keywords:', 'present' if meta('keywords') else 'absent')
print('  meta robots:', meta('robots'))
print('  meta viewport:', 'present' if meta('viewport') else 'MISSING')
print('  canonical:', (re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"', c) or [None,'MISSING'])[1] if re.search(r'rel="canonical"',c) else 'MISSING')
print('  og:title:', meta('og:title','property'))
print('  og:description:', 'present' if meta('og:description','property') else 'MISSING')
print('  og:image:', meta('og:image','property'))
print('  og:url:', meta('og:url','property'))
print('  og:type:', meta('og:type','property'))
print('  twitter:card:', meta('twitter:card'))
print('  twitter:image:', 'present' if meta('twitter:image') else 'absent')
m=re.search(r'<html[^>]*lang="([^"]+)"', c); print('  html lang:', m.group(1) if m else 'MISSING')
h1=re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
print('  H1 count:', len(h1), '->', [re.sub(r'<[^>]+>','',x).strip()[:60] for x in h1])
# heading order
heads=re.findall(r'<h([1-6])\b', c)
print('  heading sequence:', ''.join(heads))
# imgs missing alt
imgs=re.findall(r'<img\b[^>]*>', c)
noalt=[i for i in imgs if 'alt=' not in i]
emptyalt=[i for i in imgs if re.search(r'alt=""',i)]
print('  <img> total:', len(imgs), '| missing alt attr:', len(noalt), '| alt="" (decorative):', len(emptyalt))
for i in noalt: print('     NO ALT:', i[:90])

# ---------- H. JSON-LD ----------
head('H. JSON-LD')
blocks=re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', c, re.DOTALL)
for i,b in enumerate(blocks):
    try:
        d=json.loads(b); t=d.get('@type','?')
        print(f'  [{i}] valid  @type={t}')
    except Exception as e:
        print(f'  [{i}] INVALID JSON: {e}')

# ---------- I. misc red flags ----------
head('I. MISC')
print('  inline style="" count:', len(re.findall(r'style="', c)))
print('  TODO/FIXME/XXX:', len(re.findall(r'TODO|FIXME|XXX', c)))
print('  [REPLACE] markers:', c.count('[REPLACE]'))
print('  target=_blank w/o rel=noopener:',
      len([m for m in re.findall(r'<a\b[^>]*target="_blank"[^>]*>', c) if 'noopener' not in m]))
print('  http:// (insecure) refs:', len(re.findall(r'http://(?!www\.w3\.org)', c)))
print('  empty href="#":', len(re.findall(r'href="#"', c)))
