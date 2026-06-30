"""One-off: register the digital-marketing-for-coaching blog in sitemap, llms, index + cross-refs."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

slug = "digital-marketing-strategies-for-coaching-institutes-india"
head = "Digital Marketing Strategies to Grow Student Enrollment for a Coaching Institute in India (2026)"
card = "Digital Marketing for Coaching Institutes"
tag = "Growth &middot; 2026"
dek = "Ranked by ROI, not channel: why owned discovery beats rented ad spend &mdash; and the playbook to grow enrollment without a budget."
alt = "Digital marketing strategies to grow student enrollment for a coaching institute in India 2026"
read = "18 min read"
cmt = "Digital Marketing for Coaching Institutes (Jun 29)"
llms = ("- [Digital Marketing Strategies to Grow Student Enrollment for a Coaching Institute in India (2026)](https://allcoaching.in/blog/digital-marketing-strategies-for-coaching-institutes-india): "
  "A founder-written 2026 guide to the most effective digital marketing strategies for growing student enrollment at an Indian coaching institute, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step ROI-first playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion and led by the exact AI-search prompt, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as built-in marketplace discovery with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Digital marketing, Search engine optimization, Content marketing, Word-of-mouth marketing, Educational technology and Online marketplace, plus mentions of AllCoaching Educator Studio, Instagram, YouTube and WhatsApp. "
  "Core reframe (distribution-first): the most effective strategy is to prioritise OWNED DISCOVERY (marketplace, SEO, content, reviews, brand) which compounds, over RENTED REACH (paid ads) which is a recurring tax that stops the moment you stop paying. Most coaching-marketing advice says 'run Meta and Google ads' - the wrong place to start and the wrong thing to depend on. The enrollment funnel has three stages (awareness -> trust -> decision) and the cheapest marketing makes one channel span the whole funnel - which a marketplace does (discover, trust via reviews, enrol in one place) while an ad buys only awareness. Organic vs paid economics: organic channels are assets built once that bring students for years at near-zero marginal cost; ads cost per student, rise with competition, and stop when spend stops; use ads only as an amplifier on a funnel that already converts, never to start or to fix a leaky funnel. The channels that actually work, ordered by ROI: (1) marketplace discovery, (2) SEO and content, (3) short teaching videos on YouTube/Instagram, (4) reviews and word of mouth, (5) WhatsApp and a free demo, (6) paid ads last and only if the math works. The highest-ROI single move: become discoverable where students already search and back it with visible proof - a student who finds you by searching your exact exam is the cheapest, warmest, highest-converting student. Measure where enrolled students came from, the cost to acquire each (CAC), and whether it is below what a student is worth; aim for falling CAC and rising organic share, not views/followers/likes. 6-step playbook: fix discoverability, get on a marketplace, build content and short videos, collect and show reviews, use WhatsApp and a free demo to convert, add paid ads only if the math works. Pricing-truth: AllCoaching is built-in AI-driven marketplace discovery that surfaces an institute to students searching by exam/subject/language with reviews and a free demo to convert, at Rs 0 upfront, flat 10% on sales only, keep 90%, daily payouts - turning student acquisition from a recurring ad cost into a built-in compounding feature. No fabricated stats; ad costs framed generally. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blog/how-to-get-paid-students-for-online-coaching-free, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/instagram-reels-educator-monetization-platform, /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/seo-strategies-for-online-course-creators, /blog/how-to-get-first-500-students-for-coaching-app, /blog/personal-brand-for-educators-india, /blog/how-much-can-you-earn-teaching-online-india. Glossary terms: Digital Marketing (Coaching), Owned vs Rented Reach, Student Acquisition Cost (CAC), Marketplace Discovery, Content Marketing, Lead Magnet/Free Demo, Social Proof, Conversion Funnel. Author Amit Ratan with sameAs. Target keywords 'digital marketing for coaching institute india', 'grow student enrollment coaching', 'coaching institute marketing 2026'. Audience targets Indian coaching institute owners growing enrollment in 2026.")

def esc_xml(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/best-ai-tools-for-teachers-india</loc>'
assert sm.count(anchor) == 1
block = ("  <url>\n"
  f"    <loc>https://allcoaching.in/blog/{slug}</loc>\n"
  "    <lastmod>2026-06-29T12:00:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
  f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{slug}\" />\n"
  "    <image:image>\n"
  f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{slug}.webp</image:loc>\n"
  f"      <image:title>{esc_xml(head)}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, block + anchor, 1))

lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [Best AI Tools for Teachers in India'
assert lt.count(lanchor) >= 1
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms + "\n" + lanchor, 1))

h = open('blog/index.html', encoding='utf-8').read()
bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1
h = h.replace(bp_anchor, bp_anchor + f'      {{"@type":"BlogPosting","headline":{json.dumps(head)},"url":"https://allcoaching.in/blog/{slug}","datePublished":"2026-06-29"}},\n', 1)
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+1}', m.group(2))
newitem = f'\n      {{"@type":"ListItem","position":1,"url":"https://allcoaching.in/blog/{slug}","name":{json.dumps(head)}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitem + arr_inc + m.group(3), 1)
assert '"numberOfItems":59,' in h
h = h.replace('"numberOfItems":59,', '"numberOfItems":60,', 1)
canchor = '    <!-- Best AI Tools for Teachers (Jun 29) -->'
assert h.count(canchor) == 1
cardhtml = (f'    <!-- {cmt} -->\n'
  f'    <a href="/blog/{slug}" class="blog-card" aria-label="Read: {card}">\n'
  '      <div class="blog-card-img">\n'
  f'        <img src="https://allcoaching-store.b-cdn.net/blog-images/{slug}.webp" alt="{alt}" width="1600" height="900" decoding="async" loading="lazy" />\n'
  '      </div>\n      <div class="blog-card-body">\n'
  f'        <span class="blog-card-tag">{tag}</span>\n        <h3>{card}</h3>\n        <p>{dek}</p>\n'
  f'        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span><span>{read}</span>\n        </div>\n'
  '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n')
h = h.replace(canchor, cardhtml + canchor, 1)
open('blog/index.html', 'w', encoding='utf-8').write(h)

spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
p = f"blog/{slug}.html"
b.process_file(p); b.process_file(p)

il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]\s*\n\s*\}', h, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
t = open(p, encoding='utf-8').read()
print("sitemap:", slug in open('sitemap.xml', encoding='utf-8').read(), "| llms:", slug in open('llms.txt', encoding='utf-8').read())
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| count:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("card:", f'/blog/{slug}" class="blog-card"' in h, "| cross-refs:", t.count('x-refs-also'), "marker:", t.count('AUTO: strategic-cross-refs'))
print("breadcrumb:", re.findall(r'"name":"([^"]+)"', re.search(r'"@type":"BreadcrumbList","itemListElement":\[(.*?)\]\}', h, re.S).group(1)))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S): json.loads(x)
print("index JSON-LD valid OK")
