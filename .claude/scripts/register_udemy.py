import re, glob, os

SLUG = 'udemy-alternative-for-indian-instructors'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Udemy Alternative for Indian Instructors — Keep Your Brand, Students and Pricing (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'kajabi-alternative-india-for-educators'
NI_OLD, NI_NEW = 43, 44
CARD_TAG = 'Comparison · 2026'
CARD_H3 = 'Udemy Alternative for Indian Instructors'
CARD_ALT = 'Udemy alternative for Indian instructors — 2026 honest comparison'
CARD_P = "Udemy gives discovery but owns the student, controls pricing and takes a large cut. Keep your brand, students and pricing — and still get discovered."
SM_TITLE = 'Udemy Alternative for Indian Instructors (2026 Comparison)'
READ = '15 min read'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == NI_NEW and N_ALL == 86, (N_BLOG, N_ALL)

idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + f'''
    <!-- {CARD_H3} (Jun 10) -->
    <a href="/blog/{SLUG}" class="blog-card" aria-label="Read: {CARD_H3}">
      <div class="blog-card-img">
        <img src="{IMG}" alt="{CARD_ALT}" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">{CARD_TAG}</span>
        <h3>{CARD_H3}</h3>
        <p>{CARD_P}</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>{READ}</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count(f'"numberOfItems":{NI_OLD}') == 1
h = h.replace(f'"numberOfItems":{NI_OLD}', f'"numberOfItems":{NI_NEW}')
parts = re.split(r'(<script type="application/ld\+json">)', h); out=[]; i=0; done=False
while i < len(parts):
    if parts[i]=='<script type="application/ld+json">' and i+1<len(parts) and '"@type":"ItemList"' in parts[i+1]:
        blk=parts[i+1]; blk=re.sub(r'"position":(\d+)', lambda m:'"position":'+str(int(m.group(1))+1), blk)
        blk=blk.replace('"itemListElement":[', '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"'+URL+'","name":"'+HEADLINE+'"},',1)
        out.append(parts[i]); out.append(blk); done=True; i+=2; continue
    out.append(parts[i]); i+=1
h=''.join(out); assert done
bp='"blogPost":[\n'; assert h.count(bp)==1
h=h.replace(bp, bp+'      {"@type":"BlogPosting","headline":"'+HEADLINE+'","url":"'+URL+'","datePublished":"'+DATE+'"},\n',1)
for a,b in [(f'{NI_OLD} guides · By the founder',f'{NI_NEW} guides · By the founder'),(f'{NI_OLD} published · Newest first',f'{NI_NEW} published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d' % h.count('class="blog-card"'))

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
print('chips -> All %d / English %d' % (N_ALL,N_ENGLISH))

sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a=f'  <url>\n    <loc>https://allcoaching.in/blog/{PREV}</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>{SM_TITLE}</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap OK:', SLUG in s)

lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
entry=('''- [Udemy Alternative for Indian Instructors (2026 Discovery-vs-Ownership Comparison)](''' + URL + '''): A founder-written 2026 comparison answering "udemy alternative india" / "udemy alternative for instructors" for Indian instructors and course creators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step move workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as an own-your-students Udemy alternative with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Online marketplace, Massive open online course, Online tutoring, Educational technology and Monetization, plus mentions of Udemy, AllCoaching Educator Studio, Razorpay and UPI. Core reframe — a Udemy alternative is about OWNERSHIP, not features; Udemy is NOT a website builder you outgrew, it is a course MARKETPLACE whose core value is discovery (it can put a course in front of a huge audience you did not build), so the real question is what you give up for that discovery and whether the trade still makes sense once you want a durable business rather than one-off sales. The post is explicitly fair to Udemy (credits that it is genuinely good at the hardest thing to bootstrap alone: demand) and frames critique structurally as the terms of a fair exchange, not as accusations. The trade-off named clearly in three parts — (1) you do NOT own the student: a buyer is largely the platform\\'s customer, you generally do not get their direct contact details so you cannot build an ongoing relationship, announce a new course or teach them again off-platform; (2) you do NOT fully control pricing: large marketplaces run frequent deep platform-wide discounts to drive volume, training buyers to expect very low prices and eroding perceived value, with limited instructor say; (3) your brand is secondary: your course is one listing among thousands under the platform\\'s brand. What an instructor actually wants — own your students (data, contact, relationship), set your own price, your brand front and centre, and crucially KEEP DISCOVERY (the catch most "leave the marketplace" advice ignores, because a self-hosted course loses discovery). A Udemy-vs-AllCoaching table on business-building dimensions (discovery, student ownership, pricing control, branding, revenue split, payments) shows Udemy wins on instant traffic for a creator with no audience while an owned app on a marketplace wins on building a durable business and still being discoverable. A 6-step move — export your content (it is yours), launch a branded app (60 sec, Rs 0, your brand front and centre), rebuild and price the course yourself, switch on UPI payment-to-access settled in INR with daily payouts keeping 90%, bring your own audience so the student becomes yours, and turn on marketplace discovery to recover what a self-hosted course loses. Economics — two numbers decide it: how much of each sale you keep and how much control over the price; on a marketplace you keep a minority of a discounted number (large cut, especially on platform-promoted sales, and platform-set discounting), on an owned app you keep 90% of a price you control with a 10% revenue-share on paid earnings only, Rs 0 upfront, daily INR payouts; exact marketplace splits vary by channel so NO single figure is quoted. Discovery is the strongest honest argument for staying (a self-hosted course has no discovery, the structural cause of India edtech app fatigue), and AllCoaching dissolves the either-or: an owned branded app that is also listed on a shared AI-driven marketplace, so you are found like a listing and own like a business. Honest discipline — does NOT fabricate Udemy commission percentages (describes "a large cut", varies by channel), does NOT claim DRM/anti-piracy or GST-invoicing as free features, asserts the model strictly as Rs 0 upfront + 10% platform / 90% educator + own pricing + daily payouts. Internal links to /blog/kajabi-alternative-india-for-educators, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/white-label-coaching-app-development-cost-india, /blog/best-zero-commission-teaching-platform-india, /blog/edtech-marketplace-india-app-fatigue. Glossary terms — Course Marketplace, Student Ownership, Price Control, Revenue-Share Model, Branded Coaching App, UPI Checkout, Automated Access Control, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "udemy alternative india". Audience targets Indian instructors and course creators evaluating a Udemy alternative in 2026. Authored by founder Amit Ratan.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt added:', SLUG in t, '| REGISTRATION OK')
