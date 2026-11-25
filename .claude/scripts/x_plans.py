#!/usr/bin/env python3
"""Studio-style plan cards and compare table for the marketing site (owner, 2026-11-25).

Source of truth = the studio's own plan picker (allcoaching-educator-preact,
src/pages/Settings/sections/PlanPicker.tsx + Onboarding/v3/helpers.ts):
- yearly  Starter ₹6,999 (10%) · Growth ₹12,999 (7.5%) · Pro ₹24,999 (5%), fee + GST
- monthly Starter ₹3,999 · Growth ₹5,999 · Pro ₹7,999, 0% commission
- storage 512 GB / 1 TB / 3 TB yearly, 512 GB / 1 TB / 2 TB monthly; video 1080p / 1080p / 4K
- built-in live room 5 / 10 / 15 h yearly, 20 / 50 / 90 h monthly
- team seats 1 / 3 / 5 yearly, 5 / 10 / 20 monthly (owner, 22-Nov-2026)
- landing pages any 6 / any 12 / all; iOS on Growth and Pro after 30 days
- themes: Classic free on every plan; premium themes ₹10,000 each, one-time (no plan includes one)
Yearly is shown first (owner, 2026-11-25).

Writes assets/x/plans.html and assets/x/plans-compare.html, then splices them into every page
that has <!-- X PLANS --> ... <!-- /X PLANS --> or <!-- X COMPARE --> ... <!-- /X COMPARE --> markers.
"""
import glob
import os
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
TRIAL = 'https://studio.allcoaching.in/'


