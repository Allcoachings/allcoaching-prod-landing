import re, sys

SLUG = 'school-teacher-side-income-from-online-coaching'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'School Teacher Side Income From Online Coaching — How to Build a Second Income From the Skill You Already Have (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-03'

errors = []

# ---------- 1. blog/index.html ----------
idx_path = 'blog/index.html'
h = open(idx_path, encoding='utf-8').read()

# 1a. visible card after grid open
grid_anchor = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid_anchor) == 1, f'grid anchor {h.count(grid_anchor)}'
card = grid_anchor + '''
    <!-- School Teacher Side Income From Online Coaching (Jun 3) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: School Teacher Side Income From Online Coaching">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="School teacher side income from online coaching — 2026 guide for working teachers in India" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Side Income · 2026</span>
        <h3>School Teacher Side Income From Online Coaching</h3>
        <p>Build a real second income from the skill you already have — without quitting, coding, or a following. The honest ₹0-upfront playbook for working teachers.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>14 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid_anchor, card, 1)

# 1b. numberOfItems 28 -> 29
assert h.count('"numberOfItems":28') == 1, 'numberOfItems'
h = h.replace('"numberOfItems":28', '"numberOfItems":29')

# 1c. ItemList: increment positions in the ItemList script block, insert position 1
scripts = re.split(r'(<script type="application/ld\+json">)', h)
# rebuild while editing the ItemList block
out = []
i = 0
did_itemlist = False
while i < len(scripts):
    part = scripts[i]
    if part == '<script type="application/ld+json">' and i + 1 < len(scripts) and '"@type":"ItemList"' in scripts[i+1]:
        block = scripts[i+1]
        block = re.sub(r'"position":(\d+)', lambda m: '"position":' + str(int(m.group(1)) + 1), block)
        newitem = '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"' + URL + '","name":"' + HEADLINE + '"},'
        assert block.count('"itemListElement":[') == 1
        block = block.replace('"itemListElement":[', newitem, 1)
        out.append(part); out.append(block); did_itemlist = True; i += 2; continue
    out.append(part); i += 1
h = ''.join(out)
if not did_itemlist: errors.append('ItemList block not found')

# 1d. Blog.blogPost prepend
bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1, f'blogPost anchor {h.count(bp_anchor)}'
bp_new = bp_anchor + '      {"@type":"BlogPosting","headline":"' + HEADLINE + '","url":"' + URL + '","datePublished":"' + DATE + '"},\n'
h = h.replace(bp_anchor, bp_new, 1)

open(idx_path, 'w', encoding='utf-8', newline='').write(h)
# verify
cards = h.count('class="blog-card"')
items = h.count('"@type":"ListItem"')
print(f'index.html: cards={cards}, numberOfItems29={"numberOfItems\":29" in h}, ListItems(incl breadcrumb)={items}, new in blogPost={SLUG in h}')

# ---------- 2. sitemap.xml ----------
sm_path = 'sitemap.xml'
s = open(sm_path, encoding='utf-8').read()
sm_anchor = '  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(sm_anchor) == 1, f'sitemap anchor {s.count(sm_anchor)}'
sm_block = ('  <url>\n'
            f'    <loc>{URL}</loc>\n'
            f'    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n'
            '    <changefreq>monthly</changefreq>\n'
            '    <priority>0.85</priority>\n'
            f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
            '    <image:image>\n'
            f'      <image:loc>{IMG}</image:loc>\n'
            '      <image:title>School Teacher Side Income From Online Coaching — A 2026 Guide for Working Teachers in India</image:title>\n'
            '    </image:image>\n'
            '  </url>\n')
s = s.replace(sm_anchor, sm_block + sm_anchor, 1)
open(sm_path, 'w', encoding='utf-8', newline='').write(s)
import xml.dom.minidom as M
M.parseString(s)
print('sitemap.xml: added + well-formed; slug present:', SLUG in s)

# ---------- 3. llms.txt ----------
lt_path = 'llms.txt'
t = open(lt_path, encoding='utf-8').read()
lt_anchor = '## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(lt_anchor) == 1, 'llms anchor'
entry = ('- [School Teacher Side Income From Online Coaching (2026 Guide)](' + URL + '): A founder-written, honest guide for working Indian school teachers on building a real side income from online coaching in 2026 — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step time-light playbook, FAQPage with 11 Q/A, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a side-income platform with Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Online tutoring, Supplemental income, Teacher, Passive income, and UPI. Core reframe — the question is not "can a teacher earn extra?" but "why is teaching, the skill perfected over years, the only asset never paid for beyond a fixed salary?" A salary rents the skill to one employer; an owned coaching income lets the same skill earn from many students. Thesis — online coaching is the lowest-friction side income a teacher can start because the asset (subject mastery, lesson plans, credibility) already exists; the only new skill is packaging and distribution. Honest financial framing (ranges, not promises): a weekend batch of 30 students at Rs 800/month is about Rs 24,000/month (educator keeps 90%); a recorded course priced Rs 999-4,999 sells repeatedly and decouples income from time. Myths cleared — no need to quit, code, buy equipment, or have a following; Rs 0 upfront, evenings/weekends model. The 6-step playbook — pick one subject you already teach, launch a free branded studio (60s), package one evening/weekend offering, price it and enable UPI, bring first students from your wider circle plus marketplace discovery, then let a recorded course compound. Time-light models compared (recorded mini-course = near-passive; weekly live batch = recurring; test series; notes). A dedicated ethics/compliance section — check your employment terms (some government-school service rules restrict private tuition), do not coach your own school\'s current students for private fees, keep the side brand separate. Discovery without a following — AllCoaching\'s AI marketplace matches students searching for your subject to your studio organically, no ads, no audience needed. Internal links to /blog/how-to-start-online-academy-in-5-steps, /blog/online-coaching-academy-without-coding, /blog/sell-online-courses-without-monthly-subscription, /blog/white-label-coaching-app-development-cost-india, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary — Side Income, Online Coaching, Branded Studio, Recorded Course, Test Series, Marketplace Discovery, Revenue Share Model, Passive Income. Author Amit Ratan with 6-entry sameAs. Target keyword "school teacher side income from online coaching" ~14,500/mo. Audience targets working school teachers in India seeking a side income from online coaching in 2026. Authored by founder Amit Ratan.\n')
t = t.replace(lt_anchor, lt_anchor + entry, 1)
open(lt_path, 'w', encoding='utf-8', newline='').write(t)
print('llms.txt: entry added; present:', SLUG in t)

if errors:
    print('ERRORS:', errors); sys.exit(1)
print('REGISTRATION OK')
