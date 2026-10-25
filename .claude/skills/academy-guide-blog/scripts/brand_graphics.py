"""AllCoaching branded blog graphics, as SVG primitives.

Visual language (owner-approved creatives, 2026-10-24):
  - lavender-white canvas (#F7F8FD -> #ECEFFF), or a grey "before" half (#EEEEF0)
  - heavy, tightly tracked Inter Tight headline in near-black, one phrase in electric blue #2B44FF
  - white pill cards with soft shadow and a dark navy icon tile (#1B1E2E) with a white line icon
  - light-lavender icon tiles with blue line icons for feature rows
  - handwritten notes (Caveat) and hand-drawn blue arrows only on the "problem" side
  - beige tape labels for lists of pain points
  - AllCoaching lockup: pin logo + Instrument Serif italic wordmark + "The academy platform for educators"

Every function returns an SVG fragment string. `svg()` wraps fragments into a document.
Export to WebP with export_graphics.js (fonts: Inter Tight, Inter, Caveat, Instrument Serif).
"""
import base64, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_PNG = os.path.join(HERE, '..', 'graphics', 'logo-128.png')

INK = '#14161F'
NAVY_TILE = '#1B1E2E'
BLUE = '#2B44FF'
BLUE_TINT = '#E8ECFF'
MUTED = '#5B6070'
LINE = '#E4E6EF'
TAPE = '#EFE6D2'
RED = '#E5484D'
GREEN = '#1F9D55'

F_HEAD = "'Inter Tight', Inter, Arial, sans-serif"
F_BODY = "Inter, 'Inter Tight', Arial, sans-serif"
F_HAND = "Caveat, 'Segoe Print', cursive"
F_WORD = "'Instrument Serif', Georgia, serif"
F_MONO = "'IBM Plex Mono', ui-monospace, monospace"


def esc(t):
    return html.escape(str(t), quote=True)


