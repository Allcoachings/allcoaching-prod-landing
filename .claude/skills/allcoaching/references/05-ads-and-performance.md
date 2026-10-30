# 05 · Ads and performance marketing (Meta, Google, YouTube)

Goal of paid media: **educators start a 7-day free trial or buy a plan** at a cost that pays back. Every ad must pass the claims register (`04-voice-and-claims.md`) — ad platforms and educators both punish over-promising.

## Funnel
Ad → `/landing/<page>` (on-page checkout: mobile OTP → name + academy → yearly plan via Razorpay **or** 7-day trial) → studio (monthly plans via autopay in studio) → activation (theme, first course, domain, app) → paid.

**Landing pages** (all CTAs open the on-page checkout; no competitor names; no demo links):
| Page | Angle | Use for |
|---|---|---|
| `/landing/launch` | "Your own coaching academy. Live today." | Broad educator audiences |
| `/landing/jee-neet` | "Your own JEE / NEET academy. Your name on it." | Entrance-exam educators |
| `/landing/skills` | "Turn your skill into a course, sold under your name." | Skill coaches (yoga, English, marketing, music, coding) |
| `/landing/wordpress-vs-allcoaching` | "Your whole academy. One modern LMS." | WordPress / tool-stack switchers |
| `/landing/growth-upsc` | UPSC / State PSC + premium Rajya Seva theme (₹10,000 value), personal invite `?name=` | Invite-only offers |
| `/start`, `/pricing` | Full story / price comparison | Retargeting, Google Search |
Coupon / plan deep links: `?plan=starter|growth|pro`, `?checkout=1`, `?code=COUPON`, `?ref=`. Bump `?v=` on CSS/JS after edits (1-year cache).

## Measurement setup (details in `08-tracking.md`)
- Meta dataset **391186199904157** via GTM-T3KFKD3G. Optimise for **Lead** (OTP-verified number) first; switch to **Purchase** once there are ~50 purchases a week. StartTrial and CompleteRegistration are secondary signals.
- Google Ads **AW-11343265505**: Purchase is the only primary conversion; Lead, "Studio created", "Start trial" secondary. Turn on enhanced conversions.
- Attribution: Meta 7-day click / 1-day view.
- UTMs (Meta): `utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`. Google: auto-tagging (gclid) + `utm_source=google&utm_medium=cpc&utm_campaign=<name>`. YouTube: `utm_source=youtube&utm_medium=paid`.
- **Never fire test events into production.** Verify with Meta Test Events / GTM Preview / Tag Assistant.
- Known data issue until the developer fixes P1: learn-app student purchases leak into the educator dataset — read Purchase counts with care.

