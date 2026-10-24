---
name: academy-guide-blog
description: Write AllCoaching "guide" blog posts (English only from 2026-10-24) the way Shopify's blog grew Shopify, re-engineered for Indian educators. Teaches educators to build, sell, market and grow their OWN online academy (marketplace is secondary), in the Shopify-style v3 reading layout (Inter, three-column grid, sticky "On this page", CTA cards) with branded, Apple-style graphics (real Studio screenshots in MacBook/iPhone frames, real Google/YouTube/Instagram/WhatsApp marks, lavender canvas, heavy black + electric-blue headlines). Built to be eligible for every search surface at once: Google rankings, AI Overviews and AI Mode, featured snippets, People Also Ask, rich meta descriptions, Google Images/Discover, ChatGPT Search, Perplexity, Gemini and Claude. Use for any new AllCoaching blog post, any "Shopify-style" or "guide" blog, blog graphics/illustrations, refreshing an old post into the new layout, or planning the educator-growth content calendar.
---

# AllCoaching guide blog (v3) — the Shopify playbook for educators

This skill is the default for new AllCoaching blog posts from 2026-10-24. It sits on top of:
- `allcoaching` skill: product and pricing truth. Never contradict it.
- `ai-search-geo` skill: deeper GEO/AEO theory. This skill already contains the per-post checklist.
- `blog-post` skill: older essay-style house format and the JSON-LD field reference. Use it only for legacy posts that stay in the old layout.

Reference implementation (read it before writing a new post):
`blog/seo-for-online-academy-beginners-guide.html` + `blog-v3.css` + `assets/blog/seo-for-online-academy-beginners-guide/` + `.claude/skills/academy-guide-blog/graphics/seo-for-online-academy-beginners-guide.py`.

---

## 1. Positioning (what every post must make obvious)

**AllCoaching is Shopify for educators.** Shopify gave a seller their own store, not a stall in someone's marketplace; AllCoaching gives an educator their own academy.

- **Tagline in graphics and lockups:** "The academy platform for educators".
- **The automated path (repeat it, in this order):** sign up → choose a plan → upload your course → connect your domain → start selling. Payments, student access, apps and hosting run on their own.
- **Headline lines that are approved:** "Build your own LMS. In just a few clicks." · "One login. Your whole academy." · "Your knowledge deserves its own academy." · "Your domain. Your brand. Your students." · "Focus on teaching. We handle the tech." · "Your LMS shouldn't feel like a tech project."
- **What the educator owns:** academy website on their own domain, their own white-label Android and iOS app, their brand (logo, colours, theme), their student data (exportable).
- **What runs underneath:** courses (video, PDF, tests), unlimited live classes (YouTube Live, Zoom, built-in room), UPI/card checkout with automatic Razorpay payouts, Meta Pixel + Google Tag Manager, plugins.
- **Marketplace = supporting discovery**, never the headline: "your courses can also be discovered on the AllCoaching app".
- **The enemy is complexity, not competitors:** WordPress + 9 plugins, WhatsApp + Drive + Zoom + Excel, agency-built apps you cannot change. Show the stitched-together mess, then one login.
- **Who it is for:** exam educators (NEET, JEE, SSC, banking, UPSC, state PSC, CUET, CLAT, CAT) and skill educators (yoga, spoken English, marketing, vastu, music, coding, the Vedas). Use both kinds of examples.
- **Price truth:** 14-day free trial, no card; then Starter ₹6,999 / Growth ₹12,999 / Pro ₹24,999 per year excl. GST; platform fee 10% / 7.5% / 5% (keep 90–95%). Never "free forever", "₹0", "one-time", "cheapest". Say "Plans from ₹6,999/year + GST".

### Studio v5 (product design shared by the owner, 2026-10-24)
The educator app is called the **studio** and looks like Shopify admin: sidebar with Dashboard, Transactions, Content (Videos, PDFs, Test series), Courses, Free content, Live, Community, Discount, Analytics; Workspace: Own branding, Notifications, Referrals, Settings. Screenshots live in `graphics/studio-*.jpg` (sample educator "Anika Mehta", sample numbers).
- Always caption studio screenshots "Studio preview · sample data". Never present its numbers as real results.
- **Not yet confirmed as shipped, do not claim in copy:** discount codes, referral program percentages, verification badge, community module, captions/watermark automation, storage tiers shown in the prototype. Ask the owner before promising any of them.

