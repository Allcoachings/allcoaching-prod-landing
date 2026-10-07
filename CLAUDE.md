# AllCoaching — marketing site (allcoaching.in)

This repo is the static marketing site + blog for **AllCoaching** (AllCoaching Technologies) — India's educator-first EdTech marketplace. Deploys from GitHub `master`.

## Load context first
- **Company context (canonical):** invoke the `allcoaching` skill (`.claude/skills/allcoaching/SKILL.md`) whenever working on anything AllCoaching — product, pricing, brand, blog, strategy. It is the source of truth; don't contradict it.
- **Writing a blog post:** use the `blog-post` skill (house style, 6-schema JSON-LD scaffold, registration flow).
- **AI-search/GEO decisions:** use the `ai-search-geo` skill.

## Non-negotiable facts (summary — full detail in the allcoaching skill)
- **Free trial (confirmed 2026-10-07):** every plan starts with a **14-day free trial — no card needed to start**, then the educator picks a plan. A trial is not a free tier. Main pricing page is **/pricing** (`/plans` 301s to it); the homepage shows no prices and links to /pricing.
- **Pricing (confirmed 2026-09-28 — THREE annual plans, supersedes the one-time model):** **Starter ₹6,999/year** (10% platform fee, keep 90%), **Growth ₹12,999/year** (7.5%, keep 92.5%), **Pro ₹24,999/year** (5%, keep 95%, plus a premium website template). Every plan includes the educator's own connected custom domain, live classes (hours by plan: 5/10/15 per month), and marketplace discovery. Prices exclude GST. Upgrades take effect on payment with the unexpired value credited; downgrades go through support at next renewal; a non-renewed academy goes offline to students but content/data stay exportable. **There is no free tier.** Never write "₹0 to start", "free forever", "one-time fee", "no subscription" (there is an annual one), "far below a typical X/month subscription" or other cheap-positioning language — see the next bullet. Third-party free tiers (Zoom, Loom, Canva, competitors) must be preserved when editing.
- **Positioning:** core message is **"Launch your online academy yourself"** — fully self-serve (sign up → choose plan → upload course → connect domain → set up payment → publish → sell), explicitly **no sales call, no demo dependency, no technical team required**. **Never position AllCoaching as a "cheap/cheapest LMS."** The differentiator is *simple, transparent, self-driven* pricing, not low cost — say "one predictable annual plan," not "far below a typical monthly subscription."
- **Competitor pricing:** naming a rival's price is a claim about them. State the source per figure, show their transaction fee next to the fixed cost (Learnyst and Edmingle take 0%, we take 10% down to 5%), and never round up. Classplus publishes no pricing on its own site — any figure is a third-party listing and must say so.
- **Voice:** say *educator* (not creator/user), *studio* (not dashboard). No exclamation marks, no "#1 platform" claims, no fabricated stats — ₹ ranges only, illustrative figures marked as illustrative.
- **Fonts:** Instrument Serif (italic display) + Inter Tight + JetBrains Mono. **Fraunces is NOT a brand font.** Ochre `#C58B43` is the only accent.
- **Contact email:** contact@allcoaching.in (old gmail must never reappear).

## Workflow rules
- **Never `git commit` or `git push` without the user explicitly asking.** Stage, verify, report, then stop and wait.
- New blog posts: verify the keyword is distinct from existing posts (`blog/`, `blogs/en/`, `blogs/hinglish/`) before writing; register in sitemap.xml, llms.txt, blog/index.html; run the refresh scripts (`.claude/scripts/refresh_blogs_index.py`, `refresh_blogs_en_index.py`, `build_llms_full.py`, `build_feed_xml.py`); validate with `.claude/scripts/verify_meta_opt.py` (titles ≤65 chars, descriptions 50–175 chars, valid JSON-LD).
- FAQ/glossary JSON-LD must match the visible DOM **verbatim** (question count and text 1:1).
- `.claude/settings.local.json` is personal — never commit it.
