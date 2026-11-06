"""Extra graphic for /blog/affordable-lms-for-independent-educators (LMS software price in India).

The cover, verdict, prices, cost, switch and before-after graphics come from the shared spec:
  python .claude/skills/academy-guide-blog/scripts/comparison_graphics.py .claude/skills/academy-guide-blog/graphics/specs/affordable-lms-for-independent-educators.json
This script adds the "cost by type" graphic:
  python .claude/skills/academy-guide-blog/graphics/affordable-lms-for-independent-educators.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/affordable-lms-for-independent-educators

Every figure was read from the company's own pricing page on 6 Nov 2026 (sources in the article). No competitor logos.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

SLUG = 'affordable-lms-for-independent-educators'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

ICONS['wrench'] = '<path d="M14.5 6.5a4 4 0 005 5L21 13l-8 8-3-3 8-8-1.5-1.5a4 4 0 01-5-5L14 2z"/>'

TYPES = [
    ('WordPress + LMS plugin', 'wrench', 'Pro plugin from $199 a year', 'Tutor LMS Pro $199, LearnDash $350 (1 site)',
     '+ hosting, domain, gateway, upkeep; app built separately', False),
    ('International SaaS, in US dollars', 'globe', '$29 to $399 a month, billed annually', 'Teachable, Thinkific, Kajabi',
     '+ fee on some plans; branded app is an add-on or top plan', False),
    ('Indian LMS, monthly at 0% per sale', 'home', '₹3,999 to ₹49,999 a month', 'AllCoaching, Learnyst, TagMango Ultimate',
     '+ GST or taxes; payment gateway about 2% per payment', True),
    ('Indian LMS, low fixed fee + % per sale', 'chart', 'No fixed fee up to ₹15,000 a month', '+ 3% to 10% of each sale (Exly, TagMango, AllCoaching yearly)',
     '+ GST; app or custom domain often an add-on', False),
    ('Custom-built app', 'phone', 'Quoted by scope', 'No standard published price',
     '+ Google Play US$25 once, Apple US$99 a year, upkeep', False),
]

W = 1220
RH = 150
H = 210 + len(TYPES) * RH + 100
b = headline(60, 100, ['What an LMS costs, *by type*'], 54)
b += lines(62, 150, ['Published price ranges in India, checked 6 Nov 2026, before GST'], 22)
for i, (t, ic, price, sub, extra, us) in enumerate(TYPES):
    y = 200 + i * RH
    b += white_panel(50, y, 1120, RH - 18, 24)
    if us:
        b += f'<rect x="50" y="{y}" width="1120" height="{RH - 18}" rx="24" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    b += f'<rect x="78" y="{y + 34}" width="64" height="64" rx="18" fill="{BLUE if us else NAVY_TILE}"/>' + icon(ic, 94, y + 50, 32, '#fff', 2)
    b += text(166, y + 52, t, 24, BLUE if us else INK, 800, font=F_HEAD, ls=-0.6)
    b += text(166, y + 86, extra, 17, MUTED)
    b += f'<line x1="700" y1="{y + 26}" x2="700" y2="{y + RH - 44}" stroke="{LINE}" stroke-width="2"/>'
    b += text(726, y + 56, price, 24, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(726, y + 88, sub if len(sub) <= 44 else sub[:sub.rfind(' ', 0, 44)], 17, MUTED)
    if len(sub) > 44:
        b += text(726, y + 110, sub[sub.rfind(' ', 0, 44) + 1:], 17, MUTED)
b += text(60, H - 56, 'Sources: each official pricing page, checked 6 Nov 2026. Taxes extra where stated; AllCoaching + 18% GST.', 16, MUTED)
b += text(60, H - 30, 'Ranges cover published plans only. Gateway charges on student payments are separate unless a page says otherwise.', 16, MUTED)
b += signature(W, H)
with open(os.path.join(OUT, 'cost-by-type.svg'), 'w', encoding='utf-8') as f:
    f.write(svg(W, H, b, 'LMS software price in India by type: WordPress plugin, international SaaS in dollars, Indian LMS monthly at 0%, Indian LMS with a fee per sale, and a custom-built app'))
print('wrote cost-by-type')
