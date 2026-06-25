"""One-off: register the 3 June-22 blogs in sitemap.xml, llms.txt, blog/index.html."""
import re, json, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

posts = [
 dict(slug="will-ai-tutors-replace-coaching-teachers-india",
   head="Will AI Tutors Replace Coaching Teachers in India? An Honest 2026 Answer",
   card="Will AI Tutors Replace Coaching Teachers?", tag="Strategy &middot; 2026",
   dek="AI replaces explanation, not the educator. What stays human &mdash; and how to own it.",
   alt="Will AI tutors replace coaching teachers in India 2026", read="18 min read",
   cmt="Will AI Tutors Replace Coaching Teachers (Jun 22)",
   llms=("- [Will AI Tutors Replace Coaching Teachers in India? An Honest 2026 Answer](https://allcoaching.in/blog/will-ai-tutors-replace-coaching-teachers-india): "
     "A founder-written 2026 answer to whether AI tutors will replace coaching teachers in India, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step AI-proof-your-teaching method, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as the AI-era educator platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Artificial intelligence in education, Intelligent tutoring system, Educational technology, Online tutoring, Large language model and Personalized learning, plus mentions of AllCoaching Educator Studio, ChatGPT, AI tutor and NEET. "
     "Core reframe: AI will NOT replace the educator, it will replace the COMMODITY OF EXPLANATION; teaching is two bundled jobs (information delivery, which AI now does with infinite patience, 24x7 availability, instant personalisation and near-zero marginal cost; and the human work around it, which AI cannot do). What AI cannot replace: accountability that makes a student show up and finish, motivation, judgement, trust, mentorship, community and a brand a student chooses. The educators at risk are pure interchangeable explainers with no relationship, brand or outcome; the ones who thrive use AI as leverage to serve more students and own the relationship. Key line: AI will not replace teachers, but teachers who use AI will replace teachers who do not. Students still pay when explanation is free because they pay for the PATH and the outcome (structured course, accountability, a trusted teacher), not the facts (which were nearly free even before AI). The brand-and-relationship moat is the one asset AI cannot copy, and it must be OWNED (not on a borrowed platform). 6-step AI-proof playbook: use AI to remove commodity work, double down on the human layer, build a brand students choose, own the student relationship, package outcomes not explanations, reach more students with the time AI frees. Pricing-truth: AllCoaching = Rs 0 upfront, free forever, flat 10% on sales only, educator keeps 90%, daily INR payouts, AI-driven marketplace discovery. No fabricated statistics; only quote is founder-attributed plus a common education adage. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/personal-brand-for-educators-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/using-chatgpt-for-course-curriculum-design, /blog/best-platform-for-selling-pdf-notes-and-test-series. Glossary terms: AI Tutor, Commodity of Explanation, Augmentation vs Replacement, Accountability Layer, Mentorship, Owned Student Relationship, Outcome Product, Educator Brand. Author Amit Ratan with sameAs. Target keywords will ai replace teachers india, ai tutor vs human teacher, ai in education india 2026. Audience targets Indian coaching teachers and educators in the AI era.")),
 dict(slug="future-of-edtech-india-after-byjus-independent-educator",
   head="After Byju's: Why India's Edtech Future Belongs to the Independent Educator (2026)",
   card="After Byju's: The Independent Educator", tag="Analysis &middot; 2026",
   dek="One model died &mdash; the burn-for-growth super app. The future is the independent educator.",
   alt="After Byju's — India's edtech future belongs to the independent educator 2026", read="18 min read",
   cmt="After Byju's: The Independent Educator (Jun 22)",
   llms=("- [After Byju's: Why India's Edtech Future Belongs to the Independent Educator (2026)](https://allcoaching.in/blog/future-of-edtech-india-after-byjus-independent-educator): "
     "A founder-written 2026 analysis of India's edtech reset after the collapse of Byju's, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step ride-the-shift method, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as picks-and-shovels infrastructure with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Educational technology, Byju's, Online tutoring, Venture capital, Creator economy and Unit economics, plus mentions of AllCoaching Educator Studio, Byju's, PhysicsWallah and Online marketplace. "
     "Core reframe: edtech is NOT dead, one model died, the venture-funded burn-for-growth super app, not online education itself (which is larger than ever). As widely reported, Byju's, once valued around 22 billion dollars at its peak, collapsed into insolvency after a write-down to a fraction of that; the structural cause was UNIT ECONOMICS, spending more to acquire and serve each student than the student paid, fatal once cheap capital ended. What survived and thrived: vertical, value-for-money, teacher-led education (PhysicsWallah cited as the example, fair prices, outcomes, a trusted teacher). The deepest shift is from a few giants to thousands of independent, owned-brand educators, because the giant's three advantages eroded or flipped: infrastructure (app/hosting/payments) is now a free commodity, distribution is available via marketplaces, and trust is inherently local and personal (the individual's home turf). The independent educator keeps most revenue, answers to no burn rate, is profitable from the first student, and needs a few hundred students not millions. The picks-and-shovels the educator needs (branded app, hosting, payments, owned student relationship, discovery) are now free where each once needed a giant's capital. 6-step playbook: pick a vertical you own, build value-for-money not burn-for-growth, claim an owned home and brand, use shared infrastructure do not build it, grow through marketplace discovery, keep unit economics positive from day one. Honest discipline: credits that giants normalised online learning and proved demand; the problem was the financing model not the idea; Byju's figures framed as widely reported, no fabricated numbers. Pricing-truth: AllCoaching = Rs 0 upfront, free forever, flat 10% on sales only, keep 90%, daily payouts, marketplace discovery. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blog/best-zero-commission-teaching-platform-india, /blog/how-to-start-online-academy-in-5-steps, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india, /blog/how-much-can-you-earn-teaching-online-india. Glossary terms: EdTech Super App, Burn-for-Growth, Unit Economics, Vertical EdTech, Independent Educator, Picks-and-Shovels, Owned Distribution, Creator-Led Education. Author Amit Ratan with sameAs. Target keywords future of edtech india after byjus, is edtech dead in india, independent educator india. Audience targets Indian educators and founders in 2026.")),
 dict(slug="new-coaching-center-rules-india-2026",
   head="New Coaching Rules in India: What Every Educator Must Know (2026)",
   card="New Coaching Rules in India (2026)", tag="Compliance &middot; 2026",
   dek="No guaranteed ranks, no under-16, real penalties for false ads &mdash; why the honest educator wins.",
   alt="New coaching rules in India 2026 — what every educator must know", read="18 min read",
   cmt="New Coaching Rules in India 2026 (Jun 22)",
   llms=("- [New Coaching Rules in India: What Every Educator Must Know (2026)](https://allcoaching.in/blog/new-coaching-center-rules-india-2026): "
     "A founder-written 2026 plain-English overview of India's new coaching regulations, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step compliance checklist, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as the transparent-educator platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, a References section with real .gov sources, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Consumer Protection Act 2019, Digital Personal Data Protection Act 2023, False advertising, Coaching/cram school, Education in India and Consumer protection, plus mentions of the Central Consumer Protection Authority (CCPA), the Ministry of Education and NEET. "
     "IMPORTANT framing: this is GENERAL INFORMATION, NOT legal advice; applicability varies by state and circumstance and the reader should CONSULT A QUALIFIED PROFESSIONAL; a prominent disclaimer box and repeated reminders are present. Core reframe: the new rules target DECEPTION, not teaching. Three developments: (1) Ministry of Education's Guidelines for Regulation of Coaching Centres 2024, including no enrolment of students below 16 or before completing secondary school, qualified tutors, fee transparency and refunds, implementation largely left to states; (2) the CCPA's Guidelines for Prevention of Misleading Advertisement in the Coaching Sector 2024, which bar guaranteed-rank, guaranteed-selection, guaranteed-marks/admission/job claims and false success-rate or faculty claims, enforceable under the Consumer Protection Act 2019 with penalties reported up to about Rs 50 lakh, applying broadly to anyone advertising coaching including individuals; (3) the DPDP Act 2023, requiring lawful purpose-limited data handling and verifiable parental consent for children's data. What you CAN say: real verifiable outcomes and genuine reviews, never guarantees. Dummy/shadow schools (enrolled on paper while attending coaching full time) are under crackdown. The rules hurt guaranteed-rank sellers, inflated-topper claimers, opaque-fee and under-16-dependent institutes and scraped-data marketers; they help educators with real outcomes, transparent pricing, verifiable reviews and respectful data practice. 6-step compliance checklist: remove guaranteed-rank/false success claims, be transparent on fees and refunds, mind the under-16 norm, handle student data responsibly with consent for minors, keep faculty and outcome claims truthful, consult a professional. Pricing-truth: AllCoaching makes the honest setup the default (transparent pricing, verifiable outcomes not guarantees, owned brand, responsible data) at Rs 0 upfront, flat 10%, keep 90%; explicitly does NOT make anyone automatically compliant and does not replace a professional. References cite PIB, Ministry of Education, MeitY and Consumer Affairs. Internal links to /blog/indian-edtech-laws-and-regulations-for-teachers, /blog/personal-brand-for-educators-india, /blog/best-zero-commission-teaching-platform-india. Glossary terms: Coaching Centre Guidelines 2024, CCPA, Misleading Advertisement, Guaranteed-Rank Claim, DPDP Act 2023, Verifiable Parental Consent, Fee Transparency, Dummy/Shadow School. Author Amit Ratan with sameAs. Target keywords new coaching rules india 2026, coaching centre guidelines 2024, ccpa misleading advertisement coaching. Audience targets Indian coaching educators and institute owners. General information, not legal advice.")),
]