---

## 2. What made Shopify's blog work, and the AllCoaching version

| Shopify tactic | AllCoaching translation |
|---|---|
| Teaches the whole journey of a seller (idea → store → marketing → growth), not the product | Teach the educator's whole journey: start an academy → create the course → brand + domain → payments → marketing (SEO, Meta ads, YouTube, WhatsApp) → grow students and income |
| Pillar guides on head terms ("What is ecommerce", "Ecommerce SEO", "Business blueprint", "AI tools for ecommerce") | Pillars: "What is an online academy", "Online academy SEO", "Online coaching business blueprint", "AI tools to run an online academy", "Meta ads for coaching" |
| One consistent, calm reading template on every post | `blog-v3.css` layout on every new post |
| Product appears as the obvious next step, 3–5 soft CTAs, never the topic | Promo strip, left CTA card, 1–2 inline CTA cards, final dark band. Product named in 1–3 body paragraphs, by mechanism |
| Free trial CTA everywhere ("Start for free") | "Start free trial" → studio.allcoaching.in, "14 days free · No card needed" |
| Clean product screenshots on soft gradient panels | Studio screenshots in Apple-style device frames on the lavender canvas |
| Free tools as SEO magnets (business name generator, logo maker, calculators) | Build: academy name generator, course price calculator, title-tag/SERP preview tool, earnings calculator, syllabus-to-course outline tool |
| Encyclopedia/glossary pages for every term | Glossary section in every post (+ later a /glossary hub) |
| Exact-match H2 questions + FAQ at the end | Same, matched 1:1 to FAQPage JSON-LD |
| Popular posts / related grid, internal links everywhere | Right rail "Popular guides", bottom "More guides", 5–10 in-body links |

**Content mix to target:** 60% "how to" guides (build, sell, market), 20% "what is / definitions" pillars, 10% tools and calculators, 10% honest comparisons (with sourced competitor prices per CLAUDE.md).

---

## 3. Writing approach (new house style for guides)

Write like Shopify's best guides: a patient expert teaching a beginner, specific to India.

1. **Answer first.** The first sentence of the post and of every H2 section is a complete, quotable answer in plain words. Then explain.
2. **Problem before product.** Open with the educator's real situation ("You teach SSC maths in Hindi and grow on YouTube..."), never with AllCoaching.
3. **Short paragraphs** (2–4 sentences), one idea each. H2 → H3 hierarchy that mirrors real questions. Lists for steps and options, tables for comparisons.
4. **Numbered, followable steps.** Every guide has a 5–9 step procedure (`.v3-steps`) that becomes the HowTo schema.
5. **Indian specificity:** exam names, Hindi/Hinglish/regional medium, UPI, tier-2/3 phones, ₹ in lakhs. Use both exam and skill educators as examples.
6. **Evidence:** 2–5 cited facts from primary or well-known sources (Google Search Central, government sites, Ahrefs/Backlinko/Semrush studies, Meta/Google help centres) with `<sup><a href="#ref-n">` + a References list. First-party AllCoaching data only when the owner gave it (e.g. blog clicks 183 → 1,094, Jul → Sep 2026; 500+ educators selling). Never invent numbers; illustrative figures are labelled "illustrative".
7. **Experience (E-E-A-T):** at least 2 first-person lines from AllCoaching's real experience. Named author Amit Ratan, Founder & CEO.
8. **Voice:** calm, clear, confident. Say educator, studio, your students. No exclamation marks, no "unlock", "maximize", "creator", "#1", "cheapest", "game-changer". Use Indian English spelling: "optimise", "enrol".
9. **Product mentions:** 1–3 paragraphs, each tied to the step the reader is on ("Every AllCoaching plan includes connecting your own domain"). Only confirmed features (see `allcoaching` skill §4).
10. **Length:** 3,000–5,500 words for pillars, 1,800–3,000 for focused how-tos. Read time is computed by the sync script.

