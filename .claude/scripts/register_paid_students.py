import re

SLUG = 'how-to-get-paid-students-for-online-coaching-free'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'How to Get Paid Students for Online Coaching Free — A 2026 Growth-Hacking Playbook for Marketplace Traffic'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-05'

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- How to Get Paid Students for Online Coaching Free (Jun 5) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: How to Get Paid Students for Online Coaching Free">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="How to get paid students for online coaching free — growth-hacking marketplace traffic 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Growth · 2026</span>
        <h3>How to Get Paid Students for Online Coaching Free</h3>
        <p>Most "free traffic" gets you followers, not buyers. A growth-hacking playbook to fill paid seats via marketplace traffic, AI-search authority and reviews — with ₹0 ad spend.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>16 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":31') == 1
h = h.replace('"numberOfItems":31', '"numberOfItems":32')
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
for a,b in [('31 guides · By the founder','32 guides · By the founder'),('31 published · Newest first','32 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('index: cards=%d numberOfItems32=%s' % (h.count('class="blog-card"'), '"numberOfItems":32' in h))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>How to Get Paid Students for Online Coaching Free — 2026 Growth-Hacking Playbook</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('- [How to Get Paid Students for Online Coaching Free (2026 Growth-Hacking Playbook)](' + URL + '): A founder-written 2026 playbook answering "how to get paid students for online coaching free" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step free paid-student playbook, FAQPage with 10 Q/A, BreadcrumbList, SoftwareApplication AllCoaching marketplace as a free paid-student acquisition engine with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, a first-person Experience signal, and entity anchoring via Wikipedia sameAs for Customer acquisition cost, Online marketplace, Network effect and Online tutoring, plus mentions of Search engine optimization, Meta Platforms and Google Ads. Core reframe — the usual "get students free" advice (post reels, run webinars, ask referrals, do SEO) is not wrong but is slow and capped by an audience you do not yet have; the real question is which free channel puts you in front of a stranger ready to pay right now for what you teach. The intent gap — followers, subscribers and views are attention, while a paying student is buying intent; a large audience can fail to convert and a focused new educator can win, because acquisition is about matching an offer to the moment of intent (search and marketplace), not accumulating followers. Free acquisition channels ranked by paid conversion (does it reach strangers? at buying intent?) — own network/WhatsApp (first few, capped to your circle), free demo/webinar (converts but limited reach), social content/reels/YouTube (reaches strangers but low intent, slow), SEO/blog (strangers plus intent but a slow build), referrals (high trust and intent but only after happy students), and marketplace traffic (strangers plus buying intent plus scale from day one). Growth-hacking marketplace traffic — a marketplace has already aggregated thousands of students searching by subject, exam, level and language; listing taps existing buying-mode demand, an AI matching layer routes the fitting students to the studio, and the educator inherits the marketplace organic and AI-search authority on day one, bringing paying strangers with no ad spend. The six-step playbook — niche down to a specific searchable offer, launch a free branded studio with a clear price, build one free lead magnet plus a strong demo, optimise the marketplace profile, run a reviews engine, and feed a recurring free content funnel into one studio. The four compounding free engines — inherited organic and AI-search authority (ChatGPT, Perplexity, Gemini), AI student-teacher matching (a niche becomes an advantage, not buried under big brands), reviews and social proof (convert discovery and feed it), and network effects (benefit from demand you did not create). Why free acquisition usually fails — chasing followers not buyers, no clear buyable priced offer, no reviews, ad-dependence that stops the moment the budget does, and inconsistency. The CAC math — paid ads charge per click forever with low cold-traffic conversion and never stop, while free buying-intent channels (search, content, and especially marketplace traffic) have a near-zero marginal cost per paying student; AllCoaching is ₹0 ad spend and ₹0 upfront, a 10% revenue-share on paid earnings only, educator keeps 90% with daily payouts. Honest hedges — none of this replaces teaching well (free acquisition gets the first student through the door; good teaching plus honest reviews keep the rest arriving), first-month numbers are ranges not promises, and custom domain and advanced analytics are paid-tier features. Internal links to /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blog/how-to-get-first-500-students-for-coaching-app, /blog/edtech-marketplace-india-app-fatigue, /blogs/en/how-ai-search-will-change-student-teacher-discovery, /blog/best-zero-commission-teaching-platform-india, /blog/sell-online-courses-without-monthly-subscription, /blog/monetize-youtube-teaching-channel-via-personal-app. Glossary — Paid Student, Buying Intent, Student Acquisition Cost (CAC), Marketplace Traffic, Lead Magnet, Organic Discovery, Network Effects, Revenue Share Model. Author Amit Ratan with 6-entry sameAs. Target keyword "how to get paid students for online coaching free" ~21,000/mo (KD ~60). Audience targets Indian independent educators, tutors and coaching owners who want paying students online without an ad budget in 2026. Authored by founder Amit Ratan.\n')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