def esc_xml(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---------- A. sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/how-much-can-you-earn-teaching-online-india</loc>'
assert sm.count(anchor) == 1
blocks = ""
for p in posts:
    blocks += ("  <url>\n"
      f"    <loc>https://allcoaching.in/blog/{p['slug']}</loc>\n"
      "    <lastmod>2026-06-22T10:30:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
      f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{p['slug']}\" />\n"
      "    <image:image>\n"
      f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{p['slug']}.webp</image:loc>\n"
      f"      <image:title>{esc_xml(p['head'])}</image:title>\n    </image:image>\n  </url>\n")
sm = sm.replace(anchor, blocks + anchor, 1)
open('sitemap.xml', 'w', encoding='utf-8').write(sm)

# ---------- B. llms.txt ----------
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [How Much Can You Earn Teaching Online in India?'
assert lt.count(lanchor) >= 1
entry = "\n".join(p['llms'] for p in posts) + "\n"
lt = lt.replace(lanchor, entry + lanchor, 1)
open('llms.txt', 'w', encoding='utf-8').write(lt)

# ---------- C. blog/index.html ----------
h = open('blog/index.html', encoding='utf-8').read()
# C1 blogPost[]
bp_anchor = '"blogPost":[\n'
bp = ""
for p in posts:
    bp += f'      {{"@type":"BlogPosting","headline":{json.dumps(p["head"])},"url":"https://allcoaching.in/blog/{p["slug"]}","datePublished":"2026-06-22"}},\n'
assert h.count(bp_anchor) == 1
h = h.replace(bp_anchor, bp_anchor + bp, 1)
# C2 ItemList — scope to ItemList block, increment positions +3, prepend 3
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+3}', m.group(2))
new_items = ""
for i, p in enumerate(posts, 1):
    new_items += f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{p["slug"]}","name":{json.dumps(p["head"])}}},'
newblock = m.group(1) + new_items + arr_inc + m.group(3)
h = h[:idx] + h[idx:].replace(m.group(0), newblock, 1)
# C3 count
assert '"numberOfItems":51,' in h
h = h.replace('"numberOfItems":51,', '"numberOfItems":54,', 1)
# C4 cards
canchor = '    <!-- How Much Can You Earn Teaching Online (Jun 22) -->'
assert h.count(canchor) == 1
cards = ""
for p in posts:
    cards += (f'    <!-- {p["cmt"]} -->\n'
      f'    <a href="/blog/{p["slug"]}" class="blog-card" aria-label="Read: {p["card"]}">\n'
      '      <div class="blog-card-img">\n'
      f'        <img src="https://allcoaching-store.b-cdn.net/blog-images/{p["slug"]}.webp" alt="{p["alt"]}" width="1600" height="900" decoding="async" loading="lazy" />\n'
      '      </div>\n      <div class="blog-card-body">\n'
      f'        <span class="blog-card-tag">{p["tag"]}</span>\n        <h3>{p["card"]}</h3>\n        <p>{p["dek"]}</p>\n'
      f'        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span><span>{p["read"]}</span>\n        </div>\n'
      '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n')
h = h.replace(canchor, cards + canchor, 1)
open('blog/index.html', 'w', encoding='utf-8').write(h)

# ---------- verify ----------
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]\s*\n\s*\}', h, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
print("sitemap new urls:", sum(1 for p in posts if p['slug'] in open('sitemap.xml', encoding='utf-8').read()))
print("llms new entries:", sum(1 for p in posts if p['slug'] in open('llms.txt', encoding='utf-8').read()))
print("index ItemList sequential 1..N:", pos == list(range(1, len(pos)+1)), "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("index cards added:", sum(1 for p in posts if f'/blog/{p["slug"]}" class="blog-card"' in h))
bc = re.search(r'"@type":"BreadcrumbList","itemListElement":\[(.*?)\]\}', h, re.S).group(1)
print("breadcrumb intact:", re.findall(r'"name":"([^"]+)"', bc))
for b in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S):
    json.loads(b)
print("index.html JSON-LD valid OK")
