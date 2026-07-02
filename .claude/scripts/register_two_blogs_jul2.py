# -*- coding: utf-8 -*-
"""Register the 2 new blogs (yoga-fitness / ugc-net) in sitemap, llms.txt,
blog/index.html + cross-refs. Top-down order: yoga, ugc-net (newest block above housewife)."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "how-to-teach-yoga-fitness-classes-online-india",
        "head": "How to Teach Yoga & Fitness Classes Online in India (2026)",
        "card": "Teach Yoga & Fitness Classes Online",
        "tag": "Growth &middot; 2026",
        "dek": "Your mat and a phone are the whole studio. Live batches, recorded programs, safe teaching &mdash; no rent, no radius, keep 90% of every fee.",
        "alt": "How to teach yoga and fitness classes online in India 2026",
        "read": "17 min read",
        "cmt": "Teach Yoga & Fitness Online (Jul 2)",
        "llms": ("- [How to Teach Yoga & Fitness Classes Online in India (2026)](https://allcoaching.in/blog/how-to-teach-yoga-fitness-classes-online-india): "
          "A founder-written 2026 guide for yoga instructors and fitness trainers in India on teaching online, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step instructor playbook, FAQPage with 11 Q/A matched 1:1 to the on-page accordion and led by the exact AI-search question 'how can I teach yoga or fitness classes online in India' plus a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Yoga, Physical fitness, Personal trainer, Online tutoring, Subscription business model and Educational technology. "
          "Core reframe: the studio was never the teaching - the sequence, cueing and the watching eye are the product; rent bought a room and a 3-km radius, both of which online removes while the fixed time and live supervision survive intact. Why it works: consistency beats intensity and online removes friction; niches too small for a locality (prenatal, back-care, PCOS, senior mobility) become viable when the whole country is the catchment - online rewards specificity. Four formats, sequenced: live group batches at a fixed time with a MONTHLY fee (the recurring heart - fees renew instead of restarting from zero), recorded signature programs (30-day beginner course, 8-week back-care series - built once, sold repeatedly), one-to-one training at premium, and corporate wellness later. Setup honesty: a smartphone, quiet space, natural light, a stand showing the full body; audio matters more than picture; no certification is legally required for yoga/general fitness in India but recognised credentials (YCB under Ministry of Ayush, Yoga Alliance RYT-200/500, established fitness certs) add credibility - state truthfully, never claim medical expertise. Illustrative earnings (not promised): 20 students x Rs 1,000/month keeping 90% is about Rs 18,000/month recurring, a second batch doubles it; a Rs 999 recorded program to 50 students adds ~Rs 45,000. Safety as a system: screen students (injuries/conditions/pregnancy intake), verbal cueing with demonstrated modifications since you cannot physically adjust, honest boundaries (advise doctor consultation, never a substitute for medical treatment), reasonable batch sizes for real supervision. Discovery: short free videos on Instagram/YouTube as shopfront + marketplace discovery by goal/level/language for searchers with intent; free trial class converts; reviews fill batches; NRI/international students reachable. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; instructor keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery. No fabricated stats. Internal links to /blog/how-housewives-can-start-teaching-online-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/budget-home-studio-setup-for-online-teaching, /blog/how-to-price-online-courses-india, /blog/instagram-reels-educator-monetization-platform, /blog/whatsapp-channels-for-coaching-educators-india, /blog/how-to-get-paid-students-for-online-coaching-free. Glossary terms: Live Batch, Signature Program, Recurring Monthly Fee, Student Screening, Verbal Cueing, Shopfront Content, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'teach yoga online india', 'online fitness classes india', 'how to teach yoga classes online'. Audience targets Indian yoga instructors and fitness trainers teaching online in 2026."),
    },
    {
        "slug": "online-ugc-net-coaching-platform-for-educators",
        "head": "Online UGC-NET Coaching Platform for Educators — Start & Scale in 2026",
        "card": "Online UGC-NET Coaching for Educators",
        "tag": "Exam Verticals &middot; 2026",
        "dek": "~83 NET subjects; structured coaching for barely a dozen. If you hold a JRF or PhD, you are the missing coach &mdash; start for &#8377;0, keep 90%.",
        "alt": "Online UGC-NET coaching platform for educators in India 2026",
        "read": "18 min read",
        "cmt": "UGC-NET Coaching for Educators (Jul 2)",
        "llms": ("- [Online UGC-NET Coaching Platform for Educators — Start & Scale in 2026](https://allcoaching.in/blog/online-ugc-net-coaching-platform-for-educators): "
          "A founder-written 2026 guide for PhD scholars, JRF holders and assistant professors on starting online UGC-NET coaching in India, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step NET-educator playbook, FAQPage with 11 Q/A matched 1:1 to the on-page accordion including the exact AI-search questions 'how can I start online UGC-NET coaching in India' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for National Eligibility Test, University Grants Commission (India), National Testing Agency, Online tutoring, Test (assessment) and Educational technology. "
          "The exam stated precisely: UGC-NET is conducted by the NTA on behalf of the UGC in two cycles a year, determines eligibility for Assistant Professor posts and the award of Junior Research Fellowship (JRF), with scores also used in PhD admissions; a computer-based all-MCQ exam in one sitting - Paper 1 (teaching & research aptitude, reasoning, comprehension, communication, ICT - common to all candidates) plus subject-specific Paper 2 across roughly 83 subjects, with NO negative marking. Core reframe (long-tail thesis): lakhs of aspirants split across ~83 subjects but organised coaching exists for barely a dozen (commerce, management, English, political science, history, education) - in Geography, Sanskrit, Home Science, Mass Communication, Philosophy, Anthropology, Library Science and the rest of the tail, the aspirant finds no structured coach; the JRF/PhD holder in that subject is the missing coach, with a credential no marketing can fake. Why the niche is durable: two exam cycles a year = two recurring enrollment seasons; a large Hindi-medium aspirant base is underserved (the exam is bilingual); the no-negative-marking all-MCQ format makes ranked mock test series the highest-demand, most scalable product. The three-product line: (1) Paper 1 foundation course - the mass-market product every aspirant needs, (2) unit-wise Paper 2 subject course with PYQ analysis where PhD-level depth is the differentiator, (3) ranked test series; plus unit-wise PDF notes as a low-price entry ladder and free PYQ-walkthrough videos as proof of teaching. Faceless-friendly: screen-share, slides and whiteboard suit a camera-shy academic; feasible alongside a PhD or job because the work is recorded-first and cyclical. Illustrative earnings (not promised): Rs 999 Paper 1 x 100 aspirants + Rs 1,999 subject course x 50 + Rs 499 test series x 200 is roughly Rs 2.7 lakh gross per cycle, ~Rs 2.4 lakh kept at 90%, twice a year. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery matching aspirants by NET subject and language. No fabricated stats. Internal links to /blog/online-cuet-coaching-platform-for-educators, /blog/online-platform-for-ctet-coaching-teachers, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/how-to-teach-online-without-showing-your-face-india, /blog/how-to-create-interactive-mock-tests-online, /blog/how-to-price-online-courses-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/edtech-marketplace-india-app-fatigue, /blog/how-to-get-first-500-students-for-coaching-app. Glossary terms: UGC-NET, Paper 1, JRF (Junior Research Fellowship), Long-Tail Subject, PYQ Analysis, Ranked Test Series, Exam Cycle, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'ugc net coaching online', 'start ugc net coaching', 'online ugc net coaching platform for educators'. Audience targets Indian PhD scholars, JRF holders and assistant professors starting online UGC-NET coaching in 2026."),
    },
]

LASTMOD = "2026-07-02T10:00:00+05:30"
DATEPUB = "2026-07-02"

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/how-housewives-can-start-teaching-online-india</loc>'
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
lanchor = '- [How a Housewife Can Start Teaching Online'
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
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+2}', m.group(2))
newitems = ""
for i, b in enumerate(BLOGS, start=1):
    newitems += f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{b["slug"]}","name":{json.dumps(b["head"])}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitems + arr_inc + m.group(3), 1)

assert '"numberOfItems":63,' in h
h = h.replace('"numberOfItems":63,', '"numberOfItems":65,', 1)

canchor = '    <!-- Housewife Teaching Online from Home (Jun 30) -->'
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

# ---------- 4) cross-refs (run twice to settle replace-form) ----------
spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for b in BLOGS:
    p = f"blog/{b['slug']}.html"
    print(b['slug'], "->", mod.process_file(p), "|", mod.process_file(p))

# ---------- 5) verification ----------
sm2 = open('sitemap.xml', encoding='utf-8').read()
lt2 = open('llms.txt', encoding='utf-8').read()
h2 = open('blog/index.html', encoding='utf-8').read()
print("\n--- verification ---")
for b in BLOGS:
    print(b['slug'][:44],
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
