import re, glob, os

SLUG = 'online-jee-coaching-platform-for-teachers'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Online JEE Coaching Platform for Teachers — How to Choose, and Start, in 2026'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 41 and N_ALL == 81, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Online JEE Coaching Platform for Teachers (Jun 10) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Online JEE Coaching Platform for Teachers">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Online JEE coaching platform for teachers in India — 2026 guide for independent educators" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Start &amp; Earn · 2026</span>
        <h3>Online JEE Coaching Platform for Teachers</h3>
        <p>The best JEE platform isn't the one with the most features — it's the one that solves structure and distribution. What a JEE app must do, the own-app vs marketplace call, and a 6-step start.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>15 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":40') == 1
h = h.replace('"numberOfItems":40', '"numberOfItems":41')
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
for a,b in [('40 guides · By the founder','41 guides · By the founder'),('40 published · Newest first','41 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems41=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":41' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: cross-folder counts ----------
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
a='  <url>\n    <loc>https://allcoaching.in/blog/ai-based-mock-test-generator-for-indian-exams</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Online JEE Coaching Platform for Teachers (2026 Guide)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Online JEE Coaching Platform for Teachers (2026 Choose-and-Start Guide)](''' + URL + '''): A founder-written 2026 guide answering "online jee coaching platform for teachers" for independent JEE Physics, Chemistry and Maths teachers — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step setup workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as an online JEE coaching platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for the Joint Entrance Examination, the Indian Institutes of Technology (IIT), Online tutoring, Educational technology and Monetization, plus mentions of AllCoaching Educator Studio, the Joint Entrance Examination, Razorpay and UPI. Core reframe — the platform question is the wrong question; the best platform for an independent JEE teacher is NOT the one with the most features (video hosting, a payment button, a quiz tool are commodities in 2026) but the one that solves the two things a solo educator cannot solve alone: STRUCTURE (turning a problem-solving subject into a coherent paid study path) and DISTRIBUTION (getting that path in front of aspirants). What a JEE platform must actually do is six capabilities, and a platform that misses the back four is "a video host wearing a coaching badge" — live classes plus recorded PCM lessons, topic-wise problem sets, ranked test series and PYQ with negative marking and all-India rank, structured doubt-solving, automated payment-to-access, and discovery for new aspirants. Why JEE specifically needs more than a video host — the Joint Entrance Examination tests Physics, Chemistry and Maths through multi-concept numerical problem-solving and splits into JEE Main and the harder JEE Advanced for the IITs, so a student cracks it by solving thousands of problems under exam conditions, which demands a path (concept to worked example to graded problem set to full mock with a rank to targeted revision), not a flat playlist. Platform decision named with trade-offs — YouTube (reach but no paid structure, access control or ownership; rented audience, ad-shaped revenue), a custom-built app (ownership but roughly Rs 4-11 lakh year-one, months, and NO discovery of its own so every student is bought through ads), versus an educator MARKETPLACE (owned branded app PLUS shared AI-driven discovery at Rs 0 upfront) — decisive for JEE because aspirants search exam-specifically (e.g. "JEE Physics online", "JEE Advanced test series"). A 6-step setup — decide subject and target (Main, Advanced, droppers) with narrow positioning, launch a branded app (60 sec, Rs 0), structure PCM content into a course, ADD problem sets and ranked test series with PYQ, switch on payments to automate access, and turn on marketplace discovery. Offering advice — go beyond lectures (free explanations flood YouTube); the value and consistent revenue are in the practice layer the exam rewards (problem sets, ranked mocks, PYQ, doubt-solving), and ranked test series often earn more than lectures because aspirants return every cycle to measure against an all-India rank; a platform makes test series manageable because auto-evaluation, exam-pattern scoring and ranking are handled by the system. Automation core — payment IS the access event (UPI/card/net-banking checkout grants instant access, auto-expires on lapse, no manual collection). Economics are honest and NON-fabricated — earnings depend on student count, price and offering completeness so NO guaranteed figure is given; the model is educator sets price, keeps 90% (10% revenue-share on paid earnings only) with daily payouts, start-up Rs 0 upfront versus a custom build's Year-1 Rs 4-11 lakh. Discovery answer — a standalone app has no discovery of its own (India's edtech app fatigue), so AllCoaching's AI-driven marketplace surfaces the educator when an aspirant searches and brings new paid students who never knew the name; the post does NOT claim DRM/anti-piracy or GST-invoicing as free features. Internal links to /blog/how-to-start-online-academy-in-5-steps, /blog/how-to-create-interactive-mock-tests-online, /blog/ai-based-mock-test-generator-for-indian-exams, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india, /blog/online-coaching-academy-without-coding, /blog/how-to-conduct-live-classes-on-mobile-apps, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/edtech-marketplace-india-app-fatigue. Glossary terms — JEE Main, JEE Advanced, Problem Set, Test Series, Doubt-Solving, Branded Coaching App, Revenue-Share Model, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "online jee coaching platform for teachers"; Hinglish companion is /blogs/hinglish/neet-coaching-online-kaise-shuru-kare. Audience targets independent JEE Physics, Chemistry and Maths teachers and mentors starting an online coaching in India in 2026. Authored by founder Amit Ratan.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
