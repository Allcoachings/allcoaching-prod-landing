import re, glob, os

SLUG = 'multi-teacher-coaching-platform-rev-share'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Multi-Teacher Coaching Platform on Revenue Share — The Economics for Institutes With 5+ Teachers (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-09'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 39 and N_ALL == 74, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Multi-Teacher Coaching Platform on Revenue Share (Jun 9) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Multi-Teacher Coaching Platform on Revenue Share">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Multi-teacher coaching platform on revenue share — economics for institutes with 5+ teachers, 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Platform Economics · 2026</span>
        <h3>Multi-Teacher Coaching Platform on Revenue Share</h3>
        <p>For an institute with 5+ teachers, the pricing model is the decision. Revenue share charges ₹0 upfront and 10% on earnings — keep 90%, add teachers free, and let a marketplace find students per teacher.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>16 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":38') == 1
h = h.replace('"numberOfItems":38', '"numberOfItems":39')
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
for a,b in [('38 guides · By the founder','39 guides · By the founder'),('38 published · Newest first','39 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems39=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":39' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: cross-folder counts (All 74 / English 60) ----------
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
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Multi-Teacher Coaching Platform on Revenue Share — The Economics for Institutes With 5+ Teachers (2026)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Multi-Teacher Coaching Platform on Revenue Share (2026 Institute-Economics Guide)](''' + URL + '''): A founder-written 2026 analysis answering "multi teacher coaching platform rev share" for owners of Indian coaching institutes with five or more teachers — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step institute setup, FAQPage with 11 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a multi-teacher institute platform with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Online tutoring, Revenue sharing, Educational technology, Software as a service and Business model, plus mentions of AllCoaching Educator Studio, Learning management system, UPI and Razorpay. Core reframe — at one teacher the platform is a tooling choice, but at five-plus teachers it is an economics choice, because whatever the platform charges is now multiplied across the whole faculty and stretched through every slow season; features have converged across platforms, so the deciding variable is the pricing model, not the feature list. Central contrast — a subscription platform charges a fixed recurring fee (often per-seat, rising with teacher count) owed whether or not teachers earn, carried through every new teacher's ramp-up and every quiet pre-exam month; a revenue-share platform charges nothing upfront and only a share of actual paid earnings, so the platform earns when the institute earns and adding a non-earning teacher costs the institute zero. A subscription sells capacity (paid for whether used or not); a revenue-share sells outcomes (owed only against money already collected). How the split actually works on AllCoaching — the revenue-share is between the platform and the INSTITUTE: the platform takes a 10% share on paid earnings and the institute keeps 90%, settled daily; how the institute then divides its 90% among individual teachers is the institute's OWN internal arrangement (salary, percentage, per-batch deal). The platform does NOT impose or automate an owner-to-teacher split — that is explicitly stated, so institutes keep full control of faculty economics; there is no automated per-teacher payout feature claimed. Multi-teacher institute support is included on the FREE base tier — one branded white-label studio with separate teacher logins, individual content management and batch ownership under a single institute brand, at ₹0 upfront with no per-teacher subscription (custom domain, advanced analytics and priority support are paid-tier). The 6-step setup — launch the institute's branded studio at ₹0, add each teacher with a separate login, let each teacher own their batches/courses/recorded lessons/test series, set prices and take UPI/card payments with daily payouts, keep 90% and settle internal teacher payments yourself, switch on marketplace discovery per subject. The ramp-up argument — a per-seat subscription bills a new teacher's seat from day one while their first batch is still being built, taxing growth; a revenue-share model charges ₹0 until that teacher makes a sale, so an institute can expand faculty on teaching potential rather than budget. Distribution-first close — at institute scale the tooling is commoditised but discovery is not; a standalone app markets only the institute and leaves individual teachers invisible, while AllCoaching's AI marketplace matches students searching by exam, subject or language to the right teacher within the institute, adding a merit-based discovery engine that does not depend on the institute's ad budget. Honest discipline — no fabricated statistics (Year-1 white-label cost given only as the established "several lakh" range with a link to the full breakdown); does NOT claim video DRM, anti-piracy watermarking or GST-invoicing as free features; the model asserted is strictly ₹0 upfront + 10% platform / 90% institute + daily payouts + multi-teacher free-tier-included. Internal links to /blog/best-zero-commission-teaching-platform-india, /blog/sell-online-courses-without-monthly-subscription, /blog/white-label-coaching-app-development-cost-india, /blog/online-coaching-academy-without-coding, /blog/automated-fee-management-software-for-teachers, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, plus related cards to /blog/classplus-vs-graphy-vs-allcoaching. Glossary terms — Revenue-Share Model, Subscription Model, Multi-Teacher Institute Support, Per-Seat Pricing, Batch Ownership, Institute-Managed Revenue Split, Daily Payout, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "multi teacher coaching platform rev share" ~4,800/mo (KD ~25). Audience targets owners of Indian coaching institutes with multiple teachers choosing a revenue-share platform in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
