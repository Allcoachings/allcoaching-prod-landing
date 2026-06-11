import re, glob

SLUG = 'instagram-reels-educator-monetization-platform'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Instagram Reels Educator Monetization Platform — Why the Platform You Monetize on Is Not Instagram (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-06'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if not f.replace('\\','/').endswith('/index.html')])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 38 and N_ALL == 72, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Instagram Reels Educator Monetization Platform (Jun 6) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Instagram Reels Educator Monetization Platform">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Instagram Reels educator monetization platform — funnelling Reels reach into your own app, 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Growth &amp; Distribution · 2026</span>
        <h3>Instagram Reels Educator Monetization Platform</h3>
        <p>Reels are the best free discovery engine in India — but you can't monetize on Instagram. Funnel that reach into your own ₹0 branded app where viewers become paying students you own.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>17 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":37') == 1
h = h.replace('"numberOfItems":37', '"numberOfItems":38')
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
for a,b in [('37 guides · By the founder','38 guides · By the founder'),('37 published · Newest first','38 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems38=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":38' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: cross-folder counts (All 72 / English 59) ----------
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
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Instagram Reels Educator Monetization Platform — Why the Platform You Monetize on Is Not Instagram (2026)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Instagram Reels Educator Monetization Platform (2026 Trend-and-Funnel Guide)](''' + URL + '''): A founder-written 2026 guide answering "instagram reels educator monetization platform" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 8-step Reels-to-sale funnel, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as a ₹0 branded app with a Free offer, DefinedTermSet with 9 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Instagram, Social media marketing, Purchase funnel, Recommender system and Online tutoring, plus mentions of Influencer marketing, Call to action (marketing), Mobile app, Conversion rate optimization, Lead generation and Revenue sharing. Core reframe — an Instagram Reels educator monetization platform is NOT Instagram itself; Instagram is a discovery engine built to keep attention on Instagram, while the platform an educator actually monetizes on must be one they own. The two-layer model — Reels are top-of-funnel discovery (free reach to non-followers via the recommender algorithm), and an owned branded app is the bottom of the funnel where the sale, the student login, the content and the repeat purchase live; the educator's whole job is moving a viewer cleanly from layer one to layer two, with the link-in-bio and the call to action as the bridge. The rented-audience trap — followers are a number on a profile you do not control, with no native course player, no access control, one bio link for the whole catalogue, no student data you keep, and platform risk (shadowban or ban) that can erase reach and income overnight. What a real monetization platform must do that Instagram cannot — host structured courses behind a student login, take UPI and card payments natively, keep the audience data you own, support live classes, recorded lectures, test series and PDF notes, and let you notify and re-sell to past buyers without renting reach again. The Reels-to-sale funnel (8 steps) — set up the owned platform first, give every Reel one destination, teach one idea per Reel with a 3-second hook, add a call to action to the app not the DM, capture the follower with a free lead magnet, convert with a low-friction first purchase, retain and upsell inside the owned app, and measure what sells not what trends. The economics — Reels cost ₹0 to make and distribute; manual DM-and-UPI selling does not scale and leaves no owned record; a subscription platform adds a fixed monthly bill; the fit for a Reels-driven educator is no upfront cost and no monthly fee, paid only as a share of real sales. Owning the audience — a follower is rented and spiky, a student on an owned app is a durable, compounding asset; the second sale to an existing student costs nothing in reach, and an owned list survives an algorithm change or a ban. Distribution-first close — discovery has been democratized (Reels give free reach), so reach is no longer the defensible thing; the moat is owning the audience and the platform, and marketplace discovery (buyers already searching your subject) compounds Reels reach. AllCoaching positioning grounded in the confirmed free tier — a branded white-label app and course/recorded-lecture hosting at ₹0 with no upfront fee and no monthly subscription, content gated behind a student login, UPI and card payments with daily payouts, a student CRM that keeps owned audience data, and AI-driven marketplace discovery; the platform earns only a 10% revenue-share on paid earnings, the educator keeps 90%; paid tier (custom domain, advanced analytics, priority support) noted; no fabricated statistics. Internal links to /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/online-coaching-academy-without-coding, /blog/how-to-create-landing-page-for-online-course, /blog/best-zero-commission-teaching-platform-india, /blog/sell-online-courses-without-monthly-subscription, /blog/how-to-get-first-500-students-for-coaching-app, /blog/migrate-offline-coaching-to-online-zero-cost, /blog/how-to-get-paid-students-for-online-coaching-free, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary — Top-of-Funnel Discovery, Rented Audience, Owned Audience, Conversion Funnel, Link-in-Bio, Branded Educator App, Lead Magnet, Recommender Algorithm, Revenue-Share Model. Author Amit Ratan with 6-entry sameAs. Target keyword "instagram reels educator monetization platform" ~19,000/mo (KD ~58); audience targets Indian educators growing on Instagram Reels who want to sell courses on their own platform in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
