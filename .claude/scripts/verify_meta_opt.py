import json, re, glob, os

files = glob.glob('blog/*.html') + glob.glob('blogs/en/*.html') + glob.glob('blogs/hinglish/*.html')
bad_json = []; mojibake = []; long_title = []; no_desc = []; fraunces = []; long_desc = []
total = 0
for f in files:
    nf = f.replace(os.sep, '/')
    if nf.endswith('/index.html'):
        continue
    total += 1
    h = open(f, encoding='utf-8').read()
    for b in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.DOTALL):
        try:
            json.loads(b)
        except Exception as e:
            bad_json.append((os.path.basename(f), str(e)[:60]))
            break
    if 'Â' in h or 'â€' in h or 'Ã¢' in h:
        mojibake.append(os.path.basename(f))
    if 'Fraunces' in h:
        fraunces.append(os.path.basename(f))
    mt = re.search(r'<title>(.*?)</title>', h, re.DOTALL)
    if mt and len(mt.group(1)) > 65:
        long_title.append((os.path.basename(f), len(mt.group(1)), mt.group(1)))
    md = re.search(r'<meta name="description" content="([^"]*)"', h)
    if not md or len(md.group(1)) < 50:
        no_desc.append(os.path.basename(f))
    elif len(md.group(1)) > 175:
        long_desc.append((os.path.basename(f), len(md.group(1))))

print('Total blog files checked:', total)
print('Invalid JSON-LD:', len(bad_json), bad_json[:8])
print('Mojibake files:', len(mojibake), mojibake[:8])
print('Fraunces leftover:', len(fraunces), fraunces[:8])
print('Missing/short description (<50):', len(no_desc), no_desc[:8])
print('Descriptions >175 chars:', len(long_desc), long_desc[:8])
print('Titles >65 chars:', len(long_title))
for t in long_title[:30]:
    print('   ', t[1], '|', t[2])
