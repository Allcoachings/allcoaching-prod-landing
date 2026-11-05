"""Graphics for /blog/best-platform-to-sell-online-courses-in-india.

Run:  python .claude/skills/academy-guide-blog/graphics/best-platform-to-sell-online-courses-in-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/best-platform-to-sell-online-courses-in-india

Every competitor figure was read from the company's own pricing page on 5 Nov 2026 (sources in the article).
No competitor logos are drawn; platforms are shown by name. Cost bars are illustrative, before GST and gateway charges.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa
from comparison_graphics import inr  # noqa

SLUG = 'best-platform-to-sell-online-courses-in-india'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

ICONS['store'] = '<path d="M3 9l2-5h14l2 5"/><path d="M4 9v11h16V9"/><path d="M3 9a3 3 0 006 0 3 3 0 006 0 3 3 0 006 0"/><path d="M10 20v-5h4v5"/>'
ICONS['wrench'] = '<path d="M14.5 6.5a4 4 0 005 5L21 13l-8 8-3-3 8-8-1.5-1.5a4 4 0 01-5-5L14 2z"/>'
ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'
ICONS['rupee'] = '<path d="M7 4h10M7 8.5h10M7 4c5 0 7 1.5 7 4.5S12 13 7 13l8 8"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def chip(cx, y, label, kind, w=200):
    """Ownership chip: you | platform | shared."""
    col = {'you': BLUE, 'platform': '#8A90A2', 'shared': '#B7791F'}[kind]
    fill = {'you': BLUE_TINT, 'platform': '#F1F2F6', 'shared': '#FBF3E4'}[kind]
    return (f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="44" rx="22" fill="{fill}" stroke="{col}" stroke-width="2"/>' +
            text(cx, y + 29, label, 18, col, 700, 'middle', F_HEAD))


TYPES = [('Marketplace', 'Udemy-style', 'store'),
         ('Course-selling app', 'Classplus, Graphy, Exly', 'phone'),
         ('Own-academy LMS', 'AllCoaching, Learnyst, Edmingle', 'home'),
         ('DIY stack', 'WordPress + plugin, Teachable', 'wrench')]

# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += eyebrow(80, 236, 'Payments & selling · checked 5 Nov 2026')
b += headline(80, 320, ['Best platform to', '*sell online courses*', 'in India'], 70)
b += lines(84, 548, ['4 kinds of platform, 9 options priced,', 'and who owns your students in each'], 25, MUTED)
b += check_row(84, 672, 'Price and fee per sale side by side', 24)
b += check_row(84, 728, 'Yearly cost at ₹2 lakh and ₹10 lakh (illustrative)', 24)
b += check_row(84, 784, 'Which type fits which educator', 24)
b += white_panel(930, 120, 600, 660, 32, big=True)
b += eyebrow(970, 182, 'Where you can sell', MUTED)
for i, (t, s, ic) in enumerate(TYPES):
    y = 214 + i * 136
    us = i == 2
    b += f'<rect x="960" y="{y}" width="540" height="116" rx="28" fill="{BLUE_TINT if us else "#F5F6FA"}"{" stroke=" + chr(34) + BLUE + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34) if us else ""}/>'
    b += f'<rect x="984" y="{y + 28}" width="60" height="60" rx="16" fill="{BLUE if us else NAVY_TILE}"/>' + icon(ic, 1000, y + 44, 28, '#fff', 2)
    b += text(1066, y + 52, t, 28, BLUE if us else INK, 800, font=F_HEAD, ls=-0.8)
    b += text(1066, y + 84, s, 19, MUTED)
save('cover', svg(1600, 900, b, 'Best platform to sell online courses in India: marketplace, course-selling app, own-academy LMS and DIY stack compared'))

# 2. who owns what ---------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Who owns *what?*'], 54)
b += lines(62, 150, ['The four kinds of platform, by who usually holds each piece'], 22)
cols = [('Students', 520), ('Brand', 720), ('Price & payout', 900), ('Data', 1080)]
b += white_panel(40, 190, 1140, 740, 28, big=True)
for t, cx in cols:
    b += text(cx, 240, t, 21, INK, 800, 'middle', F_HEAD, -0.4)
rows = [
    ('Marketplace', 'Udemy-style', 'store', [('Platform', 'platform'), ('Platform', 'platform'), ('Platform rules', 'platform'), ('Platform', 'platform')]),
    ('Course-selling app', 'Classplus, Graphy, Exly', 'phone', [('You', 'you'), ('Shared', 'shared'), ('You + fee', 'shared'), ('Varies', 'shared')]),
    ('Own-academy LMS', 'AllCoaching, Learnyst', 'home', [('You', 'you'), ('You', 'you'), ('You', 'you'), ('You', 'you')]),
    ('DIY stack', 'WordPress, Teachable', 'wrench', [('You', 'you'), ('You', 'you'), ('You', 'you'), ('You (you fix it)', 'you')]),
]
for i, (t, s, ic, vals) in enumerate(rows):
    y = 276 + i * 160
    if i % 2 == 0:
        b += f'<rect x="60" y="{y}" width="1100" height="144" rx="18" fill="#F7F8FC"/>'
    us = i == 2
    b += f'<rect x="84" y="{y + 42}" width="60" height="60" rx="16" fill="{BLUE if us else NAVY_TILE}"/>' + icon(ic, 100, y + 58, 28, '#fff', 2)
    b += text(164, y + 68, t, 25, BLUE if us else INK, 800, font=F_HEAD, ls=-0.6)
    b += text(164, y + 98, s, 17, MUTED)
    for (lab, cx), (v, k) in zip(cols, vals):
        b += chip(cx, y + 50, v, k, 168)
leg = [('you', 'You hold it'), ('shared', 'Shared or depends on plan'), ('platform', 'Platform holds it')]
lx = 60
for k, lab in leg:
    b += chip(lx + 22, 954, '', k, 44) + text(lx + 56, 983, lab, 18, INK, 500)
    lx += 90 + len(lab) * 9
b += text(60, 1030, 'General pattern, not a promise for every plan. Check each platform\'s terms.', 16, MUTED)
b += signature(W, H)
save('who-owns-what', svg(W, H, b, 'Who owns the students, brand, price and payout, and data on a marketplace, a course-selling app, an own-academy LMS and a DIY stack'))

# 3. price + fee side by side ----------------------------------------------------
W = 1220
rows = [
    ('Marketplace', [('Udemy', 'No plan fee', 'Revenue share set by Udemy')]),
    ('Course-selling app', [('Classplus', '₹29,999 for 1 year', 'Not stated'),
                            ('Exly', 'Starter, no fixed fee', '10% per sale'),
                            ('Exly Pro', '₹30,000 a year', '6% per sale')]),
    ('Own-academy LMS', [('AllCoaching', '₹3,999 a month', '0% (monthly)'),
                         ('AllCoaching', '₹6,999 a year', '10% (yearly)'),
                         ('Learnyst', '₹8,999 a month', '0% listed'),
                         ('Edmingle', '₹7,499 a month, yearly', 'Not stated')]),
    ('DIY stack', [('Teachable', '$29 a month, yearly', '7.5% (Starter)'),
                   ('Thinkific', '$82 a month, yearly', 'Payment fees'),
                   ('Tutor LMS', '$199 a year + hosting', 'Gateway fees')]),
]
n = sum(len(r) for _, r in rows)
H = 230 + n * 66 + len(rows) * 50 + 110
b = headline(60, 100, ['Price *and* fee per sale'], 54)
b += lines(62, 150, ['Lowest listed plan on each official page, with its fee next to it'], 22)
b += text(380, 218, 'PRICE AS LISTED', 15, MUTED, 600, font=F_MONO, ls=1.6) + text(800, 218, 'FEE ON EACH SALE', 15, MUTED, 600, font=F_MONO, ls=1.6)
y = 240
for grp, items in rows:
    b += text(60, y + 30, grp.upper(), 15, BLUE, 600, font=F_MONO, ls=1.6)
    y += 46
    for name, price, fee in items:
        us = name == 'AllCoaching'
        b += f'<rect x="50" y="{y}" width="1120" height="56" rx="16" fill="{BLUE_TINT if us else "#fff"}"{" stroke=" + chr(34) + BLUE + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34) if us else ""}/>'
        b += text(74, y + 36, name, 22, BLUE if us else INK, 800, font=F_HEAD, ls=-0.5)
        b += text(380, y + 36, price, 21, INK, 600)
        col = INK if fee.startswith(('0', '10', '6', '7')) else MUTED
        b += text(800, y + 36, fee, 21, col, 600 if col == INK else 400)
        y += 66
    y += 4
b += text(60, H - 60, 'Sources: each official pricing page, checked 5 Nov 2026. Taxes extra where stated; AllCoaching + 18% GST.', 16, MUTED)
b += text(60, H - 34, 'Rupee Graphy prices not quoted (conflicting figures on its page). Payment-gateway charges are separate.', 16, MUTED)
b += signature(W, H)
save('price-and-fee', svg(W, H, b, 'Online course platforms in India: price as listed and fee per sale side by side for Udemy, Classplus, Exly, AllCoaching, Learnyst, Edmingle, Teachable, Thinkific and Tutor LMS'))

# 4. yearly cost bars (illustrative) --------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['What a year *really costs*'], 54)
b += lines(62, 150, ['Plan price + published fee on sales, lowest plan per platform. Illustrative, before GST and gateway.'], 20)
data = [  # name, at 2 lakh, at 10 lakh, note
    ('AllCoaching', 26999, 47988, 'Yearly Starter at ₹2L · Starter monthly at ₹10L'),
    ('Exly', 20000, 90000, 'Starter 10% at ₹2L · Pro ₹30,000 + 6% at ₹10L'),
    ('Classplus', 29999, 29999, '1-year plan; sales fee not stated'),
    ('Edmingle', 89988, 89988, 'Core, billed yearly; sales fee not stated'),
    ('Learnyst', 107988, 107988, 'Professional, 12 × ₹8,999; 0% listed'),
]
mx = 110000
for k, (lvl, idx) in enumerate([('At ₹2 lakh of sales a year', 1), ('At ₹10 lakh of sales a year', 2)]):
    y0 = 210 + k * 400
    b += white_panel(50, y0, 1120, 370, 26)
    b += text(80, y0 + 50, lvl, 25, INK, 800, font=F_HEAD, ls=-0.6)
    for i, row in enumerate(data):
        y = y0 + 80 + i * 56
        us = row[0] == 'AllCoaching'
        v = row[idx]
        w = max(40, 640 * v / mx)
        b += text(80, y + 30, row[0], 20, BLUE if us else INK, 700, font=F_HEAD)
        b += f'<rect x="250" y="{y + 8}" width="{w}" height="32" rx="10" fill="{BLUE if us else "#C9CEDD"}"/>'
        b += text(262 + w, y + 31, inr(v), 20, INK, 700, font=F_HEAD)
        if row[0] in ('Classplus', 'Edmingle'):
            b += text(262 + w + 92, y + 31, '+ fee not stated', 16, MUTED)
b += text(60, 1008, 'Illustrative. Teachable and Thinkific are priced in US dollars, so they are left out of the bars.', 16, MUTED)
b += text(60, 1032, 'AllCoaching + 18% GST. Gateway charges on student payments are separate. Prices checked 5 Nov 2026.', 16, MUTED)
b += signature(W, H)
save('yearly-cost', svg(W, H, b, 'Illustrative total yearly cost to sell online courses in India at 2 lakh and 10 lakh rupees of sales: AllCoaching, Exly, Classplus, Edmingle and Learnyst'))

# 5. what you keep from a 1,000 sale ---------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['What you keep from *₹1,000*'], 54)
b += lines(62, 150, ['One ₹1,000 course sale, 2% standard gateway fee + 18% GST on that fee. Illustrative.'], 21)
keep = [('0% commission', 1000 - 20 - 3.6, 0), ('5% fee per sale', 1000 - 20 - 3.6 - 50, 50),
        ('7.5% fee per sale', 1000 - 20 - 3.6 - 75, 75), ('10% fee per sale', 1000 - 20 - 3.6 - 100, 100)]
for i, (lab, k_, fee) in enumerate(keep):
    y = 210 + i * 140
    b += white_panel(50, y, 1120, 116, 24)
    b += text(80, y + 50, lab, 25, BLUE if i == 0 else INK, 800, font=F_HEAD, ls=-0.6)
    b += text(80, y + 84, f'Gateway ₹23.60' + (f' · platform fee ₹{fee}' if fee else ' · no platform fee'), 18, MUTED)
    bw = 560 * k_ / 1000
    b += f'<rect x="440" y="{y + 36}" width="560" height="44" rx="12" fill="#EEF0F6"/>'
    b += f'<rect x="440" y="{y + 36}" width="{bw:.0f}" height="44" rx="12" fill="{BLUE if i == 0 else "#7D8BEA"}"/>'
    b += text(1150, y + 68, f'₹{k_:,.2f}', 26, INK, 800, 'end', F_HEAD)
b += text(60, 790, 'Gateway rate from razorpay.com/pricing (standard plan, India), checked 5 Nov 2026. GST on platform fees not shown.', 16, MUTED)
b += signature(W, H)
save('keep-per-sale', svg(W, H, b, 'Illustrative: what an educator keeps from a 1,000 rupee online course sale at 0%, 5%, 7.5% and 10% fee per sale after a 2% payment gateway fee'))

# 6. decision tree ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Which type *fits you?*'], 54)
b += lines(62, 150, ['Start from where your students come from today'], 22)
b += f'<g filter="url(#sh)"><rect x="360" y="196" width="500" height="92" rx="46" fill="{INK}"/></g>'
b += text(610, 252, 'Do you already have an audience?', 26, '#fff', 800, 'middle', F_HEAD, -0.6)
b += arrow('M480 292 C 420 330, 300 330, 240 372', BLUE, 4) + arrow('M740 292 C 780 320, 800 340, 810 372', BLUE, 4)
b += text(360, 316, 'Not yet', 20, BLUE, 700, 'end') + text(800, 316, 'Yes', 20, BLUE, 700)
b += pill_card(60, 386, 360, 'Marketplace first', 'Test what sells', 'store', h=110, tile=NAVY_TILE, title_size=25)
b += text(240, 540, 'then move to your', 19, MUTED, anchor='middle') + text(240, 566, 'own academy', 19, MUTED, anchor='middle')
b += f'<g filter="url(#sh)"><rect x="470" y="386" width="680" height="88" rx="44" fill="#fff"/></g>' + text(810, 440, 'How do you teach?', 24, INK, 800, 'middle', F_HEAD, -0.5)
b += arrow('M650 478 L 570 574', BLUE, 4) + arrow('M810 478 L 810 574', BLUE, 4) + arrow('M970 478 L 1050 574', BLUE, 4)
profiles = [(545, 'YouTube / skill', 'Own academy, yearly Starter', 'Small sales, own brand'),
            (800, 'Exam batch, 500', 'Own academy, monthly 0%', 'Tests, rank, app'),
            (1055, 'Institute', 'Own academy, Pro', 'Team, iOS, 4K')]
for x, t, s, s2 in profiles:
    b += white_panel(x - 117, 590, 234, 190, 24)
    b += text(x, 636, t, 21, INK, 800, 'middle', F_HEAD, -0.4)
    b += text(x, 676, s.split(',')[0], 19, BLUE, 700, 'middle')
    b += text(x, 702, s.split(',')[1].strip(), 19, BLUE, 700, 'middle')
    b += text(x, 744, s2, 17, MUTED, anchor='middle')
b += white_panel(60, 830, 1100, 110, 24)
b += text(90, 876, 'Want full control of code and hosting, and have a developer?', 21, INK, 700, font=F_HEAD)
b += text(90, 910, 'A DIY stack (WordPress + an LMS plugin) works, but you maintain every part.', 19, MUTED)
b += signature(W, H)
save('decision-tree', svg(W, H, b, 'Decision tree: where to sell online courses in India for a beginner, a YouTube or skill educator, an exam batch of 500 students and a coaching institute'))

# 7. own academy promo -----------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Your domain.', 'Your brand.', '*Your students.*'], 62)
b += lines(64, 450, ['Sign up, choose a plan, upload', 'your course, connect your domain,', 'start selling.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Own domain', 'globe', 'Every plan'), ('Android app', 'phone', 'Every plan'), ('iOS app', 'phone', 'Pro monthly, yearly'),
                                     ('UPI checkout', 'card', 'Via Razorpay'), ('Test series', 'trophy', 'All-India rank')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission from ₹3,999/month + GST', 27, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('own-academy', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own domain, own Android app, iOS app on Pro monthly and yearly plans, UPI checkout and test series'))

# 8. mistakes --------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Platform', 'mistakes.'], 54)
for i, t in enumerate(['Picked by headline price', 'Ignored the fee per sale', 'Students live on their app', 'No data export plan', 'Dollar plan, rupee students']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 520, t, -1.4 if i % 2 else 1.0, 27)
b += hand(300, 790, ['Read the fee', 'line first.'], 38, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Total cost at your sales', 'Fee next to every price', 'Your domain, your app', 'Export students any time', 'UPI checkout, GST invoice']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Common mistakes when choosing a platform to sell online courses in India, and what to do instead', ('split', 600)))
