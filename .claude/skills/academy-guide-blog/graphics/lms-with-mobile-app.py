"""Graphics for /blog/lms-with-mobile-app.

Run:  python .claude/skills/academy-guide-blog/graphics/lms-with-mobile-app.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/lms-with-mobile-app

Real screens: studio Own branding > App (landing/img/studio-app.webp, sample educator), and owner-approved
showcase academies on a phone (Biology Lessons, CHEMPSI). Shared-app and home-screen phones are drawn mock-ups,
labelled illustrative. No competitor logos are drawn.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'lms-with-mobile-app')
os.makedirs(OUT, exist_ok=True)
SHOT = os.path.join(ROOT, 'landing', 'img', 'studio-app.webp')      # real studio Own branding > App (sample data)
BIO = os.path.join(ROOT, 'assets', 'showcase', 'bio-mobile.webp')   # Biology Lessons (Dr. Subhash Nair)
CHEM = os.path.join(ROOT, 'assets', 'showcase', 'chem-mobile.webp') # CHEMPSI (Anupam Kumar)

ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3M12 15v2"/>'
ICONS['download'] = '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>'
ICONS['bell'] = '<path d="M6 16V11a6 6 0 0112 0v5l2 2H4z"/><path d="M10 20a2 2 0 004 0"/>'
ICONS['refresh'] = '<path d="M20 11a8 8 0 10-2.3 5.7"/><path d="M20 4v7h-7"/>'
ICONS['door'] = '<path d="M6 21V4h10v17M4 21h16"/><path d="M13 12h.01"/>'
ICONS['wallet'] = '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>'
ICONS['apple'] = '<path d="M16 3c0 2-1.5 3.5-3.4 3.6C12.4 4.7 14 3 16 3z"/><path d="M12 8c-1.3 0-2.4-.8-3.6-.8C6.2 7.2 4.5 9.2 4.5 12.4c0 4.4 3 8.6 4.7 8.6 1.2 0 1.6-.7 2.8-.7s1.6.7 2.8.7c1.8 0 4.1-3.8 4.7-5.7-2.2-1-2.8-4.6-.4-6.2-1-1.4-2.4-1.9-3.4-1.9C14.4 7.2 13.3 8 12 8z"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def app_icon(x, y, size, label, fill=BLUE):
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .24}" fill="{fill}"/></g>' +
            text(x + size / 2, y + size / 2 + size * .14, label, size * .38, '#fff', 800, 'middle', F_HEAD, -1))


def yes(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="17" fill="{BLUE}"/>' + icon('tick', cx - 10, cy - 10, 20, '#fff', 2.8)


def no(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="17" fill="#C9CDD8"/>' + icon('x', cx - 9, cy - 9, 18, '#fff', 2.8)


def frame(x, y, w):
    """Empty phone frame; returns (svg, screen x, screen y, screen w, screen h)."""
    h = w * 2.07
    bz = w * 0.045
    r = w * 0.17
    s = (f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#121317"/></g>'
         f'<rect x="{x + bz}" y="{y + bz}" width="{w - 2 * bz}" height="{h - 2 * bz}" rx="{r - bz}" fill="#FFFFFF"/>'
         f'<rect x="{x + w * .34}" y="{y + bz + w * .035}" width="{w * .32}" height="{w * .085}" rx="{w * .0425}" fill="#000"/>')
    return s, x + bz, y + bz, w - 2 * bz, h - 2 * bz


def shared_phone(x, y, w):
    """Drawn mock of a shared platform app: platform brand on top, many educators inside (illustrative)."""
    s, sx, sy, sw, sh = frame(x, y, w)
    k = sw / 300
    s += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{90 * k}" rx="{20 * k}" fill="{NAVY_TILE}"/>'
    s += f'<rect x="{sx}" y="{sy + 60 * k}" width="{sw}" height="{30 * k}" fill="{NAVY_TILE}"/>'
    s += text(sx + 22 * k, sy + 72 * k, 'Platform App', 22 * k, '#fff', 800, font=F_HEAD)
    s += f'<rect x="{sx + 18 * k}" y="{sy + 108 * k}" width="{sw - 36 * k}" height="{40 * k}" rx="{20 * k}" fill="#F1F2F7"/>'
    s += text(sx + 38 * k, sy + 134 * k, 'Search educators...', 15 * k, MUTED)
    names = [('RS', 'R. Sharma Maths', '#7C8597'), ('YA', 'Your Academy', BLUE), ('PK', 'PK Physics', '#7C8597'),
             ('NE', 'NEET Notes Hub', '#7C8597'), ('SE', 'Spoken English', '#7C8597')]
    for i, (ab, n, col) in enumerate(names):
        yy = sy + (172 + i * 76) * k
        s += f'<rect x="{sx + 18 * k}" y="{yy}" width="{sw - 36 * k}" height="{64 * k}" rx="{14 * k}" fill="{BLUE_TINT if col == BLUE else "#F7F7FA"}"/>'
        s += f'<rect x="{sx + 30 * k}" y="{yy + 12 * k}" width="{40 * k}" height="{40 * k}" rx="{10 * k}" fill="{col}"/>'
        s += text(sx + 50 * k, yy + 39 * k, ab, 15 * k, '#fff', 800, 'middle', F_HEAD)
        s += text(sx + 84 * k, yy + 30 * k, n, 17 * k, INK, 700, font=F_HEAD)
        s += text(sx + 84 * k, yy + 51 * k, 'inside Platform App', 13 * k, MUTED)
    return s


def home_phone(x, y, w, label='Your Academy'):
    """Drawn mock of a home screen with the educator's own app icon (illustrative)."""
    s, sx, sy, sw, sh = frame(x, y, w)
    k = sw / 300
    s += f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{w * .125}" fill="#EEF1FB"/>'
    s += text(sx + sw / 2, sy + 110 * k, '9:41', 54 * k, INK, 300, 'middle', F_HEAD, -2)
    for r in range(4):
        for c in range(4):
            ix, iy = sx + (26 + c * 66) * k, sy + (160 + r * 92) * k
            if (r, c) == (1, 1):
                s += app_icon(ix - 4 * k, iy - 4 * k, 58 * k, 'YA')
                s += text(ix + 25 * k, iy + 72 * k, label, 13 * k, INK, 700, 'middle')
            else:
                s += f'<rect x="{ix}" y="{iy}" width="{50 * k}" height="{50 * k}" rx="{13 * k}" fill="#D9DEEC"/>'
    return s


