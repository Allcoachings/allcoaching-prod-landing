import re, glob, os

SLUG = 'ai-based-mock-test-generator-for-indian-exams'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'AI-Based Mock Test Generator for Indian Exams — How AI Is Rewiring Test Prep (2026 Tech Focus)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-09'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 40 and N_ALL == 75, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- AI-Based Mock Test Generator for Indian Exams (Jun 9) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: AI-Based Mock Test Generator for Indian Exams">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="AI-based mock test generator for Indian exams — the future of test prep, 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Education Technology · 2026</span>
        <h3>AI-Based Mock Test Generator for Indian Exams</h3>
        <p>AI turns a chapter or PDF into exam-pattern NEET, JEE, UPSC and SSC questions in seconds — paired with educator review. How the generators work, and where test prep is heading.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>16 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":39') == 1
h = h.replace('"numberOfItems":39', '"numberOfItems":40')
parts = re.split(r'(<script type="application/ld\+json">)', h); out=[]; i=0; done=False
while i < len(parts):
    if parts[i]=='<script type="application/ld+json">' and i+1<len(parts) and '"@type":"ItemList"' in parts[i+1]:
        blk=parts[i+1]; blk=re.sub(r'"position":(\d+)', lambda m:'"position":'+str(int(m.group(1))+1), blk)
        assert blk.count('"itemListElement":[')==1
        blk=blk.replace('"itemListElement":[', '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"'+URL+'","name":"'+HEADLINE+'"},',1)
        out.append(parts[i]); out.append(blk); done=True; i+=2; continue
    out.append(parts[i]); i+=1
h=''.join(out); assert done
bp='"blogPost":[\n'; assert h.count(bp)==1
h=h.replace(bp, bp+'      {"@type":"BlogPosting","headline":"'+HEADLINE+'","url":"'+URL+'","datePublished":"'+DATE+'"},\n',1)
for a,b in [('39 guides · By the founder','40 guides · By the founder'),('39 published · Newest first','40 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems40=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":40' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: cross-folder counts (All 75 / English 61) ----------
PUB = {'blogs/index.html': N_ALL, 'blogs/en/index.html': N_ENGLISH, 'blogs/hi/index.html': N_HI, 'blogs/hinglish/index.html': N_HING}
for f, pub in PUB.items():
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'(All <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ALL, s)
    s=re.sub(r'(English <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ENGLISH, s)
    s=re.sub(r'(Hinglish <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HING, s)
    s=re.sub(r'(हिन्दी</span> <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HI, s)
    s=re.sub(r'\d+( guides · By the founder)', r'%d\1'%N_ALL, s)
    s=re.sub(r'\d+( guides · All languages)', r'%d\1'%N_ALL, s)
    s=re.sub(r'\d+( published · Newest first)', r'%d\1'%pub, s)
    open(f,'w',encoding='utf-8',newline='').write(s)
print('chips updated -> All %d / English %d / Hinglish %d / Hindi %d' % (N_ALL,N_ENGLISH,N_HING,N_HI))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>AI-Based Mock Test Generator for Indian Exams — How AI Is Rewiring Test Prep (2026 Tech Focus)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [AI-Based Mock Test Generator for Indian Exams (2026 Tech-Focus Guide)](''' + URL + '''): A founder-written 2026 tech-focus guide answering "ai based mock test generator for indian exams" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step generate-a-mock workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Test Portal as an AI mock test generator with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Educational technology, Test preparation, Generative artificial intelligence, Multiple choice and Computerized adaptive testing, plus mentions of AllCoaching Educator Studio, NEET, the Joint Entrance Examination, the Union Public Service Commission and the Staff Selection Commission. Core reframe — in Indian test prep the scarce resource was never the questions but the educator's hours spent writing them; an AI mock test generator creates exam-pattern multiple-choice questions automatically from a chapter, PDF or topic outline, so the bottleneck (authoring, not delivery) is removed. The arithmetic — a single good MCQ takes 5-10 minutes to write, a NEET mock is 180 questions, a serious series is 40 mocks a cycle, so authoring throughput, not teaching, is the ceiling most independent educators hit. What the AI actually does (five bounded jobs) — question generation from source, distractor calibration (options plausibly wrong not obviously wrong), difficulty estimation from past-attempt data, per-student weakness detection, and next-test recommendation — while the educator still owns what to test, key accuracy and exam-worthiness. The honest limit, stated repeatedly — AI accelerates authoring roughly 10-20x (minutes per question to seconds) but is PAIRED WITH EDUCATOR REVIEW; it is an accelerant with a human quality gate, NOT a replacement for the teacher and NOT an autopilot that ships a finished exam; anyone promising correct questions with no review is overselling. Why Indian exams fit best — the format is overwhelmingly objective (NEET, JEE, SSC, banking, CTET, most state PSC prelims are four-option MCQ with fixed marking), the volume demanded is enormous, and the pattern (negative marking, section weighting, fixed timing, difficulty band) is strict, so a generator that knows the exam pattern produces exam-shaped drafts; descriptive papers like UPSC Mains are only partly served (assistant, not examiner). Beyond generation — a question is not a test and a test is not test prep: the full test portal auto-grades with instant score and all-India rank, applies section-weighted exam-pattern scoring with negative marking, schedules timed attempts with randomized order and full-screen anti-cheat, runs mobile-first with live leaderboards, and produces topic-wise analytics with a per-student weakness map and an AI-recommended next test; a comparison table contrasts "AI generator alone" (questions only) vs "generator + test portal" (delivered, graded, ranked, analysed, discoverable). The future, marked explicitly as emerging not shipped — computerized adaptive testing for the mass market (a mock that changes difficulty mid-attempt), which today's loop (generate, attempt, analyse, recommend next test) approximates between tests; mid-attempt adaptive difficulty is the trajectory, not a current feature. Economics — capabilities that a decade ago were enterprise software sold for lakhs are now default infrastructure free to an individual educator; on AllCoaching the AI mock test generator and full test portal are included in the FREE base tier (no upfront fee, no per-test charge), the platform earns only a 10% revenue-share on paid earnings and the educator keeps 90% with daily payouts, plus AI-driven marketplace discovery so generated mocks get found, not just made. Honest discipline — no DRM/anti-piracy/watermarking or GST-invoicing claimed; the only quantified claim is the established 10-20x authoring speed-up; adaptive difficulty kept as future. Internal links to /blog/how-to-create-interactive-mock-tests-online, /blog/best-app-for-state-psc-coaching-educators, /blog/online-platform-for-ctet-coaching-teachers, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blogs/en/role-of-ai-in-personalized-learning-for-coaching, /blogs/en/using-generative-ai-for-automated-quiz-creation, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/best-zero-commission-teaching-platform-india. Glossary terms — AI Mock Test Generator, Distractor Calibration, Difficulty Estimation, Auto-Grading, Exam-Pattern Scoring, Topic-Wise Analytics, Adaptive Testing, Item Bank. Author Amit Ratan with 6-entry sameAs. Target keyword "ai based mock test generator for indian exams" ~11,000/mo (KD ~38). Audience targets Indian coaching educators and institutes building mock test series for competitive exams in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
