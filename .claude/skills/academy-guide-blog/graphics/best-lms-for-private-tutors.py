"""Graphics for /blog/best-lms-for-private-tutors.

Run:  python .claude/skills/academy-guide-blog/graphics/best-lms-for-private-tutors.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/best-lms-for-private-tutors

WhatsApp, YouTube and Google Drive appear only as tools being discussed; WhatsApp uses the real mark, Drive and Zoom
are shown by name only (no fake logos). Cost figures are illustrative and use the studio pricing (2026-10-29).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'best-lms-for-private-tutors')
os.makedirs(OUT, exist_ok=True)

ICONS.setdefault('lock', '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')
ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
ICONS['file'] = '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>'
ICONS['award'] = '<circle cx="12" cy="9" r="5"/><path d="M9 13.5 7.5 21 12 18.5 16.5 21 15 13.5"/>'
ICONS['upload'] = '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v4h16v-4"/>'
ICONS['parent'] = '<circle cx="8" cy="7" r="3"/><circle cx="17" cy="9" r="2.3"/><path d="M3 20c0-3.3 2.2-6 5-6s5 2.7 5 6M13.5 20c0-2.5 1.5-4.6 3.5-4.6S20.5 17.5 20.5 20"/>'
ICONS['rupee'] = '<path d="M7 4h10M7 8.5h10M7 4c5 0 7 1.5 7 4.5S12 13 8 13l7 7"/>'
ICONS['cal'] = '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def name_tile(x, y, label, size=72, fs=None):
    """White app-style tile with a plain tool name (no logo drawn)."""
    fs = fs or size * .26
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="#fff"/></g>' +
            text(x + size / 2, y + size / 2 + fs * .36, label, fs, INK, 800, 'middle', F_HEAD, -0.4))


def dot(cx, cy, kind, r=15):
    """Matrix mark: yes (blue tick), part (outlined), no (grey x)."""
    if kind == 'y':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BLUE}"/>' + icon('tick', cx - r * .64, cy - r * .64, r * 1.28, '#fff', 2.8)
    if kind == 'p':
        return f'<circle cx="{cx}" cy="{cy}" r="{r - 1.5}" fill="#fff" stroke="{BLUE}" stroke-width="3"/>' + f'<path d="M{cx} {cy - r + 1.5} A {r - 1.5} {r - 1.5} 0 0 1 {cx} {cy + r - 1.5} Z" fill="{BLUE}"/>'
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#D5D8E2"/>' + icon('x', cx - r * .6, cy - r * .6, r * 1.2, '#fff', 2.8)


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 290, ['The best LMS for', '*private tutors*'], 68)
b += lines(84, 420, ['What a solo tutor needs, what it costs,', 'and when it is worth it'], 26, MUTED)
b += check_row(84, 550, 'Live classes, recordings, notes and tests', 25)
b += check_row(84, 610, 'UPI fees and your own brand and app', 25)
b += check_row(84, 670, 'Honest cost maths and a one-week move', 25)
b += laptop(880, 170, 600, 'studio-courses.jpg')
b += phone(1360, 330, 170, 'studio-mobile.jpg')
b += text(880, 760, 'AllCoaching Studio preview · sample data', 16, MUTED)
save('cover', svg(1600, 900, b, 'Best LMS for private tutors in India: one academy for live classes, recordings, notes, tests and UPI fees'))

# 2. mess vs one login --------------------------------------------------------------
W, H = 1220, 940
b = headline(56, 100, ['Five apps.'], 54)
b += lines(58, 148, ['How most private tuition runs today'], 22)
tools = [('WhatsApp', 'Notes, links, reminders', 'wa'), ('Google Drive', 'PDFs and recordings', 'Drive'),
         ('Zoom', 'Live class link', 'Zoom'), ('UPI app', 'Fee screenshots', 'UPI'), ('Excel / diary', 'Who paid, who did not', 'XLS')]
for i, (t, s, k) in enumerate(tools):
    y = 200 + i * 118
    x = 50 + (i % 2) * 34
    b += white_panel(x, y, 480, 96, 22)
    if k == 'wa':
        b += logo_tile(x + 14, y + 12, logo_whatsapp, 72)
    else:
        b += name_tile(x + 14, y + 12, k, 72, 19 if len(k) > 3 else 22)
    b += text(x + 104, y + 44, t, 24, INK, 700, font=F_HEAD, ls=-0.5)
    b += text(x + 104, y + 74, s, 18, MUTED)
b += tape(70, 800, 470, 'Which file was it?', -1.6, 30)
b += hand(350, 62, ['Did she pay', 'for June?'], 30, INK, -6)
b += arrow('M542 484 L 618 484', BLUE, 5)
b += headline(660, 100, ['*One login.*'], 54)
b += lines(662, 148, ['The same work inside your own academy'], 22)
one = [('Live classes', 'Zoom, YouTube Live or built-in room', 'video'), ('Recordings and notes', 'Inside each course', 'file'),
       ('Tests and results', 'Auto-graded, rank and percentile', 'check'), ('Fees by UPI', 'Checkout, access opens', 'card'),
       ('Students', 'Imported from your sheet', 'users')]
b += white_panel(640, 190, 540, 610, 28, big=True)
for i, (t, s, ic) in enumerate(one):
    b += pill_card(660, 206 + i * 116, 500, t, s, ic, h=100, tile=BLUE_TINT, title_size=23)
b += text(56, 905, 'Logos belong to their owners. Drive, Zoom and UPI shown by name only.', 16, MUTED)
b += signature(W, H)
save('tools-vs-one-login', svg(W, H, b, 'Private tutor running classes on WhatsApp, Google Drive, Zoom, UPI screenshots and Excel versus one LMS login for live classes, notes, tests and fees', ('split', 600)))

# 3. needs checklist ----------------------------------------------------------------
W, H = 1220, 1010
b = headline(60, 100, ['What a tutor *actually needs*'], 54)
b += lines(62, 150, ['Nine things to check before you pick an LMS. Skip the rest.'], 22)
needs = [('Live classes', 'Small batches and 1:1', 'video'), ('Recordings', 'For revision and absentees', 'play'),
         ('Notes and PDFs', 'Organised by chapter', 'file'), ('Tests with results', 'Marks, rank, weak topics', 'check'),
         ('Fees by UPI', 'Pay, then access opens', 'card'), ('Parent visibility', 'Progress they can see', 'parent'),
         ('Own brand and app', 'Your name, not the platform', 'phone'), ('Certificates', 'For skill courses', 'award'),
         ('Bulk import', 'Bring your students in', 'upload')]
for i, (t, s, ic) in enumerate(needs):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 146
    if i == 8:
        x = 340
    b += pill_card(x, y, 540, t, s, ic, h=116, tile=NAVY_TILE if i < 5 else BLUE, title_size=25)
    b += num_badge(x + 512, y + 6, i + 1, 20)
b += signature(W, H)
save('tutor-needs-checklist', svg(W, H, b, 'Checklist of what a private tutor needs in an LMS: live classes, recordings, notes, tests, UPI fees, parent visibility, own brand and app, certificates and bulk import'))

# 4. options by type matrix ---------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Four ways to run *private tuition*'], 54)
b += lines(62, 150, ['What each type gives a solo tutor. A summary, not a ranking.'], 22)
b += white_panel(40, 190, 1140, 690, 28, big=True)
cols = [('Sheet +', 'WhatsApp', 470), ('Tutoring', 'marketplace', 640), ('Shared-app', 'course tool', 820), ('Own-academy', 'LMS', 1010)]
for a, c2, cx in cols:
    b += text(cx, 240, a, 21, INK, 800, 'middle', F_HEAD, -0.4)
    b += text(cx, 266, c2, 21, INK, 800, 'middle', F_HEAD, -0.4)
b += f'<rect x="920" y="206" width="180" height="660" rx="20" fill="{BLUE}" opacity=".07"/>'
rows = [('Starting cost', ['y', 'y', 'y', 'p']),
        ('Finds students for you', ['n', 'y', 'n', 'p']),
        ('Student stays yours', ['y', 'n', 'p', 'y']),
        ('Your brand and app', ['n', 'n', 'p', 'y']),
        ('Sell recorded courses', ['n', 'p', 'y', 'y']),
        ('Tests with results', ['n', 'p', 'p', 'y']),
        ('Fees collected by UPI', ['p', 'y', 'y', 'y']),
        ('Paid content stays paid', ['n', 'y', 'y', 'y'])]
for i, (lab, vals) in enumerate(rows):
    y = 300 + i * 70
    if i % 2 == 0:
        b += f'<rect x="60" y="{y}" width="1100" height="62" rx="14" fill="#F5F6FC"/>'
    b += text(84, y + 40, lab, 21, INK, 600, font=F_HEAD, ls=-0.3)
    for (a, c2, cx), v in zip(cols, vals):
        b += dot(cx, y + 31, v)
b += dot(90, 912, 'y', 12) + text(110, 919, 'Usually yes', 17, INK)
b += dot(250, 912, 'p', 12) + text(270, 919, 'Depends on plan or platform', 17, INK)
b += dot(530, 912, 'n', 12) + text(550, 919, 'Usually no', 17, INK)
b += text(60, 960, 'Starting cost: a tick means little or nothing upfront. Check each platform\'s own page.', 16, MUTED)
b += signature(W, H)
save('options-by-type', svg(W, H, b, 'LMS options for private tutors by type: spreadsheet and WhatsApp, tutoring marketplace, shared-app course tool and own-academy LMS compared'))

# 5. cost maths (illustrative) ------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['The cost maths, *honestly*'], 54)
b += lines(62, 150, ['Illustrative tutors. Platform cost for a year, before GST and gateway charges.'], 22)
prof = [('Tutor A · starting online', '₹1.2 lakh a year', '6 students × ₹2,000 × 10 months', 18999, 47988),
        ('Tutor B · full batch', '₹5 lakh a year', '20 students × ₹2,500 × 10 months', 56999, 47988),
        ('Tutor C · growing', '₹12 lakh a year', '40 students × ₹3,000 × 10 months', 126999, 47988)]
mx = 130000
for i, (t, rev, calc, yr, mo) in enumerate(prof):
    y = 200 + i * 236
    b += white_panel(60, y, 1100, 212, 26)
    b += text(90, y + 48, t, 26, INK, 800, font=F_HEAD, ls=-0.7)
    b += text(1130, y + 48, rev, 24, BLUE, 800, 'end', F_HEAD, -0.5)
    b += text(90, y + 80, calc, 18, MUTED)
    for k, (lab, v, col) in enumerate([('Starter yearly · ₹6,999 + 10%', yr, '#AFC3F5'), ('Starter monthly · ₹3,999 × 12, 0%', mo, BLUE)]):
        yy = y + 106 + k * 50
        bw = 560 * v / mx
        b += text(90, yy + 28, lab, 18, INK, 500)
        b += f'<rect x="420" y="{yy + 8}" width="{bw:.0f}" height="30" rx="8" fill="{col}"/>'
        low = (v == min(yr, mo))
        b += text(430 + bw, yy + 30, f'₹{v:,}'.replace('126,999', '1,26,999') + ('  · lower' if low else ''), 19, BLUE if low else INK, 800 if low else 500, font=F_HEAD)
b += text(60, 930, 'Illustrative. Fee per sale counts on payments through your academy. Breakeven ≈ ₹4.1 lakh a year.', 17, MUTED)
b += text(60, 958, 'Prices exclude 18% GST. Growth and Pro yearly can cost less than Starter yearly at higher sales.', 17, MUTED)
b += signature(W, H)
save('cost-maths', svg(W, H, b, 'Illustrative LMS cost maths for private tutors: yearly Starter ₹6,999 plus 10% versus monthly Starter ₹3,999 at 0% commission for three tutor revenue levels'))

# 6. one-week timeline --------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Move your tuition *in one week*'], 54)
b += lines(62, 150, ['A plan most solo tutors can follow around their classes'], 22)
days = [('Day 1', 'Start the trial, name your academy', 'globe'),
        ('Day 2', 'Upload logo, colours, first course', 'upload'),
        ('Day 3', 'Add notes, recordings and one test', 'file'),
        ('Day 4', 'Set fees and connect payouts', 'card'),
        ('Day 5', 'Import students from your sheet', 'users'),
        ('Day 6', 'Run one live class from the course', 'video'),
        ('Day 7', 'Message parents, set a switch date', 'message')]
b += f'<line x1="130" y1="220" x2="130" y2="{200 + 6 * 108 + 40}" stroke="{BLUE}" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>'
for i, (d, t, ic) in enumerate(days):
    y = 196 + i * 108
    b += f'<circle cx="130" cy="{y + 44}" r="34" fill="{BLUE if i in (0, 6) else NAVY_TILE}"/>'
    b += text(130, y + 51, d.split()[1], 24, '#fff', 800, 'middle', F_HEAD)
    b += pill_card(190, y, 960, t, d, ic, h=88, tile=BLUE_TINT, title_size=25)
b += signature(W, H)
save('one-week-move', svg(W, H, b, 'One-week plan to move private tuition from WhatsApp and Drive onto an LMS: trial, branding, content, fees, student import, first live class and parent message'))

# 7. product promo ------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Your tuition,', '*your own*', '*academy.*'], 62)
b += lines(64, 440, ['Website and Android app in', 'your name. Courses, tests,', 'live classes and UPI fees.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Courses', 'file', 'Video, PDF, tests'), ('Test series', 'check', 'Rank, percentile'), ('Live', 'video', 'Zoom, YouTube'),
                                     ('Certificates', 'award', 'Auto-issued'), ('Import', 'upload', 'Excel, Sheets')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission from ₹3,999/month + GST', 26, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('academy-for-tutors', svg(W, H, b, 'AllCoaching Studio on a laptop and phone for private tutors: courses, test series with rank, live classes, certificates and bulk student import'))

# 8. mistakes -----------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['LMS mistakes', 'tutors make.'], 54)
for i, t in enumerate(['Buying institute software', 'Paying before 10 students', 'Paid notes on open links', 'Letting the platform own students', 'Moving everyone overnight']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 530, t, -1.4 if i % 2 else 1.0, 26)
b += hand(300, 790, ['Start with what', 'you teach.'], 38, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Buy for one tutor, not ten', 'Start yearly, small', 'Notes behind a login', 'Your brand, your list', 'One switch date, then move']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Mistakes private tutors make when choosing an LMS and what to do instead', ('split', 600)))
