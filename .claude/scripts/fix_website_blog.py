import sys
path = 'blogs/hinglish/apni-coaching-ki-website-kaise-banaye-free.html'
h = open(path, encoding='utf-8').read()
fixes = [
    ('deva-1', 'chalता-phirta', 'chalta-phirta', 1),          # chalता -> chalta
    ('deva-2', 'ek aisा asset', 'ek aisa asset', 1),               # aisा -> aisa
    ('creators-prose', '>course creators ke liye SEO strategies</a>',
                       '>online courses ke liye SEO strategies</a>', 1),  # drop prose "creators"; href slug stays
]
ok = True
for label, old, new, exp in fixes:
    n = h.count(old)
    if n != exp:
        print(f'  !! {label}: found {n}, expected {exp}')
        ok = False
        continue
    h = h.replace(old, new)
    print(f'  ok {label}: replaced {n}')
if not ok:
    print('ABORTED'); sys.exit(1)
open(path, 'w', encoding='utf-8', newline='').write(h)
print('written')
