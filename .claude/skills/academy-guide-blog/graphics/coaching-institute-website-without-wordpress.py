"""Graphics for /blog/coaching-institute-website-without-wordpress.

Run:  python .claude/skills/academy-guide-blog/graphics/coaching-institute-website-without-wordpress.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/coaching-institute-website-without-wordpress
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa
from brand_graphics import _img_data, _uid  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
SLUG = 'coaching-institute-website-without-wordpress'
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

THEMES = os.path.join(ROOT, 'landing', 'img', 'studio-themes.webp')
TEMPLATES = os.path.join(ROOT, 'landing', 'img', 'studio-templates.webp')
SHOW = os.path.join(ROOT, 'assets', 'showcase')


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def browser(x, y, w, shot, url, ratio=0.625):
    """Browser window (chrome bar + URL pill) showing a real screenshot."""
    _uid[0] += 1
    cid = f'bw{_uid[0]}'
    bar = 38
    ih = w * ratio
    return (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y + bar}" width="{w}" height="{ih}" rx="0"/></clipPath></defs>'
            f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{bar + ih}" rx="16" fill="#fff"/></g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{bar}" rx="16" fill="#F1F3F6"/><rect x="{x}" y="{y + bar - 16}" width="{w}" height="16" fill="#F1F3F6"/>'
            + ''.join(f'<circle cx="{x + 22 + k * 18}" cy="{y + bar / 2}" r="5.5" fill="{c}"/>' for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']))
            + f'<rect x="{x + 84}" y="{y + 8}" width="{min(w - 110, 300)}" height="22" rx="11" fill="#fff"/>'
            + text(x + 98, y + 24, url, 14, INK, 500, font=F_MONO)
            + f'<image href="{_img_data(shot)}" x="{x}" y="{y + bar}" width="{w}" height="{ih}" preserveAspectRatio="xMidYMin slice" clip-path="url(#{cid})"/>'
            + f'<rect x="{x}" y="{y}" width="{w}" height="{bar + ih}" rx="16" fill="none" stroke="{LINE}" stroke-width="1.5"/>')


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Your coaching', 'website. *Without*', '*WordPress.*'], 80)
b += lines(84, 560, ['No hosting, plugins or developer.', 'One studio, your own domain.'], 28, MUTED, 1.35)
b += check_row(84, 690, 'Theme, pages and courses', 26)
b += check_row(84, 750, 'Course pages with checkout', 26)
b += check_row(84, 810, 'Your own domain and app', 26)
b += laptop(820, 150, 700, THEMES)
b += text(820, 700, 'AllCoaching studio · Themes · sample data', 16, MUTED)
b += pill_card(1080, 730, 420, 'youracademy.in', 'Your domain, free to connect', 'globe')
save('cover', svg(1600, 900, b, 'A coaching institute website built without WordPress: the AllCoaching studio themes screen on a laptop'))

# 2. WordPress stack vs one studio ---------------------------------------------
W, H = 1220, 1040
b = headline(56, 104, ['Building it the', 'WordPress way?'], 54)
jobs = ['Hosting to renew', 'Theme + page builder', 'LMS plugin', 'Payment plugin', 'Video hosting',
        'Security + backups', 'Core + plugin updates', 'Student app: separate']
for i, t in enumerate(jobs):
    b += tape(40 + (i % 2) * 22, 200 + i * 82, 500, t, -1.4 if i % 2 else 1.0, 28)
b += hand(300, 930, ['Who fixes it', 'at 11 pm?'], 40, INK, -6) + arrow('M286 940 C 236 960, 196 940, 176 900', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['One studio.', '*Everything in it.*'], 52)
done = ['Hosting, updates, security handled', 'Themes and a page builder', 'Course pages with checkout',
        'UPI and card payments', 'Videos and live classes', 'Your domain, free to connect', 'Your own Android app']
for i, t in enumerate(done):
    b += check_row(656, 370 + i * 70, t, 23)
b += text(656, 880, 'One login. One plan. Nothing to patch.', 21, MUTED, 500)
b += signature(W, H)
save('wordpress-stack-vs-studio', svg(W, H, b, 'A coaching website on WordPress means hosting, theme, LMS plugin, payment plugin, video hosting, security, updates and a separate app; a hosted academy studio has all of it in one login', ('split', 600)))

# 3. pages a coaching website needs ----------------------------------------------
W, H = 1220, 1100
b = headline(60, 92, ['The 7 pages a *coaching website* needs'], 46)
ox, oy, pw = 60, 140, 660
px = ox + 30
b += white_panel(ox, oy, pw, 890, 26, big=True)
b += f'<rect x="{ox}" y="{oy}" width="{pw}" height="58" rx="26" fill="#F1F3F6"/><rect x="{ox}" y="{oy + 30}" width="{pw}" height="28" fill="#F1F3F6"/>'
b += ''.join(f'<circle cx="{ox + 30 + k * 22}" cy="{oy + 29}" r="7" fill="{c}"/>' for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']))
b += f'<rect x="{ox + 100}" y="{oy + 13}" width="300" height="32" rx="16" fill="#fff"/>' + text(ox + 120, oy + 35, 'youracademy.in', 16, INK)
# nav
b += f'<circle cx="{px + 16}" cy="{oy + 92}" r="16" fill="{BLUE}"/>' + text(px + 16, oy + 98, 'Y', 17, '#fff', 800, 'middle', F_HEAD)
b += text(px + 42, oy + 99, 'Your Academy', 19, INK, 700, font=F_HEAD)
b += ''.join(text(px + dx, oy + 98, t, 15, MUTED) for dx, t in [(336, 'Courses'), (420, 'About'), (488, 'Free'), (536, 'Contact')])
# 1 hero
b += f'<rect x="{px}" y="{oy + 128}" width="600" height="150" rx="16" fill="#F4F6FF"/>'
b += text(px + 24, oy + 178, 'NEET Biology in Hindi', 30, INK, 800, font=F_HEAD, ls=-1.1)
b += text(px + 24, oy + 208, 'Class 11 and 12 · live and recorded · by Your Name', 16, MUTED)
b += f'<rect x="{px + 24}" y="{oy + 226}" width="150" height="38" rx="12" fill="{BLUE}"/>' + text(px + 99, oy + 251, 'See courses', 16, '#fff', 700, 'middle', F_HEAD)
# 2 courses
b += text(px, oy + 318, 'Courses', 19, INK, 700, font=F_HEAD)
for k, (n, p) in enumerate([('Full course', '₹4,999'), ('Test series', '₹1,499'), ('Crash course', '₹999')]):
    cx = px + k * 205
    b += f'<rect x="{cx}" y="{oy + 334}" width="190" height="100" rx="14" fill="#fff" stroke="{LINE}" stroke-width="2"/>'
    b += text(cx + 16, oy + 368, n, 16, INK, 600) + text(cx + 16, oy + 410, p, 24, INK, 800, font=F_HEAD)
# 3 about
b += f'<circle cx="{px + 38}" cy="{oy + 500}" r="34" fill="#C9D3FF"/>' + icon('users', px + 22, oy + 484, 32, BLUE, 2)
b += text(px + 92, oy + 494, 'About Your Name', 19, INK, 700, font=F_HEAD) + text(px + 92, oy + 522, '12 years teaching · Hindi medium · your method', 15, MUTED)
# 4 results
b += f'<rect x="{px}" y="{oy + 560}" width="600" height="74" rx="14" fill="#fff" stroke="#A9B3E0" stroke-width="2" stroke-dasharray="7 6"/>'
b += icon('trophy', px + 20, oy + 584, 28, BLUE, 2) + text(px + 62, oy + 604, 'Results: only real ones, with permission', 17, INK, 500)
# 5 free content
for k, (ic, t) in enumerate([('play', 'Free demo lesson'), ('file', 'Free PDF notes')]):
    cx = px + k * 310
    b += f'<rect x="{cx}" y="{oy + 656}" width="290" height="70" rx="14" fill="{BLUE_TINT}"/>' + icon(ic, cx + 18, oy + 677, 28, BLUE, 2) + text(cx + 58, oy + 698, t, 17, INK, 600)
# 6 contact
b += f'<rect x="{px}" y="{oy + 748}" width="600" height="62" rx="14" fill="#F4F6FF"/>' + logo_whatsapp(px + 16, oy + 761, 36)
b += text(px + 66, oy + 785, 'Chat on WhatsApp', 17, INK, 600) + text(px + 584, oy + 785, 'Call · Address · Map', 15, MUTED, anchor='end')
# 7 footer
b += f'<line x1="{px}" y1="{oy + 832}" x2="{px + 600}" y2="{oy + 832}" stroke="{LINE}" stroke-width="2"/>'
b += text(px, oy + 862, 'Privacy  ·  Terms  ·  Refunds  ·  Contact', 15, MUTED)
callouts = [(oy + 200, 'Home', 'who you teach, in one line'),
            (oy + 384, 'Courses with prices', 'one page for each course'),
            (oy + 500, 'About the teacher', 'photo, years, method'),
            (oy + 597, 'Results', 'only if real and permitted'),
            (oy + 691, 'Free content', 'demo lessons, notes'),
            (oy + 779, 'Contact + WhatsApp', 'one tap on a phone'),
            (oy + 857, 'Policies', 'privacy, terms, refunds')]
for n, (cy, t, s) in enumerate(callouts, 1):
    b += f'<path d="M{ox + pw} {cy} H 790" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(812, cy, n) + text(846, cy - 2, t, 22, INK, 700, font=F_HEAD, ls=-0.4) + text(846, cy + 24, s, 17, MUTED)
b += text(60, H - 28, 'Illustrative coaching website. Names and prices are examples, not real data.', 16, MUTED) + signature(W, H)
save('pages-anatomy', svg(W, H, b, 'The seven pages a coaching institute website needs: home, courses with prices, about the teacher, results, free content, contact with WhatsApp and policies'))

# 4. five-step build ---------------------------------------------------------------
W, H = 1220, 780
b = headline(60, 96, ['Build it in *five steps*'], 54) + lines(62, 146, ['The order that works on a hosted academy platform'], 22)
b += f'<line x1="120" y1="214" x2="1100" y2="214" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
steps = [('image', ['Pick a', 'theme'], ['Choose a look', 'that suits your', 'students.']),
         ('type', ['Edit text,', 'colours, logo'], ['Your words,', 'your colours,', 'your photo.']),
         ('book', ['Add your', 'courses'], ['Course pages', 'with SEO and', 'checkout appear.']),
         ('globe', ['Connect', 'your domain'], ['Add two DNS', 'records at your', 'registrar.']),
         ('bolt', ['Test and', 'publish'], ['Check it on a', 'phone, then', 'share one link.'])]
for k, (ic, title, desc) in enumerate(steps):
    x = 60 + k * 222
    b += num_badge(x + 104, 214, k + 1, 22)
    b += white_panel(x, 260, 208, 320, 26)
    b += f'<rect x="{x + 22}" y="284" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon(ic, x + 38, 300, 28, '#fff', 2)
    b += text(x + 22, 398, title[0], 25, INK, 800, font=F_HEAD, ls=-0.9) + text(x + 22, 428, title[1], 25, INK, 800, font=F_HEAD, ls=-0.9)
    b += lines(x + 22, 490, desc, 17, MUTED, 1.45)
b += white_panel(60, 610, 1100, 110, 24)
b += eyebrow(92, 652, 'Then add, when you need them')
for k, t in enumerate(['Ready-made landing pages', 'Page builder: up to 100 pages', 'Blog: up to 300 posts']):
    b += check_row(92 + k * 360, 694, t, 19)
b += text(60, H - 28, 'Limits shown are AllCoaching plan limits. Landing pages: any 6, any 12 or all 16, by plan.', 16, MUTED) + signature(W, H)
save('five-step-build', svg(W, H, b, 'How to build a coaching institute website without WordPress in five steps: pick a theme, edit text, colours and logo, add courses, connect your domain, test and publish'))

# 5. studio themes ---------------------------------------------------------------
W, H = 1220, 800
b = headline(60, 96, ['Pick a theme. *Make it yours.*'], 52)
b += laptop(60, 170, 760, THEMES)
for k, (t, s, ic) in enumerate([('Text', 'Edit any section', 'type'), ('Colours', 'Your brand palette', 'image'),
                                 ('Logo', 'Header and favicon', 'star'), ('Switch', 'Courses stay put', 'layers')]):
    b += pill_card(880, 170 + k * 124, 300, t, s, ic, title_size=26)
b += text(60, 740, 'Studio preview · sample data. The Themes screen in the AllCoaching studio.', 16, MUTED) + signature(W, H)
save('studio-themes', svg(W, H, b, 'The Themes screen in the AllCoaching studio, where an educator picks a website theme and edits text, colours and logo'))

# 6. landing pages, page builder, blog --------------------------------------------------
W, H = 1220, 800
b = headline(60, 96, ['Pages for *admissions and webinars*'], 50)
b += laptop(60, 170, 760, TEMPLATES)
tiles = [('Landing pages', '6 · 12 · 16', ['ready-made pages on', 'Starter, Growth, Pro']),
         ('Page builder', 'Up to 100', ['pages, on every plan']),
         ('Blog', 'Up to 300', ['posts, on every plan'])]
for k, (eb, big, sub) in enumerate(tiles):
    y = 150 + k * 182
    b += white_panel(904, y, 266, 168, 24)
    b += eyebrow(930, y + 40, eb) + text(930, y + 92, big, 40, INK, 800, font=F_HEAD, ls=-1.4)
    b += lines(930, y + 124, sub, 17, MUTED, 1.3)
b += text(60, 740, 'Studio preview · sample data. Ready-made landing pages in the AllCoaching studio.', 16, MUTED) + signature(W, H)
save('landing-templates', svg(W, H, b, 'Ready-made landing pages for webinars, workshops, course sales and admissions in the AllCoaching studio, with a page builder and blog'))

# 7. real academies ------------------------------------------------------------------
W, H = 1220, 1020
b = headline(60, 92, ['Real academies, *their own websites*'], 48) + lines(62, 140, ['Built on AllCoaching, each on its own domain and brand'], 22)
b += browser(60, 190, 640, os.path.join(SHOW, 'bio-desktop.webp'), 'biolessons.in')
b += text(60, 672, 'Biology Lessons', 26, INK, 800, font=F_HEAD, ls=-0.8) + text(60, 702, 'Dr. Subhash Nair · biolessons.in', 18, MUTED)
b += browser(740, 190, 420, os.path.join(SHOW, 'chem-desktop.webp'), 'chempsi.com')
b += text(740, 528, 'CHEMPSI', 24, INK, 800, font=F_HEAD, ls=-0.6) + text(740, 556, 'Anupam Kumar · chempsi.com', 17, MUTED)
b += browser(740, 590, 420, os.path.join(SHOW, 'dig-desktop.webp'), 'digitekm.com')
b += text(740, 928, 'DigiteKM', 24, INK, 800, font=F_HEAD, ls=-0.6) + text(740, 956, 'digitekm.com', 17, MUTED)
b += white_panel(60, 740, 640, 200, 24)
b += eyebrow(92, 784, 'What each one controls')
for k, t in enumerate(['Own domain', 'Own logo and colours', 'Own course catalogue', 'Own student login']):
    b += check_row(92 + (k % 2) * 300, 836 + (k // 2) * 60, t, 20)
b += text(60, H - 28, 'Screens from academies built on AllCoaching.', 16, MUTED) + signature(W, H)
save('real-academies', svg(W, H, b, 'Real coaching websites built on AllCoaching: Biology Lessons at biolessons.in, CHEMPSI at chempsi.com and DigiteKM at digitekm.com'))

# 8. mobile-first ----------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 92, ['Check it on *an everyday phone*'], 50)
b += phone(90, 150, 300, os.path.join(SHOW, 'bio-mobile.webp'))
b += text(90, 806, 'Biology Lessons on a phone', 17, MUTED)
b += white_panel(470, 150, 690, 650, 28)
b += eyebrow(506, 200, 'Mobile checklist')
checks = ['Text readable without zooming', 'Buttons big enough for a thumb', 'Course price easy to find',
          'WhatsApp in one tap', 'Pay by UPI in a few taps', 'Loads on a weak 4G signal',
          'Same content as on desktop', 'In the language students read']
for i, t in enumerate(checks):
    b += check_row(506, 262 + i * 66, t, 23)
b += text(60, H - 28, 'Google indexes the mobile version of a site. Phone screen: biolessons.in, built on AllCoaching.', 16, MUTED) + signature(W, H)
save('mobile-first', svg(W, H, b, 'Mobile-first checklist for a coaching website, shown next to the Biology Lessons academy on a phone'))

# 9. launch checklist --------------------------------------------------------------------
W, H = 1220, 840
b = headline(60, 92, ['Before you *publish*'], 54) + lines(62, 140, ['Twelve checks for a coaching website, in three groups'], 22)
groups = [('Pages', 'list', ['Home says who you teach', 'Every course has a price', 'About page with a photo', 'Free demo lesson live']),
          ('Trust and legal', 'shield', ['Privacy policy', 'Terms of use', 'Refund policy', 'Real address and phone']),
          ('Selling', 'card', ['Test purchase done', 'UPI checkout works', 'Domain connected', 'Pixel or GTM added'])]
for k, (t, ic, items) in enumerate(groups):
    x = 60 + k * 375
    b += white_panel(x, 190, 350, 560, 28)
    b += f'<rect x="{x + 30}" y="220" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon(ic, x + 46, 236, 28, '#fff', 2)
    b += text(x + 30, 340, t, 32, INK, 800, font=F_HEAD, ls=-1.2)
    for i, it in enumerate(items):
        b += check_row(x + 30, 420 + i * 86, it, 20)
b += text(60, H - 28, 'General checklist, not legal advice. Ask a lawyer or CA to review your policy pages.', 16, MUTED) + signature(W, H)
save('launch-checklist', svg(W, H, b, 'Coaching website launch checklist: pages, trust and legal pages, and selling checks before you publish'))
