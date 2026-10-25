"""Graphics for /blog/sell-online-courses-without-monthly-subscription.

Run:  python3 .claude/skills/academy-guide-blog/graphics/sell-online-courses-without-monthly-subscription.py
Then: python3 .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/sell-online-courses-without-monthly-subscription

All cost figures are illustrative: plan price + published fee on sales, before GST and gateway charges.
Competitor figures come from .claude/skills/academy-guide-blog/data/competitors.json (official pricing pages,
checked 24 Oct 2026). AllCoaching: Starter ₹6,999 + 10%, Growth ₹12,999 + 7.5%, Pro ₹24,999 + 5%, Scale ₹99,999 + 0%.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SLUG = 'sell-online-courses-without-monthly-subscription'
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

AC = [(6999, .10, 'Starter'), (12999, .075, 'Growth'), (24999, .05, 'Pro'), (99999, 0, 'Scale')]
# chart palette, validated with the dataviz validator (light mode, all checks pass)
C_AC, C_EXLY, C_LY, C_TM = BLUE, '#C46A00', '#7A3FB8', '#00897B'


def ac_best(s):
    return min(p + f * s for p, f, _ in AC)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


# 1. cover ------------------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 290, ['Sell courses without', 'a *monthly bill.*'], 74)
b += lines(84, 440, ['Monthly subscription, pay per sale or one', 'annual plan: what each really costs.'], 30, MUTED)
b += check_row(84, 590, 'Costs at every sales level, worked out', 26)
b += check_row(84, 650, 'When pay-per-sale costs less, and when not', 26)
b += check_row(84, 710, 'Plan breakevens from ₹2.4L to ₹15L', 26)
cards = [('calendar', 'Monthly subscription', 'A fixed bill every month', False),
         ('tag', 'Pay per sale', 'A % of every sale, no fixed fee', False),
         ('layers', 'One annual plan', 'One yearly bill + 0–10% on sales', True)]
for i, (ic, t, s, hl) in enumerate(cards):
    y = 170 + i * 190
    b += pill_card(960, y, 560, t, s, ic, h=130, tile=BLUE if hl else NAVY_TILE, title_size=30)
    if hl:
        b += f'<rect x="960" y="{y}" width="560" height="130" rx="24" fill="none" stroke="{BLUE}" stroke-width="3"/>'
b += hand(1010, 780, ['Which costs least', 'at your sales?'], 34, BLUE, -3)
b += text(80, 860, 'Illustrative comparison, before GST.', 16, MUTED)
save('cover', svg(1600, 900, b, 'Sell online courses without a monthly subscription: monthly bill vs pay per sale vs one annual plan'))

# 2. three models ---------------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Three ways to pay', 'for your *course platform*'], 52)
cols = [('calendar', 'Monthly', 'subscription', 'A fixed bill every', 'month, sales or not', 'Sales are high', 'and steady', False),
        ('tag', 'Pay per sale', '(commission only)', 'A % of every sale,', 'no fixed fee', 'Sales are small', 'or uncertain', False),
        ('layers', 'Annual plan', '+ smaller fee', 'One yearly bill and', 'a lower %, or 0%', 'Sales are growing', 'or already large', True)]
for k, (ic, t1, t2, p1, p2, w1, w2, hl) in enumerate(cols):
    x = 60 + k * 375
    b += white_panel(x, 210, 350, 580, 28, big=hl)
    if hl:
        b += f'<rect x="{x}" y="210" width="350" height="580" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += f'<rect x="{x + 28}" y="238" width="64" height="64" rx="18" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, x + 44, 254, 32, '#fff', 2)
    b += text(x + 28, 366, t1, 32, INK, 800, font=F_HEAD, ls=-1) + text(x + 28, 400, t2, 21, MUTED)
    b += eyebrow(x + 28, 470, 'You pay', MUTED)
    b += lines(x + 28, 508, [p1, p2], 22, INK, 1.4)
    b += f'<rect x="{x + 28}" y="572" width="294" height="1.5" fill="{LINE}"/>'
    b += eyebrow(x + 28, 620, 'Costs least when', BLUE)
    b += lines(x + 28, 658, [w1, w2], 22, INK, 1.4)
b += text(60, H - 28, 'General comparison. Exact costs depend on the plan, add-ons, GST and gateway charges.', 16, MUTED) + signature(W, H)
save('three-models', svg(W, H, b, 'Three ways to sell online courses: monthly subscription, pay per sale commission, or an annual plan with a smaller fee'))

# 3. monthly vs annual (problem side on the left) ---------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['12 bills', 'a year'], 60)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
quiet = {4, 5, 10}
for i, m in enumerate(months):
    x = 56 + (i % 4) * 128
    y = 220 + (i // 4) * 132
    b += f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="112" height="112" rx="20" fill="#fff"/></g>'
    b += text(x + 56, y + 42, m, 22, INK, 700, 'middle', F_HEAD)
    b += f'<rect x="{x + 22}" y="{y + 62}" width="68" height="28" rx="14" fill="{RED if i in quiet else "#F1F2F6"}"/>'
    b += text(x + 56, y + 82, 'Bill', 16, '#fff' if i in quiet else MUTED, 700, 'middle')
b += tape(46, 640, 420, 'Quiet month, same bill', -1.2, 25)
b += hand(90, 790, ['Renewal again?'], 38, INK, -5)
b += arrow('M350 770 Q 520 770 500 616', BLUE, 4)
b += headline(650, 190, ['One plan', '*a year.*'], 62)
b += white_panel(650, 290, 510, 170, 28, big=True)
b += f'<rect x="680" y="320" width="110" height="110" rx="24" fill="{BLUE}"/>' + icon('calendar', 711, 351, 48, '#fff', 2)
b += text(820, 365, 'One renewal', 30, INK, 800, font=F_HEAD, ls=-1) + text(820, 405, 'Plan your year once', 21, MUTED)
for i, t in enumerate(['Same cost in a quiet month', 'Fee only when you sell', 'Budget known on day one', 'No monthly renewal call']):
    b += check_row(656, 540 + i * 74, t, 25)
b += text(56, H - 28, 'Months marked red are illustrative quiet months.', 16, MUTED) + signature(W, H)
save('monthly-vs-annual', svg(W, H, b, 'Monthly subscription with 12 bills a year compared with one annual plan for an online academy', ('split', 600)))

# 4. cost chart -------------------------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Yearly platform cost', 'at *your sales level*'], 52)
px0, py0, pw, ph = 170, 290, 960, 420          # plot area (left, top, width, height)
xmax, ymax = 2000000, 220000


def X(s):
    return px0 + pw * s / xmax


def Y(c):
    return py0 + ph * (1 - c / ymax)


b += white_panel(60, 200, 1100, 690, 28, big=True)
for c in range(0, ymax + 1, 50000):
    b += f'<rect x="{px0}" y="{Y(c):.1f}" width="{pw}" height="1.5" fill="{LINE}"/>'
    b += text(px0 - 16, Y(c) + 7, '₹0' if c == 0 else f'₹{c / 100000:g}L', 18, MUTED, anchor='end')
for s in range(0, xmax + 1, 500000):
    b += text(X(s), py0 + ph + 34, 'No sales' if s == 0 else f'₹{s / 100000:g}L', 18, MUTED, anchor='middle')
b += text(px0 + pw / 2, py0 + ph + 72, 'Your course sales in a year', 19, INK, 600, 'middle')
b += text(px0 - 100, py0 - 28, 'Platform cost / year', 19, INK, 600)
steps = [i * 20000 for i in range(101)]


def poly(fn, col, w=4):
    pts = ' '.join(f'{X(s):.1f},{Y(min(fn(s), ymax)):.1f}' for s in steps if fn(s) <= ymax * 1.001)
    return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'


series = [(lambda s: 0.10 * s, C_EXLY, 'Exly Starter: 10%, no upfront fee'),
          (lambda s: 8999 * 12, C_LY, 'Learnyst Professional, monthly: ₹8,999/mo, 0%'),
          (lambda s: 60000 + 0.055 * s, C_TM, 'TagMango Pro: ₹5,000/mo + 5.5%'),
          (ac_best, C_AC, 'AllCoaching: lowest-cost plan for each level')]
for fn, col, _ in series:
    b += poly(fn, col, 5 if col == C_AC else 3.5)
# crossover marker near ₹5 lakh (Pro beats commission-only above ₹5L)
b += f'<circle cx="{X(500000):.1f}" cy="{Y(49999):.1f}" r="9" fill="#fff" stroke="{INK}" stroke-width="3"/>'
b += text(X(500000) - 10, Y(49999) + 52, 'About ₹5L: an annual plan', 18, INK, 600)
b += text(X(500000) - 10, Y(49999) + 76, 'starts to cost less than 10%', 18, INK, 600)
# legend (identity never by colour alone: each line is also named here)
for i, (_, col, lab) in enumerate(series):
    lx = 90 + (i % 2) * 520
    ly = 816 + (i // 2) * 36
    b += f'<rect x="{lx}" y="{ly - 9}" width="34" height="6" rx="3" fill="{col}"/>' + text(lx + 46, ly, lab, 18, INK, 500)
b += text(60, H - 50, 'Illustrative: plan price + published fee on sales, before GST, gateway charges and add-ons. Competitor figures from', 15, MUTED)
b += text(60, H - 28, 'exlyapp.com, learnyst.com and tagmango.com pricing pages, checked 24 Oct 2026.', 15, MUTED) + signature(W, H)
save('cost-chart', svg(W, H, b, 'Chart: yearly course platform cost at sales from no sales to ₹20 lakh for AllCoaching, Exly Starter, Learnyst Professional billed monthly and TagMango Pro'))

# 5. plan breakevens --------------------------------------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['Which plan costs least', 'at *your yearly sales*'], 52)
segs = [('Starter', '₹6,999/yr + 10%', 'Under ₹2.4L', 'First batches'),
        ('Growth', '₹12,999/yr + 7.5%', '₹2.4L – ₹4.8L', 'Regular batches'),
        ('Pro', '₹24,999/yr + 5%', '₹4.8L – ₹15L', 'Established academy'),
        ('Scale', '₹99,999/yr + 0%', 'Above ₹15L', 'Large academies')]
for k, (n, price, rng, who) in enumerate(segs):
    x = 60 + k * 278
    hl = k == 3
    b += white_panel(x, 220, 258, 470, 26, big=hl)
    b += f'<rect x="{x}" y="220" width="258" height="12" rx="6" fill="{BLUE if k >= 2 else "#AFC3F5"}"/>'
    b += text(x + 26, 300, n, 36, INK, 800, font=F_HEAD, ls=-1.2)
    b += text(x + 26, 340, price, 20, MUTED, 600)
    b += eyebrow(x + 26, 420, 'Lowest cost at', MUTED)
    b += text(x + 26, 470, rng, 28, BLUE, 800, font=F_HEAD, ls=-0.8)
    b += f'<rect x="{x + 26}" y="510" width="206" height="1.5" fill="{LINE}"/>'
    b += lines(x + 26, 556, [who], 20, INK, 1.4)
    if hl:
        b += lines(x + 26, 610, ['Bought through', '"Contact us"'], 18, MUTED, 1.35)
for k in range(3):
    x = 60 + (k + 1) * 278 - 10
    b += f'<circle cx="{x}" cy="455" r="16" fill="#fff" stroke="{LINE}" stroke-width="2"/>' + icon('arrow', x - 10, 445, 20, BLUE, 2.4)
b += text(60, H - 50, 'Breakevens: plan price + platform fee on sales, before GST. Starter = Growth at ₹2.4L, Growth = Pro at ₹4.8L,', 15, MUTED)
b += text(60, H - 28, 'Pro = Scale at ₹15L. Illustrative maths, not a forecast.', 15, MUTED) + signature(W, H)
save('plan-breakevens', svg(W, H, b, 'AllCoaching plan breakevens: Starter below ₹2.4 lakh, Growth ₹2.4 to ₹4.8 lakh, Pro ₹4.8 to ₹15 lakh, Scale above ₹15 lakh of yearly sales'))

# 6. costs that stay --------------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Costs that stay on', '*any platform*'], 52)
rows = [('card', 'Payment gateway charges', 'Inside or on top of the fee: check'),
        ('file', 'GST', 'Most plan prices exclude it'),
        ('puzzle', 'Add-ons', 'App, website, Zoom, branding'),
        ('trend', 'Marketing', 'Ads, content, your time'),
        ('users', 'Student support', 'Doubts, access, refunds')]
for i, (ic, t, s) in enumerate(rows):
    b += pill_card(60, 210 + i * 116, 640, t, s, ic, h=98, tile=NAVY_TILE, title_size=27)
b += white_panel(750, 210, 410, 400, 28, big=True)
b += eyebrow(782, 266, 'Ask before you sign')
qs = ['Is GST extra?', 'Are gateway charges', 'inside the fee?', 'Which add-ons do I', 'need, at what price?', 'Can I export my', 'students and content?']
b += lines(782, 322, qs, 23, INK, 1.55)
b += eyebrow(750, 666, 'Marketing still runs here', MUTED)
for k, fn in enumerate([logo_google, logo_youtube, logo_instagram, logo_whatsapp]):
    b += logo_tile(750 + k * 92, 690, fn, 72)
b += text(60, H - 28, 'General checklist. Terms differ by platform and plan. Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('costs-that-stay', svg(W, H, b, 'Costs that remain when you sell online courses on any platform: gateway charges, GST, add-ons, marketing and student support'))

# 7. decision guide -----------------------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Pick the model by', '*your stage*'], 52)
stages = [('sparkle', 'Testing an idea', 'Under ₹1L a year', 'Pay per sale, or Starter', 'Use the 14-day trial first'),
          ('trend', 'Growing', '₹1L – ₹5L a year', 'Starter or Growth', 'Annual plan, fee 10% → 7.5%'),
          ('users', 'Established', '₹5L – ₹15L a year', 'Pro (5%)', 'Compare with monthly 0% plans'),
          ('trophy', 'Large', 'Above ₹15L a year', 'A 0% plan', 'Scale, or another annual 0% plan')]
for i, (ic, st, rng, pick, note) in enumerate(stages):
    y = 200 + i * 162
    b += white_panel(60, y, 1100, 140, 26)
    b += f'<rect x="86" y="{y + 38}" width="64" height="64" rx="18" fill="{BLUE if i == 1 else NAVY_TILE}"/>' + icon(ic, 102, y + 54, 32, '#fff', 2)
    b += text(176, y + 64, st, 30, INK, 800, font=F_HEAD, ls=-1) + text(176, y + 100, rng, 21, MUTED)
    b += icon('arrow', 520, y + 54, 32, BLUE, 2.4)
    b += text(580, y + 64, pick, 30, BLUE, 800, font=F_HEAD, ls=-1) + text(580, y + 100, note, 21, MUTED)
b += text(60, H - 28, 'Illustrative guide based on plan price + fee on sales, before GST and add-ons.', 16, MUTED) + signature(W, H)
save('decision-guide', svg(W, H, b, 'Decision guide for selling online courses without a monthly subscription by yearly sales stage'))

# 8. mistakes (problem side left) ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Avoiding the', 'monthly bill like this?'], 50)
for i, t in enumerate(['Compared monthly price only', 'Forgot the add-ons', 'Ignored the % at scale', 'Never checked GST', 'No plan to export data']):
    b += tape(40 + (i % 2) * 22, 230 + i * 104, 510, t, -1.4 if i % 2 else 1.0, 29)
b += hand(300, 800, ['No fixed fee...', 'but 10% forever?'], 34, INK, -6)
b += headline(650, 190, ['Do this', '*instead.*'], 62)
for i, t in enumerate(['Compare yearly totals', 'List every add-on', 'Run your sales level', 'Add GST to every price', 'Check data export']):
    b += check_row(656, 360 + i * 78, t, 25)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Mistakes educators make when choosing a course platform without a monthly subscription, and what to do instead', ('split', 600)))

# 9. promo ---------------------------------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['One plan a year.', '*Your own*', '*academy.*'], 62)
b += lines(64, 440, ['Sign up, choose a plan, upload your', 'course, connect your domain and', 'start selling.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Your domain', 'globe', 'Website'), ('Android app', 'phone', 'Every plan'), ('Live classes', 'video', 'Unlimited'),
                                     ('UPI & cards', 'card', 'Razorpay'), ('Meta Pixel', 'chart', '+ GTM')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, 'Plans from ₹6,999/year + GST', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '14 days free · no card needed', 21, MUTED)
save('academy-annual-plan', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: one annual plan with your own domain, Android app, unlimited live classes and UPI checkout'))
