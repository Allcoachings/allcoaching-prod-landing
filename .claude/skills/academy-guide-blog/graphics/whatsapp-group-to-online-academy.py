"""Graphics for /blog/whatsapp-group-to-online-academy.

Run:  python .claude/skills/academy-guide-blog/graphics/whatsapp-group-to-online-academy.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/whatsapp-group-to-online-academy
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'whatsapp-group-to-online-academy')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def tile(x, y, ic, size=60, dark=True):
    col = NAVY_TILE if dark else BLUE_TINT
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .27:.0f}" fill="{col}"/>' +
            icon(ic, x + size * .22, y + size * .22, size * .56, '#fff' if dark else BLUE, 2))


def grey_chip(x, y, w, label, ic):
    """Muted 'old tool' chip for the problem side."""
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="64" rx="18" fill="#fff" opacity=".9"/></g>'
            f'<rect x="{x + 12}" y="{y + 12}" width="40" height="40" rx="11" fill="#C9CCD6"/>' +
            icon(ic, x + 20, y + 20, 24, '#fff', 2) + text(x + 66, y + 40, label, 20, '#4A4E5C', 600, font=F_HEAD, ls=-0.3))


# 1. cover ----------------------------------------------------------------------
b = f'<rect width="640" height="900" fill="url(#bgG)"/>'
b += lockup(700, 60, 1.0)
b += eyebrow(64, 92, 'Before')
b += logo_tile(64, 124, logo_whatsapp, 76)
b += text(160, 162, 'Batch group · 214 members', 22, INK, 700, font=F_HEAD, ls=-0.4)
b += text(160, 190, 'Illustrative', 16, MUTED)
for i, (t, ic) in enumerate([('Google Form for admissions', 'list'), ('UPI screenshots to check', 'image'),
                             ('Zoom link, shared daily', 'link'), ('PDFs in a Drive folder', 'file')]):
    b += grey_chip(64 + (i % 2) * 18, 250 + i * 86, 470, t, ic)
b += tape(70, 618, 420, 'Payment screenshot?', -2.5, 32)
b += hand(96, 760, ['Who has paid', 'this month?'], 40, INK, -5)
b += arrow('M560 470 C 620 470, 640 470, 690 470', BLUE, 5)
b += headline(720, 270, ['From WhatsApp group', 'to *your own academy.*'], 58)
b += lines(722, 380, ['One checkout, one course library, one login.'], 26, MUTED)
b += text(720, 444, 'Studio preview · sample data', 15, MUTED)
b += laptop(720, 460, 640, 'studio-courses.jpg')
b += phone(1400, 540, 150, 'studio-mobile.jpg')
save('cover', svg(1600, 900, b, 'Moving from a WhatsApp group to your own online academy: Google Forms, UPI screenshots, Zoom links and Drive PDFs replaced by one academy in the AllCoaching studio'))

# 2. before vs after -----------------------------------------------------------------
W, H = 1220, 1080
b = headline(40, 96, ['Before', 'and *after*'], 50)
b += eyebrow(40, 210, 'WhatsApp + Forms + UPI + Drive')
for i, (t, ic) in enumerate([('Admission via Google Form', 'list'), ('Fees as UPI screenshots', 'image'),
                             ('Zoom link pasted each day', 'link'), ('Notes in a Drive folder', 'file'),
                             ('Attendance in a notebook', 'book')]):
    b += grey_chip(40 + (i % 2) * 14, 240 + i * 88, 500, t, ic)
b += tape(36, 700, 470, 'Payment screenshot?', -2.4, 30)
b += tape(70, 786, 440, 'Where are old notes?', 1.8, 30)
b += tape(30, 872, 460, 'Link not opening', -1.2, 30)
b += hand(330, 990, ['every month, by hand'], 34, INK, -4)
b += eyebrow(660, 210, 'Your own academy')
b += white_panel(660, 236, 520, 640, 28, True)
b += mark(690, 266, 44)
b += text(746, 297, 'youracademy.in', 26, INK, 800, font=F_HEAD, ls=-0.6)
rows = ['Course page with a buy button', 'UPI or card checkout', 'Access opens after payment',
        'Every past lesson and PDF in order', 'Live class link inside the course', 'Tests with scores', 'Student list you can export']
for i, t in enumerate(rows):
    b += check_row(694, 370 + i * 68, t, 21)
b += f'<rect x="660" y="900" width="520" height="70" rx="20" fill="{BLUE_TINT}"/>'
b += text(690, 944, 'WhatsApp stays for announcements', 21, BLUE, 700, font=F_HEAD, ls=-0.3)
b += text(40, H - 28, 'Illustrative. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('before-after', svg(W, H, b, 'Before and after moving a coaching batch from WhatsApp groups to an online academy: manual forms, UPI screenshots, links and Drive PDFs versus one checkout and course library', ('split', 610)))

# 3. audit map ----------------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Audit: *what moves where*'], 54)
b += lines(62, 150, ['List every tool your batch uses today, then give each one a new home.'], 22)
pairs = [('WhatsApp group', 'Announcements, reminders', 'Stays on WhatsApp', 'message', True),
         ('Google Form', 'Admission details', 'Sign-up at checkout', 'list', False),
         ('UPI screenshots', 'Fee proof', 'UPI or card checkout', 'card', False),
         ('Zoom / Meet links', 'Live classes', 'Live class inside the course', 'video', False),
         ('Drive PDFs', 'Notes, PYQs', 'Course PDFs in order', 'file', False),
         ('YouTube links', 'Recorded lectures', 'Course videos (via YouTube)', 'play', False),
         ('Excel sheet', 'Who paid, who left', 'Student list in the studio', 'users', False)]
b += eyebrow(60, 214, 'Today') + eyebrow(700, 214, 'After the move')
for i, (t, s, n, ic, stay) in enumerate(pairs):
    y = 236 + i * 106
    b += white_panel(60, y, 520, 86, 22)
    b += f'<rect x="80" y="{y + 17}" width="52" height="52" rx="14" fill="#C9CCD6"/>' + icon(ic, 92, y + 29, 28, '#fff', 2)
    b += text(150, y + 40, t, 23, INK, 800, font=F_HEAD, ls=-0.5)
    b += text(150, y + 68, s, 17, MUTED)
    b += arrow(f'M596 {y + 43} H 676', BLUE, 3)
    fill = '#fff' if stay else BLUE_TINT
    b += f'<g filter="url(#sh)"><rect x="700" y="{y}" width="460" height="86" rx="22" fill="{fill}"/></g>'
    if stay:
        b += logo_tile(716, y + 13, logo_whatsapp, 60)
    else:
        b += tile(716, y + 13, ic, 60)
    b += text(796, y + 51, n, 22, INK, 700, font=F_HEAD, ls=-0.4)
b += text(60, H - 28, 'Example audit, illustrative. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('audit-map', svg(W, H, b, 'Audit of a WhatsApp coaching batch: Google Form, UPI screenshots, Zoom links, Drive PDFs, YouTube links and Excel each mapped to their place in an online academy'))

# 4. fee collection: manual vs checkout ---------------------------------------------------
W, H = 1220, 880
b = headline(60, 100, ['Collect fees online, *not by hand*'], 52)
b += lines(62, 150, ['The same ₹ payment, two very different evenings.'], 22)
b += eyebrow(60, 222, 'Manual · six steps per student', MUTED)
man = ['Student sends a UPI payment', 'Sends a screenshot on WhatsApp', 'You open the bank app to match it',
       'You note it in a sheet', 'You add them to the group', 'You resend old links and PDFs']
for i, t in enumerate(man):
    y = 250 + i * 76
    b += f'<rect x="60" y="{y}" width="520" height="60" rx="16" fill="#EDEDF0"/>'
    b += f'<circle cx="94" cy="{y + 30}" r="16" fill="#9EA1AB"/>' + text(94, y + 37, str(i + 1), 18, '#fff', 800, 'middle', F_HEAD)
    b += text(124, y + 37, t, 19, '#4A4E5C', 500)
b += hand(120, 760, ['x 40 students,', 'every batch'], 36, INK, -4)
b += eyebrow(640, 222, 'Checkout · two steps')
b += white_panel(640, 250, 520, 200, 26)
b += num_badge(684, 300, 1, 20)
b += text(718, 308, 'Student pays by UPI or card', 23, INK, 800, font=F_HEAD, ls=-0.5)
b += text(718, 338, 'on your course page', 18, MUTED)
b += num_badge(684, 392, 2, 20)
b += text(718, 400, 'Access opens on its own', 23, INK, 800, font=F_HEAD, ls=-0.5)
b += text(718, 430, 'every past lesson, PDF and test', 18, MUTED)
b += white_panel(640, 480, 520, 300, 26)
b += eyebrow(670, 524, 'What you do instead')
for i, t in enumerate(['Teach the class', 'Answer doubts', 'Plan the next module']):
    b += check_row(674, 584 + i * 60, t, 21)
b += text(670, 760, 'Payouts reach your bank through Razorpay.', 17, MUTED)
b += text(60, H - 28, 'Illustrative.', 16, MUTED)
b += signature(W, H)
save('fee-collection', svg(W, H, b, 'Collecting coaching fees online: six manual steps with UPI screenshots on WhatsApp versus a two-step UPI or card checkout that opens course access automatically', ('split', 610)))

# 5. what stays on WhatsApp vs what moves ----------------------------------------------------
W, H = 1220, 840
b = headline(60, 100, ['Keep WhatsApp for *talking*'], 54)
b += lines(62, 150, ['Move the teaching and the money. Keep the chat.'], 22)
b += white_panel(60, 200, 530, 540, 28)
b += logo_tile(90, 230, logo_whatsapp, 68)
b += text(176, 262, 'Stays on WhatsApp', 27, INK, 800, font=F_HEAD, ls=-0.7)
b += text(176, 290, 'Group, Community or Channel', 18, MUTED)
for i, t in enumerate(['Class reminders', 'New lesson alerts', 'Exam and form dates', 'Quick motivation notes', 'Link to your academy']):
    b += check_row(94, 370 + i * 76, t, 21)
b += white_panel(630, 200, 530, 540, 28)
b += mark(660, 232, 64)
b += text(746, 262, 'Moves to your academy', 27, INK, 800, font=F_HEAD, ls=-0.7)
b += text(746, 290, 'youracademy.in + Android app', 18, MUTED)
for i, t in enumerate(['Fees and enrolment', 'Recorded lessons, in order', 'PDF notes and PYQs', 'Tests and scores', 'Live class links']):
    b += check_row(664, 370 + i * 76, t, 21)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('stays-vs-moves', svg(W, H, b, 'What stays on WhatsApp after moving to an online academy (reminders, alerts, dates) and what moves to the academy (fees, lessons, PDFs, tests, live links)'))

# 6. migration timeline ------------------------------------------------------------------------
W, H = 1220, 1120
b = headline(60, 100, ['A *four-week* migration plan'], 54)
b += lines(62, 150, ['Set a switch-over date and work back from it. Illustrative timing.'], 22)
b += f'<path d="M120 230 V 1000" stroke="{BLUE}" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>'
weeks = [('Week 1', 'Audit', 'List tools, students, content and dues', 'search'),
         ('Week 1', 'Set up and upload', 'Academy, domain, old lessons as one course', 'layers'),
         ('Week 2', 'Price and checkout', 'Set price, test a ₹ payment with a friend', 'card'),
         ('Week 2', 'Announce', 'Send the message and the switch-over date', 'message'),
         ('Week 3', 'Switch-over date', 'New fees, notes and links only in the academy', 'calendar'),
         ('Week 4', 'Follow up', 'Call or message students who have not moved', 'users')]
for i, (wk, t, s, ic) in enumerate(weeks):
    y = 200 + i * 136
    hot = i == 4
    b += f'<circle cx="120" cy="{y + 56}" r="{26 if hot else 20}" fill="{BLUE if hot else "#fff"}" stroke="{BLUE}" stroke-width="4"/>'
    if hot:
        b += icon('star', 108, y + 44, 24, '#fff', 2.2)
    else:
        b += text(120, y + 63, str(i + 1), 18, BLUE, 800, 'middle', F_HEAD)
    fill = BLUE if hot else '#fff'
    b += f'<g filter="url({"#shB" if hot else "#sh"})"><rect x="180" y="{y}" width="980" height="112" rx="26" fill="{fill}"/></g>'
    b += tile(206, y + 24, ic, 64, not hot)
    b += text(296, y + 46, wk.upper(), 15, '#DCE2FF' if hot else BLUE, 600, font=F_MONO, ls=1.6)
    b += text(296, y + 82, t, 28, '#fff' if hot else INK, 800, font=F_HEAD, ls=-0.8)
    b += text(640, y + 72, s, 19, '#DCE2FF' if hot else MUTED)
b += text(60, H - 28, 'Timing is illustrative. A small batch can move in two weeks.', 16, MUTED)
b += signature(W, H)
save('migration-timeline', svg(W, H, b, 'Migration timeline from a WhatsApp group to an online academy: audit, set up and upload, price and checkout, announce, switch-over date and follow-up'))

# 7. announcement message mock -------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['The *announcement* message'], 54)
b += lines(62, 150, ['Short, specific, with one link and one date. Template, illustrative.'], 22)
b += white_panel(60, 200, 640, 720, 30, True)
b += f'<rect x="60" y="200" width="640" height="84" rx="30" fill="#F0F2F5"/><rect x="60" y="250" width="640" height="34" fill="#F0F2F5"/>'
b += logo_whatsapp(86, 220, 44)
b += text(146, 250, 'SSC Maths · Batch 2026', 22, INK, 700, font=F_HEAD, ls=-0.3)
msg = ['From 1 December, our batch moves to', 'our own academy: youracademy.in', '',
       'What changes:', '• Fees: pay by UPI or card on the course page', '• Notes, old lessons and tests: all in one place',
       '• Live class link: inside the course', '', 'What stays: this group, for reminders.', '',
       'Already paid for November? You keep access.', 'Questions? Reply here.']
b += f'<rect x="96" y="310" width="568" height="{len(msg) * 38 + 40}" rx="20" fill="#D9FDD3"/>'
for i, ln in enumerate(msg):
    wgt = 700 if ln.endswith(':') or ln.startswith('From') else 400
    b += text(122, 352 + i * 38, ln, 20, INK, wgt)
b += white_panel(740, 200, 420, 720, 30)
b += eyebrow(772, 252, 'Every message has')
for i, (t, s) in enumerate([('One date', 'The switch-over day'), ('One link', 'Your academy URL'),
                            ('What changes', 'Fees, notes, links'), ('What stays', 'The group, for news'),
                            ('Paid students', 'Their access is safe'), ('A way to ask', 'Reply or call')]):
    y = 300 + i * 100
    b += f'<rect x="772" y="{y}" width="48" height="48" rx="14" fill="{BLUE_TINT}"/>' + icon('check', 784, y + 12, 24, BLUE, 2.2)
    b += text(838, y + 22, t, 22, INK, 800, font=F_HEAD, ls=-0.4)
    b += text(838, y + 46, s, 17, MUTED)
b += text(60, H - 28, 'Sample batch and dates. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('announcement-message', svg(W, H, b, 'Template WhatsApp announcement for moving a coaching batch to an online academy: switch-over date, academy link, what changes and what stays'))

# 8. mistakes ------------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Six *migration* mistakes'], 54)
mist = [('Moving overnight', 'Announce two weeks ahead'),
        ('Charging paid students again', 'Honour what they paid'),
        ('Deleting the group', 'Keep it for announcements'),
        ('Uploading a messy Drive', 'Rebuild it as modules'),
        ('No switch-over date', 'Pick one and keep it'),
        ('Never following up', 'Message who has not moved')]
for i, (t, fix) in enumerate(mist):
    y = 170 + i * 118
    b += tape(40 + (i % 2) * 16, y, 540, t, -1.2 if i % 2 else 0.9, 28)
    b += arrow(f'M604 {y + 36} H 660', BLUE, 3)
    b += white_panel(680, y + 2, 480, 70, 20)
    b += f'<circle cx="716" cy="{y + 37}" r="16" fill="{BLUE}"/>' + icon('tick', 706, y + 27, 20, '#fff', 2.8)
    b += text(746, y + 45, fix, 22, INK, 600, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Six common mistakes when moving students from a WhatsApp group to an online academy and the fix for each', ('split', 640)))
