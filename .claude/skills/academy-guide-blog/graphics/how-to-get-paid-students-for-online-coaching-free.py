"""Graphics for /blog/how-to-get-paid-students-for-online-coaching-free
(refreshed 2026-11-04: "How to Get Students Without Paid Ads: 9 Organic Ways").

Run:  python .claude/skills/academy-guide-blog/graphics/how-to-get-paid-students-for-online-coaching-free.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/how-to-get-paid-students-for-online-coaching-free

All academies, links and numbers drawn here are illustrative (fictional "Your Academy", youracademy.in).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SLUG = 'how-to-get-paid-students-for-online-coaching-free'
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
ICONS['send'] = '<path d="M21 3L3 10.5l7 2.5 2.5 7z"/><path d="M10 13l11-10"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def logo_telegram(x, y, size=40):
    """Telegram mark: blue circle with a white paper plane."""
    s = size / 24
    return (f'<circle cx="{x + size / 2}" cy="{y + size / 2}" r="{size / 2}" fill="#26A5E4"/>'
            f'<g transform="translate({x} {y}) scale({s:.4f})"><path d="M5.4 11.7l11.2-4.4c.5-.2 1 .1.8.9l-1.9 9c-.1.6-.5.8-1 .5l-2.9-2.1-1.4 1.3c-.2.2-.3.3-.6.3l.2-2.9 5.3-4.8c.2-.2 0-.3-.3-.1l-6.6 4.1-2.8-.9c-.6-.2-.6-.6.1-.9z" fill="#fff"/></g>')


def icon_tile(x, y, ic, size=72, tile=NAVY_TILE):
    col = BLUE if tile == BLUE_TINT else '#fff'
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="{tile}"/></g>' +
            icon(ic, x + size * .25, y + size * .25, size * .5, col, 2.1))


def course_page(x, y, w, h):
    """Illustrative course page on the educator's own domain."""
    out = white_panel(x, y, w, h, 26, big=True)
    out += f'<rect x="{x + 22}" y="{y + 20}" width="{w - 44}" height="40" rx="20" fill="#F1F3F7"/>'
    out += icon('globe', x + 36, y + 29, 22, MUTED, 2) + text(x + 68, y + 47, 'youracademy.in/neet-biology', 18, INK, 500, font=F_MONO)
    out += f'<rect x="{x + 22}" y="{y + 80}" width="{w - 44}" height="{h * .34}" rx="16" fill="{BLUE_TINT}"/>'
    out += f'<circle cx="{x + w / 2}" cy="{y + 80 + h * .17}" r="30" fill="{BLUE}"/>' + f'<path d="M{x + w / 2 - 9} {y + 80 + h * .17 - 14} l24 14 -24 14z" fill="#fff"/>'
    ty = y + 100 + h * .34
    out += text(x + 26, ty + 26, 'NEET Biology: 90-day course', 28, INK, 800, font=F_HEAD, ls=-0.8)
    out += text(x + 26, ty + 60, 'Hindi + English · recorded + live · test series', 18, MUTED)
    out += check_row(x + 26, ty + 108, 'First lesson free', 20) + check_row(x + 26, ty + 150, 'Weekly tests with rank', 20)
    out += f'<rect x="{x + 26}" y="{ty + 180}" width="{w - 52}" height="60" rx="18" fill="{BLUE}"/>'
    out += text(x + w / 2, ty + 218, 'Enrol · pay by UPI or card', 22, '#fff', 700, 'middle', F_HEAD)
    return out


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Get students', 'without *paid ads.*'], 76)
b += lines(84, 458, ['9 organic ways for educators, and a weekly routine'], 27, MUTED)
b += check_row(84, 556, 'YouTube, Instagram, WhatsApp, Telegram', 26)
b += check_row(84, 616, 'A free class that leads to a paid course', 26)
b += check_row(84, 676, 'Every link ends on your own course page', 26)
b += course_page(990, 150, 520, 600)
for i, fn in enumerate([logo_youtube, logo_instagram, logo_whatsapp, logo_telegram, logo_google]):
    yy = 170 + i * 112
    b += logo_tile(860, yy, fn, 80)
    b += arrow(f'M946 {yy + 40} L 978 {yy + 40}', BLUE, 4)
