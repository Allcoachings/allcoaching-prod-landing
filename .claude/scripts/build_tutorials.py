#!/usr/bin/env python3
"""Build /tutorials.html: Studio Tutorials 2027, all 15 episodes in one place.

Source of truth for episodes = EPS in build_feature_pages.py (YouTube id, title, release time, duration);
each episode links to the feature guide that uses it. Episodes whose release time is still in the future
show "Releases <date>" and turn playable on their own once the time passes (checked in the browser).

Usage: python .claude/scripts/build_tutorials.py [--register]
"""
import datetime as dt
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_feature_pages as F  # noqa: E402  (chdirs to the repo root)

e = F.e
SITE = F.SITE
URL = SITE + '/tutorials'
TITLE = 'Studio Tutorials 2027: Learn the AllCoaching Studio | AllCoaching'
DESC = 'Fifteen short videos that show every part of the AllCoaching studio, from your profile and first course to payments, live classes, batches and your team.'
VER = '3'

STAGES = [
    ('Set up', ['01', '12', '13']),
    ('Create', ['02', '03', '04', '05']),
    ('Teach', ['06', '10', '14']),
    ('Sell', ['07', '08', '09']),
    ('Run', ['11', '15']),
]


def is_public(vid):
    try:
        urllib.request.urlopen('https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=' + vid, timeout=10)
        return True
    except Exception:
        return False


def ep_to_feature(pages):
    m = {}
    for slug in F.ORDER:
        for ep in pages[slug]['eps']:
            m.setdefault(ep, slug)
    return m


def when(iso):
    t = dt.datetime.fromisoformat(iso)
    return t.strftime('%-d %b, %-I:%M %p') if os.name != 'nt' else t.strftime('%d %b, %I:%M %p').lstrip('0').replace(', 0', ', ')


