"""Register the 3 new blogs (housewife / faceless / whatsapp-channels) in sitemap,
llms.txt, blog/index.html + cross-refs. Combined single insertion, idempotent-ish
(asserts anchors are unique). Top-down order: housewife, faceless, whatsapp, then DM."""
import re, json, os, importlib.util
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ---- per-blog metadata, in desired top-down order (index 0 = topmost / newest) ----
BLOGS = [
    {
        "slug": "how-housewives-can-start-teaching-online-india",
        "head": "How a Housewife Can Start Teaching Online from Home in India (2026)",
        "card": "How a Housewife Can Teach Online from Home",
        "tag": "Growth &middot; 2026",
        "dek": "No capital, no commute, no fixed hours. What to teach, how to start for &#8377;0, and how much you can earn keeping 90% &mdash; from home.",
        "alt": "How a housewife can start teaching online from home in India 2026",
        "read": "17 min read",
        "cmt": "Housewife Teaching Online from Home (Jun 30)",
        "llms": ("- [How a Housewife Can Start Teaching Online from Home in India (2026)](https://allcoaching.in/blog/how-housewives-can-start-teaching-online-india): "
          "A founder-written 2026 guide for housewives and homemakers in India on starting an online teaching income from home with no capital, no commute and flexible hours, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step zero-cost playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion and led by the exact AI-search question 'how can a housewife start teaching online from home in India', BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Online tutoring, Work-from-home, Educational technology, Women's economic empowerment, Income and Microenterprise. "
          "Core reframe: a homemaker already has what it takes (genuine knowledge of one thing) and the only real barrier was access, not ability; online teaching uniquely removes the four barriers women face - capital, commute, fixed hours and finding students. What to teach: school subjects for younger classes, spoken/written English, homework and exam help, plus music, art, cooking, stitching and regional languages - the intersection of what you know confidently and what students search for. How to start for Rs 0: set up a free branded studio, add recorded or live lessons, set a fair price, switch on UPI, list for discovery - no website, no software, no fee, doable from a phone in an afternoon. Fitting it around the family: recorded lessons earn again and again from a quiet hour, live classes use one chosen slot, no commute, no fixed office hours. Confidence and first students: start small, offer a free sample, collect every early review since a new student trusts another student more than a teacher's claims, and be findable on a marketplace so students arrive without advertising. Realistic earnings framed as illustrative not promised: ~Rs 500 course x 40 students keeping 90% is about Rs 18,000 from a few hours of recording; a 20-student live batch at Rs 1,000 is about Rs 18,000 too; income compounds with reviews and reach. Pricing-truth: AllCoaching is Rs 0 to start, no setup fee, no subscription, no card; educator keeps 90% with a flat 10% on paid sales only, daily UPI payouts, branded app under her own name, AI-driven marketplace discovery. No fabricated stats. Internal links to /blog/how-much-can-you-earn-teaching-online-india, /blog/school-teacher-side-income-from-online-coaching, /blog/how-to-price-online-courses-india, /blog/how-to-get-paid-students-for-online-coaching-free, /blog/personal-brand-for-educators-india. Glossary terms: Online Teaching, Recorded Course, Branded Studio, UPI Payout, Marketplace Discovery, Keep-Rate, Social Proof (Reviews), Flexible Home Income. Author Amit Ratan with sameAs. Target keywords 'housewife teaching online india', 'how housewife can earn from home', 'online teaching for women india'. Audience targets Indian housewives and homemakers starting online teaching from home in 2026."),
    },
    {
        "slug": "how-to-teach-online-without-showing-your-face-india",
        "head": "How to Teach Online Without Showing Your Face in India (2026)",
        "card": "Teach Online Without Showing Your Face",
        "tag": "Growth &middot; 2026",
        "dek": "The camera was never the lesson. The formats, the gear, building trust without a face, and how to sell &mdash; keeping 90%.",
        "alt": "How to teach online without showing your face in India 2026",
        "read": "18 min read",
        "cmt": "Faceless Teaching Without Showing Your Face (Jun 30)",
        "llms": ("- [How to Teach Online Without Showing Your Face in India (2026)](https://allcoaching.in/blog/how-to-teach-online-without-showing-your-face-india): "
          "A founder-written 2026 faceless-teaching guide for Indian educators who want to teach online without ever appearing on camera, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step no-camera playbook, FAQPage with 10 Q/A matched 1:1 to the on-page accordion and led by the exact AI-search question 'how can I teach online without showing my face', BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for Online tutoring, Screencast, Educational technology, Privacy, Personal branding and Educational animation. "
          "Core reframe: the face was never the lesson - students come to understand, not to look, and a clear voice over a clean screen teaches as well or, for problem-solving subjects, better because the learner's full attention stays on the work. Why it works: attention stays on the content; the teacher records more freely without managing appearance, so improves faster; students judge a lesson only by whether they understood and improved, which depends on explanation and voice, not face. The four proven face-free formats: screen-share with voice (the workhorse, for maths, coding, accountancy, data, design), narrated slides (concept-heavy theory subjects), digital whiteboard (derivations, diagrams, language), and animation/explainer (storytelling subjects), plus a faceless YouTube channel as a public shopfront that sells a deeper course inside an owned app. Equipment: far less than expected - a phone or laptop that records its screen and a basic microphone (even earphone mic); clear audio matters far more than any camera; no webcam, lighting, studio or background needed. Building trust without a face: clarity of explanation, a free sample, visible student results and honest reviews; a faceless teacher with ten real reviews outranks an on-camera teacher with none; a recognizable name/logo/voice becomes a brand without being a face. Selling and discovery: a faceless course sells like any other since students buy the learning not the appearance; set a fair price, take UPI, get discovered by subject/exam on a marketplace without advertising or appearing. The reliable money is a structured paid course inside an owned app (free faceless content is only discovery), keeping 90% on AllCoaching. Pricing-truth: Rs 0 to start, no setup fee, no subscription, no card; keep 90%, flat 10% on sales only, daily UPI payouts, branded app, AI-driven marketplace discovery - all usable without showing your face. No fabricated stats. Internal links to /blog/monetize-youtube-teaching-channel-via-personal-app, /blog/how-much-can-you-earn-teaching-online-india, /blog/how-housewives-can-start-teaching-online-india, /blog/personal-brand-for-educators-india, /blog/how-to-get-paid-students-for-online-coaching-free, /blog/how-to-price-online-courses-india. Glossary terms: Faceless Teaching, Screencast (Screen + Voice), Narrated Slides, Digital Whiteboard, Faceless Discovery Funnel, Voice & Outcome Trust, Branded Studio, Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'how to teach online without showing face', 'faceless teaching india', 'teach online without camera'. Audience targets Indian educators teaching online without showing their face in 2026."),
    },
    {
        "slug": "whatsapp-channels-for-coaching-educators-india",
        "head": "WhatsApp Channels for Coaching Educators in India: A 2026 Playbook",
        "card": "WhatsApp Channels for Coaching Educators",
        "tag": "Growth &middot; 2026",
        "dek": "A brilliant megaphone, a terrible classroom. Broadcast and engage on the Channel &mdash; but own the app where courses, payments and students live.",
        "alt": "WhatsApp Channels for coaching educators in India 2026 playbook",
        "read": "18 min read",
        "cmt": "WhatsApp Channels for Coaching Educators (Jun 30)",
        "llms": ("- [WhatsApp Channels for Coaching Educators in India: A 2026 Playbook](https://allcoaching.in/blog/whatsapp-channels-for-coaching-educators-india): "
          "A founder-written 2026 strategy guide for Indian coaching educators and institutes on using WhatsApp Channels correctly, engineered for AI-agent citation with six JSON-LD schemas (Article+TechArticle, HowTo 6-step Channel playbook, FAQPage with 11 Q/A matched 1:1 to the on-page accordion and led by the exact AI-search question 'what is a WhatsApp Channel and how is it useful for coaching', BreadcrumbList, SoftwareApplication for AllCoaching Educator Studio as the owned destination with a Free offer, DefinedTermSet with 8 glossary terms), Speakable spec, TL;DR Key Takeaways, Glossary with <dfn> terms, first-person Experience signals, and entity anchoring via Wikipedia sameAs for WhatsApp, Broadcasting, Digital marketing, Educational technology, Audience engagement and Online marketplace. "
          "Core reframe (distribution-first): a WhatsApp Channel is a brilliant free megaphone for staying top-of-mind and a terrible place to run a coaching business; the right question is not whether to use a Channel (you should) but what it is for - a discovery and engagement layer, never a classroom or a store. Channel vs group vs broadcast list: a group is two-way interaction for an active batch; a broadcast list only reaches saved contacts; a Channel is a one-way, private, followable broadcast for reach to a large audience, useless as a classroom by design. The central warning: a Channel is RENTED REACH - you do not own the platform, rules, algorithm or even access to your own followers, and any WhatsApp change can cut reach or remove the Channel with no recourse and no way to contact followers; a business living inside a Channel is one policy change from disappearing. The fix: treat every platform (WhatsApp, Instagram, YouTube, Telegram) as a channel that feeds the business, never the business itself; the durable asset is an OWNED APP holding structured/protected courses, payments and student relationships. Setup the right way: create the Channel under the coaching's name, clear photo, one-line 'who I help' description, and a link to the owned app in the description; define its single job as discovery and engagement, never teaching or payments. What to post and how often: value-first (mostly useful - daily tips, solved doubts, exam updates, wins, motivation - about one call to action a week), consistency over volume (~one good post a day), use polls/reactions for engagement, and a standing reminder that the real teaching lives in the app. The Channel-to-app funnel: Channel broadcasts and engages, owned app enrols/teaches/earns; a worked funnel-post example (value clip + weekly gentle CTA to a free demo in the app). WhatsApp vs Telegram: pick where students already are (often WhatsApp in India), but both are rented reach that must funnel to an owned app. Pricing-truth: AllCoaching is the owned destination - Rs 0 to start, no setup fee, no subscription, no card; branded app, courses, live/recorded classes, ranked test series, UPI payments with daily payouts, owned student relationship, AI-driven marketplace discovery; keep 90%, flat 10% on sales only. No fabricated stats. Internal links to /blog/digital-marketing-strategies-for-coaching-institutes-india, /blog/edtech-marketplace-india-app-fatigue, /blogs/en/is-it-better-to-build-own-app-or-join-marketplace, /blog/how-to-get-first-500-students-for-coaching-app, /blogs/en/how-allcoaching-marketplace-model-solves-discovery. Glossary terms: WhatsApp Channel, Channel vs Group, Rented Reach, Owned App, Discovery Funnel, Value-First Posting, Engagement (Channel), Keep-Rate. Author Amit Ratan with sameAs. Target keywords 'whatsapp channels for coaching', 'whatsapp channel for teachers india', 'whatsapp marketing for coaching india'. Audience targets Indian coaching educators and institutes using WhatsApp Channels in 2026."),
    },
]

