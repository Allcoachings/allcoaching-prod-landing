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
AllCoaching (**allcoaching.in**) is an **educator-first EdTech marketplace** for India's independent educators — coaching-institute owners, tutors, and subject experts. It gives each educator a **branded white-label studio (web + app)** to run their whole teaching business, *plus* a **shared marketplace** so students can discover them. Legal entity: **AllCoaching Technology** (not "Pvt. Ltd."). Founded **2018** in Prayagraj. Category: **EdTech Marketplace**.

- **Tagline:** *Democratizing Education.*
- **Positioning (ideology):** *The Operating System of Education.*
- **Positioning (confirmed 2026-10-09, lead with this):** AllCoaching is an **LMS** — **"Build your own LMS. In just a few clicks."** Drag and drop your academy (courses, tests, notes, live classes, payments), **make it your brand** (logo, colours, own domain, own Google Play app), and start selling. Always pair with the **14-day free trial, no card needed**. Marketplace discovery is a supporting feature.
- **Positioning (2026-10-08, superseded by the line above):** **"Sell your courses online. Your way."** Two ways to sell, one account: (1) list courses on the AllCoaching marketplace, where students on Android, iOS and web discover and buy them; (2) launch a full white-label academy yourself — connect your own domain for your website, publish your own app on Google Play, and use the built-in marketing tools to sell under your own brand. Plug and play, no developer. Homepage shows NO founding year or city ("no legacy, no place") — keep "2018"/"Prayagraj" off marketing pages (legal/contact/about pages may keep the registered address).
- **Earlier product line (still valid as support copy):** **"Launch your online academy yourself."** Website on the educator's own domain, the AllCoaching app on Android, iOS and web, live classes, payments and marketplace discovery — all from one login. No WordPress, no separate LMS, no developer, no sales call, no demo dependency.
- **Founder / voice of the brand:** **Amit Ratan, Founder & CEO** (author of the manifesto and blog byline).
- **Studio product** (the educator app) lives at **studio.allcoaching.in** — a **separate repo/codebase** (no access from the marketing repo). Marketing site links `Log in` → studio.allcoaching.in/login, `Start free trial` → studio.allcoaching.in.

## 2. The ideology (the manifesto thesis — *why it exists*; rewritten 2026-10-15)
**One-line thesis:** *Every educator deserves their own academy, built by themselves.* Own brand (domain, logo, Google Play app) + built self-serve in a few clicks + still found by new students through the shared marketplace. Ownership and reach, without choosing.

The founding argument, in order (manifesto chapters at /manifesto):
1. **The Right Dream, Sold the Wrong Way** — "own your academy" was never the mistake. What failed was how it was sold: sales calls, demos, setup fees, agencies building it for you, every change a ticket — and then left alone after launch with no students arriving.
2. **The Educator's Trap** — a good teacher is forced to become developer, marketer and payments desk; every rupee on ads / hour on reels is one not spent on teaching. Pains: someone else holds the keys · performing replaces teaching · marketing eats quality · tech burden · hidden costs · alone after launch.
3. **The Student's Side** — two things decide an enrolment: *can the student find the teacher*, and *does what they find look like a real academy they trust*. Fix = a professional academy under the educator's name **and** a way to be found.
4. **Big EdTech is not the educator's friend** — absorption, not partnership: your brand disappears, content becomes their asset, opaque splits, growth capped by their algorithm.
5. **The False Choice** — Indian EdTech made educators pick ownership (agency-built app, alone) **or** reach (big platform, brandless). The choice was never real. Analogy: a shop with its own signboard that also sits in a busy market.
6. **The Operating System of Education** — "you build your academy, we run everything beneath it." Two paths, one account: (a) **your own white-label academy** — website on your domain, own Google Play app, your logo/colours, built and changed by you, data exportable; (b) **the marketplace** — courses also listed on the AllCoaching app (Android, iOS, web) for discovery. The marketplace supports the academy; it does not replace it.
7. **What it does differently:** Build (drag-and-drop LMS, no code) · Brand (domain, logo, own Play app) · Self-serve (14-day trial, no card, no sales call/demo) · Sell (UPI/card, T+3, keep 90–95%) · Discovery (marketplace) · Ownership (export everything) · Economics (one published yearly plan, fee 10%→5%) · Freedom (time back to teach).

**Core beliefs (verbatim manifesto tenets, ch. 8):** (1) teaching is a *vocation, not a startup*; (2) every educator should **own** their academy; (3) an educator should be able to **build it themselves** — no sales call, demo, agency or waiting; (4) **ownership and reach should not be a trade-off**; (5) a student should find the *best* teacher, not the *most advertised* one; (6) prices should be **published before anyone signs up**; (7) honest about what it takes — a fair foundation, not a magic solution.

**Retired framing (don't reuse):** "personal apps fail / are a burden", "3.5 lakh educators *with personal apps*", "the mall that brings kirana stores together", "List your courses on AllCoaching" as the primary CTA, "Founded 2022". AllCoaching now *sells* the own-brand app and website, so never argue against educators owning one — argue against owning one you can't control or that leaves you alone.

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
- **Competitive stance:** the alternative to *both* (a) agency/sales-led app builders (you get a brand but not the controls, and no discovery) *and* (b) Big-EdTech platforms that rent your audience / take large cuts (Classplus, Graphy, Teachmint, Unacademy, Byju's, Udemy, etc.). AllCoaching = own-brand studio **+** shared marketplace network effect, transparent economics (one yearly plan, platform fee 10% → 5%, keep 90–95%).

## 6. Brand & voice (apply to any AllCoaching surface)
Full system is the `brand-system` memory + repo `brand.css`; the essentials:
- **3 fonts, each one job — Fraunces is NOT a brand font.** Display = **Instrument Serif** *italic, weight 400 only* (headlines, KPI values, wordmark; emphasis via **colour**, never bold). UI = **Inter Tight** (body/buttons/nav; default emphasis 600). Mono = **JetBrains Mono** (numbers, eyebrows, IDs, code).
- **Colour (2026-10-12, current):** white / soft-mist canvas (`#FFFFFF`, `#F6F8FC`), **electric blue `#2B44FF` is the only brand accent** (hover `#1A2FD9`, tint `#E8F0FF`), cyan `#22C3F5` only inside light-ray graphics, navy `#0A0F3D` for final CTA bands and footers. Ochre and cream are retired. Full guideline: allcoaching.in/brand.
- **Voice:** calm, confident, editorial (not corporate); educator-first; restraint over decoration. Say **educator / studio / your students** (not creator / dashboard / audience). **Banned:** exclamation marks, "maximize", "onboard" (verb), "unlock", "creator", "#1 platform" ranking claims, stock photos. Confidence from accuracy, not hype.
- **Logo:** rounded-square gradient pin + wordmark in Instrument Serif italic 400 (always italic). Tagline "Democratizing Education" in mono, cyan on dark / blue on light.
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
