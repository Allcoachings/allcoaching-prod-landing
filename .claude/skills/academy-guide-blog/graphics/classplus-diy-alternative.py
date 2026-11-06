"""Graphics for /blog/classplus-diy-alternative.

Run:  python .claude/skills/academy-guide-blog/graphics/classplus-diy-alternative.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/classplus-diy-alternative

Every Classplus fact was read from Classplus's own pages on 6 Nov 2026 (classplusapp.com/diy, /create-your-own-app,
/new-web, /termsconditions.html; Google Play listing). No Classplus logo is drawn: Classplus is shown as a name tile.
"Not stated" = the page did not say. AllCoaching studio screenshots are sample data.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

SLUG = 'classplus-diy-alternative'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', SLUG)
os.makedirs(OUT, exist_ok=True)

ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'
ICONS['key'] = '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>'
ICONS['export'] = '<path d="M12 3v12M7 8l5-5 5 5"/><path d="M4 15v5h16v-5"/>'
ICONS['rupee'] = '<path d="M7 4h10M7 8.5h10M7 4c5 0 7 1.5 7 4.5S12 13 7 13l8 8"/>'

GREY = '#8A90A2'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def name_tile(x, y, label, w=None, h=56, size=22):
    """A text-only name tile for a third-party brand (no logo drawn)."""
    w = w or (len(label) * size * 0.62 + 48)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{LINE}" stroke-width="2"/>' +
            text(x + w / 2, y + h / 2 + size * 0.36, label, size, INK, 800, 'middle', F_HEAD, -0.4))


def quote_card(x, y, w, src, q, h=None, size=21):
    rows = q if isinstance(q, list) else [q]
    h = h or (78 + len(rows) * (size * 1.35))
    out = white_panel(x, y, w, h, 22)
    out += text(x + 28, y + 40, src.upper(), 14, BLUE, 600, font=F_MONO, ls=1.4)
    for i, r in enumerate(rows):
        out += text(x + 28, y + 76 + i * size * 1.35, r, size, INK, 600, font=F_HEAD, ls=-0.3)
    return out


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += eyebrow(80, 236, 'Payments & selling · checked 6 Nov 2026')
b += headline(80, 320, ['Classplus DIY:', '*what it is*, price', 'and an alternative'], 70)
b += lines(84, 548, ['Quoted from Classplus\'s own pages,', 'with what they leave unstated'], 25, MUTED)
b += check_row(84, 672, 'What the DIY sign-up leads to', 24)
b += check_row(84, 728, 'Listed price, renewal and terms', 24)
b += check_row(84, 784, 'Own app vs shared app: what to ask', 24)
b += white_panel(930, 120, 600, 660, 32, big=True)
b += name_tile(970, 160, 'Classplus DIY', 260, 60, 26)
b += text(1250, 200, 'classplusapp.com/diy', 18, MUTED, 500, font=F_MONO)
facts = [('Sign-up', '"Setup your website in', 'couple of clicks"', INK),
         ('Listed price', '₹29,999 for 1 year', '₹39,999 for 2 years', INK),
         ('Renewal', 'Same as purchase price', '', INK),
         ('Fee per sale · GST', 'Not stated', '', GREY)]
for i, (k, v1, v2, col) in enumerate(facts):
    y = 252 + i * 128
    b += f'<rect x="960" y="{y}" width="540" height="112" rx="24" fill="#F5F6FA"/>'
    b += text(988, y + 38, k.upper(), 14, BLUE, 600, font=F_MONO, ls=1.4)
    b += text(988, y + 74, v1, 25, col, 800, font=F_HEAD, ls=-0.6)
    if v2:
        b += text(988, y + 102, v2, 21, MUTED, 500)
b += text(1230, 820, 'Names shown as text; logos belong to their owners.', 15, MUTED, anchor='middle')
save('cover', svg(1600, 900, b, 'Classplus DIY explained: the classplusapp.com/diy sign-up, the listed price, what is not stated, and an alternative'))

# 2. what Classplus DIY is --------------------------------------------------------
W, H = 1220, 1080
b = headline(60, 100, ['What Classplus DIY *is*'], 54)
b += lines(62, 150, ['Where the DIY link leads, quoted from Classplus\'s pages, checked 6 Nov 2026'], 22)
steps = [
    ('1', 'Classplus blog menu', ['"Create your own App"'], 'classplusapp.com/growth', 'link'),
    ('2', 'The DIY page', ['"Setup your website in couple', 'of clicks"  ·  "Login to Classplus"'], 'classplusapp.com/diy', 'globe'),
    ('3', 'Create-your-own-app page', ['"Get your own online coaching', 'app in under 60 seconds"'], 'classplusapp.com/create-your-own-app', 'phone'),
    ('4', 'The plan behind it', ['Android App · Website · Admin Portal', '₹29,999 for 1 year · ₹39,999 for 2 years'], 'classplusapp.com/new-web', 'layers'),
]
for i, (n, t, q, src, ic) in enumerate(steps):
    y = 200 + i * 196
    b += white_panel(60, y, 1100, 170, 26)
    b += num_badge(118, y + 85, n, 28)
    b += f'<rect x="170" y="{y + 52}" width="66" height="66" rx="18" fill="{NAVY_TILE}"/>' + icon(ic, 187, y + 69, 32, '#fff', 2)
    b += text(266, y + 56, t, 27, INK, 800, font=F_HEAD, ls=-0.6)
    for k, r in enumerate(q):
        b += text(266, y + 94 + k * 32, r, 22, BLUE if i < 3 else INK, 600, font=F_HEAD, ls=-0.3)
    b += text(1136, y + 56, src, 15, MUTED, 500, 'end', F_MONO)
    if i < 3:
        b += arrow(f'M118 {y + 120} L 118 {y + 190}', BLUE, 3)
b += text(60, 1010, 'Classplus also offers "Book a Free Demo" on the create-your-own-app page. Names shown as text; logos belong to their owners.', 16, MUTED)
b += signature(W, H)
save('what-is-diy', svg(W, H, b, 'What Classplus DIY is: the Create your own App link, the classplusapp.com/diy login page, the create-your-own-app page and the Classplus plan'))

# 3. own app vs shared app --------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['Three meanings of', '*"your own app"*'], 54)
cols = [('Shared app,', "platform's name", 'Your batch inside their app', 'users', False),
        ('Branded app,', "platform's account", 'Your name, their listing', 'phone', False),
        ('Your own app,', 'your account', 'Your name, your listing', 'key', True)]
rows = [('Name students see', ['Platform', 'You', 'You']),
        ('Play Store listing held by', ['Platform', 'Platform', 'You']),
        ('Reviews and downloads', ['Platform', 'Platform', 'You']),
        ('If you leave', ['Students move app', 'Students reinstall', 'Same listing stays']),
        ]
x0, cw = 400, 260
for j, (t1, t2, s, ic, us) in enumerate(cols):
    cx = x0 + j * cw + cw / 2
    b += f'<rect x="{cx - 120}" y="210" width="240" height="190" rx="26" fill="{BLUE_TINT if us else "#fff"}"' + (f' stroke="{BLUE}" stroke-width="2"' if us else '') + '/>'
    b += f'<rect x="{cx - 32}" y="232" width="64" height="64" rx="18" fill="{BLUE if us else NAVY_TILE}"/>' + icon(ic, cx - 16, 248, 32, '#fff', 2)
    b += text(cx, 330, t1, 22, BLUE if us else INK, 800, 'middle', F_HEAD, -0.5)
    b += text(cx, 358, t2, 22, BLUE if us else INK, 800, 'middle', F_HEAD, -0.5)
    b += text(cx, 386, s, 16, MUTED, anchor='middle')
for i, (lab, vals) in enumerate(rows):
    y = 430 + i * 120
    if i % 2 == 0:
        b += f'<rect x="50" y="{y}" width="1120" height="104" rx="18" fill="#F7F8FC"/>'
    b += text(78, y + 60, lab, 22, INK, 700, font=F_HEAD, ls=-0.3)
    for j, v in enumerate(vals):
        cx = x0 + j * cw + cw / 2
        good = v.startswith(('You', 'Same'))
        b += text(cx, y + 60, v, 21, BLUE if good else MUTED, 700 if good else 500, 'middle')
b += text(60, 940, 'A general pattern; check each platform\'s terms. Classplus says its app is "registered in your Coaching’s name";', 16, MUTED)
b += text(60, 964, 'whose developer account publishes it is not stated on the pages we checked (6 Nov 2026).', 16, MUTED)
b += signature(W, H)
save('own-vs-shared', svg(W, H, b, 'Own app vs shared app: a shared app, a branded app on the platform account, and your own app on your own Google Play account'))

# 4. verified facts side by side --------------------------------------------------
W = 1220
facts = [
    ('Listed price', '₹29,999 / 1 yr · ₹39,999 / 2 yrs', 'From ₹3,999/mo or ₹6,999/yr'),
    ('Fee on each sale', 'Not stated', '0% monthly · 10 / 7.5 / 5% yearly'),
    ('GST', 'Not stated', '+ 18% GST'),
    ('Free trial', 'Not stated', '7 days, no card'),
    ('Renewal', 'Same as purchase price', 'Monthly autopay at plan price'),
    ('Cancel early', 'Not allowed; no refund', 'Monthly: stop any month'),
    ('iOS app', 'Not stated', 'Pro monthly, every yearly'),
    ('Developer account', 'Not stated', 'Your own Play / App Store'),
    ('Own domain', 'Not stated ("mini website")', 'Every plan'),
    ('Data export on exit', 'Not stated', '30 days to export'),
]
H = 300 + len(facts) * 70 + 120
b = headline(60, 100, ['Verified facts, *side by side*'], 54)
b += lines(62, 150, ['Classplus quoted from its own pages, 6 Nov 2026. Grey = the page did not say.'], 22)
b += name_tile(420, 196, 'Classplus', 230, 54, 22)
b += f'<rect x="800" y="196" width="300" height="54" rx="14" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2"/>' + text(950, 231, 'AllCoaching', 22, BLUE, 800, 'middle', F_HEAD, -0.4)
y = 276
for i, (k, a, c) in enumerate(facts):
    if i % 2 == 0:
        b += f'<rect x="40" y="{y}" width="1140" height="62" rx="14" fill="#fff"/>'
    b += text(64, y + 39, k, 21, INK, 700, font=F_HEAD, ls=-0.3)
    ns = a.startswith('Not stated')
    b += text(340, y + 39, a, 20, GREY if ns else INK, 400 if ns else 600)
    b += text(780, y + 39, c, 20, BLUE, 700)
    y += 70
b += text(60, H - 76, 'Sources: classplusapp.com/new-web, /diy, /create-your-own-app, /termsconditions.html; allcoaching.in/pricing.', 16, MUTED)
b += text(60, H - 50, '"Not stated" does not mean Classplus lacks it. AllCoaching gateway charges on student payments are separate.', 16, MUTED)
b += signature(W, H)
save('verified-facts', svg(W, H, b, 'Classplus DIY vs AllCoaching: listed price, fee per sale, GST, trial, renewal, iOS, developer account, domain and data export, checked 6 Nov 2026'))

# 5. switch steps -----------------------------------------------------------------
W, H = 1220, 1120
b = headline(60, 100, ['Switch without', '*losing a student*'], 54)
st = [('Ask the 8 questions in writing', 'App type, account, domain, fees, renewal, export', 'message'),
      ('Export your student list', 'Names, phones, batches, end dates', 'export'),
      ('Build your academy in a trial', 'One full course, your domain, your brand', 'home'),
      ('Test checkout on a phone', 'UPI on a basic Android phone, mobile data', 'card'),
      ('Run both side by side', 'Paid students stay till their batch ends', 'layers'),
      ('New admissions to the new academy', 'Update YouTube, Instagram, WhatsApp links', 'users'),
      ('Close the old plan after the last batch', 'Or when the paid term expires', 'check')]
for i, (t, s, ic) in enumerate(st):
    y = 200 + i * 124
    b += white_panel(60, y, 1100, 104, 24)
    b += num_badge(116, y + 52, str(i + 1), 26)
    b += f'<rect x="164" y="{y + 22}" width="60" height="60" rx="16" fill="{BLUE if i == 4 else NAVY_TILE}"/>' + icon(ic, 180, y + 38, 28, '#fff', 2)
    b += text(250, y + 46, t, 26, BLUE if i == 4 else INK, 800, font=F_HEAD, ls=-0.6)
    b += text(250, y + 78, s, 19, MUTED)
b += text(60, 1088, 'On a yearly plan that cannot be cancelled early, line step 7 up with the expiry date.', 17, MUTED)
b += signature(W, H)
save('switch-steps', svg(W, H, b, 'Seven steps to evaluate a self-serve coaching app and switch without losing students'))

# 6. own academy promo ------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Your domain.', 'Your brand.', '*Your students.*'], 62)
b += lines(64, 450, ['Sign up, choose a plan, upload', 'your course, connect your domain,', 'start selling.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Own domain', 'globe', 'Every plan'), ('Android app', 'phone', 'Your Play account'), ('iOS app', 'phone', 'Pro monthly, yearly'),
                                     ('UPI checkout', 'card', 'Via Razorpay'), ('30-day export', 'export', 'If you stop')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission from ₹3,999/month + GST', 27, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('own-academy', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own domain, own Android app on your Play account, iOS on Pro monthly and yearly, UPI checkout, 30-day export'))

# 7. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Self-serve', 'mistakes.'], 54)
for i, t in enumerate(['"DIY" = I own it all', 'Only the headline price', 'Never asked whose account', 'Skipped the cancel terms', 'No export plan']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 520, t, -1.4 if i % 2 else 1.0, 27)
b += hand(300, 790, ['Get it in', 'writing.'], 38, INK, -6)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Ask who holds the listing', 'Add fee, GST, renewal', 'Your own Play account', 'Read cancel and refund terms', 'Export students monthly']):
    b += check_row(656, 400 + i * 74, t, 25)
save('mistakes', svg(W, H, b, 'Mistakes to avoid with a self-serve coaching app such as Classplus DIY, and what to do instead', ('split', 600)))
