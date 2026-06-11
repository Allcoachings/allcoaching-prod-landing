import re, glob, os

SLUG = 'online-tutor-gst-income-tax-india'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = 'Do Online Tutors Pay GST and Income Tax in India? A Plain-English 2026 Overview'
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-10'
PREV = 'spayee-learnyst-alternative-india'
NI_OLD, NI_NEW = 47, 48
N_ALL_EXPECT = 91
CARD_TAG = 'Operations · 2026'
CARD_H3 = 'Do Online Tutors Pay GST and Income Tax in India?'
CARD_ALT = 'GST and income tax for online tutors in India — 2026 plain-English overview'
CARD_P = "Most small tutors fall below the GST threshold, but income tax applies on net income. A plain-English overview of GST and income tax for online tutors — not legal advice."
SM_TITLE = 'Do Online Tutors Pay GST and Income Tax in India? (2026 Overview)'
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
entry=('''- [Do Online Tutors Pay GST and Income Tax in India? (2026 Plain-English Overview)](''' + URL + '''): A founder-written 2026 plain-English overview answering "online tutor gst india" / "income tax for online tutors india" for Indian online tutors anxious about tax — engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step compliance checklist, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, BreadcrumbList, SoftwareApplication AllCoaching Educator Studio as clean-records-for-easy-filing with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Goods and Services Tax (India), Income tax in India, Online tutoring, Tax and Educational technology, plus mentions of the GST Council, the Income Tax Department of India, AllCoaching Educator Studio and UPI. IMPORTANT framing — the article repeatedly and explicitly states it is GENERAL, PLAIN-ENGLISH INFORMATION, NOT tax/legal/financial advice, that thresholds/rates/rules change and depend on individual circumstances, and that the reader should CONSULT A CHARTERED ACCOUNTANT; it carries a prominent disclaimer box and reminders throughout. Core reframe — the fear of tax stops more tutors from charging than the tax itself ever costs, and the reality for most is simpler than the rumour: below a clear turnover threshold there is NO GST at all, only ordinary income tax on what you actually earn; GST and income tax are SEPARATE taxes with different triggers. GST section — the single most important fact is the registration threshold: as of 2026, GST registration is generally required only once annual aggregate turnover crosses Rs 20 lakh for service providers (Rs 10 lakh in special-category states), so most small/individual tutors are below it and owe no GST; above the threshold, private coaching, test prep and standalone online courses are generally TAXABLE services (institutional exemptions are for recognised schools up to higher secondary and recognised degrees, not private tutoring), commonly at 18%; crossing the turnover limit triggers GST, not the act of teaching online. Income tax section — income tax usually DOES apply, on net taxable income (receipts minus legitimate expenses) per the applicable slab, independent of GST, so a tutor can be below the GST threshold and still owe income tax if net income exceeds the basic exemption limit; a PRESUMPTIVE TAXATION scheme for eligible professionals (declare a fixed percentage of gross receipts as income without detailed books, subject to conditions and a receipts limit) can simplify filing for many individual tutors who qualify. Turnover vs income — aggregate turnover (gross receipts) decides the GST threshold while net taxable income (receipts minus expenses) is what income tax is computed on; track gross receipts for GST position and expenses for income tax. A 6-step compliance checklist — track all teaching income, check the GST threshold, register for GST only if required, keep clean income/expense records, file the income-tax return (presumptive may simplify), and consult a chartered accountant. Three myths corrected — "selling online means I instantly need GST" (false: depends on turnover not being online), "no GST means no tax at all" (false: income tax is separate), and "coaching is exempt like school education" (generally false: institutional exemptions only). AllCoaching angle, stated with full honesty — the platform provides clean, exportable earnings records and daily settlement statements that make income-tax and (where applicable) GST filing easier, but it explicitly DOES NOT file taxes for the educator and DOES NOT claim to handle GST invoicing as a feature; compliance remains the educator\\'s responsibility with a CA. Honest discipline — the quoted figures (Rs 20 lakh / Rs 10 lakh threshold, 18% rate) are presented as widely-cited and stable AS OF 2026 but explicitly subject to change and verification, NO other tax numbers are fabricated, and the AllCoaching claim is strictly records-not-filing. Internal links to /blogs/hinglish/zero-investment-online-teaching-business-india, /blog/online-coaching-business-plan-2026, /blog/automated-fee-management-software-for-teachers, /blog/indian-edtech-laws-and-regulations-for-teachers. Glossary terms — GST, GST Registration Threshold, Income Tax, Aggregate Turnover, Presumptive Taxation, Income-Tax Return (ITR), Exempt Educational Services, Record-Keeping. Author Amit Ratan with 6-entry sameAs. Target keyword "online tutor gst india". Audience targets Indian online tutors and coaching educators with questions about GST and income tax in 2026. This is general information, not tax advice.\n''')
t=t.replace(anc, anc+entry, 1); open(lt,'w',encoding='utf-8',newline='').write(t)
print('llms.txt added:', SLUG in t, '| REGISTRATION OK')
