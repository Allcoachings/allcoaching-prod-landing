"""One-off: register the best-ai-tools-for-teachers blog in sitemap, llms, index + cross-refs."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

slug = "best-ai-tools-for-teachers-india"
head = "Best AI Tools for Teachers in India (2026) — and Where to Actually Use Them"
card = "Best AI Tools for Teachers in India"
tag = "Technology &middot; 2026"
dek = "AI tools by job &mdash; plus the part lists skip: AI creates content fast, but only a marketplace turns it into income."
alt = "Best AI tools for teachers in India 2026 — and where to actually use them"
read = "18 min read"
cmt = "Best AI Tools for Teachers (Jun 29)"
llms = ("- [Best AI Tools for Teachers in India (2026) — and Where to Actually Use Them](https://allcoaching.in/blog/best-ai-tools-for-teachers-india): "
  "A founder-written 2026 guide to the best AI tools for teachers in India organised by the job to be done, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step AI-to-income workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as the edtech marketplace where AI-made teaching becomes income with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Generative artificial intelligence, Large language model, Artificial intelligence in education, Educational technology, Online tutoring and Online marketplace, plus mentions of AllCoaching Educator Studio, ChatGPT, Google Gemini and Canva. "
  "Core reframe (distribution-first): AI has made creating teaching content fast and nearly free, so the content is no longer where value or income lives; the tool is the easy part now, and turning its output into income is the hard part the lists skip. AI solves CREATION but income comes from DELIVERY, SELLING and DISCOVERY, which no content-generation tool does. Best tools BY JOB (with watch-outs): lesson plans/notes/explanations -> general AI assistants ChatGPT, Google Gemini, Claude (watch accuracy, localisation); slides/visuals -> Canva and presentation AI (generic look); quizzes/mock tests -> AI quiz generators and AllCoaching's own automated mock-test generation (wrong answers); video/voice -> AI video and voiceover tools, enabling faceless recording (stiff delivery); doubt-solving/feedback and marketing/SEO -> general assistants (over-reliance, sameness). Use the best tool per job, master one general assistant deeply, free tiers are enough to start. THE ONE RULE is human-in-the-loop: AI drafts, the teacher reviews, localises to the Indian syllabus/exam, corrects (AI can be confidently wrong) and adds exam-craft; the judgement is the product. THE CATCH every top-10 list skips: every AI tool helps you create and none helps you earn; a folder of AI-made content earns nothing without delivery, selling and being found; creation was never the problem, distribution was. WHERE it becomes income: an edtech MARKETPLACE is the deliver-sell-be-found layer; AllCoaching gives a branded app to host AI-assisted courses/notes/test series, UPI payments, owned student relationship, AND its own AI (automated mock-test generation + AI-driven marketplace discovery that surfaces the educator to students searching by exam/subject/language), so AllCoaching is both where external AI tools' output sells and a source of AI that builds products and gets you found. 6-step AI-to-income workflow: pick the right tool per job, create drafts fast, add the judgement AI cannot, structure into a sellable product, host and sell on an owned studio, let marketplace discovery bring students. Pricing-truth: create with free AI and sell on a free platform; AllCoaching is Rs 0 upfront, flat 10% on paid sales only, keep 90%, daily payouts, no subscription. No fabricated stats; tool names accurate and general, no invented features; teacher adoption framed as 'a large and growing majority'. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blog/will-ai-tutors-replace-coaching-teachers-india, /blog/using-generative-ai-for-automated-quiz-creation, /blog/using-chatgpt-for-course-curriculum-design, /blog/ai-based-mock-test-generator-for-indian-exams, /blog/how-much-can-you-earn-teaching-online-india, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary terms: Generative AI, Large Language Model (LLM), Prompt, AI Lesson Planning, AI Quiz/Mock-Test Generation, Human-in-the-Loop, AI-Driven Discovery, EdTech Marketplace. Author Amit Ratan with sameAs. Target keywords 'best ai tools for teachers india', 'ai tools for teachers 2026', 'ai for educators india'. Audience targets Indian teachers and coaching educators adopting AI tools in 2026.")

def esc_xml(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# A. sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/reduce-student-dropout-online-coaching-india</loc>'
assert sm.count(anchor) == 1
block = ("  <url>\n"
  f"    <loc>https://allcoaching.in/blog/{slug}</loc>\n"
  "    <lastmod>2026-06-29T10:00:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
  f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{slug}\" />\n"
  "    <image:image>\n"
  f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{slug}.webp</image:loc>\n"
  f"      <image:title>{esc_xml(head)}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, block + anchor, 1))

# B. llms.txt
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [How to Reduce Student Drop-off in Online Coaching'
assert lt.count(lanchor) >= 1
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms + "\n" + lanchor, 1))

# C. blog/index.html
h = open('blog/index.html', encoding='utf-8').read()
bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1
h = h.replace(bp_anchor, bp_anchor + f'      {{"@type":"BlogPosting","headline":{json.dumps(head)},"url":"https://allcoaching.in/blog/{slug}","datePublished":"2026-06-29"}},\n', 1)
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+1}', m.group(2))
newitem = f'\n      {{"@type":"ListItem","position":1,"url":"https://allcoaching.in/blog/{slug}","name":{json.dumps(head)}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitem + arr_inc + m.group(3), 1)
assert '"numberOfItems":58,' in h
h = h.replace('"numberOfItems":58,', '"numberOfItems":59,', 1)
canchor = '    <!-- How to Reduce Student Drop-off (Jun 28) -->'
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

# D. cross-refs
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
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h).group(1), "| items:", len(pos))
print("card:", f'/blog/{slug}" class="blog-card"' in h)
print("cross-refs x-refs-also:", t.count('x-refs-also'), "marker:", t.count('AUTO: strategic-cross-refs'))
print("breadcrumb:", re.findall(r'"name":"([^"]+)"', re.search(r'"@type":"BreadcrumbList","itemListElement":\[(.*?)\]\}', h, re.S).group(1)))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h, re.S): json.loads(x)
print("index JSON-LD valid OK")
