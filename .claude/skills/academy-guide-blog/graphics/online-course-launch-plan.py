"""Graphics for /blog/online-course-launch-plan.

Run:  python .claude/skills/academy-guide-blog/graphics/online-course-launch-plan.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/online-course-launch-plan
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'online-course-launch-plan')
os.makedirs(OUT, exist_ok=True)
DASH = os.path.join(ROOT, 'landing', 'img', 'studio-dashboard.webp')       # real studio dashboard (sample educator)
MKT = os.path.join(ROOT, 'landing', 'img', 'studio-marketing.webp')        # real studio Own branding > Marketing tools

ICONS['flag'] = '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>'
ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def box(x, y, s=26):
    return f'<rect x="{x}" y="{y - s + 5}" width="{s}" height="{s}" rx="6" fill="#fff" stroke="{INK}" stroke-width="2.2"/>'


WEEKS = [('Week 1', 'Days 1–7', 'Validate'), ('Week 2', 'Days 8–14', 'Build'),
         ('Week 3', 'Days 15–21', 'Warm up'), ('Week 4', 'Days 22–30', 'Launch')]

# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Your online course', 'launch plan,', '*in 30 days.*'], 72)
b += lines(84, 536, ['A week-by-week checklist for educators.'], 28, MUTED)
b += check_row(84, 620, 'Check demand before you build', 26)
b += check_row(84, 680, 'Warm up with a free live class', 26)
b += check_row(84, 740, 'Launch honestly, then plan batch 2', 26)
b += text(910, 132, 'Studio preview · sample data', 15, MUTED)
b += laptop(910, 146, 590, DASH)
b += white_panel(850, 590, 700, 230, 28)
b += eyebrow(882, 634, 'Your 30-day launch plan')
for k, (w, d, t) in enumerate(WEEKS):
    x = 882 + k * 164
    hl = k == 3
    b += f'<rect x="{x}" y="656" width="148" height="134" rx="18" fill="{BLUE if hl else BLUE_TINT}"/>'
    b += text(x + 18, 696, w, 22, '#fff' if hl else INK, 800, font=F_HEAD, ls=-0.5)
    b += text(x + 18, 726, d, 16, '#fff' if hl else MUTED, 500)
    b += text(x + 18, 768, t, 22, '#fff' if hl else BLUE, 700, font=F_HEAD, ls=-0.4)
save('cover', svg(1600, 900, b, 'Online course launch plan for educators: a 30-day checklist in four weeks, from checking demand to launch day and batch 2'))

# 2. timeline ---------------------------------------------------------------------
W, H = 1220, 800
b = headline(60, 100, ['30 days, *four weeks*'], 56)
b += lines(62, 150, ['One result at the end of every week'], 22)
x0, x1 = 80, 1140
pd = (x1 - x0) / 30
spans = [(1, 7), (8, 14), (15, 21), (22, 30)]
cols = ['#C9D2FF', '#9DAEFF', '#6C83FF', BLUE]
for (a, z), c in zip(spans, cols):
    b += f'<rect x="{x0 + (a - 1) * pd + 2:.0f}" y="230" width="{(z - a + 1) * pd - 4:.0f}" height="26" rx="13" fill="{c}"/>'
for dday in (1, 7, 14, 21, 30):
    b += text(x0 + (dday - 0.5) * pd, 290, f'Day {dday}', 16, MUTED, 600, 'middle')
lx = x0 + 21.5 * pd
b += f'<line x1="{lx:.0f}" y1="196" x2="{lx:.0f}" y2="268" stroke="{INK}" stroke-width="3"/>'
b += f'<rect x="{lx - 2:.0f}" y="178" width="184" height="40" rx="12" fill="{INK}"/>' + icon('flag', lx + 10, 186, 24, '#fff', 2.2)
b += text(lx + 42, 205, 'Day 22: launch', 18, '#fff', 700)
cards = [('Validate', 'Days 1–7', ['One course + outcome', 'Check demand', 'Description + price']),
         ('Build', 'Days 8–14', ['Academy + course page', 'Free sample lesson', 'Payments, domain, test']),
         ('Warm up', 'Days 15–21', ['Free live class', 'Daily content', 'Waitlist + early-bird']),
         ('Launch + follow up', 'Days 22–30', ['Launch: waitlist first', 'Reminders, ads test', 'Feedback, batch 2'])]
cw, gap = 252, 18
for k, (t, d, items) in enumerate(cards):
    x = 60 + k * (cw + gap)
    hl = k == 3
    b += white_panel(x, 330, cw, 370, 24)
    if hl:
        b += f'<rect x="{x}" y="330" width="{cw}" height="370" rx="24" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += eyebrow(x + 24, 374, f'Week {k + 1} · {d}', BLUE if hl else MUTED)
    b += text(x + 24, 420, t, 27 if len(t) < 12 else 24, INK, 800, font=F_HEAD, ls=-0.8)
    for i, it in enumerate(items):
        y = 482 + i * 66
        b += f'<circle cx="{x + 32}" cy="{y - 6}" r="8" fill="{cols[k]}"/>'
        b += text(x + 48, y, it, 17, INK, 500)
b += text(60, H - 28, 'Day numbers are a guide. Keep the order.', 16, MUTED)
b += signature(W, H)
save('timeline', svg(W, H, b, '30-day online course launch plan timeline: validate, build, warm up, launch on day 22, follow up and plan batch 2'))

# 3. demand signals ---------------------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['Where demand *already shows up*'], 54)
b += lines(62, 150, ['Read these before you build a launch around a course'], 22)
chans = [('YouTube comments', logo_youtube, ['"Sir, full course kab aayega?"', '"CGL quant series please"']),
         ('Instagram comments, DMs', logo_instagram, ['"Interview English sikhate ho?"', '"Price kya hai?"']),
         ('WhatsApp questions', logo_whatsapp, ['"Notes milenge kya?"', '"Weekend batch hoga?"'])]
for k, (t, fn, cs) in enumerate(chans):
    x = 60 + k * 370
    b += white_panel(x, 196, 350, 400, 28)
    b += logo_tile(x + 28, 222, fn, 72)
    b += text(x + 28, 336, t, 24, INK, 800, font=F_HEAD, ls=-0.6)
    for i, c in enumerate(cs):
        y = 372 + i * 100
        b += f'<rect x="{x + 28}" y="{y}" width="294" height="76" rx="18" fill="#F1F2F7"/>'
        b += text(x + 46, y + 46, c, 17, INK, 500)
b += f'<g filter="url(#shB)"><rect x="60" y="630" width="1100" height="96" rx="24" fill="{BLUE}"/></g>'
b += icon('list', 92, 658, 40, '#fff', 2)
b += text(152, 672, "Note each request in the student's own words.", 26, '#fff', 800, font=F_HEAD, ls=-0.7)
b += text(152, 704, 'Those words go into your course description and launch posts.', 19, '#fff', opacity=.88)
b += text(60, H - 28, 'Illustrative comments. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('demand-signals', svg(W, H, b, 'Where to check demand before an online course launch: YouTube comments, Instagram comments and DMs, WhatsApp questions'))

# 4. week cards -------------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['What to finish *each week*'], 56)
b += lines(62, 150, ['Your online course launch checklist, week by week'], 22)
wk = [('Validate and prepare', ['Pick one course and outcome', 'Read comments and WhatsApp', 'Write the description', 'Set price and early-bird date']),
      ('Build', ['Academy, brand and theme', 'Course page + free lesson', 'UPI checkout and domain', 'Test purchase on a phone']),
      ('Warm up', ['Announce a free live class', 'Waitlist via a lead form', 'Post daily, tag every link', 'Teach the class on day 20']),
      ('Launch and follow up', ['Launch day: waitlist first', 'Two or three useful reminders', 'Optional small ads test', 'Feedback, fixes, batch 2'])]
for k, (t, items) in enumerate(wk):
    col, row = k % 2, k // 2
    x, y = 60 + col * 560, 196 + row * 400
    b += white_panel(x, y, 540, 370, 28)
    b += eyebrow(x + 32, y + 50, f'{WEEKS[k][0]} · {WEEKS[k][1]}', BLUE)
    b += text(x + 32, y + 100, t, 32, INK, 800, font=F_HEAD, ls=-1)
    for i, it in enumerate(items):
        b += check_row(x + 32, y + 168 + i * 54, it, 21)
b += signature(W, H)
save('week-cards', svg(W, H, b, 'Online course launch checklist by week: validate and prepare, build, warm up, launch and follow up'))

# 5. honest urgency ---------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['Urgency that *keeps trust*'], 56)
b += lines(62, 150, ['Students in one WhatsApp group compare notes'], 22)
good = ['Early-bird ends on the date announced', 'Batch starts on a fixed day', 'Live doubt slots you really have', 'One price for everyone in the group']
bad = ['A countdown that resets on refresh', '"Only 3 seats" on a recorded course', 'A price rise that never happens', '"Last chance" every single week']
for k, (t, items, ok) in enumerate([('Honest urgency', good, True), ('Fake urgency', bad, False)]):
    x = 60 + k * 560
    b += white_panel(x, 196, 540, 440, 28)
    b += eyebrow(x + 32, 248, 'Do this' if ok else 'Never do this', BLUE if ok else RED)
    b += text(x + 32, 300, t, 32, INK, 800, font=F_HEAD, ls=-1)
    for i, it in enumerate(items):
        b += check_row(x + 32, 380 + i * 70, it, 21, ok)
b += white_panel(60, 666, 1100, 96, 24)
b += f'<rect x="84" y="682" width="64" height="64" rx="16" fill="{BLUE_TINT}"/>' + icon('clock', 100, 698, 32, BLUE, 2)
b += text(172, 708, 'Illustrative early-bird: ₹1,499 until day 28, then ₹1,999.', 23, INK, 700, font=F_HEAD, ls=-0.5)
b += text(172, 738, 'Announce the end date before launch day, and close it on that date.', 18, MUTED)
b += signature(W, H)
save('honest-urgency', svg(W, H, b, 'Honest urgency for an online course launch: real early-bird end date, fixed batch start, real live slots, versus fake countdowns and invented seat limits'))

# 6. tracking: pixel before launch ------------------------------------------------
W, H = 1220, 930
b = headline(60, 100, ['Add your pixel *before launch*'], 54)
b += lines(62, 150, ['Own branding  ›  Marketing tools, in the studio'], 22, INK)
b += laptop(80, 214, 620, MKT)
b += text(80, 690, 'Studio preview · sample data', 15, MUTED)
st = [('Add your Meta Pixel ID', ['Facebook and Instagram ads', 'see visits and sales']),
      ('Add your GTM container', ['Google Ads, GA4 and more', 'through one ID']),
      ('Launch with data ready', ['Reach page visitors who', 'did not pay yet'])]
for k, (t, s) in enumerate(st):
    y = 214 + k * 150
    b += num_badge(788, y + 22, k + 1, 22)
    b += text(824, y + 31, t, 25, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(824, y + 66, s, 19, MUTED, 1.35)
for k, (t, s, ic) in enumerate([('Track enrolments', 'purchases from each ad', 'chart'),
                                 ('Retarget visitors', 'who opened the page', 'users'),
                                 ('Tag every link', 'with UTM parameters', 'link')]):
    b += pill_card(60 + k * 374, 740, 352, t, s, ic, h=104, tile=BLUE if k == 0 else NAVY_TILE, title_size=24)
b += signature(W, H)
save('tracking', svg(W, H, b, 'AllCoaching studio Marketing tools: add your own Meta Pixel and Google Tag Manager before a course launch'))

# 7. launch funnel ----------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['The launch funnel, *illustrated*'], 54)
b += lines(62, 150, ['Each stage is smaller than the one before. That is normal.'], 22)
stages = [(1000, '1,000 people reached by your posts', '#DDE3FF', INK),
          (200, '200 join the waitlist', '#B3C0FF', INK),
          (80, '80 attend the free live class', '#6C83FF', '#fff'),
          (12, '12 enrol at launch', BLUE, '#fff')]
cx = 520
for k, (n, t, c, tc) in enumerate(stages):
    w = 880 - k * 170
    y = 200 + k * 120
    b += f'<g filter="url(#sh)"><rect x="{cx - w / 2}" y="{y}" width="{w}" height="96" rx="24" fill="{c}"/></g>'
    b += text(cx, y + 58, t, 25, tc, 800, 'middle', F_HEAD, -0.6)
b += white_panel(900, 560, 260, 96, 24)
b += eyebrow(924, 598, 'Everyone else')
b += text(924, 634, 'Batch 2 waitlist', 22, INK, 800, font=F_HEAD, ls=-0.5)
b += arrow('M 776 608 L 880 608', BLUE, 4)
b += white_panel(60, 712, 1100, 96, 24)
b += text(92, 754, 'Illustrative: 12 × ₹1,499 = ₹17,988.', 24, INK, 800, font=F_HEAD, ls=-0.6)
b += text(92, 786, 'On a monthly plan, 0% commission: all of it is yours, before GST and gateway charges.', 18, MUTED)
b += text(60, H - 28, 'Illustrative numbers, not a forecast or benchmark.', 16, MUTED)
b += signature(W, H)
save('launch-funnel', svg(W, H, b, 'Online course launch funnel with illustrative numbers: 1,000 reached, 200 waitlist, 80 at the free live class, 12 enrolments, the rest to batch 2'))

# 8. printable checklist ----------------------------------------------------------
W, H = 1220, 930
b = headline(60, 100, ['Your 30-day *launch checklist*'], 54)
b += lines(62, 150, ['Print it. Tick a task when it is done, not when it is started.'], 22)
b += white_panel(60, 190, 1100, 680, 28)
groups_l = [('Week 1 · Validate', ['One course, one outcome', 'YouTube live streaming checked', 'Demand list in students\' words', 'Description written', 'Price and early-bird date set']),
            ('Week 2 · Build', ['Academy, logo, colours, theme', 'Course page published', 'Free sample lesson live', 'UPI checkout, domain, pixel', 'Test purchase on a phone'])]
groups_r = [('Week 3 · Warm up', ['Free live class announced', 'Waitlist form open', 'Seven posts, links tagged', 'Free class taught (day 20)']),
            ('Day 22 · Launch', ['Waitlist messaged first', 'Public posts, one link']),
            ('Week 4 · Follow up', ['Useful reminders sent', 'Early-bird closed on time', 'Feedback in, top fixes done', 'Batch 2 date and waitlist'])]
for col, groups in enumerate([groups_l, groups_r]):
    x = 100 + col * 540
    y = 250
    for g, items in groups:
        b += eyebrow(x, y, g, BLUE)
        y += 44
        for it in items:
            b += box(x, y) + text(x + 42, y, it, 20, INK, 500)
            y += 44
        y += 24
b += signature(W, H)
save('checklist', svg(W, H, b, 'Printable 30-day online course launch checklist for educators with tick boxes for each week and launch day'))

# 9. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Launch mistakes', 'that cost you.'], 52)
for i, t in enumerate(['No test purchase', 'Five courses at once', 'No warm-up week', 'Link to a WhatsApp no.', 'Fake countdowns']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 510, t, -1.4 if i % 2 else 1.0, 28)
b += hand(330, 790, ['Why did nobody', 'pay?'], 40, INK, -6) + arrow('M300 800 C 250 820, 210 800, 190 770', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Buy it yourself on day 14', 'One course, one outcome', 'A free live class first', 'One link: the course page', 'A real early-bird date']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Common online course launch mistakes and what to do instead', ('split', 600)))
