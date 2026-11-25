#!/usr/bin/env python3
"""Owner, 2026-11-25: use Shopify's font. Shopify's marketing site uses its own build of Inter
("Shopify-Inter", 96px/300 headlines, tight tracking), so the site moves from Inter Tight to Inter.
Instrument Serif stays for the wordmark, JetBrains Mono for mono, Devanagari fonts for Hindi.
Idempotent: rewrites font links and every 'Inter Tight' reference in HTML, CSS and JS."""
import glob, os, re, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
INTER = 'Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900'


def write(f, n):
    for _ in range(10):
        try:
            open(f, 'w', encoding='utf-8', newline='').write(n)
            return True
        except OSError:
            time.sleep(0.5)
    print('COULD NOT WRITE', f)
    return False


def fix(s):
    s = re.sub(r'Inter\+Tight:(?:ital,)?wght@[0-9.,;]+', INTER, s)
    s = s.replace('Inter Tight', 'Inter')
    # tidy fallbacks that became duplicates
    s = s.replace("'Inter','Inter'", "'Inter'").replace('"Inter","Inter"', '"Inter"').replace("&#x27;Inter&#x27;,&#x27;Inter&#x27;", "&#x27;Inter&#x27;")
    return s


n = 0
files = [f for ext in ('html', 'css', 'js') for f in glob.glob(f'**/*.{ext}', recursive=True)]
for f in files:
    f = f.replace(os.sep, '/')
    if f.startswith(('node_modules/',)) or '/node_modules/' in f:
        continue
    try:
        s = open(f, encoding='utf-8').read()
    except UnicodeDecodeError:
        continue
    t = fix(s)
    if t != s and write(f, t):
        n += 1
print('files changed:', n)
