"""Graphics for /blog/youtube-live-vs-zoom-for-teachers.

Run:  python .claude/skills/academy-guide-blog/graphics/youtube-live-vs-zoom-for-teachers.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/youtube-live-vs-zoom-for-teachers

YouTube uses the real mark (logo_youtube). Zoom has no mark in brand_graphics, so it is shown as a plain
name tile (no fake logo). Third-party facts are summarised from their own help / pricing pages, checked 4 Nov 2026.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'youtube-live-vs-zoom-for-teachers')
os.makedirs(OUT, exist_ok=True)

ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
ICONS['wifi'] = '<path d="M2 8.5a15 15 0 0 1 20 0M5 12a10 10 0 0 1 14 0M8.5 15.5a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1.2"/>'
ICONS['sun'] = '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
ICONS['monitor'] = '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>'
ICONS['cc'] = '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10.5 10a2.2 2.2 0 1 0 0 4M17 10a2.2 2.2 0 1 0 0 4"/>'
ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'
ICONS['eye'] = '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>'
ICONS['camera'] = '<path d="M4 7h4l2-3h4l2 3h4v12H4z"/><circle cx="12" cy="13" r="3.5"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def zoom_tile(x, y, size=72):
    """Plain name tile for Zoom (no logo is drawn)."""
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="#fff"/></g>' +
            text(x + size / 2, y + size / 2 + size * .12, 'Zoom', size * .3, INK, 800, 'middle', F_HEAD, -0.5))


def ac_tile(x, y, size=72):
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="#fff"/></g>' +
            mark(x + size * .16, y + size * .16, size * .68))


def tick(x, y, ok=True, size=26):
    col = BLUE if ok else '#B8BCC8'
    return (f'<circle cx="{x}" cy="{y}" r="{size / 2}" fill="{col}"/>' +
            icon('tick' if ok else 'x', x - size * .32, y - size * .32, size * .64, '#fff', 2.8))


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['YouTube Live vs Zoom', 'vs a *built-in live room*'], 64)
b += lines(84, 430, ['Which one to use for a free class, a paid batch,', 'a doubt session or a webinar'], 25, MUTED)
b += check_row(84, 560, 'Audience, interaction and privacy compared', 25)
b += check_row(84, 620, 'Free-tier limits from their own pages', 25)
b += check_row(84, 680, 'A decision table and a setup kit', 25)
cards = [(logo_tile, logo_youtube, 'YouTube Live', 'Big, public reach'),
         (None, 'zoom', 'Zoom', 'Two-way classroom'),
         (None, 'ac', 'Built-in live room', 'Paid students only')]
for i, (fn, lg, t, s) in enumerate(cards):
    y = 150 + i * 190
    b += white_panel(960, y, 540, 160, 30, big=True)
    if fn:
        b += logo_tile(990, y + 40, logo_youtube, 80)
    elif lg == 'zoom':
        b += zoom_tile(990, y + 40, 80)
    else:
        b += ac_tile(990, y + 40, 80)
    b += text(1100, y + 76, t, 32, INK, 800, font=F_HEAD, ls=-1)
    b += text(1100, y + 112, s, 22, MUTED)
b += text(960, 760, 'Logos belong to their owners · Zoom shown by name only', 16, MUTED)
save('cover', svg(1600, 900, b, 'YouTube Live vs Zoom for teachers vs a built-in live room inside your own academy'))

# 2. three-way comparison --------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Three tools, *three jobs*'], 54)
b += lines(62, 150, ['What each one does well for a teacher, side by side'], 22)
cols = [('YouTube Live', 'yt', 430), ('Zoom', 'zoom', 690), ('Built-in room', 'ac', 950)]
b += white_panel(40, 196, 1140, 660, 28, big=True)
for t, k, cx in cols:
    if k == 'yt':
        b += logo_tile(cx - 36, 222, logo_youtube, 72)
    elif k == 'zoom':
        b += zoom_tile(cx - 36, 222, 72)
    else:
        b += ac_tile(cx - 36, 222, 72)
    b += text(cx, 330, t, 24, INK, 800, 'middle', F_HEAD, -0.6)
rows = [('Best for', ['Free public class', 'Small live session', 'Paid batch']),
        ('Who can join', ['Anyone (public)', 'Anyone with link', 'Enrolled students']),
        ('Free-tier limit', ['Eligibility rules', '40 min, 100 people', 'Plan hours (paid)']),
        ('Recording', ['Saved to channel', 'Local on free tier', 'Saved in academy']),
        ('Attendance', ['No class register', 'Depends on plan', 'Built in']),
        ('Name watermark', ['No', 'No', 'Each student'])]
for i, (lab, vals) in enumerate(rows):
    y = 380 + i * 78
    if i % 2 == 0:
        b += f'<rect x="60" y="{y}" width="1100" height="70" rx="14" fill="#F5F6FC"/>'
    b += text(84, y + 44, lab, 21, INK, 700, font=F_HEAD, ls=-0.3)
    for (t, k, cx), v in zip(cols, vals):
        col = BLUE if (k == 'ac' and v in ('Enrolled students', 'Built in', 'Each student', 'Saved in academy', 'Paid batch')) else INK
        b += text(cx, y + 44, v, 19, col, 600 if col == BLUE else 400, 'middle')
b += text(60, 890, 'Summary of YouTube Help and zoom.us/pricing, checked 4 Nov 2026.', 16, MUTED)
b += text(60, 916, 'Built-in room = AllCoaching live classroom, hours by plan. Logos belong to their owners; Zoom shown by name.', 16, MUTED)
b += signature(W, H)
save('three-way', svg(W, H, b, 'YouTube Live vs Zoom vs a built-in live room compared for teachers: audience, access, interaction, free-tier limits, recording, attendance and watermark'))

# 3. decision tree ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Which one *for this class?*'], 54)
b += lines(62, 150, ['Start with two questions: is it paid, and do students need to talk?'], 22)
b += f'<g filter="url(#sh)"><rect x="410" y="200" width="400" height="96" rx="48" fill="{INK}"/></g>'
b += text(610, 258, 'Is the class paid?', 28, '#fff', 800, 'middle', F_HEAD, -0.6)
b += arrow('M520 300 C 470 340, 330 340, 300 384', BLUE, 4) + arrow('M700 300 C 750 340, 890 340, 920 384', BLUE, 4)
b += text(400, 318, 'No, free', 20, BLUE, 700, 'end') + text(820, 318, 'Yes, paid', 20, BLUE, 700)
# left branch
b += f'<g filter="url(#sh)"><rect x="80" y="400" width="440" height="88" rx="44" fill="#fff"/></g>' + text(300, 454, 'Hundreds or more viewers?', 24, INK, 800, 'middle', F_HEAD, -0.5)
b += arrow('M200 492 L 170 560', BLUE, 4) + arrow('M400 492 L 430 560', BLUE, 4)
b += text(150, 532, 'Yes', 18, BLUE, 700, 'end') + text(450, 532, 'No', 18, BLUE, 700)
b += pill_card(40, 576, 260, 'YouTube Live', 'Big free class', 'play', h=110, tile=NAVY_TILE, title_size=23)
b += pill_card(320, 576, 260, 'Zoom', 'Small free class', 'users', h=110, tile=NAVY_TILE, title_size=23)
# right branch
b += f'<g filter="url(#sh)"><rect x="700" y="400" width="440" height="88" rx="44" fill="#fff"/></g>' + text(920, 454, 'Students must speak?', 24, INK, 800, 'middle', F_HEAD, -0.5)
b += arrow('M820 492 L 790 560', BLUE, 4) + arrow('M1020 492 L 1050 560', BLUE, 4)
b += text(770, 532, 'Often', 18, BLUE, 700, 'end') + text(1070, 532, 'Mostly listen', 18, BLUE, 700)
b += pill_card(640, 576, 270, 'Zoom + access', 'Doubt session', 'message', h=110, tile=NAVY_TILE, title_size=23)
b += pill_card(930, 576, 250, 'Built-in room', 'Paid batch', 'shield', h=110, tile=BLUE, title_size=23)
b += white_panel(60, 740, 1100, 170, 24)
b += text(90, 790, 'A common mix (illustrative):', 22, INK, 700, font=F_HEAD)
b += text(90, 830, 'Free weekly class on YouTube Live → paid batch in your academy\'s live room →', 21, INK)
b += text(90, 864, 'doubt session on Zoom or in the room → recordings stay inside the course.', 21, INK)
b += signature(W, H)
save('decision-tree', svg(W, H, b, 'Decision tree for teachers: YouTube Live for free public classes and webinars, Zoom for small interactive sessions, a built-in live room for paid batches'))

# 4. access / privacy matrix ------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Who can *actually join?*'], 54)
b += lines(62, 150, ['Privacy settings decide whether a paid class stays paid'], 22)
opts = [('YouTube · Public', 'Anyone on YouTube; can show in search', 'globe', 'open'),
        ('YouTube · Unlisted', 'Anyone with the link; no Google account needed', 'link', False),
        ('YouTube · Private', 'Only you and the people you choose', 'lock', None),
        ('Zoom meeting', 'Anyone with the link and passcode', 'users', None),
        ('Built-in live room', 'Only students enrolled in the course', 'shield', True)]
for i, (t, s, ic, ok) in enumerate(opts):
    y = 200 + i * 130
    b += pill_card(60, y, 760, t, s, ic, h=108, tile=BLUE if ok is True else NAVY_TILE, title_size=25)
    lab, col = {'open': ('Open to all', MUTED), False: ('Link can leak', RED), None: ('Manage by hand', '#B7791F'), True: ('Paid-only', BLUE)}[ok]
    b += f'<rect x="850" y="{y + 30}" width="300" height="50" rx="25" fill="#fff" stroke="{col}" stroke-width="2.5"/>'
    b += text(1000, y + 63, lab, 21, col, 700, 'middle', F_HEAD)
b += text(60, 888, 'Summary of YouTube Help (video privacy settings), checked 4 Nov 2026. Zoom shown by name only.', 16, MUTED)
b += signature(W, H)
save('access-matrix', svg(W, H, b, 'Live class privacy for teachers: YouTube public, unlisted and private, a Zoom meeting link, and a built-in live room for enrolled students only'))

# 5. setup kit -------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Your live class *setup kit*'], 54)
b += lines(62, 150, ['Sound first, then light, then picture. No brand needed.'], 22)
kit = [('Microphone', 'Wired lapel or USB mic', 'mic'),
       ('Lighting', 'Face a window or a soft lamp', 'sun'),
       ('Camera', 'Phone or webcam at eye level', 'camera'),
       ('Internet', 'Wired or close to the router', 'wifi'),
       ('OBS Studio', 'Free encoder for screen + face', 'monitor'),
       ('Second screen', 'To read chat and questions', 'message'),
       ('Backup', 'Phone hotspot, charged', 'phone'),
       ('Test run', '10 minutes, unlisted, alone', 'check')]
for i, (t, s, ic) in enumerate(kit):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 150
    b += pill_card(x, y, 540, t, s, ic, h=118, tile=NAVY_TILE if i < 4 else BLUE_TINT, title_size=25)
    b += num_badge(x + 518, y + 4, i + 1, 20)
b += signature(W, H)
save('setup-kit', svg(W, H, b, 'Live class setup kit for teachers: microphone, lighting, camera, internet, OBS Studio, second screen, backup and a test run'))

# 6. built-in room features ------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Inside a *built-in live room*'], 54)
b += lines(62, 150, ['What the AllCoaching live classroom adds, as seen in the studio'], 22)
px, py, pw, ph = 60, 200, 640, 400
b += white_panel(px - 10, py - 10, pw + 20, ph + 80, 30, big=True)
b += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="20" fill="#1B1E2E"/>'
b += f'<rect x="{px + 40}" y="{py + 40}" width="{pw - 80}" height="{ph - 150}" rx="12" fill="#262A3D"/>'
b += text(px + 70, py + 100, 'Organic Chemistry · Live', 26, '#fff', 700, font=F_HEAD)
b += ghost_lines(px + 70, py + 130, [380, 300, 340], 34, ('#4A5070', '#3A4060'))
b += text(px + pw - 40, py + ph - 140, 'Riya S.', 18, '#fff', 500, 'end', opacity=.45)
b += f'<rect x="{px + 90}" y="{py + ph - 92}" width="{pw - 180}" height="44" rx="10" fill="#000" opacity=".7"/>'
b += text(px + pw / 2, py + ph - 62, 'CC  "Ab hum reaction mechanism dekhenge"', 19, '#fff', 500, 'middle')
b += f'<circle cx="{px + 48}" cy="{py + ph + 34}" r="9" fill="{RED}"/>' + text(px + 66, py + ph + 41, 'Recording', 18, INK, 600)
b += text(px + pw - 10, py + ph + 41, 'Illustrative screen', 16, MUTED, anchor='end')
feats = [('Paid-only access', 'Enrolled students only', 'lock'),
         ('Attendance', 'Who joined, built in', 'users'),
         ('Recordings', 'Saved for revision', 'video'),
         ('Name watermark', 'Each student\'s own name', 'shield'),
         ('Captions', 'Hindi, Punjabi, English', 'cc')]
for i, (t, s, ic) in enumerate(feats):
    b += pill_card(740, 196 + i * 128, 420, t, s, ic, h=106, tile=BLUE_TINT, title_size=23)
b += text(60, 860, 'Hours by plan: monthly 20 / 50 / 90 h, yearly 5 / 10 / 15 h a month.', 21, INK, 600)
b += text(60, 892, 'YouTube Live and Zoom classes are unlimited on every plan.', 18, MUTED)
b += signature(W, H)
save('built-in-room', svg(W, H, b, 'Built-in live classroom features: paid-only access, attendance, recordings, each student name watermarked and captions in Hindi, Punjabi and English'))

# 7. hours by plan ---------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Built-in live hours *by plan*'], 54)
b += lines(62, 150, ['Hours a month in the built-in room. YouTube Live and Zoom stay unlimited.'], 22)
b += white_panel(60, 196, 1100, 600, 28)
plans = [('Starter', 20, 5), ('Growth', 50, 10), ('Pro', 90, 15)]
base, top = 700, 300
scale = (base - top) / 90
for i, (n, m, y_) in enumerate(plans):
    gx = 200 + i * 330
    hm, hy = m * scale, y_ * scale
    b += f'<rect x="{gx}" y="{base - hm}" width="100" height="{hm}" rx="12" fill="{BLUE}"/>'
    b += f'<rect x="{gx + 116}" y="{base - hy}" width="100" height="{hy}" rx="12" fill="#AFC3F5"/>'
    b += text(gx + 50, base - hm - 16, f'{m} h', 26, INK, 800, 'middle', F_HEAD)
    b += text(gx + 166, base - hy - 16, f'{y_} h', 26, INK, 800, 'middle', F_HEAD)
    b += text(gx + 108, base + 44, n, 26, INK, 800, 'middle', F_HEAD, -0.6)
b += f'<line x1="120" y1="{base}" x2="1100" y2="{base}" stroke="{LINE}" stroke-width="2"/>'
b += f'<rect x="120" y="230" width="22" height="22" rx="6" fill="{BLUE}"/>' + text(152, 248, 'Monthly plan (0% commission)', 18, INK)
b += f'<rect x="120" y="264" width="22" height="22" rx="6" fill="#AFC3F5"/>' + text(152, 282, 'Yearly plan (fee per sale)', 18, INK)
b += text(60, 834, 'Monthly ₹3,999 / ₹5,999 / ₹7,999 · Yearly ₹6,999 / ₹12,999 / ₹24,999 + fee per sale · + GST', 18, MUTED)
b += signature(W, H)
save('hours-by-plan', svg(W, H, b, 'Built-in live classroom hours by AllCoaching plan: monthly Starter 20, Growth 50, Pro 90 hours; yearly 5, 10 and 15 hours a month'))

# 8. mistakes --------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Live class', 'mistakes.'], 54)
for i, t in enumerate(['Paid class on unlisted link', 'Free Zoom, 2-hour class', 'Going live untested', 'Bad mic, great camera', 'No recording plan']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 520, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 790, ['Students notice', 'sound first.'], 38, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Paid batch behind a login', 'Check the free-tier limit', 'Test run the day before', 'Spend on the mic first', 'Recording into the course']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Common live class mistakes teachers make with YouTube Live and Zoom, and what to do instead', ('split', 600)))
