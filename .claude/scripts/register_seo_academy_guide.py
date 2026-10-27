"""One-off: register /blog/seo-for-online-academy-beginners-guide in sitemap, llms.txt and blog/index.html."""
import re, json, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

slug = "seo-for-online-academy-beginners-guide"
url = f"https://allcoaching.in/blog/{slug}"
img = f"https://allcoaching.in/assets/blog/{slug}/cover.webp"
head = "Online Academy SEO: The Beginner's Guide for Indian Educators (2026)"
card = "Online Academy SEO: The Beginner's Guide for Educators"
tag = "Marketing &middot; 2026"
dek = "How students find courses on Google, the keywords to target, course pages that rank, and how to get cited in AI answers."
alt = "Get your academy found on Google: an educator's own academy ranking first for an SSC CGL maths search"
date = "2026-10-24"
llms = (f"- [{head}]({url}): A step-by-step SEO guide for Indian educators who run their own online academy, in a Shopify-style guide layout with 14 branded graphics. "
        "Defines online academy SEO using Google's SEO Starter Guide; explains crawling, indexing and serving (Google Search Central); "
        "the educator keyword formula (subject + exam + language + format + need, e.g. 'ssc cgl quant course in hindi'); search intent table (learn, compare, buy, local, branded); "
        "a flat site structure (home, exam hubs, course and guide pages within three clicks); an 8-part course page (URL, H1, title tag under ~60 characters, meta description, demo lesson, text syllabus, reviews, FAQ); "
        "technical basics (own domain with HTTPS, mobile speed, sitemap in Google Search Console, no thin pages, alt text); topic clusters (pillar + supporting posts linked to the course); "
        "local SEO with Google Business Profile for coaching centres; earning links and mentions without buying them; getting cited in Google AI Overviews and ChatGPT (answer-first, specific facts, named teacher, FAQ schema, brand mentions); "
        "measuring impressions, clicks, CTR and average position in Search Console; free tools (Search Console, Google Trends, Keyword Planner, Business Profile, YouTube search, PageSpeed Insights); common mistakes; and a 90-day plan (foundation, content, authority). "
        "Cited facts: 96.55% of pages get no Google organic traffic (Ahrefs, Dec 2023); the first organic result averages 27.6% CTR, about 10x the tenth (Backlinko, updated Apr 2025); "
        "first-party: the AllCoaching blog grew from 183 clicks in July 2026 to 1,094 in September 2026 in Search Console. "
        "AllCoaching works like Shopify for coaching: sign up, choose a plan, upload a course, connect your domain, start selling; own domain, own Android and iOS app, Google Tag Manager and Meta Pixel on every plan; 7-day free trial with no card, then plans from ₹6,999/year excl. GST. By Amit Ratan.")


def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# A. sitemap: first post in the blog section
sm = open('sitemap.xml', encoding='utf-8').read()
if url + '</loc>' not in sm:
    anchor = '  <url>\n    <loc>https://allcoaching.in/blog/free-government-coaching-impact-on-private-educators</loc>'
    assert sm.count(anchor) == 1
    block = ("  <url>\n"
             f"    <loc>{url}</loc>\n"
             f"    <lastmod>{date}T09:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.95</priority>\n"
             f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"{url}\" />\n"
             f"    <image:image>\n      <image:loc>{img}</image:loc>\n      <image:title>{esc_xml(head)}</image:title>\n    </image:image>\n  </url>\n")
    open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, block + anchor, 1))

# B. llms.txt: top of the English blog list
lt = open('llms.txt', encoding='utf-8').read()
if f"]({url})" not in lt:
    lanchor = '- [Will Free Government Coaching Hurt My Coaching Institute? (2026)]'
    assert lt.count(lanchor) == 1
    open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms + "\n" + lanchor, 1))

# C. blog/index.html
h = open('blog/index.html', encoding='utf-8').read()
if f'/blog/{slug}" class="blog-card"' not in h:
    bp_anchor = '"blogPost":[\n'
    assert h.count(bp_anchor) == 1
    h = h.replace(bp_anchor, bp_anchor + f'      {{"@type":"BlogPosting","headline":{json.dumps(head)},"url":"{url}","datePublished":"{date}"}},\n', 1)
    idx = h.find('"@type":"ItemList"')
    m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
    arr = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1)) + 1}', m.group(2))
    new = f'\n      {{"@type":"ListItem","position":1,"url":"{url}","name":{json.dumps(card)}}},'
    h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + new + arr + m.group(3), 1)
    n = int(re.search(r'"numberOfItems":(\d+),', h).group(1))
    h = h.replace(f'"numberOfItems":{n},', f'"numberOfItems":{n + 1},', 1)
    canchor = '    <!-- Free Government Coaching impact (Aug 15) -->'
    assert h.count(canchor) == 1
    cardhtml = ('    <!-- Online Academy SEO guide (Oct 24) -->\n'
                f'    <a href="/blog/{slug}" class="blog-card" aria-label="Read: {card}">\n'
                '      <div class="blog-card-img">\n'
                f'        <img src="/assets/blog/{slug}/cover.webp" alt="{alt}" width="1600" height="900" decoding="async" loading="lazy" />\n'
                '      </div>\n      <div class="blog-card-body">\n'
                f'        <span class="blog-card-tag">{tag}</span>\n        <h3>{card}</h3>\n        <p>{dek}</p>\n'
                '        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span><span>22 min read</span>\n        </div>\n'
                '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n\n')
    h = h.replace(canchor, cardhtml + canchor, 1)
    open('blog/index.html', 'w', encoding='utf-8').write(h)

# verify
h = open('blog/index.html', encoding='utf-8').read()
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]', h, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S):
    json.loads(x)
print("sitemap:", url in open('sitemap.xml', encoding='utf-8').read())
print("llms:", url in open('llms.txt', encoding='utf-8').read())
print("ItemList sequential:", pos == list(range(1, len(pos) + 1)), "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("card:", f'/blog/{slug}" class="blog-card"' in h, "| index JSON-LD valid")
