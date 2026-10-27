"""Graphics for /blog/online-coaching-academy-without-coding
(How to Create an Online Academy Without a Developer: Live in One Evening).

Run:  python .claude/skills/academy-guide-blog/graphics/online-coaching-academy-without-coding.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/online-coaching-academy-without-coding
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'online-coaching-academy-without-coding')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


EVENING = [('6:00', 'Sign up, start the trial', 'No card needed', 'users'),
           ('6:15', 'Pick a template and theme', 'Free, customisable', 'layers'),
           ('6:45', 'Add your brand', 'Logo, colours, photo, about', 'image'),
           ('7:15', 'Build your first course', 'Videos, PDFs, tests, free demo', 'play'),
           ('8:15', 'Set up payments', 'Price, UPI and card checkout', 'card'),
           ('8:45', 'Connect your domain', 'youracademy.in', 'globe'),
           ('9:15', 'Test, publish, share', 'Buy it once on your phone', 'bolt')]

# 1. cover ----------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 290, ['Create your', '*online academy*', 'tonight.'], 84)
b += lines(84, 540, ['No developer. No code. One evening.'], 30, MUTED)
chips = ['6 pm', '7 pm', '8 pm', '9 pm', '10 pm']
b += f'<path d="M100 650 H 700" stroke="{BLUE}" stroke-width="3" stroke-dasharray="5 8"/>'
for i, c in enumerate(chips):
    x = 100 + i * 150
    b += f'<circle cx="{x}" cy="650" r="11" fill="{BLUE if i in (0, 4) else "#fff"}" stroke="{BLUE}" stroke-width="3"/>'
    b += text(x, 698, c, 22, INK, 700, 'middle', F_HEAD, -0.3)
b += text(100, 760, 'Sign up  ·  brand  ·  course  ·  payments  ·  domain  ·  publish', 22, MUTED, 500)
b += text(880, 196, 'Studio preview · sample data', 15, MUTED)
b += laptop(880, 210, 580, 'studio-courses.jpg')
b += phone(1380, 360, 150, 'studio-mobile.jpg')
b += pill_card(820, 650, 440, 'Live by 10 pm', 'Illustrative evening plan', 'bolt')
save('cover', svg(1600, 900, b, 'How to create an online academy without a developer, live in one evening: sign up, brand, course, payments, domain, publish'))

# 2. evening timeline ------------------------------------------------------------------
W, H = 1220, 1180
b = headline(60, 100, ['Your academy, *6 pm to 10 pm*'], 56)
b += lines(62, 150, ['The build part of an online academy, one block at a time.'], 22)
b += f'<path d="M118 230 V 1062" stroke="{BLUE}" stroke-width="3" stroke-dasharray="5 8"/>'
for i, (t, n, s, ic) in enumerate(EVENING):
    y = 196 + i * 124
    b += white_panel(190, y, 970, 102, 24)
    b += f'<rect x="64" y="{y + 31}" width="108" height="40" rx="20" fill="{BLUE}"/>' + text(118, y + 58, t + ' pm', 19, '#fff', 700, 'middle', F_HEAD)
    b += f'<rect x="214" y="{y + 20}" width="62" height="62" rx="18" fill="{NAVY_TILE}"/>' + icon(ic, 229, y + 35, 32, '#fff', 2)
    b += text(302, y + 48, n, 29, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(302, y + 80, s, 20, MUTED)
b += f'<rect x="64" y="1062" width="108" height="40" rx="20" fill="{NAVY_TILE}"/>' + text(118, 1089, '10:00 pm', 19, '#fff', 700, 'middle', F_HEAD)
b += text(190, 1090, 'Your academy is live. Share the link.', 24, INK, 700, font=F_HEAD, ls=-0.5)
b += text(60, H - 28, 'Illustrative timeline. Recording lessons is separate; do it before the evening.', 16, MUTED)
b += signature(W, H)
save('evening-timeline', svg(W, H, b, 'Illustrative one-evening timeline to create an online academy without a developer, from 6 pm sign-up to 10 pm publish'))

# 3. what to prepare ---------------------------------------------------------------------
W, H = 1220, 800
b = headline(60, 100, ['Have these *ready by 6 pm*'], 54)
b += lines(62, 150, ['Six things that make the evening go smoothly.'], 22)
prep = [('One module recorded', 'Or videos already on YouTube', 'play'),
        ('PDF notes and a test', 'For that same module', 'file'),
        ('Logo and two colours', 'A clear photo of you too', 'image'),
        ('A domain name', 'youracademy.in, in your name', 'globe'),
        ('PAN and bank details', 'For payment verification', 'card'),
        ('A price for the course', 'Decided before you sit down', 'tag')]
for i, (t, s, ic) in enumerate(prep):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 170
    b += pill_card(x, y, 540, t, s, ic, h=130, tile=BLUE_TINT if i % 3 else NAVY_TILE, title_size=25)
b += signature(W, H)
save('what-to-prepare', svg(W, H, b, 'Checklist to prepare before you create an online academy: a recorded module, PDF notes and a test, logo, domain, PAN and bank details, a course price'))

# 4. building blocks ------------------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Six *no-code* building blocks'], 56)
b += lines(62, 150, ['What you set up, and what runs underneath.'], 22)
blocks = [('Template and theme', 'Pick, then customise', 'Hosting and updates', 'layers'),
          ('Your brand', 'Logo, colours, photo', 'Applied site-wide', 'image'),
          ('Course builder', 'Drag in videos, PDFs, tests', 'Access per student', 'play'),
          ('Payments', 'Set the price', 'UPI, cards, Razorpay payouts', 'card'),
          ('Your domain', 'Point it to the academy', 'Your website, live', 'globe'),
          ('Your app', 'Your name and logo', 'Android on every plan', 'phone')]
for i, (t, you, auto, ic) in enumerate(blocks):
    x = 60 + (i % 3) * 375
    y = 200 + (i // 3) * 380
    b += white_panel(x, y, 350, 350, 26)
    b += f'<rect x="{x + 30}" y="{y + 30}" width="68" height="68" rx="18" fill="{NAVY_TILE if i % 2 == 0 else BLUE}"/>' + icon(ic, x + 46, y + 46, 36, '#fff', 2)
    b += text(x + 30, y + 146, t, 28, INK, 800, font=F_HEAD, ls=-0.9)
    b += eyebrow(x + 30, y + 200, 'You do')
    b += text(x + 30, y + 232, you, 19, INK, 500)
    b += f'<line x1="{x + 30}" y1="{y + 260}" x2="{x + 320}" y2="{y + 260}" stroke="{LINE}" stroke-width="2"/>'
    b += eyebrow(x + 30, y + 296, 'Runs on its own', MUTED)
    b += text(x + 30, y + 328, auto, 19, INK, 500)
b += text(60, H - 28, 'On AllCoaching the iOS app is included on Pro.', 16, MUTED)
b += signature(W, H)
save('building-blocks', svg(W, H, b, 'Six no-code building blocks of an online academy: template, brand, course builder, payments, domain and app'))

# 5. studio build (annotated screenshot) ------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['One studio. *Every block.*'], 54)
b += lines(62, 150, ['Build, brand and sell from the same login.'], 22)
b += text(90, 206, 'Studio preview · sample data', 15, MUTED)
b += laptop(100, 222, 680, 'studio-desktop.jpg')
calls = [('Courses', 'Videos, PDFs, test series', 'book'),
         ('Live', 'YouTube Live, Zoom or built-in', 'video'),
         ('Own branding', 'Logo, colours, theme, domain', 'image'),
         ('Transactions', 'Every UPI and card sale', 'card')]
for i, (t, s, ic) in enumerate(calls):
    y = 220 + i * 128
    b += white_panel(850, y, 320, 108, 22)
    b += num_badge(884, y + 54, i + 1)
    b += text(920, y + 48, t, 23, INK, 800, font=F_HEAD, ls=-0.5)
    b += text(920, y + 78, s, 15, MUTED)
b += f'<g filter="url(#sh)"><rect x="90" y="760" width="740" height="120" rx="24" fill="{NAVY_TILE}"/></g>'
b += eyebrow(122, 806, 'Every plan', '#9FB0FF')
b += text(122, 846, 'Unlimited live classes · unlimited videos via YouTube', 22, '#fff', 700, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('studio-build', svg(W, H, b, 'The AllCoaching studio used to create an online academy without code: courses, live classes, own branding and transactions in one login'))

# 6. WordPress + plugins vs one login -----------------------------------------------------------
W, H = 1220, 960
b = headline(56, 110, ['Building it', 'like this?'], 58)
items = ['Hosting plan to renew', 'LMS plugin', 'Payment plugin', 'Video plugin', 'Security plugin', 'Update broke the site']
for i, t in enumerate(items):
    b += tape(40 + (i % 2) * 22, 210 + i * 96, 500, t, -1.4 if i % 2 else 1.0, 30)
b += hand(300, 840, ['Plugin conflict', 'again?'], 40, INK, -6) + arrow('M280 850 C 230 870, 190 850, 170 820', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['One login.', '*Your whole academy.*'], 52)
for i, t in enumerate(['Hosting and updates handled', 'Courses, tests and live classes', 'UPI and card checkout built in', 'Your domain, your brand', 'Your own Android app']):
    b += check_row(656, 380 + i * 74, t, 25)
b += text(656, 790, 'Nothing to install, patch or renew.', 20, MUTED, 500)
b += signature(W, H)
save('wordpress-vs-one-login', svg(W, H, b, 'WordPress plus plugins to build an online academy versus one no-code academy login', ('split', 600)))

# 7. what you do not need -----------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['What you *do not need*'], 56)
b += lines(62, 150, ['The old checklist, and what replaces each line.'], 22)
nope = [('A developer', 'Drag-and-drop course builder'),
        ('A server or hosting plan', 'Hosting runs underneath'),
        ('WordPress and plugins', 'One login for everything'),
        ('Payment gateway code', 'UPI and card checkout built in'),
        ('A separate video host', 'Videos via YouTube, unlimited'),
        ('App code to write and update', 'Your white-label Android app')]
for i, (t, fix) in enumerate(nope):
    y = 200 + i * 124
    b += white_panel(60, y, 520, 96, 22)
    b += check_row(92, y + 56, t, 23, ok=False)
    b += arrow(f'M598 {y + 48} H 652', BLUE, 3)
    b += white_panel(670, y, 490, 96, 22)
    b += check_row(702, y + 56, fix, 22)
b += text(60, H - 28, 'iOS app on AllCoaching Pro. Payment gateway verification still needs your PAN and bank details.', 16, MUTED)
b += signature(W, H)
save('dont-need', svg(W, H, b, 'What you do not need to create an online academy: a developer, a server, WordPress plugins, payment code, a separate video host or app code'))

# 8. developer vs no-code matrix -----------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Developer or *no-code*?'], 56)
b += lines(62, 150, ['Illustrative comparison for one educator with one course.'], 22)
b += white_panel(60, 190, 1100, 720, 28)
cols = [(92, 'What changes'), (420, 'Hire a developer'), (800, 'No-code academy')]
b += f'<rect x="780" y="206" width="364" height="688" rx="20" fill="{BLUE_TINT}"/>'
for x, t in cols:
    b += eyebrow(x if x != 800 else 812, 246, t, BLUE if x == 800 else MUTED)
rows = [('Time to go live', 'Weeks to months', 'One evening to a week'),
        ('Upfront cost', 'A project quote', 'From ₹3,999/mo + GST'),
        ('Ongoing upkeep', 'Updates, fixes, renewals', 'Handled by the platform'),
        ('Who makes changes', 'The developer', 'You, in the studio'),
        ('Student apps', 'Built by the developer', 'Android on every plan'),
        ('Domain and data', 'Depends on the contract', 'Your domain, exportable')]
for r, (k, dev, nc) in enumerate(rows):
    y = 330 + r * 96
    b += f'<line x1="92" y1="{y - 46}" x2="1128" y2="{y - 46}" stroke="{LINE}" stroke-width="2"/>'
    b += text(92, y, k, 22, INK, 700, font=F_HEAD, ls=-0.4)
    b += text(420, y, dev, 20, MUTED, 500)
    b += f'<circle cx="828" cy="{y - 7}" r="14" fill="{BLUE}"/>' + icon('tick', 819, y - 16, 18, '#fff', 2.8)
    b += text(854, y, nc, 20, INK, 600)
b += text(60, H - 28, 'Illustrative; developer quotes vary by scope and city. No-code column reflects AllCoaching plans, Oct 2026.', 16, MUTED)
b += signature(W, H)
save('dev-vs-nocode', svg(W, H, b, 'Hiring a developer versus a no-code online academy: time to launch, cost, upkeep, control, apps, domain and data'))

# 9. blockers and fixes -------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Stuck at 9 pm? *Quick fixes*'], 52)
blk = [('Domain not showing yet', 'Wait, then recheck the values'),
       ('Payments still verifying', 'Publish the free demo first'),
       ('Video plays for everyone', 'Set it to unlisted on YouTube'),
       ('Logo looks blurry', 'Upload a larger square PNG'),
       ('Too much to upload', 'Launch with one module'),
       ('Test purchase fails', 'Try UPI, then message support')]
for i, (t, fix) in enumerate(blk):
    y = 170 + i * 118
    b += tape(50 + (i % 2) * 18, y, 520, t, -1.2 if i % 2 else 0.9, 28)
    b += arrow(f'M{600} {y + 36} H 660', BLUE, 3)
    b += white_panel(680, y + 2, 480, 70, 20)
    b += f'<circle cx="716" cy="{y + 37}" r="16" fill="{BLUE}"/>' + icon('tick', 706, y + 27, 20, '#fff', 2.8)
    b += text(746, y + 45, fix, 21, INK, 600, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('blockers', svg(W, H, b, 'Common blockers when you create an online academy in one evening, and the fix for each', ('split', 640)))