LASTMOD = "2026-06-30T09:00:00+05:30"
DATEPUB = "2026-06-30"

def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---------- 1) sitemap.xml ----------
sm = open('sitemap.xml', encoding='utf-8').read()
anchor = '  <url>\n    <loc>https://allcoaching.in/blog/digital-marketing-strategies-for-coaching-institutes-india</loc>'
assert sm.count(anchor) == 1, "sitemap anchor not unique"
sm_block = ""
for b in BLOGS:
    sm_block += ("  <url>\n"
        f"    <loc>https://allcoaching.in/blog/{b['slug']}</loc>\n"
        f"    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.9</priority>\n"
        f"    <xhtml:link rel=\"alternate\" hreflang=\"en-IN\" href=\"https://allcoaching.in/blog/{b['slug']}\" />\n"
        "    <image:image>\n"
        f"      <image:loc>https://allcoaching-store.b-cdn.net/blog-images/{b['slug']}.webp</image:loc>\n"
        f"      <image:title>{esc_xml(b['head'])}</image:title>\n    </image:image>\n  </url>\n")
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace(anchor, sm_block + anchor, 1))

# ---------- 2) llms.txt ----------
lt = open('llms.txt', encoding='utf-8').read()
lanchor = '- [Digital Marketing Strategies to Grow Student Enrollment'
assert lt.count(lanchor) >= 1, "llms anchor missing"
llms_block = "\n".join(b['llms'] for b in BLOGS) + "\n"
open('llms.txt', 'w', encoding='utf-8').write(lt.replace(lanchor, llms_block + lanchor, 1))