def _logo_data():
    with open(LOGO_PNG, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()


# ---------------------------------------------------------------- icons
# 24x24 line icons (stroke only), drawn for these graphics.
ICONS = {
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    'video': '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
    'play': '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="M10 9l5 3-5 3z"/>',
    'card': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18M7 15h4"/>',
    'check': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 3h6v3H9zM9 13l2 2 4-4"/>',
    'phone': '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    'search': '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    'trophy': '<path d="M8 4h8v5a4 4 0 01-8 0zM8 6H5a3 3 0 003 4M16 6h3a3 3 0 01-3 4M12 13v4M8.5 21h7M10 17h4v4h-4z"/>',
    'link': '<path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/>',
    'file': '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    'image': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0113 0"/><path d="M16 4.5a3.5 3.5 0 010 7M18 14a6 6 0 013.5 6"/>',
    'chart': '<path d="M4 20V4M4 20h16"/><path d="M8 16v-3M12 16V9M16 16v-6"/>',
    'trend': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    'pin': '<path d="M12 21s7-6.2 7-11.5A7 7 0 005 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    'message': '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    'book': '<path d="M3 5a2 2 0 012-2h6v17H5a2 2 0 00-2 2zM21 5a2 2 0 00-2-2h-6v17h6a2 2 0 012 2z"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    'puzzle': '<path d="M9 4h4v2a2 2 0 104 0V4h3v5h-2a2 2 0 100 4h2v7h-6v-2a2 2 0 10-4 0v2H4v-6h2a2 2 0 100-4H4V4z"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/>',
    'server': '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'home': '<path d="M3 11l9-7 9 7v9H3z"/><path d="M9 20v-6h6v6"/>',
    'list': '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    'type': '<path d="M5 6V4h14v2M12 4v16M9 20h6"/>',
    'mic': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/>',
    'sparkle': '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 15l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>',
    'x': '<path d="M6 6l12 12M18 6L6 18"/>',
    'tick': '<path d="M5 12.5l4.5 4.5L19 7"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def icon(name, x, y, size=24, color='#fff', sw=1.9):
    s = size / 24
    return (f'<g transform="translate({x} {y}) scale({s:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw / s * s:.2f}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


# ---------------------------------------------------------------- canvas
def svg(w, h, body, title, bg='light'):
    """Wrap fragments into an SVG document. bg: light | grey | split | navy."""
    defs = f'''<defs>
  <linearGradient id="bgL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBFBFE"/><stop offset=".55" stop-color="#F3F4FC"/><stop offset="1" stop-color="#E8EBFF"/></linearGradient>
  <linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2F2F4"/><stop offset="1" stop-color="#E6E6EA"/></linearGradient>
  <linearGradient id="bgN" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0A0F3D"/><stop offset="1" stop-color="#1B2A9E"/></linearGradient>
  <radialGradient id="glow" cx=".85" cy=".1" r=".7"><stop offset="0" stop-color="#2B44FF" stop-opacity=".10"/><stop offset="1" stop-color="#2B44FF" stop-opacity="0"/></radialGradient>
  <filter id="sh" x="-20%" y="-30%" width="140%" height="190%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#1B1E2E" flood-opacity=".10"/></filter>
  <filter id="shL" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="22" stdDeviation="26" flood-color="#1B1E2E" flood-opacity=".16"/></filter>
  <filter id="shB" x="-20%" y="-40%" width="140%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#2B44FF" flood-opacity=".35"/></filter>
  <marker id="ah" viewBox="0 0 12 12" refX="7" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1L9 6 1 11" fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></marker>
  <marker id="ahK" viewBox="0 0 12 12" refX="7" refY="6" markerWidth="8" markerHeight="8" orient="auto"><path d="M1 1L9 6 1 11" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>'''
    if bg == 'grey':
        back = f'<rect width="{w}" height="{h}" fill="url(#bgG)"/>'
    elif bg == 'navy':
        back = f'<rect width="{w}" height="{h}" fill="url(#bgN)"/>'
    elif isinstance(bg, tuple) and bg[0] == 'split':
        sx = bg[1]
        back = (f'<rect width="{w}" height="{h}" fill="url(#bgL)"/><rect width="{w}" height="{h}" fill="url(#glow)"/>'
                f'<rect width="{sx}" height="{h}" fill="url(#bgG)"/>')
    else:
        back = f'<rect width="{w}" height="{h}" fill="url(#bgL)"/><rect width="{w}" height="{h}" fill="url(#glow)"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" '
            f'font-family="{F_BODY}"><title>{esc(title)}</title>{defs}{back}{body}</svg>\n')


# ---------------------------------------------------------------- type
def headline(x, y, lines, size=56, anchor='start', color=INK, lh=1.02):
    """lines: list of strings; wrap a phrase in *asterisks* to colour it blue."""
    out = []
    for i, ln in enumerate(lines):
        parts = ln.split('*')
        spans = ''.join(
            f'<tspan fill="{BLUE if k % 2 else color}">{esc(p)}</tspan>' for k, p in enumerate(parts) if p)
        out.append(f'<text x="{x}" y="{y + i * size * lh:.0f}" font-family="{F_HEAD}" font-size="{size}" '
                   f'font-weight="800" letter-spacing="{-size * 0.045:.1f}" text-anchor="{anchor}">{spans}</text>')
    return ''.join(out)


def text(x, y, t, size=20, color=MUTED, weight=400, anchor='start', font=None, ls=0, opacity=1):
    f = font or F_BODY
    return (f'<text x="{x}" y="{y}" font-family="{f}" font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{opacity}">{esc(t)}</text>')


def lines(x, y, rows, size=20, color=MUTED, lh=1.4, **kw):
    return ''.join(text(x, y + i * size * lh, r, size, color, **kw) for i, r in enumerate(rows))


def eyebrow(x, y, t, color=BLUE, anchor='start'):
    return text(x, y, t.upper(), 15, color, 600, anchor, F_MONO, 1.6)


def hand(x, y, rows, size=34, color=INK, rotate=-4, anchor='start'):
    out = ''.join(f'<text x="0" y="{i * size * 1.05:.0f}" font-family="{F_HAND}" font-size="{size}" '
                  f'font-weight="600" fill="{color}" text-anchor="{anchor}">{esc(r)}</text>' for i, r in enumerate(rows))
    return f'<g transform="translate({x} {y}) rotate({rotate})">{out}</g>'


def arrow(d, color=BLUE, width=5, head=True):
    m = ' marker-end="url(#ah)"' if head and color == BLUE else (' marker-end="url(#ahK)"' if head else '')
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{m}/>'


# ---------------------------------------------------------------- brand
def lockup(x, y, scale=1.0, tagline=True, anchor='start', dark=False):
    """Logo pin + Instrument Serif italic wordmark (+ optional tagline). (x, y) = top-left of the mark."""
    s = scale
    word_col = '#FFFFFF' if dark else INK
    tag_col = 'rgba(255,255,255,.7)' if dark else MUTED
    g = (f'<circle cx="{34 * s}" cy="{34 * s}" r="{33 * s}" fill="#fff" stroke="{LINE}" stroke-width="{2 * s}"/>'
         f'<image href="{_logo_data()}" x="{8 * s}" y="{8 * s}" width="{52 * s}" height="{52 * s}"/>'
         f'<text x="{82 * s}" y="{50 * s}" font-family="{F_WORD}" font-style="italic" font-size="{50 * s}" fill="{word_col}">AllCoaching</text>')
    if tagline:
        g += f'<text x="{84 * s}" y="{92 * s}" font-family="{F_BODY}" font-size="{21 * s}" fill="{tag_col}">The academy platform for educators</text>'
    if anchor == 'end':
        width = (450 if tagline else 350) * s
        return f'<g transform="translate({x - width} {y})">{g}</g>'
    return f'<g transform="translate({x} {y})">{g}</g>'


def mark(x, y, size=40):
    """Small logo-only watermark."""
    return (f'<circle cx="{x + size / 2}" cy="{y + size / 2}" r="{size / 2}" fill="#fff" stroke="{LINE}"/>'
            f'<image href="{_logo_data()}" x="{x + size * .12}" y="{y + size * .12}" width="{size * .76}" height="{size * .76}"/>')


def signature(w, h, dark=False):
    """Bottom-right brand signature used on every in-article graphic."""
    col = 'rgba(255,255,255,.75)' if dark else INK
    return (mark(w - 214, h - 58, 34) +
            f'<text x="{w - 170}" y="{h - 33}" font-family="{F_WORD}" font-style="italic" font-size="26" fill="{col}">AllCoaching</text>')


# ---------------------------------------------------------------- components
def pill_card(x, y, w, title, sub=None, ic='globe', h=None, tile=NAVY_TILE, tilt=0, title_size=28):
    h = h or (104 if sub else 86)
    ts = 60
    ty = y + (h - ts) / 2
    body = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="#fff"/>'
            f'<rect x="{x + 20}" y="{ty}" width="{ts}" height="{ts}" rx="16" fill="{tile}"/>' +
            icon(ic, x + 20 + (ts - 28) / 2, ty + (ts - 28) / 2, 28, BLUE if tile == BLUE_TINT else '#fff'))
    if sub:
        body += text(x + 100, y + h / 2 - 4, title, title_size, INK, 700, font=F_HEAD, ls=-0.8)
        body += text(x + 100, y + h / 2 + 26, sub, 19, MUTED)
    else:
        body += text(x + 100, y + h / 2 + 10, title, title_size, INK, 700, font=F_HEAD, ls=-0.8)
    g = f'<g filter="url(#sh)">{body}</g>'
    if tilt:
        g = f'<g transform="rotate({tilt} {x + w / 2} {y + h / 2})">{g}</g>'
    return g


def alert_dot(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="17" fill="{RED}" stroke="#fff" stroke-width="3"/>'
            f'<text x="{cx}" y="{cy + 7}" font-family="{F_HEAD}" font-size="21" font-weight="800" fill="#fff" text-anchor="middle">!</text>')


def feature_tile(cx, y, label, ic, sub=None, size=84):
    x = cx - size / 2
    out = (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="22" fill="{BLUE_TINT}"/></g>' +
           icon(ic, cx - 18, y + size / 2 - 18, 36, BLUE, 2.1) +
           text(cx, y + size + 38, label, 23, INK, 600, 'middle', F_HEAD, -0.4))
    if sub:
        out += text(cx, y + size + 68, sub, 18, MUTED, anchor='middle')
    return out


def tape(x, y, w, label, rot=-1.2, size=34):
    return (f'<g transform="rotate({rot} {x + w / 2} {y + 34})">'
            f'<rect x="{x}" y="{y}" width="{w}" height="68" fill="{TAPE}" opacity=".95"/>'
            f'<rect x="{x}" y="{y + 62}" width="{w}" height="6" fill="#000" opacity=".05"/>'
            f'<text x="{x + 34}" y="{y + 46}" font-family="{F_HAND}" font-size="{size}" font-weight="600" '
            f'fill="{INK}" letter-spacing="2">{esc(label.upper())}</text></g>')


def button(x, y, w, label, h=84, size=34):
    return (f'<g filter="url(#shB)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 3.2:.0f}" fill="{BLUE}"/></g>'
            f'<text x="{x + w / 2 - 22}" y="{y + h / 2 + size * .36:.0f}" font-family="{F_HEAD}" font-size="{size}" '
            f'font-weight="800" letter-spacing="{-size * .04:.1f}" fill="#fff" text-anchor="middle">{esc(label)}</text>' +
            icon('arrow', x + w / 2 + len(label) * size * .26 - 6, y + h / 2 - 16, 32, '#fff', 2.6))


def check_row(x, y, t, size=22, ok=True):
    col = BLUE if ok else RED
    ic = 'tick' if ok else 'x'
    return (f'<circle cx="{x + 16}" cy="{y - 7}" r="16" fill="{col}"/>' + icon(ic, x + 6, y - 17, 20, '#fff', 2.8) +
            text(x + 44, y, t, size, INK, 500))


def white_panel(x, y, w, h, r=28, big=False):
    return f'<g filter="url({"#shL" if big else "#sh"})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#fff"/></g>'


def search_bar(x, y, w, query, h=64, button_label=None, google=True):
    mark_ = logo_google(x + 20, y + h / 2 - 14, 28) if google else icon('search', x + 22, y + h / 2 - 13, 26, '#5F6368', 2.2)
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="#fff" stroke="#DADCE0" stroke-width="2"/>' +
           mark_ +
           text(x + 64, y + h / 2 + 9, query, 25, '#202124'))
    if button_label:
        out += (f'<rect x="{x + w + 20}" y="{y}" width="190" height="{h}" rx="{h / 2}" fill="{INK}"/>' +
                text(x + w + 115, y + h / 2 + 8, button_label, 22, '#fff', 600, 'middle', F_HEAD))
    return out