---

## 4. Layout: the v3 template

Stylesheets: `../brand.css` (footer, WhatsApp button) then `../blog-v3.css`. `<body class="v3">`. Fonts: Inter 300–700 (= Shopify's typeface, open source), IBM Plex Mono, Instrument Serif italic (wordmark only).

Page order (copy from the reference post):
1. `.v3-head` sticky header: logo lockup, Blog / Start an academy / Sell courses / Marketing / Pricing, Log in, black pill "Start free trial".
2. `.v3-promo` grey strip: "START YOUR ONLINE ACADEMY TODAY" + two buttons.
3. `.v3-hero`: eyebrow (BLOG • CATEGORY), H1 (Inter 330, 56px), grey dek, `.v3-cover` 16:9 cover.
4. `.v3-grid` three columns:
   - `.v3-left`: `.v3-toc` "On this page" (8–11 links, auto-highlights) + `.v3-sidecta` blue card.
   - `article.v3-body`: mobile byline, mobile TOC (auto-filled), mobile CTA card, then sections.
   - `.v3-right`: byline with read time + "Popular guides".
5. `.v3-more` four related cards, `.v3-band` dark sign-up band with the academy-features graphic, site footer.

Body components (all in `blog-v3.css`, no inline styles):
`.v3-keys#tldr` key takeaways · `.v3-fig` figure + figcaption · `.v3-steps#howto-steps` numbered steps (`<b>` name + `<span>` text) · `.v3-table` · `.v3-q` question box (inline Q&A) · `.v3-quote` pull quote · `.v3-pair` do/avoid cards · `.v3-cta` inline CTA card · `.v3-gloss#glossary` dl/dt/dfn/dd · `.v3-faq#faq` details/summary · `.v3-refs#references` · `.v3-author`.

---

## 5. Graphics: branded, minimal, Apple-style

Every post ships a cover + 6–12 in-article graphics. They are generated, never stock photos.

**Style rules (from the owner's approved creatives):**
- Lavender-white canvas; a grey left half only for "before / problem" comparisons.
- Heavy Inter Tight headline, tight tracking, near-black with ONE phrase in electric blue `#2B44FF`.
- White pill cards with soft shadow + dark navy icon tile and white line icon; light-lavender tiles with blue icons for feature rows.
- Real product: AllCoaching Studio screenshots inside MacBook + iPhone frames (`laptop()`, `phone()`).
- Real brand marks for the tools being discussed: `logo_google`, `logo_youtube`, `logo_instagram`, `logo_whatsapp` inside white app-icon tiles (`logo_tile`). Add "Logos belong to their owners" in the caption line when used.
- Handwritten Caveat notes + hand-drawn arrows + beige tape labels only on the problem side ("Plugin conflict again?", "Too many tools!").
- AllCoaching signature bottom-right on every in-article graphic; full lockup with tagline on cover and promo graphics.
- Blue CTA button "Start your academy →" only on promo graphics. Price line "Plans from ₹6,999/year + GST".
- Example data is labelled ("Illustrative", "sample data"). Fictional sites use `youracademy.in`.

**How to make them:**
1. Copy `graphics/seo-for-online-academy-beginners-guide.py` to `graphics/<slug>.py`, keep the imports, write one block per graphic using the primitives in `scripts/brand_graphics.py` (`svg`, `headline`, `lockup`, `signature`, `pill_card`, `feature_tile`, `white_panel`, `search_bar`, `result`, `check_row`, `tape`, `hand`, `arrow`, `button`, `num_badge`, `laptop`, `phone`, `logo_*`, `icon` with 35 line icons).
2. `python .claude/skills/academy-guide-blog/graphics/<slug>.py` writes SVG sources to `assets/blog/<slug>/`.
3. `python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/<slug>` renders WebP with real fonts (cover 1600×900, in-article 1220 px wide = 2× the 610 px column).
4. Look at every WebP before using it (overlaps, cut text). Fix and re-export.
5. In HTML: `<img src="/assets/blog/<slug>/<name>.webp" alt="<describes the content and includes the keyword naturally>" width="1220" height="<h>" loading="lazy" decoding="async">`; the cover gets `fetchpriority="high"` and a preload.

**Graphic menu (pick what the post needs):** cover · "before vs after" split · how-it-works 3-step cards · formula/matrix · annotated screenshot or page anatomy with numbered callouts · tree/structure · cluster/hub · timeline/roadmap · tools grid with real logos · mistakes with tape labels · product promo (devices + feature tiles + CTA).

---

## 6. Eligible for every search surface (per-post checklist)

### Google ranking + snippets
- [ ] One primary keyword (verify it is distinct from `blog/`, `blogs/en/`, `blogs/hinglish/` titles first) + 5–10 secondary long-tails in H2/H3s.
- [ ] `<title>` ≤ 60–65 chars: keyword first, then benefit/year. Matches H1 intent (H1 may be longer).
- [ ] Meta description 140–172 chars: what the reader gets + 2–3 concrete items + no fluff. Google rewrites weak ones, so mirror the intro's first sentence.
- [ ] Slug = short keyword phrase. Canonical, `lang="en-IN"`, OG/Twitter with 1600×900 cover, `article:*` times.
- [ ] `robots: max-image-preview:large, max-snippet:-1` (Discover + rich snippets).
- [ ] Featured-snippet shapes: a 40–60 word definition paragraph right under "What is X?", a numbered list for "how to", a table for comparisons.
- [ ] People Also Ask: H2/H3 written as the questions people type; 6–10 FAQs at the end.
- [ ] 5–10 in-body internal links with keyword anchors + links from 2–3 older posts to the new one (update them).
- [ ] Images: descriptive file names, alt text, width/height, WebP, lazy below the fold.
- [ ] Fresh: year in title when it matters, `dateModified` bumped on every real update, refresh pillars each exam cycle.

### AI Overviews, AI Mode, ChatGPT Search, Perplexity, Gemini, Claude
- [ ] Answer-first sentences that stand alone (the AI lifts the first 1–2 sentences of a section).
- [ ] Key takeaways (`#tldr`) with 5–7 bold-anchored facts.
- [ ] Specific entities everywhere: exam, language, tool names, ₹ figures, years.
- [ ] Cited statistics + References; at least one quote from an authority (Google docs, official body, named expert).
- [ ] Named author with Person schema and `sameAs`; first-person experience lines.
- [ ] Glossary with `<dfn>` (DefinedTermSet) for "what is" retrieval.
- [ ] Six JSON-LD blocks: Article (+TechArticle, about/mentions with Wikipedia sameAs, speakable, citation, wordCount, audience, isPartOf) · FAQPage · BreadcrumbList · HowTo · SoftwareApplication (AllCoaching, AggregateOffer ₹6,999–₹24,999) · DefinedTermSet.
- [ ] Entry in `llms.txt` (dense, entity-rich, top of the English blog list) and rebuilt `llms-full.txt`.
- [ ] Brand mentions off-site plan: YouTube description, LinkedIn post, Quora/Reddit answer that cites the guide (see `blog-post` repurposing kit).

### Run before finishing
```
python .claude/scripts/v3_sync_schema.py blog/<slug>.html        # FAQ/HowTo/Glossary JSON-LD from DOM, wordCount, read time
python .claude/scripts/blog_layout_lint.py blog/<slug>.html       # classes, JSON-LD parse
python .claude/scripts/verify_meta_opt.py                         # titles ≤65, descriptions 50–175, JSON-LD valid
python .claude/scripts/register_<slug>.py                         # copy register_seo_academy_guide.py: sitemap, llms.txt, blog/index.html
python .claude/scripts/refresh_blogs_index.py && python .claude/scripts/refresh_blogs_en_index.py
python .claude/scripts/build_llms_full.py && python .claude/scripts/build_feed_xml.py
```
Then screenshot the page at 1440 and 390 px (no horizontal scroll, TOC highlights, images sharp), scan for banned words, and **stop: never commit or push without the owner asking** (CLAUDE.md).

---

## 7. Content roadmap

The educator-growth calendar (20 English posts, deduplicated against existing posts, with REFRESH items that reuse existing URLs) is in `roadmap.md` next to this file. All new posts are written in English. Update its status column as posts ship.