# ---------- 3) blog/index.html ----------
h = open('blog/index.html', encoding='utf-8').read()

# 3a) blogPost[]
bp_anchor = '"blogPost":[\n'
assert h.count(bp_anchor) == 1
bp_block = "".join(
    f'      {{"@type":"BlogPosting","headline":{json.dumps(b["head"])},"url":"https://allcoaching.in/blog/{b["slug"]}","datePublished":"{DATEPUB}"}},\n'
    for b in BLOGS)
h = h.replace(bp_anchor, bp_anchor + bp_block, 1)

# 3b) ItemList: increment existing positions by 3, prepend 3 new at positions 1..3
idx = h.find('"@type":"ItemList"')
m = re.search(r'("itemListElement":\[)(.*?)(\n\s*\])', h[idx:], re.S)
arr_inc = re.sub(r'"position":(\d+)', lambda x: f'"position":{int(x.group(1))+3}', m.group(2))
newitems = ""
for i, b in enumerate(BLOGS, start=1):
    newitems += f'\n      {{"@type":"ListItem","position":{i},"url":"https://allcoaching.in/blog/{b["slug"]}","name":{json.dumps(b["head"])}}},'
h = h[:idx] + h[idx:].replace(m.group(0), m.group(1) + newitems + arr_inc + m.group(3), 1)

