"""Graphics for /blog/accept-upi-payments-for-online-courses.

Run:  python .claude/skills/academy-guide-blog/graphics/accept-upi-payments-for-online-courses.py
Then: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/accept-upi-payments-for-online-courses
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
OUT = os.path.join(ROOT, 'assets', 'blog', 'accept-upi-payments-for-online-courses')
os.makedirs(OUT, exist_ok=True)


def save(name, doc):
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', name)


def checkout_phone(x, y, w=300, paid=False):
    """A drawn phone showing a simple UPI checkout screen (illustrative, not a real app)."""
    h = w * 2.0
    r = w * .16
    b = w * .045
    sx, sy, sw = x + b, y + b, w - 2 * b
    out = (f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#121317"/></g>'
           f'<rect x="{sx}" y="{sy}" width="{sw}" height="{h - 2 * b}" rx="{r - b}" fill="#fff"/>'
           f'<rect x="{x + w * .36}" y="{sy + 12}" width="{w * .28}" height="{w * .07}" rx="{w * .035}" fill="#000"/>')
    px = sx + 22
    out += text(px, sy + 78, 'youracademy.in', 15, MUTED)
    out += text(px, sy + 116, 'SSC CGL Maths', 22, INK, 800, font=F_HEAD, ls=-0.6)
    out += text(px, sy + 142, 'Hindi medium · 120 lessons', 15, MUTED)
    out += f'<rect x="{px}" y="{sy + 162}" width="{sw - 44}" height="1.5" fill="{LINE}"/>'
    out += text(px, sy + 196, 'Total', 16, MUTED) + text(sx + sw - 22, sy + 196, '₹1,999', 22, INK, 800, 'end', F_HEAD)
    out += eyebrow(px, sy + 240, 'Pay with UPI', MUTED)
    for k, app in enumerate(['Google Pay', 'PhonePe', 'Paytm', 'Any UPI app']):
        yy = sy + 256 + k * 54
        sel = k == 0
        out += (f'<rect x="{px}" y="{yy}" width="{sw - 44}" height="44" rx="12" fill="{BLUE_TINT if sel else "#F5F6FA"}"'
                f'{" stroke=" + chr(34) + BLUE + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34) if sel else ""}/>')
        out += f'<circle cx="{px + 22}" cy="{yy + 22}" r="8" fill="none" stroke="{BLUE if sel else "#B5BAC8"}" stroke-width="2.5"/>'
        if sel:
            out += f'<circle cx="{px + 22}" cy="{yy + 22}" r="4" fill="{BLUE}"/>'
        out += text(px + 42, yy + 28, app, 16, INK, 600 if sel else 400)
    by = sy + 256 + 4 * 54 + 14
    if paid:
        out += f'<rect x="{px}" y="{by}" width="{sw - 44}" height="52" rx="16" fill="{GREEN}"/>'
        out += icon('tick', px + 18, by + 13, 26, '#fff', 3) + text(px + 52, by + 33, 'Paid · access open', 17, '#fff', 700, font=F_HEAD)
    else:
        out += f'<rect x="{px}" y="{by}" width="{sw - 44}" height="52" rx="16" fill="{BLUE}"/>'
        out += text(sx + sw / 2, by + 33, 'Pay ₹1,999', 19, '#fff', 700, 'middle', F_HEAD)
    return out


# 1. cover --------------------------------------------------------------------
b = lockup(72, 60, 1.0)
b += headline(80, 300, ['Accept *UPI payments*', 'for your courses.'], 80)
b += lines(84, 476, ['A step-by-step guide for Indian educators.'], 30, MUTED)
b += check_row(84, 566, 'KYC with PAN and a bank account', 26)
b += check_row(84, 626, 'Checkout on your own course page', 26)
b += check_row(84, 686, 'Course access opens on its own', 26)
b += checkout_phone(890, 130, 310)
b += pill_card(1170, 330, 370, 'Payment received', '₹1,999 · UPI', 'card', tile=BLUE)
b += pill_card(1170, 480, 370, 'Access opened', 'Course unlocked', 'tick')
b += pill_card(1170, 630, 370, 'Payout', 'To your bank account', 'home')
b += text(80, 860, 'Illustrative checkout. App names belong to their owners.', 16, MUTED)
save('cover', svg(1600, 900, b, 'Accepting UPI payments for an online course on your own academy checkout'))

# 2. how the money flows -----------------------------------------------------------
W, H = 1220, 760
b = headline(60, 100, ['How a UPI course payment', '*reaches your bank*'], 52)
cards = [('phone', 'Step 1', 'Student pays', ['Taps Pay on your', 'course page, approves', 'in their UPI app.']),
         ('bolt', 'Step 2', 'UPI moves it', ['Bank to bank, over', 'the UPI network run', 'by NPCI.']),
         ('shield', 'Step 3', 'Gateway checks', ['Marks the order paid,', 'so your platform can', 'open course access.']),
         ('home', 'Step 4', 'Settlement', ['Gateway pays your', 'verified bank account,', 'minus its fee.'])]
for i, (ic, step, title, desc) in enumerate(cards):
    x = 60 + i * 282
    y = 240
    b += white_panel(x, y, 252, 400, 26)
    tile = BLUE if i == 3 else NAVY_TILE
    b += f'<rect x="{x + 26}" y="{y + 28}" width="64" height="64" rx="18" fill="{tile}"/>' + icon(ic, x + 42, y + 44, 32, '#fff', 2)
    b += eyebrow(x + 26, y + 136, step)
    b += text(x + 26, y + 184, title, 28, INK, 800, font=F_HEAD, ls=-1.0)
    b += lines(x + 26, y + 236, desc, 19, MUTED, 1.45)
    if i < 3:
        b += arrow(f'M{x + 257} 440 H {x + 270}', BLUE, 3)
b += text(60, H - 28, 'Simplified. Timing and fees depend on your gateway or platform.', 16, MUTED) + signature(W, H)
save('upi-payment-flow', svg(W, H, b, 'How a UPI payment for an online course moves from student to gateway to the educator bank account'))

# 3. three ways --------------------------------------------------------------------
W, H = 1220, 900
b = headline(60, 100, ['Three ways to *collect UPI*'], 54) + lines(62, 150, ['What each route does for you after the student pays'], 22)
cols = [(['Personal', 'UPI QR'], 'image', 'Manual', [('No setup at all', True), ('Proof is a screenshot', False), ('You add every student', False), ('Mixes personal money', False)]),
        (['Gateway', 'payment link'], 'link', 'Partly automatic', [('Verified payment record', True), ('UPI and cards', True), ('Access still by hand', False), ('Separate from course', False)]),
        (['Checkout in', 'your academy'], 'card', 'Automatic', [('Verified payment record', True), ('UPI and cards', True), ('Access opens on its own', True), ('Sale linked to student', True)])]
for k, (title, ic, tag, rows) in enumerate(cols):
    x = 60 + k * 375
    y = 200
    hl = k == 2
    b += white_panel(x, y, 350, 610, 28)
    if hl:
        b += f'<rect x="{x}" y="{y}" width="350" height="610" rx="28" fill="none" stroke="{BLUE}" stroke-width="3"/>'
    b += f'<rect x="{x + 28}" y="{y + 30}" width="64" height="64" rx="18" fill="{BLUE if hl else NAVY_TILE}"/>' + icon(ic, x + 44, y + 46, 32, '#fff', 2)
    tw = 22 + len(tag) * 9.6
    b += f'<rect x="{x + 322 - tw}" y="{y + 44}" width="{tw}" height="36" rx="18" fill="{BLUE if hl else "#F1F2F6"}"/>'
    b += text(x + 322 - tw / 2, y + 68, tag, 15, '#fff' if hl else MUTED, 700, 'middle')
    t1, t2 = title
    b += text(x + 28, y + 158, t1, 32, INK, 800, font=F_HEAD, ls=-1.2)
    if t2:
        b += text(x + 28, y + 196, t2, 32, INK, 800, font=F_HEAD, ls=-1.2)
    for i, (r, ok) in enumerate(rows):
        b += check_row(x + 28, y + 290 + i * 76, r, 20, ok)
b += text(60, H - 28, 'General comparison. Exact features depend on the gateway or platform you choose.', 16, MUTED) + signature(W, H)
save('three-ways-to-collect-upi', svg(W, H, b, 'Three ways to accept UPI payment for online courses: personal UPI QR, gateway payment link, checkout in your own academy'))

# 4. KYC checklist -------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['What to keep ready *before KYC*'], 54)
b += lines(62, 150, ['For an individual educator without a registered business, on Razorpay'], 22)
items = [('Personal PAN', 'Checked against your KYC record', 'tag'),
         ('Bank account + IFSC', 'Verified with a ₹1 test deposit', 'home'),
         ('Mobile linked to Aadhaar', 'For CKYC or DigiLocker OTP', 'phone'),
         ('Website or app link', 'Where students will pay', 'globe'),
         ('GSTIN, if you have one', 'A no-GSTIN route exists', 'file'),
         ('Photo ID copy', 'Only if auto-fetch fails', 'users')]
for i, (t, s, ic) in enumerate(items):
    x = 60 + (i % 2) * 560
    y = 210 + (i // 2) * 160
    b += pill_card(x, y, 540, t, s, ic, h=120, tile=BLUE if i < 2 else NAVY_TILE)
b += f'<rect x="60" y="700" width="1100" height="66" rx="20" fill="{BLUE_TINT}"/>' + icon('shield', 84, 717, 32, BLUE, 2)
b += text(132, 742, 'If the automatic checks fail, the fallback is a short video KYC with PAN and Aadhaar in hand.', 19, INK, 500)
b += text(60, H - 28, 'Source: Razorpay KYC documentation, checked October 2026. Other gateways differ.', 16, MUTED) + signature(W, H)
save('kyc-checklist', svg(W, H, b, 'Checklist of documents an educator needs before payment gateway KYC to accept UPI payments: PAN, bank account, Aadhaar-linked mobile, website link'))

# 5. fee maths ----------------------------------------------------------------------
W, H = 1220, 860
b = headline(60, 100, ['What a ₹1,999 UPI sale', '*costs on a gateway*'], 52)
b += white_panel(60, 230, 680, 540, 28, big=True)
b += eyebrow(96, 284, 'One course sale · standard pricing')
rows = [('Course price paid by student', '₹1,999.00', INK, 400),
        ('UPI MDR (bank charge)', '₹0.00', INK, 400),
        ('Gateway platform fee (2%)', '− ₹39.98', RED, 400),
        ('GST on that fee (18%)', '− ₹7.20', RED, 400)]
for i, (l, v, c, w_) in enumerate(rows):
    y = 350 + i * 76
    b += text(96, y, l, 22, INK if i == 0 else MUTED) + text(704, y, v, 24, c, 700, 'end', F_HEAD)
    b += f'<rect x="96" y="{y + 26}" width="608" height="1.5" fill="{LINE}"/>'
b += f'<rect x="80" y="642" width="640" height="96" rx="20" fill="{BLUE_TINT}"/>'
b += text(104, 700, 'Settled to you', 24, INK, 700, font=F_HEAD) + text(696, 702, '₹1,951.82', 36, BLUE, 800, 'end', F_HEAD, -1)
b += pill_card(790, 260, 370, '₹0 MDR', 'on bank-to-bank UPI', 'bolt', h=120)
b += pill_card(790, 410, 370, '≈ ₹4,718', 'in fees per 100 sales', 'chart', h=120, tile=BLUE)
b += pill_card(790, 560, 370, '₹0 setup', 'no yearly maintenance', 'card', h=120)
b += text(60, H - 28, 'Illustrative. Razorpay standard rates, checked October 2026. Your rate may differ.', 16, MUTED) + signature(W, H)
save('upi-fee-maths', svg(W, H, b, 'Illustrative fee maths for a ₹1,999 UPI payment for an online course on a standard payment gateway plan'))

# 6. before / after -----------------------------------------------------------------
W, H = 1220, 900
b = eyebrow(56, 84, 'Before', RED) + headline(56, 150, ['UPI on WhatsApp'], 48)
b += logo_tile(56, 200, logo_whatsapp, 76)
for i, t in enumerate(['Sent the screenshot?', 'Who paid for batch 2?', 'Add to group by hand', 'Check bank app again']):
    b += tape(40 + (i % 2) * 20, 320 + i * 100, 500, t, -1.3 if i % 2 else 1.0, 30)
b += hand(260, 236, ['Payment', 'pending?'], 40, INK, -6) + arrow('M240 250 C 200 250, 170 235, 148 228', INK, 3)
b += eyebrow(666, 84, 'After', BLUE) + headline(666, 150, ['Checkout on', '*your academy*'], 48)
for i, t in enumerate(['Student pays on your course page', 'Access opens on its own', 'Every payment in Transactions', 'Payout to your bank']):
    b += check_row(672, 330 + i * 76, t, 23)
b += phone(1000, 580, 110, 'studio-mobile.jpg')
b += text(672, 650, 'Studio preview · sample data', 15, MUTED)
b += text(56, H - 28, 'Logos belong to their owners.', 16, MUTED) + signature(W, H)
save('before-after-upi', svg(W, H, b, 'Before and after: collecting UPI screenshots on WhatsApp compared with automatic checkout and course access on your own academy', ('split', 610)))

# 7. mistakes ------------------------------------------------------------------------
W, H = 1220, 900
b = headline(56, 110, ['Still collecting', 'fees like this?'], 56)
for i, t in enumerate(['Screenshot as proof', 'Personal account', 'No refund policy', 'QR image in bio', 'Never tested on 4G']):
    b += tape(40 + (i % 2) * 22, 240 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 32)
b += hand(330, 800, ['Fake screenshot', 'again?'], 38, INK, -6)
b += headline(650, 190, ['Do this', '*instead.*'], 62)
for i, t in enumerate(['Gateway-verified payments', 'A separate fees account', 'Written refund policy', 'A course page link', 'Test on a budget phone']):
    b += check_row(656, 360 + i * 78, t, 25)
b += signature(W, H)
save('upi-payment-mistakes', svg(W, H, b, 'Common UPI payment mistakes when selling online courses and what to do instead', ('split', 600)))

# 8. academy checkout promo ------------------------------------------------------------
W, H = 1220, 1000
b = lockup(60, 54, 0.8)
b += headline(60, 250, ['UPI checkout,', '*built into*', '*your academy.*'], 62)
b += lines(64, 440, ['Students pay with UPI or cards.', 'Access opens. Payouts go to', 'your bank through Razorpay.'], 24, MUTED, 1.4)
b += laptop(560, 120, 520, 'studio-desktop.jpg')
b += phone(1010, 220, 170, 'studio-mobile.jpg')
b += text(560, 520, 'AllCoaching Studio preview · sample data', 14, MUTED)
for k, (lab, ic, sub) in enumerate([('UPI & cards', 'card', 'Every plan'), ('Access', 'bolt', 'Automatic'), ('Payouts', 'home', 'Via Razorpay'),
                                     ('Website', 'globe', 'Your domain'), ('Your app', 'phone', 'Android')]):
    b += feature_tile(150 + k * 230, 600, lab, ic, sub, 88)
b += button(60, 850, 540, 'Start your academy', 92, 36)
b += text(640, 890, '0% commission on Growth and Pro', 28, INK, 800, font=F_HEAD, ls=-0.8) + text(640, 926, '7 days free · no card needed', 21, MUTED)
save('academy-upi-checkout', svg(W, H, b, 'AllCoaching Studio on a laptop and phone: UPI and card checkout, automatic access and Razorpay payouts on every plan'))
