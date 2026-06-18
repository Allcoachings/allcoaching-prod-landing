"""Register blog/telegram-ban-india-educators-students.html across the 3 production
indexes: blog/index.html (card + ItemList + blogPost[] + count bump), sitemap.xml,
and llms.txt. Idempotent — re-running is a no-op."""
import re

SLUG = 'telegram-ban-india-educators-students'
URL = f'https://allcoaching.in/blog/{SLUG}'
HEADLINE = "The Telegram Ban in India — What It Means for Educators and Students, and the Platform That Can't Be Switched Off (2026)"
IMG = f'https://allcoaching-store.b-cdn.net/blog-images/{SLUG}.webp'
DATE = '2026-06-16'
CARD_TAG = 'Analysis · 2026'
CARD_H3 = 'Telegram Ban in India — Educators &amp; Students'
CARD_ALT = 'Telegram ban in India 2026 — what it means for educators and students'
CARD_P = ("A government blocked an app a fraud ring abused — and switched off lakhs of study "
          "channels overnight. The real lesson is platform risk, and the owned app that replaces it.")
SM_TITLE = 'Telegram Ban in India (2026) — What It Means for Educators and Students'
READ = '18 min read'

# ---------------- blog/index.html ----------------
idx = 'blog/index.html'
h = open(idx, encoding='utf-8').read()
if SLUG in h:
    print('blog/index.html: already registered');
