import re, glob, os

SLUG = 'exly-rigi-alternative-for-coaches'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Exly & Rigi Alternative for Coaches — Monetisation Is Half the Job; Discovery Is the Other (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'unacademy-alternative-for-independent-educators'
NI_OLD, NI_NEW = 45, 46
N_ALL_EXPECT = 88
CARD_TAG = 'Comparison · 2026'
CARD_H3 = 'Exly &amp; Rigi Alternative for Coaches'
CARD_ALT = 'Exly and Rigi alternative for coaches in India — 2026 honest comparison'
CARD_P = "Creator tools monetise the audience you have but bring no new students. The alternative adds structured teaching and marketplace discovery, at Rs 0 upfront."
SM_TITLE = 'Exly and Rigi Alternative for Coaches (2026 Comparison)'
READ = '15 min read'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == NI_NEW and N_ALL == N_ALL_EXPECT, (N_BLOG, N_ALL)

idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + f'''
    <!-- Exly & Rigi Alternative for Coaches (Jun 10) -->
    <a href="/blog/{SLUG}" class="blog-card" aria-label="Read: Exly and Rigi Alternative for Coaches">
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
print('blog/index.html cards=%d' % h.count('class="blog-card"'))

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
entry=('''- [Exly & Rigi Alternative for Coaches (2026 Monetisation-vs-Discovery Comparison)](''' + URL + '''): A founder-written 2026 comparison answering "exly alternative" / "rigi alternative" for Indian coaches and creator-educators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step move workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as an Exly/Rigi alternative with discovery and a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Creator economy, Online tutoring, Educational technology, Unified Payments Interface (UPI) and Monetization, plus mentions of Exly, Rigi, AllCoaching Educator Studio and UPI. Core reframe — separate the TWO jobs of a coaching business: MONETISATION (charging the audience you already have) and DISCOVERY (reaching new students who are not yet followers); Exly and Rigi are built for and good at the first, but discovery is the job that actually decides whether a coaching business grows and is the one a monetisation tool does not address. The post is explicitly fair (credits that for a creator with a following these are well-designed, low-friction tools: link-in-bio storefront, bookings, digital products, India-friendly payments) and frames the issue as the boundary of a tool, not a defect. The gap named in three parts — (1) NO new students: no marketplace or discovery surface, so every buyer comes from the coach\\'s own channels and growth is bounded by the existing following; (2) built for SELLING not TEACHING: oriented to single products, sessions and link-in-bio sales rather than structured courses, live batches with attendance, or test series with ranks; (3) a FIXED cost regardless of sales: many such tools charge a recurring subscription or per-transaction fee (sometimes both), a cost carried whether or not sales grow. What a coach actually needs (full checklist) — monetise the existing audience (kept intact), bring new students (discovery), structured teaching (courses, live batches, test series), and costs that scale with earnings (revenue-share, no fixed subscription); a monetisation tool covers only the first and part of the fourth. A monetisation-tool-vs-coaching-app table (monetise audience, bring new students, structured courses, test series with ranks, pricing model, revenue share) shows the tool is fine to just charge an existing audience while a coaching app on a marketplace is better to GROW. A 6-step move that keeps what works and adds what is missing — list existing products, launch a branded app (60 sec, Rs 0, no fixed subscription), structure courses and test series, switch on UPI payment-to-access keeping 90% with no monthly fee, bring the existing audience via the bio link so monetisation continues uninterrupted, and turn on marketplace discovery for new students. Economics — monetisation tools show a fixed subscription, a per-transaction fee, or both (a cost not always aligned with uneven coach income); AllCoaching is Rs 0 upfront, no fixed subscription, 10% revenue-share on paid earnings only, educator keeps 90% with daily INR payouts and pays nothing in a no-sale month; exact tool plans vary so NO figures are quoted. The decisive difference is DISCOVERY — a monetisation tool by design sells to existing followers so reach equals following and no internal feature changes that (the audience cap is the ceiling), the structural gap behind India edtech app fatigue ("everyone can monetise, almost no one is findable"); AllCoaching keeps the bio-link monetisation AND lists the branded app on a shared AI-driven marketplace so students searching by subject/language discover the coach organically, adding new students who were never followers. Honest discipline — does NOT fabricate Exly/Rigi pricing specifics (describes "subscription or per-transaction fee", varies by plan), does NOT claim DRM/anti-piracy or GST-invoicing as free features, asserts the model strictly as Rs 0 upfront + no fixed subscription + 10% platform / 90% educator + daily payouts. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/instagram-reels-educator-monetization-platform, /blog/kajabi-alternative-india-for-educators, /blog/best-zero-commission-teaching-platform-india. Glossary terms — Creator-Monetisation Tool, Link-in-Bio Selling, Discovery Gap, Structured Coaching, Revenue-Share Model, Branded Coaching App, Automated Access Control, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keywords "exly alternative", "rigi alternative". Audience targets Indian coaches and creator-educators evaluating an Exly or Rigi alternative in 2026. Authored by founder Amit Ratan.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt added:', SLUG in t, '| REGISTRATION OK')
