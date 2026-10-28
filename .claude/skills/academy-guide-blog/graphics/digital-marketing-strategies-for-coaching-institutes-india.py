"""Graphics for /blog/digital-marketing-strategies-for-coaching-institutes-india.

Run:  python .claude/skills/academy-guide-blog/graphics/digital-marketing-strategies-for-coaching-institutes-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/digital-marketing-strategies-for-coaching-institutes-india
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SLUG = 'digital-marketing-strategies-for-coaching-institutes-india'
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

FB_BLUE = '#0866FF'
TG_BLUE = '#27A7E7'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def logo_facebook(x, y, size=40):
    """Facebook 'f' mark in its brand blue (nominative use), as in the Meta ads guide."""
    s = size / 24
    return (f'<g transform="translate({x} {y}) scale({s:.4f})"><path fill="{FB_BLUE}" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 '
            '1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 '
            '0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 '
            '1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></g>')


def logo_telegram(x, y, size=40):
    """Simple Telegram paper-plane mark (nominative use)."""
    s = size
    return (f'<circle cx="{x + s / 2}" cy="{y + s / 2}" r="{s / 2}" fill="{TG_BLUE}"/>'
            f'<path d="M{x + s * .22} {y + s * .5} L{x + s * .76} {y + s * .29} L{x + s * .67} {y + s * .74} L{x + s * .5} {y + s * .6} Z" fill="#fff"/>'
            f'<path d="M{x + s * .45} {y + s * .56} L{x + s * .47} {y + s * .7} L{x + s * .55} {y + s * .63}" fill="#D3ECF9"/>')


def wrap(t, n):
    rows, cur = [], ''
    for w_ in t.split():
        if cur and len(cur) + len(w_) + 1 > n:
            rows.append(cur)
            cur = ''
        cur = (cur + ' ' + w_).strip()
    rows.append(cur)
    return rows


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Digital marketing for', '*coaching institutes.*'], 76)
b += lines(84, 456, ['Every channel, one system, measured by enrolments.'], 28, MUTED)
b += check_row(84, 545, 'Own website, course pages, tracking', 26)
b += check_row(84, 605, 'SEO, Google, YouTube, Reels, WhatsApp', 26)
b += check_row(84, 665, 'Ads only where cost per enrolment works', 26)
for k, fn in enumerate([logo_google, logo_youtube, logo_instagram, logo_whatsapp, logo_facebook]):
    b += logo_tile(84 + k * 92, 728, fn, 76)
b += text(84, 846, 'Logos belong to their owners', 17, MUTED)
b += laptop(930, 150, 560, 'studio-desktop.jpg')
b += phone(1330, 330, 170, 'studio-mobile.jpg')
b += pill_card(800, 560, 400, 'youracademy.in', 'Course page on your domain', 'globe')
b += pill_card(880, 690, 330, 'Demo class booked', 'From an Instagram reel', 'calendar', tile=BLUE)
b += pill_card(1240, 120, 300, 'UPI payment', 'Enrolment recorded', 'card', tilt=2)
save('cover', svg(1600, 900, b, 'Digital marketing for coaching institutes: own academy website, Google, YouTube, Instagram, WhatsApp and ads measured by enrolments'))

# 2. marketing system --------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 96, ['One marketing *system*,', 'not ten random posts'], 52)
b += lines(62, 196, ['Every channel feeds the same academy. Every enrolment is counted there.'], 22)
cx, cy = 610, 590
b += f'<circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="4 12" stroke-linecap="round"/>'
b += f'<g filter="url(#shB)"><circle cx="{cx}" cy="{cy}" r="125" fill="{BLUE}"/></g>'
b += icon('home', cx - 22, cy - 92, 44, '#fff', 2)
b += text(cx, cy - 4, 'Your academy', 27, '#fff', 800, 'middle', F_HEAD, -0.8)
b += text(cx, cy + 28, 'youracademy.in', 19, '#fff', 500, 'middle', opacity=.9)
b += text(cx, cy + 56, 'website + own app', 17, '#fff', 400, 'middle', opacity=.8)
nodes = [(cx, cy - 290, '1 · Attract', ['SEO, Google profile,', 'YouTube, Reels'], 'search'),
         (cx + 345, cy, '2 · Convert', ['Course page, demo,', 'call, UPI checkout'], 'card'),
         (cx, cy + 290, '3 · Retain', ['WhatsApp updates,', 'results, referrals'], 'users'),
         (cx - 345, cy, '4 · Measure', ['Pixel, Tag Manager,', 'Search Console'], 'chart')]
for nx, ny, t, rows, ic in nodes:
    x0, y0 = nx - 165, ny - 70
    b += white_panel(x0, y0, 330, 140, 26)
    b += f'<rect x="{x0 + 22}" y="{y0 + 24}" width="56" height="56" rx="16" fill="{NAVY_TILE}"/>' + icon(ic, x0 + 36, y0 + 38, 28, '#fff', 2)
    b += text(x0 + 96, y0 + 52, t, 26, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(x0 + 96, y0 + 86, rows, 18, MUTED, 1.35)
b += text(60, H - 28, 'Illustrative model of a coaching marketing system.', 16, MUTED) + signature(W, H)
save('marketing-system', svg(W, H, b, 'Digital marketing system for a coaching institute: attract, convert, retain and measure around the academy website'))

# 3. foundation ----------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Build the shop', '*before the ads.*'], 64)
b += lines(64, 380, ['Course pages on your own domain, UPI', 'checkout and tracking codes in one place.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Own domain', 'globe', 'Every plan'), ('Course pages', 'file', 'Price + pay button'), ('Meta Pixel', 'chart', 'Every plan'),
                                     ('Tag Manager', 'layers', 'Every plan'), ('UPI checkout', 'card', 'Razorpay')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission on Growth and Pro', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('marketing-foundation', svg(W, H, b, 'AllCoaching Studio on laptop and phone: own domain, course pages, Meta Pixel, Google Tag Manager and UPI checkout'))

# 4. organic channels ----------------------------------------------------------------
W, H = 1220, 1080
b = headline(60, 96, ['Eight organic channels.', '*Pick two, do them well.*'], 50)
chans = [(logo_google, 'Google Search', 'Course pages and guides', 'that rank for exam queries'),
         ('gbp', 'Google Business Profile', 'Map and local results', 'for an offline centre'),
         (logo_youtube, 'YouTube', 'Full demo lessons, PYQs', 'and Shorts up to 3 min'),
         (logo_instagram, 'Instagram Reels', 'One concept per reel,', 'in your teaching language'),
         (logo_whatsapp, 'WhatsApp', 'Channel for updates,', 'chat for counselling'),
         (logo_telegram, 'Telegram', 'Notice board for some exam', 'groups, never the only home'),
         ('blog', 'Blog and free notes', 'Answers to the questions', 'students already search'),
         ('star', 'Results and reviews', 'True, provable outcomes', 'with the student\'s consent')]
for i, (fn, t, s1, s2) in enumerate(chans):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 205
    b += white_panel(x, y, 540, 180, 26)
    if callable(fn):
        b += logo_tile(x + 26, y + 26, fn, 72)
    else:
        ic = {'gbp': 'pin', 'blog': 'book', 'star': 'star'}[fn]
        b += f'<g filter="url(#sh)"><rect x="{x + 26}" y="{y + 26}" width="72" height="72" rx="19" fill="{BLUE_TINT}"/></g>' + icon(ic, x + 44, y + 44, 36, BLUE, 2.1)
    b += text(x + 122, y + 60, t, 28, INK, 800, font=F_HEAD, ls=-1)
    b += text(x + 122, y + 100, s1, 20, MUTED) + text(x + 122, y + 130, s2, 20, MUTED)
b += text(60, H - 28, 'Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('organic-channels', svg(W, H, b, 'Eight organic marketing channels for coaching institutes: Google Search, Google Business Profile, YouTube, Instagram Reels, WhatsApp, Telegram, blog and reviews'))

# 5. Google Business Profile anatomy ------------------------------------------------
W, H = 1220, 1060
b = headline(60, 96, ['A Google Business Profile', '*that brings walk-ins*'], 50)
px, py, pw = 70, 220, 520
b += white_panel(px, py, pw, 760, 30, True)
b += f'<rect x="{px}" y="{py}" width="{pw}" height="170" rx="30" fill="#DCE3FF"/><rect x="{px}" y="{py + 140}" width="{pw}" height="30" fill="#DCE3FF"/>'
b += icon('image', px + pw / 2 - 30, py + 55, 60, '#8F9BD6', 1.6)
b += text(px + 30, py + 220, 'Sharma Classes', 32, INK, 800, font=F_HEAD, ls=-1)
b += text(px + 30, py + 256, 'Coaching center · Lanka, Varanasi', 19, MUTED)
b += ''.join(icon('star', px + 30 + k * 26, py + 276, 22, '#F4B400', 2) for k in range(5))
b += text(px + 168, py + 294, 'Reviews from real students', 17, MUTED)
for k, (lab, ic) in enumerate([('Website', 'globe'), ('Directions', 'pin'), ('Call', 'phone')]):
    bx = px + 30 + k * 160
    b += f'<rect x="{bx}" y="{py + 326}" width="146" height="50" rx="25" fill="#fff" stroke="#DADCE0" stroke-width="2"/>' + icon(ic, bx + 16, py + 339, 24, '#1A73E8', 2) + text(bx + 48, py + 358, lab, 18, '#1A73E8', 600)
rows = [('clock', 'Open · 7 am to 8 pm'), ('home', 'Address shown on the map'), ('calendar', 'Post: new batch starts 5 Jan'), ('image', 'Photos: classroom, faculty, board')]
for k, (ic, t) in enumerate(rows):
    yy = py + 440 + k * 64
    b += icon(ic if ic != 'clock' else 'calendar', px + 30, yy - 20, 26, MUTED, 2) + text(px + 74, yy, t, 20, INK)
b += f'<rect x="{px + 30}" y="{py + 680}" width="{pw - 60}" height="50" rx="14" fill="{BLUE_TINT}"/>' + text(px + 50, py + 712, 'Q&A: Is there a demo class?', 19, BLUE, 600)
b += logo_tile(px + pw - 100, py + 30, logo_google, 70)
call = [(py + 220, 'Real name, no keywords', 'Google does not allow extra words in the name'),
        (py + 256, 'Accurate category', 'categories are not keywords'),
        (py + 290, 'Reviews you reply to', 'more reviews can help local ranking'),
        (py + 351, 'Website = your academy', 'link the course page, not a PDF'),
        (py + 504, 'Posts and photos', 'batch dates, classroom, faculty'),
        (py + 705, 'Answer common questions', 'fees, timings, demo class')]
for n, (cy_, t, s) in enumerate(call, 1):
    yy = 270 + (n - 1) * 120
    b += f'<path d="M{px + pw - 10} {cy_} C {px + pw + 40} {cy_}, {640} {yy}, {660} {yy}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(684, yy, n) + text(720, yy - 4, t, 23, INK, 700, font=F_HEAD, ls=-0.4) + text(720, yy + 24, s, 18, MUTED)
b += text(60, H - 50, 'Illustrative profile. For centres students can visit. Rules from Google', 16, MUTED)
b += text(60, H - 26, 'Business Profile Help, checked October 2026. Logo belongs to its owner.', 16, MUTED) + signature(W, H)
save('google-business-profile', svg(W, H, b, 'Anatomy of a Google Business Profile for a coaching centre with six numbered tips'))

# 6. organic vs paid -----------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Organic builds. *Paid speeds up.*'], 52)
b += lines(62, 146, ['You need both, in that order. Here is how they differ.'], 22)
b += white_panel(60, 200, 1100, 620, 30)
b += f'<rect x="440" y="200" width="360" height="620" fill="{BLUE_TINT}" opacity=".55"/>'
b += eyebrow(90, 262, 'Question') + text(470, 262, 'ORGANIC', 18, BLUE, 700, font=F_MONO, ls=2) + text(830, 262, 'PAID', 18, INK, 700, font=F_MONO, ls=2)
b += logo_tile(600, 222, logo_youtube, 52) + logo_tile(660, 222, logo_google, 52) + logo_tile(1000, 222, logo_facebook, 52) + logo_tile(1060, 222, logo_instagram, 52)
rows = [('Cost model', 'Your time, plus creative help', 'Pay per click, view or lead'),
        ('Starts working', 'Weeks to months', 'Same day the ad is approved'),
        ('When you stop', 'Pages and videos keep working', 'Reach stops with the budget'),
        ('Best for', 'Trust, search demand, reviews', 'Deadlines and new batches'),
        ('Judge it by', 'Enrolments from search, video', 'Cost per paid enrolment'),
        ('Main risk', 'Giving up too early', 'Clicks sent to a weak page')]
for i, (k, o, p) in enumerate(rows):
    y = 340 + i * 78
    b += f'<line x1="80" y1="{y - 42}" x2="1140" y2="{y - 42}" stroke="{LINE}" stroke-width="2"/>'
    b += text(90, y, k, 21, INK, 700, font=F_HEAD) + text(470, y, o, 20, INK) + text(830, y, p, 20, INK)
b += text(60, H - 28, 'Logos belong to their owners. Ads platforms charge per click, view or result depending on the bid you choose.', 16, MUTED) + signature(W, H)
save('organic-vs-paid', svg(W, H, b, 'Organic versus paid marketing for coaching institutes compared on cost, speed, durability and measurement'))

# 7. enrolment funnel -------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 96, ['From first view to *paid enrolment*'], 50)
b += lines(62, 146, ['Most leaks happen after the click, not before it.'], 22)
steps = [('See', 'Reel, Short, search', 'result or ad', 'play'),
         ('Visit', 'Course page on', 'youracademy.in', 'globe'),
         ('Try', 'Free demo class', 'or sample test', 'video'),
         ('Ask', 'Counselling call or', 'WhatsApp chat', 'message'),
         ('Pay', 'UPI or card,', 'instant access', 'card')]
for i, (t, s1, s2, ic) in enumerate(steps):
    x = 60 + i * 222
    w = 200
    b += white_panel(x, 220, w, 330, 26)
    tile = BLUE if i == 4 else NAVY_TILE
    b += f'<rect x="{x + 24}" y="246" width="60" height="60" rx="16" fill="{tile}"/>' + icon(ic, x + 39, 261, 30, '#fff', 2)
    b += eyebrow(x + 24, 352, f'Step {i + 1}')
    b += text(x + 24, 398, t, 34, INK, 800, font=F_HEAD, ls=-1.2)
    b += text(x + 24, 440, s1, 18, MUTED) + text(x + 24, 466, s2, 18, MUTED)
    if i < 4:
        b += arrow(f'M{x + w + 2} 385 H {x + w + 18}', BLUE, 4)
leaks = ['No price on the page', 'Demo link that needs a login', 'Nobody calls back in 24 hours', 'Pay by bank transfer and screenshot']
b += white_panel(60, 600, 1100, 190, 26)
b += eyebrow(90, 648, 'Where students drop off')
for k, t in enumerate(leaks):
    xx = 90 + (k % 2) * 540
    yy = 700 + (k // 2) * 52
    b += check_row(xx, yy, t, 21, ok=False)
b += signature(W, H)
save('enrolment-funnel', svg(W, H, b, 'Coaching enrolment funnel: see, visit course page, free demo class, counselling, UPI payment, and where students drop off'))

# 8. channel map by goal -----------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 96, ['Same channels, *different order*'], 52)
b += lines(62, 146, ['Start with the first two in your column. Add the rest later.'], 22)
cols = [('Offline centre', 'NEET/JEE centre in Kota, Patna', 'home',
         ['Google Business Profile', 'Google Search ads (local)', 'Meta ads, city radius', 'WhatsApp for parents', 'Results and reviews']),
        ('Online exam batch', 'SSC, banking, UPSC, CUET', 'trophy',
         ['YouTube lessons + Shorts', 'SEO: PYQ and syllabus', 'WhatsApp Channel', 'Meta ads before batch date', 'Free mock test as lead']),
        ('Skill course', 'Spoken English, yoga, music', 'sparkle',
         ['Instagram Reels', 'YouTube tutorials', 'Meta ads, always on', 'Free first class', 'Student stories, referrals'])]
for i, (t, s, ic, items) in enumerate(cols):
    x = 60 + i * 375
    b += white_panel(x, 210, 350, 700, 28)
    b += f'<rect x="{x + 26}" y="238" width="64" height="64" rx="18" fill="{NAVY_TILE if i != 1 else BLUE}"/>' + icon(ic, x + 42, 254, 32, '#fff', 2)
    b += text(x + 26, 360, t, 30, INK, 800, font=F_HEAD, ls=-1.1) + text(x + 26, 392, s, 18, MUTED)
    for k, it in enumerate(items):
        y = 470 + k * 88
        fill = BLUE if k < 2 else BLUE_TINT
        col = '#fff' if k < 2 else BLUE
        b += f'<circle cx="{x + 46}" cy="{y - 7}" r="18" fill="{fill}"/>' + text(x + 46, y, str(k + 1), 18, col, 800, 'middle', F_HEAD)
        b += text(x + 78, y, it, 20, INK, 600 if k < 2 else 400)
b += text(60, H - 28, 'Illustrative priorities. Your city, subject and season can change the order.', 16, MUTED) + signature(W, H)
save('channel-map-by-goal', svg(W, H, b, 'Marketing channel priorities for an offline coaching centre, an online exam batch and a skill course'))

# 9. 90-day plan ---------------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 96, ['Your first *90 days*'], 56)
b += lines(62, 150, ['Build, publish, then test paid. One phase at a time.'], 22)
b += f'<line x1="120" y1="232" x2="1100" y2="232" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
phases = [('Days 1–30', 'Foundation', ['Academy on own domain', 'Course page per batch', 'Pixel + Tag Manager', 'Search Console verified', 'Google profile (centres)']),
          ('Days 31–60', 'Content engine', ['2 lessons or Shorts a week', '3 reels a week, Hindi too', 'WhatsApp Channel started', '4 answer-first blog pages', 'Ask for honest reviews']),
          ('Days 61–90', 'Paid test', ['Small Meta or Search test', 'Retarget page visitors', 'Weekly demo class', 'Check cost per enrolment', 'Keep, fix or stop'])]
for k, (d, t, items) in enumerate(phases):
    x = 60 + k * 375
    b += f'<circle cx="{x + 175}" cy="232" r="13" fill="{BLUE}" stroke="#fff" stroke-width="4"/>'
    b += white_panel(x, 280, 350, 560, 28)
    b += eyebrow(x + 30, 330, d) + text(x + 30, 384, t, 36, INK, 800, font=F_HEAD, ls=-1.4)
    for i, it in enumerate(items):
        b += check_row(x + 30, 460 + i * 72, it, 19)
b += text(60, H - 28, 'Illustrative plan. Exam calendars and admission seasons may shift the order.', 16, MUTED) + signature(W, H)
save('ninety-day-plan', svg(W, H, b, '90-day digital marketing plan for a coaching institute: foundation, content engine, paid test'))

# 10. budget split ---------------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Where the money goes:', '*an illustrative split*'], 50)
b += lines(62, 206, ['Share of a monthly marketing budget. Not a recommendation for your city or subject.'], 21)
segs = {'Content': '#1B1E2E', 'Meta ads': BLUE, 'Google Search ads': '#7F91FF', 'YouTube ads': '#C9D3FF', 'Design, video kit, tools': '#E3E5EB'}
bars = [('Offline centre', [('Content', 20), ('Meta ads', 30), ('Google Search ads', 35), ('Design, video kit, tools', 15)]),
        ('Online exam batch', [('Content', 35), ('Meta ads', 40), ('YouTube ads', 15), ('Design, video kit, tools', 10)]),
        ('Skill course', [('Content', 35), ('Meta ads', 45), ('Google Search ads', 10), ('Design, video kit, tools', 10)])]
x0, bw = 330, 820
for i, (lab, parts) in enumerate(bars):
    y = 290 + i * 140
    b += text(60, y + 44, lab, 26, INK, 800, font=F_HEAD, ls=-0.8)
    cx_ = x0
    for name, pct in parts:
        w = bw * pct / 100
        fc = '#fff' if name in ('Content', 'Meta ads') else INK
        b += f'<rect x="{cx_ + 2}" y="{y}" width="{w - 4}" height="70" rx="12" fill="{segs[name]}"/>'
        b += text(cx_ + w / 2, y + 44, f'{pct}%', 22, fc, 700, 'middle', F_HEAD)
        cx_ += w
for k, (name, col) in enumerate(segs.items()):
    xx = 60 + (k % 3) * 360
    yy = 740 + (k // 3) * 48
    b += f'<rect x="{xx}" y="{yy - 20}" width="26" height="26" rx="7" fill="{col}"/>' + text(xx + 40, yy, name, 20, INK)
b += text(60, H - 28, 'Illustrative only. GST is added to ad charges in India. Start small and move money to what enrols.', 16, MUTED) + signature(W, H)
save('budget-split', svg(W, H, b, 'Illustrative marketing budget split for an offline centre, an online exam batch and a skill course'))

# 11. cost per enrolment --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Cost per enrolment, *per channel*'], 50)
b += lines(62, 146, ['Marketing spend ÷ paid enrolments from that channel, same period'], 22)
b += f'<g filter="url(#sh)"><rect x="60" y="200" width="320" height="230" rx="26" fill="{NAVY_TILE}"/></g>'
b += eyebrow(90, 248, 'Spend in a month', '#9FB0FF') + text(90, 330, '₹36,000', 54, '#fff', 800, font=F_HEAD, ls=-2) + text(90, 380, 'ads + creatives, before GST', 19, '#fff', opacity=.7)
b += text(420, 335, '÷', 60, INK, 300, 'middle')
b += white_panel(460, 200, 300, 230, 26) + eyebrow(490, 248, 'Paid enrolments') + text(490, 330, '24', 54, INK, 800, font=F_HEAD, ls=-2) + text(490, 380, 'from your payment records', 19, MUTED)
b += text(800, 335, '=', 60, INK, 300, 'middle')
b += f'<g filter="url(#shB)"><rect x="840" y="200" width="320" height="230" rx="26" fill="{BLUE}"/></g>'
b += eyebrow(870, 248, 'Cost per enrolment', '#DCE2FF') + text(870, 330, '₹1,500', 54, '#fff', 800, font=F_HEAD, ls=-2) + text(870, 380, 'per paying student', 19, '#fff', opacity=.85)
b += white_panel(60, 480, 1100, 300, 28)
b += eyebrow(92, 530, 'Compare with what you keep per sale')
rows = [('Course price', '₹6,000'), ('Commission on Growth (0%)', '− ₹0'), ('You keep before marketing', '₹6,000'), ('Cost per enrolment', '− ₹1,500'), ('Left per student', '₹4,500')]
for i, (k, v) in enumerate(rows):
    y = 580 + i * 40
    bold = i in (2, 4)
    b += text(92, y, k, 20, INK, 700 if bold else 400) + text(600, y, v, 20, BLUE if i == 4 else INK, 700 if bold else 500, 'end')
b += lines(680, 590, ['Work it out per channel too:', 'organic enrolments cost time,', 'paid ones cost money. Count', 'both before you scale.'], 20, MUTED, 1.5)
b += text(60, H - 28, 'Illustrative numbers before GST. Count enrolments from your own payment records.', 16, MUTED) + signature(W, H)
save('cost-per-enrolment', svg(W, H, b, 'Cost per enrolment formula for coaching marketing with an illustrative example: ₹36,000 divided by 24 enrolments equals ₹1,500'))

# 12. mistakes ---------------------------------------------------------------------------
W, H = 1220, 960
b = headline(56, 110, ['Marketing that', 'looks busy?'], 56)
for i, t in enumerate(['Selection guaranteed', 'Ads to a WhatsApp DM', 'Posting on 8 apps', 'No price on the page', 'Counting likes, not fees', 'Fake reviews']):
    b += tape(40 + (i % 2) * 22, 220 + i * 96, 510, t, -1.4 if i % 2 else 1.0, 30)
b += hand(330, 845, ['Followers but', 'no admissions?'], 38, INK, -6) + arrow('M310 870 C 260 890, 210 870, 190 840', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Only true, provable claims', 'Course page with a pay button', 'Two channels, done weekly', 'Price and batch date visible', 'Track cost per enrolment', 'Real reviews, with consent']):
    b += check_row(656, 390 + i * 70, t, 24)
b += button(650, 830, 500, 'Start your academy', 84, 32)
save('marketing-mistakes', svg(W, H, b, 'Common digital marketing mistakes coaching institutes make and what to do instead', ('split', 600)))
