import re, glob, os

SLUG = 'spayee-learnyst-alternative-india'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Spayee & Learnyst Alternative in India — The LMS Sells You Tools, Not Students (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'exly-rigi-alternative-for-coaches'
NI_OLD, NI_NEW = 46, 47
N_ALL_EXPECT = 89
CARD_TAG = 'Comparison · 2026'
CARD_H3 = 'Spayee &amp; Learnyst Alternative in India'
CARD_ALT = 'Spayee and Learnyst alternative in India — 2026 honest comparison'
CARD_P = "A course LMS charges a monthly subscription and brings no students. The alternative keeps the course tools but flips both: pay only when you earn, plus marketplace discovery."
SM_TITLE = 'Spayee and Learnyst Alternative in India (2026 Comparison)'
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
    <!-- Spayee & Learnyst Alternative in India (Jun 10) -->
    <a href="/blog/{SLUG}" class="blog-card" aria-label="Read: Spayee and Learnyst Alternative in India">
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
entry=('''- [Spayee & Learnyst Alternative in India (2026 LMS-vs-Marketplace Comparison)](''' + URL + '''): A founder-written 2026 comparison answering "spayee alternative" / "learnyst alternative" for Indian educators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step switch workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a no-subscription Spayee/Learnyst alternative with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Learning management system, Online tutoring, Educational technology, Software as a service and Monetization, plus mentions of Spayee, Learnyst, AllCoaching Educator Studio and UPI. Core reframe — be precise about what a course LMS actually sells: it sells you TOOLS (a branded website or app, course hosting, content protection, payments) so you can sell your own courses, but it does NOT sell you the two things educators most need and most struggle to provide alone: a pricing model that does not cost you before you earn, and STUDENTS. The post is explicitly fair (credits Spayee and Learnyst as capable Indian course platforms with branded site/app, hosting, content protection and India-friendly payments) and frames the issue as the boundary of a course toolkit, not a defect. The two gaps an LMS leaves — (1) a SUBSCRIPTION before you earn: a fixed monthly or annual fee due whether or not you make a sale, painful for new or seasonal exam-cycle income, so the platform earns while you wait rather than waiting with you; (2) NO students of its own: it gives selling tools but no marketplace or discovery surface, so every learner must come from the educator\\'s own ads and channels ("a well-built shop with no street outside it"). The hidden-cost insight — the subscription is only the smaller half; the larger cost is that an LMS brings no students, so you also pay in money and time to fill it, i.e. you pay TWICE (once for the tools, again to find the people the tools serve). What an educator actually needs (full checklist) — capable course tools (branded app, hosting, live classes, test series, account-bound access), pay only when you earn (revenue-share, no fixed subscription), built-in discovery (a marketplace surfacing new students), and own brand and students; an LMS covers tools and ownership and charges a subscription while leaving aligned-pricing and discovery unsolved. A subscription-LMS-vs-owned-app-on-a-marketplace table (branded app, pricing model, cost in a no-sale month, built-in discovery, test series, payments) shows both give owned course tools and the difference is the pricing model and the discovery. A 6-step switch that keeps courses and adds what is missing — export content, launch a branded app (60 sec, Rs 0, no subscription), rebuild courses and test series, switch on UPI payment-to-access keeping 90% with no fixed fee, migrate students with a launch offer, and turn on marketplace discovery. Economics — the cleanest test is the cost in a no-sale month: a subscription LMS charges regardless (and because it brings no students a slow month can mean paying for tools barely used), pay-as-you-earn costs nothing; AllCoaching is Rs 0 upfront, no monthly subscription on the base tier, 10% revenue-share on paid earnings only, educator keeps 90% with daily INR payouts, discovery included not extra; exact LMS plan fees vary so NO figures are quoted. Discovery is the most consequential difference — an LMS is by design a self-hosted course toolkit that leaves bringing people entirely to you (the structural cause of India edtech app fatigue), and AllCoaching pairs the toolkit with a shared AI-driven marketplace so students searching by exam/subject/language find the educator organically, adding new students without giving up brand or ownership. Honest discipline — does NOT fabricate Spayee/Learnyst subscription prices (describes "a fixed monthly or annual fee", varies), does NOT claim enterprise DRM or forensic watermarking as free features (asserts only login-gated, account-bound access plus automated payment-to-access), asserts the model strictly as Rs 0 upfront + no subscription + 10% platform / 90% educator + daily payouts. Internal links to /blog/affordable-lms-for-independent-educators, /blogs/en/cheapest-lms-for-early-stage-educators, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india, /blog/best-zero-commission-teaching-platform-india, /blog/kajabi-alternative-india-for-educators, /blog/edtech-marketplace-india-app-fatigue. Glossary terms — Course LMS, Subscription Pricing, Revenue-Share Model, Discovery Gap, Branded Coaching App, Automated Access Control, Account-Bound Access, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keywords "spayee alternative", "learnyst alternative". Audience targets Indian educators evaluating a Spayee or Learnyst alternative in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt added:', SLUG in t, '| REGISTRATION OK')
