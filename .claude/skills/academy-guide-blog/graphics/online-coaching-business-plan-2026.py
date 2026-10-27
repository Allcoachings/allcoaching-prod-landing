"""Graphics for /blog/online-coaching-business-plan-2026.

Run:  python .claude/skills/academy-guide-blog/graphics/online-coaching-business-plan-2026.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/online-coaching-business-plan-2026

All rupee figures are illustrative and match the post: Growth plan ₹12,999 + 18% GST, domain ₹1,000, recording kit
₹8,000, tools ₹6,000, ads test ₹30,000 = ₹60,339 fixed; ₹2,999 course, 7.5% platform fee + assumed 2% gateway charge
= about ₹2,714 kept per sale; break-even 23 students.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'online-coaching-business-plan-2026')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


BOXES = [('users', 'Audience', 'Who, exam or goal, language'),
         ('book', 'Offer', 'Batch, course, test series'),
         ('tag', 'Pricing', 'Price per offer, the ladder'),
         ('message', 'Channels', 'Where students find you'),
         ('card', 'Costs', 'Plan, tools, ads, fees'),
         ('trend', '12-month targets', 'Enrolments, revenue')]

# 1. cover --------------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 310, ['Your coaching', 'business, *on one page.*'], 76)
b += lines(84, 480, ['An online coaching business plan for 2026,', 'with costs, break-even and a 90-day launch.'], 30, MUTED)
b += check_row(84, 620, 'A one-page template you can copy', 26)
b += check_row(84, 680, 'Illustrative cost sheet and break-even', 26)
b += check_row(84, 740, 'First 90 days and monthly metrics', 26)
b += white_panel(960, 120, 580, 680, 32, big=True)
b += eyebrow(1000, 180, 'Business plan · 2026')
for i, (ic, t, s) in enumerate(BOXES):
    y = 210 + i * 94
    tile = BLUE if i == 0 else NAVY_TILE
    b += f'<rect x="1000" y="{y}" width="500" height="80" rx="20" fill="#F6F7FC"/>'
    b += f'<rect x="1016" y="{y + 12}" width="56" height="56" rx="16" fill="{tile}"/>' + icon(ic, 1030, y + 26, 28, '#fff', 2)
    b += text(1090, y + 36, t, 24, INK, 700, font=F_HEAD, ls=-0.6) + text(1090, y + 62, s, 18, MUTED)
b += text(80, 860, 'Template and figures in the guide are illustrative.', 16, MUTED)
save('cover', svg(1600, 900, b, 'Online coaching business plan 2026: a one-page template with audience, offer, pricing, channels, costs and 12-month targets'))

# 2. one-page plan ------------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['The one-page', '*business plan*'], 54)
b += lines(62, 222, ['Six boxes, two or three lines each. Fill them in pencil.'], 22)
for i, (ic, t, s) in enumerate(BOXES):
    x = 60 + (i % 2) * 560
    y = 270 + (i // 2) * 210
    b += white_panel(x, y, 540, 186, 26)
    b += num_badge(x + 40, y + 44, i + 1, 22)
    b += text(x + 76, y + 53, t, 28, INK, 800, font=F_HEAD, ls=-0.8)
    b += icon(ic, x + 482, y + 28, 30, BLUE, 2)
    b += text(x + 32, y + 92, s, 19, MUTED)
    b += ghost_lines(x + 32, y + 116, [440, 360], 28, ('#E3E5EB',))
b += text(60, H - 28, 'Template. Write your own answers; the guide shows two filled-in examples.', 16, MUTED) + signature(W, H)
save('one-page-plan', svg(W, H, b, 'One-page online coaching business plan template with six boxes: audience, offer, pricing, channels, costs and 12-month targets'))

# 3. business models ----------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Six ways an academy', '*earns*'], 54)
models = [('users', 'Live batch', 'One fee per cohort, fixed dates'),
          ('play', 'Recorded course', 'Pay once, access for a period'),
          ('check', 'Test series', 'Mocks and sectional tests'),
          ('calendar', 'Membership', 'Pay monthly, stay while useful'),
          ('layers', 'Bundle', 'Course + tests + notes'),
          ('star', 'Mentoring', 'Small group or one to one')]
for i, (ic, t, s) in enumerate(models):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 160
    b += pill_card(x, y, 540, t, s, ic, h=124, tile=BLUE if i == 0 else NAVY_TILE, title_size=27)
b += f'<rect x="60" y="700" width="1100" height="100" rx="24" fill="{BLUE_TINT}"/>'
b += text(92, 744, 'Start with one main offer and one entry offer.', 24, INK, 700, font=F_HEAD, ls=-0.5)
b += text(92, 778, 'For example, a ₹499 test series that leads to a ₹2,999 course (illustrative).', 20, MUTED)
b += text(60, H - 28, 'Check that your platform supports recurring payments before you plan a membership.', 16, MUTED) + signature(W, H)
save('business-models', svg(W, H, b, 'Online coaching business models in India: live batches, recorded courses, test series, memberships, bundles and mentoring'))

# 4. channels -----------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Every channel ends', 'at *your checkout*'], 54)
chans = [(logo_youtube, 'YouTube', 'Teach and prove it'),
         (logo_instagram, 'Instagram', 'Reach new students'),
         (logo_whatsapp, 'WhatsApp', 'Answer and announce'),
         (logo_google, 'Google search', 'Students already looking')]
for i, (fn, t, s) in enumerate(chans):
    y = 210 + i * 140
    b += white_panel(60, y, 500, 116, 24)
    b += logo_tile(80, y + 16, fn, 84)
    b += text(190, y + 54, t, 27, INK, 700, font=F_HEAD, ls=-0.6) + text(190, y + 86, s, 19, MUTED)
    b += arrow(f'M570 {y + 58} C 640 {y + 58}, 640 470, 700 470', BLUE, 3)
b += white_panel(720, 290, 440, 380, 30, big=True)
b += f'<rect x="720" y="290" width="440" height="64" rx="30" fill="{BLUE_TINT}"/><rect x="720" y="324" width="440" height="30" fill="{BLUE_TINT}"/>'
b += text(752, 332, 'youracademy.in', 20, BLUE, 600, font=F_MONO)
b += text(752, 410, 'SSC Maths in Hindi', 28, INK, 800, font=F_HEAD, ls=-0.8)
b += text(752, 446, 'Recorded course · 12 months access', 19, MUTED)
b += text(752, 520, '₹2,999', 44, INK, 800, font=F_HEAD, ls=-1.5)
b += f'<rect x="752" y="560" width="376" height="72" rx="22" fill="{INK}"/>' + text(940, 606, 'Pay by UPI or card', 23, '#fff', 700, 'middle', F_HEAD)
b += text(60, H - 28, 'Illustrative course page. Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('channels', svg(W, H, b, 'Marketing channels in an online coaching business plan: YouTube, Instagram, WhatsApp and Google search leading to your own academy website and checkout'))

# 5. cost sheet ---------------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Year-one *cost sheet*', 'for an online academy'], 54)
fixed = [('Growth plan', '₹12,999'), ('GST on plan (18%)', '₹2,340'), ('Domain name', '₹1,000'),
         ('Recording kit', '₹8,000'), ('Design and editing tools', '₹6,000'), ('Meta ads test', '₹30,000')]
b += white_panel(60, 220, 640, 640, 28, big=True)
b += eyebrow(96, 276, 'Fixed costs, year one')
for i, (l, v) in enumerate(fixed):
    y = 340 + i * 68
    b += text(96, y, l, 23, INK, 500) + text(664, y, v, 25, INK, 700, 'end', F_HEAD)
    b += f'<rect x="96" y="{y + 24}" width="568" height="1.5" fill="{LINE}"/>'
b += f'<rect x="80" y="768" width="600" height="72" rx="20" fill="{BLUE_TINT}"/>'
b += text(104, 814, 'Fixed total', 25, INK, 700, font=F_HEAD) + text(656, 816, '₹60,339', 36, BLUE, 800, 'end', F_HEAD, -1)
b += white_panel(740, 220, 420, 400, 28)
b += eyebrow(776, 276, 'Per-sale costs')
b += text(776, 350, '7.5%', 52, INK, 800, font=F_HEAD, ls=-2) + text(776, 386, 'Platform fee on Growth', 20, MUTED)
b += text(776, 480, '2%', 52, INK, 800, font=F_HEAD, ls=-2) + text(776, 516, 'Gateway charges (assumed,', 20, MUTED)
b += text(776, 544, 'shown separately)', 20, MUTED)
b += hand(770, 700, ['Add GST', 'to your plan'], 34, INK, -4)
b += text(60, H - 28, 'Illustrative figures for planning. Replace each line with your own quotes.', 16, MUTED) + signature(W, H)
save('cost-sheet', svg(W, H, b, 'Online coaching business cost sheet for year one in India: plan and GST, domain, recording kit, tools, ads and per-sale fees'))

# 6. break-even ---------------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['How many students', 'to *break even?*'], 54)
cards = [('Fixed costs', '₹60,339', 'Year one, from the cost sheet'),
         ('Kept per sale', '₹2,714', '₹2,999 − 7.5% fee − 2% gateway'),
         ('Break-even', '23', 'paid students (22.2, rounded up)')]
for i, (t, v, s) in enumerate(cards):
    x = 60 + i * 380
    hl = i == 2
    b += white_panel(x, 250, 340, 340, 28, big=hl)
    if hl:
        b += f'<rect x="{x}" y="250" width="340" height="340" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += eyebrow(x + 32, 306, t, BLUE if hl else MUTED)
    b += text(x + 32, 420, v, 76 if hl else 60, BLUE if hl else INK, 800, font=F_HEAD, ls=-2.5)
    b += text(x + 32, 480, s, 17 if i == 1 else 19, MUTED)
for x in (420, 800):
    b += f'<circle cx="{x}" cy="420" r="22" fill="#fff" stroke="{LINE}" stroke-width="2"/>'
b += text(420, 431, '÷', 30, INK, 800, 'middle', F_HEAD) + text(800, 431, '=', 32, INK, 800, 'middle', F_HEAD)
b += f'<rect x="60" y="650" width="1100" height="96" rx="24" fill="{BLUE_TINT}"/>'
b += text(92, 708, 'Break-even students = fixed costs ÷ what you keep per sale', 26, INK, 700, font=F_HEAD, ls=-0.5)
b += text(60, H - 28, 'Illustrative figures, before income tax.', 16, MUTED) + signature(W, H)
save('break-even', svg(W, H, b, 'Online coaching break-even calculation: ₹60,339 fixed costs divided by ₹2,714 kept per ₹2,999 sale equals 23 students'))

# 7. first 90 days ------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Your first *90 days*'], 54)
b += lines(62, 168, ['From a written plan to a first paid batch.'], 22)
phases = [('Days 1–14', 'Build in the free trial', ['Sign up, build the', 'academy, upload a', 'course, connect', 'your domain']),
          ('Days 15–30', 'Launch to your audience', ['Announce on YouTube,', 'Instagram, WhatsApp;', 'run a free demo, open', 'the first batch']),
          ('Days 31–60', 'Build the content engine', ['Weekly free classes,', 'add the test series,', 'collect reviews']),
          ('Days 61–90', 'Test and adjust', ['Small Meta ads test,', 'measure cost per', 'enrolment, review', 'your prices'])]
b += f'<rect x="100" y="268" width="1020" height="4" rx="2" fill="{LINE}"/>'
for i, (d, t, s) in enumerate(phases):
    x = 60 + i * 280
    b += f'<circle cx="{x + 40}" cy="270" r="20" fill="{BLUE if i == 0 else NAVY_TILE}"/>' + text(x + 40, 278, str(i + 1), 20, '#fff', 800, 'middle', F_HEAD)
    b += white_panel(x, 320, 260, 400, 26)
    b += eyebrow(x + 26, 372, d)
    tl = t.split(' ')
    mid = (len(tl) + 1) // 2
    b += lines(x + 26, 420, [' '.join(tl[:mid]), ' '.join(tl[mid:])], 26, INK, 1.15, weight=800, font=F_HEAD, ls=-0.6)
    b += lines(x + 26, 520, s, 19, MUTED, 1.5)
b += f'<rect x="60" y="780" width="1100" height="80" rx="22" fill="{BLUE_TINT}"/>'
b += text(92, 830, 'Goal for day 90: your break-even number of students, and one channel you can measure.', 22, INK, 600)
b += text(60, H - 28, 'A guide, not a rule. Time it to your exam calendar.', 16, MUTED) + signature(W, H)
save('first-90-days', svg(W, H, b, 'First 90 days of an online coaching business: build the academy in the 7-day trial, launch to your audience, build the content engine, test ads and review'))

# 8. metrics ------------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Five numbers to check', '*every month*'], 54)
mets = [('users', 'Enrolments', 'Paid enrolments, by offer'),
        ('tag', 'Cost per enrolment', 'Ad spend ÷ enrolments from it'),
        ('chart', 'Conversion rate', 'Buyers ÷ course page visitors'),
        ('check', 'Completion rate', 'Finished ÷ enrolled'),
        ('trend', 'Repeat purchases', 'Bought a second offer ÷ all students')]
for i, (ic, t, s) in enumerate(mets):
    b += pill_card(60, 200 + i * 116, 700, t, s, ic, h=98, tile=BLUE if i == 0 else NAVY_TILE, title_size=26)
b += white_panel(800, 260, 360, 420, 28, big=True)
b += eyebrow(832, 316, 'Quick test')
b += lines(832, 372, ['Keep ₹2,714 a sale?', 'An enrolment from ads', 'at ₹300 pays for itself.', 'At ₹2,500, fix the offer', 'or the course page first.'], 22, INK, 1.6)
b += text(832, 650, 'Illustrative', 18, MUTED)
b += text(60, H - 28, 'Use the same definitions every month so the numbers compare.', 16, MUTED) + signature(W, H)
save('metrics', svg(W, H, b, 'Online coaching business metrics to track monthly: enrolments, cost per enrolment, conversion rate, completion rate and repeat purchases'))

# 9. risks --------------------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Is your plan', 'built like this?'], 56)
for i, t in enumerate(['Only one channel', 'Price never changes', 'Every rupee is live', 'GST found late', 'Tools you do not own']):
    b += tape(40 + (i % 2) * 22, 230 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(300, 800, ['Reach dropped,', 'batch is empty...'], 34, INK, -6)
b += headline(650, 190, ['Plan it', '*this way.*'], 62)
for i, t in enumerate(['Two channels + own list', 'Review price each batch', 'Add recorded + tests', 'Decide GST upfront', 'Own domain, export data']):
    b += check_row(656, 360 + i * 78, t, 25)
b += signature(W, H)
save('risks', svg(W, H, b, 'Risks in an online coaching business plan and how to reduce them: one channel, underpricing, burnout, compliance and tools you do not control', ('split', 600)))

# 10. academy promo -----------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Write the plan.', '*We run*', '*the tech.*'], 62)
b += lines(64, 440, ['Sign up, choose a plan, upload your', 'course, connect your domain and', 'start selling.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Website', 'globe', 'Your domain'), ('Your app', 'phone', 'Android'), ('Live classes', 'video', 'Unlimited'),
                                     ('UPI & cards', 'card', 'Razorpay payouts'), ('Ads tracking', 'chart', 'Pixel + GTM')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, 'From ₹3,999/month + GST', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('academy-plan', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: your own academy website, Android app, live classes and UPI checkout for your online coaching business'))
