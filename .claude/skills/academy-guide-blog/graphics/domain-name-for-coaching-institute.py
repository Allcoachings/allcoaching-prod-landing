"""Graphics for /blog/domain-name-for-coaching-institute.

Run:  python .claude/skills/academy-guide-blog/graphics/domain-name-for-coaching-institute.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/domain-name-for-coaching-institute
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'domain-name-for-coaching-institute')
os.makedirs(OUT, exist_ok=True)
SHOT = os.path.join(ROOT, 'landing', 'img', 'studio-domain.webp')  # real studio Own branding > Domain screen

# extra line icons for this post
ICONS['lock'] = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3M12 15v2"/>'
ICONS['mail'] = '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'
ICONS['clock'] = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def toggle(x, y, on=True):
    if on:
        return f'<rect x="{x}" y="{y}" width="64" height="34" rx="17" fill="{BLUE}"/><circle cx="{x + 47}" cy="{y + 17}" r="13" fill="#fff"/>'
    return f'<rect x="{x}" y="{y}" width="64" height="34" rx="17" fill="#D5D8E2"/><circle cx="{x + 17}" cy="{y + 17}" r="13" fill="#fff"/>'


def browser_bar(x, y, w, url, h=64):
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="#fff"/></g>' +
            icon('lock', x + 22, y + h / 2 - 13, 26, GREEN, 2.2) +
            text(x + 62, y + h / 2 + 9, url, 25, INK, 600, font=F_HEAD, ls=-0.4))


# 1. cover ------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['A domain name', 'for your', '*coaching institute.*'], 72)
b += lines(84, 520, ['Choose it, buy it, connect it to your academy.'], 28, MUTED)
b += check_row(84, 604, 'A short name students can type', 26)
b += check_row(84, 664, 'Bought in your own name', 26)
b += check_row(84, 724, 'Connected in the studio', 26)
b += text(900, 182, 'Studio preview · sample data', 15, MUTED)
b += laptop(900, 196, 620, SHOT)
b += browser_bar(860, 670, 420, 'youracademy.in')
b += f'<rect x="1300" y="682" width="200" height="40" rx="20" fill="#fff" stroke="{BLUE}" stroke-width="2"/>' + text(1400, 709, 'HTTPS on', 19, BLUE, 700, 'middle', F_HEAD)
save('cover', svg(1600, 900, b, 'Domain name for a coaching institute: choose a short name, buy it in your own name and connect it to your academy in the AllCoaching studio'))

# 2. name checklist ---------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Six tests for a *good academy name*'], 50)
b += lines(62, 150, ['Run every name on your shortlist through all six.'], 22)
tests = [('Short', 'Ideally under 15 letters', 'type'),
         ('Easy to say once', 'Passes the phone-call test', 'mic'),
         ('No hyphens or numbers', 'Nothing to spell out', 'x'),
         ('Not tied to one year', 'No 2026 in the name', 'calendar'),
         ('Free on social too', 'Same handle on YouTube, Instagram', 'users'),
         ("Not someone else's mark", 'Check the trademark search', 'shield')]
for i, (t, s, ic) in enumerate(tests):
    b += pill_card(60, 196 + i * 112, 560, t, s, ic, h=96, tile=NAVY_TILE if i % 2 == 0 else BLUE_TINT, title_size=25)
b += white_panel(660, 196, 500, 656, 28)
b += eyebrow(692, 244, 'Examples (illustrative)')
ex = [('sharmaphysics.in', 'Your name + subject', True),
      ('rkclasses.in', 'Short, sounds like you', True),
      ('neetbiowithanu.com', 'Clear, easy to say', True),
      ('best-neet-coaching-2026.com', 'Hyphens, a year, generic', False),
      ('physics4u-classes.in', 'Number + hyphen', False),
      ('bigbrand-academy.in', "Borrows another brand's name", False)]
for i, (d, why, ok) in enumerate(ex):
    y = 312 + i * 92
    b += check_row(692, y, d, 23, ok)
    b += text(736, y + 30, why, 17, MUTED)
b += signature(W, H)
save('name-checklist', svg(W, H, b, 'Six tests for a good coaching institute domain name: short, easy to say, no hyphens or numbers, not tied to one year, free on social media, not a trademark'))

# 3. TLD comparison ---------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['*.in, .com, .co.in* or .academy?'], 52)
b += lines(62, 150, ['Which ending suits a coaching institute'], 22)
b += white_panel(60, 190, 1100, 630, 28)
b += eyebrow(100, 238, 'Ending', MUTED) + eyebrow(330, 238, 'Best for', MUTED) + eyebrow(760, 238, 'Keep in mind', MUTED)
rows = [('.in', ['Academies teaching', 'students in India'], ['Short and clearly Indian;', 'a good default'], True),
        ('.com', ['Students in India', 'and abroad'], ['Most familiar; short', 'names are often taken'], False),
        ('.co.in', ['When your .in', 'is already taken'], ['Longer to type', 'and to say aloud'], False),
        ('.academy', ['Saying "school"', 'at a glance'], ['Less familiar; check', 'the renewal price'], False)]
for i, (tld, best, keep, hl) in enumerate(rows):
    y = 262 + i * 136
    if hl:
        b += f'<rect x="80" y="{y + 6}" width="1060" height="124" rx="20" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="2"/>'
    elif i:
        b += f'<line x1="100" y1="{y + 2}" x2="1120" y2="{y + 2}" stroke="{LINE}" stroke-width="2"/>'
    b += text(100, y + 82, tld, 44, BLUE if hl else INK, 800, font=F_HEAD, ls=-1.6)
    b += lines(330, y + 60, best, 22, INK, 1.4)
    b += lines(760, y + 60, keep, 22, MUTED, 1.4)
    if hl:
        b += f'<rect x="100" y="{y + 98}" width="150" height="26" rx="13" fill="{BLUE}"/>' + text(175, y + 116, 'GOOD DEFAULT', 13, '#fff', 700, 'middle', F_MONO, 1)
b += text(60, H - 28, 'Guidance, not a rule. Check availability and the renewal price at your registrar.', 16, MUTED)
b += signature(W, H)
save('tld-compare', svg(W, H, b, 'Comparison of .in, .com, .co.in and .academy domain endings for a coaching institute'))

# 4. registrar checkout -----------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Five ticks *at checkout*'], 54)
b += lines(62, 150, ['What to set when you buy the domain'], 22)
px, py, pw = 60, 196, 640
b += white_panel(px, py, pw, 700, 26, big=True)
b += f'<rect x="{px}" y="{py}" width="{pw}" height="56" rx="26" fill="#F1F3F6"/><rect x="{px}" y="{py + 30}" width="{pw}" height="26" fill="#F1F3F6"/>'
b += ''.join(f'<circle cx="{px + 30 + k * 22}" cy="{py + 28}" r="7" fill="{c}"/>' for k, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']))
b += text(px + 120, py + 35, 'Your registrar · Checkout', 16, MUTED)
ix = px + 36
# domain row
b += f'<rect x="{ix}" y="{py + 84}" width="568" height="72" rx="16" fill="#F4F6FF"/>'
b += text(ix + 22, py + 130, 'youracademy.in', 28, INK, 800, font=F_HEAD, ls=-0.8)
b += f'<rect x="{ix + 420}" y="{py + 104}" width="128" height="34" rx="17" fill="#DDF3E5"/>' + text(ix + 484, py + 127, 'Available', 16, GREEN, 700, 'middle')
# registrant
b += text(ix, py + 200, 'Registered to', 17, MUTED) + text(ix, py + 230, 'Your name · you@gmail.com', 22, INK, 600)
b += f'<line x1="{ix}" y1="{py + 256}" x2="{ix + 568}" y2="{py + 256}" stroke="{LINE}" stroke-width="2"/>'
opts = [('Privacy protection', 'Hides your phone and address', True),
        ('Auto-renew', 'Renews before it expires', True),
        ('Registration period', '1 or 2 years', None)]
for k, (t, s, on) in enumerate(opts):
    y = py + 300 + k * 76
    b += text(ix, y, t, 22, INK, 600) + text(ix, y + 28, s, 17, MUTED)
    if on is None:
        b += f'<rect x="{ix + 448}" y="{y - 24}" width="120" height="40" rx="12" fill="#fff" stroke="{LINE}" stroke-width="2"/>' + text(ix + 508, y + 2, '1 year', 17, INK, 600, 'middle')
    else:
        b += toggle(ix + 504, y - 22, on)
b += f'<line x1="{ix}" y1="{py + 520}" x2="{ix + 568}" y2="{py + 520}" stroke="{LINE}" stroke-width="2"/>'
b += text(ix, py + 558, 'Add-ons', 17, MUTED)
for k, t in enumerate(['Hosting', 'Website builder', 'SSL certificate']):
    x = ix + k * 190
    b += f'<rect x="{x}" y="{py + 576}" width="178" height="44" rx="12" fill="#F3F4F8"/>' + text(x + 89, py + 604, t, 17, '#9A9EAB', 500, 'middle')
    b += f'<line x1="{x + 18}" y1="{py + 598}" x2="{x + 160}" y2="{py + 598}" stroke="#9A9EAB" stroke-width="1.6"/>'
b += text(ix, py + 666, 'Not needed: your academy platform hosts the site and its HTTPS.', 16, MUTED)
callouts = [(py + 120, 'Check the name', 'exact spelling, right ending'),
            (py + 216, 'Your name, your email', 'never an agency'),
            (py + 306, 'Privacy on', 'keeps your details private'),
            (py + 382, 'Auto-renew on', 'and a card that stays valid'),
            (py + 596, 'Skip the add-ons', 'buy only the domain')]
for n, (cy, t, s) in enumerate(callouts, 1):
    b += f'<path d="M{px + pw - 8} {cy} H 748" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 6"/>'
    b += num_badge(770, cy, n) + text(806, cy - 2, t, 23, INK, 700, font=F_HEAD, ls=-0.4) + text(806, cy + 26, s, 18, MUTED)
b += text(60, H - 28, 'Illustrative checkout. Screens differ by registrar. Typical .in / .com price: about ₹600–1,200 a year.', 16, MUTED)
b += signature(W, H)
save('registrar-checkout', svg(W, H, b, 'What to set when you buy a domain name for your coaching institute: your own name and email, privacy protection, auto-renew, and skip hosting add-ons'))

# 5. DNS records ------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['How DNS *points your domain*'], 52)
b += lines(62, 150, ['Your registrar holds the records. Each one has one job.'], 22)
# student
b += white_panel(60, 330, 300, 230, 26)
b += f'<rect x="88" y="358" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon('phone', 104, 374, 28, '#fff', 2)
b += text(166, 386, 'A student', 22, INK, 700, font=F_HEAD) + text(166, 412, 'types', 18, MUTED)
b += f'<rect x="88" y="452" width="244" height="52" rx="26" fill="#F4F6FF"/>' + icon('lock', 104, 465, 24, GREEN, 2.2) + text(138, 486, 'youracademy.in', 20, INK, 600)
b += arrow('M368 445 H 420', BLUE, 4)
# DNS zone
b += f'<g filter="url(#sh)"><rect x="432" y="200" width="380" height="580" rx="28" fill="{NAVY_TILE}"/></g>'
b += eyebrow(462, 246, 'DNS at your registrar', '#9FB0FF')
recs = [('TXT', 'Proves the domain', 'is yours'),
        ('CNAME / A', 'Points the website', 'to your academy'),
        ('MX', 'Sends email to your', 'mail provider')]
for k, (r, l1, l2) in enumerate(recs):
    y = 278 + k * 166
    hl = k == 1
    b += f'<rect x="462" y="{y}" width="320" height="136" rx="20" fill="{BLUE if hl else "#2A2E44"}"/>'
    b += text(488, y + 46, r, 28, '#fff', 800, font=F_MONO, ls=0)
    b += text(488, y + 84, l1, 19, '#fff', opacity=.85) + text(488, y + 110, l2, 19, '#fff', opacity=.85)
targets = [('Verified', 'The studio checks it', 'tick'),
           ('Your academy', 'HTTPS on', 'globe'),
           ('Your inbox', 'Workspace or Zoho', 'mail')]
for k, (t, s, ic) in enumerate(targets):
    y = 278 + k * 166 + 16
    b += arrow(f'M790 {y + 52} H 850', BLUE if k == 1 else INK, 3)
    b += pill_card(862, y, 300, t, s, ic, h=104, tile=BLUE if k == 1 else NAVY_TILE, title_size=24)
b += text(60, H - 28, 'Record names and values are illustrative. Copy the exact records your studio shows.', 16, MUTED)
b += signature(W, H)
save('dns-records', svg(W, H, b, 'How DNS records connect a coaching institute domain: a TXT record proves ownership, a CNAME or A record points the website to the academy, an MX record routes email'))

# 6. connect in the studio --------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Connect it *in the studio*'], 54)
b += lines(62, 150, ['Own branding  ›  Domain  ›  Connect a domain'], 22, INK)
b += laptop(80, 212, 660, SHOT)
b += text(80, 724, 'Studio preview · sample data', 15, MUTED)
steps = [('Open Domain', ['Own branding › Domain,', 'then Connect a domain']),
         ('Copy the records', ['Paste them into your', "registrar's DNS page"]),
         ('Wait for Connected', ['Verification and HTTPS', 'happen on their own'])]
for k, (t, s) in enumerate(steps):
    y = 230 + k * 160
    b += num_badge(822, y + 22, k + 1, 24)
    b += text(862, y + 32, t, 28, INK, 800, font=F_HEAD, ls=-0.9)
    b += lines(862, y + 70, s, 20, MUTED, 1.4)
for k, (t, s, ic) in enumerate([('Free to connect', 'on every plan', 'tag'),
                                 ('Free address stays', 'you.allcoaching.in', 'link'),
                                 ('HTTPS on', 'set up for you', 'lock')]):
    b += pill_card(60 + k * 375, 790, 350, t, s, ic, h=104, tile=NAVY_TILE if k != 2 else BLUE, title_size=24)
b += signature(W, H)
save('connect-in-studio', svg(W, H, b, 'How to connect a domain to your academy in the AllCoaching studio: Own branding, Domain, Connect a domain, copy the DNS records, wait for Connected with HTTPS on'))

# 7. after you save the records ---------------------------------------------------
W, H = 1220, 720
b = headline(60, 100, ['After you *save the records*'], 52)
b += lines(62, 150, ['What happens next, and how long it usually takes'], 22)
nodes = [('Records saved', 'at your registrar', 'file'),
         ('Records spread', 'across networks', 'globe'),
         ('Verified', 'domain is yours', 'tick'),
         ('HTTPS on', 'padlock appears', 'lock')]
b += f'<line x1="150" y1="290" x2="1070" y2="290" stroke="{BLUE}" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
for k, (t, s, ic) in enumerate(nodes):
    cx = 150 + k * 306.7
    last = k == 3
    b += f'<g filter="url({"#shB" if last else "#sh"})"><circle cx="{cx}" cy="290" r="54" fill="{BLUE if last else NAVY_TILE}"/></g>' + icon(ic, cx - 20, 270, 40, '#fff', 2)
    b += text(cx, 390, t, 26, INK, 800, 'middle', F_HEAD, -0.8) + text(cx, 422, s, 19, MUTED, anchor='middle')
b += white_panel(60, 480, 1100, 150, 26)
b += f'<rect x="92" y="514" width="80" height="80" rx="20" fill="{BLUE_TINT}"/>' + icon('clock', 112, 534, 40, BLUE, 2)
b += text(200, 548, 'Usually within a few hours', 30, INK, 800, font=F_HEAD, ls=-1)
b += text(200, 586, 'DNS can take up to 24–48 hours to reach every network. Your free address keeps working meanwhile.', 19, MUTED)
b += text(60, H - 28, 'Typical times, not a promise. They depend on your registrar and on DNS caching.', 16, MUTED)
b += signature(W, H)
save('after-you-save', svg(W, H, b, 'What happens after you add DNS records for your coaching institute domain: records spread, the domain is verified and HTTPS turns on, usually within a few hours'))

# 8. mistakes ---------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Domain mistakes', 'that cost you.'], 54)
for i, t in enumerate(['Agency owns the domain', 'Hyphens and numbers', 'Exam year in the name', 'Auto-renew switched off', 'Email records deleted']):
    b += tape(40 + (i % 2) * 22, 230 + i * 100, 500, t, -1.4 if i % 2 else 1.0, 30)
b += hand(330, 790, ['Site down', 'again?'], 40, INK, -6) + arrow('M300 800 C 250 820, 210 800, 190 770', INK, 3)
b += lockup(1180, 50, 0.62, True, 'end')
b += headline(650, 230, ['Do this', '*instead.*'], 64)
for i, t in enumerate(['Register it in your own name', 'One clean, short name', 'A name that lasts for years', 'Auto-renew and reminders on', 'Leave email (MX) records alone']):
    b += check_row(656, 400 + i * 74, t, 25)
save('domain-mistakes', svg(W, H, b, 'Common domain name mistakes coaching institutes make and what to do instead', ('split', 600)))
