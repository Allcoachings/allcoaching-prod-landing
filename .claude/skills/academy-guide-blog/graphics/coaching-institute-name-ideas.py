"""Graphics for /blog/coaching-institute-name-ideas.

Run:  python .claude/skills/academy-guide-blog/graphics/coaching-institute-name-ideas.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/coaching-institute-name-ideas
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'coaching-institute-name-ideas')
os.makedirs(OUT, exist_ok=True)
DOMAIN = os.path.join(ROOT, 'landing', 'img', 'studio-domain.webp')    # real studio Own branding > Domain (sample educator)
THEMES = os.path.join(ROOT, 'landing', 'img', 'studio-themes.webp')    # real studio Own branding > Themes (sample educator)

ICONS['edit'] = '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/>'
ICONS['at'] = '<circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 006 0v-1a10 10 0 10-4 8"/>'
ICONS['scale'] = '<path d="M12 3v18M7 21h10M5 7h14"/><path d="M5 7l-3 7a3 3 0 006 0zM19 7l-3 7a3 3 0 006 0z"/>'
ICONS['speech'] = '<path d="M4 5h16v11H9l-5 4z"/>'
ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def app_icon(x, y, size, label, fill=BLUE):
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .24}" fill="{fill}"/></g>' +
            text(x + size / 2, y + size / 2 + size * .14, label, size * .38, '#fff', 800, 'middle', F_HEAD, -1))


def name_chip(x, y, w, label, hl=False):
    fill = BLUE if hl else '#fff'
    col = '#fff' if hl else INK
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="58" rx="29" fill="{fill}"/></g>' +
            text(x + w / 2, y + 37, label, 22, col, 700, 'middle', F_HEAD, -0.4))


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Name your academy.', '*Then make it yours.*'], 72)
b += lines(84, 448, ['Five formulas, 80 name ideas and the checks to run first.'], 27, MUTED)
b += check_row(84, 548, 'Short, easy to say in Hindi and English', 26)
b += check_row(84, 608, 'Free as a domain, handle and app name', 26)
b += check_row(84, 668, 'Nothing misleading, nothing copied', 26)
b += text(880, 158, 'Studio preview · sample data', 15, MUTED)
b += laptop(880, 172, 600, DOMAIN)
# illustrative name chips
b += name_chip(860, 640, 220, 'Bio Sutra', True)
b += name_chip(1100, 640, 230, 'Ganit Setu')
b += name_chip(960, 716, 250, 'English Chaupal')
b += name_chip(1230, 716, 200, 'Loop Lab')
b += text(860, 830, 'Illustrative name ideas · check availability before you use any name', 15, MUTED)
save('cover', svg(1600, 900, b, 'Coaching institute name ideas: how to name your coaching institute or online academy and turn the name into your own brand on AllCoaching'))

# 2. good-name checklist -----------------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['Six tests for a *good name*'], 54)
b += lines(62, 150, ['Run every name on your shortlist through all six'], 22)
tests = [('Short', 'Two or three words, under ~15 letters', 'type'),
         ('Easy to say aloud', 'In Hindi and in English, on a call', 'speech'),
         ('Says the subject', 'Or the outcome students want', 'book'),
         ('Free everywhere', 'Domain, Instagram, YouTube, app', 'globe'),
         ('Not tied to a city or year', 'Still fits when you go online', 'pin'),
         ('Nothing misleading', 'No ranks promised, nothing official', 'shield')]
for i, (t, s, ic) in enumerate(tests):
    col, row = i % 2, i // 2
    b += pill_card(60 + col * 560, 196 + row * 140, 540, t, s, ic, h=112, tile=NAVY_TILE if (col + row) % 2 == 0 else BLUE_TINT, title_size=26)
b += f'<g filter="url(#shB)"><rect x="60" y="626" width="1100" height="96" rx="24" fill="{BLUE}"/></g>'
b += icon('check', 90, 654, 40, '#fff', 2)
b += text(150, 683, 'Five of six is not enough: drop the name and try the next one.', 25, '#fff', 700, font=F_HEAD, ls=-0.6)
b += signature(W, H)
save('good-name-checklist', svg(W, H, b, 'Six tests for coaching institute name ideas: short, easy to say in Hindi and English, says the subject, free as a domain and handle, not tied to a city or year, nothing misleading'))

# 3. naming formulas ---------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Five *naming formulas*'], 54)
b += lines(62, 150, ['Write five names with each one, then judge them'], 22)
forms = [('Teacher name + subject', "Verma Sir Maths · Yoga with Kavya", 'users'),
         ('Outcome-led', 'Fluent Hour · Daily Bio Dose', 'trend'),
         ('Exam or subject-led', 'Reasoning Room · Concept First JEE', 'book'),
         ('Hindi or Sanskrit word', 'Ganit Setu · Sthira Studio', 'type'),
         ('Place-neutral idea', 'Atlas & Ink · Loop Lab', 'globe')]
for i, (t, ex, ic) in enumerate(forms):
    y = 196 + i * 146
    b += white_panel(60, y, 1100, 124, 24)
    b += num_badge(112, y + 62, i + 1, 26)
    b += f'<rect x="164" y="{y + 30}" width="64" height="64" rx="16" fill="{BLUE_TINT}"/>' + icon(ic, 180, y + 46, 32, BLUE, 2)
    b += text(256, y + 56, t, 30, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(256, y + 94, 'e.g. ' + ex, 21, MUTED)
b += text(60, H - 28, 'Example names are illustrative and not checked for availability.', 16, MUTED)
b += signature(W, H)
save('naming-formulas', svg(W, H, b, 'Five naming formulas for coaching institute name ideas: teacher name plus subject, outcome-led, exam or subject-led, Hindi or Sanskrit word, place-neutral idea'))


# 4/5. name idea boards ------------------------------------------------------------
def board(slug, title, sub, groups, alt):
    W, H = 1220, 1060
    b = headline(60, 100, title, 54)
    b += lines(62, 150, [sub], 22)
    cw = 344
    for i, (g, ic, names) in enumerate(groups):
        col, row = i % 3, i // 3
        x, y = 60 + col * (cw + 34), 196 + row * 400
        b += white_panel(x, y, cw, 372, 24)
        b += f'<rect x="{x + 24}" y="{y + 24}" width="56" height="56" rx="14" fill="{NAVY_TILE if i % 2 == 0 else BLUE}"/>' + icon(ic, x + 38, y + 38, 28, '#fff', 2)
        b += text(x + 96, y + 62, g, 25, INK, 800, font=F_HEAD, ls=-0.7)
        for k, n in enumerate(names):
            yy = y + 112 + k * 50
            b += f'<rect x="{x + 24}" y="{yy}" width="{cw - 48}" height="40" rx="12" fill="{BLUE_TINT if k == 0 else "#F4F5FA"}"/>'
            b += text(x + 40, yy + 27, n, 20, BLUE if k == 0 else INK, 600, font=F_HEAD, ls=-0.3)
    # sixth slot: note card
    x, y = 60 + 2 * (cw + 34), 596
    b += f'<g filter="url(#shB)"><rect x="{x}" y="{y}" width="{cw}" height="372" rx="24" fill="{BLUE}"/></g>'
    b += text(x + 30, y + 70, 'All 40 ideas', 30, '#fff', 800, font=F_HEAD, ls=-0.9)
    b += lines(x + 30, y + 112, ['are in the tables', 'in this guide.'], 22, '#fff', 1.4, opacity=.9)
    b += lines(x + 30, y + 220, ['Illustrative only.', 'Check the domain,', 'trade mark and handles', 'before you use any name.'], 20, '#fff', 1.4, opacity=.85)
    b += signature(W, H)
    save(slug, svg(W, H, b, alt))


board('name-ideas-exams', ['Name ideas *by exam*'], 'Illustrative suggestions, five from each list in this guide',
      [('NEET', 'book', ['Bio Sutra', 'Cell Craft Biology', 'Mole Mitra Chemistry', 'Daily Bio Dose', 'Reaction Room']),
       ('JEE', 'chart', ['Ganit Setu', 'Vector Verse', 'Torque Tutors', 'Prism Physics Studio', 'Theta Classes']),
       ('UPSC · State PSC', 'file', ['Nibandh Room', 'Uttar Lekhan Studio', 'Polity Pathshala', 'Atlas & Ink', 'Current Kosh']),
       ('SSC · Banking', 'trend', ['Quant Kitchen', 'Reasoning Room', 'Vocab Vatika', 'Puzzle Point', 'Speed Ganit Shala']),
       ('CUET · CLAT', 'list', ['Nyaya Notes', 'Lex Ladder', 'Clause & Case', 'Comprehension Club', 'Domain Desk'])],
      'Coaching institute name ideas by exam: illustrative names for NEET, JEE, UPSC and state PSC, SSC and banking, and CUET and CLAT')

board('name-ideas-skills', ['Name ideas *by skill*'], 'Illustrative suggestions, five from each list in this guide',
      [('Spoken English', 'speech', ['Fluent Hour', 'Bolo English Club', 'English Chaupal', 'Daily Dialogue', 'Accent Aangan']),
       ('Yoga', 'sparkle', ['Prana Path Yoga', 'Sthira Studio', 'Shwas Yoga', 'Morning Mat', 'Antar Yoga']),
       ('Digital marketing', 'chart', ['Funnel Pathshala', 'Ad Craft School', 'Organic Reach Room', 'Campaign Class', 'Metrics Mandi']),
       ('Music', 'mic', ['Raag Room', 'Riyaaz Studio', 'Taal Tree', 'Strings & Swar', 'Bansuri Baithak']),
       ('Coding', 'layers', ['Code Pathshala', 'Byte Bhasha', 'Syntax Sabha', 'Loop Lab', 'Stack Shala'])],
      'Online academy name ideas by skill: illustrative names for spoken English, yoga, digital marketing, music and coding academies')

# 6. availability check flow --------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Check the name *in five places*'], 54)
b += lines(62, 150, ['Before you buy a logo, print a poster or announce it'], 22)
rows = [('Domain registrar', 'Is the .in or .com free, without hyphens or numbers?', 'globe', None),
        ('IP India trade mark search', 'Any same or similar mark, especially in Class 41?', 'scale', None),
        ('Instagram and YouTube', 'Is the same handle free on both?', None, 'social'),
        ('Google Play Store', 'Is another education app already using it?', 'phone', None),
        ('A plain Google search', 'Any coaching centre or channel with a similar name?', None, 'google')]
for i, (t, s, ic, logo) in enumerate(rows):
    y = 196 + i * 146
    if i < len(rows) - 1:
        b += f'<line x1="104" y1="{y + 110}" x2="104" y2="{y + 166}" stroke="{BLUE}" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>'
    b += white_panel(150, y, 1010, 120, 24)
    b += num_badge(104, y + 60, i + 1, 28)
    if logo == 'social':
        b += logo_tile(176, y + 22, logo_instagram, 76) + logo_tile(264, y + 22, logo_youtube, 76)
        tx = 368
    elif logo == 'google':
        b += logo_tile(176, y + 22, logo_google, 76)
        tx = 280
    else:
        b += f'<rect x="176" y="{y + 22}" width="76" height="76" rx="20" fill="{NAVY_TILE}"/>' + icon(ic, 194, y + 40, 40, '#fff', 2)
        tx = 280
    b += text(tx, y + 54, t, 28, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(tx, y + 90, s, 20, MUTED)
b += text(60, H - 28, 'Logos belong to their owners. Not legal advice; for a trade mark opinion, ask an agent or lawyer.', 16, MUTED)
b += signature(W, H)
save('availability-check', svg(W, H, b, 'How to check coaching institute name ideas for availability: domain registrar, IP India trade mark search, Instagram and YouTube handles, Google Play Store and Google search'))

# 7. name -> brand on AllCoaching ----------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['From a name *to a brand*'], 54)
b += lines(62, 150, ['What your name becomes on AllCoaching'], 22, INK)
b += laptop(60, 220, 640, THEMES)
b += text(60, 700, 'Studio preview · sample data', 15, MUTED)
steps = [('Free address at sign-up', ['yourname.allcoaching.in,', 'from the name you enter']),
         ('Your own domain', ['Connect it free on', 'every plan']),
         ('Logo and colours', ['Brand name, logo, slogan', 'and colours in Own branding']),
         ('Your own Android app', ['Your name and icon, on', 'your own Play account'])]
for k, (t, s) in enumerate(steps):
    y = 214 + k * 124
    b += num_badge(780, y + 22, k + 1, 22)
    b += text(816, y + 31, t, 26, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(816, y + 64, s, 19, MUTED, 1.35)
b += white_panel(60, 760, 1100, 150, 28)
b += app_icon(92, 790, 90, 'BS')
b += text(210, 830, 'Bio Sutra', 32, INK, 800, font=F_HEAD, ls=-1)
b += text(210, 868, 'biosutra.in  ·  @biosutra  ·  Bio Sutra app', 21, BLUE, 600)
b += text(1128, 846, 'One name, everywhere', 22, MUTED, 500, 'end')
b += text(60, H - 28, 'Illustrative academy name. iOS app on Pro monthly and every yearly plan. Prices exclude GST.', 16, MUTED)
b += signature(W, H)
save('name-to-brand', svg(W, H, b, 'From coaching institute name ideas to a brand on AllCoaching: free .allcoaching.in address, own domain, logo and colours in Own branding, own Android app with your name'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Names that', 'cost you later.'], 52)
for i, t in enumerate(['100% Selection Classes', 'Sounds like a govt body', "One letter off a big brand", 'City + year in the name', 'Spelling nobody can type']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 520, t, -1.4 if i % 2 else 1.0, 27)
b += hand(330, 790, ['Spelling kya hai?'], 40, INK, -6) + arrow('M300 800 C 250 820, 210 800, 190 770', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Name how you teach', 'Keep it clearly yours', 'Make it unmistakably new', 'Keep it place-neutral', 'Pass the phone-call test']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Coaching institute name mistakes to avoid and what to do instead', ('split', 600)))
