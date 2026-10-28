"""Graphics for /blog/recorded-lecture-hosting-cheap-india-for-teachers.

Run:  python .claude/skills/academy-guide-blog/graphics/recorded-lecture-hosting-cheap-india-for-teachers.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/recorded-lecture-hosting-cheap-india-for-teachers

Plan facts follow the final pricing (2026-10-28): Starter ₹6,999/yr + 10%, Growth ₹7,999/mo and Pro ₹14,999/mo
at 0% commission; storage/streaming 512 GB/100 GB, 1 TB/1 TB, 2 TB/2 TB; Extend ₹499 per 100 GB storage a month,
₹399 per 100 GB streaming. Hour figures are illustrative.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'recorded-lecture-hosting-cheap-india-for-teachers')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


# 1. cover ------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Recorded lecture', 'hosting, *the real cost*'], 80)
b += lines(84, 470, ['Storage is cheap. Delivery is the bill.'], 32, MUTED)
b += check_row(84, 560, 'Storage and streaming included in every plan', 26)
b += check_row(84, 620, 'Lectures play behind your students\' login', 26)
b += check_row(84, 680, '0% commission on Growth and Pro', 26)
b += laptop(860, 210, 600, 'studio-desktop.jpg')
b += phone(1390, 330, 150, 'studio-mobile.jpg')
b += pill_card(800, 650, 420, 'No per-view bill', 'Hosting priced into your plan', 'video')
b += text(860, 190, 'Studio preview · sample data', 15, MUTED)
save('cover', svg(1600, 900, b, 'Recorded lecture hosting in India: storage is cheap, delivery is the real cost; AllCoaching includes storage and streaming in every plan'))

# 2. cost components ---------------------------------------------------------
W, H = 1220, 760
b = headline(60, 100, ['Where the hosting *bill comes from*'], 52)
b += lines(62, 150, ['Three costs, very different sizes'], 22)
rows = [('Storage', 'Keeping the video files', 'Grows with library size', 170, 'server'),
        ('Encoding', 'Making every quality for every phone', 'Once per upload', 300, 'layers'),
        ('Delivery (bandwidth)', 'Streaming to every student, every view', 'Grows with every view', 820, 'trend')]
for i, (t, s, g, w, ic) in enumerate(rows):
    y = 210 + i * 160
    b += white_panel(60, y, 1100, 136, 24)
    b += f'<rect x="88" y="{y + 38}" width="60" height="60" rx="16" fill="{NAVY_TILE}"/>' + icon(ic, 104, y + 54, 28, '#fff')
    b += text(172, y + 58, t, 26, INK, 700, font=F_HEAD, ls=-0.6) + text(172, y + 92, s, 18, MUTED)
    col = BLUE if i == 2 else '#C9D0E8'
    b += f'<rect x="560" y="{y + 44}" width="{w * 0.65:.0f}" height="26" rx="13" fill="{col}"/>'
    b += text(560, y + 104, g, 17, BLUE if i == 2 else MUTED, 600)
b += text(62, 720, 'Bar lengths show relative size, illustrative.', 16, MUTED)
b += signature(W, H)
save('cost-components', svg(W, H, b, 'Video hosting costs: storage is small, encoding is once per upload, delivery bandwidth is the large cost that grows with every view'))

# 3. options compared --------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Hosting options, *compared*'], 52)
b += lines(62, 150, ['What each route costs as students watch more'], 22)
opts = [('YouTube unlisted', 'Free, but anyone with the link can watch', 'no'),
        ('Vimeo', 'Plan tiers with storage and feature limits', 'part'),
        ('AWS S3 + CloudFront', 'Billed per GB delivered; you build the player', 'no'),
        ('Bunny / Cloudflare Stream', 'Low per-GB price, still metered', 'part'),
        ('Your own server', 'Server, bandwidth, upkeep, no CDN', 'no'),
        ('Teaching platform (AllCoaching)', 'Storage and streaming included in the plan', 'yes')]
b += text(830, 205, 'Flat cost as views grow?', 17, MUTED, 600)
for i, (t, s, v) in enumerate(opts):
    y = 225 + i * 104
    hl = v == 'yes'
    b += white_panel(60, y, 1100, 88, 20)
    if hl:
        b += f'<rect x="60" y="{y}" width="1100" height="88" rx="20" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += text(92, y + 40, t, 23, INK, 700, font=F_HEAD, ls=-0.5) + text(92, y + 70, s, 17, MUTED)
    lab, col = {'yes': ('Yes', GREEN), 'part': ('Partly', '#B7791F'), 'no': ('No', RED)}[v]
    b += f'<rect x="900" y="{y + 26}" width="120" height="38" rx="19" fill="{col}" opacity=".12"/>'
    b += text(960, y + 52, lab, 19, col, 700, anchor='middle')
b += signature(W, H)
save('options', svg(W, H, b, 'Recorded lecture hosting options compared: YouTube unlisted, Vimeo, AWS, Bunny or Cloudflare Stream, own server and a teaching platform with hosting included'))

# 4. hidden costs ------------------------------------------------------------
W, H = 1220, 760
b = headline(60, 100, ['The *hidden bill* of DIY hosting'], 52)
b += lines(62, 150, ['What a storage price leaves out'], 22)
items = [('Bandwidth that grows with views', 'trend'), ('Encoding and a video player', 'play'),
         ('Student logins and access control', 'shield'), ('Keys, updates and broken embeds', 'puzzle')]
for i, (t, ic) in enumerate(items):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 170
    b += pill_card(x, y, 520, t, None, ic, h=120, title_size=24)
b += tape(80, 600, 330, 'Bill went up again?', rot=-2, size=30)
b += hand(470, 640, ['success = a bigger hosting bill'], 32, RED, -3)
b += signature(W, H)
save('hidden-costs', svg(W, H, b, 'Hidden costs of DIY video hosting: bandwidth that grows with views, encoding and a player, access control, and maintenance time'))

# 5. plans and allowances -----------------------------------------------------
W, H = 1220, 840
b = headline(60, 100, ['Hosting *included* in every plan'], 52)
b += lines(62, 150, ['Video storage and streaming on AllCoaching (prices + GST)'], 22)
plans = [('Starter', '₹6,999', 'a year · 10% per sale', '512 GB', '100 GB', False),
         ('Growth', '₹7,999', 'a month · 0% commission', '1 TB', '1 TB', True),
         ('Pro', '₹14,999', 'a month · 0% commission', '2 TB', '2 TB', True)]
for i, (n, p, per, st, sm, zero) in enumerate(plans):
    x = 60 + i * 372
    b += white_panel(x, 200, 348, 470, 26)
    if zero:
        b += f'<rect x="{x + 24}" y="226" width="182" height="34" rx="17" fill="{BLUE}"/>' + text(x + 115, 249, '0% commission', 17, '#fff', 700, anchor='middle')
    b += text(x + 28, 310, n, 30, INK, 700, font=F_HEAD, ls=-0.8)
    b += text(x + 28, 370, p, 46, INK, 800, font=F_HEAD, ls=-1.5) + text(x + 28, 402, per, 17, MUTED)
    b += f'<line x1="{x + 28}" y1="432" x2="{x + 320}" y2="432" stroke="{LINE}" stroke-width="2"/>'
    b += text(x + 28, 478, 'Video storage', 17, MUTED) + text(x + 28, 512, st, 30, BLUE, 700, font=F_HEAD)
    b += text(x + 28, 562, 'Streaming a month', 17, MUTED) + text(x + 28, 596, sm, 30, BLUE, 700, font=F_HEAD)
    b += text(x + 28, 640, 'YouTube video: unlimited', 16, MUTED)
b += text(62, 716, 'Need more? Extend from the studio: ₹499 a month per 100 GB of storage, ₹399 per 100 GB of streaming.', 18, INK, 600)
b += text(62, 748, 'At a limit only uploaded video pauses; website, app, YouTube video and live classes keep running.', 16, MUTED)
b += signature(W, H)
save('plans', svg(W, H, b, 'AllCoaching hosting by plan: Starter 512 GB storage and 100 GB streaming, Growth 1 TB and 1 TB, Pro 2 TB and 2 TB, with 0% commission on Growth and Pro'))

# 6. checklist -----------------------------------------------------------------
W, H = 1220, 800
b = headline(60, 100, ['What good lecture hosting *needs*'], 52)
b += lines(62, 150, ['Raw storage gives you one piece. Real hosting is the whole set.'], 22)
needs = [('Fast delivery across India', 'CDN servers close to students'), ('Smooth playback on weak networks', 'Adaptive quality switching'),
         ('A reliable player', 'Plays inside your website and app'), ('Phone-first playback', 'Most students watch on mobile'),
         ('Access control', 'Only students who paid can watch'), ('A known monthly cost', 'No per-view surprise bill')]
for i, (t, s) in enumerate(needs):
    x = 60 + (i % 2) * 560
    y = 200 + (i // 2) * 170
    b += white_panel(x, y, 530, 140, 24)
    b += f'<circle cx="{x + 56}" cy="{y + 70}" r="24" fill="{BLUE}"/>' + icon('tick', x + 44, y + 58, 24, '#fff', 2.6)
    b += text(x + 100, y + 64, t, 23, INK, 700, font=F_HEAD, ls=-0.5) + text(x + 100, y + 96, s, 18, MUTED)
b += signature(W, H)
save('checklist', svg(W, H, b, 'Checklist for recorded lecture hosting: CDN delivery, adaptive streaming, a player, mobile playback, access control and a known monthly cost'))
