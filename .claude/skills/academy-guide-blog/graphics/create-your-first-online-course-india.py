"""Graphics for /blog/create-your-first-online-course-india.

Run:  python .claude/skills/academy-guide-blog/graphics/create-your-first-online-course-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/create-your-first-online-course-india
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'create-your-first-online-course-india')
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
b += headline(80, 300, ['Create your', '*first online*', '*course.*'], 88)
b += lines(84, 560, ['Videos, PDF notes and tests in one place.'], 30, MUTED)
for i, (t, ic) in enumerate([('Plan modules and lessons', 'list'), ('Record on a phone budget', 'mic'),
                             ('Add notes, tests and live classes', 'layers'), ('Pilot with 5–10 students', 'users')]):
    b += f'<circle cx="100" cy="{622 + i * 56}" r="17" fill="{BLUE}"/>' + icon('tick', 90, 612 + i * 56, 20, '#fff', 2.8)
    b += text(130, 630 + i * 56, t, 25, INK, 600, font=F_HEAD, ls=-0.4)
b += text(880, 196, 'Studio preview · sample data', 15, MUTED)
b += laptop(880, 210, 580, 'studio-courses.jpg')
b += phone(1380, 360, 150, 'studio-mobile.jpg')
b += pill_card(800, 660, 440, 'NEET Biology · Hindi', '4 modules · videos, PDFs, tests', 'play', title_size=26)
save('cover', svg(1600, 900, b, 'How to create your first online course in India: plan modules and lessons, record on a budget, add PDF notes, tests and live classes'))

# 2. course structure tree -------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['Structure it like a *syllabus*'], 54)
b += lines(62, 150, ['Course → modules → lessons. Every module ends in notes and a test.'], 22)
b += f'<g filter="url(#shB)"><rect x="380" y="196" width="460" height="100" rx="26" fill="{BLUE}"/></g>'
b += text(610, 240, 'NEET Biology · Hindi medium', 27, '#fff', 800, 'middle', F_HEAD, -0.6)
b += text(610, 274, 'One course, one outcome, one price', 18, '#DCE2FF', anchor='middle')
mods = [('Module 1', 'Cell biology', ['Lesson 1 · free', 'Lessons 2–8', 'PDF notes', 'Module test']),
        ('Module 2', 'Plant physiology', ['Lessons 1–9', '12–15 min each', 'PDF + diagrams', 'Module test']),
        ('Module 3', 'Human physiology', ['Lessons 1–12', '10–14 min each', 'PDF + PYQs', 'Module test']),
        ('Module 4', 'Revision', ['Full mock tests', 'Video solutions', 'Live doubt class', 'Formula PDF'])]
icons = [['star', 'play', 'file', 'check'], ['play', 'calendar', 'file', 'check'], ['play', 'calendar', 'file', 'check'],
         ['check', 'play', 'video', 'file']]
for i, (e_, t, items) in enumerate(mods):
    x = 60 + i * 280
    b += f'<path d="M610 296 V 336 H {x + 130} V 372" fill="none" stroke="{BLUE}" stroke-width="2.5"/>'
    b += white_panel(x, 372, 260, 410, 24)
    b += eyebrow(x + 26, 416, e_)
    b += text(x + 26, 456, t, 23, INK, 800, font=F_HEAD, ls=-0.6)
    for k, it in enumerate(items):
        y = 488 + k * 70
        b += f'<rect x="{x + 26}" y="{y}" width="44" height="44" rx="12" fill="{BLUE if (i == 0 and k == 0) else BLUE_TINT}"/>'
        b += icon(icons[i][k], x + 36, y + 10, 24, '#fff' if (i == 0 and k == 0) else BLUE, 2)
        b += text(x + 82, y + 29, it, 18, INK, 500)
b += white_panel(60, 820, 1100, 120, 24)
b += tile(88, 850, 'list')
b += text(172, 876, 'Lessons of 5–15 minutes, one idea each', 25, INK, 800, font=F_HEAD, ls=-0.6)
b += text(172, 910, 'Short lessons are easier to watch on a phone and easier to update later.', 19, MUTED)
b += text(60, H - 28, 'Example structure, illustrative.', 16, MUTED)
b += signature(W, H)
save('course-structure', svg(W, H, b, 'Online course structure: one course split into modules, each with short video lessons, PDF notes and a module test, plus a free demo lesson'))

# 3. formats grid ------------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Four formats, *one course*'], 54)
b += lines(62, 150, ['What each format does for the student.'], 22)
fm = [('Video lessons', 'Teach the concept', ['Recorded once, watched often', 'Via YouTube, unlisted', '5–15 minutes each'], 'play'),
      ('PDF notes', 'Revise without the video', ['Chapter notes, diagrams', 'Formula sheets, PYQs', 'One PDF per module'], 'file'),
      ('Tests', 'Check what stuck', ['Chapter quizzes', 'Timed mock tests', 'Answers with solutions'], 'check'),
      ('Live classes', 'Answer doubts', ['Weekly doubt session', 'Revision marathon', 'YouTube Live, Zoom, built-in'], 'video')]
for i, (t, s, items, ic) in enumerate(fm):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 330
    b += white_panel(x, y, 540, 300, 26)
    b += tile(x + 30, y + 30, ic, 68)
    b += text(x + 120, y + 64, t, 30, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(x + 120, y + 94, s, 19, BLUE, 600)
    for k, it in enumerate(items):
        b += check_row(x + 32, y + 158 + k * 46, it, 20)
b += logo_tile(60, 860, logo_youtube, 64)
b += text(142, 890, 'Videos via YouTube are unlimited on every AllCoaching plan.', 20, INK, 600)
b += text(142, 918, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('formats', svg(W, H, b, 'The four formats of an online course: video lessons via YouTube, PDF notes, tests and live classes, and what each does for the student'))

# 4. budget recording kit -------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['A recording kit on a *phone budget*'], 50)
b += lines(62, 150, ['You need clear sound and a steady frame, not a studio.'], 22)
kit = [('Your smartphone', 'The one you already own', 'Already yours', 'phone'),
       ('Lapel (clip-on) mic', 'The biggest jump in quality', '₹500–₹2,000', 'mic'),
       ('Tripod or phone stand', 'Steady, eye-level frame', '₹400–₹1,500', 'pin'),
       ('Ring light or soft lamp', 'Even light on your face', '₹800–₹2,500', 'sparkle'),
       ('Screen recorder', 'For slides and problems', 'Free (OBS Studio)', 'server'),
       ('Writing pad or tablet', 'For maths and diagrams', '₹3,000–₹15,000', 'type')]
for i, (t, s, p, ic) in enumerate(kit):
    x = 60 + (i % 2) * 560
    y = 196 + (i // 2) * 172
    b += white_panel(x, y, 540, 148, 26)
    b += tile(x + 26, y + 26, ic, 64, i % 3 == 0)
    b += text(x + 112, y + 56, t, 26, INK, 800, font=F_HEAD, ls=-0.7)
    b += text(x + 112, y + 88, s, 19, MUTED)
    b += f'<rect x="{x + 112}" y="{y + 104}" width="{len(p) * 11 + 34}" height="32" rx="16" fill="{BLUE_TINT}"/>'
    b += text(x + 129, y + 126, p, 17, BLUE, 700, font=F_HEAD)
b += '<rect x="618" y="194" width="544" height="152" rx="28" fill="none" stroke="#2B44FF" stroke-width="3"/>'
b += hand(700, 770, ['Start with the mic.', 'Buy the rest later.'], 38, INK, -4)
b += text(60, 860, 'Price ranges are illustrative (India, October 2026) and vary by model and seller.', 17, MUTED)
b += text(60, 888, 'A writing tablet is optional; a phone over a notebook works too.', 17, MUTED)
b += signature(W, H)
save('recording-kit', svg(W, H, b, 'Budget recording kit for an online course in India: phone, lapel mic, tripod, ring light, free screen recorder and a writing pad, with illustrative price ranges'))

# 5. lesson anatomy ------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Anatomy of a *12-minute* lesson'], 52)
b += lines(62, 150, ['Example: SSC maths, "Percentage shortcuts" (illustrative)'], 22)
parts = [('Hook', '0:00', 'One exam question\nthey cannot yet solve', 1),
         ('Teach', '0:45', 'One idea, shown\nstep by step', 4),
         ('Examples', '5:00', 'Two solved questions,\neasy then exam-level', 3.5),
         ('Practice', '9:00', 'Pause and try one\nyourself', 2),
         ('Recap', '11:00', 'Three lines + what\ncomes next', 1.5)]
total = sum(p[3] for p in parts)
x = 60
cols = [NAVY_TILE, BLUE, '#4B63FF', '#8C9CFF', '#C3CCFF']
for i, (t, at, d, wgt) in enumerate(parts):
    w = 1100 * wgt / total
    b += f'<rect x="{x}" y="220" width="{w - 6}" height="70" rx="14" fill="{cols[i]}"/>'
    b += text(x + 16, 264, t, 22 if w > 120 else 18, '#fff' if i < 3 else INK, 800, font=F_HEAD, ls=-0.4)
    x += w
for i, (t, at, d, wgt) in enumerate(parts):
    y = 340 + i * 96
    b += white_panel(60, y, 1100, 80, 20)
    b += f'<rect x="84" y="{y + 20}" width="96" height="40" rx="20" fill="{BLUE_TINT}"/>' + text(132, y + 47, at, 18, BLUE, 700, 'middle', F_MONO)
    b += text(204, y + 50, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(400, y + 50, d.replace('\n', ' '), 20, MUTED)
b += text(60, H - 28, 'Timings are a guide. Keep each lesson to one idea.', 16, MUTED)
b += signature(W, H)
save('lesson-anatomy', svg(W, H, b, 'Anatomy of a short online course video lesson: hook, teach one idea, solved examples, practice and recap, with illustrative timings'))

# 6. workflow: record to upload ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['From recording to *your course*'], 54)
b += lines(62, 150, ['Five steps per lesson. Batch them by module.'], 22)
flow = [('Script', 'Bullet outline', 'list'), ('Record', 'Phone + mic', 'mic'), ('Edit', 'Trim, no effects', 'layers'),
        ('Upload', 'YouTube, unlisted', 'play'), ('Add', 'Course in studio', 'book')]
for i, (t, s, ic) in enumerate(flow):
    x = 60 + i * 222
    b += white_panel(x, 200, 200, 200, 24)
    b += num_badge(x + 36, 236, i + 1, 18)
    b += tile(x + 66, 254, ic, 68, i != 3)
    b += text(x + 100, 360, t, 25, INK, 800, 'middle', F_HEAD, -0.6)
    b += text(x + 100, 388, s, 16, MUTED, anchor='middle')
    if i < 4:
        b += arrow(f'M{x + 203} 300 H {x + 218}', BLUE, 3)
b += logo_tile(726 + 138, 216, logo_youtube, 44)
b += text(90, 462, 'Studio preview · sample data', 15, MUTED)
b += laptop(100, 478, 640, 'studio-courses.jpg')
b += white_panel(800, 470, 360, 380, 26)
b += eyebrow(830, 516, 'In the studio')
for i, t in enumerate(['Create the course', 'Add videos in order', 'Attach PDF notes', 'Add module tests', 'Mark lesson 1 free', 'Publish after a pilot']):
    b += check_row(830, 572 + i * 48, t, 20)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('workflow', svg(W, H, b, 'Online course workflow: script, record, edit, upload to YouTube as unlisted and add the lesson to a course in the AllCoaching studio'))

# 7. language and captions ------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Teach in *their language*'], 56)
b += lines(62, 150, ['Choose the medium students search in, then caption it.'], 22)
langs = [('Hindi', 'NEET, SSC, state exams', 'हिंदी'), ('Hinglish', 'Spoken English, banking', 'Hinglish'),
         ('Regional', 'State PSC, TET, boards', 'मराठी · தமிழ்'), ('English', 'CAT, CLAT, coding, global', 'English')]
for i, (t, s, scr) in enumerate(langs):
    x = 60 + i * 280
    b += white_panel(x, 196, 260, 210, 24)
    b += text(x + 26, 262, scr, 30, BLUE, 700, font=F_HEAD)
    b += text(x + 26, 318, t, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += lines(x + 26, 352, [s], 16, MUTED)
b += white_panel(60, 450, 1100, 360, 28)
b += logo_tile(92, 482, logo_youtube, 64)
b += text(176, 512, 'Captions with YouTube automatic captions', 26, INK, 800, font=F_HEAD, ls=-0.6)
b += text(176, 544, 'Hindi is among the supported languages.', 19, MUTED)
steps = [('Upload', 'Lesson as unlisted'), ('Wait', 'Captions generate'), ('Review', 'Fix names, terms'), ('Publish', 'Students can read along')]
for i, (t, s) in enumerate(steps):
    x = 92 + i * 262
    b += num_badge(x + 22, 630, i + 1, 20)
    b += text(x + 54, 638, t, 23, INK, 800, font=F_HEAD, ls=-0.5)
    b += text(x + 54, 670, s, 17, MUTED)
    if i < 3:
        b += arrow(f'M{x + 210} 630 H {x + 244}', BLUE, 3)
b += f'<rect x="92" y="716" width="1036" height="60" rx="16" fill="{BLUE_TINT}"/>'
b += text(116, 754, 'Always review automatic captions: exam terms and names are often misheard.', 19, INK, 600)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('language-captions', svg(W, H, b, 'Choosing Hindi, Hinglish, regional or English medium for an online course and adding YouTube automatic captions, then reviewing them'))

# 8. demo lesson funnel -------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['The *free demo lesson* does the selling'], 50)
b += lines(62, 150, ['Example path for a spoken English course (illustrative).'], 22)
stages = [('Public YouTube video', 'A useful 8-minute lesson', 1100, logo_youtube),
          ('Free demo lesson', 'Lesson 1 of the course, on your academy', 900, None),
          ('Course page', 'Syllabus, formats, price', 700, None),
          ('Enrolled student', 'UPI or card checkout', 500, None)]
for i, (t, s, w, lg) in enumerate(stages):
    x = 60 + (1100 - w) / 2
    y = 200 + i * 150
    fill = BLUE if i == 3 else '#fff'
    b += f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="120" rx="28" fill="{fill}"/></g>'
    tc, sc = ('#fff', '#DCE2FF') if i == 3 else (INK, MUTED)
    tx = x + (110 if lg else 40)
    if lg:
        b += logo_tile(x + 26, y + 26, lg, 68)
    else:
        b += tile(x + 30, y + 30, ['star', 'book', 'users'][i - 1], 60, i != 3)
        tx = x + 112
    b += text(tx, y + 54, t, 28, tc, 800, font=F_HEAD, ls=-0.8)
    b += text(tx, y + 88, s, 19, sc)
b += hand(980, 640, ['Teach one thing', 'fully. Do not tease.'], 32, INK, -5)
b += arrow('M960 650 C 900 660, 880 520, 900 480', BLUE, 3)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('demo-funnel', svg(W, H, b, 'How a free demo lesson sells an online course: public YouTube lesson, free demo lesson in the academy, course page, then UPI checkout'))

# 9. pilot checklist ----------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['Pilot with *5–10 students* first'], 54)
b += lines(62, 150, ['A small free or discounted batch finds the problems before buyers do.'], 22)
b += white_panel(60, 200, 540, 640, 28)
b += eyebrow(92, 252, 'What you ask them to do')
for i, t in enumerate(['Watch on their own phone', 'Finish module 1 in a week', 'Download every PDF', 'Take the module test', 'Join one live doubt class', 'Tell you where they got stuck']):
    b += check_row(92, 314 + i * 86, t, 21)
b += white_panel(620, 200, 540, 640, 28)
b += eyebrow(652, 252, 'What you check')
for i, (t, s) in enumerate([('Audio', 'Clear on cheap earphones?'), ('Length', 'Did they skip ahead?'), ('Order', 'Any lesson out of place?'),
                            ('Tests', 'Too easy, too hard, typos?'), ('Notes', 'Readable on a small screen?'), ('Questions', 'What did 3+ people ask?')]):
    y = 290 + i * 86
    b += f'<rect x="652" y="{y}" width="40" height="40" rx="12" fill="{BLUE_TINT}"/>' + icon('search', 660, y + 8, 24, BLUE, 2)
    b += text(708, y + 18, t, 21, INK, 800, font=F_HEAD, ls=-0.4)
    b += text(708, y + 42, s, 17, MUTED)
b += text(60, H - 50, 'Fix the top three issues, then launch to everyone.', 18, INK, 600)
b += signature(W, H)
save('pilot-checklist', svg(W, H, b, 'Pilot test checklist for a new online course: what 5 to 10 pilot students do and what the educator checks before launch'))

# 10. mistakes ------------------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Six first-course *mistakes*'], 54)
mist = [('90-minute lectures', 'Cut into 5–15 min lessons'),
        ('Buying gear first', 'Buy a mic, use your phone'),
        ('Reading the script', 'Speak from bullet points'),
        ('Over-editing', 'Trim mistakes, ship it'),
        ('Videos only', 'Add PDF notes and tests'),
        ('Launching untested', 'Pilot with 5–10 students')]
for i, (t, fix) in enumerate(mist):
    y = 170 + i * 118
    b += tape(50 + (i % 2) * 18, y, 520, t, -1.2 if i % 2 else 0.9, 30)
    b += arrow(f'M600 {y + 36} H 660', BLUE, 3)
    b += white_panel(680, y + 2, 480, 70, 20)
    b += f'<circle cx="716" cy="{y + 37}" r="16" fill="{BLUE}"/>' + icon('tick', 706, y + 27, 20, '#fff', 2.8)
    b += text(746, y + 45, fix, 22, INK, 600, font=F_HEAD, ls=-0.4)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Six common mistakes when creating a first online course and the fix for each', ('split', 640)))
