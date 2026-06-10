import re, glob, os

SLUG = 'kajabi-alternative-india-for-educators'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Kajabi Alternative in India for Educators — An Honest Fit-and-Cost Comparison (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'online-ca-cs-coaching-platform-for-educators'  # sitemap anchor (newest blog/ entry)

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 43 and N_ALL == 85, (N_BLOG, N_ALL)
NI_OLD, NI_NEW = 42, 43

idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Kajabi Alternative in India for Educators (Jun 10) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Kajabi Alternative in India for Educators">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Kajabi alternative in India for educators — 2026 honest comparison" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Comparison · 2026</span>
        <h3>Kajabi Alternative in India for Educators</h3>
        <p>Kajabi is a strong global suite, but its USD subscription, card-first checkout and lack of built-in discovery misalign with Indian educators. The India-fit alternative, honestly compared.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>15 min read</span>
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
        assert blk.count('"itemListElement":[')==1
        blk=blk.replace('"itemListElement":[', '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"'+URL+'","name":"'+HEADLINE+'"},',1)
        out.append(parts[i]); out.append(blk); done=True; i+=2; continue
    out.append(parts[i]); i+=1
h=''.join(out); assert done
bp='"blogPost":[\n'; assert h.count(bp)==1
h=h.replace(bp, bp+'      {"@type":"BlogPosting","headline":"'+HEADLINE+'","url":"'+URL+'","datePublished":"'+DATE+'"},\n',1)
for a,b in [(f'{NI_OLD} guides · By the founder',f'{NI_NEW} guides · By the founder'),(f'{NI_OLD} published · Newest first',f'{NI_NEW} published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":%d'%NI_NEW in h, h.count('"@type":"BlogPosting"')))

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
print('chips -> All %d / English %d / Hinglish %d' % (N_ALL,N_ENGLISH,N_HING))

sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a=f'  <url>\n    <loc>https://allcoaching.in/blog/{PREV}</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Kajabi Alternative in India for Educators (2026 Comparison)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Kajabi Alternative in India for Educators (2026 Honest Fit-and-Cost Comparison)](''' + URL + '''): A founder-written 2026 comparison answering "kajabi alternative india" for Indian educators and course creators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step switch workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as an India-fit Kajabi alternative with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Software as a service, Online tutoring, Educational technology, Unified Payments Interface (UPI) and Monetization, plus mentions of Kajabi, AllCoaching Educator Studio, Razorpay and UPI. Core reframe — a Kajabi alternative is a FIT question, not a feature-parity question; Kajabi is NOT weak, it is a mature, capable global all-in-one creator suite (strong course hosting, funnels, email, website builder), but it is built and priced for a global creator on a USD subscription, so the right test for an Indian educator is "what fits how I earn, get paid and get found in India", not "what matches Kajabi feature for feature". The post is explicitly fair to the incumbent (concedes Kajabi does its job well for its intended audience) and frames critique structurally, not hostilely. Three structural mismatches for Indian educators, about MODEL not quality — (1) USD subscription: a fixed monthly foreign-currency cost owed whether or not you made a sale, which is the opposite of seasonal exam-cycle income; (2) card-first not UPI-first: built for global cards while Indian students overwhelmingly pay by UPI, causing friction and failed payments plus cross-currency payouts; (3) no built-in discovery: like any all-in-one site builder it gives a place to host but no audience, so every student must be bought through ads, the hardest invisible cost for an independent Indian educator. What an Indian educator actually needs (the real checklist) — INR UPI-first checkout and fast INR payouts, zero upfront cost with pay-as-you-earn (revenue-share not a fixed foreign subscription), built-in discovery rather than just hosting, and an owned branded app. A Kajabi-vs-AllCoaching comparison table on India-fit dimensions (pricing model, payments, payouts, branded app, built-in discovery, cost in a no-sale month) shows Kajabi can win a global-features comparison and still lose an India-fit comparison because the two ask different questions. A 6-step switch — export your content from Kajabi (your content is yours), launch a branded app (60 sec, Rs 0, no USD subscription), rebuild the course structure, switch on UPI payment-to-access settled in INR with daily payouts, migrate existing students with a launch offer, and turn on marketplace discovery. Economics — the cleanest test is the cost in a month with no sales: on a subscription you owe the fixed fee regardless, on a revenue-share you pay nothing; AllCoaching is Rs 0 upfront, no subscription on the base tier, 10% revenue-share on paid earnings only, educator keeps 90% with daily INR payouts, no foreign-currency subscription to convert. Discovery is the under-discussed gap a feature comparison never captures — an all-in-one platform brings zero students (every learner arrives via your own ads/email/social), the structural cause of India\\'s edtech app fatigue; AllCoaching\\'s marketplace keeps the owned-app benefit AND adds a shared AI-driven discovery surface so students searching by exam/subject/language find you organically. Honest discipline — does NOT fabricate specific Kajabi prices (describes the model: USD monthly subscription), does NOT claim DRM/anti-piracy or GST-invoicing as free features, and frames the asserted model strictly as Rs 0 upfront + 10% platform / 90% educator + daily payouts. Internal links to /blog/best-zero-commission-teaching-platform-india, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india, /blog/edtech-marketplace-india-app-fatigue. Glossary terms — All-in-One Creator Platform, Subscription Pricing, Revenue-Share Model, UPI Checkout, Branded Coaching App, Student Ownership, Automated Access Control, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "kajabi alternative india". Audience targets Indian educators and course creators evaluating a Kajabi alternative in 2026. Authored by founder Amit Ratan.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
