import re, glob

SLUG = 'video-drm-protection-for-indian-course-creators'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Video DRM Protection for Indian Course Creators — What It Is, and Whether You Actually Need It (2026)'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-05'

def posts(d): return len([f for f in glob.glob(d+'/*.html') if not f.replace('\\','/').endswith('/index.html')])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN; N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_BLOG == 35 and N_ALL == 69, (N_BLOG, N_ALL)

# ---------- blog/index.html ----------
idx = 'blog/index.html'; h = open(idx, encoding='utf-8').read()
grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
assert h.count(grid) == 1
card = grid + '''
    <!-- Video DRM Protection for Indian Course Creators (Jun 5) -->
    <a href="/blog/''' + SLUG + '''" class="blog-card" aria-label="Read: Video DRM Protection for Indian Course Creators">
      <div class="blog-card-img">
        <img src="''' + IMG + '''" alt="Video DRM protection for Indian course creators — what it is and whether you need it, 2026" width="1600" height="900" decoding="async" loading="lazy" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Content Security · 2026</span>
        <h3>Video DRM Protection for Indian Course Creators</h3>
        <p>What video DRM actually is, how piracy really happens in India, and the practical protection most educators need — plus why a more valuable legit course beats any DRM.</p>
        <div class="blog-card-meta">
          <span>By Amit Ratan</span><span class="dot"></span><span>15 min read</span>
        </div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>
'''
h = h.replace(grid, card, 1)
assert h.count('"numberOfItems":34') == 1
h = h.replace('"numberOfItems":34', '"numberOfItems":35')
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
for a,b in [('34 guides · By the founder','35 guides · By the founder'),('34 published · Newest first','35 published · Newest first')]:
    assert h.count(a)==1, a; h=h.replace(a,b)
open(idx,'w',encoding='utf-8',newline='').write(h)
print('blog/index.html: cards=%d numberOfItems35=%s blogPost=%d' % (h.count('class="blog-card"'), '"numberOfItems":35' in h, h.count('"@type":"BlogPosting"')))

# ---------- 4 blogs/* index files: keep cross-folder counts correct (All 69 / English 56) ----------
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
print('chips updated on 4 blogs/* files -> All %d / English %d / Hinglish %d' % (N_ALL,N_ENGLISH,N_HING))

# ---------- sitemap.xml ----------
sm='sitemap.xml'; s=open(sm,encoding='utf-8').read()
a='  <url>\n    <loc>https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online</loc>'
assert s.count(a)==1
blk=('  <url>\n'
     f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T12:00:00+05:30</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.85</priority>\n'
     f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
     f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>Video DRM Protection for Indian Course Creators — What It Is and Whether You Need It (2026)</image:title>\n    </image:image>\n  </url>\n')
s=s.replace(a, blk+a, 1); open(sm,'w',encoding='utf-8',newline='').write(s)
import xml.dom.minidom as M; M.parseString(s); print('sitemap: added + well-formed:', SLUG in s)

# ---------- llms.txt ----------
lt='llms.txt'; t=open(lt,encoding='utf-8').read()
anc='## Blog — Essays on the future of online education (newest first)\n\n'
assert t.count(anc)==1
entry=('''- [Video DRM Protection for Indian Course Creators (2026 Honest Explainer)](''' + URL + '''): A founder-written, honest 2026 explainer answering "video DRM protection for Indian course creators" — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step practical protection approach, FAQPage with 10 Q/A, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as access-controlled course hosting with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, two first-person Experience signals, and entity anchoring via Wikipedia sameAs for Digital rights management, Copyright infringement, Digital watermarking and Online tutoring, plus mentions of Widevine, Encryption and Streaming media. Core reframe — video DRM is a spectrum, not a switch, and the honest question is not "which DRM stops piracy" (none does — a second camera can always film a screen) but "what protection is worth its cost for an Indian educator, and what makes a paid course worth more than a leaked copy". The three DRM layers explained plainly — access control (gate playback behind a login; stops casual file sharing; low cost), encryption such as HLS+AES (scramble video in transit; stops direct downloads; medium), and hardware DRM such as Widevine/FairPlay/PlayReady (decode in hardware-isolated memory so screen recorders capture only black; stops screen recording; high cost) — and the key limit that none can close the analog hole (a camera filming the screen), which is why even Netflix-grade DRM does not eliminate piracy. How course piracy actually happens in India — overwhelmingly low-tech: re-sharing a downloaded file, sharing one paid login, Telegram channel leaks, screen recording, and reselling — almost all defeated or deterred by access-controlled hosting, a visible watermark, device/session limits, monitoring and fast takedowns, NOT by enterprise DRM. Honest verdict on who needs enterprise hardware DRM — only narrow cases (very high-value courses, large catalogues, or platforms serving many educators where DRM is licensed once and amortised); for an educator selling a course for a few thousand rupees, enterprise DRM's cost far outweighs the marginal piracy it prevents beyond a practical stack, and that money does more good keeping the price affordable and the course updated. The strongest anti-piracy is structural, not technical — a living course (affordable, continuously updated, with live doubt-solving, community, certificates and support) beats a dead static copy, removing most of the demand for pirated versions. AllCoaching positioning is deliberately conservative and matches the confirmed free tier: course videos are delivered inside a branded studio behind a student login and streamed rather than handed out as downloadable files (which removes the easiest leak), at ₹0 upfront, with the educator keeping 90% (10% revenue-share on paid earnings only, daily payouts); the post does NOT claim enterprise hardware DRM (Widevine/FairPlay) or forensic watermarking as free AllCoaching features — it explicitly frames hardware DRM as a separate, heavier layer most educators do not need, and the platform's real anti-piracy advantage as structural (affordability, updates, community, marketplace trust). Practical 6-step protection — host inside a platform (no raw files), add a visible watermark, set device/session limits, monitor Telegram/YouTube, send fast takedowns, and make the legit version win on price and value. Honest hedges throughout — no DRM is perfect, the analog hole cannot be closed, watermarking deters/traces but does not block, and protection is about friction and economics rather than a magic switch; no fabricated statistics. Internal links to /blog/protect-course-content-from-piracy-for-free, /blog/secure-video-hosting-for-educational-content, /blog/indian-edtech-laws-and-regulations-for-teachers, /blog/best-zero-commission-teaching-platform-india, /blog/sell-online-courses-without-monthly-subscription. Glossary — Video DRM, Widevine (Hardware DRM), Encryption (HLS/AES), Digital Watermarking, The Analog Hole, Access-Controlled Streaming, Course Piracy, DMCA/Copyright Takedown. Author Amit Ratan with 6-entry sameAs. Target keyword "video drm protection for indian course creators" ~5,000/mo (KD ~45). Audience targets Indian course creators and educators selling video courses online who want to understand DRM and protect content from piracy in 2026.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt: added:', SLUG in t); print('REGISTRATION OK')
