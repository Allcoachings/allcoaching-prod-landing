# Brief: rewriting AllCoaching comparison and alternative posts (v3)

Reference implementation (copy its structure):
- Content: `.claude/skills/academy-guide-blog/content/classplus-alternative-for-coaching-institutes.json`
- Graphics spec: `.claude/skills/academy-guide-blog/graphics/specs/classplus-alternative-for-coaching-institutes.json`
- Output: `blog/classplus-alternative-for-coaching-institutes.html`

Read first: `CLAUDE.md`, `.claude/skills/allcoaching/SKILL.md`, `.claude/skills/academy-guide-blog/SKILL.md`, and the verified facts in `.claude/skills/academy-guide-blog/data/competitors.json` (+ `claims-audit.md`).

## Why we are rewriting
These posts get impressions but few clicks, and they carry the old marketplace-first positioning plus some unsourced competitor claims. The rewrite must (1) earn the click with a specific, trustworthy title and description, (2) be fair and verifiable, (3) present AllCoaching as "the academy platform for educators" (own website + own Android/iOS app, built yourself, like Shopify for coaching), and (4) convert with clear trial CTAs.

## Keep
- The same slug, folder and URL. `date_published` from `content/_inventory.json`; `date_modified` = "2026-10-24".
- The search intent of the old post (its keywords are in `_inventory.json`). Do not change what query the page answers.
- Language: posts in `blogs/hinglish/` stay in Hinglish (Roman-script Hindi + English), with `"lang": "hi-Latn"`; everything else English (`en-IN`).

## Facts rules (non-negotiable)
1. Competitor prices, fees, trials, plan names: ONLY from `competitors.json`, with its source URL and "checked 24 Oct 2026". If it says not published, write "not listed on its website (checked 24 Oct 2026)". Never estimate, never round, never take from third-party sites.
2. Do not repeat claims that `claims-audit.md` marks contradicted or unsupported. Phrase open points as questions to ask the vendor ("Ask whether...").
3. No "per public reports", "users complain", review-site summaries or anecdotes. No invented numbers, cohorts, students or stories.
4. AllCoaching facts only from the `allcoaching` skill: 7-day free trial, no card; Starter ₹6,999 + 10%, Growth ₹12,999 + 7.5%, Pro ₹24,999 + 5%, Scale ₹99,999 + 0% (contact us) a year, GST extra; own domain + own Android app on every plan, iOS app on Pro and Scale + unlimited live classes (YouTube Live, Zoom, built-in room) + unlimited YouTube videos + UPI/card checkout with automatic Razorpay payouts + Meta Pixel/GTM + data export + marketplace discovery as a supporting extra; 500+ educators selling. Banned: "free forever", "₹0", "free plan", "one-time", "no subscription", "cheapest", "daily payouts", payout speed, "flat 10%", live-hour caps, "shared app", DRM/anti-piracy as a confirmed feature, "#1", exclamation marks, "creator" for educators (fine when describing a competitor's own audience), "unlock", "maximize".
5. Fairness: every post must say where a competitor (or staying put) is the better choice, include the disclosure note (AllCoaching wrote this; sources dated; contact@allcoaching.in for corrections), and describe each competitor by what it is good at, in its own words.
6. Cost maths: never hand-type cost tables. Put plans in the graphics spec `cost` block and write `{{cost_table}}` in the content; the builder computes it. Breakeven figures in prose must be computed: AllCoaching total = min(6999 + 0.10·S, 12999 + 0.075·S, 24999 + 0.05·S, 99999).
7. For edtech brands/marketplaces (Physics Wallah, Unacademy, Vedantu, Testbook, Adda247, Toppr, Extramarks, Udemy, Cuemath, Aakash): they are mostly employers/marketplaces, not software you buy. Compare the educator's options (teach for them vs build your own academy vs both), using only officially published terms (e.g. Udemy's instructor revenue share page) and otherwise "not published".

## Click-through (titles and descriptions)
- `title` ≤ 60 characters (hard max 65): primary keyword first + year + a concrete trust or number hook. Patterns: "Best X Alternative (2026): N Options, Prices Checked" · "X vs Y (2026): Prices, Fees and Which to Pick" · "X Alternative for Educators: Own Your App (2026)". No clickbait, no "#1".
- `description` 140–172 characters: who it is for + what is compared + one specific fact or promise ("prices from each official site", "when to stay on X"). Must read naturally.
- `h1` can be longer and fuller than the title.
- The first sentence of `intro` is the direct answer to the query, quotable on its own.

## Conversion
- Inline `{{cta}}` after the cost or options section; the shell already adds promo strip, left CTA card, final band.
- One option card for AllCoaching marked `us` with the disclosure tag; position it where it honestly fits (often first for "alternative" intent, never claimed as best for everyone).
- A "Which one fits you" section by educator type and a switch/start section with `{{steps}}` (HowTo).