def web_phone(x, y, w, shot, url):
    """Phone with a real academy screenshot, plus a browser-style address pill under it."""
    out = phone(x, y, w, shot)
    py = y + w * 2.07 + 16
    out += f'<rect x="{x + w * .08}" y="{py}" width="{w * .84}" height="34" rx="17" fill="#fff" stroke="#C9CDD8" stroke-width="1.5"/>'
    out += icon('lock', x + w * .08 + 12, py + 8, 18, MUTED, 2.2)
    out += text(x + w * .08 + 38, py + 23, url, 16, INK, 600)
    return out


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['An LMS with a', 'mobile app:', '*check this first.*'], 70)
b += lines(84, 520, ['Shared app, your own app or a mobile website.', 'What each one means for your students.'], 26, MUTED)
b += check_row(84, 640, 'Whose name is on the Play Store listing', 25)
b += check_row(84, 698, 'iOS, tests, live and notifications in the app', 25)
b += check_row(84, 756, 'What happens to the app if you switch', 25)
b += shared_phone(880, 150, 190)
b += home_phone(1100, 130, 200)
b += web_phone(1330, 150, 190, CHEM, 'chempsi.com')
for cx, t in [(975, 'Shared app'), (1200, 'Your own app'), (1425, 'Mobile website')]:
    b += text(cx, 640, t, 22, INK, 800, 'middle', F_HEAD, -0.5)
