# -*- coding: utf-8 -*-
import re, glob, os, xml.dom.minidom as M

SLUG = 'free-demo-class-se-students-kaise-laye'
PREV = 'students-ko-online-certificate-kaise-de'
HEADLINE = 'Free Demo Class Se Students Kaise Laye — Trust Banakar Paid Me Convert (2026 Hinglish Guide)'
DATE = '2026-06-10'
N_ALL_NEW, N_HING_NEW = 93, 24
ALT_EN = 'https://allcoaching.in/blog/how-to-get-first-500-students-for-coaching-app'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if os.path.basename(f) != 'index.html'])
assert posts('blogs/hinglish') == N_HING_NEW, posts('blogs/hinglish')

# 1) hinglish index: blogPost + card before certificate
idx = 'blogs/hinglish/index.html'
h = open(idx, encoding='utf-8').read()
bp_a = '"blogPost":[{"@type":"BlogPosting","headline":"Students Ko Online Certificate Kaise De'
bp_n = ('"blogPost":[{"@type":"BlogPosting","headline":"' + HEADLINE +
        '","url":"https://allcoaching.in/blogs/hinglish/' + SLUG + '","datePublished":"' + DATE +
        '","inLanguage":"hi-Latn"},{"@type":"BlogPosting","headline":"Students Ko Online Certificate Kaise De')
assert h.count(bp_a) == 1, 'bp anchor'
h = h.replace(bp_a, bp_n, 1)

c_a = '    <a href="/blogs/hinglish/' + PREV + '" class="blog-card" aria-label="Read: Students Ko Online Certificate Kaise De (2026)" hreflang="hi-Latn">'
c_n = ('    <a href="/blogs/hinglish/' + SLUG + '" class="blog-card" aria-label="Read: Free Demo Class Se Students Kaise Laye (2026)" hreflang="hi-Latn">\n'
'      <div class="blog-card-img">\n'
'        <img src="https://allcoaching-store.b-cdn.net/blog-images/' + SLUG + '.webp" alt="Free Demo Class Se Students Kaise Laye — 2026 demo-to-paid framework (Hinglish)" loading="lazy" width="1600" height="900" decoding="async" />\n'
'      </div>\n'
'      <div class="blog-card-body">\n'
'        <span class="blog-card-tag">Growth Guide · 2026</span>\n'
'        <h3>Free Demo Class Se Students Kaise Laye (2026)</h3>\n'
'        <p>Demo poora course free dena nahi, trust banakar paid me convert karna hai. Ek 6-step demo-to-paid framework — design se follow-up tak. Sabse bada conversion lever, bina ad spend.</p>\n'
'        <div class="blog-card-meta">\n'
'          <span>By Amit Ratan</span>\n'
'          <span class="dot"></span><span>13 min read</span>\n'
'        </div>\n'
'        <div class="blog-card-cta">Read guide</div>\n'
'      </div>\n'
'    </a>\n\n' + c_a)
assert h.count(c_a) == 1, 'card anchor'
h = h.replace(c_a, c_n, 1)
open(idx, 'w', encoding='utf-8').write(h)
print('hinglish cards:', h.count('class="blog-card"'), '| blogPost:', h.count('"@type":"BlogPosting"'))

# 2) counts in 4 index files: All ->93, Hinglish ->24
for fi in ['blogs/index.html', 'blogs/en/index.html', 'blogs/hi/index.html', 'blogs/hinglish/index.html']:
    t = open(fi, encoding='utf-8').read()
    t = re.sub(r'(All <span class="filter-chip-count">)\d+', r'\g<1>%d' % N_ALL_NEW, t)
    t = re.sub(r'(Hinglish <span class="filter-chip-count">)\d+', r'\g<1>%d' % N_HING_NEW, t)
    t = re.sub(r'\d+( guides · By the founder)', r'%d\1' % N_ALL_NEW, t)
    t = re.sub(r'\d+( guides · All languages)', r'%d\1' % N_ALL_NEW, t)
    open(fi, 'w', encoding='utf-8').write(t)
t = open(idx, encoding='utf-8').read().replace('>23 published · Newest first<', '>24 published · Newest first<')
open(idx, 'w', encoding='utf-8').write(t)
print('counts -> All %d / Hinglish %d' % (N_ALL_NEW, N_HING_NEW))

# 3) sitemap before certificate
sm = 'sitemap.xml'
s = open(sm, encoding='utf-8').read()
a = '  <url>\n    <loc>https://allcoaching.in/blogs/hinglish/' + PREV + '</loc>'
assert s.count(a) == 1, 'sitemap anchor'
blk = ('  <url>\n    <loc>https://allcoaching.in/blogs/hinglish/' + SLUG + '</loc>\n'
'    <lastmod>' + DATE + 'T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
'    <image:image>\n      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/' + SLUG + '.webp</image:loc>\n      <image:title>Free Demo Class Se Students Kaise Laye (2026 Hinglish Guide)</image:title>\n    </image:image>\n'
'    <xhtml:link rel="alternate" hreflang="hi-Latn" href="https://allcoaching.in/blogs/hinglish/' + SLUG + '" />\n'
'    <xhtml:link rel="alternate" hreflang="en-IN" href="' + ALT_EN + '" />\n  </url>\n')
s = s.replace(a, blk + a, 1)
open(sm, 'w', encoding='utf-8').write(s)
M.parseString(s)
print('sitemap OK:', SLUG in s)