## Structure (sections, in order; adapt headings to the query)
1. `quick-answer` – short answer + `{{fig:verdict|...}}`
2. `how-we-compared` – criteria list + disclosure `<div class="v3-note">`
3. `why-switch` (or the honest context section) – fair reasons, a `{{q:...|...}}` box, `{{fig:before-after|...}}` where relevant
4. `alternatives` – one `<div class="v3-opt">` card per option (dl: Good at / Published price / Free trial / Check / Best for) + `{{fig:prices|...}}`
5. `comparison-table` – HTML `.v3-table` of published facts ("Not stated" where the source is silent) + links to `/vs/*` pages when they exist
6. `cost` – `{{fig:cost|...}}` + `{{cost_table}}` + honest reading + `{{cta}}` (only when at least one competitor publishes prices; otherwise explain why a cost comparison is not possible and show AllCoaching's own cost at sales levels)
7. `choose` – by educator type, with 3–5 internal links (keyword anchors, existing pages only)
8. `switch` – `{{fig:switch|...}}` + `{{steps}}` + link to `/blog/switch-coaching-apps-without-losing-students`
Then `faq` (6–8 Q/A, plain-text answers, first sentence answers the question), `glossary` (4–6 terms), `references` (every source used, numbered to match `<sup><a href="#ref-n">` marks), `about`/`mentions`, `related` (4 existing paths).

Length: 2,200–3,500 words. Short paragraphs, plain words, Indian examples (NEET, JEE, SSC, UPSC, banking, CBSE tuition, yoga, spoken English).

## Graphics spec
Copy the reference spec and change: `slug`, cover `lines` (query phrased as a question, one *blue* phrase) and `options` (≤6, AllCoaching last), `verdict.rows` (3–5), `prices.rows` (published only, else published:false), `cost.competitors` (only published plans: `[[yearly_price, fee_fraction], ...]` + a note when a fee is not stated or a minimum applies), `switch.steps` (4), `before_after` (tapes/checks fitting the reader). Then:

```
python .claude/skills/academy-guide-blog/scripts/comparison_graphics.py .claude/skills/academy-guide-blog/graphics/specs/<slug>.json
python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/<slug>
python .claude/scripts/build_v3_post.py .claude/skills/academy-guide-blog/content/<slug>.json
python .claude/scripts/blog_layout_lint.py <dir>/<slug>.html
```
Open every exported WebP (Read tool) and fix overlaps or clipped text before building. Delete any `.svg/.webp` you generated by mistake. Do not touch `sitemap.xml`, `llms.txt`, index pages, feeds or other posts; the lead handles registration.

## Done means
- HTML built, lint shows 6 JSON-LD blocks and 0 parse errors, title ≤ 65, description 140–175.
- No `{{` placeholders left in the HTML (`grep -c "{{"` = 0).
- Banned-word scan clean.
- Report per post: final title, description, word count, competitors cited with source URLs, and anything you could not verify.

## Special cases from the 24 Oct 2026 fact check (read `data/competitors.json` notes)
- **Graphy:** rupee prices could NOT be confirmed (the pricing page geo-redirected to US prices). Do not print any Graphy ₹ plan price or per-sale % anywhere, including old figures (₹24,999 / ₹49,999 / ₹99,999, ₹1,999/month, ₹2,800, ₹4,200). Write: "Graphy publishes plans on graphy.com/pricing, but prices are shown by country and we could not confirm the Indian rupee plans on 24 Oct 2026; check the page from India." Graphy is `published:false` in price graphics and excluded from cost charts. You may cite its 7-day trial and its own description.
- **Spayee:** spayee.com now redirects to graphy.com (checked 24 Oct 2026). Say so plainly; treat former Spayee users as now on Graphy.
- **Winuall:** winuall.com now redirects to an unrelated site (checked 24 Oct 2026). Write the post for institutes that used Winuall and need a new home; do not describe Winuall's current product or prices.
- **Rigi:** rigi.club now presents a different product (a short-video app). Say Rigi has changed direction; focus the post on Exly and the reader's options.
- **Toppr** (site unreachable), **Aakash franchise** (only a closed 2019 application page found), **Cuemath** (site now targets US students): describe only what is verifiable; otherwise frame as "check current terms directly".
- **Learnyst:** Launcher ₹10,000/yr + 10%; Professional/Premium/Business ₹8,999/₹14,999/₹49,999 a month (₹8,099/₹13,499/₹44,999 billed annually) with 0% transaction fees; taxes extra; apps under Learnyst's developer account. Never write "Learnyst takes 0%" without naming the plan.
- **Edmingle:** Core/Prime/Power ₹7,499/₹14,999/₹29,999 a month billed annually; fee on sales not stated (do not write 0%); 7-day free start.
- **Udemy:** revenue share could not be verified; do not state a percentage. **Vedantu** publishes its own teacher-earning claims ("₹25,000+ to ₹75,000+ per month"); quote only as Vedantu's claim, with source.
- USD platforms (Kajabi, Teachable, Thinkific, Skool, Circle, Tutor LMS, LearnDash): quote in USD exactly as published, say prices are in US dollars and exclude Indian GST; do not convert to ₹ unless you state the date and that it is an approximate conversion (prefer not converting).
- Old unsupported figures flagged in `claims-audit.md` (e.g. "₹4–11 lakh Year-1 trap", "12–18 day median migration", "25–65% acquisition") must be removed, not reworded.
