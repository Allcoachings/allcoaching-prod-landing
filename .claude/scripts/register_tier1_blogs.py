# -*- coding: utf-8 -*-
"""Register the 3 Tier-1 persona blogs (retired / college-student / working-professional) in
sitemap, llms.txt, blog/index.html + cross-refs. Top-down: retired, college, professional."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "how-retired-teachers-can-earn-online-india",
        "head": "How Retired Teachers Can Earn Online in India (2026)",
        "card": "How Retired Teachers Can Earn Online",
        "tag": "Growth &middot; 2026",
        "dek": "The classroom asked for your body; online asks only for your experience. Record it once, keep 90%, earn while you rest &mdash; no tech needed.",
        "alt": "How retired teachers can earn online in India 2026",
        "read": "17 min read",
        "cmt": "Retired Teachers Earn Online (Jul 6)",
        "llms": ("- [How Retired Teachers Can Earn Online in India (2026)](https://allcoaching.in/blog/how-retired-teachers-can-earn-online-india): "
          "A founder-written 2026 guide for retired teachers and professors in India on earning a second income online, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step retired-teacher playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can a retired teacher earn online in India' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Retirement, Online tutoring, Teacher, Educational technology, Passive income and Income. "
          "Core reframe: experience is the asset - decades of knowing exactly where students struggle is something no younger teacher can fake, and retirement perfected it rather than ended it; online strips away the tiring parts of a career (commute, standing, crowd, timetable) and keeps the valuable part (explaining a hard subject clearly). Why age is an advantage: trust/experience is the strongest purchase signal in education; parents actively prefer an experienced teacher; the physical demands vanish; the pace becomes recording once at your own schedule; keeping-up is beside the point because fundamentals are timeless. What to teach: the one subject/class/exam you became known for, deep not broad; resist 'my subject is too basic' and 'I'm not current' - a clear fundamentals course from an experienced teacher is exactly what students value. Start for Rs 0 with NO technical background: if you can make a WhatsApp video call and a UPI payment you can set up in an afternoon; no website, software, code or fee. Own pace: recorded course is the calm base (made once, sells again and again, earns while you rest), optional small live batch or ranked test series for those who want contact - never a full timetable. Illustrative earnings (not promised): Rs 999 recorded course x 50 students keeping 90% is about Rs 45,000 from work recorded once and it keeps selling; a 15-student live batch at Rs 800/month is about Rs 10,800/month; the defining feature is a high income-to-effort ratio - a genuine pension supplement, not a second job. No cash/agents/middlemen. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery by subject and language (Hindi/regional an advantage). No fabricated stats. Internal links to /blog/school-teacher-side-income-from-online-coaching, /blog/how-housewives-can-start-teaching-online-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/how-to-price-online-courses-india, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/how-to-get-paid-students-for-online-coaching-free. Glossary terms: Second Income, Signature Course, Experience Premium, Passive Course Income, Branded Studio, UPI Payout, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'retired teacher online income india', 'second income for retired teachers', 'retired professor teach online'. Audience targets retired teachers and professors in India earning online in 2026."),
    },
    {
        "slug": "how-college-students-can-earn-teaching-online-india",
        "head": "How College Students Can Earn by Teaching Online in India (2026)",
        "card": "How College Students Can Earn Teaching Online",
        "tag": "Growth &middot; 2026",
        "dek": "You just cleared the exam a junior is stuck on. Sell your notes, record a short course &mdash; zero investment, keep 90%, and it earns even during your exam weeks.",
        "alt": "How college students can earn by teaching online in India 2026",
        "read": "17 min read",
        "cmt": "College Students Earn Teaching Online (Jul 6)",
        "llms": ("- [How College Students Can Earn by Teaching Online in India (2026)](https://allcoaching.in/blog/how-college-students-can-earn-teaching-online-india): "
          "A founder-written 2026 guide for college students in India on earning money by teaching online with zero investment and around class/exam schedules, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step student-earner playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can a college student earn money by teaching online in India' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Student, Online tutoring, Part-time job, Peer tutoring, Educational technology and Income. "
          "Core reframe: recency is the asset - a student who cleared the exam last year remembers exactly where juniors get stuck, which the older teacher forgets; being young/close-in-age is an advantage, not a disadvantage. Two owned assets: recency (fresh accurate syllabus/exam knowledge) and relatability (juniors trust and understand a senior a few years ahead), plus notes already made for one's own study. What to teach: a subject you scored well in and cleared recently (Class 9-12, JEE/NEET topics, board chapters, a language, coding/spoken-English/design); the smartest FIRST move is selling existing notes and solved papers as PDFs - lowest-effort, no filming, and it introduces buyers who later buy a course or join a live session. Start for Rs 0: only a phone and a subject; no capital, website, equipment or fee. Balance with studies via recorded-first: recorded notes/courses keep selling even during the student's own exam weeks; live sessions optional and easy to pause; scale up in holidays, down in finals, studies first. Illustrative earnings (not promised): Rs 199 notes/short course x 100 students keeping 90% is about Rs 18,000 from work done once and it keeps selling; a 10-student live batch at Rs 500/month is about Rs 4,500/month; meaningful pocket money at zero cost. Safety: payments to own bank via UPI not cash, teach via screen/slides/voice, platform controls access. Second payoff: builds communication, discipline and a small venture - resume-worthy, not a gimmick. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; student keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery bringing junior/school students by subject; pause and resume anytime. No fabricated stats. Internal links to /blog/how-housewives-can-start-teaching-online-india, /blog/how-much-can-you-earn-teaching-online-india, /blog/personal-brand-for-educators-india, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/how-to-get-paid-students-for-online-coaching-free. Glossary terms: Peer Advantage, Notes Selling, Recorded-First, Zero Investment, Branded Studio, UPI Payout, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'how college students can earn teaching online', 'part time online tutoring for students', 'student side income india'. Audience targets college students in India earning by teaching online in 2026."),
    },
    {
        "slug": "online-teaching-side-income-for-working-professionals-india",
        "head": "Online Teaching Side Income for Working Professionals in India (2026)",
        "card": "Online Teaching Side Income for Professionals",
        "tag": "Growth &middot; 2026",
        "dek": "A second job costs evenings. A recorded course costs a few weekends &mdash; once &mdash; then earns while you work. Teach the skill your job gave you, keep 90%.",
        "alt": "Online teaching side income for working professionals in India 2026",
        "read": "17 min read",
        "cmt": "Side Income for Working Professionals (Jul 6)",
        "llms": ("- [Online Teaching Side Income for Working Professionals in India (2026)](https://allcoaching.in/blog/online-teaching-side-income-for-working-professionals-india): "
          "A founder-written 2026 guide for working professionals in India on building a side income teaching online around a full-time job with no capital, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step professional playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can a working professional earn a side income teaching online in India' and a best-platform recommendation Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Moonlighting, Online tutoring, Passive income, Skill, Educational technology and Income. "
          "Core reframe: a course is NOT a second job - a second job trades more of your hours for money (the thing you have least of), a recorded course trades a few hours once for money that keeps arriving; the asset is applied, job-tested expertise (the skill colleagues ask you about) which a working learner pays well for because it advances a career. What to teach: ask what people already come to you for; strongest families are job/career skills (Excel, coding, digital marketing, accounting, finance, design, PM), interview/workplace/communication skills, and exams/subjects you cleared or mastered; keep it focused and practical - a practitioner teaches the real-world version a textbook cannot. Recorded-first is the sustainability decision: effort is front-loaded (record one short module a weekend over a month) then selling is automatic and time-cost near zero; income arrives while you are in a meeting/asleep/on holiday; optional light weekend cohort only if wanted. Start for Rs 0 in an evening: no website, software or hire; no monthly cost, no investment to recoup. Employment terms: check contract/policy for outside-work/conflict/confidentiality rules; teach general publicly-known skills, use only your own time/equipment, share no confidential/client material; handled cleanly it strengthens standing rather than risking the job; check HR when unsure. Illustrative earnings (not promised): practical courses command higher prices than school tuition; Rs 1,999 course x 60 learners keeping 90% is about Rs 1,08,000 from a course recorded once and it keeps selling - leverage: paid many times for expertise recorded once, on top of a salary. Second payoff: deepens mastery, sharpens communication, builds visibility/personal brand that helps the main career (promotions, opportunities). Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; professional keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app, AI-driven marketplace discovery by skill. No fabricated stats. Internal links to /blog/school-teacher-side-income-from-online-coaching, /blog/how-much-can-you-earn-teaching-online-india, /blog/how-to-price-online-courses-india, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/how-to-get-paid-students-for-online-coaching-free. Glossary terms: Side Income, Recorded-First, Applied Expertise, Passive Course Income, Employment Terms, Branded Studio, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'online teaching side income working professionals', 'passive income teaching online india', 'professional teach skills online'. Audience targets working professionals in India building an online teaching side income in 2026."),
    },
]

LASTMOD = "2026-07-06T10:00:00+05:30"
DATEPUB = "2026-07-06"

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/how-to-teach-yoga-fitness-classes-online-india</loc>'
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
lanchor = '- [How to Teach Yoga & Fitness Classes Online'
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
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+3}', m.group(2))
newitems = ""
for i, b in enumerate(BLOGS, start=1):
    newitems += f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{b["slug"]}","name":{json.dumps(b["head"])}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitems + arr_inc + m.group(3), 1)

assert '"numberOfItems":65,' in h
h = h.replace('"numberOfItems":65,', '"numberOfItems":68,', 1)

canchor = '    <!-- Teach Yoga & Fitness Online (Jul 2) -->'
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
    print(b['slug'], "->", mod.process_file(p), "|", mod.process_file(p))

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
