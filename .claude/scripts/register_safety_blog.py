"""One-off: register the coaching-safety/sealing blog (Jun 28) in sitemap, llms, index + cross-refs."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

slug = "coaching-centre-library-safety-norms-avoid-sealing-india"
head = "Coaching Centre & Library Safety Norms in India: How to Avoid Sealing (2026)"
card = "Coaching Centre & Library Safety Norms"
tag = "Compliance &middot; 2026"
dek = "Why coaching centres and libraries are being sealed &mdash; comply fully, then make the business resilient."
alt = "Coaching centre and library safety norms in India 2026 — how to avoid sealing"
read = "18 min read"
cmt = "Coaching Centre & Library Safety Norms (Jun 28)"
llms = ("- [Coaching Centre & Library Safety Norms in India: How to Avoid Sealing (2026)](https://allcoaching.in/blog/coaching-centre-library-safety-norms-avoid-sealing-india): "
  "A founder-written 2026 plain-English guide for institute and study-library owners on why coaching centres and libraries are being sealed across India and how to stay both compliant and resilient, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step safety-first checklist, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as a resilience layer with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, a References section with real sources, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Fire safety, National Building Code of India, Building code, Education in India, Cram school and Occupational safety and health, plus mentions of AllCoaching Educator Studio, the Ministry of Education, fire safety NOC and study library. "
  "IMPORTANT framing: GENERAL INFORMATION, NOT legal or fire-safety advice; safety norms exist to protect LIVES and must be met IN FULL; a prominent disclaimer and repeated reminders are present; the article explicitly refuses to suggest any way around safety compliance and states clearly that going online is NOT a way to skip safety duties. Core reframe: the sealing wave is enforcement of long-ignored safety norms (triggered by fire tragedies, including a 2026 Lucknow fire that prompted a wide Uttar Pradesh crackdown sealing dozens of coaching centres and libraries across Mathura, Kanpur/Kakadeo, Varanasi, Meerut, Mirzapur, Deoria, with utility disconnection and prosecution), AND it exposes a separate business fragility: an institute wholly dependent on one physical premises can be sealed in a morning. Top violations that get a premises sealed: illegal basement classrooms (sanctioned only for parking), no valid fire NOC, missing/non-working fire equipment, blocked or single exits, over-capacity, no registration. Norms to meet (two layers): physical safety (fire NOC, working equipment, multiple clear exits, safe electrical loads, sanctioned occupancy, building bylaws / National Building Code) and the Ministry of Education coaching guidelines (registration within the prescribed time, at least about one square metre per student, no enrolment below 16 or before secondary completion, graduate tutors, fee transparency, wellbeing); several states including Delhi are moving toward dedicated coaching-regulation laws. Study libraries/reading rooms are equally exposed and have been sealed for the same basement and fire-NOC violations, and can be more dangerous (long hours, dense rows). 6-step safety-first checklist: never run classes in an unapproved basement, obtain a valid fire NOC and equipment, register and respect capacity, keep exits/wiring/building safe, follow the MoE guidelines, THEN de-risk with an online or hybrid model. The deeper lesson: even a compliant institute is a single point of failure; an online/hybrid layer (recorded + live classes, test series, owned student relationship) keeps learning and revenue going if a building is disrupted. Pricing-truth: AllCoaching provides that resilient owned online layer at Rs 0 upfront, flat 10%, keep 90%, daily payouts; it explicitly does NOT provide a fire NOC or legal compliance and does NOT reduce the duty to keep any physical premises safe. Internal links to /blog/new-coaching-center-rules-india-2026, /blog/indian-edtech-laws-and-regulations-for-teachers, /blog/migrate-offline-coaching-to-online-zero-cost, /blog/best-zero-commission-teaching-platform-india, /blog/how-much-can-you-earn-teaching-online-india. Glossary terms: Fire NOC, Building Bylaws, Basement Use Violation, Coaching Centre Registration, Occupancy/Capacity Norm, Sealing, Study Library/Reading Room, Hybrid Coaching Model. Author Amit Ratan with sameAs. Target keywords 'coaching centre fire safety norms india', 'coaching centre sealing rules', 'why coaching centres are being sealed'. Audience targets Indian coaching institute and study library owners. General information, not legal or fire-safety advice.")

def esc_xml(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# A. sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/will-ai-tutors-replace-coaching-teachers-india</loc>'
assert sm.count(anchor) == 1
block = ("  <url>\n"
  f"    <loc>https://allcoaching.in/blog/{slug}</loc>\n"
  "    <lastmod>2026-06-28T10:00:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
  f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{slug}\" />\n"
  "    <image:image>\n"
  f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{slug}.webp</image:loc>\n"
  f"      <image:title>{esc_xml(head)}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, block + anchor, 1))

# B. llms.txt
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [Will AI Tutors Replace Coaching Teachers in India?'
assert lt.count(lanchor) >= 1
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms + "\n" + lanchor, 1))

# C. blog/index.html
h = open('blog/index.html', encoding='utf-8').read()
# blogPost
bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1
h = h.replace(bp_anchor, bp_anchor + f'      {{"@type":"BlogPosting","headline":{json.dumps(head)},"url":"https://allcoaching.in/blog/{slug}","datePublished":"2026-06-28"}},\n', 1)
# ItemList increment +1, prepend pos1
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+1}', m.group(2))
newitem = f'\n      {{"@type":"ListItem","position":1,"url":"https://allcoaching.in/blog/{slug}","name":{json.dumps(head)}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitem + arr_inc + m.group(3), 1)
# count 54 -> 55
assert '"numberOfItems":54,' in h
h = h.replace('"numberOfItems":54,', '"numberOfItems":55,', 1)
# card
canchor = '    <!-- Will AI Tutors Replace Coaching Teachers (Jun 22) -->'
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

# D. cross-refs block on the new post only
spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
p = f"blog/{slug}.html"
b.process_file(p); b.process_file(p)

# verify
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]\s*\n\s*\}', h, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
t = open(p, encoding='utf-8').read()
print("sitemap:", slug in open('sitemap.xml', encoding='utf-8').read())
print("llms:", slug in open('llms.txt', encoding='utf-8').read())
print("index ItemList sequential:", pos == list(range(1, len(pos)+1)), "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("index card:", f'/blog/{slug}" class="blog-card"' in h)
print("cross-refs x-refs-also:", t.count('x-refs-also'), "marker:", t.count('AUTO: strategic-cross-refs'))
bc = re.search(r'"@type":"BreadcrumbList","itemListElement":\[(.*?)\]\}', h, re.S).group(1)
print("breadcrumb:", re.findall(r'"name":"([^"]+)"', bc))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S): json.loads(x)
print("index JSON-LD valid OK")