b += text(860, 800, 'Illustrative course page · Logos belong to their owners', 15, MUTED)
save('cover', svg(1600, 900, b, 'How to get students without paid ads: free channels pointing to an educator course page'))

# 2. channel map ------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['9 free ways to *get students*'], 54)
b += lines(62, 150, ['Each channel does one job: send people to your course page'], 22)
cards = [('YouTube', 'Search + Shorts', ('logo', logo_youtube)),
         ('Instagram', 'Reels + carousels', ('logo', logo_instagram)),
         ('WhatsApp', 'Channel, opt-in', ('logo', logo_whatsapp)),
         ('Telegram', 'Channel + group', ('logo', logo_telegram)),
         ('Free class', 'Lesson or live', ('icon', 'video')),
         ('SEO + blog', 'Course pages', ('logo', logo_google)),
         ('Google Maps', 'Business Profile', ('icon', 'pin')),
         ('Referrals', 'Students + collabs', ('icon', 'users')),
         ('Quora, Reddit', 'Helpful answers', ('icon', 'message'))]
for i, (t, s, (kind, val)) in enumerate(cards):
    col, row = i % 3, i // 3
    x, y = 60 + col * 380, 200 + row * 166
    b += white_panel(x, y, 340, 138, 24)
    b += logo_tile(x + 20, y + 33, val, 72) if kind == 'logo' else icon_tile(x + 20, y + 33, val, 72)
    b += text(x + 112, y + 64, t, 26, INK, 800, font=F_HEAD, ls=-0.7)
    b += text(x + 112, y + 96, s, 19, MUTED)
    b += num_badge(x + 322, y + 18, i + 1, 18)
for x in (230, 610, 990):
    b += arrow(f'M{x} 708 L {x} 742', BLUE, 4)
