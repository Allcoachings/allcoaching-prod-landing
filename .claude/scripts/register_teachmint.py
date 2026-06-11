import re

SLUG = 'teachmint-paid-features-alternative-free'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Teachmint Paid Features Alternative, Free in 2026 — Get the Core Premium Stack for ₹0 on AllCoaching'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-04'

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Teachmint Paid Features Alternative Free (Jun 4) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Teachmint Paid Features Alternative — Free on AllCoaching">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Teachmint paid features alternative free on AllCoaching — 2026 honest comparison" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Comparison · 2026</span>
        <h3>Teachmint Paid Features Alternative — Free on AllCoaching</h3>
        <p>An honest comparison: Teachmint's premium stack vs AllCoaching's ₹0-upfront studio. Same core features, a different model — pay only when you earn, with discovery built in.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>14 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":30') == 1
h = h.replace('"numberOfItems":30', '"numberOfItems":31')
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
for a,b in [('30 guides · By the founder','31 guides · By the founder'),('30 published · Newest first','31 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('index: cards=%d numberOfItems31=%s' % (h.count('class="blog-card"'), '"numberOfItems":31' in h))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Teachmint Paid Features Alternative — Free on AllCoaching (2026 Comparison)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('- [Teachmint Paid Features Alternative — Free on AllCoaching (2026 Comparison)](' + URL + '): A founder-written, deliberately fair 2026 comparison answering "what is a free alternative to Teachmint\'s paid features?" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step switch playbook, FAQPage with 12 Q/A, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio with Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Educational technology, Software as a service, Learning management system, and White-label product, plus a mention of Teachmint. Core reframe — the useful question is not "what is a free clone of the paid plan?" but "am I better served paying a subscription for a tool, or by a platform that costs nothing until I earn and also brings students?" Explicitly fair: not a criticism of Teachmint, which is a capable platform strong on classroom and institute infrastructure; the issue is model fit. Honest feature mapping — the core premium stack most educators pay a subscription for (branded white-label app on web+mobile, live classes, test/quiz portal, course+video hosting, payments, student CRM) is free upfront on AllCoaching at ₹0 with a 10% revenue-share on paid earnings (educator keeps 90%, daily payouts); custom domain and advanced analytics are paid-tier on AllCoaching too (stated plainly, not over-claimed); and student discovery — a marketplace — is offered by AllCoaching but not by a pure tool. The real difference is the model: a subscription you pay before revenue arrives vs a revenue-share that charges only after. Total-cost framing — a white-label coaching app from any vendor (Teachmint included) commonly reaches a real ₹3–9 lakh in Year 1 once subscription, setup, custom domain, payment commission, and add-ons are added; exact Teachmint prices change, so the post uses ranges and tells readers to check Teachmint\'s site rather than quoting a possibly-stale number. Who-should-use-which is honest: large multi-branch institutes that need deep classroom-administration may stay on Teachmint; solo educators and small coachings paying for under-used features, wanting ₹0 upfront and discovery, fit AllCoaching. 6-step low-risk switch (list features used, launch free studio, recreate courses/tests, turn on payments keeping 90%, switch on marketplace discovery, run in parallel then switch). The decisive point: a tool cannot sell you demand — you can pay for every premium feature and still have an empty class; AllCoaching\'s marketplace matches students searching your subject/exam/language to your studio organically. Internal links to /blog/classplus-vs-graphy-vs-allcoaching, /vs/teachmint, /blog/best-zero-commission-teaching-platform-india, /blog/white-label-coaching-app-development-cost-india, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary — White-Label App, Custom Domain, Revenue Share Model, Subscription/SaaS Model, Branded Studio, Marketplace Discovery, Total Cost of Ownership, Vendor Lock-in. Author Amit Ratan with 6-entry sameAs. Target keyword "teachmint paid features alternative free 2026" ~6,800/mo. Audience targets Indian educators and coaching institutes evaluating a free alternative to Teachmint\'s paid features in 2026.\n')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
