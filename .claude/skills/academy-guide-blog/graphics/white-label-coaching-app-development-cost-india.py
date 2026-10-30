"""Graphics for /blog/white-label-coaching-app-development-cost-india.

Run:  python .claude/skills/academy-guide-blog/graphics/white-label-coaching-app-development-cost-india.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/white-label-coaching-app-development-cost-india

Competitor figures come only from .claude/skills/academy-guide-blog/data/competitors.json (checked 24 Oct 2026).
Store fees: Google Play Console Help (US$25 one-time) and Apple Developer enrollment (US$99 a year), checked Oct 2026.
AllCoaching year-one maths: plan price + platform fee on sales, before GST (illustrative).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'white-label-coaching-app-development-cost-india')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def inr(v):
    n = int(round(v))
    s = str(n)
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts) + ',' + tail
    return '₹' + s


# 1. cover --------------------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['What a coaching app', '*really costs*', 'in India'], 72)
b += lines(84, 520, ['Custom build, white-label vendor or academy', 'platform: every cost line, priced honestly.'], 28, MUTED)
b += check_row(84, 650, 'Store fees from Google and Apple', 25)
b += check_row(84, 708, 'Published vendor prices, sourced', 25)
b += check_row(84, 766, 'Questions to ask before you sign', 25)
b += white_panel(1000, 170, 530, 560, 32, big=True)
b += eyebrow(1040, 232, 'Three ways to get an app')
routes = [('server', 'Custom build', 'Quoted by scope'),
          ('layers', 'White-label vendor', 'Setup + yearly fee'),
          ('home', 'Academy platform', 'Yearly plan, app included')]
for i, (ic, t, s) in enumerate(routes):
    y = 270 + i * 150
    hl = i == 2
    if hl:
        b += f'<rect x="1022" y="{y - 14}" width="486" height="132" rx="22" fill="{BLUE_TINT}"/>'
    b += f'<rect x="1040" y="{y + 12}" width="64" height="64" rx="18" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, 1056, y + 28, 32, '#fff', 2)
    b += text(1126, y + 42, t, 30, INK, 800, font=F_HEAD, ls=-0.8)
    b += text(1126, y + 76, s, 21, MUTED)
b += text(80, 860, 'Figures checked on official pages, October 2026.', 16, MUTED)
save('cover', svg(1600, 900, b, 'White label coaching app development cost in India: custom build vs white-label vendor vs academy platform'))

# 2. three routes -------------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Three ways to get', 'your *coaching app*'], 52)
cols = [('server', 'Custom build', 'An agency or developer', [('Upfront', 'Build quoted by scope'), ('Every year', 'Hosting, fixes, updates'),
                                                             ('Changes', 'A paid developer task'), ('You own', 'Code, if the contract says')]),
        ('layers', 'White-label vendor', 'Their app, your brand', [('Upfront', 'Setup fee, if any'), ('Every year', 'Licence or app add-on'),
                                                                   ('Changes', "On the vendor's roadmap"), ('You own', 'Ask: data and listing')]),
        ('home', 'Academy platform', 'You build it yourself', [('Upfront', 'Free trial, then a plan'), ('Every year', 'Plan + fee on sales'),
                                                               ('Changes', 'You, in the studio'), ('You own', 'Brand, domain, data')])]
for k, (ic, t, s, rows) in enumerate(cols):
    x = 60 + k * 375
    hl = k == 2
    b += white_panel(x, 210, 350, 700, 28, big=hl)
    if hl:
        b += f'<rect x="{x}" y="210" width="350" height="700" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += f'<rect x="{x + 28}" y="240" width="64" height="64" rx="18" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, x + 44, 256, 32, '#fff', 2)
    b += text(x + 28, 362, t, 29, INK, 800, font=F_HEAD, ls=-0.9)
    b += text(x + 28, 396, s, 19, MUTED)
    for i, (lab, val) in enumerate(rows):
        y = 470 + i * 106
        b += f'<rect x="{x + 28}" y="{y - 34}" width="294" height="1.5" fill="{LINE}"/>'
        b += eyebrow(x + 28, y, lab, BLUE if hl else MUTED)
        b += text(x + 28, y + 36, val, 20, INK, 600)
b += text(60, H - 28, 'General comparison. Check each vendor\'s written terms.', 16, MUTED) + signature(W, H)
save('three-routes', svg(W, H, b, 'Coaching app development cost in India: custom build vs white-label vendor vs academy platform compared'))

# 3. cost stack -----------------------------------------------------------------------------
W, H = 1220, 1000
b = headline(60, 100, ['Every line in a', '*coaching app budget*'], 52)
items = [('phone', 'Design and build', 'Android, iOS, admin, website'),
         ('check', 'App store accounts', 'Google Play and Apple fees'),
         ('server', 'Hosting and backend', 'Servers, logins, database'),
         ('video', 'Video and live classes', 'Hosting, streaming, live room'),
         ('card', 'Payments', 'Gateway charges, fee on sales'),
         ('globe', 'Website and domain', 'Your own address, renewals'),
         ('bolt', 'Maintenance and updates', 'New Android and iOS rules'),
         ('trend', 'Marketing', 'Ads, content, your time')]
for i, (ic, t, s) in enumerate(items):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 160
    b += pill_card(x, y, 540, t, s, ic, h=124, tile=NAVY_TILE, title_size=26)
b += f'<rect x="60" y="860" width="1100" height="70" rx="20" fill="{BLUE_TINT}"/>'
b += text(90, 904, 'Most quotes price only the first line. Ask for all eight, for a full year.', 21, INK, 600)
b += signature(W, H)
save('cost-stack', svg(W, H, b, 'Coaching app development cost components: design and build, store accounts, hosting, video, payments, domain, maintenance and marketing'))

# 4. store accounts ---------------------------------------------------------------------------
W, H = 1220, 820
b = headline(60, 100, ['App store accounts:', 'the *fixed fees*'], 52)
stores = [('Google Play', 'US$25', 'one-time registration fee',
           ['New personal accounts (after 13 Nov 2023)', 'must run a closed test: 12 testers,', '14 days in a row.',
            '', 'From 31 Aug 2026, new apps and updates', 'must target Android 16 (API level 36).']),
          ('Apple App Store', 'US$99', 'per year, Apple Developer Program',
           ['Organisations enrol with a D-U-N-S', 'Number (free in most countries).',
            '', 'Guideline 4.2.6: apps from a template', 'service are rejected unless submitted', 'by the content provider.'])]
for k, (t, big, sub, rows) in enumerate(stores):
    x = 60 + k * 560
    b += white_panel(x, 200, 540, 520, 28, big=True)
    b += f'<rect x="{x + 28}" y="228" width="64" height="64" rx="18" fill="{NAVY_TILE}"/>' + icon('phone', x + 44, 244, 32, '#fff', 2)
    b += text(x + 112, 272, t, 30, INK, 800, font=F_HEAD, ls=-1)
    b += text(x + 32, 400, big, 72, BLUE, 800, font=F_HEAD, ls=-3)
    b += text(x + 32, 440, sub, 21, MUTED)
    b += f'<rect x="{x + 32}" y="474" width="476" height="1.5" fill="{LINE}"/>'
    b += lines(x + 32, 520, rows, 20, INK, 1.45)
b += text(60, H - 28, 'Sources: Google Play Console Help, Android Developers, Apple Developer. Checked Oct 2026.', 16, MUTED) + signature(W, H)
save('store-accounts', svg(W, H, b, 'Google Play US$25 one-time and Apple Developer Program US$99 a year: app store fees for a coaching app'))

# 5. published vendor prices ----------------------------------------------------------------------
W, H = 1220, 1040
b = headline(60, 100, ['What vendors *publish*', 'for a branded app'], 52)
vend = [('Classplus', '₹29,999 for 1 year', 'Android app + website. Fee on sales, GST and renewal not stated.', False),
        ('TagMango', '₹74,999 + GST', 'Branded Apps Stack, one-time setup, on top of a plan.', False),
        ('Exly', 'From ₹60,000 a year', 'Mobile app (iOS and Android) add-on to a plan.', False),
        ('Learnyst', '₹14,999 a month', 'Premium, billed monthly + taxes: branded Android app.', False),
        ('AllCoaching', '₹3,999 a month + GST', 'Android app on every plan, 0% commission. Yearly from ₹6,999 + 10%.', True)]
for i, (n, p, note, hl) in enumerate(vend):
    y = 200 + i * 148
    b += white_panel(60, y, 1100, 128, 24, big=hl)
    if hl:
        b += f'<rect x="60" y="{y}" width="1100" height="128" rx="24" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += text(92, y + 74, n, 28, BLUE if hl else INK, 800, font=F_HEAD, ls=-0.8)
    b += text(370, y + 58, p, 30, INK, 800, font=F_HEAD, ls=-1)
    b += text(370, y + 94, note, 19, MUTED)
b += text(60, H - 52, 'Official pricing pages, checked 24 Oct 2026. Not like-for-like: plans include different things.', 16, MUTED)
b += text(60, H - 28, 'Sources in the post.', 16, MUTED) + signature(W, H)
save('published-prices', svg(W, H, b, 'Published white label coaching app prices in India: Classplus, TagMango, Exly, Learnyst and AllCoaching, checked October 2026'))

# 6. hidden costs (problem vs fix) ------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Signed for', 'the app price?'], 56)
for i, t in enumerate(['Renewal price?', 'Fee on every sale', 'Apple app is extra', 'Setup fee', 'Data export?']):
    b += tape(40 + (i % 2) * 22, 240 + i * 104, 470, t, -1.4 if i % 2 else 1.0, 32)
b += hand(300, 800, ['Wait, that is', 'extra too?'], 36, INK, -6)
b += headline(650, 190, ['Ask for', '*the full year.*'], 62)
for i, t in enumerate(['Renewal price in writing', 'Fee on sales, GST shown', 'Which apps are included', 'Whose store account', 'Export your data any time']):
    b += check_row(656, 360 + i * 78, t, 24)
b += signature(W, H)
save('hidden-costs', svg(W, H, b, 'Hidden costs in a white label coaching app contract and what to ask for instead', ('split', 600)))

# 7. year-one cost on AllCoaching plans --------------------------------------------------------------
W, H = 1220, 1080
SALES = 1000000
plans = [('Starter', 'Yearly · 10% fee · Android and iOS app', 6999, 0.10),
         ('Growth', 'Yearly · 7.5% fee · Android and iOS app', 12999, 0.075),
         ('Pro', 'Yearly · 5% fee · Android and iOS app, 4K', 24999, 0.05),
         ('Starter', 'Monthly ₹3,999 × 12 · 0% commission', 47988, 0.0),
         ('Growth', 'Monthly ₹5,999 × 12 · 0% commission', 71988, 0.0),
         ('Pro', 'Monthly ₹7,999 × 12 · 0% · iOS app and 4K', 95988, 0.0)]
tot = [p + f * SALES for _, _, p, f in plans]
low = min(tot)
b = headline(60, 100, ['Year-one cost at', '*₹10 lakh of sales*'], 52)
b += white_panel(60, 200, 1100, 740, 28, big=True)
heads = [('Plan', 100, 'start'), ('Plan price', 640, 'end'), ('Fee on sales', 880, 'end'), ('Year one', 1110, 'end')]
for t_, x, a_ in heads:
    b += eyebrow(x, 262, t_, MUTED, a_)
for i, ((n, sub, p, f), t_) in enumerate(zip(plans, tot)):
    y = 290 + i * 106
    hl = t_ == low
    if hl:
        b += f'<rect x="80" y="{y}" width="1060" height="96" rx="20" fill="{BLUE_TINT}"/>'
    else:
        b += f'<rect x="100" y="{y}" width="1020" height="1.5" fill="{LINE}"/>'
    b += text(100, y + 46, n, 30, BLUE if hl else INK, 800, font=F_HEAD, ls=-1)
    b += text(100, y + 76, sub, 17, MUTED, 500)
    b += text(640, y + 58, inr(p), 26, INK, 600, 'end', F_HEAD)
    pct = ('%g' % (f * 100)) + '%'
    b += text(880, y + 58, (f'{pct} = {inr(f * SALES)}' if f else '0% = no fee'), 24, INK, 500, 'end', F_HEAD)
    b += text(1110, y + 58, inr(t_), 30, BLUE if hl else INK, 800, 'end', F_HEAD, -1)
b += text(60, 990, 'Below about ₹4 lakh of yearly sales, yearly Starter usually costs least; above that, a monthly 0% plan usually leaves more.', 18, INK, 600)
b += text(60, H - 28, 'Illustrative. Plan price and platform fee only, before GST. Gateway charges separate.', 16, MUTED) + signature(W, H)
save('year-one-cost', svg(W, H, b, 'Illustrative year-one cost of a coaching app with website on AllCoaching plans at ₹10 lakh of sales'))

# 8. vendor questions ------------------------------------------------------------------------------
W, H = 1220, 920
b = headline(60, 100, ['Ask these', '*before you sign*'], 52)
qs = ['What is the renewal price?', 'Is there a setup fee?', 'What is the fee on each sale?', 'Is GST included or extra?',
      'Are Android and iOS included?', 'Whose developer account?', 'Who pays the store fees?', 'Is a website included?',
      'Can I use my own domain?', 'Can I export my data?', 'Who makes changes, how fast?', 'What does support cover?']
for i, q in enumerate(qs):
    x = 60 + (i // 6) * 560
    y = 240 + (i % 6) * 100
    b += white_panel(x, y - 46, 540, 76, 22)
    b += num_badge(x + 40, y - 8, i + 1, 20)
    b += text(x + 76, y, q, 23, INK, 600)
b += text(60, H - 28, 'Get every answer in writing, for a full year of use.', 16, MUTED) + signature(W, H)
save('vendor-questions', svg(W, H, b, 'Twelve questions to ask a white label coaching app vendor before you sign'))

# 9. AllCoaching promo -----------------------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['Your own app.', '*No build*', '*project.*'], 62)
b += lines(64, 440, ['Website on your domain and your', 'own Android app on every plan.', 'iOS app on Pro or yearly plans.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('Android app', 'phone', 'Every plan'), ('iOS app', 'phone', 'Pro or yearly'), ('Website', 'globe', 'Your domain'),
                                     ('Live classes', 'users', 'Unlimited'), ('UPI & cards', 'card', 'Razorpay payouts')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += logo_tile(60, 790, logo_youtube, 56)
b += text(132, 826, 'Unlimited video via YouTube', 20, INK, 600)
b += button(60, 870, 540, 'Start your academy', 92, 36)
b += text(640, 910, '0% commission on monthly plans', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 946, '7 days free · no card needed', 21, MUTED)
b += text(1160, 826, 'Logos belong to their owners.', 14, MUTED, anchor='end')
save('academy-app-promo', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: own Android app on every plan, iOS on Pro monthly and every yearly plan, website on your domain'))
