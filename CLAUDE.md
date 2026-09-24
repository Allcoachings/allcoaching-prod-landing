# AllCoaching — marketing site (allcoaching.in)

This repo is the static marketing site + blog for **AllCoaching** (AllCoaching Technologies) — India's educator-first EdTech marketplace. Deploys from GitHub `master`.

## Load context first
- **Company context (canonical):** invoke the `allcoaching` skill (`.claude/skills/allcoaching/SKILL.md`) whenever working on anything AllCoaching — product, pricing, brand, blog, strategy. It is the source of truth; don't contradict it.
- **Writing a blog post:** use the `blog-post` skill (house style, 6-schema JSON-LD scaffold, registration flow).
- **AI-search/GEO decisions:** use the `ai-search-geo` skill.

## Non-negotiable facts (summary — full detail in the allcoaching skill)
- **Pricing (confirmed 2026-09-23 — ONE price, nothing else):** **₹6,999 one-time onboarding**, paid once, covering everything including the educator's own custom domain and live classes. Then a **flat 10% on completed sales — educator keeps 90%**, daily INR payouts. A month with no sales costs nothing. **There is no free tier any more.** Never write "₹0 to start", "free forever", "free tier/base/plan", "no card at signup", "no setup fee", "start free", "Pro tier", a ₹10,000 custom-domain charge, or metered live-class plans — all were true in earlier models and are now false. Third-party free tiers (Zoom, Loom, Canva, competitors) must be preserved when editing.
- **Competitor pricing:** naming a rival's price is a claim about them. State the source per figure, show their transaction fee next to the fixed cost (Learnyst and Edmingle take 0%, we take 10%), and never round up. Classplus publishes no pricing on its own site — any figure is a third-party listing and must say so.
- **Voice:** say *educator* (not creator/user), *studio* (not dashboard). No exclamation marks, no "#1 platform" claims, no fabricated stats — ₹ ranges only, illustrative figures marked as illustrative.
- **Fonts:** Instrument Serif (italic display) + Inter Tight + JetBrains Mono. **Fraunces is NOT a brand font.** Ochre `#C58B43` is the only accent.
- **Contact email:** contact@allcoaching.in (old gmail must never reappear).

## Workflow rules
- **Never `git commit` or `git push` without the user explicitly asking.** Stage, verify, report, then stop and wait.
- New blog posts: verify the keyword is distinct from existing posts (`blog/`, `blogs/en/`, `blogs/hinglish/`) before writing; register in sitemap.xml, llms.txt, blog/index.html; run the refresh scripts (`.claude/scripts/refresh_blogs_index.py`, `refresh_blogs_en_index.py`, `build_llms_full.py`, `build_feed_xml.py`); validate with `.claude/scripts/verify_meta_opt.py` (titles ≤65 chars, descriptions 50–175 chars, valid JSON-LD).
- FAQ/glossary JSON-LD must match the visible DOM **verbatim** (question count and text 1:1).
- `.claude/settings.local.json` is personal — never commit it.
