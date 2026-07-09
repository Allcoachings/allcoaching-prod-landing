# -*- coding: utf-8 -*-
"""Register the Day-6 July-pipeline blogs (Teachable/Thinkific alternative + CLAT app)
in sitemap, llms.txt, blog/index.html + cross-refs. Newest-first: Teachable/Thinkific, then CLAT."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "teachable-thinkific-alternative-india",
        "head": "Indian Teachable/Thinkific Alternative — UPI Payouts (2026)",
        "card": "Teachable &amp; Thinkific Alternative in India",
        "tag": "Comparison &middot; 2026",
        "dek": "Your students pay by UPI; your month runs on cash-flow. The rails argument for an India-first platform &mdash; daily INR payouts, keep 90%.",
        "alt": "Indian alternative to Teachable and Thinkific with UPI and daily INR payouts, 2026",
        "read": "16 min read",
        "cmt": "Teachable Thinkific Alternative (Jul 11)",
        "llms": ("- [Indian Teachable/Thinkific Alternative — UPI Payouts (2026)](https://allcoaching.in/blog/teachable-thinkific-alternative-india): "
          "A founder-written 2026 guide for the Indian educator asking whether there is an Indian alternative to Teachable and Thinkific that supports UPI and daily INR payouts, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step parallel-run migration off a USD-subscription platform, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'is there an Indian alternative to Teachable and Thinkific that supports UPI and daily INR payouts' and an international-students dual-track Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Unified Payments Interface, Software as a service, Subscription business model, Educational technology, Online marketplace and Revenue sharing, plus Teachable, Thinkific and NPCI. "
          "Core reframe: a course platform is payment infrastructure first and a website builder second, and payment infrastructure has a geography — rails built for Western card-first buyers tax an Indian educator at both ends (buyers who cannot finish a card-first checkout, and payouts that arrive on someone else's calendar); differentiated from the sibling Kajabi-alternative post (cost/discovery angle) by centring entirely on rails and settlement mechanics. What Teachable/Thinkific honestly are: excellent US-built course SaaS on an own-traffic model — USD subscription tiers, card-first checkout, zero audience of their own. The three-layer rails mismatch: (1) UPI-first students and parents lost silently at card-first checkouts — checkout completion is the whole game at accessible price points; (2) INR price psychology — Rs 199/499/999 points profitable from the first sale under a flat 10% but strained under a fixed USD subscription; (3) settlement speed as cash-flow — daily INR settlement makes yesterday's enrolments usable today, versus queues and currency conversion. The distribution gap no subscription fixes: own-traffic platforms bring no students; marketplace discovery adds the second engine. Honest dual-track advice for educators with genuine international card-paying buyers: keep the global platform for that track, run the Rs 0 India-first studio for the Indian majority, let the numbers decide. Parallel-run migration: mirror catalogue, INR/UPI pricing, both platforms for one cycle, repoint links, let the USD subscription lapse at renewal. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, UPI-first checkout, marketplace discovery. No fabricated stats; competitors described respectfully and structurally, no invented Teachable/Thinkific prices or payout delays. Internal links to /blog/kajabi-alternative-india-for-educators, /blog/udemy-alternative-for-indian-instructors, /blog/spayee-learnyst-alternative-india, /blog/best-upi-payment-gateway-for-online-courses, /blog/sell-online-courses-without-monthly-subscription, /blog/best-zero-commission-teaching-platform-india, /blog/how-to-price-online-courses-india, /blog/automated-fee-management-software-for-teachers, /blog/how-to-get-first-500-students-for-coaching-app, /blog/migrate-offline-coaching-to-online-zero-cost. Glossary terms: Course SaaS, Own-Traffic Model, Payment Rails, UPI-First Checkout, Settlement Cycle, INR Price Psychology, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'indian alternative to teachable', 'thinkific alternative india', 'course platform with upi', 'daily inr payouts course platform'. Audience targets Indian educators selling courses to Indian students who need UPI checkout and daily INR payouts in 2026."),
    },
    {
        "slug": "clat-coaching-app-for-law-educators",
        "head": "CLAT Coaching App for Law Educators — Own Brand (2026)",
        "card": "CLAT Coaching App for Law Educators",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "CLAT is a passage-based exam and legal reasoning is a trainable skill. Passage-faithful mocks + discussion-led lives, your name. Keep 90%.",
        "alt": "CLAT coaching app for law educators to run legal-reasoning tests and live classes, 2026",
        "read": "16 min read",
        "cmt": "CLAT Coaching App (Jul 11)",
        "llms": ("- [CLAT Coaching App for Law Educators — Own Brand (2026)](https://allcoaching.in/blog/clat-coaching-app-for-law-educators): "
          "A founder-written 2026 guide for the CLAT or law-entrance coach asking which app is best to run legal-reasoning tests and live classes, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend law-practice launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'which app is best for a CLAT or law-entrance coach to run legal-reasoning tests and live classes' and a what-makes-CLAT-different Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Common Law Admission Test, Legal education, Test (assessment), Educational technology, Online marketplace and Revenue sharing, plus the Consortium of National Law Universities. "
          "Core reframe: modern CLAT is a passage-based reading exam — every section delivers questions through passages — and legal reasoning tests no prior law (a novel principle applied to engineered facts), so the coach sells two scarce things: a passage bank written by someone who understands how the traps are built, and a live room where wrong answers are defended until they break; a two-half product (test engine + discussion classroom) distinct from bank-exam speed/cut-off mechanics and UPSC evaluation economics. The buyer: class 11–12 students and droppers aiming at NLUs through the CLAT consortium (AILET and other entrances sharing the prep); parent pays and evaluates, so parent-visible seriousness (schedule, ranks, receipts) matters; a boutique pool where passage quality is discoverable fact and craft is distribution. The test half, five layers: passage-based sectional drills across English, legal reasoning, logical reasoning, GK/current affairs and quant; full-length mocks with negative marking and all-India ranks; explanations that argue the answer; a monthly legal GK and current-affairs compendium (the fastest-dating section, the between-mocks hook); and progress analytics. The live half: discussion-led classes — passage walkthroughs, answer defence, mock post-mortems — evening schedule with recordings; retention through belonging. Solo-coach honesty: anchor lives in your strong section, structure quant via drills/recordings or a colleague (multi-teacher free-tier included). Boutique economics (illustrative, not promised): 50-seat live batch at Rs 1,499/month ~Rs 67,500 kept monthly at 90%; Rs 799 mock series x 250 ~Rs 1.8 lakh a season; GK compendium as accessible subscription; no fixed platform cost. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; coach keeps 90% with a flat 10% on paid sales only, daily UPI payouts, ranked test engine + live classes + discovery included. No fabricated stats; only widely-known CLAT facts (passage-based format, principle-application legal reasoning, NLU consortium admissions). Internal links to /blog/cat-mba-coaching-app-for-trainers, /blog/online-upsc-coaching-platform-for-educators, /blog/bank-exam-coaching-app-for-educators, /blog/vedantu-alternative-for-online-tuition, /blog/testbook-alternative-for-educators, /blog/how-to-create-interactive-mock-tests-online, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/reduce-student-dropout-online-coaching-india, /blog/how-to-price-online-courses-india, /blog/sell-online-courses-without-monthly-subscription, /blog/how-to-get-first-500-students-for-coaching-app, /blog/budget-home-studio-setup-for-online-teaching. Glossary terms: Passage-Based Paper, Principle-Fact Application, Legal-Reasoning Drill, Legal GK &amp; Current-Affairs Compendium, Discussion-Led Live Class, NLU Route, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'clat coaching app', 'law entrance coaching platform', 'legal reasoning test app', 'clat mock test platform'. Audience targets CLAT and law-entrance coaches in India running legal-reasoning tests and live classes under their own brand in 2026."),
    },
]

LASTMOD = "2026-07-11T10:00:00+05:30"
DATEPUB = "2026-07-11"
N = len(BLOGS)

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/adda247-alternative-for-educators</loc>'
assert sm.count(anchor) == 1, "sitemap anchor not unique"
sm_block = ""
for b in BLOGS:
    sm_block += ("  <url>\n"
        f"    <loc>https://allcoaching.in/blog/{b['slug']}</loc>\n"
        f"    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
        f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{b['slug']}\" />\n"
        "    <image:image>\n"
        f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{b['slug']}.webp</image:loc>\n"
        f"      <image:title>{esc_xml(b['head'])}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, sm_block + anchor, 1))

# ---------- 2) llms.txt ----------
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [Adda247 Alternative for Educators — Own Your Brand (2026)]'
assert lt.count(lanchor) >= 1, "llms anchor missing"
llms_block = "\n".join(b['llms'] for b in BLOGS) + "\n"
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms_block + lanchor, 1))

# ---------- 3) blog/index.html ----------
h = open('blog/index.html', encoding='utf-8').read()

bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1
bp_block = "".join(
    f'      {{"@type":"BlogPosting","headline":{json.dumps(b["head"])},"url":"https://allcoaching.in/blog/{b["slug"]}","datePublished":"{DATEPUB}"}},\n'
    for b in BLOGS)
h = h.replace(bp_anchor, bp_anchor + bp_block, 1)

idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+N}', m.group(2))
newitems = ""
for i, b in enumerate(BLOGS, start=1):
    newitems += f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{b["slug"]}","name":{json.dumps(b["head"])}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitems + arr_inc + m.group(3), 1)

assert '"numberOfItems":78,' in h
h = h.replace('"numberOfItems":78,', f'"numberOfItems":{78+N},', 1)

assert '78 published · Newest first' in h
h = h.replace('78 published · Newest first', f'{78+N} published · Newest first', 1)

canchor = '    <!-- Adda247 Alternative (Jul 10) -->'
assert h.count(canchor) == 1
cards = ""
for b in BLOGS:
    cards += (f'    <!-- {b["cmt"]} -->\n'
      f'    <a href="/blog/{b["slug"]}" class="blog-card" aria-label="Read: {b["card"]}">\n'
      '      <div class="blog-card-img">\n'
      f'        <img src="https://allcoaching-store.b-cdn.net/blog-images/{b["slug"]}.webp" alt="{b["alt"]}" width="1600" height="900" decoding="async" loading="lazy" />\n'
      '      </div>\n      <div class="blog-card-body">\n'
      f'        <span class="blog-card-tag">{b["tag"]}</span>\n        <h3>{b["card"]}</h3>\n        <p>{b["dek"]}</p>\n'
      '        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span>'
      f'<span>{b["read"]}</span>\n        </div>\n'
      '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n')
h = h.replace(canchor, cards + canchor, 1)

open('blog/index.html', 'w', encoding='utf-8').write(h)

# ---------- 4) cross-refs (idempotent; posts already carry the block) ----------
spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for b in BLOGS:
    p = f"blog/{b['slug']}.html"
    print(b['slug'], "->", mod.process_file(p))

# ---------- 5) verification ----------
sm2 = open('sitemap.xml', encoding='utf-8').read()
lt2 = open('llms.txt', encoding='utf-8').read()
h2 = open('blog/index.html', encoding='utf-8').read()
print("\n--- verification ---")
for b in BLOGS:
    print(b['slug'][:46],
          "| sitemap:", f"/{b['slug']}</loc>" in sm2,
          "| llms:", f"/blog/{b['slug']})" in lt2,
          "| card:", f'/blog/{b["slug"]}" class="blog-card"' in h2,
          "| xrefs:", open(f"blog/{b['slug']}.html", encoding='utf-8').read().count('id="strategic-cross-refs"'))
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]', h2, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| count:", len(pos),
      "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h2).group(1))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h2, re.S):
    json.loads(x)
print("index JSON-LD valid OK")
