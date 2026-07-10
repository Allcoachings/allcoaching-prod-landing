---
name: allcoaching
description: >-
  Canonical context for AllCoaching (allcoaching.in) — India's educator-first EdTech
  marketplace: what the product is, the free-forever + flat-10% pricing truth, the
  "Operating System of Education" ideology/manifesto, brand identity + voice, target
  audience, competitive positioning, and key company facts. Load this WHENEVER the
  user mentions AllCoaching, or works on its website / blog / marketing / brand /
  product / pricing / strategy — so the context is already known before responding.
  Global reference skill; the deeper execution skills (blog-post, ai-search-geo) and
  live implementation live inside this repo.
---

# AllCoaching — core context & ideology

Use this as the ground truth about the company. If a request touches AllCoaching, assume these facts; don't re-derive or contradict them. When something below is marked **unverified**, do not assert it — ask or leave it out.

## 1. What AllCoaching is (one line)
AllCoaching (**allcoaching.in**) is an **educator-first EdTech marketplace** for India's independent educators — coaching-institute owners, tutors, and subject experts. It gives each educator a **branded white-label studio (web + app)** to run their whole teaching business, *plus* a **shared marketplace** so students can discover them. Legal entity: **AllCoaching Technologies Pvt. Ltd.** Founded **2022**. Category: **EdTech Marketplace**.

- **Tagline:** *Democratizing Education.*
- **Positioning:** *The Operating System of Education.*
- **Founder / voice of the brand:** **Amit Ratan, Founder & CEO** (author of the manifesto and blog byline).
- **Studio product** (the educator app) lives at **studio.allcoaching.in** — a **separate repo/codebase** (no access from the marketing repo). Marketing site links `Log in` → studio.allcoaching.in/login, `Join now` → studio.allcoaching.in.

## 2. The ideology (the manifesto thesis — *why it exists*)
The founding argument, in order:
1. **The Pandemic Mirage** — COVID handed every educator a "personal app / own your students" dream. The lockdown ended; the **fragmentation didn't**. Personal apps produced isolation, debt, abandoned courses, empty classrooms.
2. **The Educator's Trap** — a good teacher is forced to become a marketer, app-maintainer, and payment-ops person. *"A teacher who has to think about student acquisition, app maintenance, payment gateways, and marketing budgets has already stopped being a teacher."* Every rupee on ads / hour on reels is one not spent on teaching.
3. **The Student's Nightmare** — 3.5 lakh isolated apps, zero discovery. The best teacher is invisible behind a download wall no one knows to climb.
4. **Big EdTech is not the educator's friend** — it advertises the loudest, not the best; it rents the educator's audience.
5. **The Missing Layer** — Indian EdTech never built a **network effect for individual educators**. AllCoaching *is* that layer: a marketplace that gets stronger with every educator who joins.
6–8. **The Operating System of Education** — the educator owns their identity and student relationship; the platform supplies discovery + infrastructure so their **only job is to teach**.

**Core beliefs (verbatim manifesto tenets):** teaching is a *vocation, not a startup*; quality education is held hostage by inferior infrastructure; the internet's promise of scale to education hasn't been kept; **network effects should serve educators, not exploit them**; a student should find the *best* teacher, not the *most advertised* one; we are building the world's most **educator-centric** EdTech marketplace, honestly.

**What it does differently:** structured discovery replaces paid marketing · a marketplace that compounds with every educator · educator owns the relationship (their brand, not ours) · zero technical dependency for the educator · one student app solves the download-fatigue problem · transparent revenue sharing, no hidden charges.

## 3. Pricing truth (⚠️ money claim — get this exactly right)
**Confirmed model (as of 2026-07):**
- **₹0 free-forever BASE** — no card, no KYC, no contract at signup; the free part **never expires**.
- **Flat 10% platform fee, charged only on what the educator sells** — educator **keeps 90%**. **Daily INR payouts.**
- **Optional paid Pro tier (~₹999–4999/month)** unlocks **advanced features: custom domain, advanced analytics, priority support** — buying it is optional; the base stays free whether or not you upgrade.
- **NEVER frame it as:** "30-day free trial → then a plan", "premium trial that ends", "free trial · then plan". There is **no trial that expires and no forced upgrade**. The free base is permanent.
- Money in ₹ only (lakhs/crores, e.g. `₹4.8L`, `₹1.2Cr`) — never `$` / "INR" / "rupees". Use **ranges**, never fabricated exact stats.

