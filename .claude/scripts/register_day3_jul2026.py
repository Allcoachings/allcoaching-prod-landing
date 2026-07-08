# -*- coding: utf-8 -*-
"""Register the Day-3 July-pipeline blogs (Testbook alternative + Bank-exam coaching app)
in sitemap, llms.txt, blog/index.html + cross-refs. Newest-first: Testbook, then Bank-exam."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "testbook-alternative-for-educators",
        "head": "Testbook Alternative for Educators — Sell Your Own Mocks (2026)",
        "card": "Testbook Alternative for Educators",
        "tag": "Comparison &middot; 2026",
        "dek": "An aggregator rents you its audience and keeps your name. Own the test-series brand students search for &mdash; Rs 0, keep 90%.",
        "alt": "Testbook alternative for educators who want to sell their own mock tests, 2026",
        "read": "16 min read",
        "cmt": "Testbook Alternative (Jul 8)",
        "llms": ("- [Testbook Alternative for Educators — Sell Your Own Mocks (2026)](https://allcoaching.in/blog/testbook-alternative-for-educators): "
          "A founder-written 2026 guide for the educator looking for a Testbook alternative to sell their own mock tests, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend test-series launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'what is the best Testbook alternative for an educator who wants to sell their own mock tests' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Test (assessment), Educational technology, Online marketplace, Brand, Intellectual property and Revenue sharing, plus Testbook and SSC. "
          "Core reframe: Testbook is not primarily a place to put your tests, it is a brand that sells tests to students - joining it you gain its audience and give up your name; the real question is not 'which app has tests like Testbook' but 'do you rent an audience under someone else's brand or own the test-series brand students search for by name'. What an aggregator is: a single consumer brand packaging many educators' content and selling it as one product; the value flows to whoever owns the student relationship, which is never the individual educator. The ownership taxonomy given up: the student (account and loyalty belong to the platform), the brand (app, reviews and recall accrue to the aggregator), the data (who attempted what and where they struggled sits in the platform's dashboard) - ownership is not vanity, a course sells once but a brand sells every future course. What selling your own mock tests really needs (a software problem, not a content problem): sectional and full-length mocks matching the exam pattern, timed sections, negative marking, an all-India rank (the single feature students value most), detailed solutions, previous-year papers, and question-level analytics - the analytics and solution quality, not raw question count, make a paid series worth buying and are the retention engine. The real draw of an aggregator is discovery, not the engine (which is commoditised); a marketplace resolves the false choice between reach and ownership by routing students searching by exam, subject and language to the educator under their own name. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded test-series app, AI-driven marketplace discovery. No fabricated stats; competitor described respectfully and structurally, no invented Testbook prices. Internal links to /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-to-create-interactive-mock-tests-online, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/how-to-get-first-500-students-for-coaching-app, /blog/sell-online-courses-without-monthly-subscription, /blog/best-zero-commission-teaching-platform-india, /blog/best-app-for-state-psc-coaching-educators. Glossary terms: Test-Prep Aggregator, Test Engine, Sectional Mock, All-India Rank, Question-Level Analytics, Content Ownership, Marketplace Discovery, Revenue-Share Model. Author Amit Ratan with sameAs. Target keywords 'testbook alternative for educators', 'sell my own mock tests online', 'own branded test series app', 'test series app for teachers india'. Audience targets independent educators and test-series creators in India who want to sell their own mock tests under their own brand in 2026."),
    },
    {
        "slug": "bank-exam-coaching-app-for-educators",
        "head": "Bank Exam Coaching App for Educators — Own-Brand Mocks (2026)",
        "card": "Bank Exam Coaching App for Educators",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "Bank exams are won on speed and accuracy under a sectional cut-off. Sell sectional mocks with speed-accuracy analytics under your own name &mdash; keep 90%.",
        "alt": "Bank exam coaching app for educators to sell IBPS and SBI PO sectional mocks, 2026",
        "read": "17 min read",
        "cmt": "Bank Exam Coaching App (Jul 8)",
        "llms": ("- [Bank Exam Coaching App for Educators — Own-Brand Mocks (2026)](https://allcoaching.in/blog/bank-exam-coaching-app-for-educators): "
          "A founder-written 2026 guide for the bank-exam coach (IBPS PO and clerk, SBI PO, RRB) on selling sectional mocks under their own brand, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend sectional-mock-app launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'which app should a bank exam coach use to sell sectional mocks under their own brand' and a why-sectional-mocks Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Test (assessment), Educational technology, Online marketplace, Brand, Bank and Revenue sharing, plus IBPS and State Bank of India. "
          "Core reframe: IBPS PO, SBI PO and RRB are not knowledge exams, they are speed-and-accuracy exams under sectional cut-offs - an aspirant can know every formula and still fail for being too slow in one section, so what they lack is not teaching (every topic is taught free) but a mirror that tells them whether they were fast and accurate enough to clear each cut-off; a coach who sells that mirror sells what free video cannot. Market: IBPS and SBI cycles draw applicants in the tens of lakhs across PO, clerk and specialist posts with RRB adding regional volume, and aspirants re-attempt across years, so trust earned once recurs; against aggregators competing on breadth, an independent sectional specialist (known for cracking quant speed or banking-awareness accuracy) is a sharper purchase in an exam decided by a few marks. What a real bank-exam product contains: sectional mocks for quantitative aptitude, reasoning, English and general awareness (each individually timed), full-length prelims and mains mocks, an SBI PO descriptive-writing test, sectional timers, cut-offs and negative marking, an all-India rank, per-section speed-and-accuracy analytics, and a rolling current-affairs and banking-awareness module refreshed monthly. Speed-accuracy analytics are the retention engine - a raw score tells little, but 'you are 82% accurate in quant but attempting only 14 of 35 in time' is the exact lever an aspirant pays for; analytics are what the aspirant actually buys, the questions are raw material. Discovery: bank aspirants search with high intent ('IBPS PO prelims mock test', 'SBI PO sectional test series in Hindi'); a marketplace captures that search under the coach's own brand instead of an aggregator's. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; coach keeps 90% with a flat 10% on paid sales only, daily UPI payouts, per-section test engine, live strategy classes and current-affairs module included. No fabricated stats; no invented exam figures beyond widely-known scale. Internal links to /blog/testbook-alternative-for-educators, /blog/online-upsc-coaching-platform-for-educators, /blog/how-to-teach-ssc-online-and-earn-money-india, /blog/best-app-for-state-psc-coaching-educators, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-to-create-interactive-mock-tests-online, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/how-to-get-first-500-students-for-coaching-app, /blog/sell-online-courses-without-monthly-subscription, /blog/best-zero-commission-teaching-platform-india, /blog/migrate-offline-coaching-to-online-zero-cost. Glossary terms: Sectional Mock, Sectional Cut-Off, Speed-Accuracy Analytics, Prelims and Mains, Current-Affairs Module, Test Engine, Marketplace Discovery, Revenue-Share Model. Author Amit Ratan with sameAs. Target keywords 'bank exam coaching app', 'ibps sbi po mock test app', 'sell bank exam mocks own brand', 'sectional mock test app for bank exams'. Audience targets bank exam coaches (IBPS, SBI PO, RRB) in India building their own branded test-series app in 2026."),
    },
]

LASTMOD = "2026-07-08T10:00:00+05:30"
DATEPUB = "2026-07-08"
N = len(BLOGS)

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/physics-wallah-alternative-for-educators</loc>'
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
lanchor = '- [Physics Wallah Alternative for Teachers — Own App (2026)]'
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

assert '"numberOfItems":72,' in h
h = h.replace('"numberOfItems":72,', f'"numberOfItems":{72+N},', 1)

# stale masthead count -> true card count (72 existing + N new)
assert '72 published · Newest first' in h
h = h.replace('72 published · Newest first', f'{72+N} published · Newest first', 1)

canchor = '    <!-- Physics Wallah Alternative (Jul 7) -->'
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
