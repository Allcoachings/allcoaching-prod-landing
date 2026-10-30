# 01 · Product and studio

What AllCoaching actually is, screen by screen. Use it for feature copy, product explanations, onboarding design, support answers and screenshots. Feature claims must match the claims register in `SKILL.md` §3.

## The three products
| Product | URL | Who uses it | Notes |
|---|---|---|---|
| **Studio** | studio.allcoaching.in | Educator and their team | Where the academy is built and run. Separate codebase (React/Vite); developer **Sumit**. Login `studio.allcoaching.in/login`. |
| **Academy website + student web app** | `<handle>.allcoaching.in` free, or the educator's own domain (e.g. biolessons.in, chempsi.com, digitekm.com); served by learn.allcoaching.in | Students | Branded with the educator's logo, colours, theme. Course pages, checkout, student login, video player, tests, live. |
| **Educator's own apps** | Google Play / App Store under the educator's own developer account | Students | Own white-label Android app on every plan; iOS on Pro monthly and every yearly plan. |
| **AllCoaching marketplace app** | Android `org.student.allcoaching` · iOS id6758305866 · learn.allcoaching.in | Students discovering educators | Educators' courses are listed as an extra discovery channel. Never promise students or sales from it. |

## Studio map (live bundle, Oct 2026)
**Main:** Dashboard `/` · Transactions `/transactions` (owner only) · Content → Videos `/videos`, PDFs `/pdfs`, Test series `/tests` · Courses `/course` · Free content `/free-content` · Live `/live` (new class, built-in live studio, publish; `/live/plans` = live-classroom hours) · Community `/post` · Discount `/discount` · Analytics `/analytics`.
**Workspace:** Own branding `/branding/overview` (owner only) → Themes `/website`, Pages, Blog `/branding/blog`, Domain `/branding/domain`, App `/branding/app`, Marketing tools `/branding/marketing` (educator's own GTM ID and Meta Pixel), Preferences `/branding/preferences` (brand name, logo, favicon, slogan, colours, SEO title/description/image, access lock, cookie notice, crawl settings for Google/Bing/AI, spam protection) · Integrations `/integrations` (Razorpay OAuth, YouTube OAuth, Zoom, Google Play Console, App Store Connect) · Notifications `/notification` · Referrals `/referral` · Settings `/settings` (profile, plan and autopay, billing, team, payments, notifications, account).

> Some studio modules (Community, Discount, Referrals) exist in the navigation, but the **studio v5 design mock-up** shows sample numbers (referral 2%/1.5%/1%, discount stats, verification badge). Don't publish those numbers or present the mock-up's data as real. Caption mock-up / sample screenshots **"Studio preview · sample data"**.

## Onboarding (real studio, 29 Oct 2026 build)
1. **Verify** — "Continue with Google" or "Continue with mobile" (6-digit OTP; password fallback).
2. **Name** — your name + academy name → shows "Your free address: `<handle>`.allcoaching.in".
3. **Plan** — "Choose your plan." Monthly / Yearly toggle ("Billed monthly · stop any month" / "Billed yearly"), badges Growth "Most popular", Pro "Best value · Recommended", "Commission per sale", "Compare all features", "Try free for 7 days — no card needed".
4. **Checkout** — order summary, GST (18%), coupon code, Razorpay (UPI: Google Pay, PhonePe, Paytm; card; netbanking), "GST invoice to your email". Monthly: "Autopay then charges ₹X each month — stop any month."
5. **Setup** — "Creating your studio" → "Applying your brand to the website" → "Getting your Android app ready" → "Open my studio".
Design principle the owner asked for: simple and smooth, no skippable filler steps, focus on the pay / trial button, land the educator in **Own branding** after checkout. A prototype for Sumit exists (Claude-login + Shopify-signup style).

## Plan management (Settings ▸ Plan)
- Monthly autopay mandate is held by Razorpay; "Stop autopay" → plan runs to the end of the paid month.
- To switch monthly → yearly: stop autopay first, then pick a yearly plan.
- Upgrades any time (unexpired paid value credited); downgrades through support at renewal.
- Stopping: offline at end of paid period → 30 days to export or come back → uploaded videos deleted.

## Feature truths by area
**Content and courses** — Videos (upload to AllCoaching storage within plan limits, or unlimited YouTube in a branded player), PDFs/notes, test series, courses that bundle them, free content for lead generation. Course page with SEO meta, schema and checkout is created automatically when a course is saved; the educator can edit title, description, URL.
**Tests** — Exam-pattern test series, auto-grading, negative marking, all-India rank and percentile, leaderboards, topic-wise analytics, full-screen anti-cheat lock, randomised question order. **No AI question generation** — educators may draft with ChatGPT/Gemini/Claude, review every question, then upload.
**Live** — Unlimited live classes on YouTube Live or Zoom on every plan. The **built-in live classroom** has monthly hours by plan (monthly 20/50/90 h, yearly 5/10/15 h). Built-in room features seen in the studio: recordings, attendance, captions (Hindi, Punjabi, English), each student's name watermarked on video. Separate live-classroom add-on plans exist on `/live/plans`; an old screen showed "Free ₹0 forever / ₹999 / ₹2,899 / ₹5,999" — **don't publish those**, they're pending an owner decision.
**Certificates** — branded completion certificates (logo, name), completion criteria, auto-issued, unique certificate ID, student can download and share. A completion proof, not an accredited degree.
**Students** — unlimited students, student list/CRM, bulk import from Excel / Google Sheet, enrol links, notifications.
**Payments** — UPI/card/netbanking via Razorpay; automatic payouts to the educator's bank (don't advertise payout speed); coupons; GST invoice for the plan fee. Gateway charges on student payments are separate.
**Brand and website** — themes (premium themes free for the first 2 months; then per plan), drag-and-drop page builder (up to 100 pages), ready-made landing pages (6 / 12 / 16), blog (up to 300 posts), own domain (bought from any registrar, ~₹600–1,200/yr; connecting is free), lead forms.
**Apps** — studio builds the educator's own branded Android app (and iOS per plan). Published on the educator's own Play Console / App Store account — by the educator, or by AllCoaching with API access. Google/Apple review it; never promise approval or timelines. New personal Play accounts must run a closed test (12 testers, 14 days) — a Google rule.
**Team** — seats 3 / 5 / 7 (owner + team), separate logins; institutes handle their own teacher pay (no auto-split claim).
**Marketing tools** — own Meta Pixel and GTM per academy, SEO settings, AI/Google/Bing crawl controls, coupons, lead forms, WhatsApp plugin.
**Protection** — DRM and watermarking are part of every plan. Don't name specific DRM standards or forensic watermarking.

## API reference (for developer briefs only — never in public copy)
Base `https://allcoaching-admin.b-cdn.net/v1/educator/`. Onboarding: `login/`, `login/verify`, `login/google`, `login/onboarding/pricing` (public; the source of truth for plan data), `login/onboarding/claim`, `.../trial`, `.../coupon/check`, `.../pay/checkout`, `.../pay/verify`. Plan: `institute/plan/checkout|verify|subscribe` (autopay). Branding: `themes/preferences/`, `institute/tracking/`. The marketing site calls the API through `/acapi/proxy.php?p=`.

## Open product items (as of 2026-10-30)
- Confirm the studio no longer says "14 days" anywhere (fixed in the 29 Oct build; verify live).
- Owner decision on the old live-classroom add-on plans shown in the studio.
- Real Settings tab names and Analytics detail not documented; check the live studio before writing about them.
