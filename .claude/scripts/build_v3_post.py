"""Build a v3 (Shopify-style guide layout) blog post from a content JSON file.

Usage: python .claude/scripts/build_v3_post.py .claude/skills/academy-guide-blog/content/<slug>.json

The JSON holds only content; this script supplies the page shell (head + 6 JSON-LD blocks, header, promo,
hero, three-column grid, CTA cards, more-guides grid, sign-up band, footer, scripts) so every post is
identical in structure. After writing the HTML it runs v3_sync_schema.py (FAQ / HowTo / glossary schema
from the DOM, word count, read time).

Content JSON keys
  slug, dir ("blog" | "blogs/en" | "blogs/hinglish"), lang (default "en-IN")
  title (<=65 chars), description (140-172 chars), og_description, keywords (list)
  h1, dek, category (eyebrow + articleSection), date_published, date_modified, checked (optional "24 Oct 2026")
  cover_alt, audience
  intro: [html paragraphs]           takeaways: [html list items]
  sections: [{id, h2, toc (short label or null), html}]
     inside html you may use:
       {{fig:name|alt|caption}}   -> figure from assets/blog/<slug>/<name>.webp (size read from the file)
       {{cta}}                    -> inline CTA card       {{steps}} -> numbered HowTo steps
       {{q:Question|Answer html}} -> question box
  steps: {name, description, total_time, items: [[name, text], ...]}
  faq: [[question, answer], ...]  (plain text answers; 6-10)
  glossary: [[id, term, definition], ...]
  references: [html, ...]
  about: [{name, sameAs?}], mentions: [{name, url?, type?}]
  related: [path, ...]  e.g. "/blog/how-to-sell-courses-online-in-india"
"""
import html as H, json, os, re, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(ROOT, 'blog', 'seo-for-online-academy-beginners-guide.html')
SITE = 'https://allcoaching.in'
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 3l5 5-5 5"/></svg>'


def e(t):
    return H.escape(t, quote=True)


def shell_parts():
    ref = open(REF, encoding='utf-8').read()
    gtm = re.search(r'  <!-- Google Tag Manager -->\n  <script>.*?</script>\n', ref, re.S).group(0)
    header = ref[ref.index('<header class="v3-head">'):ref.index('</aside>', ref.index('<aside class="v3-promo"')) + len('</aside>')]
    foot = ref[ref.index('<!-- ================= FOOTER ================= -->'):ref.index('</body>')]
    band = ref[ref.index('<section class="v3-band"'):ref.index('</section>', ref.index('<section class="v3-band"')) + len('</section>')]
    return gtm, header, foot, band


def img_size(path):
    with Image.open(path) as im:
        return im.size


def page_meta(path):
    """Title + image for a related-post card."""
    rel = path.strip('/')
    f = os.path.join(ROOT, rel + '.html')
    if not os.path.exists(f):
        return None
    s = open(f, encoding='utf-8').read()
    t = re.search(r'<title>(.*?)</title>', s, re.S).group(1).split(' | ')[0]
    slug = rel.split('/')[-1]
    local = os.path.join(ROOT, 'assets', 'blog', slug, 'cover.webp')
    if os.path.exists(local):
        img = f'/assets/blog/{slug}/cover.webp'
    else:
        m = re.search(r'property="og:image" content="([^"]+)"', s)
        img = m.group(1) if m else ''
    cat = re.search(r'"articleSection":"([^"]+)"', s)
    return H.unescape(t), img, (cat.group(1) if cat else 'Guide')


