# -*- coding: utf-8 -*-
"""Apply the confirmed brand-audit fixes to press.html. Idempotent-ish (asserts each
replacement applies once). Run: python .claude/scripts/fix_press_brand.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.join(ROOT, 'press.html')
c = open(p, encoding='utf-8').read()

REPL = [
    # 1. mono uppercase running sentence -> Inter Tight caption
    ("font-family:'JetBrains Mono',monospace; font-size:10.5px; letter-spacing:.14em; font-weight:700; color:#8C8378; text-transform:uppercase; margin-top:1.1rem;\">Wordmark set",
     "font-family:'Inter Tight',sans-serif; font-size:13px; font-weight:400; color:#8C8378; margin-top:1.1rem; line-height:1.6;\">Wordmark set"),
    # 2. semantic green used decoratively on WhatsApp icon -> inherit button colour
    ('<svg class="w-5 h-5" style="color:#2F8F4E;"><use href="#i-whatsapp"/></svg>',
     '<svg class="w-5 h-5"><use href="#i-whatsapp"/></svg>'),
    # 3. off-palette cream #FBF6EA -> #F6F2EA
    ('background:linear-gradient(180deg,#FBF6EA,#F5E8D2);',
     'background:linear-gradient(180deg,#F6F2EA,#F5E8D2);'),
    # 4. off-palette cream #FFF8E8 -> #F6F2EA
    ('background:linear-gradient(180deg,#FFF8E8,#FFFFFF);',
     'background:linear-gradient(180deg,#F6F2EA,#FFFFFF);'),
    # 5. off-palette cream #EEE7DA (quote-card gradient) -> #F6F2EA
    ('background:linear-gradient(180deg,#F5F0E8,#EEE7DA);',
     'background:linear-gradient(180deg,#F5F0E8,#F6F2EA);'),
    # 6. off-palette cream #EEE7DA (.bg-tint) -> #F6F2EA
    ('.bg-tint{ background:#EEE7DA; }', '.bg-tint{ background:#F6F2EA; }'),
    # 7. .asset-cta off-palette light ochre + generic ease
    ('background:#15110D; color:#F5D8AE; border-radius:8px;',
     'background:#15110D; color:#F5E8D2; border-radius:8px;'),
    ('transition:all .18s ease; }', 'transition:all .18s cubic-bezier(.22,.85,.25,1); }'),
    # 8. AA contrast: white on ochre hover -> ink-brown (5.68:1)
    ('.asset-cta:hover{ background:#C58B43; color:#FFFFFF; }',
     '.asset-cta:hover{ background:#C58B43; color:#2A1B07; }'),
    # 9. .asset-card generic ease -> brand curve
    ('transition:all .22s ease; }', 'transition:all .22s cubic-bezier(.22,.85,.25,1); }'),
    # 10. mark must never be shadowed -> drop box-shadow on the logo mark img
    ('.logo-tile img{ width:34px; height:34px; border-radius:9px; box-shadow:0 4px 12px rgba(20,17,13,.18); }',
     '.logo-tile img{ width:34px; height:34px; border-radius:9px; }'),
    # 11. .logo-tile generic ease -> brand curve
    ('transition:transform .2s ease, box-shadow .2s ease;',
     'transition:transform .2s cubic-bezier(.22,.85,.25,1), box-shadow .2s cubic-bezier(.22,.85,.25,1);'),
    # 12. off-palette light ochre wordmark on ink tile
    ('.logo-tile.ink .w{ color:#F5D8AE; }', '.logo-tile.ink .w{ color:#F5E8D2; }'),
    # 13. off-palette light ochre label on ink tile
    ('.logo-tile.ink .lab{ color:rgba(245,216,174,.55); }', '.logo-tile.ink .lab{ color:rgba(245,232,210,.6); }'),
    # 14. .tdl generic ease -> brand curve
    ('transition:opacity .2s ease;', 'transition:opacity .2s cubic-bezier(.22,.85,.25,1);'),
    # 15. AA contrast: quote attribution deep ochre -> #8E5F22 on lightened gradient
    ("letter-spacing:.16em; font-weight:700; color:#9C6A2E; text-transform:uppercase; }",
     "letter-spacing:.16em; font-weight:700; color:#8E5F22; text-transform:uppercase; }"),
    # 16. complete the prefers-reduced-motion guard (cards, tiles, tdl, float-y)
    ('@media (prefers-reduced-motion: reduce){ .reveal{ opacity:1; transform:none; transition:none; } }',
     '@media (prefers-reduced-motion: reduce){ .reveal{ opacity:1; transform:none; transition:none; } .asset-card,.logo-tile,.logo-tile .tdl{ transition:none; } .asset-card:hover,.logo-tile:hover{ transform:none; } .float-y{ animation:none; } }'),
]

missing = []
for old, new in REPL:
    n = c.count(old)
    if n == 1:
        c = c.replace(old, new)
    elif n == 0 and new in c:
        pass  # already applied
    else:
        missing.append((old[:60], n))

open(p, 'w', encoding='utf-8', newline='\n').write(c)
print('applied; unresolved:', missing or 'none')