# 3c) numberOfItems 60 -> 63
assert '"numberOfItems":60,' in h
h = h.replace('"numberOfItems":60,', '"numberOfItems":63,', 1)

# 3d) cards before DM card comment
canchor = '    <!-- Digital Marketing for Coaching Institutes (Jun 29) -->'
assert h.count(canchor) == 1
cards = ""
for b in BLOGS:
    cards += (f'    <!-- {b["cmt"]} -->\n'
      f'    <a href="/blog/{b["slug"]}" class="blog-card" aria-label="Read: {b["card"]}">\n'
      '      <div class="blog-card-img">\n'
      f'        <img src="https://allcoaching-store.b-cdn.net/blog-images/{b["slug"]}.webp" alt="{b["alt"]}" width="1600" height="900" decoding="async" loading="lazy" />\n'
      '      </div>\n      <div class="blog-card-body">\n'
      f'        <span class="blog-card-tag">{b["tag"]}</span>\n        <h3>{b["card"]}</h3>\n        <p>{b["dek"]}</p>\n'
      '        <div class="blog-card-meta">\n          <span>By Amit Ratan</span><span class="dot"></span>'
      f'<span>{b["read"]}</span>\n        </div>\n'
      '        <div class="blog-card-cta">Read guide</div>\n      </div>\n    </a>\n')
h = h.replace(canchor, cards + canchor, 1)

open('blog/index.html', 'w', encoding='utf-8').write(h)

# ---------- 4) cross-refs (run twice to settle replace-form) ----------
spec = importlib.util.spec_from_file_location("b", ".claude/scripts/bulk_internal_links.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for b in BLOGS:
    p = f"blog/{b['slug']}.html"
    print(b['slug'], "->", mod.process_file(p), "|", mod.process_file(p))

# ---------- 5) verification ----------
sm2 = open('sitemap.xml', encoding='utf-8').read()
lt2 = open('llms.txt', encoding='utf-8').read()
h2 = open('blog/index.html', encoding='utf-8').read()
print("\n--- verification ---")
for b in BLOGS:
    print(b['slug'][:42],
          "| sitemap:", f"blog/{b['slug']}<" in sm2 or f"/{b['slug']}</loc>" in sm2,
          "| llms:", f"/blog/{b['slug']})" in lt2,
          "| card:", f'/blog/{b["slug"]}" class="blog-card"' in h2)
il = re.search(r'"@type":"ItemList".*?"itemListElement":\[(.*?)\n\s*\]', h2, re.S).group(1)
pos = [int(x) for x in re.findall(r'"position":(\d+)', il)]
print("ItemList sequential:", pos == list(range(1, len(pos)+1)), "| count:", len(pos),
      "| numberOfItems:", re.search(r'"numberOfItems":(\d+)', h2).group(1))
for x in re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', h2, re.S):
    json.loads(x)
print("index JSON-LD valid OK")