b += f'<rect x="1112" y="654" width="176" height="6" rx="3" fill="{BLUE}"/>'
b += text(880, 710, 'Shared app and home screen: illustrative mock-ups.', 15, MUTED)
b += text(880, 734, 'Right: CHEMPSI, an academy on AllCoaching, on a phone.', 15, MUTED)
save('cover', svg(1600, 900, b, 'LMS with mobile app: a shared platform app, your own white-label app and a mobile website compared'))

# 2. three kinds of app -----------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Three things *"app"* can mean'], 54)
b += lines(62, 150, ['Ask the LMS which one it sells before you compare anything else'], 22)
b += white_panel(40, 196, 1140, 760, 28, big=True)
cols = [('Shared app', 'Your course inside', 'their app', 'users', 430), ('Your own app', 'White-label, in', 'your name', 'phone', 690), ('Mobile website', 'Browser or PWA,', 'no store', 'globe', 950)]
for t, s1, s2, ic, cx in cols:
    tile = BLUE if t == 'Your own app' else NAVY_TILE
    b += f'<rect x="{cx - 34}" y="222" width="68" height="68" rx="18" fill="{tile}"/>' + icon(ic, cx - 17, 239, 34, '#fff', 2.1)
    b += text(cx, 330, t, 24, INK, 800, 'middle', F_HEAD, -0.6)
    b += text(cx, 358, s1, 17, MUTED, anchor='middle') + text(cx, 380, s2, 17, MUTED, anchor='middle')
rows = [('Name on the store', ['The platform', 'You', 'No store listing']),
        ('Student installs', ['Platform app', 'Your app', 'Nothing / home icon']),
        ('Your icon on phone', ['No', 'Yes', 'Only if added']),
        ('Push notifications', ['Platform decides', 'In your name', 'Limited, varies']),
        ('Store listing owner', ['The platform', 'Your account*', 'Not applicable']),
        ('If you switch LMS', ['Students move apps', 'Listing stays yours*', 'Point domain anew']),
        ('Extra cost to you', ['Usually included', 'Plan + store fees', 'Usually included'])]
for i, (lab, vals) in enumerate(rows):
    y = 410 + i * 74
    if i % 2 == 0:
        b += f'<rect x="60" y="{y}" width="1100" height="66" rx="14" fill="#F5F6FC"/>'
    b += text(84, y + 41, lab, 20, INK, 700, font=F_HEAD, ls=-0.3)
    for (t, *_r, cx), v in zip(cols, vals):
        own = t == 'Your own app'
        b += text(cx, y + 41, v, 18, BLUE if own else INK, 600 if own else 400, 'middle')
b += text(60, 990, '* Only when the app is published on your own Google Play / Apple developer account. Ask the LMS in writing.', 17, MUTED)
b += signature(W, H)
save('three-kinds', svg(W, H, b, 'Three kinds of LMS mobile app: a shared platform app, your own white-label app and a mobile website or PWA, compared on store name, installs, notifications and switching'))

# 3. shared vs own ----------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Same course. *Two very different apps.*'], 50)
b += lines(62, 150, ['What a student sees in a shared app versus an academy in your own name'], 22)
b += shared_phone(110, 220, 300)
b += phone(810, 220, 300, BIO)
b += text(260, 900, 'Shared app', 28, INK, 800, 'middle', F_HEAD, -0.6)
b += text(260, 932, 'Illustrative mock-up', 17, MUTED, anchor='middle')
b += text(960, 900, 'Your own academy', 28, BLUE, 800, 'middle', F_HEAD, -0.6)
b += text(960, 932, 'Biology Lessons, on AllCoaching', 17, MUTED, anchor='middle')
mid = [('Brand on top', 'Theirs', 'Yours'), ('Other educators', 'Next to you', 'None'), ('Developer name', 'Platform', 'You')]
for i, (lab, l, r) in enumerate(mid):
    y = 300 + i * 170
    b += white_panel(470, y, 280, 130, 22)
    b += text(610, y + 40, lab, 20, MUTED, 600, 'middle')
    b += text(540, y + 92, l, 22, INK, 700, 'middle', F_HEAD)
    b += text(680, y + 92, r, 22, BLUE, 800, 'middle', F_HEAD)
    b += f'<line x1="610" y1="{y + 64}" x2="610" y2="{y + 110}" stroke="{LINE}" stroke-width="2"/>'
