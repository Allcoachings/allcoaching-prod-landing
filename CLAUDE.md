# AllCoaching — marketing site (allcoaching.in)

Static marketing site + blog for **AllCoaching** (AllCoaching Technology), founder & CEO Amit Ratan. Deploys from GitHub `master`. The educator app (studio.allcoaching.in) is a separate codebase.

## Load first (always)
- **`allcoaching` skill = MASTER source of truth** (`.claude/skills/allcoaching/SKILL.md` + `references/01–13`: product/studio, pricing, brand/design, voice/claims, ads, social, SEO, tracking, repo/deploy, competitors, growth/scale, decision log, checklists). Load it FIRST for anything AllCoaching. Don't contradict it; correct requests that conflict with it.
- **Blog ("blog likho")** → `academy-guide-blog` skill (v3 layout, graphics, pipeline). `ai-search-geo` for GEO strategy, `behavioral-search` for query selection, `blog-post` only for legacy essay posts / JSON-LD reference.
- History of every owner decision and every retired model: `.claude/skills/allcoaching/references/12-decision-log.md`. Only the current facts below are valid.

## Current facts (summary — detail in the master skill)
- **Concept:** educators build their own LMS / academy with **full control** (brand, own domain, own Android app, iOS on Pro monthly and every yearly plan, students, data). Works like Shopify for coaching: sign up → choose a plan → upload your course → connect your domain → start selling. Marketplace listing is a supporting extra. Never cheap/cheapest positioning.
- **Pricing (studio = final, 2026-10-29):** 7-day free trial, no card. **Monthly, 0% commission:** Starter ₹3,999 · Growth ₹5,999 (Most popular) · Pro ₹7,999 (Best value · Recommended). **Yearly, fee per sale:** Starter ₹6,999 + 10% · Growth ₹12,999 + 7.5% · Pro ₹24,999 + 5%. Prices + 18% GST. No sales limit, no setup fee. "0% / keep 100%" = monthly only. Full plan table, cost maths and rules: `references/02-pricing.md`.
- **If an educator stops:** offline at end of paid period → 30 days to export or come back → uploaded videos deleted.
- **Never claim:** free plan / free forever / ₹0 / one-time / lifetime; AI question or test generation; a live or free product demo (`/demo/` retired → redirects to /start); 14-day trial; Scale; Growth ₹7,999/mo or Pro ₹14,999/mo; ₹79,990 / ₹1,49,990; Extend packs; sales limits; payout speed; guaranteed students/income; "#1", "cheapest"; fabricated or unsourced stats. Full register: `references/04-voice-and-claims.md`.
- **Real features (owner-confirmed):** test series with all-India rank and percentile, anti-cheat lock, random order; certificates; bulk student import; auto-built course pages with SEO/schema/checkout; 500+ educators.
- **Showcase:** Biology Lessons (Dr. Subhash Nair), CHEMPSI (Anupam Kumar), DigiteKM — names, logos, site screenshots only; no numbers, no quotes.
- **Competitors:** cite source + check date, show their fee next to their price, never round up (`references/10-competitors.md`).
- **Voice:** educator (not creator/user), studio (not dashboard); no exclamation marks; illustrative numbers marked.
- **Look:** white/mist, electric blue `#2B44FF` only accent, navy `#0A0F3D` footer, Inter Tight 200 + 700 headlines, Instrument Serif italic wordmark, JetBrains Mono eyebrows; full guide at /brand.
- **Contact:** contact@allcoaching.in · WhatsApp +91 98899 77262.

## Workflow rules
- **Never `git commit` or `git push` without the owner explicitly asking.** Stage, verify, report, then stop. Deploy flow: `references/09-website-and-repo.md`.
- When a fact changes: update the master skill + decision log, then sweep every surface (pages, blogs, `sources/`, `llms.txt`, schema, ads, other skills).
- New blog posts: keyword distinct from existing posts; register in sitemap.xml, llms.txt, blog/index.html; run `refresh_blogs_index.py`, `refresh_blogs_en_index.py`, `build_llms_full.py`, `build_feed_xml.py`; validate with `verify_meta_opt.py` (titles ≤65, descriptions 50–175, valid JSON-LD).
- FAQ/glossary JSON-LD must match the visible DOM **verbatim**.
- Never send test events to production Meta/Google.
- `.claude/settings.local.json` is personal — never commit it.
- The owner uploads the `allcoaching` and `academy-guide-blog` skills to claude.ai as zips; after changing either, give the owner a fresh zip.
