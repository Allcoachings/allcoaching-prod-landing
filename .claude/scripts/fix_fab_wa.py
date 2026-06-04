import re, glob, os

# Extract the canonical WhatsApp floating button markup from the root index.html (the reference)
idx = open('index.html', encoding='utf-8').read()
m = re.search(r'<a [^>]*class="fab-wa"[^>]*>.*?</a>', idx, re.DOTALL)
assert m, 'index.html fab-wa anchor not found'
canonical = m.group(0)
print('canonical fab-wa (from index.html), length:', len(canonical))

pat = re.compile(r'<a [^>]*class="fab-wa"[^>]*>.*?</a>', re.DOTALL)
files = sorted(glob.glob('**/*.html', recursive=True))
changed = 0; nofab = 0; already = 0; skipped = 0
for f in files:
    nf = f.replace(os.sep, '/')
    if nf == 'index.html':
        skipped += 1
        continue
    h = open(f, encoding='utf-8').read()
    found = pat.findall(h)
    if not found:
        nofab += 1
        continue
    if all(x == canonical for x in found):
        already += 1
        continue
    h2 = pat.sub(lambda _: canonical, h)
    open(f, 'w', encoding='utf-8', newline='').write(h2)
    changed += 1

print(f'changed={changed}, already-canonical={already}, no-fab={nofab}, skipped(root index)={skipped}')

# verify: every changed page now contains the inline path + no pulse-ring span inside fab-wa
sample = ['blog/school-teacher-side-income-from-online-coaching.html', 'blogs/hinglish/youtube-se-coaching-app-par-kaise-shift-kare.html', 'about.html', 'pricing.html', 'blog/index.html']
pathsig = 'M17.47 14.38c-.3-.15-1.76-.87'
for s in sample:
    if os.path.isfile(s):
        h = open(s, encoding='utf-8').read()
        fab = pat.search(h)
        print(f'  {s}: inline-path={pathsig in (fab.group(0) if fab else "")}, has <use>={"<use" in (fab.group(0) if fab else "")}, pulse-ring-in-fab={"pulse-ring" in (fab.group(0) if fab else "")}')
