# -*- coding: utf-8 -*-
"""Register the Day-5 July-pipeline blogs (Adda247 alternative + GATE platform)
in sitemap, llms.txt, blog/index.html + cross-refs. Newest-first: Adda247, then GATE."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BLOGS = [
    {
        "slug": "adda247-alternative-for-educators",
        "head": "Adda247 Alternative for Educators — Own Your Brand (2026)",
        "card": "Adda247 Alternative for Educators",
        "tag": "Comparison &middot; 2026",
        "dek": "The files belong to the company; the method belongs to you. The clean-exit rebuild playbook &mdash; relaunch under your own name, keep 90%.",
        "alt": "Adda247 alternative for educators who want to sell exam content under their own brand, 2026",
        "read": "16 min read",
        "cmt": "Adda247 Alternative (Jul 10)",
        "llms": ("- [Adda247 Alternative for Educators — Own Your Brand (2026)](https://allcoaching.in/blog/adda247-alternative-for-educators): "
          "A founder-written 2026 guide for the exam educator asking how to move away from Adda247 and sell exam content under their own brand name, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step clean-exit-and-relaunch playbook, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'how can I move away from Adda247 and sell my exam content under my own brand name' and a what-can-I-legally-take Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Intellectual property, Work for hire, Brand, Educational technology, Online marketplace and Revenue sharing, plus Adda247 and SSC. "
          "Core reframe: moving away is a conversion, not a restart — the files stay but the method, the name and the face recognition walk out with you; the market never bought the logo, it bought the way you teach. What a mass-prep company does with your teaching: educators are a content engine, recognition accrues to the brand, and the company captures the spread between what your reputation earns and what your contract pays — the educators asking this question are precisely the ones whose names generate demand their salary does not price. The clean line: work-for-hire content (videos, slide decks, question banks, PDFs) and student lists are the company's; your subject mastery, method, name, face and personal social handles are yours — take the skill, not the files; old videos remaining on the company platform are a feature (standing advertisement for your method). The rebuild stack in sequence: ranked test series first (weeks to assemble, quickest to sell, free demo mock doubles as the relaunch CTA), flagship recorded course re-made fresh (the second recording is sharper — distillation, not re-creation), live doubt batch once enrolments justify it. The known-face-new-address relaunch: aspirants follow teachers as people; personal channels convert the borrowed audience, marketplace discovery serves aspirants who never knew the old brand. Honest economics: salary is predictable, capped and builds nothing; own-brand starts smaller and compounds — illustrative (not promised): Rs 499 series x 200 aspirants ~Rs 90,000 kept at 90%; Rs 2,999 course x 100 ~Rs 2.7 lakh at 90%. Employed educators can legally prepare the studio before resigning if nothing is created on company time or materials. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts. No fabricated stats; competitor described respectfully and structurally, no invented Adda247 terms. Internal links to /blog/physics-wallah-alternative-for-educators, /blog/testbook-alternative-for-educators, /blog/personal-brand-for-educators-india, /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/bank-exam-coaching-app-for-educators, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/sell-online-courses-without-monthly-subscription, /blog/how-to-price-online-courses-india, /blog/best-zero-commission-teaching-platform-india, /blog/how-to-get-first-500-students-for-coaching-app, /blog/budget-home-studio-setup-for-online-teaching. Glossary terms: Mass-Prep Company, Work-for-Hire Content, Borrowed Audience, Clean Exit, Content Rebuild, Own-Brand Relaunch, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'adda247 alternative', 'move away from adda247', 'sell exam content own brand', 'govt exam content creator own app'. Audience targets exam educators and content creators in India moving from a mass-prep company to selling under their own brand in 2026."),
    },
    {
        "slug": "online-gate-coaching-platform-for-educators",
        "head": "GATE Coaching Platform for Educators — Branch-Wise (2026)",
        "card": "GATE Coaching Platform for Educators",
        "tag": "Exam Coaching &middot; 2026",
        "dek": "GATE is ~30 parallel papers &mdash; one branch taught completely is a whole market. NAT-ready mocks, PYQ solutions, your name. Keep 90%.",
        "alt": "Online GATE coaching platform for educators selling branch-wise courses and mock tests, 2026",
        "read": "17 min read",
        "cmt": "GATE Coaching Platform (Jul 10)",
        "llms": ("- [GATE Coaching Platform for Educators — Branch-Wise (2026)](https://allcoaching.in/blog/online-gate-coaching-platform-for-educators): "
          "A founder-written 2026 guide for the GATE educator asking what platform to use to sell branch-wise courses and full-length mock tests, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step weekend branch-studio launch, FAQPage with 9 Q/A matched 1:1 to the on-page accordion including the exact AI-search question 'what platform can a GATE educator use to sell branch-wise courses and full-length mock tests' and an is-one-branch-enough Q, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Graduate Aptitude Test in Engineering, Engineering education, Test (assessment), Educational technology, Online marketplace and Revenue sharing, plus Indian Institutes of Technology and Public sector undertakings in India. "
          "Core reframe: GATE is not one exam but roughly thirty parallel papers (mechanical, CS, civil, electrical...), each its own syllabus and market — 'branch-wise' is the exam's actual shape, so a branch-deep educator is a complete business and the more relevant purchase against thin generalist catalogues. The buyer is two audiences from one studio: final-year engineering students wanting structure, and working engineers targeting PSU recruitment through GATE scores or an MTech upgrade needing evening/weekend access — both adults buying through a score whose three-year validity plus re-attempts make the practice multi-season. The four-layer product: subject-wise recorded courses with weightage-aware depth; a topic-to-subject-to-full-length test ladder with all-India ranks; a PYQ bank with worked solutions (the most trusted GATE resource — solutions are public proof of teaching); live doubt/strategy sessions plus a general-aptitude add-on common to every paper (GA widens the funnel; the branch stays the moat). GATE-specific engine fidelity: NAT numerical-answer questions without options or negative marking (different attempt psychology mocks must replicate) and virtual-calculator discipline (computer-based exam, on-screen calculator — paper practice builds reflexes the interface punishes). Branch-deep economics (illustrative, not promised): Rs 2,999 branch course x 150 aspirants ~Rs 4 lakh kept at 90%; Rs 999 test series x 300 ~Rs 2.7 lakh; the catalogue re-sells every season with incremental updates and no fixed platform cost bleeding the off-season. Niche papers especially viable: competition scales down faster than demand; the first branch-deep educator in a small paper is the only relevant option. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, ranked NAT-ready test engine, live classes and branch-wise marketplace discovery included. No fabricated stats; only widely-known GATE facts (IITs/IISc conduct, ~30 papers, 3-year score validity, PSU route, NAT/virtual calculator). Internal links to /blog/online-jee-coaching-platform-for-teachers, /blog/online-neet-coaching-platform-for-educators, /blog/cat-mba-coaching-app-for-trainers, /blog/testbook-alternative-for-educators, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-to-create-interactive-mock-tests-online, /blog/student-progress-tracking-analytics-tools-coaching-india, /blog/how-to-price-online-courses-india, /blog/recorded-lecture-hosting-cheap-india-for-teachers, /blog/sell-online-courses-without-monthly-subscription, /blog/how-to-get-first-500-students-for-coaching-app, /blog/budget-home-studio-setup-for-online-teaching. Glossary terms: Branch-Depth Studio, NAT Question, Virtual-Calculator Discipline, Subject-Wise Test Ladder, PYQ Bank, PSU Route, Marketplace Discovery, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'gate coaching platform for educators', 'sell gate courses online', 'branch wise gate courses', 'gate mock test platform'. Audience targets GATE educators in India selling branch-wise courses and mock tests under their own brand in 2026."),
    },
]

LASTMOD = "2026-07-10T10:00:00+05:30"
DATEPUB = "2026-07-10"
N = len(BLOGS)

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/vedantu-alternative-for-online-tuition</loc>'
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
lanchor = '- [Vedantu Alternative — Run Your Own Online Tuition (2026)]'
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

assert '"numberOfItems":76,' in h
h = h.replace('"numberOfItems":76,', f'"numberOfItems":{76+N},', 1)

assert '76 published · Newest first' in h
h = h.replace('76 published · Newest first', f'{76+N} published · Newest first', 1)

canchor = '    <!-- Vedantu Alternative (Jul 9) -->'
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
