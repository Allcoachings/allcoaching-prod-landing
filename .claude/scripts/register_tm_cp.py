import re

SLUG='teachmint-vs-classplus-konsa-best-hai'
URL=f'https://allcoaching.in/blogs/hinglish/{SLUG}'
HEADLINE='Teachmint vs Classplus — Konsa Best Hai? Giants vs New-Age Platforms Ka Detailed 2026 Review (Hinglish)'
IMG=f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE='2026-06-04'

# ---------- blogs/hinglish/index.html ----------
idx='blogs/hinglish/index.html'; h=open(idx,encoding='utf-8').read()
assert h.count('10 published · Newest first')==1
h=h.replace('10 published · Newest first','11 published · Newest first')
assert h.count('"dateModified":"2026-06-03"}</script>')==1
h=h.replace('"dateModified":"2026-06-03"}</script>','"dateModified":"2026-06-04"}</script>')
bp='"blogPost":[{"@type":"BlogPosting","headline":"Apni Coaching Ki Website'
assert h.count(bp)==1
h=h.replace(bp, '"blogPost":[{"@type":"BlogPosting","headline":"'+HEADLINE+'","url":"'+URL+'","datePublished":"'+DATE+'","inLanguage":"hi-Latn"},{"@type":"BlogPosting","headline":"Apni Coaching Ki Website',1)
card_anchor='    <a href="/blogs/hinglish/apni-coaching-ki-website-kaise-banaye-free" class="blog-card"'
assert h.count(card_anchor)==1
newcard='''    <a href="/blogs/hinglish/''' + SLUG + '''" class="blog-card" aria-label="Read: Teachmint vs Classplus — Konsa Best Hai? (2026 Hindi Review)" hreflang="hi-Latn">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Teachmint vs Classplus konsa best hai — giants vs new-age 2026 Hinglish review" loading="lazy" width="1600" height="900" decoding="async" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Comparison · 2026</span>
        <h3>Teachmint vs Classplus — Konsa Best Hai? (2026)</h3>
        <p>Dono giants ke honest pros/cons, unki common kami (subscription + students khud laao), aur kab new-age ₹0 platform (AllCoaching) inse behtar fit hai.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span>
          <span class="dot"></span><span>15 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>

'''
h=h.replace(card_anchor, newcard+card_anchor, 1)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('hinglish index: cards=%d count11=%s blogPost+=%s' % (h.count('class="blog-card"'), '11 published' in h, SLUG in h))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
block=('  <url>\n'
       f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
       f'    <xhtml:link rel="alternate" hreflang="hi-Latn" href="{URL}" />\n'
       '    <xhtml:link rel="alternate" hreflang="en-IN" href="https://allcoaching.in/blog/classplus-vs-graphy-vs-allcoaching" />\n  </url>\n')
assert s.count('\n</urlset>')==1
s=s.replace('\n</urlset>', '\n'+block+'</urlset>', 1)
open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s)
print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('- [Teachmint vs Classplus — Konsa Best Hai? (2026 Hinglish Comparison)](' + URL + '): A founder-written, deliberately fair Hinglish review answering "Teachmint vs Classplus konsa best hai" for Indian educators — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step decision framework, FAQPage with 13 Q/A, BreadcrumbList, SoftwareApplication AllCoaching as the new-age alternative with Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Educational technology, Software as a service, White-label product, and Learning management system, plus mentions of Teachmint and Classplus. Core reframe — "konsa best" ka jawab kisi brand ka naam nahi, aapke stage par depend karta hai; aur usse zaroori sawal: kya giant chahiye hi, ya ek model jo tab tak kuch na le jab tak aap kamaye aur students bhi laaye? Explicitly fair, not a criticism of either: both are capable white-label SaaS giants. Teachmint pros (classroom/institute infrastructure, attendance, multi-teacher admin, mature live classes) and cons (paid subscription, Year-1 ~₹3-9 lakh range, students khud laane padte hain); Classplus pros (white-label apps, strong sales/onboarding support, marketing/CRM) and cons (cost often higher/sales-led, Year-1 ~₹4-11 lakh, annual lock-in, students khud laane padte hain). Head-to-head table on core strength, model, real Year-1 total, onboarding, lock-in, and "students laata hai?" (both: nahi). The shared structural gap — both run a subscription/upfront model and, more importantly, both give tools but not students; the best white-label app stays empty without an audience. The new-age alternative AllCoaching changes the model: ₹0 upfront, 10% revenue-share on paid earnings (90% to educator, daily payout), and marketplace discovery that matches students searching by subject/exam/language to the studio — software plus students, not just software. Honest disclosure that custom domain and advanced analytics are paid-tier on AllCoaching too (claim is "subscription stack free upfront," not "everything free"). Honest who-should-use-which: large multi-branch institutes needing classroom-admin depth may pick a giant; solo/small educators wanting ₹0 upfront and discovery fit AllCoaching; smartest approach is to run all three in parallel for one batch and decide by results, not brand name. Exact prices change — the post uses house-standard ranges and tells readers to verify on each vendor\'s site, never quoting a possibly-stale figure. Internal links to /blog/classplus-vs-graphy-vs-allcoaching, /vs/teachmint, /vs/classplus, /blog/teachmint-paid-features-alternative-free, /blogs/hinglish/teachers-ke-liye-best-coaching-app-2026, /blog/white-label-coaching-app-development-cost-india, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary — White-Label SaaS, Subscription Model, Revenue Share Model, Marketplace Discovery, Total Cost of Ownership, Vendor Lock-in, Branded Studio, Classroom Infrastructure. Author Amit Ratan with 6-entry sameAs. Target keyword "teachmint vs classplus konsa best hai" ~12,500/mo (KD high). Audience targets Indian educators comparing Teachmint vs Classplus and evaluating a new-age ₹0 alternative in 2026. Authored by founder Amit Ratan.\n')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
