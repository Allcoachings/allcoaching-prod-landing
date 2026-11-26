#!/usr/bin/env python3
"""Build /journey.html: the educator journey, every step with a real studio screenshot.

Layout studied from Shopify Editions (research in video-studio/research/editions): a hero with a giant
vertical word, a mono chapter index and a clickable map; then one full-colour chapter per stage with a
giant chapter title, a sticky chapter index, and feature blocks. Everything else is AllCoaching's own:
Inter + JetBrains Mono, our colours, our words, and the owner-checked copy and screenshots in
data/features/<slug>.json (the same data the /features pages use), so no claim is written twice.

Usage: python .claude/scripts/build_journey.py [--register]
"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_feature_pages as F  # noqa: E402  (chdirs to the repo root)

e = F.e
SITE = F.SITE
URL = SITE + '/journey'
TITLE = 'Educator Journey 2027: Your Own Website and App | AllCoaching'
DESC = ('See how an educator builds their own website and app in 2027: name your academy, connect your domain, '
        'add a course and sell. Then all 14 steps, with real studio screens.')
VER = '22'

CHAPTERS = [
    ('setup', 'Set up', 'Your name, your website and your own app.', '#1B2FE0', ['academy-website', 'mobile-app']),
    ('create', 'Create', 'Courses, notes and tests, built once and sold again and again.', '#6D28D9', ['courses', 'notes-pdfs', 'test-series']),
    ('teach', 'Teach', 'Live classes, batches and a feed your students open every day.', '#B5174F', ['live-classes', 'batches', 'community']),
    ('sell', 'Sell', 'Your own checkout, offers that bring students in, and free lessons that convert.', '#0B7A3B', ['payments', 'discount-codes', 'free-content']),
    ('run', 'Run', 'Your numbers, your team and the tools you already use.', '#1b1b1b', ['analytics', 'team', 'integrations']),
]
TOTAL = sum(len(c[4]) for c in CHAPTERS)


def join(parts):
    return ' '.join(parts) if isinstance(parts, list) else parts


def mins(sec):
    return max(1, round(sec / 60))


def feature(p, n, pages):
    slug = p['slug']
    tabs, panes, shots = [], [], []
    for i, s in enumerate(p['sections']):
        on = ' on' if i == 0 else ''
        tabs.append(f'<button type="button" class="jr-tab{on}" data-i="{i}" aria-pressed="{"true" if i == 0 else "false"}"><i>{i + 1}</i>{e(s["eyebrow"])}</button>')
        lis = ''.join(f'<li>{e(b)}</li>' for b in s['bullets'])
        panes.append(f'<div class="jr-pane{on}" data-i="{i}"><h4>{e(join(s["h2"]))}</h4><p>{e(s["body"])}</p><ul>{lis}</ul></div>')
        shots.append(f'<img class="jr-shot{on}" data-i="{i}" src="{e(s["img"])}" alt="{e(s["alt"])}" loading="lazy" width="1600" height="900"/>')
    ep = p['eps'][0]
    vid, vt, _up, dur = F.EPS[ep]
    steps = ''.join(f'<li><b>{e(s["t"])}</b><span>{e(s["d"])}</span></li>' for s in p['steps'])
    return f'''<article class="jr-f" id="f-{slug}" data-jr>
      <header class="jr-fh">
        <span class="jr-n">Step {n:02d} <em>/ {TOTAL}</em></span>
        <h3>{e(p["nav"])}</h3>
        <p>{e(p["card"])}</p>
        <div class="jr-links"><a class="jr-pill" href="/features/{slug}">Open the guide</a><a class="jr-pill ghost" href="/features/{slug}#tutorial"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>Tutorial · {mins(dur)} min</a></div>
      </header>
      <div class="jr-stage">
        <div class="jr-tabs" role="group" aria-label="{e(p["nav"])}: parts">{''.join(tabs)}</div>
        <div class="jr-grid">
          <div class="jr-text">{''.join(panes)}</div>
          <div class="jr-screen"><div class="jr-bar"><s></s><s></s><s></s><em>studio.allcoaching.in</em></div>{''.join(shots)}</div>
        </div>
      </div>
      <aside class="jr-notes"><div class="jr-nh">How to do it</div><ol>{steps}</ol></aside>
    </article>'''


def constellation(pages):
    cx, cy = 505, 360
    out = []
    names = []
    for ci, (cid, name, _sub, col, slugs) in enumerate(CHAPTERS):
        a = -math.pi / 2 + ci * 2 * math.pi / len(CHAPTERS) + 0.35
        r = 230 if ci % 2 == 0 else 260
        x, y = cx + r * math.cos(a) * 1.22, cy + r * math.sin(a)
        out.append(f'<line class="l1" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>')
        for k, slug in enumerate(slugs):
            b = a + (k - (len(slugs) - 1) / 2) * 0.95
            rr = 118 + 22 * (k % 2)
            fx, fy = x + rr * math.cos(b) * 1.15, y + rr * math.sin(b)
            left = fx < x
            out.append(f'<line class="l2" x1="{x:.0f}" y1="{y:.0f}" x2="{fx:.0f}" y2="{fy:.0f}"/>')
            out.append(f'<a href="#f-{slug}" class="jr-sat"><title>{e(pages[slug]["nav"])}</title><rect x="{fx - 7:.0f}" y="{fy - 7:.0f}" width="14" height="14" rx="3"/>'
                       f'<text x="{fx - 14 if left else fx + 14:.0f}" y="{fy + 4:.0f}" text-anchor="{"end" if left else "start"}">{e(pages[slug]["nav"])}</text></a>')
        for k in range(5):  # quiet background dots
            b = a + 1.1 + k * 0.9
            dx, dy = x + (70 + 37 * k) * math.cos(b) * 1.4, y + (70 + 37 * k) * math.sin(b)
            out.append(f'<circle class="dot" cx="{dx:.0f}" cy="{dy:.0f}" r="1.6"/>')
        names.append(f'<a href="#{cid}" class="jr-node" style="--c:{col if cid != "run" else "#8A93B8"}"><circle cx="{x:.0f}" cy="{y:.0f}" r="26" class="halo"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7"/>'
                     f'<text x="{x + 16:.0f}" y="{y - 14:.0f}">{e(name)}<tspan dx="5" dy="-6">{len(slugs):02d}</tspan></text></a>')
    hub = f'<g class="jr-hub"><circle cx="{cx}" cy="{cy}" r="46" class="halo"/><circle cx="{cx}" cy="{cy}" r="10"/><text x="{cx}" y="{cy + 34}" text-anchor="middle">Your academy</text></g>'
    return ('<svg class="jr-svg" viewBox="0 0 1120 720" role="img" aria-label="A map of the educator journey: five stages around your academy, with every step linked">'
            + ''.join(out) + ''.join(names) + hub + '</svg>')


BRAND_TABS = [
    ('Website and domain', 'Your own web address.', 'Start on a free .allcoaching.in address, then connect a domain you buy from any registrar, like youracademy.in. Connecting is free on every plan.',
     ['Your own domain, registered in your name', 'Course pages and checkout built for you', 'Drag-and-drop page builder for your own pages'],
     '/assets/x/f/academy-website-2.webp', 'An academy website built on AllCoaching showing its courses page', 'youracademy.in'),
    ('Your own app', 'Your icon on their phone.', 'Publish your own Android app from your Google Play Console account. Your own iOS app comes with Growth and Pro, after 30 days on the plan.',
     ['Your app name, icon and colours', 'Published on your own store account', 'Courses, tests and live classes inside'],
     '/assets/x/f/mobile-app-3.webp', 'Three phone screens of an academy app: courses, a course page and test series', 'Your app'),
    ('Name and logo', 'Your name on everything.', 'Set your logo, cover, display name and handle once in the studio. They appear on your website, your app, your course pages and your certificates.',
     ['Your logo and colours, not ours', 'Your academy name at the top of every screen', 'Certificates carry your branding'],
     '/assets/x/f/academy-website-1.webp', 'Educator Profile in the studio with the academy cover, logo, display name and handle', 'studio.allcoaching.in'),
    ('Your videos', 'Your logo on every lesson.', 'Switch on the video watermark and your logo becomes part of every video you upload. Each student also sees their own name on screen while they watch.',
     ['Logo watermark, placed where you want it', 'Student-name watermark while watching', 'DRM-protected player on every plan'],
     '/assets/x/f/academy-website-3.webp', 'Video watermark settings with a logo placed in the video frame', 'studio.allcoaching.in'),
    ('Theme and pages', 'Your look, your pages.', 'The Classic theme is free on every plan and fully customizable, with ready-made landing pages. Premium themes are ₹10,000 each, one-time.',
     ['Classic theme free on every plan', 'Ready-made landing pages', 'Blog for Google, up to 300 posts'],
     '/assets/x/a-home.webp', 'The home page of an academy website in the Classic theme', 'youracademy.in'),
]


def branding():
    tabs, panes, shots = [], [], []
    for i, (tab, h, body, bullets, img, alt, bar) in enumerate(BRAND_TABS):
        on = ' on' if i == 0 else ''
        tabs.append(f'<button type="button" class="jr-tab{on}" data-i="{i}" aria-pressed="{"true" if i == 0 else "false"}"><i>{i + 1}</i>{e(tab)}</button>')
        lis = ''.join(f'<li>{e(b)}</li>' for b in bullets)
        panes.append(f'<div class="jr-pane{on}" data-i="{i}"><h4>{e(h)}</h4><p>{e(body)}</p><ul>{lis}</ul></div>')
        shots.append(f'<img class="jr-shot{on}" data-i="{i}" src="{img}" alt="{e(alt)}" {"" if i == 0 else "loading=\"lazy\" "}width="1600" height="900"/>')
    return f'''<section class="jr-brand" id="own-branding">
  <div class="jr-in">
    <div class="jr-bh">
      <div class="jr-duo" role="img" aria-label="Your academy website on your own domain, and the same academy as your own app on a phone">
        <div class="jr-screen"><div class="jr-bar"><s></s><s></s><s></s><em>youracademy.in</em></div><img src="/assets/x/a-home.webp" alt="" width="1600" height="900"/></div>
        <div class="jr-ph">{F.PHONE.replace('IMG', '/assets/x/m-home.webp').replace('ALT', 'The academy app on a phone')}</div>
        <span class="jr-tag t1"><b>1</b>Your website</span><span class="jr-tag t2"><b>2</b>Your app</span>
      </div>
      <span class="jr-chn">Before step 01 · what "own branding" means</span>
      <h2>Your own website. <b>Your own app.</b></h2>
      <p>Own branding means students see your academy, not ours. Your website on your own domain and your app on their phone both carry your name, your logo and your colours. AllCoaching stays in the background and runs the technology.</p>
      <div class="jr-vs"><div><small>A shared coaching app</small><b>Their name, their logo, your course inside</b></div><div class="on"><small>Own branding on AllCoaching</small><b>Your name, your logo, your domain, your app</b></div></div>
    </div>
    <article class="jr-f" data-jr>
      <div class="jr-stage">
        <div class="jr-tabs" role="group" aria-label="Own branding: where your brand shows">{"".join(tabs)}</div>
        <div class="jr-grid">
          <div class="jr-text">{"".join(panes)}</div>
          <div class="jr-screen"><div class="jr-bar"><s></s><s></s><s></s><em>your brand</em></div>{"".join(shots)}</div>
        </div>
      </div>
    </article>
  </div>
</section>'''


def build(pages):
    idx = '<li><a href="#build"><span>Build yours now</span><em>try</em></a></li><li><a href="#own-branding"><span>Own branding</span><em>00</em></a></li>' + ''.join(f'<li><a href="#{cid}"><span>{e(name)}</span><em>{i + 1:02d}</em></a></li>' for i, (cid, name, *_r) in enumerate(CHAPTERS))
    hero = f'''<section class="jr-hero" id="top">
  <div class="jr-word" aria-hidden="true">2027</div>
  <div class="jr-side">
    <div class="xh-eye">The educator journey · 2027</div>
    <h1>Your own website and app. A few clicks, not a project.</h1>
    <p class="jr-lede">An academy app used to mean an agency, a developer and a long wait. Now you name your academy, connect your domain, add a course and start selling, all by yourself. Try it below and build your own, in 6 steps.</p>
    <ol class="jr-index">{idx}</ol>
    <div class="jr-tiles">
      <a href="#setup"><img src="/assets/x/s-studio-home.webp" alt="The AllCoaching studio home" width="800" height="450"/><span>It starts in your studio</span></a>
      <a href="#sell"><img src="/assets/x/s-getpaid-800.webp" alt="Get paid settings in the studio" width="800" height="450"/><span>Paid to your own bank</span></a>
    </div>
    <div class="xcta"><a class="xbtn xbtn-w" href="https://studio.allcoaching.in/">Start free trial</a><a class="xbtn xbtn-o" href="#build">Build my academy</a></div>
    <div class="xnote"><span>7 days free, no card needed</span><span>500+ educators</span></div>
  </div>
  <div class="jr-map">{constellation(pages)}</div>
</section>'''
    chapters, n = [], 0
    for ci, (cid, name, sub, col, slugs) in enumerate(CHAPTERS):
        feats = []
        for slug in slugs:
            n += 1
            feats.append(feature(pages[slug], n, pages))
        nxt = CHAPTERS[ci + 1] if ci + 1 < len(CHAPTERS) else None
        tail = (f'<a class="jr-next" href="#{nxt[0]}"><span>Next stage</span><b>{e(nxt[1])}</b><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg></a>' if nxt
                else '<a class="jr-next" href="/pricing"><span>Last step</span><b>Pick your plan</b><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>')
        chapters.append(f'''<section class="jr-ch" id="{cid}" style="--c:{col}" data-ch="{ci}">
  <div class="jr-in">
    <div class="jr-chh"><span class="jr-chn">Stage {ci + 1:02d} / {len(CHAPTERS):02d}</span><h2 class="jr-big">{e(name)}</h2><p>{e(sub)}</p></div>
    {''.join(feats)}
    {tail}
  </div>
</section>''')
    side = ''.join(f'<a href="#{cid}" data-ch="{i}"><span>{e(name)}</span><i></i></a>' for i, (cid, name, *_r) in enumerate(CHAPTERS))
    final = '''<section class="xfinal plain">
  <div class="xw">
    <h2 class="xd" style="font-size:clamp(44px,6vw,96px);max-width:14ch">Your journey, <b>free for 7 days.</b></h2>
    <p class="xlead">Do every step above in your own studio before you pay anything. No card, no developer, no sales call.</p>
    <div class="xcta"><a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start free trial</a><a class="xbtn xbtn-o" href="/pricing">See the plans</a></div>
    <p class="xlead" style="font-size:14px;color:rgba(255,255,255,.52)">Yearly plans from ₹6,999 · Monthly plans with 0% commission · Prices exclude GST</p>
  </div>
</section>'''
    main = hero + '\n' + open('assets/x/journey-build.html', encoding='utf-8').read().strip().replace('<!--PHONE-->', F.PHONE.replace('IMG', '/assets/x/m-home.webp').replace('ALT', 'The real academy app on a phone').replace(' loading="lazy"', '')) + '\n' + branding() + '\n<div class="jr-body"><nav class="jr-idx" aria-label="Stages">' + side + '</nav>\n' + '\n'.join(chapters) + '\n</div>\n' + final
    ld = F.jsonld([
        {'@context': 'https://schema.org', '@type': 'WebPage', '@id': URL + '#page', 'name': TITLE, 'description': DESC, 'url': URL, 'inLanguage': 'en-IN',
         'isPartOf': {'@type': 'WebSite', '@id': SITE + '/#website'}, 'dateModified': F.TODAY, 'about': {'@type': 'SoftwareApplication', '@id': SITE + '/#studio'}},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Educator journey', 'item': URL}]},
        {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'The educator journey on AllCoaching', 'numberOfItems': TOTAL, 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': pages[s]['nav'], 'url': '%s/features/%s' % (SITE, s)}
            for i, s in enumerate(s for c in CHAPTERS for s in c[4])]},
    ])
    page = F.shell_page(TITLE, DESC, 'educator journey, how to start online coaching, build online academy step by step, coaching app setup, sell courses online india',
                        URL, SITE + '/assets/x/tut/01.webp', 'The AllCoaching studio', ld, main)
    page = page.replace('xpage xin xfeat">', 'xpage xin xjr">', 1)
    page = page.replace('</head>', f'<link rel="stylesheet" href="/assets/x/journey.css?v={VER}"/>\n</head>', 1)
    page = page.replace('</body>', f'<script src="/assets/x/journey.js?v={VER}" defer></script>\n</body>', 1)
    return page


def register():
    sm = open('sitemap.xml', encoding='utf-8').read()
    if '/journey</loc>' not in sm:
        anchor = '<!-- features:start -->'
        sm = sm.replace(anchor, '<url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n  %s' % (URL, F.TODAY, anchor), 1)
        open('sitemap.xml', 'w', encoding='utf-8', newline='').write(sm)
    ll = open('llms.txt', encoding='utf-8').read()
    if '/journey)' not in ll:
        k = ll.index('## Features (each with a studio tutorial)')
        ll = ll[:k] + '- [Educator journey](%s): %s\n\n' % (URL, DESC) + ll[k:]
        open('llms.txt', 'w', encoding='utf-8', newline='').write(ll)
    print('registered /journey')


if __name__ == '__main__':
    pages = F.load()
    open('journey.html', 'w', encoding='utf-8', newline='').write(build(pages))
    print('built journey.html', TOTAL, 'steps')
    if '--register' in sys.argv:
        register()
