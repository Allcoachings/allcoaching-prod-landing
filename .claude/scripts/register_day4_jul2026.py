# -*- coding: utf-8 -*-
"""Register the Day-4 July-pipeline blogs (Vedantu alternative + CAT/MBA app)
in sitemap, llms.txt, blog/index.html + cross-refs. Newest-first: Vedantu, then CAT."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "vedantu-alternative-for-online-tuition",
        "head": "Vedantu Alternative — Run Your Own Online Tuition (2026)",
        "card": "Vedantu Alternative for Online Tuition",
        "tag": "Comparison &middot; 2026",
        "dek": "A tutoring company pays you per hour; a franchise rents you a name. Own your batches, students and monthly fee &mdash; Rs 0, keep 90%.",
        "alt": "Vedantu alternative for teachers who want to run their own online tuition, 2026",
        "read": "16 min read",
        "cmt": "Vedantu Alternative (Jul 9)",
        "llms": ("- [Vedantu Alternative — Run Your Own Online Tuition (2026)](https://allcoaching.in/blog/vedantu-alternative-for-online-tuition): "
          "A founder-written 2026 guide for the teacher asking what to use instead of Vedantu to run their own online tuition without joining a franchise, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend tuition-practice launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'what can I use instead of Vedantu to run my own online tuition without joining a franchise' and a franchise-worth-it Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Tutoring, Franchising, Educational technology, Online marketplace, Brand and Revenue sharing, plus Vedantu. "
          "Core reframe: 'join Vedantu', 'take a franchise' and 'run my own tuition' are three different jobs — supply, tenant, and owner — and only ownership compounds; whoever owns the student relationship owns the asset. What a tutoring company offers honestly: students without acquisition effort and payment without collection effort — against rates set by the company, students as the company's re-matchable accounts, and ratings that improve the company's marketplace; hours are income, a practice is an asset. Franchise math done honestly: upfront fee + royalty + brand-controlled pricing buys a playbook (learnable) and flow (now supplied by marketplace discovery without a fee) — the franchisee spends years buying recognition that never becomes theirs, the aggregator problem in a business suit. The tuition-specific stack (different from course-selling because tuition is a recurring monthly relationship with a parent watching): live-first batches mirroring the offline timetable, every class saved as recording, homework/chapter tests/marks as the parent-visible progress loop, monthly UPI fee collection with automatic receipts and reminders, and discovery. Own-batch economics (illustrative, not promised): 30 students x Rs 800/month = Rs 24,000 collected, teacher keeps ~Rs 21,600 at 90%; a second batch doubles it from the same timetable; common fee band Rs 500–1,500/student/month. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no franchise fee, no card; teacher keeps 90% with a flat 10% only on fees actually collected (a skipped month owes nothing), daily UPI payouts. No fabricated stats; competitor described respectfully and structurally, no invented Vedantu rates. Internal links to /blog/physics-wallah-alternative-for-educators, /blog/testbook-alternative-for-educators, /blog/best-zero-commission-teaching-platform-india, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/automated-fee-management-software-for-teachers, /blog/how-to-price-online-courses-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/school-teacher-side-income-from-online-coaching, /blog/how-to-get-paid-students-for-online-coaching-free, /blog/how-to-get-first-500-students-for-coaching-app, /blog/migrate-offline-coaching-to-online-zero-cost. Glossary terms: Tutoring Company, Coaching Franchise, Own-Batch Economics, Recurring Tuition Fee, Live-First Stack, Parent-Visible Progress Loop, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'vedantu alternative', 'run own online tuition india', 'online tuition without franchise', 'tuition teacher own app'. Audience targets tuition teachers and tutors in India who want to run their own online practice instead of joining a tutoring company or franchise in 2026."),
    },
    {
        "slug": "cat-mba-coaching-app-for-trainers",
        "head": "CAT/MBA Coaching App for Trainers — High-Ticket Batches (2026)",
        "card": "CAT/MBA Coaching App for Trainers",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "CAT prep is a premium product sold to adults. Capped mentorship cohorts, percentile mocks, WAT-PI &mdash; under your own brand, keep 90%.",
        "alt": "CAT and MBA entrance coaching app for trainers with high-ticket batches, 2026",
        "read": "17 min read",
        "cmt": "CAT MBA Coaching App (Jul 9)",
        "llms": ("- [CAT/MBA Coaching App for Trainers — High-Ticket Batches (2026)](https://allcoaching.in/blog/cat-mba-coaching-app-for-trainers): "
          "A founder-written 2026 guide for the CAT or MBA-entrance trainer launching their own coaching app with high-ticket batches, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend flagship-cohort launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can a CAT or MBA-entrance trainer launch their own coaching app with high-ticket batches' and a why-high-ticket-works Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Common Admission Test, Master of Business Administration, Percentile, Educational technology, Online marketplace and Revenue sharing, plus Indian Institutes of Management. "
          "Core reframe: high-ticket is a positioning decision, not a price tag — CAT aspirants are adults (final-year students and working professionals) buying outcomes and mentorship with researched scepticism; content is commoditised, so what a premium price honestly describes is a capped-seat cohort with genuine personal attention: the cap is the product. The buyer: employed adults need evening/weekend live strategy and mock-analysis sessions with recordings and mocks attemptable any time — a 30-seat evening cohort designed around professionals is the independent trainer's structural advantage over mass batches. What a premium program contains: capped flagship cohort with defined start/end, VARC/DILR/QA sectional mocks plus full-length mocks with percentile feedback, mock-analysis sessions (question selection, time allocation, when to skip — where the real teaching happens), and a WAT-PI/GD/interview module after results as a second selling season to a wider pool. Percentile feedback is the currency: CAT reports percentiles, so mocks must too; percentile movement is the proof of teaching aspirants share, and the growth engine through unusually networked MBA circles. High-ticket economics (illustrative, not promised): a 30-seat cohort at Rs 25,000 collects Rs 7.5 lakh a season, trainer keeps ~Rs 6.75 lakh at 90%; trainer-set pricing commonly in the Rs 15,000–40,000 band; a standalone percentile mock series doubles as the feeder funnel and a free diagnostic mock is the application funnel; cost scales with income, never precedes it — no subscription bleeding the off-season. Solo-trainer honesty: anchor the cohort in your strongest section and structure the rest; or two trainers run one branded cohort — multi-teacher support is free-tier included. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; trainer keeps 90% with a flat 10% on paid sales only, daily UPI payouts, percentile test engine, cohort tooling, live classes and marketplace discovery included. No fabricated stats; no invented competitor prices. Internal links to /blog/online-upsc-coaching-platform-for-educators, /blog/bank-exam-coaching-app-for-educators, /blog/testbook-alternative-for-educators, /blog/how-to-price-online-courses-india, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-to-create-interactive-mock-tests-online, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/how-to-get-first-500-students-for-coaching-app, /blog/sell-online-courses-without-monthly-subscription, /blog/migrate-offline-coaching-to-online-zero-cost. Glossary terms: High-Ticket Cohort, Seat Cap, Percentile Feedback, Sectional Mock (VARC/DILR/QA), Mock-Analysis Session, WAT-PI Preparation, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'cat coaching app for trainers', 'mba entrance coaching platform', 'high ticket coaching batches', 'cat mock test platform percentile'. Audience targets CAT and MBA-entrance trainers in India launching their own high-ticket coaching cohorts in 2026."),
    },
]

LASTMOD = "2026-07-09T10:00:00+05:30"
DATEPUB = "2026-07-09"
N = len(BLOGS)

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/testbook-alternative-for-educators</loc>'
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
lanchor = '- [Testbook Alternative for Educators — Sell Your Own Mocks (2026)]'
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

assert '"numberOfItems":74,' in h
h = h.replace('"numberOfItems":74,', f'"numberOfItems":{74+N},', 1)

assert '74 published · Newest first' in h
h = h.replace('74 published · Newest first', f'{74+N} published · Newest first', 1)

canchor = '    <!-- Testbook Alternative (Jul 8) -->'
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