def mins(sec):
    return '%d:%02d' % (sec // 60, sec % 60)


def build(pages):
    f_of = ep_to_feature(pages)
    first = '01'
    vid0, t0, _u0, _d0 = F.EPS[first]
    cards = []
    for name, eps in STAGES:
        items = []
        for ep in eps:
            vid, title, up, dur = F.EPS[ep]
            slug = f_of.get(ep)
            guide = f'<a class="tu-guide" href="/features/{slug}">Read the guide</a>' if slug else '<a class="tu-guide" href="/pricing">See the plans</a>'
            live = ' data-live="1"' if is_public(vid) else ''
            items.append(f'''<li class="tu-ep" data-up="{up}"{live}>
          <button type="button" class="tu-play" data-ytpick="{vid}" data-thumb="/assets/x/tut/{ep}.webp" data-title="{e(title)}" data-ep="{ep}" aria-label="Play EP {ep}: {e(title)}">
            <span class="tu-th"><img src="/assets/x/tut/{ep}.webp" alt="" loading="lazy" width="1280" height="720"/><span class="tu-dur">{mins(dur)}</span><span class="tu-soon">Releases {e(when(up))}</span></span>
            <span class="tu-meta"><em>EP {ep}</em><b>{e(title)}</b></span>
          </button>
          {guide}
        </li>''')
        cards.append(f'<section class="tu-stage"><h2><span>{e(name)}</span><i>{len(eps)} videos</i></h2><ol class="tu-grid">{"".join(items)}</ol></section>')
    main = f'''<section class="tu-hero">
  <div class="xw">
    <div class="tu-head">
      <div class="xh-eye">Studio Tutorials 2027 · 15 videos</div>
      <h1>Learn the whole studio. <b>Two minutes at a time.</b></h1>
      <p>Short videos in Hindi, with an English audio track on YouTube. Each one shows a real part of the AllCoaching studio, step by step.</p>
    </div>
    <div class="tu-player">
      <div class="xf-video"><button type="button" class="xyt" data-yt="{vid0}" aria-label="Play the tutorial: {e(t0)}"><img src="/assets/x/tut/{first}.webp" alt="Studio tutorial: {e(t0)}" width="1280" height="720" fetchpriority="high"/><span class="pl"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></button></div>
      <div class="tu-now"><span>Now playing</span><b class="xf-vcap"><b>{e(t0)}</b></b><a href="{F.PLAYLIST}" target="_blank" rel="noopener">All videos on YouTube</a></div>
    </div>
  </div>
</section>
<div class="xlight tu-body">
  <div class="xw">
    {"".join(cards)}
    <div class="tu-help"><b>Stuck on a step?</b><span>Message the team on WhatsApp, in Hindi or English.</span><a class="xbtn xbtn-d" href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
  </div>
</div>
''' + F.final('Watch, then <b>build it yourself.</b>', 'Every step in these videos works in your own studio during the 7-day free trial. No card, no developer, no sales call.')
    objs = [
        {'@context': 'https://schema.org', '@type': 'WebPage', '@id': URL + '#page', 'name': TITLE, 'description': DESC, 'url': URL, 'inLanguage': 'en-IN',
         'isPartOf': {'@type': 'WebSite', '@id': SITE + '/#website'}, 'dateModified': F.TODAY},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Studio tutorials', 'item': URL}]},
        {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'AllCoaching Studio Tutorials 2027', 'numberOfItems': len(F.EPS), 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'item': {
                '@type': 'VideoObject', 'name': 'AllCoaching studio tutorial: ' + F.EPS[ep][1],
                'description': 'A step-by-step AllCoaching studio tutorial in Hindi, with an English audio track: ' + F.EPS[ep][1] + '.',
                'thumbnailUrl': [SITE + '/assets/x/tut/%s.webp' % ep], 'uploadDate': F.EPS[ep][2], 'duration': F.iso_dur(F.EPS[ep][3]),
                'embedUrl': 'https://www.youtube.com/embed/' + F.EPS[ep][0], 'url': 'https://www.youtube.com/watch?v=' + F.EPS[ep][0],
                'inLanguage': 'hi', 'publisher': {'@id': SITE + '/#organization'}}}
            for i, ep in enumerate(sorted(F.EPS))]},
    ]
    page = F.shell_page(TITLE, DESC, 'allcoaching studio tutorial, how to use allcoaching, online coaching app tutorial hindi, create online course tutorial, sell courses online tutorial',
                        URL, SITE + '/assets/x/tut/01.webp', 'AllCoaching Studio Tutorials 2027', F.jsonld(objs), main)
    page = page.replace('xpage xin xfeat">', 'xpage xin xfeat xtu">', 1)
    page = page.replace('</head>', f'<link rel="stylesheet" href="/assets/x/tutorials.css?v={VER}"/>\n</head>', 1)
    page = page.replace('</body>', f'<script src="/assets/x/tutorials.js?v={VER}" defer></script>\n</body>', 1)
    return page


def register():
    sm = open('sitemap.xml', encoding='utf-8').read()
    if '/tutorials</loc>' not in sm:
        anchor = '<!-- features:start -->'
        sm = sm.replace(anchor, '<url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n  %s' % (URL, F.TODAY, anchor), 1)
        open('sitemap.xml', 'w', encoding='utf-8', newline='').write(sm)
    ll = open('llms.txt', encoding='utf-8').read()
    if '/tutorials)' not in ll:
        k = ll.index('## Features (each with a studio tutorial)')
        ll = ll[:k] + '- [Studio Tutorials 2027](%s): %s\n\n' % (URL, DESC) + ll[k:]
        open('llms.txt', 'w', encoding='utf-8', newline='').write(ll)
    print('registered /tutorials')


if __name__ == '__main__':
    pages = F.load()
    open('tutorials.html', 'w', encoding='utf-8', newline='').write(build(pages))
    print('built tutorials.html', len(F.EPS), 'episodes')
    if '--register' in sys.argv:
        register()
