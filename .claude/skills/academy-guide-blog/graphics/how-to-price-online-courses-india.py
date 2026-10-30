"""Graphics for /blog/how-to-price-online-courses-india.

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-price-online-courses-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-price-online-courses-india

All rupee figures are illustrative. The worked numbers use the same assumptions as the table in the post:
each cell uses the lowest-cost AllCoaching plan at that sales level (studio pricing, owner 2026-10-29): yearly Starter
(10%, ₹6,999 + 18% GST), yearly Growth (7.5%, ₹12,999 + GST), yearly Pro (5%, ₹24,999 + GST) or a monthly 0% plan
(₹3,999 / ₹5,999 / ₹7,999 × 12 + GST),
an assumed 2% gateway charge and no GST registration.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'how-to-price-online-courses-india')
os.makedirs(OUT, exist_ok=True)

GATEWAY = 0.02
PLANS = [('Starter yearly', 6999 * 1.18, 0.10), ('Growth yearly', 12999 * 1.18, 0.075), ('Pro yearly', 24999 * 1.18, 0.05),
         ('Starter monthly', 47988 * 1.18, 0.0), ('Growth monthly', 71988 * 1.18, 0.0), ('Pro monthly', 95988 * 1.18, 0.0)]


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def inr(v):
    """Indian digit grouping: 1234567 -> ₹12,34,567."""
    n = int(round(v))
    s = str(n)
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts) + ',' + tail
    return '₹' + s


def best(p, n):
    """(take-home, plan name) on whichever plan leaves more."""
    return max((p * n * (1 - f - GATEWAY) - c, name) for name, c, f in PLANS)


def take_home(p, n):
    return best(p, n)[0]


# 1. cover --------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Price your course.', '*Know your take-home.*'], 76)
b += lines(84, 470, ['How to price an online course in India,', 'with a worked revenue calculator.'], 30, MUTED)
b += check_row(84, 610, 'Seven pricing models compared', 26)
b += check_row(84, 670, 'Fees, gateway and GST in one formula', 26)
b += check_row(84, 730, 'A worksheet you can copy', 26)
b += white_panel(990, 150, 540, 600, 32, big=True)
b += eyebrow(1030, 210, 'Revenue calculator')
rows = [('Course price', '₹2,999'), ('Students', '× 500'), ('Sales', inr(2999 * 500)), ('Commission, monthly plan (0%)', '− ₹0'),
        ('Gateway (assumed 2%)', '− ' + inr(2999 * 500 * GATEWAY)), ('Starter monthly + GST', '− ' + inr(47988 * 1.18))]
for i, (l, v) in enumerate(rows):
    y = 272 + i * 64
    b += text(1030, y, l, 21, MUTED) + text(1490, y, v, 23, RED if v.startswith('−') else INK, 700, 'end', F_HEAD)
    b += f'<rect x="1030" y="{y + 22}" width="460" height="1.5" fill="{LINE}"/>'
b += f'<rect x="1014" y="652" width="492" height="78" rx="20" fill="{BLUE_TINT}"/>'
b += text(1038, 700, 'Take-home', 23, INK, 700, font=F_HEAD) + text(1484, 702, inr(take_home(2999, 500)), 34, BLUE, 800, 'end', F_HEAD, -1)
b += text(80, 860, 'Illustrative figures, before income tax.', 16, MUTED)
save('cover', svg(1600, 900, b, 'How to price an online course in India with a worked revenue calculator showing take-home after fees'))

# 2. the formula ----------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['The take-home formula', 'for *any course price*'], 52)
steps = [('tag', 'Price × students', 'Your gross sales', INK),
         ('layers', '− Platform fee', '0% monthly; 10%, 7.5% or 5% yearly', RED),
         ('card', '− Gateway charges', 'If charged separately to you', RED),
         ('file', '− GST', 'Only if you are registered', RED),
         ('calendar', '− Yearly costs', 'Plan, tools, ads', RED)]
for i, (ic, t, s, c) in enumerate(steps):
    y = 230 + i * 104
    b += pill_card(60, y, 640, t, s, ic, h=88, tile=BLUE if i == 0 else NAVY_TILE, title_size=27)
b += white_panel(760, 300, 400, 380, 30, big=True)
b += eyebrow(800, 360, 'Equals')
b += text(800, 440, 'Take-home', 52, BLUE, 800, font=F_HEAD, ls=-2)
b += lines(800, 500, ['before income tax.', 'This is the number to', 'plan your year on,', 'not the course price.'], 22, MUTED, 1.45)
b += arrow('M712 492 H 748', BLUE, 4)
b += text(60, H - 28, 'Illustrative method. Confirm your platform and gateway charges before you price.', 16, MUTED) + signature(W, H)
save('take-home-formula', svg(W, H, b, 'Online course pricing formula: price times students minus platform fee, gateway charges, GST and yearly costs equals take-home'))

# 3. the worked calculator table --------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Take-home at *3 prices*', 'and 3 batch sizes'], 52)
b += lines(62, 220, ['Lowest-cost AllCoaching plan per cell, assumed 2% gateway, plan price + GST'], 21)
prices, counts = [999, 2999, 7999], [50, 200, 500]
x0, y0, cw, rh = 60, 270, 275, 150
b += white_panel(x0, y0, 1100, 90 + rh * 3, 28, big=True)
b += eyebrow(x0 + 32, y0 + 56, 'Price / students', MUTED)
for j, n in enumerate(counts):
    b += text(x0 + 275 + j * cw + cw / 2, y0 + 58, f'{n} students', 24, INK, 800, 'middle', F_HEAD, -0.6)
for i, p in enumerate(prices):
    y = y0 + 90 + i * rh
    b += f'<rect x="{x0 + 24}" y="{y}" width="1052" height="1.5" fill="{LINE}"/>'
    b += text(x0 + 32, y + 86, inr(p), 34, BLUE, 800, font=F_HEAD, ls=-1)
    for j, n in enumerate(counts):
        cx = x0 + 275 + j * cw + cw / 2
        b += text(cx, y + 76, inr(take_home(p, n)), 30, INK, 800, 'middle', F_HEAD, -0.8)
        b += text(cx, y + 106, 'of ' + inr(p * n), 18, MUTED, anchor='middle')
        b += text(cx, y + 132, best(p, n)[1], 17, BLUE, 700, anchor='middle')
b += text(60, H - 64, 'Illustrative. Rounded to the rupee, before income tax. Monthly plans = 0% commission, price × 12.', 16, MUTED)
b += text(60, H - 40, '₹7,999 × 500 crosses ₹20 lakh of sales, so GST registration would generally apply.', 16, MUTED) + signature(W, H)
save('take-home-table', svg(W, H, b, 'Online course fee calculator table: illustrative take-home at ₹999, ₹2,999 and ₹7,999 for 50, 200 and 500 students'))

# 4. pricing models ----------------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Seven ways to *charge*', 'for what you teach'], 52)
models = [('book', 'One-time course fee', 'Pay once, access for a set period'),
          ('users', 'Batch fee', 'Fixed dates, live classes, a cohort'),
          ('calendar', 'Monthly membership', 'Pay each month, stay while useful'),
          ('check', 'Test series', 'Mock tests sold alone or as add-on'),
          ('layers', 'Bundle', 'Course + tests + notes together'),
          ('card', 'Instalments', 'Fee split into parts, a concept'),
          ('play', 'Free demo + paid course', 'Sample first, then the full course')]
for i, (ic, t, s) in enumerate(models):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 160
    b += pill_card(x, y, 540, t, s, ic, h=124, tile=BLUE if i == 6 else NAVY_TILE, title_size=26)
b += f'<rect x="620" y="690" width="540" height="124" rx="24" fill="{BLUE_TINT}"/>'
b += lines(650, 742, ['Most academies mix two or three:', 'a free demo, a course, a test series.'], 21, INK, 1.45)
b += text(60, H - 28, 'Instalments shown as a general concept, not a confirmed platform feature.', 16, MUTED) + signature(W, H)
save('pricing-models', svg(W, H, b, 'Seven online course pricing models in India: one-time course fee, batch fee, monthly membership, test series, bundle, instalments, free demo plus paid course'))

# 5. value ladder -----------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['A value ladder', 'from *free to premium*'], 52)
rungs = [('play', 'Free demo', ['YouTube class,', 'sample notes'], 'Free'),
         ('check', 'Test series', ['Mocks with', 'analysis'], '₹299–₹1,999'),
         ('book', 'Recorded', ['Self-paced', 'lessons'], '₹499–₹2,999'),
         ('users', 'Live batch', ['Classes and', 'doubt sessions'], '₹2,999–₹14,999'),
         ('star', 'Mentorship', ['Small group', 'or 1-on-1'], '₹15,000+')]
for i, (ic, t, s, p) in enumerate(rungs):
    x = 60 + i * 222
    h = 290 + i * 70
    y = 770 - h
    hl = i == 3
    b += white_panel(x, y, 202, h, 24)
    if hl:
        b += f'<rect x="{x}" y="{y}" width="202" height="{h}" rx="24" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += f'<rect x="{x + 22}" y="{y + 24}" width="56" height="56" rx="16" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, x + 36, y + 38, 28, '#fff', 2)
    b += text(x + 22, y + 124, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += lines(x + 22, y + 158, s, 17, MUTED, 1.35)
    b += text(x + 22, y + 238, p, 20 if len(p) > 12 else 22, BLUE, 700, font=F_HEAD)
b += text(60, H - 28, 'Illustrative ranges, not market data. Your audience and outcome set the real number.', 16, MUTED) + signature(W, H)
save('value-ladder', svg(W, H, b, 'Online course value ladder: free demo, test series, recorded course, live batch and mentorship with illustrative price ranges'))

# 6. price by audience ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['What moves the price', '*up or down*'], 52)
cols = [('Moves it up', BLUE, 'trend', ['High-stakes exam outcome', 'Live classes and feedback', 'Visible results and reviews', 'Small batch, personal access', 'Career or income skill']),
        ('Moves it down', RED, 'chart', ['Hobby or casual interest', 'Self-paced recordings only', 'New educator, little proof', 'Many free alternatives', 'Budget-sensitive families'])]
for k, (t, c, ic, rows_) in enumerate(cols):
    x = 60 + k * 560
    b += white_panel(x, 200, 540, 560, 28)
    b += f'<rect x="{x + 28}" y="228" width="64" height="64" rx="18" fill="{c if k == 0 else NAVY_TILE}"/>' + icon(ic, x + 44, 244, 32, '#fff', 2)
    b += text(x + 112, 272, t, 32, INK, 800, font=F_HEAD, ls=-1)
    for i, r in enumerate(rows_):
        b += check_row(x + 32, 370 + i * 82, r, 22, k == 0)
b += text(60, 810, 'Hindi or English medium changes who you reach, not the value of the outcome.', 21, INK, 600)
b += text(60, H - 28, 'General guidance. Test prices with your own students.', 16, MUTED) + signature(W, H)
save('price-by-audience', svg(W, H, b, 'Factors that move an online course price up or down in India: exam stakes, live classes, proof, audience budget and alternatives'))

# 7. good-better-best tiers -------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Three tiers, one *clear*', '*middle choice*'], 52)
tiers = [('Basic', '₹1,499', ['Recorded lessons', 'PDF notes', '6 months access'], False),
         ('Standard', '₹3,999', ['Everything in Basic', 'Weekly live doubt class', 'Full test series'], True),
         ('Premium', '₹9,999', ['Everything in Standard', 'Small-group mentoring', 'Answer-sheet review'], False)]
for k, (t, p, feats, hl) in enumerate(tiers):
    x = 60 + k * 375
    y = 210 if hl else 250
    hh = 600 if hl else 560
    b += white_panel(x, y, 350, hh, 28, big=hl)
    if hl:
        b += f'<rect x="{x}" y="{y}" width="350" height="{hh}" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
        b += f'<rect x="{x + 28}" y="{y + 28}" width="176" height="38" rx="19" fill="{BLUE}"/>' + text(x + 116, y + 53, 'Most students', 16, '#fff', 700, 'middle')
    b += text(x + 28, y + 130, t, 30, INK, 800, font=F_HEAD, ls=-1)
    b += text(x + 28, y + 200, p, 52, BLUE if hl else INK, 800, font=F_HEAD, ls=-2)
    for i, f_ in enumerate(feats):
        b += check_row(x + 28, y + 300 + i * 74, f_, 20)
b += text(60, H - 28, 'Illustrative tiers for a state PSC course. The top tier anchors the middle one.', 16, MUTED) + signature(W, H)
save('good-better-best', svg(W, H, b, 'Good-better-best course pricing tiers: basic, standard and premium with the middle tier as the anchored choice'))

# 8. raise-price signals ------------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['Signs it is time to', '*raise your price*'], 52)
sig = [('users', 'Batches fill before the deadline', 'Seats go early, two batches running'),
       ('star', 'Results and reviews are visible', 'Selections, scores, written feedback'),
       ('message', 'Almost nobody asks for a discount', 'Price questions have stopped'),
       ('layers', 'You added real value', 'Live classes, tests, a new module'),
       ('trend', 'Completion is high', 'Students finish and come back')]
for i, (ic, t, s) in enumerate(sig):
    b += pill_card(60, 200 + i * 116, 760, t, s, ic, h=98, tile=BLUE if i == 0 else NAVY_TILE, title_size=26)
b += white_panel(860, 300, 300, 300, 28, big=True)
b += eyebrow(890, 356, "How to raise")
b += lines(890, 412, ['Next batch only.', 'Keep current students', 'at their price.', 'Announce the date', 'early, and keep it.'], 22, INK, 1.6)
b += text(60, H - 28, 'General guidance, not a rule. Raise in steps you can explain.', 16, MUTED) + signature(W, H)
save('raise-price-signals', svg(W, H, b, 'Five signals it is time to raise your online course price, and how to raise it for the next batch'))

# 9. mistakes ----------------------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Pricing your', 'course like this?'], 56)
for i, t in enumerate(['Copied a rival price', 'Forgot the fees', 'Fake last-day offer', 'Price never changes', 'GST surprise later']):
    b += tape(40 + (i % 2) * 22, 240 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(310, 800, ['Why so cheap?', 'Is it any good?'], 36, INK, -6)
b += headline(650, 190, ['Do this', '*instead.*'], 62)
for i, t in enumerate(['Price on the outcome', 'Work out take-home', 'Real, dated deadlines', 'Review every batch', 'Decide GST upfront']):
    b += check_row(656, 360 + i * 78, t, 25)
b += signature(W, H)
save('pricing-mistakes', svg(W, H, b, 'Common online course pricing mistakes in India and what to do instead', ('split', 600)))

# 10. academy promo --------------------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Set your price.', '*Students pay*', '*by UPI.*'], 62)
b += lines(64, 440, ['Your course page, your price.', 'Checkout by UPI or card, payouts', 'to your bank through Razorpay.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Your price', 'tag', 'Per course'), ('UPI & cards', 'card', 'Every plan'), ('Payouts', 'home', 'Via Razorpay'),
                                     ('Website', 'globe', 'Your domain'), ('Your app', 'phone', 'Android')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission from ₹3,999/month', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('academy-course-pricing', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: set your own course price, UPI and card checkout and Razorpay payouts on every plan'))