b += f'<g filter="url(#shB)"><rect x="60" y="756" width="1100" height="104" rx="28" fill="{BLUE}"/></g>'
b += icon('globe', 96, 786, 44, '#fff', 2.1)
b += text(162, 802, 'Your course page on your own domain', 30, '#fff', 800, font=F_HEAD, ls=-0.8)
b += text(162, 834, 'free lesson → free class → paid course', 20, '#fff', 500, opacity=.85)
b += text(60, 930, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('channel-map', svg(W, H, b, 'Nine free ways to get students online: YouTube, Instagram, WhatsApp, Telegram, free class, SEO and blog, Google Business Profile, referrals, Quora and Reddit, all pointing to a course page'))

# 3. YouTube flow -----------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['From a YouTube video', 'to *a paid seat*'], 54)
steps = [('Search-led video', 'The question students type', ('logo', logo_youtube)),
         ('Pinned comment', 'One link, with a UTM tag', ('icon', 'link')),
         ('Free lesson', 'On your course page', ('icon', 'play')),
         ('Enrol', 'UPI or card checkout', ('icon', 'card'))]
for i, (t, s, (kind, val)) in enumerate(steps):
    y = 230 + i * 150
    b += white_panel(60, y, 500, 118, 24)
    b += logo_tile(80, y + 23, val, 72) if kind == 'logo' else icon_tile(80, y + 23, val, 72, BLUE if i == 3 else NAVY_TILE)
    b += text(176, y + 54, t, 27, INK, 800, font=F_HEAD, ls=-0.7)
    b += text(176, y + 86, s, 19, MUTED)
    b += num_badge(540, y + 16, i + 1, 18)
    if i < 3:
        b += arrow(f'M310 {y + 121} L 310 {y + 131}', BLUE, 4)
b += laptop(640, 236, 520, 'studio-courses.jpg')
b += text(640, 600, 'Studio preview · sample data', 15, MUTED)
b += white_panel(620, 640, 560, 196, 22)
b += f'<circle cx="660" cy="684" r="20" fill="{BLUE}"/>' + text(660, 691, 'Y', 18, '#fff', 700, 'middle')
b += text(694, 678, 'Your Academy', 19, INK, 700) + text(842, 678, '· Pinned', 17, MUTED)
b += text(694, 710, 'Free notes + first lesson of the full course:', 18, INK)
b += text(694, 742, 'youracademy.in/neet-biology', 18, '#065FD4', 500, font=F_MONO)
b += text(694, 768, '?utm_source=youtube&utm_medium=social', 15, '#065FD4', 500, font=F_MONO)
b += text(694, 808, 'Illustrative pinned comment', 15, MUTED)
b += text(60, 900, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('youtube-flow', svg(W, H, b, 'From a YouTube video to a paid student: search-led video, pinned comment with a tagged link, free lesson on the course page, enrolment'))

# 4. WhatsApp do / don't ------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Spam that gets', 'you *blocked.*'], 54)
for i, t in enumerate(['Adding numbers unasked', 'Bought contact lists', 'Ten forwards a day', 'No way to leave', 'Fake last-seat panic']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 500, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 790, ['Students leave.', 'Reports follow.'], 38, INK, -6)
b += logo_tile(1080, 40, logo_whatsapp, 80)
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['A join link they choose to tap', 'Channel for one-way updates', '2–4 useful posts a week', 'Stop on the first request', 'Real dates, real seats']):
    b += check_row(656, 400 + i * 74, t, 25)
b += text(656, 790, 'Summary of the WhatsApp Business', 16, MUTED)
b += text(656, 816, 'Messaging Policy, checked Nov 2026', 16, MUTED)
b += text(656, 842, 'Logos belong to their owners.', 16, MUTED)
save('whatsapp-do-dont', svg(W, H, b, 'WhatsApp for educators: spam that gets you blocked versus opt-in channel habits', ('split', 600)))

# 5. free-to-paid ladder ------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['The free-to-paid *ladder*'], 54)
b += lines(62, 150, ['Each free step earns the right to offer the next one'], 22)
rungs = [('Free video', 'YouTube, reels', 'video', 'Free', '2,000 viewers'),
         ('Free notes', 'Via a lead form', 'file', 'Free', '300 sign-ups'),
         ('Free live class', 'Q&A at the end', 'users', 'Free', '80 attend'),
         ('Paid course', 'Honest early-bird', 'card', '₹', '12 enrol'),
         ('Next course', 'Or a test series', 'trophy', '₹', 'Repeat buyers')]
base = 820
for i, (t, s, ic, price, num) in enumerate(rungs):
    x = 60 + i * 222
    top = 300 + (4 - i) * 80
    hgt = base - top
    paid = price == '₹'
    b += f'<g filter="url(#sh)"><rect x="{x}" y="{top}" width="204" height="{hgt}" rx="22" fill="{BLUE if paid else "#fff"}"/></g>'
    tc, sc = ('#fff', '#fff') if paid else (INK, MUTED)
    b += f'<rect x="{x + 20}" y="{top + 22}" width="56" height="56" rx="16" fill="{"#fff" if paid else NAVY_TILE}"/>'
    b += icon(ic, x + 34, top + 36, 28, BLUE if paid else '#fff', 2)
    b += f'<rect x="{x + 124}" y="{top + 32}" width="60" height="34" rx="17" fill="{"#fff" if paid else BLUE_TINT}"/>'
    b += text(x + 154, top + 56, price, 18, BLUE, 700, 'middle', F_HEAD)
    b += text(x + 20, top + 116, t, 23, tc, 800, font=F_HEAD, ls=-0.6)
    b += text(x + 20, top + 144, s, 17, sc, opacity=.9 if paid else 1)
    b += text(x + 102, base + 40, num, 18, INK, 600, 'middle')
b += arrow('M120 250 C 420 170, 820 165, 1110 225', BLUE, 4)
b += text(60, 912, 'Illustrative numbers for one launch, not a benchmark or a promise.', 18, MUTED)
b += signature(W, H)
save('free-paid-ladder', svg(W, H, b, 'Free to paid ladder for educators: free video, free notes through a lead form, free live class, paid course with an honest early-bird price, next course'))

# 6. weekly routine --------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['A weekly *organic routine*'], 54)
b += lines(62, 150, ['About 8–10 hours a week. Illustrative plan; move days to fit your timetable.'], 22)
b += white_panel(60, 196, 1100, 760, 28)
rows = [('Mon', 'Record one search-led YouTube lesson', '2 h', [logo_youtube]),
        ('Tue', 'Cut 3 Shorts / reels from it', '1.5 h', [logo_youtube, logo_instagram]),
        ('Wed', 'One carousel + one channel post', '1 h', [logo_instagram, logo_whatsapp]),
        ('Thu', 'Answer 5 questions on Quora or Reddit', '1 h', []),
        ('Fri', 'Free live class or doubt session', '1.5 h', [logo_telegram]),
        ('Sat', 'Follow up leads, ask for referrals', '1 h', [logo_whatsapp]),
        ('Sun', 'Check tagged links, plan next week', '0.5 h', [logo_google])]
for i, (d, t, hrs, logos) in enumerate(rows):
    y = 226 + i * 104
    if i % 2 == 0:
        b += f'<rect x="80" y="{y}" width="1060" height="96" rx="18" fill="#F6F7FC"/>'
    b += f'<rect x="100" y="{y + 22}" width="86" height="52" rx="14" fill="{NAVY_TILE}"/>' + text(143, y + 56, d, 22, '#fff', 700, 'middle', F_HEAD)
    b += text(214, y + 58, t, 25, INK, 600)
    b += text(940, y + 58, hrs, 22, BLUE, 700, 'end', F_HEAD)
    for k, fn in enumerate(logos):
        b += fn(984 + k * 66, y + 26, 44) if fn is not logo_youtube else fn(978 + k * 66, y + 32, 34)
    if not logos:
        b += icon('message', 990, y + 30, 36, MUTED, 2)
b += text(60, 990, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('weekly-routine', svg(W, H, b, 'Weekly organic marketing routine for an educator: YouTube lesson, Shorts and reels, carousel and channel post, Quora answers, free live class, follow-ups and referrals, review'))

# 7. playbook steps ---------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['The playbook in *7 steps*'], 54)
b += lines(62, 150, ['Steps 1–2 once; steps 3–7 every week'], 22)
ps = [('Pick one exam or skill', 'And the questions students type', 'search'),
      ('Course page + free lesson', 'On your own domain', 'globe'),
      ('One YouTube lesson a week', 'Pinned link to the course', 'video'),
      ('Cut reels and carousels', 'Same lesson, more reach', 'layers'),
      ('Opt-in channel', 'WhatsApp or Telegram', 'message'),
      ('Free live class', 'Ends with a clear offer', 'users'),
      ('Follow up and measure', 'Referrals, tagged links', 'chart')]
for i, (t, s, ic) in enumerate(ps):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 150
    b += pill_card(x, y, 540, t, s, ic, h=118, tile=NAVY_TILE if i < 2 else BLUE_TINT, title_size=25)
    b += num_badge(x + 518, y + 4, i + 1, 20)
b += signature(W, H)
save('playbook-steps', svg(W, H, b, 'Organic growth playbook for educators in 7 steps'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 700
b = headline(60, 100, ['Mistakes that *waste* free reach'], 52)
b += lines(62, 150, ['Each one has a simple fix'], 22)
ms = [('Viral, not searchable', 'Teach what students search for'),
      ('No link to a course page', 'Pin one link on every video'),
      ('Free with no next step', 'Every free class ends in an offer'),
      ('Spamming groups', 'An opt-in channel only'),
      ('Fake urgency', 'Real dates and real seat limits'),
      ('Nothing measured', 'A UTM tag on every link')]
for i, (t, s) in enumerate(ms):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 150
    b += pill_card(x, y, 540, t, 'Fix: ' + s, 'x', h=118, tile=RED, title_size=25)
b += signature(W, H)
save('mistakes', svg(W, H, b, 'Organic marketing mistakes educators make and how to fix them'))
