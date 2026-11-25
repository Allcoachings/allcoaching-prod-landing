#!/usr/bin/env python3
"""Build the product feature pages /features/<slug>.html and the hub /features/index.html
from data/features/<slug>.json (schema: data/features/_BRIEF.md).

Shell (head meta, footer, scripts) comes from vs/index.html; the X header is already in it.
Each page: dark hero with the studio tutorial (YouTube lite embed), light sheet with three
screenshot sections, the tutorial steps, a visible FAQ (mirrored verbatim in FAQPage JSON-LD)
and related features, then a dark final CTA.

Usage: python .claude/scripts/build_feature_pages.py            (build all)
       python .claude/scripts/build_feature_pages.py --check    (validate JSON only)
"""
import html, json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
SITE = 'https://allcoaching.in'
TODAY = '2026-11-25'
PLAYLIST = 'https://www.youtube.com/@Allcoaching'

# Studio tutorial episodes on the AllCoaching YouTube channel (2027 series).
EPS = {
    '01': ('c2s03E8TqtE', 'Set up your educator profile', '2026-11-25T11:00:00+05:30', 126),
    '02': ('HwCXi5r2VhE', 'Create and sell a course', '2026-11-26T11:00:00+05:30', 170),
    '03': ('zlzCLha8XNE', 'Upload course videos securely', '2026-11-26T15:00:00+05:30', 145),
    '04': ('TeVHM5F8ZP8', 'Sell PDF notes', '2026-11-26T19:00:00+05:30', 125),
    '05': ('0NgkE10LHZQ', 'Create a test series', '2026-11-27T11:00:00+05:30', 125),
    '06': ('_x8oR2eyddo', 'Take live classes', '2026-11-27T15:00:00+05:30', 126),
    '07': ('hx17qiQBfJo', 'Get students with free content', '2026-11-27T19:00:00+05:30', 108),
    '08': ('-7-X2VLpWBU', 'Get paid for your courses', '2026-11-28T11:00:00+05:30', 150),
    '09': ('uFt2H2sTCJk', 'Create discount codes', '2026-11-28T15:00:00+05:30', 101),
    '10': ('x4C8cyyqTCM', 'Engage students in your community', '2026-11-28T19:00:00+05:30', 104),
    '11': ('BvlaaDBeKrg', 'Track sales and transactions', '2026-11-29T11:00:00+05:30', 154),
    '12': ('eg8oydK4lCQ', 'Connect YouTube, Zoom and Razorpay', '2026-11-29T15:00:00+05:30', 88),
    '13': ('ufKAcit4tuE', 'Monthly vs yearly plans', '2026-11-29T19:00:00+05:30', 123),
    '14': ('Hq3QNfDHwuw', 'Create batches for a course', '2026-11-30T11:00:00+05:30', 200),
    '15': ('Df-61n1ntjE', 'Add teachers and staff', '2026-11-30T15:00:00+05:30', 104),
}
ART = {'academy-website': ('theme', '#2B44FF'), 'mobile-app': ('app', '#2B44FF'), 'courses': ('course', '#7C3AED'), 'notes-pdfs': ('pdfs', '#0891B2'), 'test-series': ('tests', '#D97706'), 'live-classes': ('live', '#DC2626'), 'free-content': ('free', '#0D9488'), 'payments': ('payments', '#16A34A'), 'discount-codes': ('coupons', '#EA580C'), 'community': ('community', '#2563EB'), 'integrations': ('integrations', '#4F46E5'), 'batches': ('batches', '#0EA5E9'), 'team': ('team', '#7C3AED'), 'analytics': ('tracking', '#9333EA')}

GROUPS = [('build', 'Build your academy'), ('teach', 'Teach'), ('sell', 'Sell and grow'), ('run', 'Run it')]
ORDER = ['academy-website', 'mobile-app', 'courses', 'notes-pdfs', 'test-series', 'live-classes', 'free-content',
         'payments', 'discount-codes', 'community', 'integrations', 'batches', 'team', 'analytics']

e = lambda s: html.escape(str(s), quote=True)
PHONE = open('assets/x/phone.html', encoding='utf-8').read().split('\n', 1)[1].strip()