def expand(htm, c):
    slug = c['slug']

    def fig(m):
        name, alt, cap = (m.group(1).split('|') + ['', ''])[:3]
        p = os.path.join(ROOT, 'assets', 'blog', slug, name + '.webp')
        if not os.path.exists(p):
            p2 = os.path.join(ROOT, 'assets', 'blog', 'seo-for-online-academy-beginners-guide', name + '.webp')
            if os.path.exists(p2):
                p, src = p2, f'/assets/blog/seo-for-online-academy-beginners-guide/{name}.webp'
            else:
                sys.exit(f'missing figure {name}.webp for {slug}')
        else:
            src = f'/assets/blog/{slug}/{name}.webp'
        w, h = img_size(p)
        capt = f'\n        <figcaption>{cap}</figcaption>' if cap else ''
        return (f'<figure class="v3-fig">\n        <img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async" />{capt}\n      </figure>')

    def q(m):
        qq, a = m.group(1).split('|', 1)
        return (f'<div class="v3-q">\n        <p class="l">Question educators ask</p>\n        <h3>{qq}</h3>\n        <p>{a}</p>\n      </div>')

    htm = re.sub(r'\{\{fig:(.*?)\}\}', fig, htm)
    htm = re.sub(r'\{\{q:(.*?)\}\}', q, htm, flags=re.S)
    cta = ('<div class="v3-cta">\n        <p class="t">Build your own academy. <em>Try it free for 14 days.</em></p>\n'
           '        <p class="s">Website on your own domain, your own Android and iOS app, unlimited live classes and UPI checkout on every plan. Plans from ₹6,999 a year after the trial (excl. GST).</p>\n'
           '        <div class="row"><a href="https://studio.allcoaching.in/" class="v3-btn">Start free trial</a><a href="/pricing" class="v3-btn ghost">See plans</a></div>\n'
           '        <small>No card needed · Cancel anytime in the trial · Your data stays exportable</small>\n      </div>')
    htm = htm.replace('{{cta}}', cta)
    if '{{cost_table}}' in htm:
        htm = htm.replace('{{cost_table}}', cost_table(slug))
    if '{{steps}}' in htm:
        items = ''.join(f'\n        <li><b>{n}</b><span>{t}</span></li>' for n, t in c['steps']['items'])
        htm = htm.replace('{{steps}}', f'<ol class="v3-steps" id="howto-steps" data-total-time="{c["steps"].get("total_time", "P14D")}">{items}\n      </ol>')
    return htm


def cost_table(slug):
    """Cost-at-sales-level table computed from graphics/specs/<slug>.json (same maths as the chart)."""
    sys.path.insert(0, os.path.join(ROOT, '.claude', 'skills', 'academy-guide-blog', 'scripts'))
    import comparison_graphics as cg
    sp = json.load(open(os.path.join(ROOT, '.claude', 'skills', 'academy-guide-blog', 'graphics', 'specs', slug + '.json'), encoding='utf-8'))
    c = sp['cost']
    levels = c.get('levels', [0, 100000, 300000, 500000, 1000000])
    comps = c['competitors']

    def best_ac(sales):
        p, f, n = min(cg.AC_PLANS, key=lambda x: x[0] + x[1] * sales)
        return f'{cg.inr(p + f * sales)} ({n})'

    def label(v):
        return '₹0' if v == 0 else (f'₹{v / 100000:g} lakh' if v >= 100000 else cg.inr(v))
    head = '<th>Your sales in a year</th><th>AllCoaching (best plan)</th>' + ''.join(f'<th>{H.escape(x["name"])}</th>' for x in comps)
    rows = ''.join('<tr><td>' + label(v) + '</td><td>' + best_ac(v) + '</td>' +
                   ''.join(f'<td>{cg.inr(cg.comp_cost(x["plans"], v))}</td>' for x in comps) + '</tr>' for v in levels)
    notes = ' '.join(x['note'] + '.' for x in comps if x.get('note'))
    return (f'<div class="v3-table"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody>'
            f'<caption>Plan price + published fee on sales, cheapest plan per row, before GST. {H.escape(notes)}</caption></table></div>')


