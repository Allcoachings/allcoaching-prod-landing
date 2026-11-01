"""Graphics for /blog/google-business-profile-for-coaching-centre.

Run:  python .claude/skills/academy-guide-blog/graphics/google-business-profile-for-coaching-centre.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/google-business-profile-for-coaching-centre

All Google listings drawn here are illustrative, for a fictional "Your Academy" centre.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'google-business-profile-for-coaching-centre')
os.makedirs(OUT, exist_ok=True)
SHOT_DOMAIN = os.path.join(ROOT, 'landing', 'img', 'studio-domain.webp')       # real studio Own branding > Domain (sample educator)
SHOT_MKT = os.path.join(ROOT, 'landing', 'img', 'studio-marketing.webp')       # real studio Marketing tools (sample educator)

ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
ICONS['nav'] = '<path d="M3 11l18-8-8 18-2-8z"/>'
ICONS['share'] = '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/>'
ICONS['camera'] = '<path d="M4 7h4l2-3h4l2 3h4v12H4z"/><circle cx="12" cy="13" r="3.5"/>'
ICONS['edit'] = '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def stars(x, y, n=5, size=20, fill='#FBBC05'):
    out = ''
    for i in range(n):
        cx = x + i * (size + 4) + size / 2
        cy = y
        pts = []
        import math
        for k in range(10):
            r = size / 2 if k % 2 == 0 else size / 4.6
            a = -math.pi / 2 + k * math.pi / 5
            pts.append(f'{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}')
        out += f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'
    return out


def map_strip(x, y, w, h, r=24, pin=True):
    cid = f'mp{x}{y}'
    roads = (f'<path d="M{x} {y + h * .62} C {x + w * .3} {y + h * .5}, {x + w * .6} {y + h * .78}, {x + w} {y + h * .58}" stroke="#fff" stroke-width="14" fill="none"/>'
             f'<path d="M{x + w * .28} {y} L {x + w * .38} {y + h}" stroke="#fff" stroke-width="10" fill="none"/>'
             f'<path d="M{x + w * .72} {y} L {x + w * .66} {y + h}" stroke="#fff" stroke-width="8" fill="none"/>'
             f'<rect x="{x + w * .05}" y="{y + h * .12}" width="{w * .16}" height="{h * .28}" rx="8" fill="#CDE8D3"/>'
             f'<rect x="{x + w * .8}" y="{y + h * .7}" width="{w * .14}" height="{h * .22}" rx="8" fill="#CDE8D3"/>'
             f'<rect x="{x + w * .44}" y="{y + h * .1}" width="{w * .18}" height="{h * .3}" rx="8" fill="#DDE3EE"/>')
    out = (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath></defs>'
           f'<g clip-path="url(#{cid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#EAEEF3"/>{roads}</g>')
    if pin:
        px, py = x + w * .52, y + h * .52
        out += (f'<path d="M{px} {py + 30} C {px - 6} {py + 16}, {px - 22} {py + 4}, {px - 22} {py - 12} a 22 22 0 0 1 44 0 C {px + 22} {py + 4}, {px + 6} {py + 16}, {px} {py + 30} z" fill="#EA4335"/>'
                f'<circle cx="{px}" cy="{py - 12}" r="8" fill="#A50E0E"/>')
    return out


def action(cx, y, label, ic, primary=False):
    fill = BLUE if primary else '#fff'
    stroke = BLUE if primary else '#DADCE0'
    col = '#fff' if primary else BLUE
    return (f'<circle cx="{cx}" cy="{y}" r="28" fill="{fill}" stroke="{stroke}" stroke-width="2"/>' +
            icon(ic, cx - 13, y - 13, 26, col, 2.1) + text(cx, y + 56, label, 17, '#1A73E8' if not primary else BLUE, 600, 'middle'))


def gbp_card(x, y, w, compact=False):
    """Illustrative Google Business Profile card for the fictional 'Your Academy' centre. Height ~ 560 (compact 470)."""
    mh = 150 if compact else 190
    out = white_panel(x, y, w, (430 if compact else 500), 26, big=True)
    out += map_strip(x + 14, y + 14, w - 28, mh, 18)
    yy = y + mh + 66
    out += text(x + 32, yy, 'Your Academy', 34, '#202124', 700, font=F_HEAD, ls=-0.8)
    out += text(x + 32, yy + 38, '4.8', 19, '#202124', 600) + stars(x + 70, yy + 31, 5, 18) + text(x + 192, yy + 38, '(126)', 18, '#70757A')
    out += text(x + 32, yy + 70, 'Coaching · Boring Road, Patna', 19, '#70757A')
    out += text(x + 32, yy + 102, 'Open', 19, '#188038', 600) + text(x + 84, yy + 102, '· Office closes 7 pm', 19, '#70757A')
    ay = yy + 158
    n = 4
    gap = (w - 64) / n
    for i, (lab, ic) in enumerate([('Call', 'phone'), ('Directions', 'nav'), ('Website', 'globe'), ('Share', 'share')]):
        out += action(x + 32 + gap * i + gap / 2, ay, lab, ic, primary=(lab == 'Website'))
    return out


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Put your coaching', 'centre on *Google Maps.*'], 68)
b += lines(84, 450, ['Google Business Profile: a local SEO guide for educators'], 27, MUTED)
b += check_row(84, 548, 'Eligibility, setup and verification', 26)
b += check_row(84, 608, 'Real name, right category, real reviews', 26)
b += check_row(84, 668, 'Linked to your own academy website', 26)
b += f'<rect x="900" y="118" width="590" height="66" rx="33" fill="#fff" stroke="#DADCE0" stroke-width="2"/>' + logo_google(922, 134, 34) + text(974, 160, 'neet coaching near me', 25, '#202124')
b += gbp_card(900, 210, 590)
b += text(900, 752, 'Illustrative listing for a fictional centre · Logos belong to their owners', 15, MUTED)
save('cover', svg(1600, 900, b, 'Google Business Profile for a coaching centre: an illustrative Google Maps listing for a fictional academy'))

# 2. local result ----------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['What students see for *"near me"*'], 52)
b += lines(62, 150, ['The map listing comes from your Google Business Profile, not your website'], 22)
b += f'<rect x="60" y="196" width="620" height="66" rx="33" fill="#fff" stroke="#DADCE0" stroke-width="2"/>' + logo_google(82, 212, 34) + text(134, 238, 'neet coaching near me', 25, '#202124')
b += gbp_card(60, 290, 620)
callouts = [('Name, rating, category', 'The real-world name and reviews', 'star'),
            ('Open now', 'Your office hours', 'clock'),
            ('Call and Directions', 'The two taps that bring walk-ins', 'phone'),
            ('Website', 'Sends them to your own academy', 'globe')]
for i, (t, s, ic) in enumerate(callouts):
    b += pill_card(720, 290 + i * 132, 440, t, s, ic, h=108, tile=BLUE if t == 'Website' else NAVY_TILE, title_size=23)
b += text(60, H - 28, 'Illustrative listing for a fictional centre. Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('local-result', svg(W, H, b, 'Illustrative Google Maps local result for a coaching centre with rating, hours, call, directions and website buttons'))

# 3. setup steps -----------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Set it up in *8 steps*'], 54)
b += lines(62, 150, ['Steps 1–5 create the profile; 6–8 keep it working'], 22)
steps = [('Check eligibility', 'Students visit you in person', 'check'),
         ('Real-world name', 'As on your signboard', 'type'),
         ('Primary category', 'The most specific one', 'tag'),
         ('Address, phone, website', 'Or a service area', 'pin'),
         ('Verify', 'The method Google offers', 'shield'),
         ('Hours, photos, description', 'Office hours, real photos', 'camera'),
         ('Courses with fees', 'Same as your website', 'book'),
         ('Reviews and updates', 'Every batch, every month', 'star')]
for i, (t, s, ic) in enumerate(steps):
    col, row = i % 2, i // 2
    x, y = 60 + col * 560, 196 + row * 150
    b += pill_card(x, y, 540, t, s, ic, h=118, tile=NAVY_TILE if i < 5 else BLUE_TINT, title_size=25)
    b += num_badge(x + 518, y + 4, i + 1, 20)
b += signature(W, H)
save('setup-steps', svg(W, H, b, 'How to set up a Google Business Profile for a coaching centre in 8 steps'))

# 4. profile anatomy --------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['Anatomy of a *complete profile*'], 52)
b += lines(62, 150, ['Eight parts students read before they call'], 22)
px, pw = 60, 560
b += white_panel(px, 196, pw, 780, 26, big=True)
b += map_strip(px + 14, 210, pw - 28, 120, 18)
b += text(px + 32, 384, 'Your Academy', 32, '#202124', 700, font=F_HEAD, ls=-0.8)
b += text(px + 32, 416, 'Test preparation · Boring Road, Patna', 18, '#70757A')
b += text(px + 32, 452, 'Open', 18, '#188038', 600) + text(px + 80, 452, '· Office 9 am – 7 pm', 18, '#70757A')
b += f'<rect x="{px + 32}" y="474" width="230" height="44" rx="22" fill="#fff" stroke="#DADCE0" stroke-width="2"/>' + icon('phone', px + 48, 484, 22, BLUE, 2) + text(px + 80, 503, 'Call', 18, '#1A73E8', 600)
b += f'<rect x="{px + 276}" y="474" width="250" height="44" rx="22" fill="{BLUE}"/>' + icon('globe', px + 292, 484, 22, '#fff', 2) + text(px + 324, 503, 'youracademy.in', 18, '#fff', 600)
for k in range(3):
    b += f'<rect x="{px + 32 + k * 168}" y="540" width="156" height="104" rx="14" fill="#E3E7F0"/>' + icon('image', px + 32 + k * 168 + 62, 574, 32, '#9AA3B8', 2)
b += text(px + 32, 680, 'Courses', 20, '#202124', 700)
for k, (c, p) in enumerate([('NEET 2027 classroom', '₹ fee'), ('Class 10 maths, Hindi', '₹ fee'), ('Online test series', '₹ fee')]):
    yy = 712 + k * 36
    b += text(px + 32, yy, c, 18, '#3C4043') + text(px + pw - 40, yy, p, 18, '#70757A', anchor='end')
b += text(px + 32, 840, '4.8', 18, '#202124', 600) + stars(px + 66, 834, 5, 17) + text(px + 186, 840, 'Reviews, with replies', 18, '#70757A')
b += f'<rect x="{px + 32}" y="866" width="{pw - 64}" height="86" rx="14" fill="#F1F3F4"/>' + text(px + 52, 900, 'Update: new NEET batch from 5 Jan', 18, '#202124', 600) + text(px + 52, 930, 'Learn more → course page', 17, '#1A73E8')
# numbered markers on the card
marks = [(384, 1), (416, 2), (452, 3), (496, 4), (592, 5), (712, 6), (834, 7), (906, 8)]
for yy, n in marks:
    b += num_badge(px + pw + 2, yy - 6, n, 19)
labels = [('Real-world name', 'No keywords or taglines'),
          ('Primary category', 'Most specific match'),
          ('Office hours', 'When staff receive visitors'),
          ('Phone and website', 'Your own domain'),
          ('Real photos', 'Signboard, classroom, reception'),
          ('Courses with fees', 'Same as your website'),
          ('Reviews with replies', 'Genuine, never rewarded'),
          ('Updates', 'Each linked to a course page')]
for i, (t, s) in enumerate(labels):
    y = 214 + i * 96
    b += num_badge(694, y + 20, i + 1, 20)
    b += text(728, y + 28, t, 25, INK, 800, font=F_HEAD, ls=-0.7)
    b += text(728, y + 58, s, 19, MUTED)
b += text(60, H - 28, 'Illustrative profile for a fictional centre. Sections differ by category and country.', 16, MUTED)
b += signature(W, H)
save('profile-anatomy', svg(W, H, b, 'Anatomy of a Google Business Profile for a coaching centre with eight numbered parts'))

# 5. reviews do / don't ------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Reviews that', 'get removed.'], 54)
for i, t in enumerate(['Fee discount for 5 stars', 'Free notes for a review', 'Asking only toppers', 'Staff write reviews', '"Review it now, here"']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 510, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 790, ['Not worth', 'the risk.'], 40, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Ask every student and parent', 'Same link, same moment', 'Let them review at home', 'Reply to every review', 'Keep personal details private']):
    b += check_row(656, 400 + i * 74, t, 25)
b += text(656, 820, "Summary of Google's review policy, checked Nov 2026", 16, MUTED)
save('reviews-do-dont', svg(W, H, b, "Getting genuine Google reviews for a coaching centre: what Google's review policy allows and what it does not", ('split', 600)))

# 6. tracking ---------------------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Measure it in *two places*'], 54)
b += lines(62, 150, ['The profile shows who found you; your website shows who enrolled'], 22)
b += white_panel(60, 196, 520, 600, 28)
b += logo_tile(92, 226, logo_google, 64)
b += text(176, 252, 'Profile performance', 24, INK, 800, font=F_HEAD, ls=-0.6)
b += text(176, 280, 'Illustrative month', 17, MUTED)
for i, (lab, val, ic) in enumerate([('Searches', '1,240', 'search'), ('Profile views', '860', 'users'),
                                    ('Calls', '42', 'phone'), ('Directions', '57', 'nav'), ('Website clicks', '96', 'globe')]):
    y = 330 + i * 90
    b += f'<rect x="92" y="{y}" width="56" height="56" rx="16" fill="{BLUE_TINT}"/>' + icon(ic, 106, y + 14, 28, BLUE, 2)
    b += text(168, y + 36, lab, 22, INK, 600)
    b += text(548, y + 38, val, 28, INK, 800, 'end', F_HEAD, -0.8)
b += arrow('M594 470 L 648 470', BLUE, 5)
b += text(690, 806, 'Website link tagged ?utm_source=google', 16, MUTED, 600, font=F_MONO)
b += text(680, 230, 'Your academy analytics', 24, INK, 800, font=F_HEAD, ls=-0.6)
b += text(680, 258, 'Studio preview · sample data', 15, MUTED)
b += laptop(690, 290, 460, SHOT_MKT)
for k, (t, ic) in enumerate([('Visits', 'globe'), ('Sign-ups', 'users'), ('Purchases', 'card')]):
    cx = 700 + k * 160 + 70
    b += feature_tile(cx, 630, t, ic, None, 74)
b += text(60, 850, 'Illustrative numbers, not real results. Performance metrics shown depend on your business.', 17, MUTED)
b += text(60, 878, 'Source: Google Business Profile Help, checked November 2026. Logos belong to their owners.', 17, MUTED)
b += signature(W, H)
save('tracking', svg(W, H, b, 'Tracking a Google Business Profile: searches, views, calls, directions and website clicks, and visits, sign-ups and purchases on your academy website'))

# 7. hybrid flow ------------------------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['From the map to *your academy*'], 54)
b += lines(62, 150, ['Your profile brings local students; your academy keeps teaching them'], 22)
nodes = [('Google profile', 'On Search and Maps', 'pin', 60),
         ('Your centre', 'Classroom batches', 'home', 440),
         ('Your academy', 'Own domain and app', 'globe', 820)]
for t, s, ic, x in nodes:
    b += pill_card(x, 200, 340, t, s, ic, h=110, tile=BLUE if t == 'Your academy' else NAVY_TILE, title_size=26)
b += arrow('M404 255 L 432 255', BLUE, 4) + arrow('M784 255 L 812 255', BLUE, 4)
b += logo_tile(330, 176, logo_google, 50)
b += laptop(110, 380, 560, SHOT_DOMAIN)
b += text(110, 770, 'Studio preview · sample data', 15, MUTED)
for i, (t, s, ic) in enumerate([('Hybrid batches', 'Classroom + recorded lectures', 'video'),
                                ('Test series online', 'Rank and percentile', 'trophy'),
                                ('Online-only courses', 'Students in other cities', 'users')]):
    b += pill_card(760, 380 + i * 132, 400, t, s, ic, h=108, tile=BLUE_TINT, title_size=24)
b += text(60, 860, 'Link each course on your profile to its course page on your own domain.', 21, INK, 600)
b += text(60, 892, 'Logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('hybrid-flow', svg(W, H, b, 'Connecting an offline coaching centre to an online academy: Google Business Profile, classroom, and an online academy with recorded lectures, test series and hybrid batches'))

# 8. checklist --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Your profile *checklist*'], 54)
b += lines(62, 150, ['Run it once at setup, then every month'], 22)
b += white_panel(60, 196, 1100, 620, 28)
items = ['Students visit the centre in person', 'Name exactly as on the signboard', 'Most specific primary category',
         'Profile verified', 'Office hours, festival hours updated', 'Real photos: board, classroom, desk',
         'Courses listed with the same fees', 'Website on your own domain, tagged',
         'Reviews asked for and answered', 'Calls, directions, clicks noted monthly']
for i, t in enumerate(items):
    col, row = i % 2, i // 2
    b += check_row(100 + col * 540, 266 + row * 112, t, 22)
b += signature(W, H)
save('checklist', svg(W, H, b, 'Google Business Profile checklist for coaching centres'))