def result(x, y, w, site, url, title, desc, highlight=False, title_size=27):
    h = 150
    out = ''
    if highlight:
        out += f'<rect x="{x - 18}" y="{y - 16}" width="{w + 36}" height="{h + 12}" rx="20" fill="{BLUE_TINT}" stroke="{BLUE}" stroke-width="3"/>'
    out += (f'<circle cx="{x + 18}" cy="{y + 20}" r="18" fill="{BLUE if highlight else "#C9CDD8"}"/>' +
            text(x + 18, y + 27, site[0], 18, '#fff', 700, 'middle') +
            text(x + 48, y + 15, site, 19, '#202124') + text(x + 48, y + 38, url, 16, '#4D5156') +
            text(x, y + 82, title, title_size, '#1A0DAB') + text(x, y + 118, desc, 18, '#4D5156'))
    return out


def ghost_lines(x, y, widths, gap=30, colors=('#C9CDD8', '#AFC3F5', '#E3E5EB')):
    out = ''
    for i, w in enumerate(widths):
        c = colors[i % len(colors)]
        hh = 18 if len(colors) > 1 and c == colors[1] else 12
        out += f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{hh}" rx="{hh / 2}" fill="{c}"/>'
    return out


def num_badge(cx, cy, n, r=22):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BLUE}"/>' +
            text(cx, cy + 8, str(n), 22, '#fff', 800, 'middle', F_HEAD))