b += signature(W, H)
save('shared-vs-own', svg(W, H, b, 'Shared LMS app versus your own branded academy on a phone: platform brand and other educators next to you, versus your name only'))

# 4. checklist --------------------------------------------------------------------
W, H = 1220, 1120
b = headline(60, 100, ['12 checks before you *pay for an LMS*'], 50)
b += lines(62, 150, ['Ask every LMS these questions about its mobile app, and get the answers in writing'], 22)
items = [('Own Play Console listing', 'Published in your name', 'door'),
         ('iOS app, on which plan', 'And whose Apple account', 'apple'),
         ('Video in the app', 'Playback, quality, download', 'video'),
         ('Tests in the app', 'Rank, timer, lock', 'check'),
         ('Live classes in the app', 'Join from the course', 'play'),
         ('Push notifications', 'Sent in your name', 'bell'),
         ('Payments in the app', 'Store billing rules', 'wallet'),
         ('App updates', 'Who ships them, how', 'refresh'),
         ('Same login as website', 'One account per student', 'lock'),
         ('Branding control', 'Icon, name, colours', 'image'),
         ('If you leave', 'Who keeps the listing', 'link'),
         ('Extra app cost', 'Setup, yearly, store fees', 'tag')]
for i, (t, s, ic) in enumerate(items):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 146
    b += pill_card(x, y, 540, t, s, ic, h=116, tile=BLUE if i in (0, 10) else NAVY_TILE, title_size=24)
    b += num_badge(x + 516, y + 6, i + 1, 20)
b += text(60, 1080, 'Blue = the two checks that decide who owns the app.', 18, MUTED)
b += signature(W, H)
save('checklist', svg(W, H, b, 'LMS with mobile app checklist: own Play Console listing, iOS plan, video, tests, live classes, push notifications, payments, updates, login, branding, exit and extra cost'))

