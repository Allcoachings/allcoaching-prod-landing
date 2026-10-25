"""Graphics for /blog/how-to-start-online-academy-in-5-steps.

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-start-online-academy-in-5-steps.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-start-online-academy-in-5-steps
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'how-to-start-online-academy-in-5-steps')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


STEPS = [('Plan your academy', 'One exam or skill, one first course', 'list'),
         ('Sign up, choose a plan', '14-day free trial, no card', 'users'),
         ('Upload your course', 'Videos, PDF notes, tests, live', 'play'),
         ('Connect your domain', 'youracademy.in, logo, colours', 'globe'),
         ('Start selling', 'UPI checkout, share one link', 'trend')]

# 1. cover ----------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Start your', '*online academy*', 'in 5 steps.'], 84)
b += lines(84, 560, ['A practical guide for Indian educators.'], 30, MUTED)
for i, (t, _, _) in enumerate(STEPS):
    b += num_badge(100, 628 + i * 52, i + 1, 17)
    b += text(130, 636 + i * 52, t, 24, INK, 600, font=F_HEAD, ls=-0.4)
b += text(880, 196, 'Studio preview · sample data', 15, MUTED)
b += laptop(880, 210, 580, 'studio-courses.jpg')
b += phone(1380, 360, 150, 'studio-mobile.jpg')
b += pill_card(820, 650, 420, 'youracademy.in', 'Your domain, your brand', 'globe')
save('cover', svg(1600, 900, b, 'How to start an online academy in 5 steps: plan, sign up, upload your course, connect your domain, start selling'))

# 2. roadmap ----------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['The *5-step* roadmap'], 56)
b += lines(62, 150, ['From an idea to your first paid student, in order.'], 22)
b += f'<path d="M118 230 V 850" stroke="{BLUE}" stroke-width="3" stroke-dasharray="5 8"/>'
when = ['Day 1', 'Day 1', 'Days 2–7', 'Day 7', 'Day 8 onward']
for i, (t, s, ic) in enumerate(STEPS):
    y = 200 + i * 132
    b += white_panel(170, y, 990, 108, 26)
    b += num_badge(118, y + 54, i + 1, 26)
    b += f'<rect x="196" y="{y + 22}" width="64" height="64" rx="18" fill="{NAVY_TILE}"/>' + icon(ic, 212, y + 38, 32, '#fff', 2)
    b += text(286, y + 50, t, 30, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(286, y + 82, s, 20, MUTED)
    b += f'<rect x="{1130 - 190}" y="{y + 34}" width="190" height="40" rx="20" fill="{BLUE_TINT}"/>' + text(1035, y + 61, when[i], 18, BLUE, 700, 'middle', F_HEAD)
b += text(60, H - 28, 'Illustrative timeline for one educator with one course. Yours may be faster or slower.', 16, MUTED)
b += signature(W, H)
save('roadmap', svg(W, H, b, 'Roadmap: the five steps to start an online academy, with an illustrative timeline from day 1 to the first sale'))

# 3. before / after ------------------------------------------------------------------
W, H = 1220, 940
b = headline(56, 110, ['Starting like', 'this?'], 58)
b += logo_tile(206, 120, logo_whatsapp, 58) + logo_tile(276, 120, logo_youtube, 58)
for i, t in enumerate(['Fees on WhatsApp', 'Notes as Drive links', 'Zoom link every day', 'Students in Excel', 'Who paid? Not sure']):
    b += tape(40 + (i % 2) * 22, 250 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(330, 820, ['Five tools,', 'five logins.'], 40, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['One login.', '*Your whole academy.*'], 52)
for i, t in enumerate(['Fees collected at UPI checkout', 'Videos, notes, tests in courses', 'Live classes from the studio', 'Every student on record', 'Your domain, your app']):
    b += check_row(656, 380 + i * 74, t, 25)
b += text(656, 800, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('before-after', svg(W, H, b, 'Before: fees on WhatsApp, notes on Drive, Zoom links and Excel. After: one online academy login', ('split', 600)))

# 4. what you need ---------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['What you need *before you start*'], 50)
b += lines(62, 150, ['Eight things. Most educators already have six.'], 22)
need = [('One topic you teach well', 'An exam, subject or skill', 'trophy'),
        ('A syllabus for one course', 'Chapters, lessons and tests', 'list'),
        ('One demo lesson', '10 to 20 minutes, free', 'play'),
        ('A phone and a clip-on mic', 'Good audio beats a camera', 'mic'),
        ('PAN and a bank account', 'For payment KYC', 'card'),
        ('A domain name', 'youracademy.in, in your name', 'globe'),
        ('A logo and two colours', 'Simple is fine to start', 'image'),
        ('A few hours each week', 'To record, teach and reply', 'calendar')]
for i, (t, s, ic) in enumerate(need):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 170
    b += pill_card(x, y, 540, t, s, ic, h=130, tile=BLUE_TINT if i % 3 else NAVY_TILE, title_size=25)
b += signature(W, H)
save('what-you-need', svg(W, H, b, 'Checklist of what you need before you start an online academy: topic, syllabus, demo lesson, mic, PAN and bank account, domain, logo and time'))

# 5. first course structure -----------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Structure your *first course*'], 54)
b += lines(62, 150, ['Example: SSC CGL Quant, Hindi medium (illustrative)'], 22)
b += f'<g filter="url(#shB)"><rect x="410" y="200" width="400" height="96" rx="26" fill="{BLUE}"/></g>'
b += text(610, 242, 'SSC CGL Quant · Hindi', 26, '#fff', 800, 'middle', F_HEAD, -0.6)
b += text(610, 274, 'One course, sold at one price', 18, '#DCE2FF', anchor='middle')
mods = [('Module 1', 'Number system', ['8 video lessons', 'PDF formula sheet', 'Chapter test']),
        ('Module 2', 'Percentage, ratio', ['10 video lessons', 'PDF practice set', 'Chapter test']),
        ('Module 3', 'Algebra, geometry', ['12 video lessons', 'PDF notes', 'Chapter test']),
        ('Module 4', 'Full mocks', ['5 timed mock tests', 'Video solutions', 'Live doubt class'])]
for i, (e_, t, items) in enumerate(mods):
    x = 60 + i * 280
    b += f'<path d="M610 296 V 340 H {x + 130} V 380" fill="none" stroke="{BLUE}" stroke-width="2.5"/>'
    b += white_panel(x, 380, 260, 330, 24)
    b += eyebrow(x + 26, 424, e_)
    b += text(x + 26, 464, t, 23, INK, 800, font=F_HEAD, ls=-0.6)
    for k, it in enumerate(items):
        ic = ['play', 'file', 'check'][k] if i < 3 else ['check', 'play', 'video'][k]
        b += f'<rect x="{x + 26}" y="{500 + k * 64}" width="44" height="44" rx="12" fill="{BLUE_TINT}"/>' + icon(ic, x + 36, 510 + k * 64, 24, BLUE, 2)
        b += text(x + 84, 529 + k * 64, it, 18, INK, 500)
b += white_panel(60, 750, 1100, 120, 24)
b += f'<rect x="88" y="780" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon('star', 104, 796, 28, '#fff', 2)
b += text(172, 806, 'Lesson 1 is free: your demo lesson', 25, INK, 800, font=F_HEAD, ls=-0.6)
b += text(172, 840, 'Students judge your teaching here before they pay.', 19, MUTED)
b += signature(W, H)
save('first-course', svg(W, H, b, 'How to structure the first course of an online academy: four modules with video lessons, PDF notes, chapter tests, mocks and a free demo lesson'))

# 6. studio upload (annotated screenshot) ------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Upload once. *It stays organised.*'], 50)
b += lines(62, 150, ['Courses in the studio bundle videos, PDFs and tests.'], 22)
b += text(90, 206, 'Studio preview · sample data', 15, MUTED)
b += laptop(100, 222, 680, 'studio-courses.jpg')
calls = [('New course', 'Name it and set the price', 'tag'),
         ('Add content', 'YouTube videos, PDFs, tests', 'layers'),
         ('Free demo', 'Share one lesson for free', 'star'),
         ('Publish', 'Draft until you are ready', 'bolt')]
for i, (t, s, ic) in enumerate(calls):
    y = 220 + i * 128
    b += white_panel(850, y, 320, 108, 22)
    b += num_badge(884, y + 54, i + 1)
    b += text(920, y + 48, t, 23, INK, 800, font=F_HEAD, ls=-0.5)
    b += text(920, y + 78, s, 16, MUTED)
b += f'<g filter="url(#sh)"><rect x="90" y="760" width="740" height="120" rx="24" fill="{NAVY_TILE}"/></g>'
b += eyebrow(122, 806, 'Every plan', '#9FB0FF')
b += text(122, 846, 'Unlimited videos via YouTube · unlimited live classes', 22, '#fff', 700, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('studio-upload', svg(W, H, b, 'Uploading the first course in the AllCoaching studio: create a course, add YouTube videos, PDFs and tests, mark a free demo lesson and publish'))

# 7. domain connection ---------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Connect *your own domain*'], 54)
b += lines(62, 150, ['Two DNS records at your registrar. No developer.'], 22)
cols = [('1', 'Buy the domain', ['At any registrar,', 'in your own name'], 'tag'),
        ('2', 'Add DNS records', ['The values your', 'platform shows you'], 'server'),
        ('3', 'Wait, then check', ['Minutes to a day,', 'then open your site'], 'shield')]
for i, (n, t, s, ic) in enumerate(cols):
    x = 60 + i * 375
    b += white_panel(x, 200, 350, 290, 26)
    b += num_badge(x + 46, 246, n)
    b += f'<rect x="{x + 30}" y="290" width="68" height="68" rx="18" fill="{NAVY_TILE}"/>' + icon(ic, x + 46, 306, 36, '#fff', 2)
    b += text(x + 30, 404, t, 27, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(x + 30, 440, s, 19, MUTED, 1.4)
    if i < 2:
        b += arrow(f'M{x + 354} 345 H {x + 372}', BLUE, 3)
b += white_panel(60, 530, 1100, 250, 26)
b += eyebrow(92, 578, 'Example DNS records (illustrative values)')
hdr = ['Type', 'Name', 'Points to / value']
xs = [92, 262, 492]
for k, hh in enumerate(hdr):
    b += text(xs[k], 624, hh, 18, MUTED, 600)
rows = [('TXT', '@ or _verify', 'verification code from your platform'), ('CNAME', 'www', 'the address your platform gives you')]
for r, row in enumerate(rows):
    y = 676 + r * 62
    b += f'<line x1="92" y1="{y - 34}" x2="1128" y2="{y - 34}" stroke="{LINE}" stroke-width="2"/>'
    b += f'<rect x="92" y="{y - 26}" width="110" height="38" rx="10" fill="{BLUE_TINT}"/>' + text(147, y, row[0], 18, BLUE, 700, 'middle', F_MONO)
    b += text(262, y, row[1], 19, INK, 500, font=F_MONO) + text(492, y, row[2], 19, INK, 500)
b += text(60, H - 28, 'Record names and values differ by platform; copy them exactly from your settings page.', 16, MUTED)
b += signature(W, H)
save('domain-connection', svg(W, H, b, 'How to connect your own domain to an online academy: buy the domain, add TXT and CNAME DNS records, then wait for it to go live'))

# 8. payment flow -------------------------------------------------------------------------------
W, H = 1220, 880
b = headline(60, 100, ['What happens when a *student pays*'], 52)
b += lines(62, 150, ['Four things, none of which need you.'], 22)
flow = [('Student taps Buy', 'On your site or app', 'phone'),
        ('Pays by UPI or card', 'Google Pay, PhonePe, cards', 'card'),
        ('Access opens', 'Course unlocks itself', 'shield'),
        ('Payout to your bank', 'Automatic via Razorpay', 'home')]
for i, (t, s, ic) in enumerate(flow):
    x = 60 + i * 280
    b += white_panel(x, 210, 260, 300, 26)
    b += num_badge(x + 44, 254, i + 1)
    b += f'<rect x="{x + 96}" y="290" width="68" height="68" rx="18" fill="{BLUE if i == 2 else NAVY_TILE}"/>' + icon(ic, x + 112, 306, 36, '#fff', 2)
    b += text(x + 130, 414, t, 22, INK, 800, 'middle', F_HEAD, -0.6)
    b += text(x + 130, 446, s, 17, MUTED, anchor='middle')
    if i < 3:
        b += arrow(f'M{x + 262} 360 H {x + 278}', BLUE, 3)
b += logo_tile(60, 560, logo_whatsapp, 72)
b += white_panel(150, 560, 1010, 210, 26)
b += eyebrow(182, 606, 'What you no longer do')
for i, t in enumerate(['Check payment screenshots on WhatsApp', 'Add students to groups by hand', 'Chase "sir, payment ho gaya" messages']):
    b += check_row(182, 656 + i * 40, t, 20, ok=False)
b += text(60, H - 28, 'Gateway charges apply per transaction. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('payment-flow', svg(W, H, b, 'Online academy payment flow: student taps buy, pays by UPI or card, course access opens and the payout reaches the educator through Razorpay'))

# 9. launch checklist ----------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Your *launch week* checklist'], 54)
b += white_panel(60, 160, 540, 700, 28)
b += eyebrow(92, 214, 'Before you share the link')
for i, t in enumerate(['Buy your own course as a test', 'Open it on a cheap Android phone', 'Demo lesson easy to find', 'Price and refund policy written', 'Contact email on the site', 'Meta Pixel and GTM added']):
    b += check_row(92, 276 + i * 92, t, 21)
b += white_panel(620, 160, 540, 700, 28)
b += eyebrow(652, 214, 'Launch week')
logos = [logo_youtube, logo_instagram, logo_whatsapp]
for i, t in enumerate(['Link in YouTube descriptions', 'Link in Instagram bio', 'Post in your WhatsApp groups', 'Run one free live demo class', 'Reply to every question', 'Ask first students for feedback']):
    y = 276 + i * 92
    if i < 3:
        b += logo_tile(649, y - 26, logos[i], 38) + text(696, y, t, 21, INK, 500)
    else:
        b += check_row(652, y, t, 21)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('launch-checklist', svg(W, H, b, 'Online academy launch week checklist: test purchase, mobile check, demo lesson, tracking, then share on YouTube, Instagram and WhatsApp'))

# 10. mistakes ------------------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Six mistakes that *slow a launch*'], 52)
mist = [('Teaching everyone', 'Pick one exam or skill first'),
        ('Ten courses on day one', 'Launch one good course'),
        ('No free demo lesson', 'Let students try first'),
        ('Waiting to be perfect', 'Publish, then improve'),
        ('Domain in a vendor\'s name', 'Register it in yours'),
        ('Selling only on WhatsApp', 'Send them to checkout')]
for i, (t, fix) in enumerate(mist):
    y = 170 + i * 118
    b += tape(50 + (i % 2) * 18, y, 520, t, -1.2 if i % 2 else 0.9, 30)
    b += arrow(f'M{600} {y + 36} H 660', BLUE, 3)
    b += white_panel(680, y + 2, 480, 70, 20)
    b += f'<circle cx="716" cy="{y + 37}" r="16" fill="{BLUE}"/>' + icon('tick', 706, y + 27, 20, '#fff', 2.8)
    b += text(746, y + 45, fix, 22, INK, 600, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Six common mistakes when starting an online academy and the fix for each', ('split', 640)))
