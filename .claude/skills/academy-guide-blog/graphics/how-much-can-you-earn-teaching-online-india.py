"""Graphics for /blog/how-much-can-you-earn-teaching-online-india (v3 refresh, 2026-10-27).

Run:  python .claude/skills/academy-guide-blog/graphics/how-much-can-you-earn-teaching-online-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-much-can-you-earn-teaching-online-india

All rupee figures are illustrative and use the same maths as the post and its calculator:
take-home before tax = students x price x (1 - platform fee) - plan price (ex-GST) - ads and tools.
Plans: Starter 6,999 + 10%, Growth 12,999 + 7.5%, Pro 24,999 + 5%, Scale 99,999 + 0% (yearly, before GST).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SLUG = 'how-much-can-you-earn-teaching-online-india'
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

PLANS = [('Starter', 6999, .10), ('Growth', 12999, .075), ('Pro', 24999, .05), ('Scale', 99999, 0.0)]


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def inr(v):
    """Indian digit grouping: 1234567 -> ₹12,34,567."""
    n = int(round(v))
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts) + ',' + tail
    return ('−' if n < 0 else '') + '₹' + s


def plan(name):
    return next(p for p in PLANS if p[0] == name)


def take_home(students, price, plan_name, ads):
    _, cost, fee = plan(plan_name)
    gross = students * price
    return gross, gross * fee, cost, gross - gross * fee - cost - ads


# Scenario A: SSC maths in Hindi, YouTube; 280 x 1,499, Growth, 36,000 ads/tools
A = take_home(280, 1499, 'Growth', 36000)
# Scenario B: spoken English, Instagram; 100 x 1,999, Starter, 24,000 ads
B = take_home(100, 1999, 'Starter', 24000)
# Scenario C: small institute, live batches; 300 x 8,000, Scale, 1,50,000 ads/tools
C = take_home(300, 8000, 'Scale', 150000)

# 1. cover --------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['What can you earn', '*teaching online?*'], 76)
b += lines(84, 470, ['Online coaching income in India,', 'worked out with a free calculator.'], 30, MUTED)
b += check_row(84, 610, 'The take-home formula', 26)
b += check_row(84, 670, 'Three illustrative educators', 26)
b += check_row(84, 730, 'Which plan costs least at your sales', 26)
b += white_panel(990, 150, 540, 600, 32, big=True)
b += eyebrow(1030, 210, 'Income calculator')
rows = [('Students', '280'), ('Price', '₹1,499'), ('Gross sales', inr(A[0])), ('Platform fee 7.5%', '− ' + inr(A[1])),
        ('Growth plan', '− ' + inr(A[2])), ('Ads and tools', '− ₹36,000')]
for i, (l, v) in enumerate(rows):
    y = 272 + i * 64
    b += text(1030, y, l, 21, MUTED) + text(1490, y, v, 23, RED if v.startswith('−') else INK, 700, 'end', F_HEAD)
    b += f'<rect x="1030" y="{y + 22}" width="460" height="1.5" fill="{LINE}"/>'
b += f'<rect x="1014" y="652" width="492" height="78" rx="20" fill="{BLUE_TINT}"/>'
b += text(1038, 700, 'Take-home', 23, INK, 700, font=F_HEAD) + text(1484, 702, inr(A[3]), 34, BLUE, 800, 'end', F_HEAD, -1)
b += text(80, 860, 'Illustrative figures, yearly, before GST and income tax.', 16, MUTED)
save('cover', svg(1600, 900, b, 'How much can you earn teaching online in India: an income calculator showing gross sales, platform fee, plan cost and take-home'))

# 2. the formula --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Online coaching income', 'is a *formula*'], 52)
steps = [('users', 'Students × price', 'Your gross sales for the year', BLUE),
         ('layers', '− Platform fee', '10%, 7.5%, 5% or 0% by plan', NAVY_TILE),
         ('calendar', '− Plan price', '₹6,999 to ₹99,999 a year, ex-GST', NAVY_TILE),
         ('trend', '− Ads and tools', 'Meta ads, mic, editing apps', NAVY_TILE),
         ('file', '− GST and income tax', 'Depends on your turnover and income', NAVY_TILE)]
for i, (ic, t, s, tile) in enumerate(steps):
    y = 200 + i * 108
    b += pill_card(60, y, 640, t, s, ic, h=90, tile=tile, title_size=27)
b += white_panel(760, 300, 400, 380, 30, big=True)
b += eyebrow(800, 360, 'Equals')
b += text(800, 440, 'Take-home', 52, BLUE, 800, font=F_HEAD, ls=-2)
b += lines(800, 500, ['what you keep.', 'Plan your year on', 'this number, not on', 'gross sales.'], 22, MUTED, 1.45)
b += arrow('M712 492 H 748', BLUE, 4)
b += text(60, H - 28, 'Method, not a promise. Check GST and tax with official sources or a CA.', 16, MUTED) + signature(W, H)
save('income-formula', svg(W, H, b, 'Online coaching income formula: students times price minus platform fee, plan price, ads and tools, then GST and income tax equals take-home'))

# 3. plan breakeven chart -------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Which plan costs least', 'at *your sales level*'], 52)
b += lines(62, 214, ['Yearly cost = plan price + platform fee on sales, before GST'], 21)
X0, X1, Y0, Y1 = 150, 1000, 350, 800
SMAX, CMAX = 2000000, 220000


def px(s):
    return X0 + (X1 - X0) * s / SMAX


def py(c):
    return Y1 - (Y1 - Y0) * c / CMAX


b += white_panel(40, 250, 1140, 640, 28, big=True)
for c in (0, 50000, 100000, 150000, 200000):
    b += f'<rect x="{X0}" y="{py(c)}" width="{X1 - X0}" height="1.5" fill="{LINE}"/>'
    b += text(X0 - 14, py(c) + 6, '₹0' if c == 0 else f'₹{c / 100000:g}L', 17, MUTED, anchor='end')
for s in (0, 500000, 1000000, 1500000, 2000000):
    b += text(px(s), Y1 + 34, '₹0' if s == 0 else f'₹{s / 100000:g}L', 17, MUTED, anchor='middle')
b += text((X0 + X1) / 2, Y1 + 66, 'Your sales in a year', 18, INK, 600, 'middle')
for be in (240000, 480000, 1500000):
    b += f'<line x1="{px(be)}" y1="{Y0 - 10}" x2="{px(be)}" y2="{Y1}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="5 6"/>'
cols = {'Starter': '#9AA0B4', 'Growth': '#6C7390', 'Pro': '#1B1E2E', 'Scale': '#E5484D'}
for n, p, f in PLANS:
    b += f'<line x1="{px(0)}" y1="{py(p)}" x2="{px(SMAX)}" y2="{py(p + f * SMAX)}" stroke="{cols[n]}" stroke-width="3"/>'
env = [(0, 6999), (240000, 30999), (480000, 48999), (1500000, 99999), (SMAX, 99999)]
b += '<polyline points="' + ' '.join(f'{px(s):.1f},{py(c):.1f}' for s, c in env) + f'" fill="none" stroke="{BLUE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity=".35"/>'
labels = [('Starter', 206999), ('Growth', 162999), ('Pro', 124999), ('Scale', 99999)]
for n, c in labels:
    b += f'<circle cx="{X1 + 20}" cy="{py(c) - 6}" r="7" fill="{cols[n]}"/>' + text(X1 + 34, py(c), n, 21, INK, 700, font=F_HEAD)
bands = [('Starter', '< ₹2.4L', 0, 240000), ('Growth', '₹2.4–4.8L', 240000, 480000), ('Pro', '₹4.8–15L', 480000, 1500000), ('Scale', '> ₹15L', 1500000, SMAX)]
for n, rng, a, z in bands:
    cx = (px(a) + px(z)) / 2
    b += text(cx, Y0 - 50, n, 16, BLUE, 700, 'middle', F_HEAD) + text(cx, Y0 - 30, rng, 14, BLUE, 600, 'middle')
b += text(60, H - 40, 'Shaded blue line = lowest yearly cost. Breakevens ₹2.4 lakh, ₹4.8 lakh and ₹15 lakh. Prices exclude GST.', 16, MUTED) + signature(W, H)
save('plan-breakeven', svg(W, H, b, 'Chart of yearly cost by AllCoaching plan against yearly sales: Starter lowest below ₹2.4 lakh, Growth to ₹4.8 lakh, Pro to ₹15 lakh, Scale above ₹15 lakh'))

# 4. three illustrative educators ------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Three educators,', '*three take-homes*'], 52)
cards = [('play', 'SSC maths, Hindi', 'Grows on YouTube', '280 × ₹1,499', A, 'Growth', 'Ads and tools ₹36,000'),
         ('image', 'Spoken English', 'Grows on Instagram', '100 × ₹1,999', B, 'Starter', 'Meta ads ₹24,000'),
         ('users', 'Coaching institute', 'Moves live batches online', '300 × ₹8,000', C, 'Scale', 'Ads and tools ₹1,50,000')]
for k, (ic, t, s, calc, r, pl, ads) in enumerate(cards):
    x = 60 + k * 375
    y = 210
    b += white_panel(x, y, 350, 690, 28, big=k == 0)
    b += f'<rect x="{x + 28}" y="{y + 28}" width="64" height="64" rx="18" fill="{BLUE if k == 0 else NAVY_TILE}"/>' + icon(ic, x + 44, y + 44, 32, '#fff', 2)
    b += text(x + 28, y + 142, t, 28, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(x + 28, y + 176, s, 19, MUTED)
    b += eyebrow(x + 28, y + 236, 'Students × price')
    b += text(x + 28, y + 280, calc, 30, INK, 800, font=F_HEAD, ls=-1)
    b += text(x + 28, y + 314, 'Sales ' + inr(r[0]), 19, MUTED)
    b += f'<rect x="{x + 28}" y="{y + 340}" width="294" height="1.5" fill="{LINE}"/>'
    b += eyebrow(x + 28, y + 384, 'Lowest-cost plan')
    b += text(x + 28, y + 426, pl, 30, BLUE, 800, font=F_HEAD, ls=-1)
    b += text(x + 28, y + 460, 'Fee ' + inr(r[1]) + ' + plan ' + inr(r[2]), 18, MUTED)
    b += text(x + 28, y + 490, ads, 18, MUTED)
    b += f'<rect x="{x + 16}" y="{y + 540}" width="318" height="120" rx="20" fill="{BLUE_TINT}"/>'
    b += text(x + 36, y + 584, 'Take-home before tax', 18, INK, 600)
    b += text(x + 36, y + 634, inr(r[3]), 36, BLUE, 800, font=F_HEAD, ls=-1.2)
b += text(60, H - 40, 'Illustrative, yearly, before GST and income tax. The institute still pays its teachers from this.', 16, MUTED) + signature(W, H)
save('three-educators', svg(W, H, b, 'Online tutor earnings in India, three illustrative examples: SSC maths educator on Growth, spoken English educator on Starter, coaching institute on Scale'))

# 5. revenue levers -------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Five levers that', 'move *your income*'], 52)
lev = [('tag', 'Price', 'Charge for the outcome, not the hours'),
       ('trend', 'Conversion', 'More demo watchers become buyers'),
       ('book', 'Repeat courses', 'The next level for students you have'),
       ('check', 'Test series', 'A low-price add-on many students buy'),
       ('users', 'Live batches', 'A premium tier with doubt classes')]
for i, (ic, t, s) in enumerate(lev):
    b += pill_card(60, 200 + i * 116, 760, t, s, ic, h=98, tile=BLUE if i == 0 else NAVY_TILE, title_size=27)
b += white_panel(860, 300, 300, 300, 28, big=True)
b += eyebrow(890, 356, 'Rule of thumb')
b += lines(890, 412, ['Move one lever', 'at a time, for one', 'batch, and compare', 'take-home, not', 'just sales.'], 22, INK, 1.5)
b += text(60, H - 28, 'General guidance. Test changes with your own students.', 16, MUTED) + signature(W, H)
save('revenue-levers', svg(W, H, b, 'Five levers to grow online coaching income: price, conversion, repeat courses, test series and live batches'))

# 6. formats and how they scale --------------------------------------------------------
W, H = 1220, 760
b = headline(60, 100, ['What each format', '*earns and scales with*'], 52)
fm = [('play', 'Free demo', ['YouTube class,', 'sample notes'], 'Free', 'Brings students'),
      ('check', 'Test series', ['Mocks with', 'analysis'], '₹299–₹1,999', 'Scales with reach'),
      ('book', 'Recorded', ['Self-paced', 'lessons'], '₹499–₹2,999', 'Scales with reach'),
      ('users', 'Live batch', ['Classes and', 'doubt sessions'], '₹2,999–₹14,999', 'Limited by hours'),
      ('star', 'One-to-one', ['Personal', 'sessions'], '₹300–₹1,500/hr', 'Limited by hours')]
for i, (ic, t, s, p, sc) in enumerate(fm):
    x = 60 + i * 222
    y = 220
    hl = i == 2
    b += white_panel(x, y, 202, 420, 24)
    if hl:
        b += f'<rect x="{x}" y="{y}" width="202" height="420" rx="24" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += f'<rect x="{x + 22}" y="{y + 24}" width="56" height="56" rx="16" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, x + 36, y + 38, 28, '#fff', 2)
    b += text(x + 22, y + 130, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += lines(x + 22, y + 166, s, 17, MUTED, 1.35)
    b += text(x + 22, y + 270, p, 19 if len(p) > 12 else 22, BLUE, 700, font=F_HEAD)
    b += f'<rect x="{x + 22}" y="{y + 300}" width="158" height="1.5" fill="{LINE}"/>'
    b += lines(x + 22, y + 340, sc.split(' ', 1), 18, INK, 1.35, weight=600)
b += text(60, H - 40, 'Illustrative price ranges, not market data. Your audience and outcome set the real number.', 16, MUTED) + signature(W, H)
save('formats-scale', svg(W, H, b, 'Online teaching formats in India with illustrative prices: free demo, test series, recorded course, live batch and one-to-one, and what each scales with'))

# 7. mistakes -----------------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Counting your', 'income like this?'], 56)
for i, t in enumerate(['Sales = income', 'Forgot the fees', 'Ads not counted', 'Wrong plan for sales', 'Tax left to March']):
    b += tape(40 + (i % 2) * 22, 240 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(300, 800, ['Where did the', 'money go?'], 36, INK, -6)
b += headline(650, 190, ['Do this', '*instead.*'], 62)
for i, t in enumerate(['Track take-home', 'Fee + plan, per year', 'Budget ads up front', 'Recheck plan yearly', 'Set tax aside monthly']):
    b += check_row(656, 360 + i * 78, t, 25)
b += signature(W, H)
save('income-mistakes', svg(W, H, b, 'Common mistakes when Indian educators calculate online teaching income, and what to do instead', ('split', 600)))

# 8. academy promo --------------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Keep 90–100%', '*of every sale.*'], 62)
b += lines(64, 380, ['One yearly plan, a published fee,', 'UPI and card checkout, payouts', 'to your bank through Razorpay.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Website', 'globe', 'Your domain'), ('Android app', 'phone', 'Every plan'), ('Live classes', 'video', 'Unlimited'),
                                     ('UPI & cards', 'card', 'Every plan'), ('Scale', 'star', '0% fee')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, 'Plans from ₹6,999/year + GST', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '14 days free · no card needed', 21, MUTED)
save('academy-income', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own website, own Android app, unlimited live classes, UPI checkout and a 0% fee Scale plan'))
