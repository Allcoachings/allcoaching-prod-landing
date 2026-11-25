#!/usr/bin/env python3
"""Switch the X layer from navy to the studio dashboard's charcoal palette (studio dark tokens:
--bg #1b1b1b, --surface #232323, --surface-2 #2a2a2a, --surface-3 #323232, --ink #f2f2f2,
--accent #2b44ff, --accent-fg (dark) #a9b6ff). Idempotent: maps known navy values to charcoal.
Applies to assets/x/x.css and to page-level <style> blocks / inline styles in pages that use the X layer."""
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

MAP = [
    # tokens and bases
    ('--x-bg:#050819', '--x-bg:#151515'), ('--x-bg2:#0A0F3D', '--x-bg2:#1b1b1b'), ('--x-panel:#0B1033', '--x-panel:#1f1f1f'),
    ('--x-line:rgba(255,255,255,.1)', '--x-line:rgba(255,255,255,.09)'),
    ('--x-dim:rgba(255,255,255,.52)', '--x-dim:rgba(242,242,242,.56)'), ('--x-soft:rgba(255,255,255,.72)', '--x-soft:rgba(242,242,242,.78)'),
    ('--x-blue-l:#8FA0FF', '--x-blue-l:#A9B6FF'),
    # navy greys -> charcoal greys
    ('rgba(5,8,25,', 'rgba(21,21,21,'), ('#050819', '#151515'), ('#0A0F3D', '#1b1b1b'), ('#070A26', '#151515'),
    ('#0B1033', '#1f1f1f'), ('#0D1340', '#232323'), ('#101640', '#232323'), ('#0B1240', '#1f1f22'), ('#0A0D1F', '#0c0c0e'),
    ('#070B2A', '#181818'), ('#0C1450', '#1f1f22'), ('#18237A', '#272a3d'), ('#16207A', '#262a3a'), ('#0E1650', '#1f1f22'),
    ('#0A1150', '#1f1f22'), ('#0B1A7A', '#1c1f30'), ('#1428B8', '#2337d8'), ('#3A2A06', '#26283a'),
    ('rgba(11,16,51,.85)', 'rgba(35,35,35,.9)'), ('rgba(3,5,16,', 'rgba(10,10,10,'),
    ('rgba(43,68,255,.42)', 'rgba(43,68,255,.22)'), ('rgba(43,68,255,.2),transparent', 'rgba(43,68,255,.1),transparent'),
    ('rgba(143,160,255,', 'rgba(169,182,255,'), ('#8FA0FF', '#A9B6FF'), ('#C9D1FF', '#D5DBFF'),
]

def remap(s):
    for a, b in MAP:
        s = s.replace(a, b)
    return s

p = 'assets/x/x.css'
s = open(p, encoding='utf-8').read(); n = remap(s)
if n != s:
    open(p, 'w', encoding='utf-8').write(n); print('x.css updated')

changed = 0
for f in glob.glob('**/*.html', recursive=True):
    f = f.replace(os.sep, '/')
    if f.startswith(('dist/', 'node_modules/', 'landing/', 'demo/')) or f == 'brand.html':
        continue
    s = open(f, encoding='utf-8').read()
    if '/assets/x/x.css' not in s:
        continue
    # only touch page <style> blocks and inline style="" attributes, never content text
    def fix_style(m): return m.group(1) + remap(m.group(2)) + m.group(3)
    n = re.sub(r'(<style[^>]*>)(.*?)(</style>)', fix_style, s, flags=re.S)
    n = re.sub(r'(style=")([^"]*)(")', fix_style, n)
    if n != s:
        open(f, 'w', encoding='utf-8', newline='').write(n); changed += 1
print('pages updated:', changed)