## 4. Product / feature scope (don't over-claim)
- **Confirmed FREE-tier features:** branded white-label studio (web + app), live classes, recorded courses, test series, payments (UPI/card + daily payout), student CRM, marketplace discovery. **Multi-teacher institutes are FREE-included** (separate teacher logins, batch ownership; split is platform-10% / institute-90%, institute handles its own internal teacher pay — no auto-split claim).
- **Paid Pro-tier only:** custom domain, advanced analytics, priority support.
- **UNVERIFIED — do NOT state as free-included:** video DRM / anti-piracy, GST-invoicing. Treat these as *concepts you can explain*, never as confirmed AllCoaching free features.

## 5. Audience & positioning
- **Audience:** India's ~**3.5 lakh independent educators** — coaching owners, tutors, exam mentors, subject/skill teachers; Hinglish- and regional-language-aware; cost-anxious tier-2/3 included.
- **Say "educator", not "creator"/"user".** Lead with what the educator gets.
- **Competitive stance:** the alternative to *both* (a) DIY personal apps (isolation, no discovery) *and* (b) Big-EdTech platforms that rent your audience / take large cuts (Classplus, Graphy, Teachmint, Unacademy, Byju's, Udemy, etc.). AllCoaching = own-brand studio **+** shared marketplace network effect, zero-commission-style economics (flat 10%, keep 90%).

## 6. Brand & voice (apply to any AllCoaching surface)
Full system is the `brand-system` memory + repo `brand.css`; the essentials:
- **3 fonts, each one job — Fraunces is NOT a brand font.** Display = **Instrument Serif** *italic, weight 400 only* (headlines, KPI values, wordmark; emphasis via **colour**, never bold). UI = **Inter Tight** (body/buttons/nav; default emphasis 600). Mono = **JetBrains Mono** (numbers, eyebrows, IDs, code).
- **Colour:** warm **cream** canvas (`#FAF8F4`), **ochre is the ONLY spotlight accent** (core `#C58B43`, deep `#8E5F22`) — owns every CTA / live-ribbon / educator-name. No second accent. Ink `#15110D`. Semantic colours = meaning only.
- **Voice:** calm, confident, editorial (not corporate); educator-first; restraint over decoration. Say **educator / studio / your students** (not creator / dashboard / audience). **Banned:** exclamation marks, "maximize", "onboard" (verb), "unlock", "creator", "#1 platform" ranking claims, stock photos. Confidence from accuracy, not hype.
- **Logo:** rounded-square gradient pin + wordmark in Instrument Serif italic 400 (always italic). Tagline "Democratizing Education" in mono, ochre shimmer.
- Accessibility + reduced-motion always respected; AA contrast.

## 7. Key facts & links
- Domain **allcoaching.in** · Studio **studio.allcoaching.in** (separate repo).
- Public contact email: **contact@allcoaching.in** (since 2026-07-08; the old gmail must never reappear). Founder's personal amitpc95@gmail.com appears only on the author page.
- Socials: LinkedIn `in/allamitk`, X `@allcoachings`, YouTube `@Allcoaching`, Instagram `allcoachings`, Facebook, Telegram.
- Analytics: **GTM-T3KFKD3G** (no GA4/Ads/Meta IDs committed in the marketing repo). A marketing-site tracking layer (`assets/track.js`) exists on a local unpushed branch.
- Marketing repo (this machine): `c:\Users\allco\codes\allcoaching-prod-landing`. Static site deployed from GitHub `master`. Discovery files: `sitemap.xml`, `llms.txt`, `llms-full.txt`, `robots.txt` (all AI-citation crawlers allowed, data-resale scrapers blocked).

## 8. When working *in* the marketing repo, defer to these
- **Skills (project-level, richer):** `blog-post` (house style + HTML component system + 6-schema scaffold + registration) and `ai-search-geo` (GEO/AEO strategy — answer-first, entity-anchored, citation-shaped). Use both when writing/optimizing content.
- **Active project:** a **daily 2-blog pipeline for July 2026** — 60 AEO full-conversational-query keywords in `.claude/content-calendar-july-2026.md`, all distinct from the existing ~70 blogs; the user assigns a daily task, Claude completes that day's 2 blogs. (See the repo's `MEMORY.md` index.)

## 9. Guardrails (non-negotiable)
- **Never fabricate** stats, cohort sizes, student anecdotes, sources, or `sameAs` URLs — YMYL topic; fabrication breaks trust and suppresses AI citation.
- **Never** use the outdated "trial-that-ends" pricing framing (§3).
- **Commit/push only when the user explicitly asks** — stage, verify, then stop and wait.
- Keep the free vs paid vs unverified feature boundary (§4) exact.
- New keyword/blog work must be **distinct from existing content** — verify before writing.
