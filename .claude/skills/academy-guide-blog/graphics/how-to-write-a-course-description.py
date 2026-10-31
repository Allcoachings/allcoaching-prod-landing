"""Graphics for /blog/how-to-write-a-course-description.

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-write-a-course-description.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-write-a-course-description
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'how-to-write-a-course-description')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def browser(ox, oy, w, h, url):
    """White browser window with traffic lights and an address bar."""
    b = white_panel(ox, oy, w, h, 26, big=True)
    b += f'<rect x="{ox}" y="{oy}" width="{w}" height="58" rx="26" fill="#F1F3F6"/><rect x="{ox}" y="{oy + 30}" width="{w}" height="28" fill="#F1F3F6"/>'
    b += ''.join(f'<circle cx="{ox + 30 + k * 22}" cy="{oy + 29}" r="7" fill="{c}"/>' for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']))
    b += f'<rect x="{ox + 100}" y="{oy + 13}" width="{w - 150}" height="32" rx="16" fill="#fff"/>' + text(ox + 120, oy + 35, url, 16, INK)
    return b


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 320, ['Write a course', 'description', '*that sells.*'], 80)
b += lines(84, 580, ['For exam and skill educators in India.'], 28, MUTED)
b += check_row(84, 650, 'An outcome-first title', 26)
b += check_row(84, 706, 'What is inside, in numbers', 26)
b += check_row(84, 762, 'Real proof, honest price', 26)
ox, oy = 860, 120
b += browser(ox, oy, 680, 660, 'youracademy.in/neet-biology-droppers')
px = ox + 40
b += eyebrow(px, oy + 108, 'NEET · Hindi medium')
b += text(px, oy + 152, 'NEET Biology for Droppers:', 32, INK, 800, font=F_HEAD, ls=-1.2)
b += text(px, oy + 192, 'NCERT in 120 Days', 32, BLUE, 800, font=F_HEAD, ls=-1.2)
b += text(px, oy + 232, 'For Class 12 droppers retaking NEET next year.', 18, MUTED)
for k, (ic, t) in enumerate([('play', '180 video lessons'), ('file', '38 chapter PDFs'), ('check', '25 tests + 10 mocks'), ('video', 'Weekly live doubt class')]):
    x = px + (k % 2) * 300
    y = oy + 270 + (k // 2) * 70
    b += f'<rect x="{x}" y="{y}" width="284" height="56" rx="14" fill="#F4F6FF"/>' + icon(ic, x + 16, y + 16, 24, BLUE, 2) + text(x + 52, y + 35, t, 18, INK, 600)
b += f'<rect x="{px}" y="{oy + 430}" width="600" height="110" rx="16" fill="{BLUE_TINT}"/>'
b += text(px + 24, oy + 474, 'Watch lesson 1 free', 20, INK, 700, font=F_HEAD) + text(px + 24, oy + 506, 'before you pay', 18, MUTED)
b += f'<rect x="{px + 380}" y="{oy + 456}" width="200" height="58" rx="18" fill="{BLUE}"/>' + text(px + 480, oy + 493, 'Enrol · ₹2,999', 19, '#fff', 700, 'middle', F_HEAD)
b += text(px, oy + 600, 'Illustrative course page · youracademy.in is an example', 15, MUTED)
save('cover', svg(1600, 900, b, 'How to write a course description that sells: outcome-first title, what is inside in numbers, real proof and an honest price'))

# 2. before / after ------------------------------------------------------------
W, H = 1220, 980
b = eyebrow(56, 84, 'Before', RED) + headline(56, 146, ['Weak description'], 46)
b += white_panel(56, 200, 500, 420, 24)
b += text(86, 258, 'Biology Course', 30, INK, 800, font=F_HEAD, ls=-1)
b += lines(86, 312, ['Best biology course by an', 'experienced teacher. Learn all', 'topics in an easy way. Join now', 'and get success.'], 21, MUTED, 1.5)
b += text(86, 500, 'Price: ₹2,999', 22, INK, 600)
b += f'<rect x="86" y="530" width="180" height="52" rx="16" fill="#9AA0AE"/>' + text(176, 563, 'Buy now', 19, '#fff', 700, 'middle', F_HEAD)
for i, t in enumerate(['Who is it for?', 'What is inside?', 'Why trust you?']):
    b += tape(70 + (i % 2) * 24, 660 + i * 84, 420, t, -1.2 if i % 2 else 1.0, 30)
b += eyebrow(666, 84, 'After', BLUE) + headline(666, 146, ['Strong *description*'], 46)
b += white_panel(666, 200, 500, 680, 24)
b += text(696, 254, 'NEET Biology for Droppers:', 26, INK, 800, font=F_HEAD, ls=-0.9)
b += text(696, 288, 'NCERT in 120 Days (Hindi)', 26, BLUE, 800, font=F_HEAD, ls=-0.9)
b += lines(696, 334, ['For Class 12 droppers retaking NEET', 'next year who want NCERT Biology', 'finished and revised on time.'], 19, MUTED, 1.45)
for i, t in enumerate(['180 video lessons, 8–20 min each', '38 chapter PDFs with NCERT lines', '25 chapter tests + 10 full mocks', 'All-India rank and percentile', 'Weekly live doubt class', 'Lesson 1 free before you pay']):
    b += check_row(696, 460 + i * 52, t, 19)
b += text(696, 800, '₹2,999 + GST · valid till exam day', 20, INK, 700, font=F_HEAD)
b += f'<rect x="696" y="822" width="200" height="44" rx="14" fill="{BLUE}"/>' + text(796, 851, 'Enrol now', 18, '#fff', 700, 'middle', F_HEAD)
b += text(56, H - 28, 'Illustrative example. Course, numbers and price are not real data.', 16, MUTED) + signature(W, H)
save('before-after', svg(W, H, b, 'Weak versus strong course description for a NEET biology course', ('split', 610)))

# 3. course page anatomy -----------------------------------------------------------
W, H = 1220, 1160
b = headline(60, 96, ['Anatomy of a course page *that sells*'], 50)
ox, oy = 60, 150
b += browser(ox, oy, 690, 920, 'youracademy.in/spoken-english-interviews')
px = ox + 40
b += text(px, oy + 120, 'Spoken English for Job Interviews', 30, INK, 800, font=F_HEAD, ls=-1.1)
b += text(px, oy + 156, 'For freshers who freeze in English interviews.', 17, MUTED)
b += f'<rect x="{px}" y="{oy + 180}" width="380" height="200" rx="14" fill="{NAVY_TILE}"/><circle cx="{px + 190}" cy="{oy + 280}" r="32" fill="#fff"/><path d="M{px + 181} {oy + 265} L{px + 205} {oy + 280} L{px + 181} {oy + 295}Z" fill="{NAVY_TILE}"/>'
b += text(px + 18, oy + 364, 'Free lesson: Tell me about yourself', 15, '#fff', opacity=.85)
b += f'<rect x="{px + 400}" y="{oy + 180}" width="210" height="200" rx="14" fill="#F4F6FF"/>' + text(px + 420, oy + 222, '30-day course', 16, MUTED) + text(px + 420, oy + 264, '₹1,499', 34, INK, 800, font=F_HEAD)
b += text(px + 420, oy + 290, '+ GST', 15, MUTED)
b += f'<rect x="{px + 420}" y="{oy + 312}" width="170" height="46" rx="16" fill="{BLUE}"/>' + text(px + 505, oy + 342, 'Enrol now', 17, '#fff', 700, 'middle', F_HEAD)
b += text(px, oy + 430, 'After 30 days you will be able to', 20, INK, 700, font=F_HEAD)
b += lines(px, oy + 462, ['✓  Answer 25 common interview questions', '✓  Speak for 2 minutes without notes'], 16, MUTED, 1.6)
b += text(px, oy + 540, 'Inside the course', 20, INK, 700, font=F_HEAD)
for k, t in enumerate(['30 video lessons · 30 speaking tasks · 4 PDFs', '8 live practice classes on Zoom · Hinglish']):
    b += f'<rect x="{px}" y="{oy + 558 + k * 46}" width="610" height="38" rx="10" fill="#F4F6FF"/>' + text(px + 16, oy + 583 + k * 46, t, 15, INK)
b += text(px, oy + 692, 'About your teacher', 20, INK, 700, font=F_HEAD) + text(px, oy + 722, '9 years teaching English to job seekers in Indore.', 16, MUTED)
b += text(px, oy + 778, 'Questions students ask', 20, INK, 700, font=F_HEAD)
for k, t in enumerate(['I am a complete beginner. Can I join?', 'What if I miss a live class?']):
    b += f'<rect x="{px}" y="{oy + 796 + k * 46}" width="610" height="38" rx="10" fill="#fff" stroke="{LINE}"/>' + text(px + 16, oy + 821 + k * 46, t, 15, INK)
callouts = [(oy + 112, oy + 100, 'Outcome-first title', 'skill + result + who', 690),
            (oy + 152, oy + 195, 'Who it is for', 'one line, their words', 520),
            (oy + 335, oy + 300, 'Price, one button', 'GST stated, no tricks', 690),
            (oy + 394, oy + 400, 'Free sample lesson', 'proof before payment', px + 190),
            (oy + 452, oy + 495, 'Outcomes', 'what they can do after', 540),
            (oy + 580, oy + 600, 'What is inside', 'in numbers, not adjectives', 690),
            (oy + 712, oy + 712, 'Real proof', 'your record, real feedback', 560),
            (oy + 820, oy + 830, 'FAQ on the page', 'answers before they ask', 690)]
for n, (ty, ly, t, s, lx) in enumerate(callouts, 1):
    b += f'<circle cx="{lx}" cy="{ty}" r="5" fill="{BLUE}"/><path d="M{lx} {ty} H 766 V {ly} H 790" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(812, ly, n) + text(846, ly - 2, t, 21, INK, 700, font=F_HEAD, ls=-0.4) + text(846, ly + 24, s, 17, MUTED)
b += text(60, H - 28, 'Illustrative course page. Price, numbers and details are examples, not real data.', 16, MUTED) + signature(W, H)
save('course-page-anatomy', svg(W, H, b, 'Anatomy of a course page that sells, with eight numbered parts'))

# 4. title formula --------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['The *course title* formula'], 52) + lines(62, 150, ['Outcome + exam or skill + who + format = a title students click'], 22)
parts = [('Outcome', 'trophy', ['Crack', 'Finish', 'Speak', 'Run']),
         ('Exam or skill', 'book', ['SSC CGL Quant', 'NEET Biology', 'English', 'Meta ads']),
         ('Who', 'users', ['for beginners', 'for droppers', 'for freshers', 'for shop owners']),
         ('Format', 'calendar', ['90-day course', 'in 120 days', '30 days, Hinglish', 'hands-on'])]
for k, (h, ic, items) in enumerate(parts):
    x = 60 + k * 280
    b += white_panel(x, 200, 250, 310, 24)
    b += f'<rect x="{x + 22}" y="222" width="52" height="52" rx="14" fill="{BLUE_TINT if k else NAVY_TILE}"/>' + icon(ic, x + 34, 234, 28, '#fff' if k == 0 else BLUE, 2)
    b += eyebrow(x + 22, 310, h)
    b += lines(x + 22, 352, items, 21, INK, 1.6)
    if k < 3:
        b += text(x + 265, 370, '+', 40, INK, 300, 'middle')
b += white_panel(60, 560, 1100, 300, 28)
b += eyebrow(92, 608, 'Example titles (illustrative)')
ex = ['Crack SSC CGL Quant: 90-Day Course in Hindi', 'NEET Biology for Droppers: NCERT in 120 Days',
      'Spoken English for Interviews: 30 Days, Hinglish', 'Meta Ads for Local Shops: Hands-on Course',
      'Yoga for Back Pain: 21-Day Beginner Programme', 'UPSC Prelims Test Series 2027 in Hindi']
for i, p in enumerate(ex):
    x = 92 + (i % 2) * 530
    y = 632 + (i // 2) * 70
    hl = i == 1
    stroke = f' stroke="{BLUE}" stroke-width="2"' if hl else ''
    b += f'<rect x="{x}" y="{y}" width="506" height="54" rx="27" fill="{BLUE_TINT if hl else "#F3F4F8"}"{stroke}/>'
    b += text(x + 24, y + 35, p, 19, BLUE if hl else INK, 600)
b += signature(W, H)
save('title-formula', svg(W, H, b, 'Course title formula: outcome plus exam or skill plus who it is for plus format, with example titles'))

# 5. what's inside ---------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 96, ['Say what is inside *in numbers*'], 52) + lines(62, 146, ['Students compare courses by what they get. Count it for them.'], 22)
cards = [('play', 'Video lessons', '120 lessons, 8–20 min'), ('file', 'PDF notes', 'One per chapter'),
         ('check', 'Test series', '20 mocks, all-India rank'), ('video', 'Live classes', 'Weekly doubt class'),
         ('calendar', 'Validity', 'Till exam day or 12 months'), ('message', 'Language', 'Hindi, Hinglish, English')]
for i, (ic, t, s) in enumerate(cards):
    x = 60 + (i % 3) * 375
    y = 190 + (i // 3) * 190
    b += white_panel(x, y, 350, 160, 24)
    b += f'<rect x="{x + 26}" y="{y + 26}" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon(ic, x + 42, y + 42, 28, '#fff', 2)
    b += text(x + 104, y + 58, t, 26, INK, 800, font=F_HEAD, ls=-0.8) + text(x + 26, y + 128, s, 20, MUTED)
b += eyebrow(60, 620, 'Vague  →  specific')
pairs = [('"Complete study material"', '38 chapter PDFs and 500 PYQs'),
         ('"Regular tests"', 'A test after every chapter, 10 full mocks'),
         ('"Full support"', 'Weekly live doubt class till exam day')]
for i, (v, s) in enumerate(pairs):
    y = 648 + i * 80
    b += f'<rect x="60" y="{y}" width="430" height="60" rx="16" fill="#EEEEF2"/>' + text(84, y + 38, v, 20, MUTED, 500)
    b += f'<line x1="84" y1="{y + 31}" x2="{84 + len(v) * 9.6:.0f}" y2="{y + 31}" stroke="{RED}" stroke-width="2"/>'
    b += arrow(f'M510 {y + 30} H 580', BLUE, 4)
    b += f'<rect x="600" y="{y}" width="560" height="60" rx="16" fill="{BLUE_TINT}"/>' + text(624, y + 38, s, 20, INK, 600)
b += text(60, H - 28, 'Illustrative numbers. Count what your own course really contains.', 16, MUTED) + signature(W, H)
save('whats-inside', svg(W, H, b, 'What is inside a course, said in numbers: videos, PDFs, tests, live classes, validity and language'))

# 6. proof: avoid vs use ------------------------------------------------------------
W, H = 1220, 900
b = eyebrow(56, 84, 'Never use', RED) + headline(56, 146, ['Fake proof'], 50)
for i, t in enumerate(['Invented reviews', 'Fake "3 seats left"', 'Guaranteed selection', 'Stock-photo toppers', 'Pass rates with no source']):
    b += check_row(60, 240 + i * 74, t, 24, ok=False)
b += hand(110, 690, ['Students can', 'tell.'], 46, INK, -6) + arrow('M100 700 C 70 660, 70 620, 90 600', INK, 3)
b += eyebrow(666, 84, 'Use instead', BLUE) + headline(666, 146, ['*Real* proof'], 50)
for i, t in enumerate(['A free sample lesson', 'Your years and record', 'Real messages, with consent', 'A clip of a live class', 'Your free YouTube lessons', 'A sample PDF and test']):
    b += check_row(670, 240 + i * 74, t, 24)
b += white_panel(666, 700, 500, 110, 22)
b += icon('message', 692, 726, 30, BLUE, 2) + text(736, 748, 'Ask after each chapter test:', 19, INK, 700)
b += text(736, 778, '"What helped you most so far?"', 19, MUTED)
b += signature(W, H)
save('real-proof', svg(W, H, b, 'Fake proof to avoid in a course description and real proof to use instead', ('split', 610)))

# 7. language ---------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 96, ['Write in the language *you teach in*'], 50)
b += lines(62, 146, ['Title in the words students search. Body in the words they speak.'], 22)
for k, (lab, sub, rows) in enumerate([('English', 'English-medium students', ['Finish NCERT Biology in 120 days,', 'with a test after every chapter.']),
                                      ('Hinglish', 'Hindi-medium, phone-first', ['120 din me poori NCERT Biology,', 'har chapter ke baad test.'])]):
    x = 60 + k * 560
    b += white_panel(x, 200, 540, 280, 26)
    b += eyebrow(x + 32, 250, lab) + text(x + 32, 284, sub, 18, MUTED)
    b += f'<rect x="{x + 32}" y="310" width="476" height="130" rx="16" fill="{BLUE_TINT if k else "#F4F6FF"}"/>'
    b += lines(x + 52, 362, rows, 22, INK, 1.5, weight=600)
b += white_panel(60, 520, 1100, 250, 26)
b += eyebrow(92, 570, 'Keep these in English, in every version')
for i, t in enumerate(['NEET', 'SSC CGL', 'NCERT', 'PDF notes', 'Test series', 'Live class', 'Mock test', 'Syllabus']):
    x = 92 + (i % 4) * 262
    y = 600 + (i // 4) * 74
    b += f'<rect x="{x}" y="{y}" width="236" height="56" rx="28" fill="#F3F4F8"/>' + text(x + 118, y + 36, t, 21, INK, 600, 'middle')
b += text(60, H - 28, 'Illustrative lines. Match the medium of your actual classes.', 16, MUTED) + signature(W, H)
save('language-hinglish', svg(W, H, b, 'Writing a course description in English and Hinglish, keeping exam and product words in English'))

# 8. search preview ---------------------------------------------------------------
W, H = 1220, 840
b = headline(60, 96, ['How your course page *looks on Google*'], 50)
b += white_panel(60, 150, 1100, 320, 30, big=True)
b += search_bar(100, 190, 760, 'neet biology course for droppers hindi', 60)
b += result(122, 300, 980, 'Your Academy', 'youracademy.in › neet-biology-droppers-hindi',
            'NEET Biology for Droppers: NCERT in 120 Days (Hindi)',
            '180 Hindi lessons, 38 chapter PDFs, 25 tests and 10 mocks with all-India rank. Watch lesson 1 free.', True, 26)
items = [('1', 'URL (slug)', 'Short words: exam, subject, who, language', 'link'),
         ('2', 'Title tag', 'About 60 characters, outcome first', 'type'),
         ('3', 'Meta description', 'A unique summary of this page', 'file'),
         ('4', 'Page text', 'Syllabus and FAQ written as text', 'list')]
for i, (n, t, s, ic) in enumerate(items):
    x = 60 + (i % 2) * 560
    y = 520 + (i // 2) * 130
    b += white_panel(x, y, 540, 108, 22)
    b += num_badge(x + 46, y + 54, n) + text(x + 86, y + 48, t, 24, INK, 800, font=F_HEAD, ls=-0.6) + text(x + 86, y + 80, s, 18, MUTED)
b += text(60, H - 28, 'Illustrative result. Google may show a different title or snippet.', 16, MUTED) + signature(W, H)
save('search-preview', svg(W, H, b, 'How a course page appears in Google search: URL, title tag, meta description and page text'))
