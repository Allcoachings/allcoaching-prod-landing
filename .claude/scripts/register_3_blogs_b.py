"""One-off: register the 3 Jun-28 blogs (retention, CUET, pricing) in sitemap, llms, index + cross-refs."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

posts = [
 dict(slug="reduce-student-dropout-online-coaching-india",
   head="How to Reduce Student Drop-off in Online Coaching — A 2026 Retention Playbook",
   card="How to Reduce Student Drop-off", tag="Operations &middot; 2026",
   dek="Drop-off is an architecture failure, not willpower &mdash; where students quit, why, and the systems that keep them.",
   alt="How to reduce student drop-off in online coaching, AllCoaching 2026", read="18 min read",
   cmt="How to Reduce Student Drop-off (Jun 28)",
   llms=("- [How to Reduce Student Drop-off in Online Coaching — A 2026 Retention Playbook](https://allcoaching.in/blog/reduce-student-dropout-online-coaching-india): "
     "A founder-written 2026 retention playbook for Indian online educators, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step retention playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as a retention platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Student retention, Churn rate, Online tutoring, Educational technology, Onboarding and Learning analytics, plus mentions of AllCoaching Educator Studio, completion rate, customer retention and NEET. "
     "Core reframe: student drop-off is a failure of ARCHITECTURE (onboarding, early engagement, accountability), NOT a failure of student willpower; the same student quits a badly designed course and finishes a well-designed one. Economics: a retained student is income earned without fresh acquisition cost, so retention is the cheapest growth and far more profitable than constantly replacing leavers. Where students drop off: heaviest in week 1 (the cliff, before teaching takes hold), a second fade mid-course (novelty gone, hard part begins), a smaller give-up near the end. Why they leave (five structural causes, none laziness): no early win, no clear path, no accountability, isolation, invisible progress; online makes all worse because the student is alone and no one notices when they stop. Fix the first seven days (highest leverage): engineer an early quick win, show the path, make the student feel noticed. Three sustaining forces for the middle: accountability (deadlines, check-ins, being noticed), visible progress (scores, completion), community (cohort, belonging). Catch drop-off early via simple signals (missed logins, unfinished lessons, skipped tests, going quiet) and re-engage fast with a specific human nudge. 6-step playbook: early quick win, clear path with visible progress, accountability and human contact, detect at-risk early, re-engage fast, design for community. Pricing-truth: AllCoaching gives structured courses with visible progress, ranked test series and live classes for accountability, engagement visibility, owned student CRM for nudges, community, at Rs 0 upfront keeping 90%. No fabricated stats; drop-off pattern framed via first-person observation. Internal links to /blog/how-much-can-you-earn-teaching-online-india, /blog/how-to-get-paid-students-for-online-coaching-free, /blog/automate-student-onboarding-for-coaching-app, /blog/best-platform-for-selling-pdf-notes-and-test-series. Glossary terms: Student Drop-off, Retention Rate, Onboarding, Activation (Quick Win), Early-Warning Signal, Cohort, Completion Rate, Churn. Author Amit Ratan with sameAs. Target keywords 'how to reduce student dropout in online coaching', 'student retention coaching', 'course completion rate india'. Audience targets Indian online educators improving retention in 2026.")),
 dict(slug="online-cuet-coaching-platform-for-educators",
   head="Online CUET Coaching Platform for Educators — How to Choose, and Start, in 2026",
   card="Online CUET Coaching Platform", tag="Strategy &middot; 2026",
   dek="CUET is one exam with a hundred open niches. Why it suits online, and how to own a piece of it.",
   alt="Online CUET coaching platform for educators, AllCoaching 2026", read="18 min read",
   cmt="Online CUET Coaching Platform (Jun 28)",
   llms=("- [Online CUET Coaching Platform for Educators — How to Choose, and Start, in 2026](https://allcoaching.in/blog/online-cuet-coaching-platform-for-educators): "
     "A founder-written 2026 guide for educators on building an online CUET coaching platform, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step start method, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as a CUET coaching platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Common University Entrance Test, National Testing Agency, Educational entrance examination, Education in India, Online tutoring and Electronic assessment, plus mentions of AllCoaching Educator Studio, the National Testing Agency, CUET and University. "
     "Core reframe: CUET is not one crowded exam but a fragmented opportunity, effectively a hundred niches wearing one name, with far more demand than focused high-quality coaching; the question 'who is the best online educator for this domain subject in this language?' usually has no answer (the seat is empty). Scale: CUET-UG, conducted by the NTA for UG admission across 130-plus central, state, deemed and private universities, taken by lakhs of students for a very large number of seats; big enough to matter, broad enough to leave room. Format (as of 2026, verify with NTA): a computer-based test with Language, Domain-Specific Subject and General Test sections, offered in many languages; modular (students take only their sections) and CBT, which makes realistic on-screen timed mocks the single most valuable product. Why CUET suits online: computer-based (on-screen mock practice is exactly what online does best), pan-India aspirant base, multilingual (serve a language audience nationally), and mock-heavy and modular. What a CUET platform must have: CBT-format ranked mock series mirroring the exam, structured courses by section/subject, multilingual support, ranked tests, discovery, plus owned brand/students and fair payments. The niche gap: go narrow and deep (own one section/subject/language) and beat generalists; teaching in an under-served language is a top opening. 6-step start: pick a focused section/domain, build CBT mocks and courses, support relevant languages, launch an owned branded platform, get discovered on a marketplace, retain with mocks and accountability. Pricing-truth: AllCoaching = branded app, CBT mocks, multilingual, discovery, Rs 0 upfront, keep 90%. Exam specifics framed as indicative and to be verified with the NTA; no fabricated precise figures. Internal links to /blog/online-jee-coaching-platform-for-teachers, /blog/online-platform-for-ctet-coaching-teachers, /blog/how-to-create-interactive-mock-tests-online, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/best-app-for-state-psc-coaching-educators, /blog/personal-brand-for-educators-india, /blog/how-to-get-paid-students-for-online-coaching-free. Glossary terms: CUET, CUET Domain Subject, General Test (CUET), Computer-Based Test (CBT), National Testing Agency (NTA), Sectional Test Series, Multilingual Coaching, Participating University. Author Amit Ratan with sameAs. Target keywords 'online cuet coaching platform for educators', 'cuet coaching online', 'cuet test series platform'. Audience targets Indian educators building online CUET coaching in 2026.")),
 dict(slug="how-to-price-online-courses-india",
   head="How to Price Your Online Course in India — A 2026 Value-Based Pricing Guide",
   card="How to Price Your Online Course", tag="Economics &middot; 2026",
   dek="Price is positioning, not a number. Why underpricing costs you, and how to price on value instead.",
   alt="How to price your online course in India, AllCoaching 2026", read="18 min read",
   cmt="How to Price Your Online Course (Jun 28)",
   llms=("- [How to Price Your Online Course in India — A 2026 Value-Based Pricing Guide](https://allcoaching.in/blog/how-to-price-online-courses-india): "
     "A founder-written 2026 value-based pricing guide for Indian educators, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step pricing method, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as a set-your-own-price platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Pricing, Value-based pricing, Pricing strategies, Online tutoring, Consumer behaviour and Educational technology, plus mentions of AllCoaching Educator Studio, Anchoring, Willingness to pay and UPI. "
     "IMPORTANT honesty: every rupee figure is an ILLUSTRATIVE example, not a prescription; no fabricated statistics. Core reframe: the right question is not 'how much should I charge?' but 'what value am I charging for and how do I want to be positioned?' Price is positioning, the first signal a student reads about value, not just a number. The #1 mistake is UNDERPRICING (out of underconfidence or belief that cheaper means more students): it cuts income per student AND signals low quality, often attracting fewer, less committed students and repelling serious ones. Cost-plus vs value-based: cost-plus (cost + margin) systematically underprices because a course's outcome value (a rank, skill, career) far exceeds its production cost; value-based prices a fair share of the outcome's worth to the student. What sets the price: outcome value, audience willingness to pay, format (live vs recorded), brand and proof, and the alternatives. Anchoring and good-better-best tiers let students self-select and lift average revenue, with a high top tier anchoring the middle (target) tier. India-specific psychology: price is read as a quality signal (a too-low price can repel serious families), and the answer to price-sensitivity is INSTALLMENTS, not permanent discounts (hold a fair value-based price, make it accessible by paying in parts). 6-step method: define the outcome, understand willingness to pay, study alternatives, set value-based not cost-plus, build good-better-best tiers, test and raise over time. Raise prices as proof and reputation grow (per cohort, grandfather existing students, genuine deadlines). Pricing-truth: AllCoaching lets the educator set their own price and tiers, installment-friendly checkout, keep 90% (flat 10% on sales only), Rs 0 upfront, no subscription. Internal links to /blog/how-much-can-you-earn-teaching-online-india, /blog/personal-brand-for-educators-india, /blog/sell-online-courses-without-monthly-subscription, /blog/online-coaching-business-plan-2026, /blog/reduce-student-dropout-online-coaching-india. Glossary terms: Value-Based Pricing, Cost-Plus Pricing, Price Anchoring, Tiered Pricing, Willingness to Pay, Price-Quality Signal, Underpricing, Positioning. Author Amit Ratan with sameAs. Target keywords 'how to price online courses in india', 'value based pricing course', 'course pricing strategy'. Audience targets Indian educators and course creators pricing online courses in 2026. All figures illustrative.")),
]

def esc_xml(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# A. sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/coaching-centre-library-safety-norms-avoid-sealing-india</loc>'
assert sm.count(anchor) == 1
blocks = ""
for p in posts:
    blocks += ("  <url>\n"
      f"    <loc>https://allcoaching.in/blog/{p['slug']}</loc>\n"
      "    <lastmod>2026-06-28T11:00:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
      f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{p['slug']}\" />\n"
      "    <image:image>\n"
      f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{p['slug']}.webp</image:loc>\n"
      f"      <image:title>{esc_xml(p['head'])}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, blocks + anchor, 1))

# B. llms.txt
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [Coaching Centre & Library Safety Norms in India'
assert lt.count(lanchor) >= 1
entry = "\n".join(p['llms'] for p in posts) + "\n"
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, entry + lanchor, 1))

# C. blog/index.html
h = open('blog/index.html', encoding='utf-8').read()
bp_anchor = '"blogPost":[\n'
bp = "".join(f'      {{"@type":"BlogPosting","headline":{json.dumps(p["head"])},"url":"https://allcoaching.in/blog/{p["slug"]}","datePublished":"2026-06-28"}},\n' for p in posts)
assert h.count(bp_anchor) == 1
h = h.replace(bp_anchor, bp_anchor + bp, 1)
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+3}', m.group(2))
new_items = "".join(f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{p["slug"]}","name":{json.dumps(p["head"])}}},' for i, p in enumerate(posts, 1))
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + new_items + arr_inc + m.group(3), 1)
assert '"numberOfItems":55,' in h
h = h.replace('"numberOfItems":55,', '"numberOfItems":58,', 1)
canchor = '    <!-- Coaching Centre & Library Safety Norms (Jun 28) -->'
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

# D. cross-refs on the 3 new posts only
spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
for p in posts:
    pp = f"blog/{p['slug']}.html"
    b.process_file(pp); b.process_file(pp)

# verify
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]\s*\n\s*\}', h, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
print("sitemap new:", sum(1 for p in posts if p['slug'] in open('sitemap.xml', encoding='utf-8').read()))
print("llms new:", sum(1 for p in posts if p['slug'] in open('llms.txt', encoding='utf-8').read()))
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("cards:", sum(1 for p in posts if f'/blog/{p["slug"]}" class="blog-card"' in h))
for p in posts:
    t = open(f"blog/{p['slug']}.html", encoding='utf-8').read()
    print(" ", p['slug'][:38], "x-refs-also", t.count('x-refs-also'), "marker", t.count('AUTO: strategic-cross-refs'))
bc = re.search(r'"@type":"BreadcrumbList","itemListElement":\[(.*?)\]\}', h, re.S).group(1)
print("breadcrumb:", re.findall(r'"name":"([^"]+)"', bc))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S): json.loads(x)
print("index JSON-LD valid OK")