def build(cpath):
    c = json.load(open(cpath, encoding='utf-8'))
    slug, d = c['slug'], c.get('dir', 'blog')
    url = f'{SITE}/{d}/{slug}'
    cover = f'{SITE}/assets/blog/{slug}/cover.webp'
    gtm, header, foot, band = shell_parts()
    date_p, date_m = c['date_published'], c.get('date_modified', '2026-10-24')

    toc = [(s['id'], s['toc']) for s in c['sections'] if s.get('toc')] + [('faq', c.get('faq_toc', 'FAQ'))]
    toc_html = ''.join(f'\n        <li><a href="#{i}">{e(t)}</a></li>' for i, t in toc)

    secs = ''
    for s in c['sections']:
        secs += f'\n\n    <section id="{s["id"]}">\n      <h2>{s["h2"]}</h2>\n      {expand(s["html"], c)}\n    </section>'

    faq = ''.join(f'\n      <details open><summary>{e(q)}</summary><p>{a}</p></details>' for q, a in c['faq'])
    gl = ''.join(f'\n        <dt><dfn id="dfn-{i}">{e(t)}</dfn></dt>\n        <dd>{dd}</dd>' for i, t, dd in c['glossary'])
    refs = ''.join(f'\n        <li id="ref-{k + 1}">{r}</li>' for k, r in enumerate(c.get('references', [])))
    keys = ''.join(f'\n        <li>{t}</li>' for t in c['takeaways'])
    intro = '\n      '.join(f'<p>{p}</p>' for p in c['intro'])
    checked = (f'<p class="v3-checked">Prices and plans checked on official sites · {e(c["checked"])} · Sources linked below</p>' if c.get('checked') else '')

    rel = [page_meta(p) + (p,) for p in c.get('related', []) if page_meta(p)]
    rail = ''.join(f'\n    <a class="v3-rail-post" href="{p}"><small>{e(cat)}</small><span>{e(t)}</span></a>' for t, img, cat, p in rel[:4])
    more = ''.join(f'\n    <a href="{p}"><div class="th"><img src="{img}" alt="" width="1600" height="900" loading="lazy" /></div><small>{e(cat)}</small><span>{e(t)}</span></a>' for t, img, cat, p in rel[:4])

    about = [{"@type": "Thing", **a} for a in c.get('about', [])]
    mentions = [{"@type": m.pop('type', 'Organization'), **m} for m in [dict(x) for x in c.get('mentions', [])]]
    article = {
        "@context": "https://schema.org", "@type": ["Article", "TechArticle"], "@id": url + '#article',
        "headline": re.sub('<.*?>', '', c['h1']), "description": c['description'],
        "image": {"@type": "ImageObject", "url": cover, "width": 1600, "height": 900},
        "author": {"@id": "https://allcoaching.in/author/amit-ratan#person", "@type": "Person", "name": "Amit Ratan", "jobTitle": "Founder & CEO",
                   "worksFor": {"@id": "https://allcoaching.in/#organization"}, "url": "https://allcoaching.in/author/amit-ratan",
                   "image": "https://allcoaching.in/assets/amit-ratan-2026.webp",
                   "sameAs": ["https://www.linkedin.com/in/allamitk/", "https://x.com/allamitk", "https://www.instagram.com/allamitk/",
                              "https://allcoaching.in/about", "https://allcoaching.in/manifesto", "https://allcoaching.in/author/amit-ratan"]},
        "publisher": {"@type": "Organization", "@id": "https://allcoaching.in/#organization", "name": "AllCoaching", "url": "https://allcoaching.in",
                      "logo": {"@type": "ImageObject", "url": "https://allcoaching.in/assets/logo/allcoaching-logo.webp?v=20260707", "width": 512, "height": 512},
                      "sameAs": ["https://x.com/allcoachings", "https://www.youtube.com/@Allcoaching", "https://www.instagram.com/allcoachings/",
                                 "https://www.facebook.com/allcoaching.in", "https://t.me/allcoaching", "https://play.google.com/store/apps/details?id=org.student.allcoaching"]},
        "datePublished": date_p, "dateModified": date_m,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "isPartOf": {"@type": "Blog", "@id": "https://allcoaching.in/blog/"},
        "articleSection": c['category'], "inLanguage": c.get('lang', 'en-IN'), "wordCount": 0, "timeRequired": "PT0M",
        "audience": {"@type": "Audience", "audienceType": c.get('audience', 'Indian educators, tutors and coaching institute owners')},
        "about": about, "mentions": mentions,
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#tldr", "#faq summary", "#faq details > p", "#glossary dt"]},
        "citation": c.get('citations', []),
    }
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://allcoaching.in/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://allcoaching.in/blog/"},
        {"@type": "ListItem", "position": 3, "name": c['title'], "item": url}]}
    software = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "AllCoaching", "url": "https://allcoaching.in",
                "applicationCategory": "EducationalApplication", "applicationSubCategory": "Learning management system for educators",
                "operatingSystem": "Web, Android, iOS",
                "description": "AllCoaching works like Shopify for coaching: sign up, choose a plan, upload a course, connect your own domain and start selling, with payments, student access, apps and hosting handled automatically.",
                "offers": {"@type": "AggregateOffer", "priceCurrency": "INR", "lowPrice": "6999", "highPrice": "24999", "offerCount": "3",
                           "description": "14-day free trial with no card needed, then Starter ₹6,999, Growth ₹12,999 or Pro ₹24,999 per year (excl. GST), with a 10%, 7.5% or 5% platform fee on sales."},
                "featureList": ["Academy website on your own connected domain", "Own white-label Android and iOS app", "Unlimited live classes via YouTube Live, Zoom or the built-in live room",
                                "Unlimited videos via YouTube", "Courses, PDF notes and test series", "UPI and card checkout with automatic Razorpay payouts",
                                "Meta Pixel and Google Tag Manager", "Free customizable themes and templates", "Student data export", "Marketplace discovery on the AllCoaching app"],
                "provider": {"@id": "https://allcoaching.in/#organization"}, "countriesSupported": "IN"}

    def ld(o):
        return '  <script type="application/ld+json">\n  ' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '\n  </script>\n'

    kw = ', '.join(c['keywords'])
    head = f'''<!doctype html>
<html lang="{c.get('lang', 'en-IN')}" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#FFFFFF" />
  <meta name="color-scheme" content="light" />
  <meta name="application-name" content="AllCoaching" />
{gtm}
  <title>{e(c['title'])}</title>
  <meta name="description" content="{e(c['description'])}" />
  <meta name="keywords" content="{e(kw)}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="author" content="Amit Ratan, Founder &amp; CEO, AllCoaching" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" type="application/rss+xml" title="AllCoaching Blog" href="https://allcoaching.in/feed.xml" />
  <link rel="icon" type="image/webp" href="/assets/fevicon.webp?v=20260707" />
  <link rel="apple-touch-icon" href="/assets/logo/allcoaching-logo.webp?v=20260707" />
  <link rel="manifest" href="/manifest.webmanifest" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="AllCoaching" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{e(c['title'])}" />
  <meta property="og:description" content="{e(c.get('og_description', c['description']))}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{cover}" />
  <meta property="og:image:width" content="1600" />
  <meta property="og:image:height" content="900" />
  <meta property="og:image:alt" content="{e(c['cover_alt'])}" />
  <meta property="article:published_time" content="{date_p}T09:00:00+05:30" />
  <meta property="article:modified_time" content="{date_m}T09:00:00+05:30" />
  <meta property="article:author" content="https://allcoaching.in/author/amit-ratan" />
  <meta property="article:section" content="{e(c['category'])}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@allcoachings" />
  <meta name="twitter:title" content="{e(c['title'])}" />
  <meta name="twitter:description" content="{e(c.get('og_description', c['description']))}" />
  <meta name="twitter:image" content="{cover}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" as="image" href="/assets/blog/{slug}/cover.webp" fetchpriority="high" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300..700&family=IBM+Plex+Mono:wght@500;600&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/brand.css?v=20261015" />
  <link rel="stylesheet" href="/blog-v3.css?v=20261024b" />

  <!-- Schema 1/6: Article -->
{ld(article)}
  <!-- Schema 2/6: FAQPage (built from #faq by v3_sync_schema.py) -->
{ld({"@context": "https://schema.org", "@type": "FAQPage"})}
  <!-- Schema 3/6: BreadcrumbList -->
{ld(crumbs)}
  <!-- Schema 4/6: HowTo (built from #howto-steps) -->
{ld({"@context": "https://schema.org", "@type": "HowTo"})}
  <!-- Schema 5/6: SoftwareApplication -->
{ld(software)}
  <!-- Schema 6/6: DefinedTermSet (built from #glossary) -->
{ld({"@context": "https://schema.org", "@type": "DefinedTermSet"})}</head>
'''
    body = f'''
<body class="v3">
<div class="v3-progress" id="progress" aria-hidden="true"></div>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T3KFKD3G" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

{header}

<header class="v3-hero">
  <p class="v3-eyebrow"><a href="/blog/">Blog</a><i></i><span>{e(c['category'])}</span></p>
  <h1>{c['h1']}</h1>
  <p class="v3-dek">{c['dek']}</p>
  {checked}
  <figure class="v3-cover">
    <img src="/assets/blog/{slug}/cover.webp" alt="{e(c['cover_alt'])}" width="1600" height="900" fetchpriority="high" decoding="async" />
  </figure>
</header>

<div class="v3-grid">
  <aside class="v3-left">
    <nav class="v3-toc" aria-label="On this page">
      <h2>On this page</h2>
      <ol id="toc-list">{toc_html}
      </ol>
    </nav>
    <div class="v3-sidecta">
      <p>Start your online academy today. <b>14 days free.</b></p>
      <a href="https://studio.allcoaching.in/">Start free trial {ARROW}</a>
    </div>
  </aside>

  <article class="v3-body" id="article">
    <div class="v3-byline v3-byline-m">
      <img src="/assets/amit-ratan-2026.webp" alt="Amit Ratan" width="56" height="56" loading="lazy" />
      <div><b><a href="/author/amit-ratan">Amit Ratan</a></b><span>Updated {fmt(date_m)} · <span class="rt">min read</span></span></div>
    </div>
    <details class="v3-toc-m">
      <summary>On this page</summary>
      <ol></ol>
    </details>
    <div class="v3-sidecta-m"><div class="v3-sidecta"><p>Start your online academy today. <b>14 days free.</b></p><a href="https://studio.allcoaching.in/">Start free trial {ARROW}</a></div></div>

    <section id="intro">
      {intro}
    </section>

    <div class="v3-keys" id="tldr">
      <h2>Key takeaways</h2>
      <ul>{keys}
      </ul>
    </div>
{secs}

    <section id="glossary" class="v3-gloss">
      <h2>{c.get('glossary_title', 'Glossary')}</h2>
      <dl>{gl}
      </dl>
    </section>

    <section id="faq" class="v3-faq">
      <h2>{c.get('faq_title', 'Frequently asked questions')}</h2>{faq}
    </section>

    <section id="references" class="v3-refs">
      <h2>Sources</h2>
      <ol>{refs}
      </ol>
    </section>

    <div class="v3-author" id="about-author">
      <img src="/assets/amit-ratan-2026.webp" alt="Amit Ratan, Founder and CEO of AllCoaching" width="72" height="72" loading="lazy" />
      <div>
        <b><a href="/author/amit-ratan">Amit Ratan</a></b>
        <span>Founder &amp; CEO, AllCoaching</span>
        <p>Amit builds AllCoaching, the academy platform Indian educators set up themselves: their own website on their own domain, their own app, and the tools to grow it. AllCoaching wrote this comparison, so we link every competitor figure to its official source and say where another option fits better.</p>
      </div>
    </div>
  </article>

  <aside class="v3-right">
    <div class="v3-byline">
      <img src="/assets/amit-ratan-2026.webp" alt="Amit Ratan" width="56" height="56" loading="lazy" />
      <div><b><a href="/author/amit-ratan">Amit Ratan</a></b><span>Updated {fmt(date_m)} · <span class="rt">min read</span></span></div>
    </div>
    <p class="v3-rail-h">Related guides</p>{rail}
  </aside>
</div>

<section class="v3-more" aria-label="More guides">
  <h2>More guides for educators</h2>
  <div class="v3-more-grid">{more}
  </div>
</section>

{band}

{foot}</body>
</html>
'''
    out = os.path.join(ROOT, d, slug + '.html')
    open(out, 'w', encoding='utf-8').write(head + body)
    subprocess.run([sys.executable, os.path.join(ROOT, '.claude', 'scripts', 'v3_sync_schema.py'), out], check=True)


def fmt(iso):
    import datetime
    dt = datetime.date.fromisoformat(iso)
    return dt.strftime('%-d %b %Y')


if __name__ == '__main__':
    for p in sys.argv[1:]:
        build(p)