def load():
    pages = {}
    for f in sorted(glob.glob('data/features/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        pages[d['slug']] = d
    return pages


def check(d):
    errs = []
    req = ['slug', 'nav', 'group', 'eps', 'title', 'description', 'eyebrow', 'h1', 'lede', 'notes', 'card', 'sections', 'steps', 'faq']
    for k in req:
        if k not in d:
            errs.append('missing ' + k)
    if errs:
        return errs
    if len(d['title']) > 65: errs.append('title %d chars' % len(d['title']))
    if not 50 <= len(d['description']) <= 175: errs.append('description %d chars' % len(d['description']))
    if d['group'] not in dict(GROUPS): errs.append('bad group')
    for ep in d['eps']:
        if ep not in EPS: errs.append('bad ep ' + ep)
    if len(d['sections']) != 3: errs.append('%d sections' % len(d['sections']))
    for s in d['sections']:
        if not os.path.exists(s['img'].lstrip('/')): errs.append('missing img ' + s['img'])
        if s.get('phone') and not os.path.exists(s['phone'].lstrip('/')): errs.append('missing phone ' + s['phone'])
    blob = json.dumps(d, ensure_ascii=False)
    for bad in ['!', 'free forever', '₹0', '#1', 'cheapest', '14-day trial', '14 day trial', '14 days free', '14 din', 'unlock', 'maximi', 'creator', 'Biology Lessons', 'CHEMPSI', 'DigiteKM']:
        if bad.lower() in blob.lower():
            errs.append('banned: ' + bad)
    return errs


def soft(t):
    # lower-case the first letter only when the next one is lower-case too (keeps PDFs, iOS)
    return t[0].lower() + t[1:] if len(t) > 1 and t[1].islower() else t


def iso_dur(sec):
    return 'PT%dM%dS' % (sec // 60, sec % 60)


def h1(parts):
    return '%s <span class="bd">%s</span>' % (e(parts[0]), e(parts[1])) if len(parts) > 1 else e(parts[0])


def h2(parts):
    return '%s <b>%s</b>' % (e(parts[0]), e(parts[1])) if len(parts) > 1 else e(parts[0])


def card(p, label=None):
    ep = p['eps'][0]
    art = ART.get(p['slug'], ('setup', '#2B44FF'))[0]
    return ('<a class="xf-card" href="/features/%s"><img src="/assets/x/art/%s.webp" alt="" loading="lazy" width="960" height="540"/>'
            '<div><small>%s</small><b>%s</b><span>%s</span></div></a>') % (p['slug'], art, e(label or dict(GROUPS)[p['group']]), e(p['nav']), e(p['card']))


def hero(p):
    ep = p['eps'][0]
    vid, vtitle, _, dur = EPS[ep]
    picks = ''
    if len(p['eps']) > 1:
        picks = '<div class="xf-picks" role="group" aria-label="Choose a tutorial">' + ''.join(
            '<button type="button" class="%s" data-ytpick="%s" data-thumb="/assets/x/tut/%s.webp" data-title="%s">EP %s · %s</button>' % (
                'on' if i == 0 else '', EPS[x][0], x, e(EPS[x][1]), x, e(EPS[x][1])) for i, x in enumerate(p['eps'])) + '</div>'
    notes = ''.join('<span>%s</span>' % e(n) for n in p['notes'])
    return f'''<section class="xphero" id="top">
  <div class="xw">
    <div class="tx">
      <div class="xf-crumb"><a href="/">Home</a><span>/</span><a href="/features/">Features</a><span>/</span>{e(p['nav'])}</div>
      <div class="xh-eye">{e(p['eyebrow'])}</div>
      <h1>{h1(p['h1'])}</h1>
      <p class="sub">{e(p['lede'])}</p>
      <div class="xcta">
        <a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start free trial</a>
        <a href="#tutorial" class="xbtn xbtn-o" onclick="var v=document.querySelector('.xyt');if(v){{v.scrollIntoView({{block:'center'}});v.click();}}return false;"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>Watch the tutorial</a>
      </div>
      <div class="xnote">{notes}</div>
    </div>
    <div class="vis" id="tutorial">
      <button type="button" class="xyt" data-yt="{vid}" aria-label="Play the tutorial: {e(vtitle)}"><img src="/assets/x/tut/{ep}.webp" alt="Studio tutorial: {e(vtitle)}" width="1280" height="720" fetchpriority="high"/><span class="pl"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></button>
      <div class="xf-vcap"><i>EP {ep}</i><b>{e(vtitle)}</b><span>{dur // 60} min · Hindi, with English audio</span></div>
      {picks}
    </div>
  </div>
</section>'''


def sections(p):
    out = []
    for i, s in enumerate(p['sections']):
        bullets = ''.join('<li>%s</li>' % e(b) for b in s.get('bullets', []))
        phone = ''
        if s.get('phone'):
            phone = PHONE.replace('IMG', s['phone']).replace('ALT', e(s.get('phone_alt') or ('%s on a phone' % p['nav'])))
        out.append(f'''<section class="xf-sec">
  <div class="xw xf-row{' rev' if i % 2 else ''}">
    <div class="xf-tx">
      <div class="xf-eye">{e(s['eyebrow'])}</div>
      <h2>{h2(s['h2'])}</h2>
      <p>{e(s['body'])}</p>
      {('<ul class="xf-ul">' + bullets + '</ul>') if bullets else ''}
    </div>
    <div class="xf-vis{' has-phone' if phone else ''}">
      <div class="xf-shot"><img src="{s['img']}" alt="{e(s['alt'])}" loading="lazy" width="1600" height="900"/></div>
      {phone}
    </div>
  </div>
</section>''')
    return '\n'.join(out)


def steps(p):
    lis = ''.join('<li><b>%s</b><span>%s</span></li>' % (e(s['t']), e(s['d'])) for s in p['steps'])
    return f'''<section class="xf-sec" id="how">
  <div class="xw">
    <div class="xf-steps-h"><div class="xf-eye">How it works</div><h2>{e(p['nav'])}, <b>step by step.</b></h2><p>The same steps as the studio tutorial at the top of this page.</p></div>
    <ol class="xf-steps">{lis}</ol>
  </div>
</section>'''


def faq(p):
    items = ''.join('<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if i == 0 else '', e(q['q']), e(q['a'])) for i, q in enumerate(p['faq']))
    return f'''<section class="xf-sec" id="faq">
  <div class="xw">
    <div class="xf-steps-h"><div class="xf-eye">Questions</div><h2>What educators ask <b>about {e(soft(p['nav']))}.</b></h2></div>
    <div class="xf-faq">{items}</div>
  </div>
</section>'''


def related(p, pages):
    same = [x for x in ORDER if x in pages and x != p['slug'] and pages[x]['group'] == p['group']]
    other = [x for x in ORDER if x in pages and x != p['slug'] and x not in same]
    pick = (same + other)[:3]
    cards = ''.join(card(pages[x]) for x in pick)
    return f'''<section class="xf-sec">
  <div class="xw">
    <div class="xf-steps-h"><div class="xf-eye">Keep exploring</div><h2>More from <b>your studio.</b></h2></div>
    <div class="xf-rel">{cards}</div>
    <p style="text-align:center;margin-top:36px"><a class="xbtn" style="background:#14161F;color:#fff" href="/features/">See all features</a></p>
  </div>
</section>'''


def final(title, sub):
    return f'''<section class="xfinal plain">
  <div class="xw">
    <h2 class="xd" style="font-size:clamp(44px,6vw,96px);max-width:14ch">{title}</h2>
    <p class="xlead">{sub}</p>
    <div class="xcta"><a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start free trial</a><a class="xbtn xbtn-o" href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
    <p class="xlead" style="font-size:14px;color:rgba(255,255,255,.52)">7 days free, no card needed · Monthly plans from ₹3,999 with 0% commission · Prices exclude GST</p>
  </div>
</section>'''


def jsonld(objs):
    return '\n'.join('<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False) for o in objs)


def ld_for(p):
    url = '%s/features/%s' % (SITE, p['slug'])
    objs = [
        {'@context': 'https://schema.org', '@type': 'WebPage', '@id': url + '#page', 'name': p['title'], 'description': p['description'], 'url': url,
         'inLanguage': 'en-IN', 'isPartOf': {'@type': 'WebSite', '@id': SITE + '/#website'}, 'dateModified': TODAY,
         'about': {'@type': 'SoftwareApplication', '@id': SITE + '/#studio'},
         'primaryImageOfPage': SITE + '/assets/x/tut/%s.webp' % p['eps'][0]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Features', 'item': SITE + '/features/'},
            {'@type': 'ListItem', 'position': 3, 'name': p['nav'], 'item': url}]},
    ]
    for ep in p['eps']:
        vid, vt, up, dur = EPS[ep]
        objs.append({'@context': 'https://schema.org', '@type': 'VideoObject', 'name': 'AllCoaching studio tutorial: ' + vt,
                     'description': '%s A step-by-step AllCoaching studio tutorial in Hindi, with an English audio track.' % p['card'],
                     'thumbnailUrl': [SITE + '/assets/x/tut/%s.webp' % ep], 'uploadDate': up, 'duration': iso_dur(dur),
                     'embedUrl': 'https://www.youtube.com/embed/' + vid, 'url': 'https://www.youtube.com/watch?v=' + vid,
                     'inLanguage': 'hi', 'publisher': {'@id': SITE + '/#organization'}})
    objs.append({'@context': 'https://schema.org', '@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
        {'@type': 'Question', 'name': q['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': q['a']}} for q in p['faq']]})
    return objs


def shell_page(title, desc, keywords, url, image, image_alt, ld, main):
    s = open('vs/index.html', encoding='utf-8').read()
    head, body = s[:s.index('</head>')], s[s.index('</head>'):]
    sub = lambda pat, rep, txt: re.sub(pat, lambda m: rep, txt, count=1)
    head = sub(r'<title>.*?</title>', '<title>%s</title>' % e(title), head)
    head = sub(r'<meta name="description" content="[^"]*"\s*/>', '<meta name="description" content="%s" />' % e(desc), head)
    head = sub(r'<meta name="keywords" content="[^"]*"\s*/>', '<meta name="keywords" content="%s" />' % e(keywords), head)
    head = sub(r'<link rel="canonical" href="[^"]*"\s*/>', '<link rel="canonical" href="%s" />' % url, head)
    for k, v in [('og:title', title), ('og:description', desc), ('og:url', url), ('og:image', image), ('og:image:alt', image_alt),
                 ('og:updated_time', TODAY + 'T12:00:00+05:30'), ('article:modified_time', TODAY)]:
        head = sub(r'<meta property="%s" content="[^"]*"\s*/>' % re.escape(k), '<meta property="%s" content="%s" />' % (k, e(v)), head)
    for k, v in [('twitter:title', title), ('twitter:description', desc), ('twitter:image', image), ('twitter:image:alt', image_alt)]:
        head = sub(r'<meta name="%s" content="[^"]*"\s*/>' % re.escape(k), '<meta name="%s" content="%s" />' % (k, e(v)), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', head, flags=re.S)
    head = re.sub(r'<style[^>]*>.*?</style>\s*', '', head, flags=re.S)
    head = head.replace('<link rel="stylesheet" href="/assets/x/x.css', ld + '\n<link rel="stylesheet" href="/assets/x/x.css', 1)
    a = body.index('<main id="main-content">'); b = body.index('</main>') + len('</main>')
    body = body[:a] + '<main id="main-content">\n' + main + '\n</main>' + body[b:]
    body = body.replace('<body class="uni bg-white text-[#14161F] antialiased xpage xin">', '<body class="uni bg-white text-[#14161F] antialiased xpage xin xfeat">')
    return head + body


def build_page(p, pages):
    main = '\n'.join([hero(p), '<div class="xlight xf">', sections(p), steps(p), faq(p), related(p, pages), '</div>',
                      final('%s, <b>free for 7 days.</b>' % e(p['nav']), 'Set it up in your own studio, under your own brand. No card, no developer, no sales call.')])
    url = '%s/features/%s' % (SITE, p['slug'])
    return shell_page(p['title'], p['description'], p.get('keywords', ''), url, SITE + '/assets/x/tut/%s.webp' % p['eps'][0],
                      'AllCoaching studio tutorial: ' + EPS[p['eps'][0]][1], jsonld(ld_for(p)), main)


def build_hub(pages):
    groups = ''
    for g, label in GROUPS:
        items = [pages[x] for x in ORDER if x in pages and pages[x]['group'] == g]
        if not items:
            continue
        groups += '<div class="xf-group"><div class="xf-eye">%s</div><h2>%s</h2><div class="xf-rel">%s</div></div>' % (
            e(label), {'build': 'Your website, <b>your app.</b>', 'teach': 'Everything you teach, <b>in one place.</b>',
                       'sell': 'Get paid and <b>grow.</b>', 'run': 'Run your academy <b>like a team.</b>'}[g],
            ''.join(card(p, 'EP ' + p['eps'][0] + ' · tutorial') for p in items))
    main = f'''<section class="xphero solo" id="top">
  <div class="xw"><div class="tx">
    <div class="xf-crumb"><a href="/">Home</a><span>/</span>Features</div>
    <div class="xh-eye">Features · with a studio tutorial for each</div>
    <h1>Everything your academy needs. <span class="bd">In one studio.</span></h1>
    <p class="sub">Your website and app, courses, tests, live classes, payments and your team, all from one AllCoaching login. Every feature below has a short studio tutorial, so you can see exactly how it works before you start.</p>
    <div class="xcta"><a href="https://studio.allcoaching.in/" class="xbtn xbtn-w">Start free trial</a><a href="{PLAYLIST}" class="xbtn xbtn-o" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>All tutorials on YouTube</a></div>
    <div class="xnote"><span>7 days free, no card needed</span><span>{len(pages)} features</span><span>Hindi, with English audio</span></div>
  </div></div>
</section>
<div class="xlight xf"><section class="xf-sec"><div class="xw">{groups}</div></section></div>
{final('Build your academy <b>on AllCoaching.</b>', 'Sign up, upload your course, connect your domain and start selling. Free for 7 days.')}'''
    url = SITE + '/features/'
    title = 'AllCoaching Features: Website, App, Courses, Tests, Payments'
    desc = 'Every AllCoaching feature in one place: your website and app, courses, test series, live classes, payments and team, each with a short studio tutorial.'
    ld = [
        {'@context': 'https://schema.org', '@type': 'CollectionPage', '@id': url + '#page', 'name': title, 'description': desc, 'url': url,
         'inLanguage': 'en-IN', 'isPartOf': {'@type': 'WebSite', '@id': SITE + '/#website'}, 'dateModified': TODAY, 'mainEntity': {'@id': url + '#list'}},
        {'@context': 'https://schema.org', '@type': 'ItemList', '@id': url + '#list', 'name': 'AllCoaching features', 'numberOfItems': len(pages),
         'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': pages[x]['nav'], 'url': SITE + '/features/' + x}
                             for i, x in enumerate([x for x in ORDER if x in pages])]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Features', 'item': url}]},
    ]
    return shell_page(title, desc, 'AllCoaching features, online coaching platform features, LMS for educators India, studio tutorials',
                      url, SITE + '/assets/x/tut/02.webp', 'AllCoaching studio tutorials', jsonld(ld), main)


if __name__ == '__main__':
    pages = load()
    bad = False
    for slug, p in pages.items():
        errs = check(p)
        if errs:
            bad = True
            print('ERR', slug, errs)
    if '--check' in sys.argv or bad:
        print('checked', len(pages), 'pages', 'with errors' if bad else 'ok')
        sys.exit(1 if bad else 0)
    os.makedirs('features', exist_ok=True)
    for slug, p in pages.items():
        open('features/%s.html' % slug, 'w', encoding='utf-8', newline='').write(build_page(p, pages))
    open('features/index.html', 'w', encoding='utf-8', newline='').write(build_hub(pages))
    print('built', len(pages), 'feature pages + hub')


# ---------------------------------------------------------------- registration
def register(pages):
    """Idempotently add the feature pages to sitemap.xml and llms.txt (between marker comments)."""
    slugs = [x for x in ORDER if x in pages]
    # sitemap.xml: one block after the /vs/ hub entry
    sm = open('sitemap.xml', encoding='utf-8').read()
    sm = re.sub(r'\s*<!-- features:start -->.*?<!-- features:end -->', '', sm, flags=re.S)
    urls = ['/features/'] + ['/features/' + s for s in slugs]
    block = '\n  <!-- features:start -->' + ''.join(
        '\n  <url>\n    <loc>%s%s</loc>\n    <lastmod>%sT12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>' % (
            SITE, u, TODAY, '0.8' if u == '/features/' else '0.7') for u in urls) + '\n  <!-- features:end -->'
    anchor = '<loc>https://allcoaching.in/vs/</loc>'
    i = sm.index(anchor); j = sm.index('</url>', i) + len('</url>')
    sm = sm[:j] + block + sm[j:]
    open('sitemap.xml', 'w', encoding='utf-8', newline='').write(sm)
    # llms.txt: a "Features" section right before "## Other pages"
    ll = open('llms.txt', encoding='utf-8').read()
    ll = re.sub(r'## Features \(each with a studio tutorial\)\n.*?(?=\n## )', '', ll, flags=re.S)
    lines = ['## Features (each with a studio tutorial)', '',
             '- [All features](%s/features/): Every AllCoaching feature in one place, each with a short studio tutorial video in Hindi with English audio.' % SITE]
    for s in slugs:
        p = pages[s]
        lines.append('- [%s](%s/features/%s): %s' % (p['nav'], SITE, s, p['description']))
    sec = '\n'.join(lines) + '\n\n'
    k = ll.index('## Other pages')
    ll = ll[:k] + sec + ll[k:]
    open('llms.txt', 'w', encoding='utf-8', newline='').write(ll)
    print('registered', len(urls), 'urls in sitemap.xml and llms.txt')


if __name__ == '__main__' and '--register' in sys.argv:
    register(load())
