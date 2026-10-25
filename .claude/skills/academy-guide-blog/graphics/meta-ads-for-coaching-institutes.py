"""Graphics for /blog/meta-ads-for-coaching-institutes.

Run:  python .claude/skills/academy-guide-blog/graphics/meta-ads-for-coaching-institutes.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/meta-ads-for-coaching-institutes
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa
from brand_graphics import _uid

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'meta-ads-for-coaching-institutes')
os.makedirs(OUT, exist_ok=True)

FB_BLUE = '#0866FF'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def logo_facebook(x, y, size=40):
    """Facebook 'f' mark in its brand blue (nominative use)."""
    s = size / 24
    return (f'<g transform="translate({x} {y}) scale({s:.4f})"><path fill="{FB_BLUE}" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 '
            '1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 '
            '0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 '
            '1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></g>')


def reel_phone(x, y, w, hook=('Percentage in', '2 minute mein'), sub='NEET 2027 · Dropper batch', cta='Learn more'):
    """A drawn phone showing an illustrative Instagram reel ad (not a real ad)."""
    h = w * 2.07
    b = w * 0.045
    r = w * 0.17
    _uid[0] += 1
    cid = f'rp{_uid[0]}'
    ix, iy, iw, ih = x + b, y + b, w - 2 * b, h - 2 * b
    out = (f'<defs><clipPath id="{cid}"><rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="{r - b}"/></clipPath>'
           f'<linearGradient id="{cid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A3170"/><stop offset=".6" stop-color="#1B1E2E"/><stop offset="1" stop-color="#0E1022"/></linearGradient></defs>'
           f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#121317"/></g>'
           f'<g clip-path="url(#{cid})"><rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" fill="url(#{cid}g)"/>'
           # whiteboard + teacher
           f'<rect x="{ix + iw * .1}" y="{iy + ih * .2}" width="{iw * .8}" height="{ih * .26}" rx="10" fill="#F4F6FF" opacity=".95"/>'
           f'<text x="{ix + iw * .15}" y="{iy + ih * .28}" font-family="{F_HAND}" font-size="{w * .075:.0f}" fill="{INK}">20% of 450 = ?</text>'
           f'<text x="{ix + iw * .15}" y="{iy + ih * .36}" font-family="{F_HAND}" font-size="{w * .075:.0f}" fill="{BLUE}">10% = 45, × 2 = 90</text>'
           f'<circle cx="{ix + iw * .5}" cy="{iy + ih * .6}" r="{iw * .1}" fill="#C9A68A"/>'
           f'<path d="M{ix + iw * .24} {iy + ih * .78} q {iw * .26} -{ih * .2} {iw * .52} 0 z" fill="{BLUE}"/>'
           # hook caption
           f'<rect x="{ix + iw * .08}" y="{iy + ih * .06}" width="{iw * .84}" height="{ih * .11}" rx="12" fill="#fff"/>'
           f'<text x="{ix + iw * .5}" y="{iy + ih * .105}" font-family="{F_HEAD}" font-size="{w * .07:.0f}" font-weight="800" fill="{INK}" text-anchor="middle">{esc(hook[0])}</text>'
           f'<text x="{ix + iw * .5}" y="{iy + ih * .15}" font-family="{F_HEAD}" font-size="{w * .07:.0f}" font-weight="800" fill="{BLUE}" text-anchor="middle">{esc(hook[1])}</text>'
           # sponsored row + CTA
           f'<circle cx="{ix + iw * .11}" cy="{iy + ih * .83}" r="{iw * .045}" fill="#fff"/>'
           f'<text x="{ix + iw * .2}" y="{iy + ih * .838}" font-size="{w * .05:.0f}" font-weight="700" fill="#fff">youracademy · Ad</text>'
           f'<text x="{ix + iw * .06}" y="{iy + ih * .878}" font-size="{w * .045:.0f}" fill="#fff" opacity=".8">{esc(sub)}</text>'
           f'<rect x="{ix + iw * .06}" y="{iy + ih * .9}" width="{iw * .88}" height="{ih * .06}" rx="10" fill="#fff" fill-opacity=".18" stroke="#fff" stroke-opacity=".5"/>'
           f'<text x="{ix + iw * .1}" y="{iy + ih * .94}" font-size="{w * .052:.0f}" font-weight="700" fill="#fff">{esc(cta)}</text>'
           f'<text x="{ix + iw * .88}" y="{iy + ih * .94}" font-size="{w * .06:.0f}" font-weight="700" fill="#fff" text-anchor="end">›</text>'
           f'</g>'
           f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{w - 3}" height="{h - 3}" rx="{r - 1}" fill="none" stroke="#4A4D57" stroke-width="2"/>'
           f'<rect x="{x + w * .34}" y="{y + b + w * .035}" width="{w * .32}" height="{w * .085}" rx="{w * .0425}" fill="#000"/>')
    return out


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Meta ads that fill', '*your next batch.*'], 82)
b += lines(84, 470, ['Facebook and Instagram ads for coaching, step by step.'], 28, MUTED)
b += check_row(84, 560, 'Objective, audience, creative', 26)
b += check_row(84, 620, 'Landing page on your own domain', 26)
b += check_row(84, 680, 'Purchases tracked with Meta Pixel', 26)
b += logo_tile(84, 740, logo_facebook, 76) + logo_tile(176, 740, logo_instagram, 76)
b += text(270, 788, 'Logos belong to their owners', 17, MUTED)
b += reel_phone(1010, 90, 330)
b += pill_card(680, 300, 300, 'Sales', 'Campaign objective', 'trophy', tile=BLUE)
b += pill_card(1260, 470, 300, 'Purchase', 'Pixel event received', 'check')
b += pill_card(640, 640, 330, 'youracademy.in', 'Your course page', 'globe')
save('cover', svg(1600, 900, b, 'Meta ads for coaching institutes: an Instagram reel ad leading to a course page on the academy domain'))

# 2. funnel -------------------------------------------------------------------
W, H = 1220, 820
b = headline(60, 96, ['From reel to *enrolment*'], 54) + lines(62, 146, ['Every paid student follows the same four steps. Measure each one.'], 22)
steps = [('Ad', 'Reel or post on', 'Instagram / Facebook', 'play'),
         ('Course page', 'youracademy.in/', 'neet-dropper-batch', 'globe'),
         ('Checkout', 'UPI or card,', 'access is automatic', 'card'),
         ('Pixel event', 'Purchase sent', 'back to Meta', 'check')]
for i, (t, s1, s2, ic) in enumerate(steps):
    x = 60 + i * 280
    b += white_panel(x, 220, 250, 330, 28)
    tile = BLUE if i == 3 else NAVY_TILE
    b += f'<rect x="{x + 28}" y="248" width="68" height="68" rx="18" fill="{tile}"/>' + icon(ic, x + 44, 264, 36, '#fff', 2)
    b += eyebrow(x + 28, 368, f'Step {i + 1}')
    b += text(x + 28, 414, t, 32, INK, 800, font=F_HEAD, ls=-1.2)
    b += text(x + 28, 456, s1, 19, MUTED) + text(x + 28, 484, s2, 19, MUTED)
    if i < 3:
        b += arrow(f'M{x + 254} 385 H {x + 276}', BLUE, 4)
b += logo_tile(170, 256, logo_instagram, 52) + logo_tile(232, 256, logo_facebook, 52)
b += f'<path d="M1090 560 C 1090 680, 900 700, 610 700 S 190 680, 185 566" fill="none" stroke="{BLUE}" stroke-width="3.5" stroke-dasharray="8 9" marker-end="url(#ah)"/>'
b += f'<rect x="380" y="676" width="460" height="48" rx="24" fill="#fff" stroke="{BLUE}" stroke-width="2"/>' + text(610, 707, 'Meta learns who buys, finds more like them', 18, BLUE, 600, 'middle')
b += text(60, H - 28, 'Illustrative flow. Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('ad-to-enrolment-funnel', svg(W, H, b, 'Meta ads funnel for a coaching institute: ad, course page on own domain, checkout, Pixel purchase event'))

# 3. objectives ------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Six objectives. *Pick the one*', '*that matches the result.*'], 50)
objs = [('Awareness', 'Reach people near your centre before admissions open', 'users', False),
        ('Traffic', 'Send people to a page; cheap clicks, weak buyers', 'link', False),
        ('Engagement', 'Video views and WhatsApp or Messenger chats', 'message', False),
        ('Leads', 'Instant form for counselling calls and demo classes', 'file', True),
        ('App promotion', 'Installs of your own academy app', 'phone', False),
        ('Sales', 'Course purchases on your website, tracked by Pixel', 'card', True)]
for i, (t, d, ic, hl) in enumerate(objs):
    x = 60 + (i % 3) * 375
    y = 200 + (i // 3) * 310
    b += white_panel(x, y, 350, 280, 28)
    if hl:
        b += f'<rect x="{x}" y="{y}" width="350" height="280" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
        b += f'<rect x="{x + 190}" y="{y + 40}" width="130" height="34" rx="17" fill="{BLUE}"/>' + text(x + 255, y + 63, 'Best for coaching', 14, '#fff', 700, 'middle')
    b += f'<rect x="{x + 28}" y="{y + 28}" width="60" height="60" rx="16" fill="{BLUE if hl else BLUE_TINT}"/>' + icon(ic, x + 44, y + 44, 28, '#fff' if hl else BLUE, 2)
    b += text(x + 28, y + 150, t, 32, INK, 800, font=F_HEAD, ls=-1.2)
    words = d.split()
    rows, cur = [], ''
    for w_ in words:
        if len(cur) + len(w_) > 28:
            rows.append(cur.strip()); cur = ''
        cur += w_ + ' '
    rows.append(cur.strip())
    b += lines(x + 28, y + 192, rows, 19, MUTED, 1.4)
b += text(60, H - 28, 'Objective names as listed in Meta Ads Manager, checked October 2026.', 16, MUTED) + signature(W, H)
save('campaign-objectives', svg(W, H, b, 'The six Meta Ads Manager objectives and which ones suit coaching institutes: Leads and Sales'))

# 4. campaign structure ------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 96, ['One campaign, *three levels*'], 52) + lines(62, 146, ['Campaign sets the goal. Ad set picks the people. Ad is what they see.'], 22)
b += f'<g stroke="{INK}" stroke-width="2.5" fill="none" opacity=".35"><path d="M610 290 V 330 H 250 V 370"/><path d="M610 330 H 970 V 370"/>'
b += '<path d="M250 500 V 540 H 140 V 580"/><path d="M250 540 H 360 V 580"/><path d="M970 500 V 540 H 860 V 580"/><path d="M970 540 H 1080 V 580"/></g>'
b += f'<g filter="url(#sh)"><rect x="330" y="200" width="560" height="90" rx="45" fill="{NAVY_TILE}"/></g>'
b += eyebrow(610, 236, 'Campaign · Sales objective', '#9FB0FF', 'middle') + text(610, 272, 'NEET 2027 Dropper Batch', 28, '#fff', 800, 'middle', F_HEAD, -0.8)
for cx, t, s in [(250, 'Ad set A', 'Kota + 25 km · age 18+'), (970, 'Ad set B', 'Site visitors · last 30 days')]:
    b += f'<g filter="url(#shB)"><rect x="{cx - 200}" y="370" width="400" height="130" rx="26" fill="{BLUE}"/></g>'
    b += text(cx, 422, t, 30, '#fff', 800, 'middle', F_HEAD, -0.8) + text(cx, 462, s, 19, '#fff', 500, 'middle', opacity=.9)
for cx, t, s in [(140, 'Demo reel', 'Hindi · 30 sec'), (360, 'Faculty intro', 'carousel'), (860, 'Batch reminder', 'image + date'), (1080, 'FAQ reel', 'fees, timings')]:
    b += white_panel(cx - 100, 580, 200, 110, 22) + text(cx, 628, t, 21, INK, 700, 'middle', F_HEAD) + text(cx, 660, s, 17, MUTED, anchor='middle')
rows = [('Campaign', 'Objective, special ad category check, budget if campaign-level'),
        ('Ad set', 'Audience, location, placements, schedule, optimisation event'),
        ('Ad', 'Video or image, primary text, headline, button, destination URL')]
for i, (k, v) in enumerate(rows):
    y = 750 + i * 46
    b += text(60, y, k, 20, BLUE, 700, font=F_HEAD) + text(200, y, v, 20, INK)
b += signature(W, H)
save('campaign-structure', svg(W, H, b, 'Meta ads campaign structure for a NEET batch: one campaign, two ad sets, four ads'))

# 5. exam vs skill ---------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Exam batch or skill course?', '*Set it up differently.*'], 50)
cols = [('Exam batch', 'NEET, JEE, SSC, banking', 'trophy',
         ['Deadline: admissions close', 'Buyer is often a parent', 'Leads objective + call back', 'City radius for offline centre', 'Ads stop when the batch fills']),
        ('Skill course', 'Spoken English, yoga, Excel', 'sparkle',
         ['Evergreen: sells all year', 'Buyer is the learner', 'Sales objective + Pixel', 'All India, Hindi or English', 'Always-on, small daily budget'])]
for i, (t, s, ic, items) in enumerate(cols):
    x = 60 + i * 560
    b += white_panel(x, 220, 540, 600, 30)
    b += f'<rect x="{x + 32}" y="252" width="72" height="72" rx="20" fill="{NAVY_TILE if i == 0 else BLUE}"/>' + icon(ic, x + 50, 270, 36, '#fff', 2)
    b += text(x + 128, 286, t, 36, INK, 800, font=F_HEAD, ls=-1.4) + text(x + 128, 318, s, 19, MUTED)
    for k, it in enumerate(items):
        b += check_row(x + 34, 418 + k * 76, it, 23)
b += signature(W, H)
save('exam-vs-skill', svg(W, H, b, 'How to set up Meta ads for an exam batch versus a skill course'))

# 6. audience map ------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 96, ['Three audiences, *three messages*'], 52) + lines(62, 146, ['Cold people meet you. Warm people know you. Hot people almost bought.'], 22)
aud = [('Cold', 'New people', '#C9D3FF', INK, ['Advantage+ audience, broad', 'City or radius (offline centre)', 'Interests: NEET, yoga, English', 'Lookalike of past buyers'], 'Message: free demo class'),
       ('Warm', 'Saw your content', '#7F91FF', '#fff', ['Watched 50% of your reel', 'Engaged with your Instagram', 'Opened your lead form', 'Follow your Facebook Page'], 'Message: batch details, faculty'),
       ('Hot', 'Visited your site', BLUE, '#fff', ['Viewed the course page', 'Started checkout, did not pay', 'Website custom audience', 'Exclude people who bought'], 'Message: last date, FAQs')]
for i, (t, s, fill, fc, items, msg) in enumerate(aud):
    x = 60 + i * 375
    b += white_panel(x, 200, 350, 640, 28)
    b += f'<rect x="{x}" y="200" width="350" height="130" rx="28" fill="{fill}"/><rect x="{x}" y="300" width="350" height="30" fill="{fill}"/>'
    b += text(x + 30, 262, t, 44, fc, 800, font=F_HEAD, ls=-1.6) + text(x + 30, 302, s, 20, fc, 500, opacity=.85)
    for k, it in enumerate(items):
        b += f'<circle cx="{x + 40}" cy="{388 + k * 70}" r="6" fill="{BLUE}"/>' + text(x + 60, 395 + k * 70, it, 19, INK)
    b += f'<rect x="{x + 24}" y="720" width="302" height="92" rx="18" fill="{BLUE_TINT}"/>' + lines(x + 42, 758, msg.split(': ', 1)[0:1] + [msg.split(': ', 1)[1]], 19, BLUE, 1.4, weight=600)
b += text(60, H - 64, 'Ads that reach under-18s: no interests, custom or lookalike audiences,', 16, MUTED)
b += text(60, H - 38, 'and no location smaller than a city (Meta rules).', 16, MUTED) + signature(W, H)
save('audience-map', svg(W, H, b, 'Cold, warm and hot Meta ad audiences for a coaching institute with the message for each'))

# 7. reel anatomy ------------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 96, ['Anatomy of a reel ad *that enrols*'], 50)
b += reel_phone(110, 160, 380, ('Percentage in', '2 minute mein'), 'NEET 2027 · Dropper batch', 'Learn more')
callouts = [(250, 'Hook on screen, first seconds', 'the question your student is stuck on'),
            (360, 'Teach one real thing', 'a demo, not a promise'),
            (560, 'Your face, your voice', 'Hindi, Hinglish or English, as you teach'),
            (845, 'Batch, date and fee clarity', 'no "guaranteed selection" claims'),
            (920, 'One clear button', 'to your course page, not a DM maze')]
for n, (cy, t, s) in enumerate(callouts, 1):
    b += f'<path d="M470 {cy} H 600" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(624, cy, n) + text(660, cy - 2, t, 23, INK, 700, font=F_HEAD, ls=-0.4) + text(660, cy + 26, s, 18, MUTED)
b += text(660, 680, 'Add captions so the reel', 19, INK, 600) + text(660, 706, 'still works with sound off.', 19, INK, 600)
b += text(60, H - 28, 'Illustrative ad, not a real campaign. Claims about results must be true and verifiable.', 16, MUTED) + signature(W, H)
save('reel-ad-anatomy', svg(W, H, b, 'Anatomy of an Instagram reel ad for a coaching institute with five numbered parts'))

# 8. budget test timeline -----------------------------------------------------------
W, H = 1220, 800
b = headline(60, 96, ['A four-week *budget test*'], 52) + lines(62, 146, ['Illustrative plan for a ₹4,999 course. Your numbers will differ.'], 22)
b += f'<line x1="80" y1="210" x2="1140" y2="210" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
weeks = [('Week 1', 'Learn', '₹500/day', ['3 reels, 1 ad set', 'Pixel firing checked', 'Do not edit daily']),
         ('Week 2', 'Compare', '₹500/day', ['Pause weakest reel', 'Add 1 new hook', 'Note cost per click']),
         ('Week 3', 'Retarget', '+ ₹200/day', ['Visitors, 30 days', 'FAQ and fee reel', 'Exclude buyers']),
         ('Week 4', 'Decide', 'Keep / stop', ['Cost per enrolment', 'vs your margin', 'Scale or stop'])]
for k, (wk, t, bud, items) in enumerate(weeks):
    x = 60 + k * 280
    b += f'<circle cx="{x + 125}" cy="210" r="12" fill="{BLUE}" stroke="#fff" stroke-width="4"/>'
    b += white_panel(x, 250, 260, 440, 26)
    b += eyebrow(x + 26, 298, wk) + text(x + 26, 348, t, 36, INK, 800, font=F_HEAD, ls=-1.4)
    b += f'<rect x="{x + 26}" y="372" width="{150 if k < 3 else 160}" height="40" rx="20" fill="{BLUE_TINT}"/>' + text(x + 46, 399, bud, 19, BLUE, 700)
    for i, it in enumerate(items):
        b += check_row(x + 26, 480 + i * 70, it, 18)
b += text(60, H - 28, 'Illustrative. Daily amounts are examples, not Meta minimums or recommendations. GST is added to ad charges.', 16, MUTED) + signature(W, H)
save('budget-test-plan', svg(W, H, b, 'Illustrative four-week Meta ads budget test plan for an online course'))

# 9. cost per enrolment -----------------------------------------------------------
W, H = 1220, 880
b = headline(60, 96, ['The only number that *pays the rent*'], 50) + lines(62, 146, ['Cost per enrolment = ad spend ÷ paid enrolments'], 22)
b += f'<g filter="url(#sh)"><rect x="60" y="200" width="320" height="230" rx="26" fill="{NAVY_TILE}"/></g>'
b += eyebrow(90, 248, 'Ad spend', '#9FB0FF') + text(90, 330, '₹20,000', 54, '#fff', 800, font=F_HEAD, ls=-2) + text(90, 380, 'before GST on the invoice', 19, '#fff', opacity=.7)
b += text(420, 335, '÷', 60, INK, 300, 'middle')
b += white_panel(460, 200, 300, 230, 26) + eyebrow(490, 248, 'Paid enrolments') + text(490, 330, '16', 54, INK, 800, font=F_HEAD, ls=-2) + text(490, 380, 'counted by Pixel + UPI', 19, MUTED)
b += text(800, 335, '=', 60, INK, 300, 'middle')
b += f'<g filter="url(#shB)"><rect x="840" y="200" width="320" height="230" rx="26" fill="{BLUE}"/></g>'
b += eyebrow(870, 248, 'Cost per enrolment', '#DCE2FF') + text(870, 330, '₹1,250', 54, '#fff', 800, font=F_HEAD, ls=-2) + text(870, 380, 'per paying student', 19, '#fff', opacity=.85)
b += white_panel(60, 480, 1100, 300, 28)
b += eyebrow(92, 530, 'Is it worth it? Compare with what you keep')
rows = [('Course price', '₹4,999'), ('Platform fee on Growth (7.5%)', '− ₹375'), ('You keep before ads', '₹4,624'), ('Cost per enrolment', '− ₹1,250'), ('Left per student', '₹3,374')]
for i, (k, v) in enumerate(rows):
    y = 580 + i * 40
    bold = i in (2, 4)
    b += text(92, y, k, 20, INK, 700 if bold else 400) + text(600, y, v, 20, BLUE if i == 4 else INK, 700 if bold else 500, 'end')
b += lines(680, 590, ['Fine if teaching each student', 'costs you less than ₹3,374.', 'If not, fix the page or creative', 'before raising the budget.'], 20, MUTED, 1.5)
b += text(60, H - 28, 'Illustrative numbers, before GST. Meta adds GST to ad charges in India; check your invoice.', 16, MUTED) + signature(W, H)
save('cost-per-enrolment', svg(W, H, b, 'Cost per enrolment formula for Meta ads with an illustrative coaching example'))

# 10. mistakes ---------------------------------------------------------------------
W, H = 1220, 940
b = headline(56, 110, ['Burning money', 'on ads like this?'], 56)
for i, t in enumerate(['Boost post, no Pixel', 'Selection guaranteed', 'Interests for 16-year-olds', 'Edit the ad every day', 'Link to a WhatsApp DM']):
    b += tape(40 + (i % 2) * 22, 240 + i * 104, 510, t, -1.4 if i % 2 else 1.0, 30)
b += hand(320, 800, ['Leads but', 'no fees?'], 40, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Sales objective + Pixel', 'Only true, provable claims', 'Parents or 18+ droppers', 'Wait for ~50 results', 'Course page on your domain']):
    b += check_row(656, 400 + i * 74, t, 25)
b += button(650, 790, 500, 'Start your academy', 84, 32)
save('meta-ads-mistakes', svg(W, H, b, 'Common Meta ads mistakes coaching institutes make and what to do instead', ('split', 600)))

# 11. academy ready for ads (promo) -------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Your academy,', '*ready for ads.*'], 64)
b += lines(64, 380, ['Course pages on your domain, UPI', 'checkout and Meta Pixel built in.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
for k, (lab, ic, sub) in enumerate([('Own domain', 'globe', 'Every plan'), ('Meta Pixel', 'chart', 'Every plan'), ('GTM', 'layers', 'Every plan'),
                                     ('UPI checkout', 'card', 'Razorpay'), ('Your app', 'phone', 'iOS on Pro, Scale')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, 'Plans from ₹6,999/year + GST', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '14 days free · no card needed', 21, MUTED)
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
save('academy-ready-for-ads', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own domain, Meta Pixel, Google Tag Manager, UPI checkout and own app'))
