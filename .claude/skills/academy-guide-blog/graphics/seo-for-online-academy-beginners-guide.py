"""Graphics for /blog/seo-for-online-academy-beginners-guide.

Run:  python .claude/skills/academy-guide-blog/graphics/seo-for-online-academy-beginners-guide.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/seo-for-online-academy-beginners-guide
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'seo-for-online-academy-beginners-guide')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 320, ['Get your academy', '*found on Google.*'], 82)
b += lines(84, 500, ['SEO for educators who teach, not code.'], 30, MUTED)
b += check_row(84, 580, 'Keywords your students type', 26)
b += check_row(84, 640, 'Course pages that rank', 26)
b += check_row(84, 700, 'Cited in AI answers', 26)
b += white_panel(880, 150, 660, 590, 32, big=True)
b += search_bar(910, 195, 400, 'ssc cgl maths in hindi', 64, 'Search')
b += result(925, 305, 570, 'Your Academy', 'youracademy.in › ssc-cgl-maths-hindi',
            'SSC CGL Maths Course in Hindi', 'Chapter-wise lessons, PYQs and 20 mocks. Free demo.', True)
b += f'<rect x="1420" y="300" width="84" height="38" rx="19" fill="{BLUE}"/>' + text(1462, 326, '#1', 21, '#fff', 800, 'middle', F_HEAD)
b += ghost_lines(925, 500, [300, 500, 560, 260, 460, 520], 34)
b += pill_card(760, 660, 360, 'youracademy.in', 'Your own domain', 'globe')
b += white_panel(1300, 610, 270, 170, 24)
b += eyebrow(1328, 652, 'Organic clicks', MUTED)
b += f'<polyline points="1330,744 1376,730 1420,734 1464,706 1508,690 1546,662" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="1546" cy="662" r="9" fill="{BLUE}"/>'
save('cover', svg(1600, 900, b, "An educator's own academy ranking first on Google for a course search"))

# 2. serp anatomy -------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 96, ['Four places to be *found on Google*'], 50)
b += white_panel(60, 150, 700, 780, 28, big=True)
b += search_bar(90, 180, 640, 'upsc prelims test series in hindi', 56)
b += f'<rect x="90" y="262" width="640" height="176" rx="18" fill="#F1F4FF"/>' + icon('sparkle', 110, 280, 26, BLUE, 2) + text(146, 302, 'AI Overview', 21, INK, 700)
b += ghost_lines(110, 326, [560, 520, 420], 24, ('#C9D0EE',))
b += f'<rect x="110" y="396" width="190" height="30" rx="15" fill="#fff" stroke="{BLUE}" stroke-width="2"/>' + text(205, 417, 'youracademy.in', 16, BLUE, 600, 'middle')
b += text(90, 482, 'Sponsored', 16, INK, 700) + ghost_lines(90, 496, [380, 560], 26)
b += f'<rect x="90" y="560" width="640" height="130" rx="18" fill="#fff" stroke="{LINE}" stroke-width="2"/><rect x="90" y="560" width="210" height="130" rx="18" fill="#DDF0E0"/><rect x="282" y="560" width="18" height="130" fill="#DDF0E0"/>'
b += icon('pin', 140, 590, 34, RED, 2.4) + icon('pin', 214, 628, 34, RED, 2.4)
b += text(324, 604, 'Your Coaching Centre', 21, INK, 700) + text(324, 636, '★★★★★  ·  Coaching centre  ·  Open', 17, MUTED) + ghost_lines(324, 656, [300], 20, ('#E3E5EB',))
b += result(112, 740, 600, 'Your Academy', 'youracademy.in › upsc-prelims-hindi', 'UPSC Prelims Test Series in Hindi',
            'Hindi-medium mocks with solutions. Try one free.', True, 25)
for (yy, cy, t, s, ic) in [(300, 350, 'AI Overview', 'Cites clear answers', 'sparkle'),
                           (444, 505, 'Paid ads', 'You pay per click', 'card'),
                           (574, 625, 'Local pack', 'Google Business Profile', 'pin'),
                           (760, 812, 'Organic result', 'Free, earned by SEO', 'trophy')]:
    b += f'<path d="M738 {cy} H 800" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6 6"/>'
    b += pill_card(800, yy, 380, t, s, ic, tile=BLUE if ic == 'trophy' else NAVY_TILE)
b += text(60, H - 28, 'Illustrative layout. Real result pages vary by query, device and location.', 16, MUTED)
b += signature(W, H)
save('serp-anatomy', svg(W, H, b, 'Four places an online academy can appear on a Google results page'))

# 3. rented vs owned ------------------------------------------------------------
W, H = 1220, 780
b = eyebrow(56, 84, 'Rented reach', RED) + headline(56, 148, ['A reel or a post'], 46)
b += logo_tile(400, 40, logo_instagram, 64) + logo_tile(476, 40, logo_youtube, 64)
b += f'<polyline points="70,560 130,290 175,340 220,470 280,530 360,552 470,560 560,562" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
b += f'<line x1="66" y1="590" x2="560" y2="590" stroke="#CFCFD6" stroke-width="2"/>' + text(66, 624, 'Day 1', 17, MUTED) + text(560, 624, 'Day 30', 17, MUTED, anchor='end')
b += hand(330, 300, ['Gone in', 'three days?'], 40, INK, -6) + arrow('M372 380 C 360 430, 330 460, 300 500', INK, 3)
b += lines(56, 690, ['The feed decides who sees it.'], 22, INK)
b += eyebrow(666, 84, 'Owned search', BLUE) + headline(666, 148, ['A page on *your domain*'], 46)
b += logo_tile(1100, 40, logo_google, 64)
b += f'<path d="M680 562 C 800 556, 880 540, 960 500 S 1100 380, 1160 300" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><circle cx="1160" cy="300" r="11" fill="{BLUE}"/>'
b += f'<line x1="676" y1="590" x2="1170" y2="590" stroke="{LINE}" stroke-width="2"/>' + text(676, 624, 'Month 1', 17, MUTED) + text(1170, 624, 'Month 12', 17, MUTED, anchor='end')
b += lines(666, 690, ['Starts slow, keeps compounding.'], 22, INK)
b += text(56, H - 28, 'Illustrative shapes, not measured data.', 16, MUTED) + signature(W, H)
save('rented-vs-owned', svg(W, H, b, 'Rented social reach fades while search traffic to your own domain compounds', ('split', 610)))

# 4. how google works ------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['How Google *finds your academy*'], 52) + lines(62, 150, ['Three stages, as described by Google Search Central'], 22)
cards = [(60, 'search', 'Step 1', 'Crawl', ['Googlebot follows links', 'and your sitemap to', 'discover every page.'], 'You control: links, sitemap'),
         (450, 'layers', 'Step 2', 'Index', ['Google reads each page', 'and files it under the', 'topics it clearly covers.'], 'You control: words, titles'),
         (840, 'trophy', 'Step 3', 'Serve', ['For each search, Google', 'shows the pages it judges', 'most useful.'], 'You control: usefulness')]
for i, (x, ic, step, title, desc, ctrl) in enumerate(cards):
    y = 200
    b += white_panel(x, y, 320, 580, 28)
    b += f'<rect x="{x + 28}" y="{y + 28}" width="68" height="68" rx="18" fill="{NAVY_TILE}"/>' + icon(ic, x + 44, y + 44, 36, '#fff', 2)
    b += eyebrow(x + 28, y + 140, step) + text(x + 28, y + 192, title, 44, INK, 800, font=F_HEAD, ls=-1.8)
    mx, my = x + 28, y + 222
    b += f'<rect x="{mx}" y="{my}" width="264" height="170" rx="16" fill="#F4F6FF"/>'
    if i == 0:
        b += f'<rect x="{mx + 16}" y="{my + 16}" width="232" height="26" rx="13" fill="#fff" stroke="{LINE}"/>' + text(mx + 30, my + 34, 'youracademy.in/ssc', 14, MUTED)
        for k, (bx, by) in enumerate([(16, 58), (136, 58), (16, 112), (136, 112)]):
            b += f'<rect x="{mx + bx}" y="{my + by}" width="112" height="42" rx="10" fill="{"#C9D3FF" if k < 2 else "#E1E6FF"}"/>'
        b += f'<path d="M{mx + 72} {my + 100} V {my + 112} M{mx + 192} {my + 100} V {my + 112}" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="4 4"/>'
    elif i == 1:
        for k, t in enumerate(['ssc maths → course', 'pyq analysis → guide', 'hindi medium → course', 'demo → video page']):
            fill = BLUE if k == 3 else '#fff'
            b += f'<rect x="{mx + 14}" y="{my + 12 + k * 38}" width="236" height="30" rx="8" fill="{fill}" stroke="{LINE}"/>' + text(mx + 26, my + 33 + k * 38, t, 15, '#fff' if k == 3 else INK)
    else:
        b += f'<rect x="{mx + 14}" y="{my + 14}" width="236" height="30" rx="15" fill="#fff" stroke="{LINE}"/>' + text(mx + 30, my + 34, 'best ssc maths course', 14, MUTED)
        b += f'<rect x="{mx + 14}" y="{my + 58}" width="236" height="52" rx="10" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2"/><rect x="{mx + 28}" y="{my + 70}" width="130" height="10" rx="5" fill="{BLUE}"/><rect x="{mx + 28}" y="{my + 90}" width="190" height="8" rx="4" fill="#9AA6D9"/>'
        b += f'<rect x="{mx + 14}" y="{my + 122}" width="236" height="16" rx="8" fill="#E3E5EB"/><rect x="{mx + 14}" y="{my + 146}" width="180" height="12" rx="6" fill="#E3E5EB"/>'
    b += lines(x + 28, y + 444, desc, 20, MUTED, 1.35)
    b += text(x + 28, y + 552, ctrl, 18, BLUE, 600)
    if i < 2:
        b += arrow(f'M{x + 330} 490 H {x + 382}', BLUE, 4)
b += signature(W, H)
save('how-google-works', svg(W, H, b, 'How Google finds an online academy: crawl, index, serve'))

# 5. keyword formula --------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['The educator *keyword formula*'], 52) + lines(62, 150, ['Subject + modifiers = the exact phrase a student types'], 22)
b += f'<g filter="url(#sh)"><rect x="60" y="200" width="220" height="300" rx="26" fill="{NAVY_TILE}"/></g>'
b += eyebrow(88, 250, 'Seed', '#9FB0FF') + text(88, 320, 'Quant', 46, '#fff', 800, font=F_HEAD, ls=-1.8) + text(88, 370, 'maths', 46, '#fff', 800, font=F_HEAD, ls=-1.8)
b += text(88, 460, 'What you teach', 18, '#fff', opacity=.7)
b += text(305, 370, '+', 50, INK, 300, 'middle')
cols = [('Exam', 'trophy', ['SSC CGL', 'Bank PO', 'CAT', 'Railway NTPC']),
        ('Language', 'message', ['in Hindi', 'Hinglish', 'in Bengali', 'English medium']),
        ('Format', 'file', ['course', 'test series', 'PYQ PDF', 'live batch']),
        ('Need', 'bolt', ['for beginners', 'tricks', '2026 syllabus', 'crash course'])]
for k, (h, ic, items) in enumerate(cols):
    x = 330 + k * 210
    b += white_panel(x, 200, 196, 300, 24)
    b += f'<rect x="{x + 20}" y="{220}" width="48" height="48" rx="14" fill="{BLUE_TINT}"/>' + icon(ic, x + 32, 232, 24, BLUE, 2)
    b += eyebrow(x + 20, 302, h)
    b += lines(x + 20, 344, items, 20, INK, 1.6)
b += text(610, 560, '=', 54, INK, 300, 'middle')
b += white_panel(60, 600, 1100, 270, 28)
b += eyebrow(92, 648, 'Long-tail keywords (examples)')
pills = ['ssc cgl quant course in hindi', 'bank po maths tricks for beginners', 'cat quant crash course 2026',
         'railway ntpc maths pyq pdf in hindi', 'ssc cgl maths test series hinglish', 'quant live batch english medium']
for i, p in enumerate(pills):
    x = 92 + (i % 2) * 530
    y = 672 + (i // 2) * 64
    hl = i == 4
    b += f'<rect x="{x}" y="{y}" width="506" height="50" rx="25" fill="{BLUE_TINT if hl else "#F3F4F8"}"{" stroke=" + chr(34) + BLUE + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34) if hl else ""}/>'
    b += text(x + 24, y + 33, p, 21, BLUE if hl else INK, 500)
b += signature(W, H)
save('keyword-matrix', svg(W, H, b, 'Educator keyword formula: subject plus exam, language, format and need'))

# 6. autocomplete ---------------------------------------------------------------
W, H = 1220, 800
b = headline(60, 96, ['Let Google show you *what students type*'], 48)
b += white_panel(60, 150, 760, 560, 30, big=True)
b += icon('search', 100, 194, 30, '#5F6368', 2.2) + text(146, 218, 'neet physics course', 27, '#202124') + f'<rect x="412" y="194" width="2.5" height="30" fill="{BLUE}"/>'
b += f'<line x1="90" y1="252" x2="790" y2="252" stroke="{LINE}" stroke-width="2"/>'
sugg = ['in hindi', 'for dropper', 'for class 11', 'free', 'with test series', 'online best']
for i, s in enumerate(sugg):
    y = 300 + i * 66
    if i == 1:
        b += f'<rect x="80" y="{y - 38}" width="720" height="60" rx="14" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2.5"/>'
    b += icon('search', 100, y - 21, 22, '#9AA0A6', 2.2)
    b += f'<text x="140" y="{y}" font-size="24" fill="#202124">neet physics course <tspan font-weight="700">{esc(s)}</tspan></text>'
b += hand(880, 300, ['Every suggestion', '= a page idea'], 44, INK, -5)
b += arrow('M930 360 C 900 400, 860 380, 812 374', BLUE, 5)
b += pill_card(860, 470, 320, 'Page idea', 'Course for droppers', 'file')
b += text(60, H - 28, 'Illustrative suggestions. Type your own subject into Google and note what it completes.', 16, MUTED) + signature(W, H)
save('autocomplete', svg(W, H, b, 'Using Google autocomplete to find what students search'))

# 7. site structure -------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 96, ['Every page within *three clicks*'], 52) + lines(62, 146, ['A flat structure helps students and Googlebot reach every course'], 22)
b += f'<g stroke="{INK}" stroke-width="2.5" fill="none" opacity=".35"><path d="M610 270 V 300 H 220 V 340"/><path d="M610 300 V 340"/><path d="M610 300 H 1000 V 340"/>'
hubs = [(220, 'SSC hub', '/ssc'), (610, 'Banking hub', '/banking'), (1000, 'Free guides', '/blog')]
kids = [(130, 'CGL Maths', 'course'), (310, 'CGL Mocks', 'test series'), (520, 'PO Quant', 'course'), (700, 'Clerk Mocks', 'test series'), (910, 'Syllabus', 'guide'), (1090, 'PYQ analysis', 'guide')]
for i, (hx, _, _) in enumerate(hubs):
    a, c = kids[2 * i][0], kids[2 * i + 1][0]
    b += f'<path d="M{hx} 430 V 465 H {a} V 500"/><path d="M{hx} 465 H {c} V 500"/>'
b += '<path d="M130 590 V 640"/><path d="M310 590 V 640"/></g>'
b += f'<g filter="url(#sh)"><rect x="460" y="190" width="300" height="80" rx="40" fill="{NAVY_TILE}"/></g>' + icon('home', 494, 216, 28, '#fff') + text(626, 240, 'youracademy.in', 26, '#fff', 700, 'middle', F_HEAD)
for hx, t, u in hubs:
    b += f'<g filter="url(#shB)"><rect x="{hx - 125}" y="340" width="250" height="90" rx="22" fill="{BLUE}"/></g>'
    b += text(hx, 380, t, 25, '#fff', 800, 'middle', F_HEAD, -0.6) + text(hx, 410, u, 17, '#fff', 500, 'middle', F_MONO, opacity=.8)
for kx, t, u in kids:
    b += white_panel(kx - 82, 500, 164, 90, 20) + text(kx, 540, t, 20, INK, 700, 'middle', F_HEAD) + text(kx, 568, u, 16, MUTED, anchor='middle')
for kx, t in [(130, 'Demo lesson'), (310, 'Free mock')]:
    b += f'<rect x="{kx - 82}" y="640" width="164" height="62" rx="16" fill="#fff" fill-opacity=".7" stroke="#A9B3E0" stroke-dasharray="6 6"/>' + text(kx, 678, t, 18, INK, 500, 'middle')
b += text(60, H - 28, 'Guides link down to courses; courses link back up to their hub.', 16, MUTED) + signature(W, H)
save('site-structure', svg(W, H, b, 'A flat site structure for an online academy: home, exam hubs, courses and guides'))

# 8. course page anatomy -----------------------------------------------------------
W, H = 1220, 1200
b = headline(60, 96, ['Anatomy of a course page *that ranks*'], 50)
ox, oy = 60, 150
b += white_panel(ox, oy, 690, 960, 26, big=True)
b += f'<rect x="{ox}" y="{oy}" width="690" height="58" rx="26" fill="#F1F3F6"/><rect x="{ox}" y="{oy + 30}" width="690" height="28" fill="#F1F3F6"/>'
b += ''.join(f'<circle cx="{ox + 30 + k * 22}" cy="{oy + 29}" r="7" fill="{c}"/>' for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']))
b += f'<rect x="{ox + 100}" y="{oy + 13}" width="440" height="32" rx="16" fill="#fff"/>' + text(ox + 120, oy + 35, 'youracademy.in/ssc-cgl-maths-hindi', 16, INK)
px = ox + 40
b += text(px, oy + 122, 'SSC CGL Maths Course in Hindi', 32, INK, 800, font=F_HEAD, ls=-1.2)
b += text(px, oy + 156, 'By Your Name · 12 years teaching quant · Hindi medium', 16, MUTED)
b += f'<rect x="{px}" y="{oy + 180}" width="380" height="214" rx="14" fill="{NAVY_TILE}"/><circle cx="{px + 190}" cy="{oy + 287}" r="32" fill="#fff"/><path d="M{px + 181} {oy + 272} L{px + 205} {oy + 287} L{px + 181} {oy + 302}Z" fill="{NAVY_TILE}"/>'
b += text(px + 18, oy + 378, 'Free demo: Percentage in 20 minutes', 15, '#fff', opacity=.85)
b += f'<rect x="{px + 400}" y="{oy + 180}" width="210" height="214" rx="14" fill="#F4F6FF"/>' + text(px + 420, oy + 224, 'Full course', 16, MUTED) + text(px + 420, oy + 266, '₹1,999', 34, INK, 800, font=F_HEAD)
b += f'<rect x="{px + 420}" y="{oy + 326}" width="170" height="46" rx="16" fill="{BLUE}"/>' + text(px + 505, oy + 356, 'Enrol now', 17, '#fff', 700, 'middle', F_HEAD)
b += text(px, oy + 446, 'What you will be able to do', 20, INK, 700, font=F_HEAD)
b += lines(px, oy + 478, ['✓  Solve Tier 1 arithmetic faster with PYQ drills', '✓  Cover all 16 quant chapters'], 16, MUTED, 1.6)
b += text(px, oy + 560, 'Syllabus · 120 lessons', 20, INK, 700, font=F_HEAD)
for k, t in enumerate(['Chapter 1 · Number system · 9 lessons', 'Chapter 2 · Percentage · 8 lessons']):
    b += f'<rect x="{px}" y="{oy + 578 + k * 46}" width="610" height="38" rx="10" fill="#F4F6FF"/>' + text(px + 16, oy + 603 + k * 46, t, 15, INK)
b += text(px, oy + 712, 'Student reviews', 20, INK, 700, font=F_HEAD) + text(px, oy + 742, '“The PYQ discussion after every chapter helped me most.”', 16, MUTED)
b += text(px, oy + 798, 'Frequently asked questions', 20, INK, 700, font=F_HEAD)
for k, t in enumerate(['Is this course in Hindi medium?', 'How long do I get access?']):
    b += f'<rect x="{px}" y="{oy + 816 + k * 46}" width="610" height="38" rx="10" fill="#fff" stroke="{LINE}"/>' + text(px + 16, oy + 841 + k * 46, t, 15, INK)
b += text(px, oy + 934, 'Related: SSC CGL mock test series  →', 16, BLUE, 600)
callouts = [(oy + 29, 'Short, readable URL', 'keyword in the slug', 560),
            (oy + 112, 'One clear H1', 'exam + subject + language', 600),
            (oy + 260, 'Free demo lesson', 'proof before payment', 460),
            (oy + 350, 'Price, one button', 'no hidden steps', 690),
            (oy + 470, 'Outcomes in plain words', 'what students can do after', 520),
            (oy + 600, 'Full syllabus as text', 'Google reads text, not images', 690),
            (oy + 728, 'Real student reviews', 'trust for students and Google', 600),
            (oy + 850, 'FAQ + internal links', 'answers AI search can quote', 690)]
for n, (cy, t, s, lx) in enumerate(callouts, 1):
    b += f'<path d="M{lx} {cy} H 790" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(812, cy, n) + text(846, cy - 2, t, 21, INK, 700, font=F_HEAD, ls=-0.4) + text(846, cy + 24, s, 17, MUTED)
b += text(60, H - 28, 'Illustrative course page. Price, lesson counts and review are examples, not real data.', 16, MUTED) + signature(W, H)
save('course-page-anatomy', svg(W, H, b, 'Anatomy of an SEO-ready course page with eight labelled parts'))

# 9. content cluster -------------------------------------------------------------
W, H = 1220, 880
b = headline(60, 96, ['One topic, *many doors in*'], 52) + lines(62, 146, ['A pillar guide, supporting posts around it, all pointing to your course'], 22)
cx, cy = 610, 500
spokes = [(250, 300, 'Weightage', 'chart'), (970, 300, 'PYQ analysis', 'list'), (200, 520, 'Best books', 'book'),
          (1020, 520, 'Speed tricks', 'bolt'), (290, 730, '90-day plan', 'calendar')]
b += f'<g stroke="{INK}" stroke-width="2.5" opacity=".3" stroke-dasharray="7 7">' + ''.join(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}"/>' for x, y, _, _ in spokes) + f'<line x1="{cx}" y1="{cy}" x2="930" y2="730"/></g>'
b += f'<g filter="url(#shB)"><circle cx="{cx}" cy="{cy}" r="150" fill="{BLUE}"/></g>'
b += eyebrow(cx, cy - 40, 'Pillar guide', '#C9D3FF', 'middle') + text(cx, cy + 6, 'SSC CGL Maths:', 30, '#fff', 800, 'middle', F_HEAD, -1) + text(cx, cy + 44, 'Complete Guide', 30, '#fff', 800, 'middle', F_HEAD, -1)
for x, y, t, ic in spokes:
    b += pill_card(x - 150, y - 43, 300, t, None, ic, title_size=24)
b += f'<g filter="url(#sh)"><rect x="780" y="687" width="300" height="86" rx="24" fill="{NAVY_TILE}"/></g>' + f'<rect x="800" y="700" width="60" height="60" rx="16" fill="{BLUE}"/>' + icon('play', 816, 716, 28, '#fff') + text(880, 724, 'Every post links to', 16, '#fff', opacity=.7) + text(880, 752, 'Your paid course', 24, '#fff', 800, font=F_HEAD, ls=-0.6)
b += signature(W, H)
save('content-cluster', svg(W, H, b, 'Topic cluster: one pillar guide linked to supporting posts and a course page'))

# 10. roadmap ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 96, ['Your first *90 days* of academy SEO'], 52) + lines(62, 146, ['A realistic plan for an educator working a few hours a week'], 22)
b += f'<line x1="80" y1="210" x2="1140" y2="210" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
phases = [('Days 1–30', 'Foundation', ['Connect your own domain', 'Verify Search Console', 'Submit your sitemap', 'List 30 keywords', 'Fix titles and H1s', 'Business Profile (local)']),
          ('Days 31–60', 'Content', ['One pillar guide', 'One post a week', 'FAQs on every course', 'Link posts to courses', 'Link site in YouTube', 'Refresh old titles']),
          ('Days 61–90', 'Authority', ['Ask for student reviews', 'Earn 3–5 real mentions', 'Read Search Console', 'Rewrite low-CTR titles', 'Update pillar pages', 'Plan the next 90 days'])]
for k, (when, title, items) in enumerate(phases):
    x = 60 + k * 375
    b += f'<circle cx="{x + 170}" cy="210" r="12" fill="{BLUE}" stroke="#fff" stroke-width="4"/>'
    b += white_panel(x, 250, 350, 560, 28)
    b += eyebrow(x + 30, 300, when) + text(x + 30, 352, title, 40, INK, 800, font=F_HEAD, ls=-1.6)
    for i, it in enumerate(items):
        b += check_row(x + 30, 420 + i * 64, it, 19)
b += text(60, H - 28, 'Google: some changes show in hours, others take several months.', 16, MUTED) + signature(W, H)
save('roadmap-90-days', svg(W, H, b, 'A 90-day SEO roadmap for an online academy in three phases'))

# 11. mistakes (before / after) -------------------------------------------------------
W, H = 1220, 940
b = headline(56, 110, ['Still doing', 'SEO like this?'], 58)
for i, t in enumerate(['One page, all courses', 'Syllabus as an image', 'Subdomain only', 'Bought backlinks', 'Same text everywhere']):
    b += tape(40 + (i % 2) * 22, 250 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(330, 820, ['No clicks', 'again?'], 40, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['One page per course', 'Syllabus written as text', 'Your own domain', 'Mentions you earn', 'A unique description per page']):
    b += check_row(656, 400 + i * 74, t, 25)
b += button(650, 790, 500, 'Start your academy', 84, 32)
b += signature(W, H) if False else ''
save('seo-mistakes', svg(W, H, b, 'Common academy SEO mistakes and what to do instead', ('split', 600)))

# 12. academy features (promo band) ------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['One login.', '*Your whole*', '*academy.*'], 64)
b += lines(64, 440, ['Website, app, live classes, tests', 'and payments. Already built in.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
for k, (lab, ic, sub) in enumerate([('Website', 'globe', 'Your domain'), ('Live', 'video', 'Unlimited'), ('Payments', 'card', 'UPI & cards'),
                                     ('Tests', 'check', 'Built in'), ('Your app', 'phone', 'Android & iOS')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission on Growth and Pro', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · own domain on every plan', 21, MUTED)
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
save('academy-features', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: website, live classes, payments, tests and your own app in one login'))

# 13. free tools -----------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 96, ['Free tools that do *the heavy lifting*'], 50) + lines(62, 146, ['Everything in this guide works with tools that cost nothing'], 22)
tools = [(logo_google, 'Search Console', 'Queries, clicks, positions', 'Must have'),
         (logo_google, 'Google Trends', 'Exam-season demand', 'Free'),
         (logo_google, 'Keyword Planner', 'Monthly search ranges', 'Free'),
         (logo_google, 'Business Profile', 'Local pack and reviews', 'Free'),
         (logo_youtube, 'YouTube search', 'What students type on video', 'Free'),
         (logo_google, 'PageSpeed Insights', 'Mobile speed checks', 'Free')]
for i, (fn, name, use, tag) in enumerate(tools):
    x = 60 + (i % 3) * 375
    y = 200 + (i // 3) * 300
    b += white_panel(x, y, 350, 270, 28)
    b += logo_tile(x + 30, y + 30, fn, 76)
    hl = tag == 'Must have'
    b += f'<rect x="{x + 214}" y="{y + 46}" width="{106 if hl else 64}" height="34" rx="17" fill="{BLUE if hl else BLUE_TINT}"/>' + text(x + (267 if hl else 246), y + 69, tag, 15, '#fff' if hl else BLUE, 700, 'middle')
    b += text(x + 30, y + 166, name, 30, INK, 800, font=F_HEAD, ls=-1) + text(x + 30, y + 204, use, 20, MUTED)
b += text(60, H - 28, 'Keyword Planner needs a free Google Ads account. Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('free-tools', svg(W, H, b, 'Free SEO tools for educators: Search Console, Google Trends, Keyword Planner, Business Profile, YouTube search and PageSpeed Insights'))
