"""Graphics for /blog/white-label-app-for-educators-india.

Run:  python .claude/skills/academy-guide-blog/graphics/white-label-app-for-educators-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/white-label-app-for-educators-india
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'white-label-app-for-educators-india')
os.makedirs(OUT, exist_ok=True)
SHOT = os.path.join(ROOT, 'landing', 'img', 'studio-app.webp')        # real studio Own branding > App screen (sample educator)
BIO = os.path.join(ROOT, 'assets', 'showcase', 'bio-mobile.webp')     # Biology Lessons (Dr. Subhash Nair), owner-approved showcase

ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3M12 15v2"/>'
ICONS['download'] = '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>'
ICONS['edit'] = '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/>'
ICONS['door'] = '<path d="M6 21V4h10v17M4 21h16"/><path d="M13 12h.01"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def app_icon(x, y, size, label, fill=BLUE):
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .24}" fill="{fill}"/></g>' +
            text(x + size / 2, y + size / 2 + size * .14, label, size * .38, '#fff', 800, 'middle', F_HEAD, -1))


def yes(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="17" fill="{BLUE}"/>' + icon('tick', cx - 10, cy - 10, 20, '#fff', 2.8)


def no(cx, cy):
    return f'<circle cx="{cx}" cy="{cy}" r="17" fill="#C9CDD8"/>' + icon('x', cx - 9, cy - 9, 18, '#fff', 2.8)


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['A white-label app', 'for your academy,', '*in your name.*'], 70)
b += lines(84, 520, ['What it means, what to check, how to get one.'], 28, MUTED)
b += check_row(84, 604, 'Your name, icon and colours', 26)
b += check_row(84, 664, 'Published under your own account', 26)
b += check_row(84, 724, 'Built and updated from the studio', 26)
b += text(880, 158, 'Studio preview · sample data', 15, MUTED)
b += laptop(880, 172, 600, SHOT)
b += phone(1340, 430, 170, BIO)
# store-listing pill (illustrative)
b += white_panel(840, 690, 470, 120, 26)
b += app_icon(862, 712, 76, 'YA')
b += text(958, 744, 'Your Academy', 28, INK, 800, font=F_HEAD, ls=-0.8)
b += text(958, 778, 'Developer: Your Academy', 19, BLUE, 600)
b += text(840, 840, 'Illustrative listing · phone: Biology Lessons, an academy on AllCoaching', 15, MUTED)
save('cover', svg(1600, 900, b, 'White-label app for educators in India: your own branded app, published under your own developer account, built from the AllCoaching studio'))

# 2. three ways -------------------------------------------------------------------
W, H = 1220, 980
b = headline(60, 100, ['Three ways to get *an app*'], 54)
b += lines(62, 150, ['What students see, and who stays in control'], 22)
b += white_panel(60, 190, 1100, 700, 28)
cols = [(510, 'Marketplace app', False), (760, 'White-label app', True), (1010, 'Agency-built app', False)]
b += f'<rect x="640" y="206" width="240" height="668" rx="20" fill="{BLUE_TINT}"/>'
for cx, t, hl in cols:
    b += text(cx, 262, t, 22, BLUE if hl else INK, 800, 'middle', F_HEAD, -0.5)
rows = [('Your name and icon', ['No, the platform\'s', 'Yes', 'Yes']),
        ('Developer account', ['The platform\'s', 'Yours, or ask', 'Yours, or ask']),
        ('Change it yourself', ['No', 'Yes, from a panel', 'Through the agency']),
        ('Updates and store rules', ['Platform', 'Platform', 'Paid agency work']),
        ('Upfront build', ['None', 'None, a plan fee', 'A build project']),
        ('Students on screen', ['Beside other educators', 'Only yours', 'Only yours'])]
for i, (lab, vals) in enumerate(rows):
    y = 300 + i * 96
    b += f'<line x1="92" y1="{y}" x2="1128" y2="{y}" stroke="{LINE}" stroke-width="2"/>'
    b += text(96, y + 56, lab, 21, INK, 700, font=F_HEAD, ls=-0.3)
    for (cx, _, hl), v in zip(cols, vals):
        b += text(cx, y + 56, v, 19, BLUE if hl else MUTED, 700 if hl else 400, 'middle')
b += text(60, H - 28, 'A qualitative guide. Check each vendor\'s own terms before you choose.', 16, MUTED)
b += signature(W, H)
save('three-ways', svg(W, H, b, 'White-label app vs marketplace app vs agency-built app for educators: name and icon, developer account, control, updates, upfront build and which students appear'))

# 3. store listing: whose name is under the app ------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Whose name is *under the app?*'], 54)
b += lines(62, 150, ['The developer line on a store listing shows whose account published it'], 22)


def listing(x, y, w, title, dev, good):
    out = white_panel(x, y, w, 560, 28)
    out += eyebrow(x + 32, y + 50, 'Your own account' if good else 'A vendor\'s account', BLUE if good else MUTED)
    out += app_icon(x + 32, y + 84, 104, 'YA', BLUE if good else '#8A90A6')
    out += text(x + 160, y + 124, title, 30, INK, 800, font=F_HEAD, ls=-0.9)
    if good:
        out += f'<rect x="{x + 150}" y="{y + 144}" width="{w - 182}" height="44" rx="12" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2.5"/>'
    out += text(x + 162, y + 174, dev, 21, BLUE if good else MUTED, 700 if good else 500)
    out += text(x + 160, y + 214, 'Education', 18, MUTED)
    out += f'<rect x="{x + 32}" y="{y + 252}" width="{w - 64}" height="54" rx="27" fill="{INK}"/>' + text(x + w / 2, y + 286, 'Install', 21, '#fff', 700, 'middle', F_HEAD)
    for k in range(3):
        out += f'<rect x="{x + 32 + k * ((w - 64 - 32) / 3 + 16):.0f}" y="{y + 334}" width="{(w - 64 - 32) / 3:.0f}" height="190" rx="16" fill="#EEF0F6"/>'
    return out


b += listing(60, 200, 520, 'Your Academy', 'Developer: Your Academy', True)
b += listing(640, 200, 520, 'Your Academy', 'Developer: Vendor Pvt Ltd', False)
b += text(60, H - 28, 'Illustrative store listings; not real apps. Store layouts differ between Google Play and the App Store.', 16, MUTED)
b += signature(W, H)
save('store-listing', svg(W, H, b, 'Illustrative app store listing for a white-label app: Developer: Your Academy when published on your own account, versus a vendor name when published on the vendor\'s account'))

# 4. checklist before you choose ---------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['Seven questions *before you choose*'], 52)
b += lines(62, 150, ['Ask every white-label app provider, including us'], 22)
qs = [('Whose developer account?', 'Your name should be the developer', 'users'),
      ('Can you change it yourself?', 'Logo, colours, content, no ticket', 'edit'),
      ('Can you export your data?', 'Students, sales and content', 'download'),
      ('Is iOS included?', 'On which plan, at what price', 'phone'),
      ('Who handles store review?', 'Submissions, fixes, policy updates', 'shield'),
      ('What does it cost each year?', 'Plan, store fees, renewal, GST', 'tag'),
      ('What if you leave?', 'App, account and data stay yours', 'door')]
for i, (t, s, ic) in enumerate(qs):
    col, row = i % 2, i // 2
    b += pill_card(60 + col * 560, 196 + row * 132, 540, t, s, ic, h=108, tile=NAVY_TILE if (col + row) % 2 == 0 else BLUE_TINT, title_size=25)
b += f'<g filter="url(#shB)"><rect x="620" y="592" width="540" height="108" rx="24" fill="{BLUE}"/></g>'
b += icon('check', 646, 626, 40, '#fff', 2)
b += text(706, 640, 'Get every answer in writing', 25, '#fff', 800, font=F_HEAD, ls=-0.8)
b += text(706, 670, 'before you pay or sign anything', 19, '#fff', opacity=.85)
b += signature(W, H)
save('choose-checklist', svg(W, H, b, 'Seven questions to ask before choosing a white-label app for teachers: developer account, self-editing, data export, iOS, store review, yearly cost and what happens if you leave'))

# 5. how it works on AllCoaching ---------------------------------------------------
W, H = 1220, 960
b = headline(60, 100, ['How it works *on AllCoaching*'], 54)
b += lines(62, 150, ['Own branding  ›  App, in the studio'], 22, INK)
b += laptop(80, 214, 620, SHOT)
b += text(80, 690, 'Studio preview · sample data', 15, MUTED)
steps = [('Set your brand', ['Name, icon and colours', 'in Own branding']),
         ('The studio builds it', ['Your Android app; iOS', 'on eligible plans']),
         ('Publish on your account', ['By you, or by us with', 'API access you grant']),
         ('Stores review it', ['Then students install', 'your app by name'])]
for k, (t, s) in enumerate(steps):
    y = 206 + k * 124
    b += num_badge(788, y + 22, k + 1, 22)
    b += text(824, y + 31, t, 26, INK, 800, font=F_HEAD, ls=-0.8)
    b += lines(824, y + 64, s, 19, MUTED, 1.35)
for k, (t, s, ic) in enumerate([('Android app', 'on every plan', 'phone'),
                                 ('iOS app', 'Pro monthly, all yearly', 'phone'),
                                 ('Store fees', 'paid by you to the stores', 'card')]):
    b += pill_card(60 + k * 374, 760, 352, t, s, ic, h=104, tile=BLUE if k == 0 else NAVY_TILE, title_size=24)
b += signature(W, H)
save('how-it-works', svg(W, H, b, 'How a white-label app works on AllCoaching: set your brand in Own branding, the studio builds the app, publish it on your own developer account, Google and Apple review it'))

# 6. Android and iOS by plan -------------------------------------------------------
W, H = 1220, 940
b = headline(60, 100, ['Android and iOS *by plan*'], 54)
b += lines(62, 150, ['Your own app on every AllCoaching plan'], 22)
b += white_panel(60, 190, 1100, 660, 28)
hx = [96, 420, 660, 900, 1060]
for x, t in zip(hx, ['Plan', 'Price', 'Fee per sale', 'Android', 'iOS']):
    b += eyebrow(x, 244, t, MUTED, 'middle' if t in ('Android', 'iOS') else 'start')
plans = [('Starter', '₹3,999 a month', '0%', False), ('Growth', '₹5,999 a month', '0%', False), ('Pro', '₹7,999 a month', '0%', True),
         ('Starter', '₹6,999 a year', '10%', True), ('Growth', '₹12,999 a year', '7.5%', True), ('Pro', '₹24,999 a year', '5%', True)]
y0 = 270
for i, (n, p, f, ios) in enumerate(plans):
    if i in (0, 3):
        b += f'<rect x="80" y="{y0}" width="1060" height="40" rx="10" fill="{BLUE_TINT}"/>'
        b += eyebrow(96, y0 + 26, 'Monthly · 0% commission' if i == 0 else 'Yearly · fee per sale')
        y0 += 52
    b += text(96, y0 + 40, n, 25, INK, 800, font=F_HEAD, ls=-0.6)
    b += text(420, y0 + 40, p, 22, INK, 600)
    b += text(660, y0 + 40, f, 22, BLUE if f == '0%' else INK, 700)
    b += yes(900, y0 + 32) + (yes(1060, y0 + 32) if ios else no(1060, y0 + 32))
    if i not in (2, 5):
        b += f'<line x1="96" y1="{y0 + 64}" x2="1124" y2="{y0 + 64}" stroke="{LINE}" stroke-width="2"/>'
    y0 += 70
b += text(60, H - 54, 'Prices exclude 18% GST. 7-day free trial, no card needed. No sales limit, no setup fee.', 17, MUTED)
b += text(60, H - 28, 'Store fees are paid by you: Google Play US$25 once, Apple Developer Program US$99 a year.', 17, MUTED)
b += signature(W, H)
save('android-ios-by-plan', svg(W, H, b, 'AllCoaching plans and white-label apps: own Android app on every plan, own iOS app on Pro monthly and every yearly plan, with monthly and yearly prices'))

# 7. store fees and rules ----------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['The store side: *fees and rules*'], 52)
b += lines(62, 150, ['Set by Google and Apple, the same for every educator'], 22)
for k, (who, amt, per) in enumerate([('Google Play developer account', 'US$25', 'one-time registration fee'),
                                      ('Apple Developer Program', 'US$99', 'a year, in local currency')]):
    x = 60 + k * 560
    b += white_panel(x, 196, 540, 220, 28)
    b += eyebrow(x + 36, 246, who)
    b += text(x + 36, 336, amt, 76, INK, 800, font=F_HEAD, ls=-3)
    b += text(x + 36, 384, per, 21, MUTED)
b += white_panel(60, 446, 1100, 150, 28)
b += f'<rect x="92" y="481" width="80" height="80" rx="20" fill="{BLUE_TINT}"/>' + icon('users', 112, 501, 40, BLUE, 2)
b += text(200, 512, 'New personal Play account? Closed test first.', 28, INK, 800, font=F_HEAD, ls=-0.9)
b += text(200, 548, 'At least 12 testers, opted in for 14 days in a row, before you can apply for production.', 19, MUTED)
b += text(200, 576, 'Applies to personal accounts created after 13 November 2023.', 19, MUTED)
b += white_panel(60, 626, 1100, 130, 28)
b += f'<rect x="92" y="651" width="80" height="80" rx="20" fill="{BLUE_TINT}"/>' + icon('shield', 112, 671, 40, BLUE, 2)
b += text(200, 684, 'Your app goes through store review.', 28, INK, 800, font=F_HEAD, ls=-0.9)
b += text(200, 720, 'Google and Apple decide the timing. Nobody can promise you a date.', 19, MUTED)
b += text(60, H - 28, 'Sources: Play Console Help and Apple Developer, checked November 2026.', 16, MUTED)
b += signature(W, H)
save('store-rules', svg(W, H, b, 'App store fees and rules for a white-label app: Google Play US$25 once, Apple Developer Program US$99 a year, closed test with 12 testers for 14 days for new personal Play accounts'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['White-label mistakes', 'that cost you.'], 52)
for i, t in enumerate(["App on a vendor's account", 'No data export', 'iOS "coming soon"', 'Every change is a ticket', 'No plan for 12 testers']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 510, t, -1.4 if i % 2 else 1.0, 28)
b += hand(330, 790, ['Whose app', 'is this?'], 40, INK, -6) + arrow('M300 800 C 250 820, 210 800, 190 770', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Publish on your own account', 'Get data export in writing', 'Check iOS on your plan', 'Change it yourself, any day', 'Line up testers early']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Common white-label app mistakes educators make and what to do instead', ('split', 600)))
