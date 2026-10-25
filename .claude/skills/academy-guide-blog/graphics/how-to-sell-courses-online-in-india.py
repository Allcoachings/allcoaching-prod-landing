"""Graphics for /blog/how-to-sell-courses-online-in-india.

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-sell-courses-online-in-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-sell-courses-online-in-india
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'how-to-sell-courses-online-in-india')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def tile(x, y, ic, size=64, fill=NAVY_TILE, col='#fff'):
    return f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .27:.0f}" fill="{fill}"/>' + icon(ic, x + size * .22, y + size * .22, size * .56, col, 2)


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 320, ['Sell your first course.', '*Earn your first ₹10,000.*'], 76)
b += lines(84, 470, ['How to sell courses online in India, step by step.'], 30, MUTED)
b += check_row(84, 570, 'Pick a course students already ask for', 26)
b += check_row(84, 630, 'A course page with UPI checkout', 26)
b += check_row(84, 690, 'Launch to WhatsApp, YouTube, Instagram', 26)
b += logo_tile(84, 750, logo_whatsapp, 64) + logo_tile(162, 750, logo_youtube, 64) + logo_tile(240, 750, logo_instagram, 64)
b += text(322, 790, 'Logos belong to their owners', 17, MUTED)
b += laptop(900, 250, 560, 'studio-desktop.jpg')
b += phone(1380, 360, 150, 'studio-mobile.jpg')
b += text(900, 232, 'Studio preview · sample data', 15, MUTED)
b += pill_card(840, 650, 400, 'New enrolment', 'SSC Maths in Hindi · ₹1,999', 'card', tile=BLUE)
save('cover', svg(1600, 900, b, 'How to sell courses online in India: from your first student to your first ₹10,000, with an academy on your own domain'))

# 2. roadmap --------------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['The road to your *first ₹10,000*'], 52)
b += lines(62, 150, ['Eight steps, in order. Allow roughly four to six weeks (illustrative).'], 22)
steps = [('Pick the course', 'One your students already ask for', 'message'),
         ('Validate demand', 'Comments, polls, Trends, suggestions', 'search'),
         ('Record a minimum course', 'Videos + PDF notes + a test', 'mic'),
         ('Set the price', 'Illustrative: 10 × ₹999 or 5 × ₹1,999', 'tag'),
         ('Build the course page', 'Promise, demo, syllabus, pay button', 'globe'),
         ('Turn on UPI checkout', 'Access opens on payment', 'card'),
         ('Launch to your warm audience', 'WhatsApp, YouTube, Instagram', 'users'),
         ('Collect reviews, open batch 2', 'Then ads and SEO', 'star')]
for i, (t, s, ic) in enumerate(steps):
    col, row = i % 2, i // 2
    x = 60 + col * 560
    y = 200 + row * 190
    b += white_panel(x, y, 540, 160, 26)
    b += num_badge(x + 46, y + 48, i + 1)
    b += tile(x + 28, y + 80, ic, 56, BLUE_TINT, BLUE)
    b += text(x + 104, y + 56, t, 26, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(x + 104, y + 116, s, 19, MUTED)
b += text(60, H - 28, 'Timeline and prices are illustrative.', 16, MUTED)
b += signature(W, H)
save('first-10000-roadmap', svg(W, H, b, 'Eight steps to sell your first online course in India and earn your first ₹10,000'))

# 3. demand sources ---------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Four free ways to *check demand*'], 52)
b += lines(62, 150, ['Before you record anything, find proof that students want it.'], 22)
src = [(logo_youtube, 'YouTube comments', ['"Sir, full course kab aayega?"', 'Count repeated requests on', 'your most-watched videos.']),
       (logo_whatsapp, 'WhatsApp group poll', ['Ask: which topic should the', 'paid batch cover first?', 'Two or three options only.']),
       (logo_google, 'Google Trends', ['Compare two topics or exams', 'over 12 months in India.', 'Look for steady interest.']),
       (logo_google, 'Search suggestions', ['Type "ssc maths" or "spoken', 'english" and note what Google', 'and YouTube suggest.'])]
for i, (lg, t, d) in enumerate(src):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 300
    b += white_panel(x, y, 540, 270, 26)
    b += logo_tile(x + 28, y + 28, lg, 72)
    if i == 3:
        b += f'<rect x="{x + 116}" y="{y + 46}" width="36" height="36" rx="10" fill="{BLUE_TINT}"/>' + icon('search', x + 122, y + 52, 24, BLUE, 2.2)
    b += text(x + 28, y + 150, t, 28, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(x + 28, y + 192, d, 19, MUTED, 1.4)
b += f'<rect x="60" y="796" width="880" height="46" rx="23" fill="{BLUE_TINT}"/>' + text(500, 826, 'Strong signal: the same request shows up in two or more places.', 19, BLUE, 600, 'middle')
b += text(60, H - 12, 'Logos belong to their owners.', 15, MUTED)
b += signature(W, H)
save('demand-validation-sources', svg(W, H, b, 'Four free ways to validate demand for an online course: YouTube comments, WhatsApp polls, Google Trends and search suggestions'))

# 4. minimum course ---------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['The *minimum course* that can sell'], 52)
b += lines(62, 150, ['Small in scope, complete for one promise. Example: SSC CGL Percentage in Hindi.'], 22)
parts = [('1 free demo lesson', 'Your best 10–15 minutes, public', 'play', True),
         ('8–12 video lessons', 'One topic each, 10–25 min, via YouTube', 'video', False),
         ('PDF notes', 'Formula sheet + solved examples', 'file', False),
         ('Chapter tests', 'Short quiz after each part', 'check', False),
         ('1 final mock', 'Timed, with solutions', 'trophy', False),
         ('Live doubt class', 'Weekly, recorded into the course', 'users', False)]
for i, (t, s, ic, hl) in enumerate(parts):
    y = 200 + i * 108
    b += white_panel(60, y, 640, 92, 22)
    b += tile(82, y + 16, ic, 60, BLUE if hl else NAVY_TILE)
    b += text(164, y + 42, t, 25, INK, 800, font=F_HEAD, ls=-0.6) + text(164, y + 72, s, 18, MUTED)
b += f'<g filter="url(#sh)"><rect x="750" y="200" width="410" height="632" rx="28" fill="{NAVY_TILE}"/></g>'
b += eyebrow(784, 254, 'Rule of thumb', '#9FB0FF')
b += lines(784, 306, ['Finish one promise', 'fully. Do not record', 'the whole syllabus', 'before anyone pays.'], 30, '#fff', 1.3, weight=700, font=F_HEAD)
b += lines(784, 520, ['Your first buyers tell you', 'what to add next: the', 'doubts they ask are your', 'next chapter.'], 20, '#C9D3FF', 1.5)
b += hand(784, 740, ['Ship it in', 'two weeks.'], 40, '#fff', -4)
b += text(60, H - 28, 'Illustrative structure. Adjust lesson count to your subject.', 16, MUTED)
b += signature(W, H)
save('minimum-course-structure', svg(W, H, b, 'Minimum online course structure: free demo lesson, 8 to 12 video lessons, PDF notes, chapter tests, a final mock and a live doubt class'))

# 5. the ₹10,000 maths -----------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['Three ways to *₹10,000*'], 52)
b += lines(62, 150, ['Illustrative maths. Pick the one that fits your course.'], 22)
opts = [('20', '₹499', '₹9,980', 'Notes + test pack', 'Low price, more buyers', False),
        ('10', '₹999', '₹9,990', 'Recorded course', 'The middle path', True),
        ('5', '₹1,999', '₹9,995', 'Course + live doubts', 'Fewer buyers, more support', False)]
for i, (n, p, tot, what, note, hl) in enumerate(opts):
    x = 60 + i * 370
    if hl:
        b += f'<g filter="url(#shB)"><rect x="{x}" y="200" width="350" height="470" rx="28" fill="{BLUE}"/></g>'
        c1, c2, c3 = '#fff', '#DCE2FF', '#fff'
    else:
        b += white_panel(x, 200, 350, 470, 28)
        c1, c2, c3 = INK, MUTED, BLUE
    b += eyebrow(x + 32, 250, what, '#DCE2FF' if hl else BLUE)
    b += text(x + 32, 350, n, 96, c1, 800, font=F_HEAD, ls=-4)
    b += text(x + 32 + {'20': 126, '10': 112, '5': 66}[n], 350, 'students', 24, c2, 600)
    b += text(x + 32, 410, '× ' + p, 40, c1, 800, font=F_HEAD, ls=-1.4)
    b += f'<line x1="{x + 32}" y1="450" x2="{x + 318}" y2="450" stroke="{"#ffffff55" if hl else LINE}" stroke-width="2"/>'
    b += text(x + 32, 530, tot, 54, c3, 800, font=F_HEAD, ls=-2)
    b += text(x + 32, 580, 'in sales', 20, c2)
    b += text(x + 32, 630, note, 19, c2, 600)
b += white_panel(60, 700, 1100, 90, 22)
b += lines(92, 738, ['Before platform fee, payment gateway charges and taxes. On AllCoaching you keep 90–95% after the', 'platform fee (10% on Starter, 7.5% on Growth, 5% on Pro), or 100% on Scale. Plan price is separate.'], 18, INK, 1.45)
b += text(60, H - 28, 'Illustrative figures, not a forecast.', 16, MUTED)
b += signature(W, H)
save('first-10000-maths', svg(W, H, b, 'Illustrative maths for a first ₹10,000: 20 students at ₹499, 10 at ₹999 or 5 at ₹1,999'))

# 6. course page anatomy ------------------------------------------------------------
W, H = 1220, 1060
b = headline(60, 100, ['Anatomy of a course page *that sells*'], 50)
bx, by, bw, bh = 60, 170, 600, 820
b += white_panel(bx, by, bw, bh, 22, big=True)
b += f'<rect x="{bx}" y="{by}" width="{bw}" height="52" rx="22" fill="#F1F2F7"/><rect x="{bx}" y="{by + 30}" width="{bw}" height="22" fill="#F1F2F7"/>'
for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']):
    b += f'<circle cx="{bx + 26 + k * 20}" cy="{by + 26}" r="6" fill="{c}"/>'
b += f'<rect x="{bx + 100}" y="{by + 12}" width="420" height="28" rx="14" fill="#fff"/>' + text(bx + 118, by + 32, 'youracademy.in/ssc-maths-hindi', 15, MUTED)
# 1 promise
b += text(bx + 30, by + 104, 'SSC CGL Maths in Hindi:', 26, INK, 800, font=F_HEAD, ls=-0.8)
b += text(bx + 30, by + 136, 'Percentage to Profit & Loss in 30 days', 22, INK, 600, font=F_HEAD)
# 2 demo video
b += f'<rect x="{bx + 30}" y="{by + 164}" width="330" height="186" rx="14" fill="{NAVY_TILE}"/>'
b += f'<circle cx="{bx + 195}" cy="{by + 257}" r="30" fill="#fff"/><path d="M{bx + 186} {by + 241} L{bx + 212} {by + 257} L{bx + 186} {by + 273}Z" fill="{NAVY_TILE}"/>'
b += text(bx + 46, by + 336, 'Free demo lesson · 14 min', 15, '#fff', 600)
# 3 price + button
b += f'<rect x="{bx + 380}" y="{by + 164}" width="190" height="186" rx="14" fill="{BLUE_TINT}"/>'
b += text(bx + 400, by + 214, '₹999', 40, INK, 800, font=F_HEAD, ls=-1.5) + text(bx + 400, by + 242, 'Illustrative price', 14, MUTED)
b += f'<rect x="{bx + 400}" y="{by + 270}" width="150" height="54" rx="27" fill="{BLUE}"/>' + text(bx + 475, by + 304, 'Enrol now', 19, '#fff', 700, 'middle', F_HEAD)
# 4 syllabus
b += eyebrow(bx + 30, by + 400, 'What you get')
for k, t in enumerate(['12 video lessons in Hindi', 'PDF notes and formula sheet', '6 chapter tests + 1 mock', 'Weekly live doubt class']):
    b += check_row(bx + 30, by + 446 + k * 42, t, 18)
# 5 teacher
b += f'<circle cx="{bx + 62}" cy="{by + 660}" r="32" fill="{BLUE_TINT}"/>' + icon('users', bx + 46, by + 644, 32, BLUE, 2)
b += text(bx + 110, by + 654, 'Your name, your story', 20, INK, 700, font=F_HEAD) + text(bx + 110, by + 680, 'Years teaching, students taught', 16, MUTED)
# 6 reviews + FAQ
b += f'<rect x="{bx + 30}" y="{by + 720}" width="260" height="70" rx="14" fill="#F6F7FB"/>'
for k in range(5):
    b += icon('star', bx + 44 + k * 26, by + 732, 22, '#F5A524', 2)
b += text(bx + 44, by + 778, 'Student reviews', 16, MUTED)
b += f'<rect x="{bx + 310}" y="{by + 720}" width="260" height="70" rx="14" fill="#F6F7FB"/>' + text(bx + 326, by + 750, 'FAQ: validity, refund,', 16, INK, 600) + text(bx + 326, by + 774, 'app, language', 16, INK, 600)
calls = [(by + 100, 'One clear promise', 'Exam, topic, language, time'),
         (by + 200, 'Free demo lesson', 'Lets them judge your teaching'),
         (by + 297, 'Price and one button', 'UPI or card, access on payment'),
         (by + 480, 'What is included', 'Lessons, notes, tests, live'),
         (by + 660, 'Who teaches', 'Real experience, no fake claims'),
         (by + 755, 'Reviews and FAQ', 'Answer the doubts before they ask')]
xs = [bx + 520, None, bx + 570, bx + 420, bx + 400, bx + 570]
for n, ((cy, t, s), x0) in enumerate(zip(calls, xs), 1):
    d = f'M{bx + 345} {by + 152} H 690 L 720 {cy}' if x0 is None else f'M{x0} {cy} H 720'
    b += f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(744, cy, n) + text(780, cy - 2, t, 23, INK, 700, font=F_HEAD, ls=-0.4) + text(780, cy + 26, s, 17, MUTED)
b += text(60, H - 28, 'Illustrative page on a sample domain.', 16, MUTED)
b += signature(W, H)
save('course-page-anatomy', svg(W, H, b, 'Anatomy of an online course page that sells: promise, free demo, price and button, syllabus, teacher, reviews and FAQ'))

# 7. launch week -------------------------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['A seven-day *launch week*'], 52)
b += lines(62, 150, ['Sell to people who already know you first. Illustrative plan.'], 22)
b += f'<line x1="100" y1="220" x2="1120" y2="220" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
days = [('Day 1', 'Announce', ['Course page live,', 'post on WhatsApp', 'and YouTube'], logo_whatsapp),
        ('Day 2', 'Demo', ['Free lesson on', 'YouTube, link to', 'the course page'], logo_youtube),
        ('Day 3', 'Proof', ['Share syllabus,', 'notes sample,', 'your results'], logo_instagram),
        ('Day 4', 'Live Q&A', ['Answer doubts', 'about the course', 'on YouTube Live'], logo_youtube),
        ('Day 5', 'Reminder', ['Early-batch seats', 'or start date', 'reminder'], logo_whatsapp),
        ('Day 6', 'Follow up', ['Reply to every', 'DM and comment', 'personally'], logo_instagram),
        ('Day 7', 'Batch starts', ['Welcome note', 'and the first', 'live class'], None)]
for k, (d, t, items, lg) in enumerate(days):
    x = 60 + k * 158
    b += f'<circle cx="{x + 70}" cy="220" r="11" fill="{BLUE}" stroke="#fff" stroke-width="4"/>'
    b += white_panel(x, 260, 142, 380, 22)
    b += eyebrow(x + 18, 302, d)
    b += text(x + 18, 342, t, 22 if len(t) < 9 else 19, INK, 800, font=F_HEAD, ls=-0.6)
    b += lines(x + 18, 392, items, 15, MUTED, 1.5)
    if lg:
        b += logo_tile(x + 18, 550, lg, 60)
    else:
        b += tile(x + 18, 550, 'calendar', 60, BLUE)
b += text(60, 720, 'Your warm audience: past students, WhatsApp groups, YouTube subscribers, Instagram followers.', 19, INK, 600)
b += text(60, H - 28, 'Illustrative plan. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('launch-week-plan', svg(W, H, b, 'Seven-day launch week plan to sell an online course to your warm audience on WhatsApp, YouTube and Instagram'))

# 8. where to sell -------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Where to sell: *three honest options*'], 50)
cols = ['Social only', 'Marketplace', 'Own academy']
rows = [('Your brand and domain', ['no', 'no', 'yes']),
        ('Checkout and auto access', ['no', 'yes', 'yes']),
        ('You set the price', ['yes', 'part', 'yes']),
        ('Student data you keep', ['part', 'no', 'yes']),
        ('Your own app', ['no', 'no', 'yes']),
        ('Built-in buyers', ['no', 'yes', 'no']),
        ('Setup effort', ['yes', 'part', 'part'])]
b += white_panel(60, 160, 1100, 680, 28, big=True)
lx, cx0, cw = 92, 520, 200
for k, c in enumerate(cols):
    x = cx0 + k * cw + cw / 2
    hl = k == 2
    if hl:
        b += f'<rect x="{cx0 + k * cw + 10}" y="176" width="{cw - 20}" height="648" rx="20" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2"/>'
    b += text(x, 240, c, 21, BLUE if hl else INK, 700, 'middle', F_HEAD)
for r, (lab, vals) in enumerate(rows):
    y = 320 + r * 76
    b += f'<line x1="{lx}" y1="{y - 40}" x2="1130" y2="{y - 40}" stroke="{LINE}" stroke-width="2"/>'
    b += text(lx, y + 6, lab, 21, INK, 600)
    for k, v in enumerate(vals):
        x = cx0 + k * cw + cw / 2
        if r == 6:
            lab2 = {'yes': 'Low', 'part': 'Medium'}[v]
            b += text(x, y + 7, lab2, 19, INK, 600, 'middle')
            continue
        if v == 'yes':
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="{BLUE}"/>' + icon('tick', x - 10, y - 10, 20, '#fff', 2.8)
        elif v == 'no':
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="#ECEDF2"/>' + icon('x', x - 8, y - 8, 16, '#9AA0AE', 2.6)
        else:
            b += f'<circle cx="{x}" cy="{y}" r="17" fill="#fff" stroke="{BLUE}" stroke-width="2.5"/><path d="M{x} {y - 15} A15 15 0 0 1 {x} {y + 15} Z" fill="{BLUE}"/>'
b += f'<circle cx="76" cy="{H - 34}" r="9" fill="{BLUE}"/>' + text(92, H - 28, 'Yes', 16, MUTED)
b += f'<circle cx="150" cy="{H - 34}" r="9" fill="#fff" stroke="{BLUE}" stroke-width="2"/><path d="M150 {H - 43} A9 9 0 0 1 150 {H - 25} Z" fill="{BLUE}"/>' + text(166, H - 28, 'Partly', 16, MUTED)
b += f'<circle cx="240" cy="{H - 34}" r="9" fill="#ECEDF2"/>' + text(256, H - 28, 'Usually not  ·  Typical setups; platforms vary.', 16, MUTED)
b += signature(W, H)
save('where-to-sell-comparison', svg(W, H, b, 'Where to sell online courses in India: social media only, a marketplace or your own academy, compared'))

# 9. after the first sale -------------------------------------------------------------
W, H = 1220, 880
b = headline(60, 100, ['After the first sale: *the loop*'], 52)
b += lines(62, 150, ['Your first students help you find the next ones.'], 22)
cx, cy = 610, 520
b += f'<circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="4 10"/>'
b += f'<circle cx="{cx}" cy="{cy}" r="110" fill="{BLUE}" filter="url(#shB)"/>'
b += text(cx, cy - 6, 'Happy', 28, '#fff', 800, 'middle', F_HEAD) + text(cx, cy + 28, 'students', 28, '#fff', 800, 'middle', F_HEAD)
loop = [(cx, cy - 250, 'Ask for reviews', 'Two lines + result', 'star'),
        (cx + 290, cy - 40, 'Word of mouth', 'They tell friends', 'message'),
        (cx + 175, cy + 250, 'Use their doubts', 'Next course outline', 'list'),
        (cx - 175, cy + 250, 'Open batch 2', 'Same page, new date', 'calendar'),
        (cx - 290, cy - 40, 'Better course page', 'Reviews + FAQ added', 'globe')]
for x, y, t, s, ic in loop:
    w = 300
    b += pill_card(x - w / 2, y - 48, w, t, s, ic, tile=NAVY_TILE, title_size=22)
b += text(60, H - 28, 'Concept diagram.', 16, MUTED)
b += signature(W, H)
save('after-first-sale-loop', svg(W, H, b, 'After the first course sale: reviews, word of mouth, student doubts, batch two and a better course page'))

# 10. mistakes --------------------------------------------------------------------------
W, H = 1220, 940
b = headline(56, 110, ['Stuck before', 'the first sale?'], 58)
for i, t in enumerate(['60 lessons, no buyers yet', 'Course for everyone', 'Pay on WhatsApp QR', 'Drive link gets shared', 'Ads before any sale']):
    b += tape(40 + (i % 2) * 22, 250 + i * 104, 510, t, -1.4 if i % 2 else 1.0, 30)
b += hand(330, 820, ['Still no', 'sale?'], 40, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Ship a minimum course', 'One exam, one language', 'UPI checkout on your page', 'Access only after payment', 'Warm audience first']):
    b += check_row(656, 400 + i * 74, t, 25)
b += button(650, 790, 500, 'Start your academy', 84, 32)
save('first-sale-mistakes', svg(W, H, b, 'Mistakes that stop educators from making their first online course sale, and what to do instead', ('split', 600)))

# 11. promo --------------------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 230, ['Sell your', 'course on your', '*own academy.*'], 58)
b += lines(64, 430, ['Sign up, choose a plan, upload your', 'course, connect your domain,', 'start selling.'], 24, MUTED, 1.4)
b += laptop(600, 130, 500, 'studio-desktop.jpg')
b += phone(1030, 230, 160, 'studio-mobile.jpg')
for k, (lab, ic, sub) in enumerate([('Own domain', 'globe', 'Every plan'), ('UPI checkout', 'card', 'Razorpay'), ('Live classes', 'video', 'Unlimited'),
                                     ('Meta Pixel', 'chart', 'Plus GTM'), ('Your app', 'phone', 'iOS on Pro, Scale')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, 'Plans from ₹6,999/year + GST', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '14 days free · no card needed', 21, MUTED)
b += text(600, 112, 'AllCoaching Studio preview · sample data', 14, MUTED)
save('sell-on-your-academy', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own domain, UPI checkout, unlimited live classes, Meta Pixel and your own app'))
