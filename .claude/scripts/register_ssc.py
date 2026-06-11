import re, sys

SLUG = 'how-to-teach-ssc-online-and-earn-money-india'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'How to Teach SSC Online and Earn Money in India — A Subject-Niche Playbook With SSC-Specific Marketing (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-04'

# ---------- blog/index.html ----------
idx = 'blog/index.html'
h = open(idx, encoding='utf-8').read()

grid_anchor = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid_anchor) == 1
card = grid_anchor + '''
    <!-- How to Teach SSC Online and Earn Money in India (Jun 4) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: How to Teach SSC Online and Earn Money in India">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="How to teach SSC online and earn money in India — 2026 subject-niche playbook" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Subject Niche · 2026</span>
        <h3>How to Teach SSC Online and Earn Money in India</h3>
        <p>SSC is huge but crowded. Niche down, build the test series aspirants pay for, market where they gather, and earn — the ₹0-upfront 2026 playbook.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>14 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid_anchor, card, 1)

assert h.count('"numberOfItems":29') == 1
h = h.replace('"numberOfItems":29', '"numberOfItems":30')

# ItemList: increment positions in the ItemList block, insert position 1
parts = re.split(r'(<script type="application/ld\+json">)', h)
out = []; i = 0; done = False
while i < len(parts):
    if parts[i] == '<script type="application/ld+json">' and i+1 < len(parts) and '"@type":"ItemList"' in parts[i+1]:
        blk = parts[i+1]
        blk = re.sub(r'"position":(\d+)', lambda m: '"position":'+str(int(m.group(1))+1), blk)
        assert blk.count('"itemListElement":[') == 1
        blk = blk.replace('"itemListElement":[', '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"'+URL+'","name":"'+HEADLINE+'"},', 1)
        out.append(parts[i]); out.append(blk); done = True; i += 2; continue
    out.append(parts[i]); i += 1
h = ''.join(out)
assert done

bp = '"blogPost":[\n'
assert h.count(bp) == 1
h = h.replace(bp, bp+'      {"@type":"BlogPosting","headline":"'+HEADLINE+'","url":"'+URL+'","datePublished":"'+DATE+'"},\n', 1)

# count texts 29 -> 30
for a,b in [('29 guides · By the founder','30 guides · By the founder'), ('29 published · Newest first','30 published · Newest first')]:
    assert h.count(a) == 1, a
    h = h.replace(a, b)

open(idx, 'w', encoding='utf-8', newline='').write(h)
print('index: cards=%d numberOfItems30=%s blogPost+=%s' % (h.count('class="blog-card"'), '"numberOfItems":30' in h, SLUG in h))

# ---------- sitemap.xml ----------
sm = 'sitemap.xml'; s = open(sm, encoding='utf-8').read()
a = '  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a) == 1
blk = ('  <url>\n'
       f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
       f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
       f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>How to Teach SSC Online and Earn Money in India — A 2026 Subject-Niche Playbook</image:title>\n    </image:image>\n  </url>\n')
s = s.replace(a, blk+a, 1)
open(sm, 'w', encoding='utf-8', newline='').write(s)
import xml.dom.minidom as M; M.parseString(s)
print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt = 'llms.txt'; t = open(lt, encoding='utf-8').read()
anc = '## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc) == 1
entry = ('- [How to Teach SSC Online and Earn Money in India (2026 Subject-Niche Playbook)](' + URL + '): A founder-written 2026 playbook for teaching SSC (Staff Selection Commission) exams online and earning in India — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step SSC playbook, FAQPage with 11 Q/A, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as an SSC platform with Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Staff Selection Commission, Online tutoring, Competitive examination, Test preparation, and SSC CGL. Core reframe — the question is not "can I teach SSC online?" but "in a crowded market of big brands, how do I get a specific aspirant to find me, trust me, and pay me?" SSC is one of the largest exam niches in India (CGL, CHSL, MTS, GD, Stenographer) with recurring exam cycles, but it is crowded at the center and wide open at the edges — so win an edge, not the center. Niche down three ways: by subject (CGL Quant, Reasoning, English, GA), by exam/tier (CGL/CHSL/MTS/GD, Tier-1 vs Tier-2), or by language/segment (Hindi-medium, droppers) — the sharpest niches combine slices ("SSC CGL Quant shortcuts for non-Maths backgrounds, in Hindi"). What SSC aspirants actually pay for, in order: a Previous-Year-Question (PYQ) based test series (the single biggest earner — speed, accuracy, ranks), concept clarity with shortcuts (Quant/Reasoning), recurring current-affairs/General-Awareness, and doubt-solving. The 6-step playbook — pick a sub-niche, launch a free branded studio (₹0), build concepts + PYQ test series, price for aspirants, acquire where they gather, scale with recurring test series each cycle. SSC-specific marketing: a free PYQ PDF or sectional test is the most effective lead magnet; aspirants gather on Telegram and YouTube (not general social); time pushes to notification/admit-card/result dates; a large Hindi-medium audience is underserved; honest results convert. Economics are a volume game — accessible pricing (batch ₹199-999, test series ₹149-799) beats premium; a ₹299 test series bought by 500 aspirants is about ₹1.5 lakh (educator keeps 90% on AllCoaching, daily payouts). Discovery is the whole game for a price-sensitive niche — a standalone site has no reach; AllCoaching\'s AI marketplace matches aspirants searching "SSC CGL Maths" or "CHSL test series" to the studio organically, no ad budget. Internal links to /blog/how-to-create-interactive-mock-tests-online, /blogs/en/how-to-sell-banking-exam-test-series-online-india, /blog/online-coaching-academy-without-coding, /blog/school-teacher-side-income-from-online-coaching, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india. Glossary — SSC, Test Series, Previous Year Questions (PYQ), General Awareness (GA), Branded Studio, Marketplace Discovery, Revenue Share Model, Lead Magnet. Author Amit Ratan with 6-entry sameAs. Target keyword "how to teach ssc online and earn money india" ~13,000/mo. Audience targets SSC subject experts and educators in India teaching SSC exams online to earn in 2026.\n')
t = t.replace(anc, anc+entry, 1)
open(lt, 'w', encoding='utf-8', newline='').write(t)
print('llms.txt: added:', SLUG in t)
print('REGISTRATION OK')
