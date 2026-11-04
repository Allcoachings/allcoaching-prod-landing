"""Graphics for /blog/grow-online-coaching-students.

Run:  python .claude/skills/academy-guide-blog/graphics/grow-online-coaching-students.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/grow-online-coaching-students

Every number drawn here is illustrative (fictional academy, ₹3,000 average ticket) and computed
with the current AllCoaching plan maths (references/02-pricing.md).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'grow-online-coaching-students')
os.makedirs(OUT, exist_ok=True)

ICONS['refresh'] = '<path d="M20 11a8 8 0 00-14.3-4.9L4 8"/><path d="M4 3v5h5"/><path d="M4 13a8 8 0 0014.3 4.9L20 16"/><path d="M20 21v-5h-5"/>'
ICONS['help'] = '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 114 2c-.9.6-1.5 1.1-1.5 2.2M12 17h.01"/>'
ICONS['award'] = '<circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def card(x, y, w, h, r=24):
    return white_panel(x, y, w, h, r)


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Grow from *50 to 1,000*', 'students.'], 70)
b += lines(84, 450, ['A three-stage plan for your online coaching'], 27, MUTED)
b += check_row(84, 548, 'Retention and word of mouth first', 26)
b += check_row(84, 608, 'Systems, tests and a team next', 26)
b += check_row(84, 668, 'Channels and ads once the maths works', 26)
extra = {'1': [], '2': ['Batches, tests', 'Team seats', 'Live timetable'], '3': ['YouTube, ads', 'Referrals', 'Second tier', 'Own app', 'Partners']}
steps = [(900, 560, '1', '50 → 150', 'Retention', 'refresh'),
         (1100, 430, '2', '150 → 400', 'Systems', 'layers'),
         (1300, 290, '3', '400 → 1,000', 'Channels', 'trend')]
for x, y, n, rng, job, ic in steps:
    b += white_panel(x, y, 190, 760 - y, 22, big=True)
    b += f'<rect x="{x + 22}" y="{y + 24}" width="56" height="56" rx="16" fill="{NAVY_TILE if n != "3" else BLUE}"/>' + icon(ic, x + 36, y + 38, 28, '#fff')
    b += text(x + 22, y + 122, rng, 25, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(x + 22, y + 154, job, 21, BLUE, 600)
    for k, t in enumerate(extra[n]):
        b += text(x + 22, y + 200 + k * 30, t, 18, MUTED)
b += f'<rect x="880" y="760" width="630" height="4" rx="2" fill="{LINE}"/>'
b += text(900, 800, 'Illustrative roadmap · students, not guarantees', 16, MUTED)
save('cover', svg(1600, 900, b, 'Grow online coaching from 50 to 1,000 students: a three-stage staircase of retention, systems and channels'))

# 2. staircase --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Three stages, *three jobs*'], 54)
b += lines(62, 150, ['Each stage fixes what would break the next one'], 22)
stages = [(60, 430, '50 → 150', 'Fix retention', 'refresh', NAVY_TILE,
           ['Course completion', 'Doubt replies in a day', 'Track every result', 'Real reviews, with consent']),
          (435, 330, '150 → 400', 'Build systems', 'layers', NAVY_TILE,
           ['Batches with dates', 'Test series, rank, %ile', 'Fixed live timetable', 'Team seats, bulk import']),
          (810, 230, '400 → 1,000', 'Add channels', 'trend', BLUE,
           ['Weekly YouTube rhythm', 'Ads when CPA pays back', 'Referrals, partners', 'Second tier, own app'])]
for x, y, rng, job, ic, tile, bullets in stages:
    b += white_panel(x, y, 350, 800 - y, 26, big=True)
    b += f'<rect x="{x + 28}" y="{y + 28}" width="60" height="60" rx="16" fill="{tile}"/>' + icon(ic, x + 44, y + 44, 28, '#fff')
    b += text(x + 104, y + 70, rng, 32, INK, 800, font=F_HEAD, ls=-1)
    b += text(x + 28, y + 132, job, 26, BLUE, 700, font=F_HEAD, ls=-0.6)
    for k, t in enumerate(bullets):
        yy = y + 186 + k * 46
        b += f'<circle cx="{x + 36}" cy="{yy - 6}" r="5" fill="{BLUE}"/>' + text(x + 52, yy, t, 20, INK, 500)
b += text(60, 850, 'Illustrative ranges. Your numbers depend on subject, price and consistency.', 17, MUTED)
b += signature(W, H)
save('growth-staircase', svg(W, H, b, 'Three stages to grow online coaching students: retention, systems and channels'))

# 3. retention loop ---------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['The *retention loop*'], 54)
b += lines(62, 150, ['Students who finish and get results bring the next students'], 22)
nodes = [(425, 200, 'Enrol', 'Clear start date', 'users', NAVY_TILE),
         (790, 420, 'Complete', 'Short lessons, tests', 'check', NAVY_TILE),
         (680, 680, 'Get results', 'Scores tracked', 'trophy', NAVY_TILE),
         (170, 680, 'Renew', 'Next course or batch', 'refresh', NAVY_TILE),
         (60, 420, 'Refer', 'Reviews, with consent', 'message', BLUE)]
for x, y, t, s, ic, tile in nodes:
    b += pill_card(x, y, 370, t, s, ic, h=104, tile=tile, title_size=26)
b += arrow('M800 290 Q 900 330 925 410', BLUE, 4)
b += arrow('M1000 532 Q 995 610 940 668', BLUE, 4)
b += arrow('M672 732 L 552 732', BLUE, 4)
b += arrow('M250 672 Q 200 620 214 536', BLUE, 4)
b += arrow('M220 412 Q 250 290 416 258', BLUE, 4)
b += headline(610, 470, ['Word of', '*mouth*'], 44, 'middle')
b += text(610, 580, 'The easiest student to win', 20, MUTED, anchor='middle')
b += text(610, 608, 'is the one a student sends you', 20, MUTED, anchor='middle')
b += text(60, 880, 'Each loop that closes makes the next enrolment easier.', 18, MUTED)
b += signature(W, H)
save('retention-loop', svg(W, H, b, 'Retention loop for online coaching: enrol, complete, get results, renew and refer'))

# 4. metrics dashboard ------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Six numbers, *every month*'], 54)
b += lines(62, 150, ['Write them in one sheet on the 1st of every month'], 22)
tiles = [('Enrolments', '62', 'new paid students this month', 'users'),
         ('Completion rate', '58%', 'finished ÷ enrolled × 100', 'check'),
         ('Renewal rate', '41%', 'bought next ÷ finished × 100', 'refresh'),
         ('CPL / CPA', '₹50 / ₹1,000', 'ad spend ÷ leads  ·  ÷ paid', 'tag'),
         ('Refund rate', '2%', 'refunds ÷ paid enrolments × 100', 'card'),
         ('LTV', '₹4,500', 'avg ticket × purchases each', 'trend')]
for i, (lab, val, f, ic) in enumerate(tiles):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 200 + row * 210
    b += card(x, y, 540, 186)
    b += f'<rect x="{x + 28}" y="{y + 28}" width="52" height="52" rx="14" fill="{BLUE_TINT}"/>' + icon(ic, x + 40, y + 40, 28, BLUE, 2)
    b += text(x + 98, y + 62, lab, 24, INK, 700, font=F_HEAD, ls=-0.5)
    b += text(x + 28, y + 136, val, 44, INK, 800, font=F_HEAD, ls=-1.6)
    b += text(x + 512, y + 162, f, 16, MUTED, 500, 'end', F_MONO)
b += text(60, 880, 'Illustrative numbers for a fictional academy, not benchmarks or real results.', 17, MUTED)
b += text(60, 908, 'LTV = lifetime value. CPL = cost per lead. CPA = cost per paid enrolment.', 17, MUTED)
b += signature(W, H)
save('metrics-dashboard', svg(W, H, b, 'Online coaching growth metrics: enrolments, completion rate, renewal rate, CPL and CPA, refund rate and LTV with formulas'))

# 5. unit economics ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Do the ads *pay back*?'], 54)
b += lines(62, 150, ['One illustrative month of Meta ads for a ₹3,000 course'], 22)
b += card(60, 196, 640, 640)
rows = [('Ad spend', '₹20,000', None), ('Leads (form or WhatsApp)', '400', 'CPL ₹50'),
        ('Paid enrolments', '20', 'CPA ₹1,000'), ('First purchase per student', '₹3,000', None),
        ('Purchases per student (avg)', '1.5', None), ('Lifetime value (LTV)', '₹4,500', 'LTV ÷ CPA = 4.5')]
for i, (lab, val, note) in enumerate(rows):
    y = 256 + i * 88
    if i:
        b += f'<rect x="92" y="{y - 52}" width="576" height="1.5" fill="{LINE}"/>'
    b += text(92, y, lab, 22, INK, 500)
    b += text(668, y, val, 30, INK, 800, 'end', F_HEAD, -0.8)
    if note:
        b += text(92, y + 28, note, 17, BLUE, 600, font=F_MONO)
b += f'<rect x="92" y="786" width="24" height="24" rx="12" fill="{GREEN}"/>' + icon('tick', 96, 790, 16, '#fff', 3)
b += text(130, 805, 'Each student pays back the ad cost 3 times on the first sale', 18, INK, 600)
b += text(740, 230, 'What you keep of ₹3,000', 24, INK, 800, font=F_HEAD, ls=-0.6)
b += text(740, 258, 'Per sale, before GST and gateway', 16, MUTED)
keep = [('Any monthly plan', '0%', '₹3,000', BLUE), ('Yearly Pro', '5%', '₹2,850', NAVY_TILE),
        ('Yearly Growth', '7.5%', '₹2,775', NAVY_TILE), ('Yearly Starter', '10%', '₹2,700', NAVY_TILE)]
for i, (p, fee, k, col) in enumerate(keep):
    y = 296 + i * 128
    b += card(740, y, 420, 108, 22)
    b += f'<rect x="762" y="{y + 26}" width="76" height="56" rx="16" fill="{col}"/>' + text(800, y + 62, fee, 21, '#fff', 800, 'middle', F_HEAD)
    b += text(858, y + 48, p, 22, INK, 700, font=F_HEAD, ls=-0.5)
    b += text(858, y + 80, 'keep ' + k, 20, MUTED)
b += text(60, 900, 'Illustrative numbers. Fees per AllCoaching plan as of November 2026; prices + 18% GST.', 17, MUTED)
b += text(60, 928, 'Payment-gateway charges on student payments are separate.', 17, MUTED)
b += signature(W, H)
save('unit-economics', svg(W, H, b, 'Unit economics for online coaching ads: ad spend, leads, CPL, paid enrolments, CPA and lifetime value, plus what you keep per sale on each plan'))

# 6. plan by stage ----------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['A plan for *each stage*'], 54)
b += lines(62, 150, ['Choose by needs first, then by cost'], 22)
plans = [('50 → 150', '₹1.5–4.5 lakh a year', 'Yearly Starter', '₹6,999/yr + 10% per sale', ['3 team seats', '512 GB storage', 'Own Android + iOS app'], NAVY_TILE),
         ('150 → 400', '₹4.5–12 lakh a year', 'Monthly Growth', '₹5,999/mo · 0% commission', ['5 team seats', '1 TB · 50 h live', 'Own Android app'], NAVY_TILE),
         ('400 → 1,000', '₹12–30 lakh a year', 'Monthly Pro', '₹7,999/mo · 0% commission', ['7 team seats', '2 TB · 4K · 90 h live', 'Own Android + iOS app'], BLUE)]
for i, (rng, sales, plan, price, feats, col) in enumerate(plans):
    y = 200 + i * 200
    b += card(60, y, 1100, 176)
    b += f'<rect x="60" y="{y}" width="10" height="176" rx="5" fill="{col}"/>'
    b += text(100, y + 74, rng, 34, INK, 800, font=F_HEAD, ls=-1.2)
    b += text(100, y + 110, 'Sales ' + sales, 18, MUTED)
    b += text(440, y + 74, plan, 28, BLUE if col == BLUE else INK, 800, font=F_HEAD, ls=-0.8)
    b += text(440, y + 110, price, 20, INK, 500)
    for k, f in enumerate(feats):
        b += check_row(800, y + 52 + k * 42, f, 19)
b += text(60, 836, 'Illustrative at ₹3,000 a student. Prices + 18% GST. 7-day free trial, no card. No sales limit.', 17, MUTED)
b += text(60, 864, 'Below about ₹4 lakh a year yearly Starter usually costs least; above that a monthly plan usually leaves more.', 17, MUTED)
b += signature(W, H)
save('plan-by-stage', svg(W, H, b, 'AllCoaching plan by growth stage: yearly Starter, monthly Growth and monthly Pro with seats, storage, live hours and apps'))

# 7. team org ---------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Who you hire, *and when*'], 54)
b += lines(62, 150, ['Hire at a clear signal, not at a student count'], 22)
b += pill_card(435, 196, 350, 'You', 'Founder and head teacher', 'star', h=104, tile=BLUE, title_size=28)
b += f'<path d="M610 300 V 350 M235 350 H 985 M235 350 V 404 M610 350 V 404 M985 350 V 404" stroke="{BLUE}" stroke-width="3" fill="none" stroke-linecap="round"/>'
team = [(60, 'Second teacher', 'Live classes, a subject', 'users', ['Your live hours crowd out', 'new content and tests']),
        (435, 'Support person', 'Doubts, fees, WhatsApp', 'message', ['Messages take you two', 'or more hours a day']),
        (810, 'Content and ops', 'Uploads, tests, notes', 'layers', ['Tests and notes reach', 'students late'])]
for x, t, s, ic, sig in team:
    b += pill_card(x, 404, 350, t, s, ic, h=104, tile=NAVY_TILE, title_size=25)
    b += card(x, 540, 350, 150, 22)
    b += eyebrow(x + 28, 584, 'Hire when')
    b += lines(x + 28, 624, sig, 20, INK, 1.45, weight=500)
b += card(60, 730, 1100, 96, 22)
b += icon('users', 92, 764, 30, BLUE, 2)
b += text(140, 786, 'Team seats (you included): Starter 3 · Growth 5 · Pro 7', 23, INK, 600)
b += text(60, 880, 'Signals are a practical guide from our side, not rules. Each person gets their own studio login.', 17, MUTED)
b += signature(W, H)
save('team-org', svg(W, H, b, 'Online coaching team structure: founder, second teacher, support person and content and operations, with the signal to hire each'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['What stalls', 'growth.'], 54)
for i, t in enumerate(['Ads before retention', 'A discount every batch', 'One teacher does it all', 'No numbers tracked', 'Made-up testimonials']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 510, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 790, ['Busy, but', 'not growing.'], 40, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Fix completion first', 'Price tiers, not discounts', 'Hire at a clear signal', 'Six numbers, monthly', 'Real reviews, with consent']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Mistakes that stall online coaching growth and what to do instead', ('split', 600)))
