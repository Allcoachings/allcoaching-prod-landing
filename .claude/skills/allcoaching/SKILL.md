---
name: allcoaching
description: >-
  Canonical context for AllCoaching (allcoaching.in) — India's educator-first EdTech
  marketplace: what the product is, the 14-day-trial + three-annual-plan pricing truth, the
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
AllCoaching (**allcoaching.in**) is an **educator-first EdTech marketplace** for India's independent educators — coaching-institute owners, tutors, and subject experts. It gives each educator a **branded white-label studio (web + app)** to run their whole teaching business, *plus* a **shared marketplace** so students can discover them. Legal entity: **AllCoaching Technologies** (not "Pvt. Ltd."). Founded **2018** in Prayagraj. Category: **EdTech Marketplace**.

- **Tagline:** *Democratizing Education.*
- **Positioning (ideology):** *The Operating System of Education.*
- **Positioning (confirmed 2026-10-08, lead with this):** **"Sell your courses online. Your way."** Two ways to sell, one account: (1) list courses on the AllCoaching marketplace, where students on Android, iOS and web discover and buy them; (2) launch a full white-label academy yourself — connect your own domain for your website, publish your own app on Google Play, and use the built-in marketing tools to sell under your own brand. Plug and play, no developer. Homepage shows NO founding year or city ("no legacy, no place") — keep "2018"/"Prayagraj" off marketing pages (legal/contact/about pages may keep the registered address).
- **Earlier product line (still valid as support copy):** **"Launch your online academy yourself."** Website on the educator's own domain, the AllCoaching app on Android, iOS and web, live classes, payments and marketplace discovery — all from one login. No WordPress, no separate LMS, no developer, no sales call, no demo dependency.
- **Founder / voice of the brand:** **Amit Ratan, Founder & CEO** (author of the manifesto and blog byline).
- **Studio product** (the educator app) lives at **studio.allcoaching.in** — a **separate repo/codebase** (no access from the marketing repo). Marketing site links `Log in` → studio.allcoaching.in/login, `Start free trial` → studio.allcoaching.in.

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
**Confirmed model (2026-10-07; supersedes free-forever, flat-10%, one-time and "Pro ~₹999/month" — all wrong now):**
- **14-day free trial on every plan** — sign up, build the academy, then pick a plan. It is a *trial*, **not a free tier**: there is no free-forever plan. **No card is needed to start the trial** (user-confirmed 2026-10-07). Still unconfirmed: what happens to the academy when a trial lapses — don't claim it.
- **Three annual plans (prices exclude GST):** **Starter ₹6,999/yr** (10% platform fee, keep 90%, 512 GB, 1080p, 5 live hrs/month) · **Growth ₹12,999/yr** (7.5%, keep 92.5%, 1 TB, 1080p, 10 hrs) · **Pro ₹24,999/yr** (5%, keep 95%, 3 TB, 4K, 15 hrs, premium website template worth ₹10,000).
- **Every plan:** own connected custom domain, website templates, the AllCoaching app on Android/iOS/web, marketplace discovery, UPI/card checkout, **T+3 payouts**, student CRM, separate teacher logins, data export.
- Upgrades apply on payment with paid value credited; downgrades via support at next renewal; a non-renewed academy goes offline to students but content/data stay exportable. No setup fee, no monthly bill.
- **Never** position as "cheap/cheapest LMS". The register is *simple, transparent, self-driven*: one predictable yearly plan.
- Cost breakevens (illustrative, pre-GST): Starter is lowest below ~₹2.4L/yr sales, Growth ₹2.4–4.8L, Pro above ₹4.8L. Live pricing page: **/pricing** (`/plans` 301s there).
- Money in ₹ only (lakhs/crores, e.g. `₹4.8L`, `₹1.2Cr`) — never `$` / "INR" / "rupees". Use **ranges**, never fabricated exact stats.

## 4. Product / feature scope (don't over-claim)
- **Included on every plan:** branded studio, academy website from templates, own custom domain, the AllCoaching app (Android, iOS, web), live classes (5/10/15 hrs by plan), recorded courses, PDF notes, test series, UPI/card payments with T+3 payouts, student CRM, marketplace discovery, data export. **Multi-teacher institutes** are included (separate teacher logins, batch ownership; the institute handles its own internal teacher pay — no auto-split claim).
- **Pro only:** premium website template (₹10,000 value), 4K video. There is **no** "paid tier for custom domain / advanced analytics" — that was never true.
- **Own Google Play app:** confirmed as part of the white-label path (2026-10-08). Which plans include it is NOT confirmed — don't put it in plan tables until the user says so. Marketing tools: confirmed to exist; don't list specific tools until confirmed.
- **UNVERIFIED — do NOT state as free-included:** video DRM / anti-piracy, GST-invoicing. Treat these as *concepts you can explain*, never as confirmed AllCoaching free features.

## 5. Audience & positioning
- **Audience:** India's ~**3.5 lakh independent educators** — coaching owners, tutors, exam mentors, subject/skill teachers; Hinglish- and regional-language-aware; cost-anxious tier-2/3 included.
- **Say "educator", not "creator"/"user".** Lead with what the educator gets.
- **Competitive stance:** the alternative to *both* (a) DIY personal apps (isolation, no discovery) *and* (b) Big-EdTech platforms that rent your audience / take large cuts (Classplus, Graphy, Teachmint, Unacademy, Byju's, Udemy, etc.). AllCoaching = own-brand studio **+** shared marketplace network effect, transparent economics (one yearly plan, platform fee 10% → 5%, keep 90–95%).

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
- **Always** state pricing per §3: 14-day free trial, then one of three annual plans. Never "free forever", "₹0 to start", "free tier", "flat 10%", "one-time fee" or "daily payouts".
- **Commit/push only when the user explicitly asks** — stage, verify, then stop and wait.
- Keep the free vs paid vs unverified feature boundary (§4) exact.
- New keyword/blog work must be **distinct from existing content** — verify before writing.
