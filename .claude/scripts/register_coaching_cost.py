import re, glob, os

SLUG = 'coaching-app-banane-me-kitna-paisa-lagta-hai'
URL = f'https://allcoaching.in/blogs/hinglish/{SLUG}'
HEADLINE = 'Coaching Ka App Banane Me Kitna Paisa Lagta Hai — Server Vs Dev Cost Ka Honest Breakdown (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-09'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_HING == 15 and N_ALL == 76, (N_HING, N_ALL)

# ---------- blogs/hinglish/index.html: card + blogPost[] ----------
idx = 'blogs/hinglish/index.html'; h = open(idx, encoding='utf-8').read()
tg_card = '    <a href="/blogs/hinglish/telegram-channel-se-paid-app-kaise-jaye" class="blog-card"'
assert h.count(tg_card) == 1, 'telegram card anchor'
card = '''    <a href="/blogs/hinglish/''' + SLUG + '''" class="blog-card" aria-label="Read: Coaching App Banane Me Kitna Paisa Lagta Hai (2026)" hreflang="hi-Latn">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Coaching App Banane Me Kitna Paisa Lagta Hai — 2026 cost breakdown (Hinglish)" loading="lazy" width="1600" height="900" decoding="async" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Cost Analysis · 2026</span>
        <h3>Coaching App Banane Me Kitna Paisa Lagta Hai (2026)</h3>
        <p>Dev cost sirf headline number hai — asli kharcha server, maintenance aur recurring costs me chhupa hota hai. Teen routes ka honest breakdown, aur ₹0 upfront ka alternative.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span>
          <span class="dot"></span><span>15 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>

'''
h = h.replace(tg_card, card + tg_card, 1)
bp_anchor = '"blogPost":[{"@type":"BlogPosting","headline":"Telegram Channel Se Paid App'
assert h.count(bp_anchor) == 1, 'blogPost anchor'
bp_new = '"blogPost":[{"@type":"BlogPosting","headline":"' + HEADLINE + '","url":"' + URL + '","datePublished":"' + DATE + '","inLanguage":"hi-Latn"},{"@type":"BlogPosting","headline":"Telegram Channel Se Paid App'
h = h.replace(bp_anchor, bp_new, 1)
open(idx, 'w', encoding='utf-8', newline='').write(h)
print('hinglish index: cards=%d blogPost=%d telegram-before-mine=%s' % (h.count('class="blog-card"'), h.count('"@type":"BlogPosting"'), h.find(SLUG) < h.find('telegram-channel-se-paid-app-kaise-jaye')))

# ---------- 4 blogs/* index files: cross-folder counts (All 76 / English 61 / Hinglish 15) ----------
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

# ---------- sitemap.xml (insert at end of hinglish block, before </urlset>) ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
assert s.count('</urlset>')==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Coaching App Banane Me Kitna Paisa Lagta Hai (2026 Hinglish Cost Breakdown)</image:title>\n    </image:image>\n'
     f'    <xhtml:link rel="alternate" hreflang="hi-Latn" href="{URL}" />\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="https://allcoaching.in/blog/white-label-coaching-app-development-cost-india" />\n  </url>\n')
s=s.replace('</urlset>', blk+'</urlset>', 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Coaching App Banane Me Kitna Paisa Lagta Hai (2026 Hinglish Cost-Transparency Guide)](''' + URL + '''): A founder-written Hinglish (Latin-script Hindi) cost-breakdown guide answering "coaching ka app banane me kitna paisa lagta hai" for Indian educators in 2026 — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step true-cost workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a Rs 0-upfront coaching app with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Mobile app development, Online tutoring, Cloud computing, Total cost of ownership and Software as a service, plus mentions of AllCoaching Educator Studio, Content delivery network, Razorpay and Google Play. Core reframe — "kitna paisa lagta hai" ka asli jawab ek number nahi hai; app ek product nahi balki an ongoing service hai, so the real question is the TOTAL cost of a chosen route (build + run + bring students), not the dev quote. The central insight — DEV COST (one-time design + code) is only the headline number a vendor shows first; the real cost hides in SERVER/HOSTING (recurring, and it GROWS with students and video, so the more successful you are the bigger the bill), maintenance, payment-gateway fees, app-store fees, security and lock-in. The server-vs-dev distinction explained — dev cost is a one-time bridge, server cost is the per-vehicle toll on that bridge; video bandwidth is the worst offender because a one-hour HD lecture watched by 500 students is massive per-GB delivery, pushing hosting to Rs 20,000-30,000+/month at scale, invisible in the dev quote. Three routes with established (non-fabricated) ranges — DIY/freelancer (Rs 50,000-3 lakh upfront but breaks at scale, hosting/maintenance fall on the educator), white-label/agency (Year-1 Rs 4-11 lakh with setup + subscription + fees + high lock-in), big custom build (Rs 15 lakh to crores), and a ready platform (Rs 0 upfront). True Year-1 math table contrasts dev/setup, server, maintenance, lock-in, Year-1 total and discovery across the three routes. The one-time-cost myth — "ek baar paisa do, app ban jaata hai" is the most dangerous misconception; an app is a living system needing hosting, updates, security and OS-compatibility forever, so its cost model must be ongoing, which is exactly what a revenue-share reframes. The Rs 0 route — on AllCoaching a branded coaching app (web + Android + iOS) launches at Rs 0 upfront with no dev cost, no hosting bill, no maintenance; the platform takes a 10% revenue-share on paid earnings only and the educator keeps 90% with daily payouts, while hosting/bandwidth/updates/security/scaling are all managed platform-side, so the recurring costs that break the DIY route never reach the educator (custom domain and advanced analytics are paid-tier). The biggest hidden cost — discovery: a standalone app has no discovery of its own, so bringing students means paid ads (expensive per student, ongoing), whereas AllCoaching's AI-driven marketplace surfaces the educator on exam/subject/language search for free, the structural alternative to ad spend; any honest app-cost calculation must include the cost of getting found. Honest discipline — figures are established ranges, not fabricated; no DRM/anti-piracy/watermarking or GST-invoicing claimed as free features; the model asserted is strictly Rs 0 upfront + 10% platform / 90% educator + daily payouts. Internal links to /blog/white-label-coaching-app-development-cost-india, /blogs/hinglish/physics-wallah-jaise-coaching-app-kaise-banaye, /blog/secure-video-hosting-for-educational-content, /blog/recorded-lecture-hosting-cheap-india-for-teachers, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blogs/hinglish/apna-coaching-app-kaise-banaye-free. Glossary terms — Development Cost, Server/Hosting Cost, Bandwidth Cost, Maintenance Cost, White-Label App, Payment Gateway Fee, Total Cost of Ownership (TCO), Revenue-Share Model. Author Amit Ratan with 6-entry sameAs. Target keyword "coaching ka app banane me kitna paisa lagta hai" with ~22,000 monthly searches (KD ~48); English companion is /blog/white-label-coaching-app-development-cost-india. Audience targets Indian coaching educators and institutes evaluating the cost of building a coaching app in 2026. Authored by founder Amit Ratan.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
