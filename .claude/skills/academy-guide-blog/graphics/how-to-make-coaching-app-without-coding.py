"""Graphics for /blog/how-to-make-coaching-app-without-coding.

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-make-coaching-app-without-coding.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-make-coaching-app-without-coding
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'how-to-make-coaching-app-without-coding')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def tile(x, y, ic, size=60, dark=True):
    col = NAVY_TILE if dark else BLUE_TINT
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .27:.0f}" fill="{col}"/>' +
            icon(ic, x + size * .22, y + size * .22, size * .56, '#fff' if dark else BLUE, 2))


# 1. cover ----------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Your own', '*coaching app.*', 'No coding.'], 88)
b += lines(84, 560, ['Courses, tests, live classes and payments, in your brand.'], 28, MUTED)
for i, (t, ic) in enumerate([('Sign up and choose a plan', 'check'), ('Upload courses, PDFs and tests', 'layers'),
                             ('Add your name, logo and colours', 'sparkle'), ('Share the app with your students', 'users')]):
    b += f'<circle cx="100" cy="{622 + i * 56}" r="17" fill="{BLUE}"/>' + icon('tick', 90, 612 + i * 56, 20, '#fff', 2.8)
    b += text(130, 630 + i * 56, t, 25, INK, 600, font=F_HEAD, ls=-0.4)
b += text(1010, 120, 'Studio preview · sample data', 15, MUTED)
b += phone(1030, 140, 300, 'studio-mobile.jpg')
b += pill_card(830, 330, 300, 'Android app', 'On every plan', 'phone', title_size=26)
b += pill_card(1250, 620, 300, 'iOS app', 'On Pro', 'phone', title_size=26)
save('cover', svg(1600, 900, b, 'How to make a coaching app without coding in India: courses, tests, live classes and payments in your own branded Android app'))

# 2. three routes -----------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Three ways to get *your own app*'], 54)
b += lines(62, 150, ['Same goal, very different work for you.'], 22)
routes = [('Agency or freelancer', 'Custom build', 'users',
           [('Who builds it', 'A developer team'), ('Launch time', 'Depends on scope'), ('Who changes it', 'The developer'),
            ('Still needed', 'Hosting, payments, updates'), ('Cost shape', 'Project quote + upkeep')]),
          ('No-code app builder', 'Generic drag and drop', 'puzzle',
           [('Who builds it', 'You, screen by screen'), ('Launch time', 'Days to weeks'), ('Who changes it', 'You'),
            ('Still needed', 'Courses, checkout, video'), ('Cost shape', 'Builder plan + add-ons')]),
          ('Academy platform', 'App included with your LMS', 'layers',
           [('Who builds it', 'You fill it in'), ('Launch time', 'Same week (illustrative)'), ('Who changes it', 'You, in the studio'),
            ('Still needed', 'Your content'), ('Cost shape', 'Yearly plan + fee on sales')])]
for i, (t, s, ic, rows) in enumerate(routes):
    x = 60 + i * 375
    hi = i == 2
    if hi:
        b += f'<rect x="{x - 8}" y="192" width="371" height="756" rx="32" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += white_panel(x, 200, 355, 740, 26)
    b += tile(x + 26, 228, ic, 64, not hi)
    b += text(x + 26, 344, t, 27, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(x + 26, 376, s, 18, BLUE, 600)
    for k, (lab, val) in enumerate(rows):
        y = 430 + k * 100
        b += f'<line x1="{x + 26}" y1="{y - 22}" x2="{x + 329}" y2="{y - 22}" stroke="{LINE}" stroke-width="2"/>'
        b += eyebrow(x + 26, y + 6, lab, MUTED)
        b += text(x + 26, y + 42, val, 21, INK, 600, font=F_HEAD, ls=-0.3)
b += text(60, H - 70, 'Example comparison; times are illustrative. Agency costs: see our white label app cost guide.', 16, MUTED)
b += signature(W, H)
save('three-routes', svg(W, H, b, 'Three ways to make a coaching app: hire an agency or freelancer, use a no-code app builder, or use an academy platform with a white-label app included'))

# 3. what a coaching app needs -------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['What a coaching app *needs*'], 54)
b += lines(62, 150, ['Eight things students expect on day one.'], 22)
left = [('Student login', 'Own account, own purchases', 'users'), ('Course library', 'Modules in syllabus order', 'book'),
        ('Video lessons', 'Recorded, watch any time', 'play'), ('PDF notes', 'Revise on a small screen', 'file')]
right = [('Tests', 'Quizzes and timed mocks', 'check'), ('Live classes', 'Doubts and revision', 'video'),
         ('Payments', 'UPI and card checkout', 'card'), ('Your brand', 'Name, logo, colours', 'star')]
for i, (t, s, ic) in enumerate(left):
    y = 220 + i * 170
    b += white_panel(60, y, 400, 140, 24)
    b += tile(84, y + 38, ic, 64, True)
    b += text(168, y + 64, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(168, y + 96, s, 18, MUTED)
for i, (t, s, ic) in enumerate(right):
    y = 220 + i * 170
    b += white_panel(760, y, 400, 140, 24)
    b += tile(784, y + 38, ic, 64, False)
    b += text(868, y + 64, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(868, y + 96, s, 18, MUTED)
b += phone(505, 250, 210, 'studio-mobile.jpg')
b += text(610, 724, 'Studio preview · sample data', 15, MUTED, anchor='middle')
b += text(60, H - 28, 'Your website on your own domain carries the same courses.', 16, MUTED)
b += signature(W, H)
save('app-needs', svg(W, H, b, 'What a coaching app needs: student login, course library, video lessons, PDF notes, tests, live classes, UPI payments and your own brand'))

# 4. steps ------------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Your app in *six steps*'], 56)
b += lines(62, 150, ['No code at any step. Payments, access and hosting run on their own.'], 22)
st = [('Sign up', 'Start the 7-day free trial, no card', 'check'), ('Choose a plan', 'Android on all, iOS on Pro', 'tag'),
      ('Upload your course', 'Videos via YouTube, PDFs, tests', 'layers'), ('Brand it', 'Academy name, logo and colours', 'sparkle'),
      ('Connect your domain', 'youracademy.in for the website', 'globe'), ('Share with students', 'Link on YouTube, WhatsApp, Instagram', 'users')]
for i, (t, s, ic) in enumerate(st):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 230
    b += white_panel(x, y, 540, 200, 26)
    b += num_badge(x + 50, y + 54, i + 1, 24)
    b += tile(x + 440, y + 30, ic, 70, i % 2 == 0)
    b += text(x + 30, y + 130, t, 30, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(x + 30, y + 166, s, 19, MUTED)
b += text(60, H - 28, '0% commission on Growth and Pro. Starter ₹6,999/year + 10%. GST extra.', 16, MUTED)
b += signature(W, H)
save('six-steps', svg(W, H, b, 'How to make a coaching app without coding in six steps: sign up, choose a plan, upload your course, brand it, connect your domain and share it with students'))

# 5. brand kit ------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Make it *look like yours*'], 56)
b += lines(62, 150, ['Four things to decide before you open the studio.'], 22)
b += white_panel(60, 200, 640, 640, 28)
b += eyebrow(92, 250, 'Your brand kit')
items = [('Academy name', 'Short, easy to say, easy to type', 'type'), ('Logo', 'Square version that reads at icon size', 'image'),
         ('Colours', 'One main colour + one accent', 'sparkle'), ('Domain', 'youracademy.in, matching the name', 'globe')]
for i, (t, s, ic) in enumerate(items):
    y = 290 + i * 132
    b += tile(92, y, ic, 64, i % 2 == 0)
    b += text(176, y + 26, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(176, y + 56, s, 18, MUTED)
for k, col in enumerate(['#2B44FF', '#0A0F3D', '#22C3F5', '#F3F4FC']):
    b += f'<circle cx="{480 + k * 34}" cy="{581}" r="14" fill="{col}" stroke="{LINE}" stroke-width="2"/>'
b += phone(830, 200, 260, 'studio-mobile.jpg')
b += text(960, 770, 'Studio preview · sample data', 15, MUTED, anchor='middle')
b += hand(760, 850, ['Same name everywhere:', 'app, website, YouTube.'], 32, INK, -3)
b += signature(W, H)
save('brand-kit', svg(W, H, b, 'Branding a coaching app: academy name, square logo, brand colours and your own domain, shown on a phone with the AllCoaching studio'))

# 6. plans and apps -----------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Which app comes with *which plan*'], 52)
b += lines(62, 150, ['Every plan: website on your own domain + your own Android app.'], 22)
plans = [('Starter', '₹6,999', 'a year + GST, 10% per sale', 'Keep 90% of each sale', '512 GB storage, 100 GB streaming', False),
         ('Growth', '₹7,999', 'a month + GST', '0% commission · keep 100%', '1 TB storage, 1 TB streaming', False),
         ('Pro', '₹14,999', 'a month + GST', '0% commission · keep 100%', '2 TB + 2 TB streaming, 4K', True)]
for i, (n, p, per, yearly, lim, ios) in enumerate(plans):
    x = 60 + i * 370
    b += white_panel(x, 200, 350, 560, 26)
    b += eyebrow(x + 28, 246, n)
    b += text(x + 28, 300, p, 40, INK, 800, font=F_HEAD, ls=-1.2)
    b += text(x + 28, 330, per, 17, MUTED)
    b += f'<rect x="{x + 28}" y="350" width="{len(yearly) * 9.6 + 30}" height="34" rx="17" fill="{BLUE_TINT}"/>'
    b += text(x + 43, 373, yearly, 16, BLUE, 700, font=F_HEAD)
    b += check_row(x + 28, 450, 'Website', 20)
    b += check_row(x + 28, 520, 'Android app', 20)
    b += check_row(x + 28, 590, 'iOS app', 20, ios)
    b += check_row(x + 28, 660, 'Unlimited live', 20)
    b += text(x + 28, 730, lim, 17, MUTED, 600)
b += text(60, 810, 'All plans start with a 7-day free trial, no card. No sales limit on any plan; monthly billing has no lock-in.', 18, INK, 600)
b += text(60, 840, 'Prices exclude GST. Growth and Pro: 0% commission, ₹79,990/₹1,49,990 if paid yearly. Gateway charges separate.', 16, MUTED)
b += signature(W, H)
save('plans-apps', svg(W, H, b, 'Which coaching app comes with which AllCoaching plan: own Android app on every plan, iOS app on Pro'))

# 7. install path ------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['How students *find and install* it'], 52)
b += lines(62, 150, ['Send them where they already are, with one link.'], 22)
srcs = [(logo_youtube, 'YouTube', 'Pinned comment + description'), (logo_whatsapp, 'WhatsApp', 'Group, channel, status'),
        (logo_instagram, 'Instagram', 'Bio link + story')]
for i, (lg, t, s) in enumerate(srcs):
    y = 210 + i * 150
    b += white_panel(60, y, 420, 120, 24)
    b += logo_tile(84, y + 24, lg, 72)
    b += text(180, y + 54, t, 26, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(180, y + 86, s, 18, MUTED)
    b += arrow(f'M490 {y + 60} C 540 {y + 60}, 540 360, 590 360', BLUE, 3)
b += f'<g filter="url(#shB)"><rect x="600" y="300" width="560" height="120" rx="28" fill="{BLUE}"/></g>'
b += text(630, 352, 'youracademy.in', 32, '#fff', 800, font=F_HEAD, ls=-0.8)
b += text(630, 388, 'Free demo lesson + link to your app', 19, '#DCE2FF')
b += arrow('M880 430 V 510', BLUE, 3)
b += white_panel(600, 520, 560, 120, 26)
b += tile(626, 548, 'phone', 64)
b += text(710, 574, 'Installs your app', 26, INK, 800, font=F_HEAD, ls=-0.6)
b += text(710, 606, 'Logs in and finds your courses', 18, MUTED)
b += arrow('M880 650 V 720', BLUE, 3)
b += white_panel(600, 730, 560, 120, 26)
b += tile(626, 758, 'card', 64, False)
b += text(710, 784, 'Buys and studies in the app', 26, INK, 800, font=F_HEAD, ls=-0.6)
b += text(710, 816, 'UPI or card; access opens on its own', 18, MUTED)
b += text(60, H - 28, 'Example path, illustrative. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('install-path', svg(W, H, b, 'How students find and install a coaching app: links from YouTube, WhatsApp and Instagram lead to the academy website, then the app, then checkout'))

# 8. mistakes ------------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Six coaching app *mistakes*'], 54)
mist = [('App before content', 'Upload one full course first'),
        ('Ten features, no plan', 'Start with the eight basics'),
        ('No website link', 'Website and app together'),
        ('Unclear app name', 'Same name as your channel'),
        ('Launch and forget', 'Weekly live class, new tests'),
        ('No way to leave', 'Check data export first')]
for i, (t, fix) in enumerate(mist):
    y = 170 + i * 118
    b += tape(50 + (i % 2) * 18, y, 520, t, -1.2 if i % 2 else 0.9, 30)
    b += arrow(f'M600 {y + 36} H 660', BLUE, 3)
    b += white_panel(680, y + 2, 480, 70, 20)
    b += f'<circle cx="716" cy="{y + 37}" r="16" fill="{BLUE}"/>' + icon('tick', 706, y + 27, 20, '#fff', 2.8)
    b += text(746, y + 45, fix, 22, INK, 600, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Six common mistakes when making a coaching app without coding and the fix for each', ('split', 640)))