# 5. listing ownership -------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Who owns the *Play Store listing?*'], 54)
b += lines(62, 150, ['The developer account decides what happens when you switch LMS'], 22)
for j, (who, dev, good) in enumerate([('Published on your account', 'Your Academy', True), ("Published on the platform's account", 'Platform Pvt Ltd', False)]):
    x = 60 + j * 570
    b += white_panel(x, 200, 530, 300, 26, big=True)
    b += text(x + 30, 250, who, 22, BLUE if good else MUTED, 700, font=F_HEAD)
    b += app_icon(x + 30, 280, 96, 'YA', BLUE)
    b += text(x + 146, 318, 'Your Academy', 30, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(x + 146, 352, 'Developer: ' + dev, 19, BLUE if good else RED, 600)
    b += text(x + 146, 380, 'Education', 17, MUTED)
    b += f'<rect x="{x + 30}" y="410" width="470" height="56" rx="28" fill="{BLUE}"/>'
    b += text(x + 265, 446, 'Install', 22, '#fff', 700, 'middle', F_HEAD)
b += text(60, 570, 'If you move to another LMS later', 28, INK, 800, font=F_HEAD, ls=-0.8)
left = ['The listing stays in your account', 'Reviews and install history stay with it', 'You decide what ships next']
right = ['The listing stays with the platform', 'You may need a new app in your name', 'Students may have to install again']
for i, t in enumerate(left):
    b += check_row(70, 640 + i * 62, t, 21)
for i, t in enumerate(right):
    b += check_row(640, 640 + i * 62, t, 21, ok=False)
b += text(60, 860, 'Moving an existing app between developer accounts needs the current account holder to start a transfer.', 18, MUTED)
b += text(60, 890, 'Illustrative listings, not real apps. Check what your platform supports before you plan a move.', 18, MUTED)
b += signature(W, H)
save('listing-ownership', svg(W, H, b, 'Play Store listing ownership for an LMS app: published on your own developer account versus the platform account, and what happens when you switch'))

# 6. student journey ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['A student\'s week in *your app*'], 54)
b += lines(62, 150, ['From the store listing to the next class, with one login'], 22)
steps = [('Finds you on Play Store', 'Searches your academy name', 'search'),
         ('Installs and logs in', 'Same account as your website', 'download'),
         ('Opens the course', 'Video, PDFs and notes', 'video'),
         ('Takes the weekly test', 'Rank and percentile', 'trophy'),
         ('Joins the live class', 'From inside the course', 'play'),
         ('Gets a reminder', 'Class or test alert', 'bell')]
for i, (t, s, ic) in enumerate(steps):
    y = 200 + i * 124
    b += pill_card(60, y, 620, t, s, ic, h=104, tile=BLUE if i == 0 else NAVY_TILE, title_size=25)
    b += num_badge(660, y + 6, i + 1, 20)
    if i < 5:
        b += f'<line x1="110" y1="{y + 104}" x2="110" y2="{y + 124}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="4 4"/>'
b += phone(800, 200, 310, BIO)
b += text(955, 880, 'Biology Lessons, an academy on AllCoaching', 16, MUTED, anchor='middle')
b += signature(W, H)
save('student-journey', svg(W, H, b, 'Student journey in an LMS mobile app: find it on Play Store, install and log in, open the course, take a test, join a live class and get a notification'))

# 7. iOS by plan --------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Android and iOS app *by plan*'], 54)
b += lines(62, 150, ['AllCoaching plans. Every app is published on your own developer account.'], 22)
b += white_panel(40, 196, 1140, 620, 28, big=True)
heads = [('Plan', 90, 'start'), ('Price', 500, 'middle'), ('Fee per sale', 720, 'middle'), ('Android', 900, 'middle'), ('iOS', 1060, 'middle')]
for t, x, a in heads:
    b += text(x, 250, t, 20, MUTED, 700, a, F_HEAD)
plans = [('Starter · monthly', '₹3,999 / month', '0%', False),
         ('Growth · monthly', '₹5,999 / month', '0%', False),
         ('Pro · monthly', '₹7,999 / month', '0%', True),
         ('Starter · yearly', '₹6,999 / year', '10%', True),
         ('Growth · yearly', '₹12,999 / year', '7.5%', True),
         ('Pro · yearly', '₹24,999 / year', '5%', True)]
for i, (n, p, f, ios) in enumerate(plans):
    y = 278 + i * 86
    if i % 2 == 0:
        b += f'<rect x="60" y="{y}" width="1100" height="76" rx="14" fill="#F5F6FC"/>'
    b += text(90, y + 47, n, 23, INK, 700, font=F_HEAD, ls=-0.4)
    b += text(500, y + 47, p, 22, INK, 500, 'middle')
    b += text(720, y + 47, f, 22, BLUE if f == '0%' else INK, 700, 'middle', F_HEAD)
    b += yes(900, y + 39)
    b += yes(1060, y + 39) if ios else no(1060, y + 39)
b += text(60, 856, 'Prices exclude 18% GST. 7-day free trial, no card needed. Google Play US$25 once and Apple US$99 a year are paid', 17, MUTED)
b += text(60, 882, 'by you to Google and Apple. Store review is done by Google and Apple.', 17, MUTED)
save('ios-by-plan', svg(W, H, b + signature(W, H), 'LMS with Android and iOS app by AllCoaching plan: own Android app on every plan, own iOS app on Pro monthly and every yearly plan, prices excluding GST'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['LMS app', 'mistakes.'], 54)
for i, t in enumerate(['"App included" = their app', 'Never asked about iOS', 'Listing in vendor account', 'Paid course, no billing plan', 'App nobody installs']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 520, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 790, ['Ask whose', 'name is on it.'], 38, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Ask which kind of app it is', 'Check iOS plan and account', 'Publish on your own account', 'Read the store billing rules', 'Give students a reason']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Common mistakes when choosing an LMS with a mobile app, and what to do instead', ('split', 600)))
