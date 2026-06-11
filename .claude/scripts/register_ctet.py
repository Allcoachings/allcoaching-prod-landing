import re, glob

SLUG = 'online-platform-for-ctet-coaching-teachers'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Online Platform for CTET Coaching Teachers — Why Recorded Batches Win This Exam Niche (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-05'

# ---- true counts (this post's file already exists on disk) ----
def posts(d): return len([f for f in glob.glob(d+'/*.html') if not f.replace('\\','/').endswith('/index.html')])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 34 and N_ALL == 68, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Online Platform for CTET Coaching Teachers (Jun 5) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Online Platform for CTET Coaching Teachers (recorded batches)">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Online platform for CTET coaching teachers — why recorded batches win, 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Exam Niche · 2026</span>
        <h3>Online Platform for CTET Coaching Teachers</h3>
        <p>The best CTET platform lets you record an evergreen batch once and sell it across every cycle — recorded-first, with a PYQ test series and discovery, at ₹0 upfront.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>15 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":33') == 1
h = h.replace('"numberOfItems":33', '"numberOfItems":34')
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
for a,b in [('33 guides · By the founder','34 guides · By the founder'),('33 published · Newest first','34 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems34=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":34' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: keep cross-folder counts correct (All 68 / English 55) ----------
PUB = {'blogs/index.html': N_ALL, 'blogs/en/index.html': N_ENGLISH, 'blogs/hi/index.html': N_HI, 'blogs/hinglish/index.html': N_HING}
for f, pub in PUB.items():
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'(All <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ALL, s)
    s=re.sub(r'(English <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ENGLISH, s)
    s=re.sub(r'(Hinglish <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HING, s)
    s=re.sub(r'(हिन्दी</span> <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HI, s)
    s=re.sub(r'\d+( guides · By the founder)', r'%d\1'%N_ALL, s)
    s=re.sub(r'\d+( published · Newest first)', r'%d\1'%pub, s)
    open(f,'w',encoding='utf-8',newline='').write(s)
print('chips updated on 4 blogs/* files -> All %d / English %d / Hinglish %d' % (N_ALL,N_ENGLISH,N_HING))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Online Platform for CTET Coaching Teachers — Why Recorded Batches Win (2026)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Online Platform for CTET Coaching Teachers (2026 Guide — Why Recorded Batches Win)](''' + URL + '''): A founder-written 2026 guide answering "what is the best online platform for CTET coaching teachers" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step recorded-first setup, FAQPage with 10 Q/A, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a CTET platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, two first-person Experience signals, and entity anchoring via Wikipedia sameAs for Teacher Eligibility Test, Pedagogy, Online tutoring and Test preparation, plus mentions of the Central Board of Secondary Education (CBSE), Educational technology and Online marketplace. Core reframe — the best platform for a CTET teacher is not the one with the flashiest live classes but the one that lets you build recorded batches that sell across every CTET cycle and brings aspirants who are already searching for the exam. CTET (Central Teacher Eligibility Test, conducted by CBSE for teachers of classes I-VIII, Paper 1 and Paper 2) is uniquely suited to recorded content because of three structural traits: its Child Development and Pedagogy (CDP) core syllabus is evergreen and barely changes, the exam runs in cycles roughly twice a year, and most aspirants are working people, college or B.Ed students who study asynchronously. Therefore recorded batches are the highest-leverage product: record the evergreen syllabus once, sell to each new cohort every cycle, and decouple income from live teaching hours (one recording sells to unlimited aspirants). Recorded vs live for CTET — recorded is the backbone (the stable syllabus, studied at the aspirant's pace), live is the supplement (weekly doubt-solving, pre-exam strategy near the cycle); a live-only platform forces re-teaching the same content each cycle, caps income at live hours, and leaves between-cycle searchers with nothing to buy. What a CTET platform must support — recorded batch hosting, a PYQ-based mock test series for Paper 1 and Paper 2 (the most-bought product after the batch, needs an auto-grading engine with ranks), structured CDP and subject courses, Hindi and English content, optional live doubt classes, student access and CRM, and — most important — discovery; a plain video host limits the educator to the least differentiated product. Discovery is the decisive factor: hosting a recording is storage, not distribution; a standalone app/website starts with zero aspirants, whereas AllCoaching's AI marketplace has already aggregated CTET searchers and matches them by Paper, subject and language to the recorded batch, and re-surfaces it to each new cycle's wave of aspirants with no ad budget. 6-step setup — pick your CTET niche (paper, subject, language), launch a free branded studio (₹0), record one evergreen batch, add a PYQ mock test series, switch on marketplace discovery, and refresh lightly each cycle so the recording compounds. Economics — work is front-loaded once and revenue recurs; a price-sensitive high-volume CTET audience cannot support a several-lakh white-label fee or heavy subscription, so AllCoaching is ₹0 upfront, no subscription on the free tier, a 10% revenue-share on paid earnings only, educator keeps 90% with daily payouts (custom domain and advanced analytics are paid-tier). Honest hedges — recorded is the backbone but live still matters; a modest phone-and-mic recording setup is enough (clarity beats polish); no fabricated statistics (cycle frequency and aspirant profile stated qualitatively). Internal links to /blog/best-app-for-state-psc-coaching-educators, /blog/how-to-create-interactive-mock-tests-online, /blog/best-free-tools-for-teachers-to-record-lectures, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/how-to-teach-ssc-online-and-earn-money-india, /blog/sell-online-courses-without-monthly-subscription. Glossary — CTET, Recorded Batch, Child Development and Pedagogy (CDP), PYQ Test Series, Evergreen Content, Marketplace Discovery, Branded Studio, Revenue Share Model. Author Amit Ratan with 6-entry sameAs. Target keyword "online platform for ctet coaching teachers" ~9,000/mo (KD ~31). Audience targets Indian educators teaching CTET and TET aspirants online in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
