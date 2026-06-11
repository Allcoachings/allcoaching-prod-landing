import re, glob

SLUG = 'how-to-record-upsc-lectures-and-sell-online'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'How to Record UPSC Lectures and Sell Online — The Tools and Workflow for High-Quality Recording (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-06'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if not f.replace('\\','/').endswith('/index.html')])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 37 and N_ALL == 71, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- How to Record UPSC Lectures and Sell Online (Jun 6) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: How to Record UPSC Lectures and Sell Online">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="How to record UPSC lectures and sell online — the 2026 recording workflow for educators" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Tools &amp; Workflow · 2026</span>
        <h3>How to Record UPSC Lectures and Sell Online</h3>
        <p>The gear, audio and screen-recording workflow to produce high-quality UPSC lectures — then host and sell them access-controlled at ₹0, keeping 90% of revenue.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>17 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":36') == 1
h = h.replace('"numberOfItems":36', '"numberOfItems":37')
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
for a,b in [('36 guides · By the founder','37 guides · By the founder'),('36 published · Newest first','37 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems37=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":37' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: cross-folder counts (All 71 / English 58) ----------
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
print('chips updated -> All %d / English %d / Hinglish %d' % (N_ALL,N_ENGLISH,N_HING))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>How to Record UPSC Lectures and Sell Online — The Tools and Workflow for High-Quality Recording (2026)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [How to Record UPSC Lectures and Sell Online (2026 Tools-and-Workflow Guide)](''' + URL + '''): A founder-written, practical 2026 guide answering "how to record UPSC lectures and sell online" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 8-step record-and-sell workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as ₹0 recorded-lecture hosting with a Free offer, DefinedTermSet with 9 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs. Core thesis — recording quality is decided by audio and legibility, not camera resolution: for UPSC content the aspirant is watching the concept, the timeline, the map or the answer being built, so a clean screen recording with a good mic beats an expensive talking-head camera. The gear that actually matters, cheapest-impact-first — a clip-on lavalier or a USB condenser mic and a quiet room (audio first), a digital writing pad / pen tablet so concepts and answer-writing are built live on screen, optional document camera for handwritten notes, soft front lighting, and a mid-range laptop; a dedicated camera is optional and lowest priority. The recording workflow — OBS Studio (free, no watermark, no time limit) capturing slides, webcam inset, writing pad and document camera as switchable scenes; record in focused modules rather than 3-hour marathons (lecture modularization) so content is reusable, rerecordable and easy for students to navigate; separate evergreen concept lectures (record once, sell across cycles) from current-affairs/dated content (rerecord each cycle). Selling and hosting — the where is access-controlled streaming to a logged-in paying aspirant inside your own branded studio, streamed not downloadable, which removes the easiest leakage; this is explicitly NOT enterprise hardware DRM (a heavier, separate layer most educators do not need), and the honest piracy picture is linked out. AllCoaching positioning grounded in the confirmed free tier — recorded-lecture and course hosting at ₹0 with no per-GB storage fee and no per-view bandwidth bill, CDN-backed delivery and adaptive bitrate streaming for smooth mobile playback on Indian networks, branded studio behind a student login, UPI/card payments with daily payouts, student CRM, and AI-driven marketplace discovery; the platform earns only a 10% revenue-share on paid earnings, educator keeps 90%; paid tier (custom domain, advanced analytics, priority support) noted; conservative on infra specifics, no fabricated statistics. Distribution-first close — once recording and hosting cost the educator ₹0, the scarce lever is discovery, which a marketplace supplies by matching aspirants searching the subject to the studio. Internal links to /blog/best-free-tools-for-teachers-to-record-lectures, /blog/recorded-lecture-hosting-cheap-india-for-teachers, /blog/secure-video-hosting-for-educational-content, /blog/video-drm-protection-for-indian-course-creators, /blog/best-app-for-state-psc-coaching-educators, /blog/online-platform-for-ctet-coaching-teachers, /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/best-zero-commission-teaching-platform-india, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary — Lavalier Microphone, Digital Writing Pad, Screen Recording, Adaptive Bitrate Streaming, Access-Controlled Streaming, Bitrate, Lecture Modularization, Evergreen vs Current-Affairs Content, Revenue-Share Model. Author Amit Ratan with 6-entry sameAs. Target keyword "how to record upsc lectures and sell online"; audience targets Indian UPSC and civil-services educators recording and selling video lectures online in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