# ---------------------------------------------------------------- real product shots in Apple-style devices
GRAPHICS = os.path.join(HERE, '..', 'graphics')
_uid = [0]


def _img_data(name):
    ext = name.rsplit('.', 1)[1]
    mime = 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/' + ext
    with open(os.path.join(GRAPHICS, name), 'rb') as f:
        return f'data:{mime};base64,' + base64.b64encode(f.read()).decode()


def laptop(x, y, w, shot='studio-desktop.jpg'):
    """MacBook-style laptop showing a real AllCoaching Studio screenshot (16:10 screen)."""
    _uid[0] += 1
    cid = f'lc{_uid[0]}'
    bez = w * 0.022
    sw, sh = w - 2 * bez, (w - 2 * bez) * 0.625
    h = sh + 2 * bez
    return (f'<defs><clipPath id="{cid}"><rect x="{x + bez}" y="{y + bez}" width="{sw}" height="{sh}" rx="{w * .006}"/></clipPath>'
            f'<linearGradient id="{cid}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9EAEE"/><stop offset="1" stop-color="#B9BCC6"/></linearGradient></defs>'
            f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w * .03}" fill="#16171C"/></g>'
            f'<image href="{_img_data(shot)}" x="{x + bez}" y="{y + bez}" width="{sw}" height="{sh}" preserveAspectRatio="xMidYMin slice" clip-path="url(#{cid})"/>'
            f'<circle cx="{x + w / 2}" cy="{y + bez / 2}" r="{bez * .18}" fill="#3A3C44"/>'
            f'<path d="M{x - w * .08} {y + h} H {x + w * 1.08} v {w * .012} q 0 {w * .022} -{w * .03} {w * .022} H {x - w * .05} q -{w * .03} 0 -{w * .03} -{w * .022} z" fill="url(#{cid}b)"/>'
            f'<rect x="{x + w * .42}" y="{y + h}" width="{w * .16}" height="{w * .008}" rx="{w * .004}" fill="#9EA1AB"/>')