def inr(n):
    s = f'{n:,.2f}' if n != int(n) else f'{int(n):,}'
    # Indian grouping
    whole, _, dec = s.replace(',', '').partition('.')
    if len(whole) > 3:
        head, tail = whole[:-3], whole[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        whole = ','.join(parts + [tail])
    return '₹' + whole + ('.' + dec if dec else '')


PLANS = {
    'yearly': [
        dict(key='starter', name='Starter', blurb='For a new academy', price=6999, fee=10, storage='512 GB', stream='512 GB', video='1080p', live=5, seats=1, pages='Any 6', ios=False),
        dict(key='growth', name='Growth', blurb='For a growing academy', price=12999, fee=7.5, storage='1 TB', stream='1 TB', video='1080p', live=10, seats=3, pages='Any 12', ios=True),
        dict(key='pro', name='Pro', blurb='For an established academy', price=24999, fee=5, storage='3 TB', stream='3 TB', video='4K', live=15, seats=5, pages='All', ios=True),
    ],
    'monthly': [
        dict(key='starter', name='Starter', blurb='For a new academy', price=3999, fee=0, storage='512 GB', stream='512 GB', video='1080p', live=20, seats=5, pages='Any 6', ios=False),
        dict(key='growth', name='Growth', blurb='For a growing academy', price=5999, fee=0, storage='1 TB', stream='1 TB', video='1080p', live=50, seats=10, pages='Any 12', ios=True),
        dict(key='pro', name='Pro', blurb='For an established academy', price=7999, fee=0, storage='2 TB', stream='2 TB', video='4K', live=90, seats=20, pages='All', ios=True),
    ],
}

CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 12.5l4 4L18 8.5"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>'
DISK = '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg>'


def seats(n):
    return f'{n} team seat' if n == 1 else f'{n} team seats'


def highlights(bill, plans, i):
    c = plans[i]
    if i == 0:
        return ['Your own website and Android app', 'Custom-encrypted video (DRM)',
                'Unlimited videos &amp; live classes via YouTube and Zoom',
                f'{c["storage"]} private video hosting', f'{c["live"]} hours a month in the built-in live room', seats(c['seats'])]
    p = plans[i - 1]
    out = [f'Everything in {p["name"]}']
    if p['key'] == 'starter':
        out.append('Your own iOS app, after 30 days')
    if bill == 'yearly' and c['fee'] < p['fee']:
        out.append(f'Lower fee: {c["fee"]:g}% + GST, keep {100 - c["fee"]:g}%')
    if c['storage'] != p['storage']:
        out.append(f'{c["storage"]} private video hosting')
    if c['video'] != p['video']:
        out.append(f'{c["video"]} video quality')
    if c['live'] != p['live']:
        out.append(f'{c["live"]} live-room hours a month')
    if c['seats'] != p['seats']:
        out.append(seats(c['seats']))
    if c['pages'] != p['pages']:
        out.append('Every ready-made landing page' if c['pages'] == 'All' else f'{c["pages"]} ready-made landing pages')
    return out


def card(bill, plans, i, where):
    c = plans[i]
    feat = c['key'] == 'growth'
    badge = '<span class="sp-badge pop">Most popular</span>' if feat else ('<span class="sp-badge">Best value</span>' if c['key'] == 'pro' else '')
    unit = '/year + GST' if bill == 'yearly' else '/month + GST'
    with_gst = inr(round(c['price'] * 1.18, 2))
    sub = f'{with_gst} a year with GST' if bill == 'yearly' else f'{with_gst} a month with GST, by autopay'
    keep = f'<span>You keep <b>{100 - c["fee"]:g}%</b></span><small>{c["fee"]:g}% platform fee + GST</small>' if bill == 'yearly' \
        else '<span>You keep <b>100%</b></span><small>0% commission</small>'
    items = ''.join(f'<li>{CHECK}<span>{h}</span></li>' for h in highlights(bill, plans, i))
    return (f'<article class="sp-card{" featured" if feat else ""}">'
            f'<div class="sp-top"><div><h3>{c["name"]}</h3><p>{c["blurb"]}</p></div>{badge}</div>'
            f'<div class="sp-price"><b>{inr(c["price"])}</b><span>{unit}</span></div>'
            f'<small class="sp-sub">{sub}</small>'
            f'<div class="sp-keep">{keep}</div>'
            f'<div class="sp-chips"><span class="sp-chip drm">{SHIELD}DRM protected</span><span class="sp-chip">{DISK}Extendable storage</span></div>'
            f'<a class="sp-cta" href="{TRIAL}" data-track="join" data-where="{where}-{bill}-{c["key"]}">Start 7-day free trial</a>'
            f'<ul class="sp-list">{items}</ul></article>')


def block(where):
    grids = ''.join(
        f'<div class="sp-cards" data-show="{b}">' + ''.join(card(b, PLANS[b], i, where) for i in range(3)) + '</div>'
        for b in ('yearly', 'monthly'))
    return f'''<!-- X PLANS (generated by .claude/scripts/x_plans.py; studio = source of truth) -->
<div class="sp" data-sp data-bill="yearly">
  <div class="sp-switch" role="group" aria-label="Billing">
    <span class="sp-pill" aria-hidden="true"></span>
    <button type="button" data-b="yearly" aria-pressed="true">Yearly<em>pay once a year</em></button>
    <button type="button" data-b="monthly" aria-pressed="false">Monthly<em>0% commission</em></button>
  </div>
  {grids}
  <p class="sp-fine"><span data-show="yearly">Yearly plans: one payment a year, plus a platform fee of 10%, 7.5% or 5% + GST only when a student pays you.</span><span data-show="monthly">Monthly plans: 0% commission, paid by autopay, stop any month.</span> Prices exclude GST. Payment-gateway charges are separate. No sales limit and no setup fee on any plan. The Classic theme is free on every plan; premium themes are ₹10,000 each, one-time. Every plan starts with a 7-day free trial, no card needed.</p>
</div>
<!-- /X PLANS -->'''


def compare():
    Y, M = PLANS['yearly'], PLANS['monthly']
    tick = f'<span class="sp-tick" aria-label="Included">{CHECK}</span>'
    dash = '<span class="sp-dash" aria-label="Not included">—</span>'

    def both(fy, fm):
        return [f'<span data-show="yearly">{fy(y)}</span><span data-show="monthly">{fm(m)}</span>' for y, m in zip(Y, M)]

    def same(v):
        return [v, v, v]
    sections = [
        ('Pricing', [
            ('Price', None, both(lambda c: f'<b>{inr(c["price"])}</b><small>/year + GST</small>', lambda c: f'<b>{inr(c["price"])}</b><small>/month + GST</small>')),
            ('Platform fee per sale', 'Plus GST on yearly plans', both(lambda c: f'<b>{c["fee"]:g}%</b>', lambda c: '<b>0%</b>')),
            ('You keep of every sale', None, both(lambda c: f'{100 - c["fee"]:g}%', lambda c: '100%')),
            ('Sales limit', None, same('None')),
            ('Setup fee', None, same('None')),
            ('Free trial', 'No card needed to start', same(tick)),
        ]),
        ('Video &amp; live', [
            ('Custom-encrypted video (DRM)', 'Encryption and a watermark on every video you upload', same(tick)),
            ('Unlimited videos via YouTube', 'In your own branded player', same(tick)),
            ('Unlimited live classes', 'On YouTube Live or Zoom', same(tick)),
            ('Private video hosting', 'Extend storage on any plan', both(lambda c: c['storage'], lambda c: c['storage'])),
            ('Streaming a month', None, both(lambda c: c['stream'], lambda c: c['stream'])),
            ('Best video quality', None, both(lambda c: c['video'], lambda c: c['video'])),
            ('Built-in live room', None, both(lambda c: f'{c["live"]} h / month', lambda c: f'{c["live"]} h / month')),
        ]),
        ('Your brand', [
            ('Own website &amp; web address', 'Free address, or connect your own domain', same(tick)),
            ('Own Android app', None, same(tick)),
            ('Own iOS app', 'On Growth and Pro, after 30 days on the plan', [dash, 'After 30 days', 'After 30 days']),
            ('Published on your own console', 'Your Google Play Console and App Store Connect account', same(tick)),
            ('Drag-and-drop page builder', None, same(tick)),
            ('Ready-made landing pages', None, both(lambda c: c['pages'], lambda c: c['pages'])),
            ('Classic theme', 'Free on every plan. Premium themes are ₹10,000 each, one-time.', same(tick)),
            ('Blog for Google', 'Up to 300 posts', same(tick)),
        ]),
        ('Grow &amp; team', [
            ('Team seats', 'You included', both(lambda c: str(c['seats']), lambda c: str(c['seats']))),
            ('Coupons &amp; lead forms', None, same(tick)),
            ('Plugins', 'YouTube, Zoom, WhatsApp, Meta Pixel, Tag Manager', same(tick)),
            ('Marketplace discovery', None, same(tick)),
            ('Payouts to your bank', 'Razorpay settlement, usually T+2 days; instant available', same(tick)),
            ('Export your data', 'Any time, and for 30 days after you stop', same(tick)),
        ]),
    ]
    head = ''.join(f'<div class="sp-th"><b>{c["name"]}</b><span data-show="yearly">{inr(c["price"])}/yr</span><span data-show="monthly">{inr(m["price"])}/mo</span></div>' for c, m in zip(Y, M))
    rows = ''
    for title, rs in sections:
        rows += f'<div class="sp-sec">{title}</div>'
        for label, hint, cells in rs:
            h = f'<small>{hint}</small>' if hint else ''
            rows += f'<div class="sp-tr"><div class="sp-tl">{label}{h}</div>' + ''.join(f'<div class="sp-td">{x}</div>' for x in cells) + '</div>'
    return f'''<!-- X COMPARE (generated by .claude/scripts/x_plans.py) -->
<div class="sp sp-cmp" data-sp data-bill="yearly">
  <div class="sp-switch" role="group" aria-label="Billing in the table">
    <span class="sp-pill" aria-hidden="true"></span>
    <button type="button" data-b="yearly" aria-pressed="true">Yearly<em>pay once a year</em></button>
    <button type="button" data-b="monthly" aria-pressed="false">Monthly<em>0% commission</em></button>
  </div>
  <div class="sp-table" role="table" aria-label="Compare AllCoaching plans">
    <div class="sp-thead"><div class="sp-th sp-th-l">Compare plans</div>{head}</div>
    {rows}
  </div>
</div>
<!-- /X COMPARE -->'''


def write(path, text):
    for _ in range(10):
        try:
            open(path, 'w', encoding='utf-8', newline='').write(text)
            return
        except OSError:
            time.sleep(1)
    raise SystemExit('could not write ' + path)


def splice(s, mk, body):
    a = f'<!-- X {mk}'
    e = f'<!-- /X {mk} -->'
    if a not in s:
        return s
    i = s.index(a)
    j = s.index(e, i) + len(e)
    return s[:i] + body + s[j:]


if __name__ == '__main__':
    write('assets/x/plans.html', block('plans') + '\n')
    write('assets/x/plans-compare.html', compare() + '\n')
    n = 0
    for f in glob.glob('**/*.html', recursive=True):
        f = f.replace(os.sep, '/')
        if f.startswith(('assets/', 'node_modules/', 'dist/')):
            continue
        s = open(f, encoding='utf-8').read()
        if '<!-- X PLANS' not in s and '<!-- X COMPARE' not in s:
            continue
        where = os.path.splitext(os.path.basename(f))[0]
        t = splice(splice(s, 'PLANS', block(where)), 'COMPARE', compare())
        if t != s:
            write(f, t)
            n += 1
            print('plans ->', f)
    print('pages updated:', n)
