"""One-off: inject /assets/track.js site-wide (idempotent) and add the GTM
container to the 5 pages that lack it. GTM snippet is copied verbatim from
index.html so it is byte-identical to the rest of the site."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

idx = open('index.html', encoding='utf-8').read()
gtm_head = re.search(r'<script>\(function\(w,d,s,l,i\).*?GTM-T3KFKD3G.*?</script>', idx, re.S).group(0)
gtm_nos = re.search(r'<noscript><iframe src="https://www\.googletagmanager\.com/ns\.html\?id=GTM-T3KFKD3G".*?</noscript>', idx, re.S).group(0)

TRACK = '<script src="/assets/track.js?v=1" defer></script>'
MISSING_GTM = {'about.html', 'contact.html', 'privacy.html', 'terms.html', '404.html'}
SKIP = {'.git', 'node_modules', '.claude'}

n_track = n_gtm = total = 0
for dp, dn, fn in os.walk('.'):
    dn[:] = [d for d in dn if d not in SKIP]
    for f in fn:
        if not f.endswith('.html'):
            continue
        path = os.path.join(dp, f)
        total += 1
        h = open(path, encoding='utf-8').read()
        orig = h
        base = os.path.basename(path)

        if base in MISSING_GTM and 'GTM-T3KFKD3G' not in h:
            if re.search(r'<meta charset="[^"]*"\s*/?>', h):
                h = re.sub(r'(<meta charset="[^"]*"\s*/?>)', lambda m: m.group(1) + '\n' + gtm_head, h, count=1)
            else:
                h = re.sub(r'(<head[^>]*>)', lambda m: m.group(1) + '\n' + gtm_head, h, count=1)
            h = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + gtm_nos, h, count=1)
            n_gtm += 1

        if 'assets/track.js' not in h:
            h = h.replace('</body>', '  ' + TRACK + '\n</body>', 1)
            n_track += 1

        if h != orig:
            open(path, 'w', encoding='utf-8', newline='').write(h)

print(f"  pages scanned:     {total}")
print(f"  track.js injected: {n_track}")
print(f"  GTM added to:      {n_gtm} pages")
