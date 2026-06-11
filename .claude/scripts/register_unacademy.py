import re, glob, os

SLUG = 'unacademy-alternative-for-independent-educators'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Unacademy Alternative for Independent Educators — Own Your Brand, Not Just Teach on One (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'udemy-alternative-for-indian-instructors'
NI_OLD, NI_NEW = 44, 45
CARD_TAG = 'Comparison · 2026'
CARD_H3 = 'Unacademy Alternative for Independent Educators'
CARD_ALT = 'Unacademy alternative for independent educators in India — 2026 honest comparison'
CARD_P = "On a large platform you teach under its brand and terms. Own your brand, students and pricing — and still get discovered through a marketplace."
SM_TITLE = 'Unacademy Alternative for Independent Educators (2026 Comparison)'
READ = '15 min read'
N_ALL_EXPECT = 87

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == NI_NEW and N_ALL == N_ALL_EXPECT, (N_BLOG, N_ALL)

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
entry=('''- [Unacademy Alternative for Independent Educators (2026 Own-Your-Brand Comparison)](''' + URL + '''): A founder-written 2026 comparison answering "unacademy alternative" / "unacademy alternative for educators" for independent Indian educators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step start-your-own workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a be-your-own-platform Unacademy alternative with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Educational technology, Online tutoring, Distance education, Brand and Monetization, plus mentions of Unacademy, AllCoaching Educator Studio, Razorpay and UPI. Core reframe — an Unacademy alternative is about OWNERSHIP, not features; Unacademy is NOT a tool you outgrew, it is a large edtech platform whose core offer is reach and production (it can put a capable educator in front of a huge audience with polish), so the real choice is "teach on a brand, or own one" and whose brand and business you build when you teach on it. The post is explicitly fair to Unacademy (credits real scale, production and an established student base, the things hardest to build alone) and frames critique structurally as the terms of a fair exchange, not hostilely. The ownership trade-off named in three parts — (1) you build the PLATFORM\\'s brand: classes carry the platform\\'s name, recognition you build stays behind if you leave; (2) the students are the platform\\'s: learners are its customers, your relationship is mediated, you generally cannot reach them directly to launch something new; (3) pricing and packaging are not yours: how your teaching is sold, bundled and priced is the platform\\'s decision and your income follows its terms. What an independent educator actually wants — your own brand (recognition you keep), your own students (a relationship you can serve for years), your own pricing (your value on your terms), and crucially KEEP THE REACH (the catch most "go independent" advice ignores, because a lone app has no reach). A teach-on-a-platform-vs-own-your-own table (reach/discovery, brand, student ownership, pricing, revenue, independence) shows a large platform wins on instant reach and production while an owned app on a marketplace wins on building an independent durable business and still being discoverable. A 6-step start-your-own — define your own positioning (your name and angle, not a catalogue slot), launch a branded app (60 sec, Rs 0, your brand front and centre), structure your course and test series under your brand, switch on UPI payment-to-access settled in INR with daily payouts keeping 90% and your own price, bring your YouTube/Telegram/Instagram following so students become yours, and turn on marketplace discovery to point a platform-scale reach at your own brand. Economics — on a large platform earnings follow the platform\\'s model (contract, share or platform-set pricing) and the brand value accrues to it; on an owned app you set your own price, keep 90% (10% revenue-share on paid earnings only), are paid daily in INR, and every student and bit of recognition is yours; exact platform arrangements vary so NO figure is quoted. Reach is the strongest honest argument for staying (an independent app with no discovery can be invisible, the structural cause of India edtech app fatigue), and AllCoaching removes the either-or: an owned branded app that is also on a shared AI-driven marketplace, so reach is now pointed at the educator\\'s own name. The lasting-brand test — if the platform changed terms tomorrow, could you take your students with you? On a large platform usually not; a brand you own is one where students follow your name and you can reach them directly. Honest discipline — does NOT fabricate Unacademy contract/commission specifics (describes "the platform\\'s model and terms"), does NOT claim DRM/anti-piracy or GST-invoicing as free features, asserts the model strictly as Rs 0 upfront + own brand/students/pricing + 10% platform / 90% educator + daily payouts. Internal links to /blogs/en/why-educators-are-leaving-subscription-platforms, /blog/udemy-alternative-for-indian-instructors, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/white-label-coaching-app-development-cost-india, /blog/best-zero-commission-teaching-platform-india, /blog/edtech-marketplace-india-app-fatigue. Glossary terms — Large Edtech Platform, Brand Ownership, Student Ownership, Price Control, Revenue-Share Model, Branded Coaching App, Educator Independence, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "unacademy alternative". Audience targets independent Indian educators evaluating an Unacademy alternative in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt added:', SLUG in t, '| REGISTRATION OK')