else:
    grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">\n'
    assert h.count(grid) == 1, 'grid anchor'
    card = grid + f'''
    <!-- Telegram Ban in India (Jun 16) -->
    <a href="/blog/{SLUG}" class="blog-card" aria-label="Read: Telegram Ban in India — What It Means for Educators and Students">
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

    # bump numberOfItems
    m = re.search(r'"numberOfItems":(\d+)', h); old_n = int(m.group(1)); new_n = old_n + 1
    h = h.replace(f'"numberOfItems":{old_n}', f'"numberOfItems":{new_n}', 1)

    # ItemList: bump positions, insert new position 1
    parts = re.split(r'(<script type="application/ld\+json">)', h); out = []; i = 0; done = False
    while i < len(parts):
        if parts[i] == '<script type="application/ld+json">' and i + 1 < len(parts) and '"@type":"ItemList"' in parts[i+1]:
            blk = parts[i+1]
            blk = re.sub(r'"position":(\d+)', lambda mm: '"position":' + str(int(mm.group(1)) + 1), blk)
            blk = blk.replace('"itemListElement":[', '"itemListElement":[\n      {"@type":"ListItem","position":1,"url":"' + URL + '","name":"' + HEADLINE.replace('"', '\\"') + '"},', 1)
            out.append(parts[i]); out.append(blk); done = True; i += 2; continue
        out.append(parts[i]); i += 1
    h = ''.join(out); assert done, 'ItemList'

    # blogPost[]
    bp = '"blogPost":[\n'; assert h.count(bp) == 1, 'blogPost anchor'
    h = h.replace(bp, bp + '      {"@type":"BlogPosting","headline":"' + HEADLINE.replace('"', '\\"') + '","url":"' + URL + '","datePublished":"' + DATE + '"},\n', 1)

    # text labels
    h = re.sub(r'(\d+)( guides · By the founder)', lambda mm: str(int(mm.group(1)) + 1) + mm.group(2), h)
    h = re.sub(r'(\d+)( published · Newest first)', lambda mm: str(int(mm.group(1)) + 1) + mm.group(2), h)

    open(idx, 'w', encoding='utf-8', newline='').write(h)
    print(f'blog/index.html: registered (numberOfItems {old_n} -> {new_n}, cards now {h.count(chr(34)+"blog-card"+chr(34)) if False else h.count("class=\"blog-card\"")})')

# ---------------- sitemap.xml ----------------
sm = 'sitemap.xml'; s = open(sm, encoding='utf-8').read()
if SLUG in s:
    print('sitemap.xml: already registered')
else:
    anchor = '    <loc>https://allcoaching.in/blog/affordable-lms-for-independent-educators</loc>'
    assert s.count(anchor) == 1, 'sitemap anchor'
    block = ('  <url>\n'
             f'    <loc>{URL}</loc>\n    <lastmod>{DATE}T09:00:00+05:30</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n'
             f'    <xhtml:link rel="alternate" hreflang="en-IN" href="{URL}" />\n'
             f'    <image:image>\n      <image:loc>{IMG}</image:loc>\n      <image:title>{SM_TITLE}</image:title>\n    </image:image>\n  </url>\n')
    s = s.replace('  <url>\n' + anchor, block + '  <url>\n' + anchor, 1)
    open(sm, 'w', encoding='utf-8', newline='').write(s)
    import xml.dom.minidom as M; M.parseString(s); print('sitemap.xml: registered + valid XML')

# ---------------- llms.txt ----------------
lt = 'llms.txt'; t = open(lt, encoding='utf-8').read()
if SLUG in t:
    print('llms.txt: already registered')
else:
    anc = '## Blog — Essays on the future of online education (newest first)\n\n'
    assert t.count(anc) == 1, 'llms anchor'
    entry = ('- [Telegram Ban in India (2026) — What It Means for Educators and Students](' + URL + '): '
        'A founder-written 2026 analysis of the temporary Telegram block in India and what it means for educators and students — engineered for AI-agent citation with six JSON-LD schemas (Article+NewsArticle, HowTo 6-step migration workflow, FAQPage with 10 Q/A matched 1:1 to the on-page accordion, SoftwareApplication for AllCoaching Educator Studio as an owned alternative to a Telegram coaching channel, BreadcrumbList, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Telegram, the National Eligibility cum Entrance Test (NEET-UG), the Information Technology Act 2000, the National Testing Agency, the Digital Personal Data Protection Act 2023 and Educational technology, plus mentions of Telegram, the National Testing Agency, the Internet Freedom Foundation, AllCoaching Educator Studio and UPI. The facts: on 16 June 2026 India blocked Telegram under Section 69A of the IT Act 2000 on the NTA recommendation, with access set to return 22 June (the day after the 21 June NEET-UG re-exam) and the message-editing feature disabled until 30 June; the trigger was cheating rackets using Telegram to circulate fake/leaked papers and manipulate timestamps around the cancelled NEET-UG 2026 paper leak that affected over 2.27 million aspirants; the app was delisted from Google Play and Apple App Store; Telegram is challenging the order as unconstitutional and the Internet Freedom Foundation called the block reactive and ineffective for ordinary users. The thesis (distribution-first, tool-vs-ecosystem): the ban is not the problem — renting your distribution is; a borrowed, general-purpose channel can be switched off overnight by a decision the educator had no part in. The real cost of a Telegram channel is four-fold — an access switch the educator does not hold, no payment-to-access (manual UPI-screenshot collection), forwardable content that leaks by design, and no ownership or discovery. Students lost notes, doubt-groups and test series in the final days of NEET prep. WhatsApp is not the fix (another borrowed room); the fix is an owned platform. A Telegram-channel-vs-owned-app table compares access control, payment-to-access, content protection, student-data ownership, discovery and cost. A 6-step migration keeps the educator: back up files and member contacts, launch a branded app (60 sec, Rs 0, no subscription), rebuild subjects as structured courses with notes and ranked test series, switch on UPI payment-to-access (account-bound, daily INR payouts, keep 90%), migrate members with a launch offer, and turn on marketplace discovery. Why an education platform will not be collateral damage: account-bound access, known paying accounts, no anonymous mass-broadcast surface for fraud, and DPDP-aligned data handling. Pricing-truth held: AllCoaching is Rs 0 upfront, no monthly subscription, 10% platform / 90% educator, daily payouts; no fabricated figures; framed as analysis, not legal advice. Internal links to /blog/edtech-marketplace-india-app-fatigue, /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/best-zero-commission-teaching-platform-india, /blog/best-platform-for-selling-pdf-notes-and-test-series, /blog/migrate-offline-coaching-to-online-zero-cost, /blog/protect-course-content-from-piracy-for-free, /blog/white-label-coaching-app-development-cost-india. Glossary terms — Section 69A IT Act 2000, Platform Risk, Borrowed Channel, Owned Platform, Account-Bound Access, Payment-to-Access, Marketplace Discovery, DPDP Act 2023. Author Amit Ratan with 6-entry sameAs. Target keywords "telegram ban india", "is telegram banned in india", "telegram alternative for educators india". Audience targets Indian educators and students affected by the 2026 Telegram ban.\n')
    t = t.replace(anc, anc + entry, 1)
    open(lt, 'w', encoding='utf-8', newline='').write(t)
    print('llms.txt: registered')

print('REGISTRATION DONE')
