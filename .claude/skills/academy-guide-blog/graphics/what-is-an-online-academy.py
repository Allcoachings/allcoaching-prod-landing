"""Graphics for /blog/what-is-an-online-academy.

Run:  python .claude/skills/academy-guide-blog/graphics/what-is-an-online-academy.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/what-is-an-online-academy
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'what-is-an-online-academy')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 330, ['What is an', '*online academy?*'], 92)
b += lines(84, 510, ['Meaning, types and how it works.'], 32, MUTED)
b += check_row(84, 600, 'Your website on your own domain', 26)
b += check_row(84, 660, 'Courses, tests, notes and live classes', 26)
b += check_row(84, 720, 'Payments and your own app, built in', 26)
b += laptop(860, 210, 600, 'studio-desktop.jpg')
b += phone(1390, 330, 150, 'studio-mobile.jpg')
b += pill_card(800, 650, 380, 'youracademy.in', 'Your domain, your brand', 'globe')
b += text(860, 190, 'Studio preview · sample data', 15, MUTED)
save('cover', svg(1600, 900, b, 'What is an online academy: an educator\'s own website, courses, live classes, payments and app in one place'))

# 2. anatomy -------------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['The parts of an *online academy*'], 52)
b += lines(62, 150, ['Seven parts, one place. Students see the front; you run the back.'], 22)
b += laptop(110, 230, 470, 'studio-desktop.jpg')
b += phone(500, 330, 130, 'studio-mobile.jpg')
b += text(110, 214, 'Studio preview · sample data', 15, MUTED)
parts = [('Website on your domain', 'youracademy.in, your logo and colours', 'globe'),
         ('Courses', 'Video lessons, PDF notes, test series', 'play'),
         ('Live classes', 'Batches, doubt sessions, recordings', 'video'),
         ('Payments', 'UPI and card checkout, auto access', 'card'),
         ('Student app', 'Your name on the student\'s phone', 'phone'),
         ('Student data', 'Who enrolled, paid and progressed', 'users'),
         ('Marketing tools', 'Pixel, tag manager, SEO pages', 'trend')]
for i, (t, s, ic) in enumerate(parts):
    y = 200 + i * 112
    b += white_panel(690, y, 470, 94, 22)
    b += num_badge(728, y + 47, i + 1)
    b += f'<rect x="770" y="{y + 20}" width="54" height="54" rx="15" fill="{BLUE_TINT}"/>' + icon(ic, 783, y + 33, 28, BLUE, 2)
    b += text(842, y + 42, t, 23, INK, 700, font=F_HEAD, ls=-0.5) + text(842, y + 72, s, 17, MUTED)
b += f'<g filter="url(#sh)"><rect x="110" y="740" width="520" height="190" rx="26" fill="{NAVY_TILE}"/></g>'
b += eyebrow(140, 790, 'The difference', '#9FB0FF')
b += lines(140, 838, ['A course is one product.', 'An academy is the whole school.'], 26, '#fff', 1.4, weight=700, font=F_HEAD)
b += signature(W, H)
save('anatomy', svg(W, H, b, 'The seven parts of an online academy: website, courses, live classes, payments, student app, student data and marketing tools'))

# 3. comparison matrix -----------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Academy vs course vs *channel*'], 52)
b += lines(62, 150, ['What each option usually gives an educator'], 22)
cols = ['Single course', 'YouTube channel', 'Marketplace listing', 'LMS software', 'Online academy']
rows = [('Your brand and domain', ['no', 'no', 'no', 'part', 'yes']),
        ('Many courses, one place', ['no', 'part', 'part', 'yes', 'yes']),
        ('Checkout built in', ['part', 'no', 'yes', 'part', 'yes']),
        ('Live classes', ['no', 'yes', 'part', 'part', 'yes']),
        ('Student data you can export', ['part', 'no', 'no', 'yes', 'yes']),
        ('Your own student app', ['no', 'no', 'no', 'part', 'yes']),
        ('Discovery traffic', ['no', 'yes', 'yes', 'no', 'part'])]
b += white_panel(60, 190, 1100, 700, 28, big=True)
lx, cx0, cw = 92, 400, 150
for k, c in enumerate(cols):
    x = cx0 + k * cw + cw / 2
    hl = k == 4
    if hl:
        b += f'<rect x="{cx0 + k * cw + 6}" y="206" width="{cw - 12}" height="668" rx="20" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2"/>'
    words = c.split(' ')
    b += text(x, 250, words[0], 18, BLUE if hl else INK, 700, 'middle', F_HEAD)
    b += text(x, 274, ' '.join(words[1:]), 18, BLUE if hl else INK, 700, 'middle', F_HEAD)
for r, (lab, vals) in enumerate(rows):
    y = 340 + r * 78
    b += f'<line x1="{lx}" y1="{y - 40}" x2="1130" y2="{y - 40}" stroke="{LINE}" stroke-width="2"/>'
    b += text(lx, y + 6, lab, 20, INK, 600)
    for k, v in enumerate(vals):
        x = cx0 + k * cw + cw / 2
        if v == 'yes':
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="{BLUE}"/>' + icon('tick', x - 10, y - 10, 20, '#fff', 2.8)
        elif v == 'no':
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="#ECEDF2"/>' + icon('x', x - 8, y - 8, 16, '#9AA0AE', 2.6)
        else:
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="#fff" stroke="{BLUE}" stroke-width="2.5"/><path d="M{x} {y - 15} A15 15 0 0 1 {x} {y + 15} Z" fill="{BLUE}"/>'
b += f'<circle cx="76" cy="{H - 34}" r="9" fill="{BLUE}"/>' + text(92, H - 28, 'Yes', 16, MUTED)
b += f'<circle cx="150" cy="{H - 34}" r="9" fill="#fff" stroke="{BLUE}" stroke-width="2"/><path d="M150 {H - 43} A9 9 0 0 1 150 {H - 25} Z" fill="{BLUE}"/>' + text(166, H - 28, 'Depends on the platform', 16, MUTED)
b += f'<circle cx="378" cy="{H - 34}" r="9" fill="#ECEDF2"/>' + text(394, H - 28, 'Usually not  ·  Typical setups; individual platforms vary.', 16, MUTED)
b += signature(W, H)
save('comparison-matrix', svg(W, H, b, 'Online academy compared with a single online course, a YouTube channel, a marketplace listing and LMS software'))

# 4. academy vs LMS ---------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['An LMS is the engine.', 'The academy is *the whole school.*'], 50)
cx, cy = 430, 520
b += f'<circle cx="{cx}" cy="{cy}" r="300" fill="#fff" filter="url(#shL)"/>'
b += f'<circle cx="{cx}" cy="{cy}" r="140" fill="{BLUE}" filter="url(#shB)"/>'
b += eyebrow(cx, cy - 22, 'LMS', '#C9D3FF', 'middle')
b += text(cx, cy + 16, 'Courses, tests,', 24, '#fff', 700, 'middle', F_HEAD) + text(cx, cy + 46, 'progress tracking', 24, '#fff', 700, 'middle', F_HEAD)
ring = [(cx, cy - 250, 'Brand + domain'), (cx + 222, cy - 120, 'Checkout'), (cx + 222, cy + 130, 'Student app'),
        (cx, cy + 262, 'Live classes'), (cx - 222, cy + 130, 'Marketing'), (cx - 222, cy - 120, 'Student data')]
for x, y, t in ring:
    w = len(t) * 12 + 40
    b += f'<rect x="{x - w / 2}" y="{y - 22}" width="{w}" height="44" rx="22" fill="{BLUE_TINT}"/>' + text(x, y + 7, t, 19, INK, 600, 'middle', F_HEAD)
b += eyebrow(800, 330, 'LMS answers')
b += lines(800, 372, ['How do students learn', 'and how is it tracked?'], 26, INK, 1.35, weight=700, font=F_HEAD)
b += eyebrow(800, 520, 'An academy also answers')
b += lines(800, 562, ['Who finds you, how they pay,', 'what they install, and whose', 'name they remember?'], 26, INK, 1.35, weight=700, font=F_HEAD)
b += text(60, H - 28, 'Concept diagram. Many LMS products include some of the outer ring.', 16, MUTED)
b += signature(W, H)
save('academy-vs-lms', svg(W, H, b, 'Online academy vs LMS: the LMS handles learning; the academy adds brand, checkout, app, live classes, marketing and student data'))

# 5. types grid ----------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Six *types* of online academy'], 52)
b += lines(62, 150, ['Most Indian educators fit one of these, or mix two'], 22)
types = [('Exam-prep academy', 'trophy', ['NEET, JEE, SSC, UPSC,', 'banking, CUET, CLAT']),
         ('Skill academy', 'sparkle', ['Spoken English, yoga,', 'music, coding, design']),
         ('School-tuition academy', 'book', ['CBSE and state boards,', 'Class 6 to 12']),
         ('Cohort or bootcamp', 'calendar', ['Fixed dates, one batch,', 'live-first, 4–12 weeks']),
         ('Membership academy', 'users', ['Monthly or yearly access,', 'community, new content']),
         ('Institute going online', 'home', ['Offline centre adds', 'online batches and tests'])]
for i, (t, ic, d) in enumerate(types):
    x = 60 + (i % 3) * 375
    y = 200 + (i // 3) * 370
    b += white_panel(x, y, 350, 340, 28)
    b += f'<rect x="{x + 30}" y="{y + 30}" width="72" height="72" rx="20" fill="{NAVY_TILE}"/>' + icon(ic, x + 48, y + 48, 36, '#fff', 2)
    b += eyebrow(x + 30, y + 150, f'Type {i + 1}')
    b += text(x + 30, y + 196, t, 27 if len(t) < 20 else 24, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(x + 30, y + 250, d, 20, MUTED, 1.45)
b += signature(W, H)
save('types', svg(W, H, b, 'Six types of online academy: exam-prep, skill, school tuition, cohort or bootcamp, membership and an institute going online'))

# 6. how it works ------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['How an online academy *works*'], 52)
b += lines(62, 150, ['Five things you do. Four that run on their own.'], 22)
steps = [('Sign up', 'user'), ('Choose a plan', 'tag'), ('Upload your course', 'play'), ('Connect your domain', 'globe'), ('Start selling', 'trend')]
for i, (t, ic) in enumerate(steps):
    x = 60 + i * 226
    b += white_panel(x, 210, 200, 250, 26)
    b += num_badge(x + 44, 254, i + 1)
    b += f'<rect x="{x + 66}" y="{300}" width="68" height="68" rx="18" fill="{NAVY_TILE}"/>' + icon(ic if ic != 'user' else 'users', x + 82, 316, 36, '#fff', 2)
    words = t.split(' ')
    if len(words) > 2:
        b += text(x + 100, 412, ' '.join(words[:2]), 22, INK, 800, 'middle', F_HEAD, -0.6) + text(x + 100, 440, ' '.join(words[2:]), 22, INK, 800, 'middle', F_HEAD, -0.6)
    else:
        b += text(x + 100, 420, t, 22, INK, 800, 'middle', F_HEAD, -0.6)
    if i < 4:
        b += arrow(f'M{x + 204} 335 H {x + 222}', BLUE, 3)
b += eyebrow(60, 540, 'Then, automatically')
b += f'<path d="M610 470 V 510" stroke="{BLUE}" stroke-width="3" stroke-dasharray="4 6"/>'
auto = [('Payments', 'UPI and cards collected', 'card'), ('Access', 'Paid students get in', 'shield'),
        ('Apps', 'Your branded app, kept running', 'phone'), ('Hosting', 'Site stays online', 'server')]
for i, (t, s, ic) in enumerate(auto):
    x = 60 + (i % 2) * 560
    y = 570 + (i // 2) * 124
    b += pill_card(x, y, 540, t, s, ic, tile=BLUE)
b += signature(W, H)
save('how-it-works', svg(W, H, b, 'How an online academy works: sign up, choose a plan, upload your course, connect your domain, start selling; payments, access, apps and hosting run automatically'))

# 7. before / after ------------------------------------------------------------------------
W, H = 1220, 940
b = headline(56, 110, ['Teaching online', 'like this?'], 58)
b += logo_tile(310, 118, logo_whatsapp, 58) + logo_tile(380, 118, logo_youtube, 58)
for i, t in enumerate(['Fees on WhatsApp', 'Notes as Drive links', 'New Zoom link daily', 'Attendance in Excel', 'Who paid? Not sure']):
    b += tape(40 + (i % 2) * 22, 250 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(330, 820, ['Too many', 'tools.'], 40, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['One login.', '*Your whole academy.*'], 52)
for i, t in enumerate(['Fees collected at checkout', 'Notes and videos in courses', 'Live class inside the app', 'Progress tracked for you', 'Every payment on record']):
    b += check_row(656, 380 + i * 74, t, 25)
b += text(656, 800, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('before-after', svg(W, H, b, 'Before: fees on WhatsApp, notes on Drive, Zoom links and Excel. After: one online academy login', ('split', 600)))

# 8. cost components -----------------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['What an online academy *costs*'], 52)
b += lines(62, 150, ['Six lines to add up before you launch'], 22)
costs = [('Platform plan', 'Yearly or monthly fee for the', 'software. Check if GST is extra.', 'layers'),
         ('Fee on sales', 'A percentage some platforms', 'keep from each sale.', 'tag'),
         ('Domain name', 'Bought yearly from a registrar,', 'renewed in your name.', 'globe'),
         ('Payment gateway', 'Per-transaction charge, e.g.', 'Razorpay standard: 2% + GST.', 'card'),
         ('GST', 'On platform bills, and on your', 'own fees if you are registered.', 'file'),
         ('Content and gear', 'Mic, lighting, your time to', 'record and plan the syllabus.', 'mic')]
for i, (t, d1, d2, ic) in enumerate(costs):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 210
    b += white_panel(x, y, 540, 186, 26)
    b += f'<rect x="{x + 28}" y="{y + 30}" width="64" height="64" rx="18" fill="{BLUE_TINT}"/>' + icon(ic, x + 44, y + 46, 32, BLUE, 2)
    b += text(x + 116, y + 72, t, 28, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(x + 116, y + 118, [d1, d2], 19, MUTED, 1.45)
b += text(60, H - 28, 'Razorpay standard rate from razorpay.com/pricing, checked Oct 2026. Rates change; check before you sign.', 16, MUTED)
b += signature(W, H)
save('cost-components', svg(W, H, b, 'Online academy cost components: platform plan, fee on sales, domain, payment gateway, GST and content production'))

# 9. is it right for you ------------------------------------------------------------------------------
W, H = 1220, 780
b = headline(60, 100, ['Is an online academy *right for you?*'], 50)
b += white_panel(60, 160, 540, 530, 28)
b += eyebrow(92, 214, 'Good fit if you')
for i, t in enumerate(['Teach a subject people pay for', 'Get student questions every week', 'Can teach live or record weekly', 'Want students to know your name', 'Plan more than one batch']):
    b += check_row(92, 270 + i * 90, t, 21)
b += white_panel(620, 160, 540, 530, 28)
b += eyebrow(652, 214, 'Wait a little if you', RED)
for i, t in enumerate(['Have not taught the topic yet', 'Have no content or syllabus', 'Want income without teaching', 'Cannot spare a few hours a week']):
    b += check_row(652, 270 + i * 90, t, 21, ok=False)
b += hand(680, 610, ['Start with one course.', 'Grow from there.'], 36, BLUE, -3)
b += signature(W, H)
save('right-for-you', svg(W, H, b, 'Checklist: is an online academy right for you as an educator'))