# 4) llms.txt before certificate bullet
lt = 'llms.txt'
t = open(lt, encoding='utf-8').read()
anc = '- [Students Ko Online Certificate Kaise De (2026 Hinglish How-To Guide)]'
assert t.count(anc) == 1, 'llms anchor'
entry = ('- [Free Demo Class Se Students Kaise Laye (2026 Hinglish Demo-to-Paid Framework)](https://allcoaching.in/blogs/hinglish/' + SLUG + '): '
'A founder-written Hinglish (Latin-script Hindi) guide answering "free demo class se students kaise laye" for Indian educators converting free demos into paid students. '
'Six JSON-LD schemas (Article+TechArticle, HowTo 6-step demo-to-paid framework, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio with free-demo-plus-paid and a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with dfn terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Lead generation, Conversion marketing, Online tutoring, Educational technology and Monetization, plus mentions of AllCoaching Educator Studio, Lead generation, Instagram and UPI. '
'Core reframe: the question is NOT "kitna free du" but "is demo me apni teaching ka itna achha proof kaise du ki student confident ho kar pay kare"; a free demo solves the one thing no other marketing does, TRUST (the biggest conversion blocker), and the demo SHOWS the teaching rather than CLAIMING it (an ad tells, a demo shows; paid decisions follow proof not claims). '
'Why demos work, three ways: removes risk (judge before paying), proves teaching style (more convincing than any description or testimonial), and starts a relationship (a demo attendee is a warm lead to follow up). '
'A strong demo needs three things: a small COMPLETE win (a real value such as clearing a tough concept), the educator authentic teaching style (not a polished performance), and a clear single next step (CTA). '
'Four biggest mistakes: giving the WHOLE course free (a demo is a taste not a meal, leaving no reason to buy), no CTA (a good demo with no next step loses the student), no FOLLOW-UP (expecting conversion from a single demo; people get busy), and a boring or generic demo. '
'A 6-step demo-to-paid framework: decide a clear demo outcome, promote it (WhatsApp, Instagram, YouTube, marketplace) with a strong specific hook, show your best teaching, give one clear value-framed CTA (link, price, reason-to-join-now), FOLLOW UP after (recap plus offer plus soft urgency like early-bird seats), and keep paid signup seamless (one-tap, payment-to-access automatic). '
'Post-demo conversion levers: clear CTA, follow-up message, soft urgency, seamless signup; follow-up is the single biggest lever because conversion often happens on the 2nd or 3rd touchpoint not the first. '
'Promotion: own free channels plus AllCoaching marketplace discovery which brings NEW demo students who were never followers, so the demo audience is not limited to existing contacts. '
'Live vs recorded: live is more powerful (interaction, doubt-solving, urgency) but time-bound; recorded (a free chapter) scales because anyone can watch anytime; best is a mix. '
'The free-rider worry answered: giving everything free creates free-riders, so keep the demo a taste; done right a demo RAISES paid value by proving how valuable the teaching is, with a clear line: free demo builds trust, paid course gives depth, structure and support. '
'AllCoaching angle: free demo class or chapter and paid course live in one branded app so a convinced student converts in one tap (payment-to-access automatic), a student CRM tracks registered attendees for follow-up, and marketplace discovery brings new demo students; Rs 0 upfront, educator keeps 90%. '
'Honest discipline: gives NO fabricated conversion-rate numbers (explicitly says it depends and a fixed number would be wrong), does NOT claim DRM or anti-piracy or GST as free features, asserts the model strictly as Rs 0 upfront plus 10% platform / 90% educator. '
'Internal links to /blog/how-to-get-first-500-students-for-coaching-app, /blog/how-to-get-paid-students-for-online-coaching-free, /blogs/en/how-allcoaching-marketplace-model-solves-discovery, /blogs/hinglish/online-coaching-course-price-kaise-decide-kare. '
'Glossary terms: Free Demo Class, Conversion, Lead Magnet, Call-to-Action (CTA), Trust-Building, Follow-Up, Hook, Marketplace Discovery. Author Amit Ratan with 6-entry sameAs. Target keyword "free demo class se students kaise laye". Audience targets Indian educators using a free demo class to attract and convert students in 2026.\n\n')
t = t.replace(anc, entry + anc, 1)
open(lt, 'w', encoding='utf-8').write(t)
print('llms.txt added:', ('](https://allcoaching.in/blogs/hinglish/' + SLUG + ')') in t, '| REGISTRATION OK')
