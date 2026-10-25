"""Branded graphics for comparison / alternative posts, driven by one JSON spec per post.

Usage:
  python .claude/skills/academy-guide-blog/scripts/comparison_graphics.py .claude/skills/academy-guide-blog/graphics/specs/<slug>.json
  python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/<slug>

Spec (JSON):
{
  "slug": "classplus-alternative-for-coaching-institutes",
  "checked": "24 Oct 2026",
  "cover": {"eyebrow": "Honest comparison", "lines": ["Looking for a", "*Classplus alternative?*"], "sub": "Prices checked on each official site",
            "options": ["Graphy", "Learnyst", "Edmingle", "Teachmint", "AllCoaching"]},
  "verdict": {"title": ["Pick by *what you need*"], "rows": [{"need": "...", "pick": "...", "why": "...", "icon": "globe", "us": false}]},
  "prices": {"title": ["Entry price, *as published*"], "rows": [{"name": "Classplus", "price": 29999, "label": "₹29,999/yr", "fee": "Fee not stated", "published": true}]},
  "cost": {"title": [...], "competitors": [{"name": "Classplus", "plans": [[29999, 0]], "note": "listed price; sales fee not stated"}], "levels": [0, 100000, 300000, 500000, 1000000]},
  "switch": {"title": [...], "steps": [["Title", "One line"], ...]},
  "before_after": {"left_title": ["Still running", "your batches *like this?*"], "tapes": [...], "notes": [...], "right_title": [...], "checks": [...]}
}
Any block can be omitted. Every competitor figure in a spec must come from data/competitors.json (official source + date).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand_graphics import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
AC_PLANS = [(6999, 0.10, 'Starter'), (12999, 0.075, 'Growth'), (24999, 0.05, 'Pro'), (59999, 0.0, 'Scale')]


def inr(n):
    n = int(round(n))
    s = str(n)
    if len(s) <= 3:
        return '₹' + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return '₹' + ','.join(parts) + ',' + tail


def lakh(n):
    if n == 0:
        return '₹0'
    if n >= 100000:
        v = round(n / 100000, 2)
        return f'₹{v:g}L'
    if n >= 1000:
        return f'₹{round(n / 1000):g}K'
    return inr(n)


def ac_cost(sales):
    return min(p + f * sales for p, f, _ in AC_PLANS)


def comp_cost(plans, sales):
    return min(p + f * sales for p, f in plans)


def cover(sp):
    c = sp['cover']
    b = lockup(72, 60, 1.0)
    b += eyebrow(80, 250, c.get('eyebrow', 'Honest comparison'))
    b += headline(80, 330, c['lines'], 80)
    b += lines(84, 330 + 80 * len(c['lines']) + 14, [c.get('sub', '')], 28, MUTED)
    stamp_y = 330 + 80 * len(c['lines']) + 70
    b += (f'<rect x="80" y="{stamp_y}" width="380" height="54" rx="27" fill="#fff" stroke="{BLUE}" stroke-width="2"/>' +
          icon('check', 98, stamp_y + 13, 28, BLUE, 2) + text(138, stamp_y + 35, c.get('stamp', f'Prices checked {sp["checked"]}'), 21, BLUE, 700))
    opts = c['options']
    gap = min(104, 560 / max(1, len(opts)))
    ph = 130 + gap * len(opts)
    py = max(120, (900 - ph) / 2)
    b += white_panel(920, py, 600, ph, 32, big=True)
    b += eyebrow(960, py + 60, 'Options compared', MUTED)
    base = py + 90
    for i, o in enumerate(opts):
        y = base + i * gap
        us = o == 'AllCoaching'
        fill = BLUE_TINT if us else '#F5F6FA'
        b += f'<rect x="950" y="{y}" width="540" height="{gap - 16}" rx="{(gap - 16) / 2}" fill="{fill}"{(" stroke=" + chr(34) + BLUE + chr(34) + " stroke-width=" + chr(34) + "2" + chr(34)) if us else ""}/>'
        if us:
            b += mark(966, y + (gap - 16) / 2 - 20, 40)
        else:
            b += f'<circle cx="{986}" cy="{y + (gap - 16) / 2}" r="20" fill="#fff" stroke="{LINE}" stroke-width="2"/>' + text(986, y + (gap - 16) / 2 + 7, o[0], 19, INK, 700, 'middle', F_HEAD)
        b += text(1022, y + (gap - 16) / 2 + 9, o, 26, BLUE if us else INK, 700, font=F_HEAD, ls=-0.5)
    return svg(1600, 900, b, f'{" ".join(l.replace("*", "") for l in c["lines"])}: options compared, prices checked {sp["checked"]}')


def verdict(sp):
    v = sp['verdict']
    rows = v['rows']
    RH = 140
    H = 200 + len(rows) * RH + 70
    b = headline(60, 96, v['title'], 50) + lines(62, 146, [v.get('sub', 'There is no single best option. Start from what you need.')], 22)
    for i, r in enumerate(rows):
        y = 190 + i * RH
        us = r.get('us', False)
        b += white_panel(60, y, 1100, RH - 20, 26)
        b += f'<rect x="84" y="{y + 28}" width="64" height="64" rx="18" fill="{BLUE if us else NAVY_TILE}"/>' + icon(r.get('icon', 'check'), 100, y + 44, 32, '#fff', 2)
        need = wrap(r['need'], 38)[:2]
        b += lines(176, y + 42, need, 19, MUTED, 1.3)
        b += text(176, y + 42 + len(need) * 25 + 14, r['pick'], 28, BLUE if us else INK, 800, font=F_HEAD, ls=-1)
        b += f'<line x1="690" y1="{y + 24}" x2="690" y2="{y + RH - 44}" stroke="{LINE}" stroke-width="2"/>'
        b += lines(716, y + 50, wrap(r['why'], 38)[:3], 19, INK, 1.4)
    b += signature(1220, H)
    return svg(1220, H, b, 'Which option to choose, by what you need')


def wrap(t, n):
    words, out, cur = t.split(), [], ''
    for w in words:
        if len(cur) + len(w) + 1 > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out


def prices(sp):
    p = sp['prices']
    rows = p['rows']
    H = 230 + len(rows) * 92 + 90
    b = headline(60, 96, p['title'], 50) + lines(62, 146, [p.get('sub', 'Lowest yearly plan on each official pricing page')], 22)
    mx = max(r['price'] for r in rows if r.get('published')) or 1
    for i, r in enumerate(rows):
        y = 200 + i * 92
        us = r['name'] == 'AllCoaching'
        b += text(60, y + 42, r['name'], 25, BLUE if us else INK, 800, font=F_HEAD, ls=-0.6)
        if r.get('published') and r['price'] == 0:
            b += text(300, y + 44, r['label'], 23, INK, 700, font=F_HEAD)
            b += text(300, y + 70, r.get('fee', ''), 16, MUTED)
        elif r.get('published'):
            w = max(70, 480 * r['price'] / mx)
            b += f'<rect x="300" y="{y + 12}" width="{w}" height="46" rx="14" fill="{BLUE if us else "#C9CEDD"}"/>'
            b += text(300 + w + 16, y + 44, r['label'], 23, INK, 700, font=F_HEAD)
            b += text(300 + w + 16, y + 70, r.get('fee', ''), 16, MUTED)
        else:
            b += f'<rect x="300" y="{y + 12}" width="260" height="46" rx="14" fill="none" stroke="#B9BECC" stroke-width="2" stroke-dasharray="7 7"/>' + text(430, y + 42, r.get('label', 'Price not listed'), 19, MUTED, 600, 'middle')
            b += text(580, y + 42, r.get('fee', ''), 16, MUTED)
    b += text(60, H - 28, f'Sources linked in the article. Checked {sp["checked"]}. GST extra where stated.', 16, MUTED) + signature(1220, H)
    return svg(1220, H, b, 'Entry prices as published on each official site')


def cost(sp):
    c = sp['cost']
    levels = c.get('levels', [0, 100000, 300000, 500000, 1000000])
    series = [('AllCoaching', BLUE, [ac_cost(s) for s in levels])]
    palette = ['#14161F', '#8A90A2', '#C27C0E', '#7A4DD8']
    for k, comp in enumerate(c['competitors']):
        series.append((comp['name'], palette[k % len(palette)], [comp_cost(comp['plans'], s) for s in levels]))
    W, H = 1220, 940
    x0, y0, cw, ch = 140, 230, 1000, 470
    raw = max(max(v) for _, _, v in series)
    step = 25000 if raw <= 200000 else 50000
    mx = step * 4 * -(-raw // (step * 4))
    mx = max(mx, step * 4)
    b = headline(60, 96, c['title'], 48) + lines(62, 146, [c.get('sub', 'Plan price + fee on sales, lowest-cost plan at each level, before GST')], 22)
    for g in range(5):
        yy = y0 + ch - ch * g / 4
        b += f'<line x1="{x0}" y1="{yy}" x2="{x0 + cw}" y2="{yy}" stroke="{LINE}" stroke-width="2"/>' + text(x0 - 14, yy + 6, lakh(mx * g / 4), 15, MUTED, anchor='end')
    for i, s in enumerate(levels):
        xx = x0 + cw * i / (len(levels) - 1)
        b += text(xx, y0 + ch + 34, lakh(s), 17, INK, 600, 'middle')
    b += text(x0 + cw / 2, y0 + ch + 66, 'Your course sales in a year', 16, MUTED, anchor='middle')
    for name, col, vals in series:
        pts = ' '.join(f'{x0 + cw * i / (len(levels) - 1):.0f},{y0 + ch - ch * v / mx:.0f}' for i, v in enumerate(vals))
        b += f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{6 if name == "AllCoaching" else 4}" stroke-linejoin="round" stroke-linecap="round"{"" if name == "AllCoaching" else " stroke-dasharray=" + chr(34) + "2 0" + chr(34)}/>'
        for i, v in enumerate(vals):
            b += f'<circle cx="{x0 + cw * i / (len(levels) - 1):.0f}" cy="{y0 + ch - ch * v / mx:.0f}" r="7" fill="{col}"/>'
    lx = x0
    for name, col, _ in series:
        b += f'<rect x="{lx}" y="{y0 - 50}" width="26" height="8" rx="4" fill="{col}"/>' + text(lx + 36, y0 - 41, name, 18, INK, 600)
        lx += 60 + len(name) * 11
    notes = [cm.get('note') for cm in c['competitors'] if cm.get('note')]
    notes.append('AllCoaching: Starter ₹6,999 + 10%, Growth ₹12,999 + 7.5%, Pro ₹24,999 + 5%, Scale ₹59,999 + 0%. GST extra.')
    for k, n in enumerate(notes[-6:]):
        b += text(60, H - 24 - (len(notes[-6:]) - k) * 24 + 10, n, 15, MUTED)
    b += signature(W, H)
    return svg(W, H, b, 'Total yearly cost at different sales levels, from published prices')


def switch(sp):
    s = sp['switch']
    steps = s['steps']
    W, H = 1220, 640
    b = headline(60, 96, s['title'], 50) + lines(62, 146, [s.get('sub', 'Run both side by side, so no student loses access')], 22)
    n = len(steps)
    cw = (1100 - (n - 1) * 24) / n
    for i, (t, d) in enumerate(steps):
        x = 60 + i * (cw + 24)
        b += white_panel(x, 200, cw, 360, 26)
        b += num_badge(x + 48, 252, i + 1, 26)
        b += lines(x + 28, 334, wrap(t, int(cw / 15)), 27, INK, 1.2, weight=800, font=F_HEAD, ls=-0.8)
        b += lines(x + 28, 440, wrap(d, int(cw / 10.5)), 18, MUTED, 1.4)
        if i < n - 1:
            b += arrow(f'M{x + cw + 2} 380 H {x + cw + 20}', BLUE, 3)
    b += signature(W, H)
    return svg(W, H, b, 'How to switch platforms without losing students')


def before_after(sp):
    a = sp['before_after']
    W, H = 1220, 940
    b = headline(56, 110, a['left_title'], 54)
    for i, t in enumerate(a['tapes'][:5]):
        b += tape(36 + (i % 2) * 22, 250 + i * 104, 500, t, -1.4 if i % 2 else 1.0, 30)
    if a.get('note'):
        b += hand(320, 815, a['note'], 38, INK, -6) + arrow('M300 830 C 250 850, 210 830, 190 800', INK, 3)
    b += lockup(1180, 50, 0.62, True, 'end')
    b += headline(650, 230, a['right_title'], 60)
    for i, t in enumerate(a['checks'][:5]):
        b += check_row(656, 400 + i * 74, t, 24)
    b += button(650, 790, 500, 'Start your academy', 84, 32)
    return svg(W, H, b, 'Before and after: separate tools versus one academy login', ('split', 600))


def main(spec_path):
    sp = json.load(open(spec_path, encoding='utf-8'))
    out = os.path.join(ROOT, 'assets', 'blog', sp['slug'])
    os.makedirs(out, exist_ok=True)
    for name, fn in [('cover', cover), ('verdict', verdict), ('prices', prices), ('cost', cost), ('switch', switch), ('before-after', before_after)]:
        key = 'before_after' if name == 'before-after' else name
        if key in sp:
            with open(os.path.join(out, name + '.svg'), 'w', encoding='utf-8') as f:
                f.write(fn(sp))
            print('wrote', name)
    feat = os.path.join(ROOT, 'assets', 'blog', 'seo-for-online-academy-beginners-guide', 'academy-features.webp')
    if os.path.exists(feat):
        print('promo band image: /assets/blog/seo-for-online-academy-beginners-guide/academy-features.webp (shared)')


if __name__ == '__main__':
    main(sys.argv[1])