def phone(x, y, w, shot='studio-mobile.jpg'):
    """iPhone-style phone with a real screenshot (9:19.5)."""
    _uid[0] += 1
    cid = f'pc{_uid[0]}'
    h = w * 2.07
    b = w * 0.045
    r = w * 0.17
    return (f'<defs><clipPath id="{cid}"><rect x="{x + b}" y="{y + b}" width="{w - 2 * b}" height="{h - 2 * b}" rx="{r - b}"/></clipPath></defs>'
            f'<g filter="url(#shL)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#121317"/></g>'
            f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{w - 3}" height="{h - 3}" rx="{r - 1}" fill="none" stroke="#4A4D57" stroke-width="2"/>'
            f'<image href="{_img_data(shot)}" x="{x + b}" y="{y + b}" width="{w - 2 * b}" height="{h - 2 * b}" preserveAspectRatio="xMidYMin slice" clip-path="url(#{cid})"/>'
            f'<rect x="{x + w * .34}" y="{y + b + w * .035}" width="{w * .32}" height="{w * .085}" rx="{w * .0425}" fill="#000"/>')


# ---------------------------------------------------------------- real brand marks (nominative use: naming the tool)
def logo_google(x, y, size=40):
    """Google 'G' mark in its four brand colours."""
    s = size / 48
    return (f'<g transform="translate({x} {y}) scale({s:.4f})">'
            '<path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>'
            '<path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>'
            '<path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>'
            '<path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></g>')


def logo_youtube(x, y, size=40):
    w, h = size * 1.42, size
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h * .24}" fill="#FF0000"/>'
            f'<path d="M{x + w * .4} {y + h * .29} L{x + w * .66} {y + h * .5} L{x + w * .4} {y + h * .71}Z" fill="#fff"/>')


def logo_whatsapp(x, y, size=40):
    s = size / 24
    return (f'<circle cx="{x + size / 2}" cy="{y + size / 2}" r="{size / 2}" fill="#25D366"/>'
            f'<g transform="translate({x + size * .18} {y + size * .18}) scale({s * .64:.4f})" fill="#fff">'
            '<path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57a1.1 1.1 0 00-.8.37c-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.87 1.22 3.07.15.2 2.1 3.2 5.08 4.49.7.3 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2-1.42.25-.69.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35m-5.42 7.4c-1.76 0-3.49-.47-5.03-1.37l-.36-.22-3.74.99 1-3.65-.24-.38a9.86 9.86 0 01-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88a9.83 9.83 0 019.88 9.89c0 5.45-4.44 9.88-9.89 9.88"/></g>')


def logo_instagram(x, y, size=40):
    _uid[0] += 1
    gid = f'ig{_uid[0]}'
    return (f'<defs><radialGradient id="{gid}" cx=".3" cy="1.05" r="1.2"><stop offset="0" stop-color="#FFD776"/><stop offset=".25" stop-color="#F3A554"/>'
            f'<stop offset=".5" stop-color="#E1306C"/><stop offset=".8" stop-color="#9B36B7"/><stop offset="1" stop-color="#515ECF"/></radialGradient></defs>'
            f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="url(#{gid})"/>'
            f'<rect x="{x + size * .2}" y="{y + size * .2}" width="{size * .6}" height="{size * .6}" rx="{size * .18}" fill="none" stroke="#fff" stroke-width="{size * .07}"/>'
            f'<circle cx="{x + size / 2}" cy="{y + size / 2}" r="{size * .14}" fill="none" stroke="#fff" stroke-width="{size * .07}"/>'
            f'<circle cx="{x + size * .69}" cy="{y + size * .31}" r="{size * .045}" fill="#fff"/>')


def logo_tile(x, y, logo_fn, size=72):
    """White rounded app-icon tile holding a brand mark."""
    inner = size * .56
    off = (size - inner) / 2
    extra = inner * .21 if logo_fn is logo_youtube else 0
    return (f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size * .26}" fill="#fff"/></g>' +
            logo_fn(x + off - extra, y + off + (inner * .0), inner))