## Audiences (Meta)
- **Interest/behaviour seeds:** teachers, tutors, coaching institutes, online teaching, educational content creators, YouTube education, competitive-exam interests (NEET, JEE, UPSC, SSC, banking), skill interests (yoga teaching, spoken English, digital marketing). Use broad + Advantage+ audience once Lead volume exists.
- **Custom:** site visitors 30/90 d (`/pricing`, `/start`, landing pages), checkout openers who didn't verify (InitiateCheckout − Lead), trial starters who didn't pay, video viewers 50%+.
- **Lookalikes** (later): paid educators, trial starters.
- Geography: India; languages English + Hindi. Age 22–55.
- Exclude: existing paid educators; students (don't target exam aspirants with educator ads).

## Angles that fit the model (pick one per ad)
1. **Own brand / full control** — "Students see your name. Not ours." Your domain, your app, your students.
2. **0% commission monthly** — "Every rupee of every sale is yours. 0% commission on every monthly plan, from ₹3,999."
3. **One login vs tool chaos** — WhatsApp + Drive + Zoom + Excel → one studio.
4. **Own app without the agency** — own Android app on every plan; compare to agency quotes / ₹14,999+ elsewhere (sourced).
5. **Set it up yourself** — sign up → plan → upload → domain → sell; no sales call, no developer.
6. **Exam vertical** — "Your own NEET / JEE / UPSC academy" with test series, rank and percentile.
7. **Skill vertical** — "Turn your skill into a course sold under your name."
8. **Switcher** — from WordPress / Classplus-style apps (on blog/vs pages, not on ads that name rivals unless sourced and fair).
Each ad: hook (pain) → proof (product moment) → offer (7-day free trial, no card; price line) → CTA.

## Copy bank (ready to use; English + Hinglish)
- **Primary text (EN):** "Your own academy — website, Android app, courses, tests and live classes — under your name. 0% commission on every monthly plan, from ₹3,999 + GST. Start with a 7-day free trial, no card needed."
- **Primary text (Hinglish):** "Apni website, apna Android app, courses, tests aur live classes — sab ek login me, aapke naam se. Monthly plans par 0% commission, ₹3,999 se (+GST). 7 din free trial, card nahi chahiye."
- **Pain hook (Hinglish):** "Class links WhatsApp par, notes Drive par, fees alag links se? 5 jagah ka kaam, ek login me."
- **Headlines (≤40 chars):** "Apna LMS. Apna brand." · "Your academy. Your name." · "0% commission. Your own app." · "Build your LMS in a few clicks" · "Your own NEET academy, live today"
- **Descriptions:** "7-day free trial · no card needed" · "Own domain + Android app on every plan" · "Set it up yourself. No developer."
- **CTA buttons:** Sign Up / Learn More (Meta) → landing page; on creative: "Start free trial" / "Apni academy banaiye".
- **Price line (must be exact):** "0% commission on monthly plans from ₹3,999/month + GST · or yearly from ₹6,999 + fee per sale."

## Google Ads
- **Search themes:** create coaching app / own coaching app; LMS for coaching institute India; sell courses online India; online academy platform; course selling website; coaching app with own brand; Hindi: "coaching app kaise banaye", "apna app kaise banaye". Brand: AllCoaching / All Coaching.
- **Negatives:** free, free download, job, vacancy, salary, student login, apk, mod, course for students (exam prep searches), "learn" intent terms (e.g. "NEET coaching near me").
- **RSA rules:** headlines ≤30 chars, descriptions ≤90; pin one headline with the offer ("7-Day Free Trial, No Card"); include price only exactly as `02-pricing.md`.
- **Competitor keywords:** allowed with care (bid on terms, never use rivals' trademarks in ad text). Send to the relevant `/vs/` page only if it's sourced and current.
- **YouTube:** product walkthrough (real studio), founder explainer, educator showcase (approved academies only, no numbers). 15–30 s cut-downs, captions burned in, first 3 seconds = pain or product moment.

## Creative specs
Feed 1080×1080 and 1080×1350 · Stories/Reels 1080×1920 (safe zones 250px top/bottom) · Google display 1200×628 / 1200×1200 · YouTube 16:9 1920×1080 and 9:16. Style per `03-brand-and-design.md` §Ads. Text on image short; logo + "The academy platform for educators" lockup; studio screenshot with "Studio preview · sample data" when data is sample. Existing set: `assets/ads/2026-10/`.

## Budget and testing (owner sets amounts; these are working rules)
- Start with 2–3 angles × 2 creatives each, one campaign per objective, enough daily budget for ~50 optimisation events a week per ad set (consolidate if you can't reach it).
- Judge creatives on cost per Lead and Lead→trial/paid rate, not CTR alone. Kill after ~2–3× target CPL with no conversions; scale winners 20–30% every few days.
- Refresh creative every 2–4 weeks or when frequency > 3 on prospecting.
- Report weekly: spend, Leads, CPL, trials, purchases, CPA, revenue (ex-GST), ROAS, by angle.

## Compliance and policy
- Meta personal-attributes rule: don't write "Are you a teacher who…" style lines that assert attributes; use "For educators who…".
- No before/after income claims, no guaranteed results, no fake urgency/countdowns, no fake scarcity ("only 200 slots").
- Price and trial must match the landing page exactly; GST note visible.
- Draft ads made before 2026-10-29 may still show 14 days or old pricing — fix before publishing.
