# -*- coding: utf-8 -*-
"""Register the 4 July-pipeline blogs (Day 1: physics-wallah-alt + NEET; Day 2: winuall-alt + UPSC)
in sitemap, llms.txt, blog/index.html + cross-refs. Top-down order: PW, NEET, Winuall, UPSC."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "physics-wallah-alternative-for-educators",
        "head": "Physics Wallah Alternative for Teachers — Own App (2026)",
        "card": "Physics Wallah Alternative for Educators",
        "tag": "Comparison &middot; 2026",
        "dek": "A faculty seat pays a salary; your own app builds an asset. The proven trust-plus-affordability architecture, under your name &mdash; Rs 0, keep 90%.",
        "alt": "Physics Wallah alternative for educators who want their own branded app, 2026",
        "read": "17 min read",
        "cmt": "Physics Wallah Alternative (Jul 7)",
        "llms": ("- [Physics Wallah Alternative for Teachers — Own App (2026)](https://allcoaching.in/blog/physics-wallah-alternative-for-educators): "
          "A founder-written 2026 guide to the best Physics Wallah alternative for a teacher who wants their own branded app instead of a faculty seat inside someone else's brand, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step independent-teacher playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'what is the best alternative to Physics Wallah for a teacher who wants their own branded app' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for PhysicsWallah, Educational technology, Brand, Mobile app, Online marketplace and Network effect. "
          "Core reframe: PhysicsWallah is a coaching company you can join, NOT a platform a teacher can build a brand on - the searcher's real want is the thing PW's founder had: a teaching brand of their own; the honest alternative is ownership of the same architecture (teacher trust + accessible pricing + direct student reach) at the scale of one niche. What PW proved: students trust a teacher further than a corporation, and trust priced accessibly beats marketing budgets - a portable blueprint, not a moat. The two paths compared honestly: the faculty seat pays a predictable salary but builds no asset (students, reviews, reputation accrue to the company's app and the seat can end); your own brand compounds everything to you, and in 2026 the historical capital barrier is gone. The six systems a branded app needs: app, video hosting, live classes, ranked test engine, payments, and discovery - the first five are solved software, the sixth (distribution) is the real bottleneck a standalone app never solves. Honest cost math: custom build Rs 3-15 lakh upfront plus Rs 50,000-3 lakh/year maintenance; white-label SaaS roughly Rs 15,000-1 lakh/year billed before earning; free educator marketplace Rs 0 upfront and Rs 0 subscription with flat 10% only on sales. Illustrative earnings (not promised): 100-student live batch at Rs 999/month keeping 90% is about Rs 90,000/month, with recorded course and ranked test series stacking on top. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery by exam, subject and language. No fabricated stats; competitor described respectfully and structurally. Internal links to /blog/white-label-coaching-app-development-cost-india, /blog/unacademy-alternative-for-independent-educators, /blog/future-of-edtech-india-after-byjus-independent-educator, /blog/how-to-get-first-500-students-for-coaching-app, /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/classplus-vs-graphy-vs-allcoaching, /blog/how-to-price-online-courses-india, /blog/best-zero-commission-teaching-platform-india. Glossary terms: Teacher-as-Brand, Faculty Seat, Branded App, White-Label Build, Distribution Bottleneck, Niche Depth, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'physics wallah alternative for teachers', 'platform like physics wallah for educators', 'own branded coaching app india'. Audience targets Indian teachers deciding between joining a large EdTech company and building their own branded app in 2026."),
    },
    {
        "slug": "online-neet-coaching-platform-for-educators",
        "head": "Best NEET Coaching Platform for Educators — Own App (2026)",
        "card": "NEET Coaching Platform for Educators",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "Biology is half the paper &mdash; one subject is a complete business. Test series, recorded lectures and live doubts under your own name. Keep 90%.",
        "alt": "Online NEET coaching platform for educators — own branded app, 2026",
        "read": "17 min read",
        "cmt": "NEET Coaching Platform (Jul 7)",
        "llms": ("- [Best NEET Coaching Platform for Educators — Own App (2026)](https://allcoaching.in/blog/online-neet-coaching-platform-for-educators): "
          "A founder-written 2026 guide for NEET teachers on starting their own app to sell biology test series and recorded lectures, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step NEET-educator playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can a NEET teacher start their own app to sell test series and recorded lectures' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for NEET (Undergraduate), Biology, NCERT, Educational technology, Online tutoring and Test (assessment). "
          "Core reframe: one well-taught NEET subject is a complete sellable business, not a fragment - aspirants buy marks, not completeness, and biology carries 360 of NEET's 720 marks (half the paper), making a dedicated biology educator the highest-leverage single purchase an aspirant can make. Market shape: registrations crossing twenty lakh in recent cycles against around a lakh medical seats; the fastest-growing segments (droppers, Hindi-medium, small-town aspirants) are underserved by breadth and hungry for depth. What the app must include: an NCERT-anchored recorded course, a ranked test series (chapter-wise + full-length mocks with ranks and percentile feedback - the weekly retention engine), a live doubt batch at a fixed hour, and UPI payments with daily payouts. A standalone biology test series is a legitimate first product - explanations are the teaching. Illustrative economics (not promised): 100-aspirant live batch at Rs 999/month keeping 90% is about Rs 90,000/month; a Rs 499 test series sold to 200 students adds about Rs 90,000 at 90% keep; the recorded course keeps selling every season - three products from one preparation effort. Language-matched teaching (Hindi/regional) is a moat, not a limitation. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery by exam, subject and language. No fabricated stats. Internal links to /blog/online-jee-coaching-platform-for-teachers, /blog/physics-wallah-alternative-for-educators, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-to-create-interactive-mock-tests-online, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/multi-language-lms-for-regional-indian-languages, /blog/reduce-student-dropout-online-coaching-india, /blog/budget-home-studio-setup-for-online-teaching, /blog/how-to-price-online-courses-india. Glossary terms: Biology Weightage, NCERT-First Teaching, Ranked Test Series, Dropper Batch, Language-Matched Teaching, Branded Studio, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'neet coaching platform for educators', 'sell neet test series online', 'neet teacher own app'. Audience targets NEET teachers and biology educators in India building their own online coaching in 2026."),
    },
    {
        "slug": "winuall-alternative-for-coaching-institutes",
        "head": "Winuall Alternative for Coaching Institutes (2026)",
        "card": "Winuall Alternative for Coaching Institutes",
        "tag": "Comparison &middot; 2026",
        "dek": "A subscription bills your calendar; a marketplace bills your success. No subscription, Rs 0 upfront, flat 10% only on sales &mdash; keep 90%.",
        "alt": "Winuall alternative for coaching institutes — no subscription, 2026",
        "read": "16 min read",
        "cmt": "Winuall Alternative (Jul 7)",
        "llms": ("- [Winuall Alternative for Coaching Institutes (2026)](https://allcoaching.in/blog/winuall-alternative-for-coaching-institutes): "
          "A founder-written 2026 guide for coaching institutes weighing a Winuall alternative, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step zero-downtime migration playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'is there a Winuall alternative that doesn't charge a subscription' and a best-alternative recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Software as a service, White-label product, Subscription business model, Revenue sharing, Educational technology and Online marketplace. "
          "Core reframe: the question behind 'who takes no commission' is WHEN should the bill arrive - before you earn or after; every platform is paid somehow, and 'zero commission' platforms recover cost as calendar-driven subscriptions (typically Rs 15,000-1 lakh/year for white-label coaching SaaS) owed regardless of earnings. What Winuall-class white-label SaaS provides: genuinely useful software (branded app, live classes, test engine, fee management) that digitises the institute you already have - but the app arrives empty and filling it with students remains entirely the institute's problem (tool vs ecosystem). Honest fee taxonomy with both failure modes stated: a Rs 25,000 subscription against Rs 40,000 of sales is a 62% effective take-rate, while at Rs 10 lakh of sales a 10% share is Rs 1 lakh on paper - the comparison holds only because the 10% includes marketplace discovery, the expensive part of growth. Aligned incentive: a platform paid 10% of sales grows only by growing you. The practical test: if your online revenue stopped tomorrow, which model would still be billing you? Multi-teacher institute support is free-tier included (separate teacher logins, batch ownership, no per-seat pricing); optional Pro tier (roughly Rs 999-4,999/month: custom domain, advanced analytics, priority support) is genuinely optional with no trial that expires. Zero-downtime migration playbook: parallel studio setup, mirror batch structure, content before students, one-batch pilot, switch payments at the fee cycle, retire the old subscription at renewal. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; institute keeps 90% with a flat 10% on paid sales only, daily UPI payouts. No fabricated stats; competitor described structurally, no invented Winuall prices. Internal links to /blog/classplus-vs-graphy-vs-allcoaching, /blog/spayee-learnyst-alternative-india, /blog/teachmint-paid-features-alternative-free, /blog/sell-online-courses-without-monthly-subscription, /blog/white-label-coaching-app-development-cost-india, /blog/best-zero-commission-teaching-platform-india, /blog/automated-fee-management-software-for-teachers, /blog/how-to-get-first-500-students-for-coaching-app, /blog/migrate-offline-coaching-to-online-zero-cost. Glossary terms: White-Label SaaS, Subscription Model, Revenue-Share Model, Aligned Incentive, Distribution Bottleneck, Migration Window, Branded Studio, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'winuall alternative for coaching institutes', 'coaching app without subscription', 'coaching platform pay only on sales'. Audience targets coaching institute owners in India comparing white-label app platforms in 2026."),
    },
    {
        "slug": "online-upsc-coaching-platform-for-educators",
        "head": "Best Platform for UPSC Mentors — Test Series Online (2026)",
        "card": "UPSC Mentor Platform — Answer-Writing &amp; Test Series",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "Lectures are commoditised; evaluation is scarce. Run answer-writing and ranked prelims mocks under your own name &mdash; Rs 0, keep 90%.",
        "alt": "Online UPSC coaching platform for educators — answer-writing and prelims test series, 2026",
        "read": "17 min read",
        "cmt": "UPSC Mentor Platform (Jul 7)",
        "llms": ("- [Best Platform for UPSC Mentors — Test Series Online (2026)](https://allcoaching.in/blog/online-upsc-coaching-platform-for-educators): "
          "A founder-written 2026 guide for UPSC mentors on running mains answer-writing practice and prelims test series online under their own name, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step UPSC-mentor playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'what is the best platform for a UPSC mentor to run answer-writing and prelims test series online' and a copy-evaluation workflow Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Union Public Service Commission, Civil Services Examination (India), Essay, Test (assessment), Educational technology and Online tutoring. "
          "Core reframe: lecture content is commoditised while evaluation is starving - every UPSC topic is taught free many times over, but an aspirant cannot evaluate their own copy, and personalised feedback (what this answer missed, where marks leaked) requires a skilled human reading that specific copy and cannot be mass-produced; the mentor who evaluates seriously sells what no free video can substitute. Market shape: around ten lakh candidates apply in recent cycles with final selections around a thousand; trust runs person-to-person (aspirants distrust ads, follow marked copies posted in study circles); the volume-institute model breaks precisely at evaluation, opening the capped-batch independent niche. The answer-writing engine as a four-station loop: question calendar, PDF/photo copy submission, marked copy returned on a stated turnaround, recorded model-answer discussion per question set (reusable content); disciplines that matter - honoured turnaround and ruthless batch caps. The ranked prelims series: sectional + full-length mocks on a fixed schedule with ranks/percentiles, explanations that teach elimination and negative-marking discipline (when NOT to attempt scores as surely as knowledge). Illustrative economics (not promised): 50-aspirant mentorship batch at Rs 1,999/month keeping 90% is about Rs 90,000/month; a Rs 999 prelims series sold to 300 aspirants adds about Rs 2.7 lakh a season at 90% keep; premium-capped core with volume edges. No ex-IAS badge needed - evaluation quality is inspectable (model answers, sample marked copies); face-optional and job-compatible. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; mentor keeps 90% with a flat 10% on paid sales only, daily UPI payouts, ranked test engine, live hours and recorded content included. No fabricated stats. Internal links to /blog/how-to-record-upsc-lectures-and-sell-online, /blog/best-app-for-state-psc-coaching-educators, /blog/how-to-create-interactive-mock-tests-online, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/how-to-teach-online-without-showing-your-face-india, /blog/reduce-student-dropout-online-coaching-india, /blog/how-to-price-online-courses-india. Glossary terms: Answer-Writing Practice, Copy Evaluation, Model Answer, Prelims Test Series, Negative-Marking Discipline, Mentorship Batch, Branded Studio, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'upsc coaching platform for educators', 'upsc answer writing practice online', 'prelims test series platform'. Audience targets UPSC mentors and civil services educators in India building their own online mentorship in 2026."),
    },
]

LASTMOD = "2026-07-07T10:00:00+05:30"
DATEPUB = "2026-07-07"
N = len(BLOGS)

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/how-retired-teachers-can-earn-online-india</loc>'
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
lanchor = '- [How Retired Teachers Can Earn Online in India (2026)]'
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

assert '"numberOfItems":68,' in h
h = h.replace('"numberOfItems":68,', f'"numberOfItems":{68+N},', 1)

# stale masthead count -> true card count (68 existing + N new)
assert '49 published · Newest first' in h
h = h.replace('49 published · Newest first', f'{68+N} published · Newest first', 1)

canchor = '    <!-- Retired Teachers Earn Online (Jul 6) -->'
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

# ---------- 4) cross-refs ----------
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
          "| card:", f'/blog/{b["slug"]}" class="blog-card"' in h2)
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]', h2, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| count:", len(pos),
      "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h2).group(1))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h2, re.S):
    json.loads(x)
print("index JSON-LD valid OK")
