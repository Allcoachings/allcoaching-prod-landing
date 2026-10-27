"""Graphics for /blog/edtech-marketplace-india-app-fatigue
(EdTech App Fatigue: Why Students Won't Install Your App).

Run:  python .claude/skills/academy-guide-blog/graphics/edtech-marketplace-india-app-fatigue.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/edtech-marketplace-india-app-fatigue

Every number shown is illustrative and labelled so. Studio screenshots are sample data.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'edtech-marketplace-india-app-fatigue')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


TILE_COLS = ['#C9CDD8', '#AFC3F5', '#D9D2F2', '#F3D9C6', '#CFE7DA', '#E9D5D5', '#D6DBE6', '#E8E0C8']


def crowded_phone(x, y, w, labels, badges=(1, 4, 6, 9, 13, 15)):
    """A drawn phone home screen packed with generic app tiles (no real brands)."""
    h = w * 2.07
    out = (f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w * .16}" fill="#121317"/></g>'
           f'<rect x="{x + w * .045}" y="{y + w * .045}" width="{w * .91}" height="{h - w * .09}" rx="{w * .13}" fill="#EEF0F6"/>'
           f'<rect x="{x + w * .34}" y="{y + w * .08}" width="{w * .32}" height="{w * .07}" rx="{w * .035}" fill="#000"/>')
    # storage warning bar
    out += (f'<rect x="{x + w * .1}" y="{y + w * .2}" width="{w * .8}" height="{w * .17}" rx="{w * .05}" fill="#fff"/>'
            f'<circle cx="{x + w * .19}" cy="{y + w * .285}" r="{w * .045}" fill="{RED}"/>' +
            text(x + w * .27, y + w * .27, 'Storage almost full', w * .055, INK, 700, font=F_HEAD) +
            text(x + w * .27, y + w * .33, 'Remove apps to free space', w * .042, MUTED))
    ts = w * .17
    gap = (w * .8 - 4 * ts) / 3
    for i, lab in enumerate(labels):
        cx = x + w * .1 + (i % 4) * (ts + gap)
        cy = y + w * .45 + (i // 4) * (ts + w * .12)
        out += f'<rect x="{cx}" y="{cy}" width="{ts}" height="{ts}" rx="{ts * .26}" fill="{TILE_COLS[i % len(TILE_COLS)]}"/>'
        out += text(cx + ts / 2, cy + ts + w * .055, lab, w * .04, INK, 500, 'middle')
        if i in badges:
            out += (f'<circle cx="{cx + ts - 2}" cy="{cy + 2}" r="{w * .035}" fill="{RED}" stroke="#fff" stroke-width="2"/>')
    # dock
    dy = y + h - w * .36
    out += f'<rect x="{x + w * .08}" y="{dy}" width="{w * .84}" height="{w * .25}" rx="{w * .09}" fill="#DADDE7"/>'
    for k in range(4):
        out += f'<rect x="{x + w * .1 + k * (ts + gap)}" y="{dy + w * .04}" width="{ts}" height="{ts}" rx="{ts * .26}" fill="{TILE_COLS[(k + 3) % len(TILE_COLS)]}"/>'
    return out


# 1. cover ----------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 290, ['One more app?', '*Students say no.*'], 80)
b += lines(84, 460, ['App fatigue is real. Build an academy that', 'opens from one link, on your own domain.'], 30, MUTED)
b += check_row(84, 600, 'Works in the browser first', 26)
b += check_row(84, 660, 'Your own app, optional for students', 26)
b += check_row(84, 720, 'One academy instead of five tools', 26)
b += crowded_phone(860, 120, 300, ['Batch', 'Tests', 'School', 'Notes', 'Live', 'Doubts', 'Mock', 'PDFs', 'Quiz', 'Class', 'Fees', 'Extra', 'Maths', 'Revise', 'GK', 'Exam'])
b += tape(840, 770, 330, 'Another OTP?', -2.5, 30)
b += text(1250, 196, 'Studio preview · sample data', 15, MUTED)
b += phone(1270, 210, 230, 'studio-mobile.jpg')
b += pill_card(1190, 720, 360, 'youracademy.in', 'Opens in any browser', 'globe')
save('cover', svg(1600, 900, b, 'EdTech app fatigue: a student phone full of coaching apps versus one academy link on your own domain', ('split', 1210)))

# 2. what app fatigue looks like ----------------------------------------------------
W, H = 1220, 1020
b = headline(56, 110, ['What *app fatigue*', 'looks like'], 58)
b += lines(58, 230, ['One student. One phone.', 'Every teacher wants their own app.'], 24)
b += crowded_phone(80, 330, 300, ['Batch', 'Tests', 'School', 'Notes', 'Live', 'Doubts', 'Mock', 'PDFs', 'Quiz', 'Class', 'Fees', 'Extra', 'Maths', 'Revise', 'GK', 'Exam'])
notes = ['Storage full', 'Another OTP', 'Which app had the test?', 'Data pack over', 'Too many alerts']
for i, t in enumerate(notes):
    b += tape(470 + (i % 2) * 26, 300 + i * 112, 600, t, -1.4 if i % 2 else 1.1, 30)
b += hand(560, 900, ['I will just watch', 'on YouTube'], 40, INK, -5)
b += arrow('M540 905 C 470 930, 430 900, 400 860', INK, 3)
b += text(56, H - 28, 'Illustrative.', 16, MUTED)
b += signature(W, H)
save('what-app-fatigue-looks-like', svg(W, H, b, 'What edtech app fatigue looks like: a student phone crowded with coaching apps, storage full, repeated OTPs and too many alerts', 'grey'))

# 3. why students skip the install -----------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Why students *skip the install*'], 52)
b += lines(62, 150, ['Six reasons, and what each one asks of you.'], 22)
why = [('Low storage', 'Budget phones fill up fast', 'Nothing to install first'),
       ('Data limits', 'A big download costs data', 'Light pages, video on YouTube'),
       ('Shared phone', 'A parent or sibling uses it', 'Sign in from any browser'),
       ('Low trust', 'Unknown app from a link', 'Your name on your domain'),
       ('Too many alerts', 'Every app wants attention', 'Fewer places to check'),
       ('Not sure yet', 'They have not paid you', 'A free lesson, no install')]
for i, (t, s, fix) in enumerate(why):
    y = 200 + i * 124
    b += white_panel(60, y, 560, 100, 22)
    b += check_row(92, y + 46, t, 24, ok=False)
    b += text(136, y + 78, s, 17, MUTED)
    b += arrow(f'M636 {y + 50} H 690', BLUE, 3)
    b += white_panel(706, y, 454, 100, 22)
    b += check_row(738, y + 58, fix, 21)
b += signature(W, H)
save('why-students-skip', svg(W, H, b, 'Why students won\'t download a coaching app: low storage, data limits, shared phones, low trust, too many alerts and not being sure yet, with the fix for each'))

# 4. where students drop (illustrative) --------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Where the *install step* loses students'], 50)
b += lines(62, 150, ['Two paths from the same link. Illustrative, not measured data.'], 22)
for col, (x, title, steps, widths, blue) in enumerate([
        (60, 'App first', ['Taps your link', 'Sent to the app store', 'Installs the app', 'Signs up, OTP', 'Finds the course, pays'], [500, 450, 380, 330, 300], False),
        (640, 'Web first', ['Taps your link', 'Course page opens', 'Watches the free lesson', 'Signs up, OTP', 'Pays by UPI'], [500, 470, 420, 380, 330], True)]):
    b += white_panel(x, 200, 520, 680, 28)
    b += eyebrow(x + 36, 250, title, BLUE if blue else MUTED)
    for i, (st, w) in enumerate(zip(steps, widths)):
        y = 290 + i * 112
        b += f'<rect x="{x + 36}" y="{y}" width="{w * 0.88:.0f}" height="58" rx="16" fill="{BLUE if blue else "#C9CDD8"}" opacity="{1 - i * 0.12:.2f}"/>'
        b += text(x + 56, y + 37, st, 21, '#fff' if blue else INK, 700, font=F_HEAD, ls=-0.3)
b += hand(436, 512, ['most', 'drop', 'here'], 30, RED, -4)
b += arrow('M440 560 C 430 548, 425 540, 418 532', INK, 3)
b += text(640, 930, 'Bar widths are illustrative. Measure your own path.', 17, MUTED)
b += signature(W, H)
save('install-step', svg(W, H, b, 'Illustrative comparison of an app-first and a web-first path from one shared link to a paid enrolment, showing where the install step loses students'))

# 5. coaching app vs website ------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Coaching app *or* website?'], 56)
b += lines(62, 150, ['What each does best for an Indian educator.'], 22)
b += white_panel(60, 190, 1100, 720, 28)
b += f'<rect x="780" y="206" width="364" height="688" rx="20" fill="{BLUE_TINT}"/>'
b += eyebrow(92, 246, 'Question', MUTED) + eyebrow(420, 246, 'App only', MUTED) + eyebrow(812, 246, 'Web first + app', BLUE)
rows = [('First visit', 'Install before anything', 'Opens from one link'),
        ('Found on Google', 'App pages are not', 'Course pages can rank'),
        ('Low-storage phones', 'Often skipped', 'Nothing to install'),
        ('Daily learners', 'Good, one tap away', 'Your app is there too'),
        ('Shared in WhatsApp', 'Link to a store page', 'Link to the course'),
        ('Who maintains it', 'Depends who built it', 'Runs on the platform')]
for r, (k, a, w_) in enumerate(rows):
    y = 330 + r * 96
    b += f'<line x1="92" y1="{y - 46}" x2="1128" y2="{y - 46}" stroke="{LINE}" stroke-width="2"/>'
    b += text(92, y, k, 22, INK, 700, font=F_HEAD, ls=-0.4)
    b += text(420, y, a, 20, MUTED, 500)
    b += f'<circle cx="828" cy="{y - 7}" r="14" fill="{BLUE}"/>' + icon('tick', 819, y - 16, 18, '#fff', 2.8)
    b += text(854, y, w_, 20, INK, 600)
b += text(60, H - 28, 'General comparison. On AllCoaching the Android app is on every plan, iOS on Pro.', 16, MUTED)
b += signature(W, H)
save('app-vs-website', svg(W, H, b, 'Coaching app vs website compared: first visit, Google search, low-storage phones, daily learners, WhatsApp sharing and maintenance'))

# 6. web-first path with studio ----------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['One link. *No install needed.*'], 54)
b += lines(62, 150, ['A student goes from your link to your course in the browser.'], 22)
flow = [('Your link', 'youracademy.in/neet-bio', 'link'),
        ('Course page', 'Free lesson, syllabus, price', 'book'),
        ('UPI checkout', 'Access opens on its own', 'card'),
        ('Learn', 'Videos, PDFs, tests, live', 'play')]
for i, (t, s, ic) in enumerate(flow):
    y = 210 + i * 150
    b += pill_card(60, y, 470, t, s, ic, h=112, tile=NAVY_TILE if i % 2 == 0 else BLUE, title_size=26)
    if i < 3:
        b += arrow(f'M120 {y + 116} V {y + 146}', BLUE, 3)
b += text(620, 236, 'Studio preview · sample data', 15, MUTED)
b += laptop(630, 252, 520, 'studio-courses.jpg')
b += white_panel(630, 650, 520, 190, 24)
b += eyebrow(660, 700, 'Optional, for daily learners')
b += icon('phone', 662, 724, 40, BLUE, 2)
b += text(716, 756, 'Your own Android app', 24, INK, 700, font=F_HEAD, ls=-0.5)
b += text(716, 790, 'iOS app on Pro', 19, MUTED)
b += text(60, H - 28, 'youracademy.in is an example address.', 16, MUTED)
b += signature(W, H)
save('web-first-path', svg(W, H, b, 'Web-first academy path that avoids app fatigue: one link, course page, UPI checkout and learning in the browser, with an optional own app'))

# 7. who needs the app --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Make the app *optional*'], 56)
b += lines(62, 150, ['Who is happy on the web, and who will want your app.'], 22)
for col, (x, title, items, ic) in enumerate([
        (60, 'Web is enough', ['Trying a free lesson', 'Buying a short course', 'Low-storage phone', 'Shared family phone'], 'globe'),
        (640, 'Offer the app', ['Daily test series', 'Long batch, live every day', 'Watches on the go', 'Asked you for an app'], 'phone')]):
    b += white_panel(x, 200, 520, 600, 28)
    b += f'<rect x="{x + 32}" y="232" width="68" height="68" rx="18" fill="{BLUE if col else NAVY_TILE}"/>' + icon(ic, x + 48, 248, 36, '#fff', 2)
    b += text(x + 122, 278, title, 32, INK, 800, font=F_HEAD, ls=-1)
    for i, t in enumerate(items):
        b += check_row(x + 40, 390 + i * 96, t, 24)
b += text(60, H - 28, 'Both groups use the same academy: the website and the app run on it together.', 16, MUTED)
b += signature(W, H)
save('optional-app', svg(W, H, b, 'Who is happy with a web academy and who will want a coaching app: make the app optional to avoid app fatigue'))

# 8. five tools vs one academy ------------------------------------------------------------
W, H = 1220, 980
b = headline(56, 110, ['Five places', 'to check?'], 58)
tools = [(logo_whatsapp, 'Fees and links'), (logo_youtube, 'Lessons'), (logo_google, 'Notes in Drive'),
         (logo_instagram, 'Updates'), (None, 'A separate test app')]
for i, (fn, t) in enumerate(tools):
    y = 220 + i * 112
    if fn:
        b += logo_tile(56, y, fn, 76)
    else:
        b += f'<g filter="url(#sh)"><rect x="56" y="{y}" width="76" height="76" rx="20" fill="#fff"/></g>' + icon('check', 76, y + 18, 38, MUTED, 2)
    b += tape(156 + (i % 2) * 14, y + 4, 400, t, -1.2 if i % 2 else 0.9, 28)
b += hand(120, 870, ['Where was', "today's link?"], 38, INK, -5)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 240, ['One link.', '*Your whole academy.*'], 50)
for i, t in enumerate(['Lessons, notes and tests', 'Live classes on schedule', 'UPI and card checkout', 'Your domain, your brand', 'Your own app, if wanted']):
    b += check_row(656, 390 + i * 74, t, 25)
b += text(656, 790, 'Keep WhatsApp for reminders. Teach inside the academy.', 19, MUTED, 500)
b += text(56, H - 28, 'Logos belong to their owners.', 15, MUTED)
b += signature(W, H)
save('tools-vs-one-academy', svg(W, H, b, 'Too many education apps and tools (WhatsApp, YouTube, Drive, Instagram, a test app) versus one academy link', ('split', 600)))

# 9. seven-step plan ------------------------------------------------------------------------
W, H = 1220, 1120
b = headline(60, 100, ['Beat app fatigue in *7 steps*'], 56)
b += lines(62, 150, ['From an app-only habit to a web-first academy.'], 22)
st = [('Count where students drop', 'Link, install, sign-up, payment', 'chart'),
      ('Put the academy on your domain', 'One address students remember', 'globe'),
      ('Make lesson one free on the web', 'No install to try you', 'play'),
      ('Take UPI on the course page', 'Access opens on its own', 'card'),
      ('Offer the app after purchase', 'For daily learners only', 'phone'),
      ('Cut the tool stack', 'One place for class and tests', 'layers'),
      ('Send one link everywhere', 'YouTube, Instagram, WhatsApp', 'link')]
for i, (t, s, ic) in enumerate(st):
    y = 196 + i * 124
    b += white_panel(150, y, 1010, 102, 24)
    b += num_badge(96, y + 51, i + 1, 26)
    b += f'<rect x="174" y="{y + 20}" width="62" height="62" rx="18" fill="{NAVY_TILE if i % 2 == 0 else BLUE}"/>' + icon(ic, 189, y + 35, 32, '#fff', 2)
    b += text(262, y + 48, t, 28, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(262, y + 80, s, 19, MUTED)
b += signature(W, H)
save('seven-steps', svg(W, H, b, 'Seven steps to beat edtech app fatigue: measure drop-off, own domain, free web lesson, UPI checkout, optional app, fewer tools, one link'))
