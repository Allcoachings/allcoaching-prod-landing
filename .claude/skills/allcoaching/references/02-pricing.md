# 02 · Pricing (money claims — get every digit right)

**Source of truth:** the studio plan screen (studio.allcoaching.in, public API `login/onboarding/pricing`). Owner, 2026-10-29: "studio wala pricing final hai". If the API ever differs from this file, the API wins: tell the owner, then update this file, `SKILL.md` §2, `CLAUDE.md` and run the site sweep.

## Plans
Two ways to pay, same three plans. 7-day free trial on every plan, **no card needed to start**. No setup fee. **No sales limit on any plan.** Prices exclude 18% GST.

### Monthly — 0% commission (keep 100% of every sale); autopay; stop any month
| | Starter | Growth (Most popular) | Pro (Best value · Recommended) |
|---|---|---|---|
| Price | ₹3,999 a month | ₹5,999 a month | ₹7,999 a month |
| Year equivalent | ₹47,988 | ₹71,988 | ₹95,988 |
| Commission | 0% | 0% | 0% |
| Video storage / streaming a month | 512 GB / 512 GB | 1 TB / 1 TB | 2 TB / 2 TB |
| Video quality | 1080p | 1080p | 4K |
| Built-in live classroom | 20 h/month | 50 h/month | 90 h/month |
| Team seats | 3 (you + 2) | 5 (you + 4) | 7 (you + 6) |
| Ready-made landing pages | any 6 | any 12 | all 16 |
| Premium themes | any 2 | any 5 | all |
| Own Android app | yes | yes | yes |
| Own iOS app | no | no | **yes** |

### Yearly — lower fixed fee, small fee per sale
| | Starter | Growth (Most popular) | Pro (Best value · Recommended) |
|---|---|---|---|
| Price | ₹6,999 a year | ₹12,999 a year | ₹24,999 a year |
| Fee per sale | 10% (keep 90%) | 7.5% (keep 92.5%) | 5% (keep 95%) |
| Video storage / streaming a month | 512 GB / 512 GB | 1 TB / 1 TB | 3 TB / 3 TB |
| Video quality | 1080p | 1080p | 4K |
| Built-in live classroom | 5 h/month | 10 h/month | 15 h/month |
| Team seats | 3 | 5 | 7 |
| Ready-made landing pages | any 6 | any 12 | all 16 |
| Premium themes | — | — | one included (₹10,000 value) |
| Own Android app | yes | yes | yes |
| Own iOS app | **yes** | **yes** | **yes** |

### Every plan (both billings)
Unlimited YouTube video (branded player) · unlimited live classes on YouTube Live or Zoom (built-in classroom hours above are separate) · unlimited courses, tests and students · watermarking, DRM and piracy protection · marketplace listing (extra channel, no ad spend) · free `.allcoaching.in` address · own domain · drag-and-drop page builder (up to 100 pages) · blog (up to 300 posts) · premium themes free for the first 2 months · plugins: YouTube, Zoom, WhatsApp, Google Analytics, Meta Pixel, Tag Manager, Play Console, App Store Connect · coupons and lead forms · automatic payouts to the educator's bank.

## Copy rules
- "0% commission", "keep 100%", "zero commission" = **monthly only**. Say "0% commission on every monthly plan" or "keep 90–100% of every sale".
- Headline (as on studio): **"0% commission on every monthly plan"**, from ₹3,999 a month. Yearly is the alternative: "lower fixed fee, small fee per sale", from ₹6,999 a year.
- Lead with monthly 0% on /pricing, the homepage and ads; monthly is the default toggle state; `/pricing#yearly` opens yearly.
- Always add "+ GST" or "prices exclude GST" near prices. Payment-gateway charges on student payments are separate (gateway's rate).
- Never "free plan", "free forever", "₹0 to start", "no upfront cost", "one-time", "lifetime", "no subscription" (both billings are subscriptions), "cheap/cheapest/affordable/lowest price".
- Payouts: automatic via Razorpay; never sell payout speed (no "T+0", "instant", "money in 3 days").
- Apps: on the educator's own developer accounts; Google Play $25 once, Apple Developer $99 a year, paid by the educator.
- Domain: bought by the educator (~₹600–1,200 a year at any registrar); connecting is free on every plan.

## Cost maths (illustrative, before GST and gateway charges)
Breakeven line to quote: **below about ₹4 lakh of yearly sales, yearly Starter usually costs least; above that, a monthly plan usually leaves more.** (Starter yearly ₹6,999 + 10% = Starter monthly ₹47,988 at ₹4,09,890 of sales.)

Total yearly platform cost by yearly sales:
| Yearly sales | Starter yearly | Growth yearly | Pro yearly | Starter monthly | Growth monthly | Pro monthly |
|---|---|---|---|---|---|---|
| ₹1 lakh | ₹16,999 | ₹20,499 | ₹29,999 | ₹47,988 | ₹71,988 | ₹95,988 |
| ₹2 lakh | ₹26,999 | ₹27,999 | ₹34,999 | ₹47,988 | ₹71,988 | ₹95,988 |
| ₹4 lakh | ₹46,999 | ₹42,999 | ₹44,999 | ₹47,988 | ₹71,988 | ₹95,988 |
| ₹6 lakh | ₹66,999 | ₹57,999 | ₹54,999 | ₹47,988 | ₹71,988 | ₹95,988 |
| ₹10 lakh | ₹1,06,999 | ₹87,999 | ₹74,999 | ₹47,988 | ₹71,988 | ₹95,988 |
| ₹20 lakh | ₹2,06,999 | ₹1,62,999 | ₹1,24,999 | ₹47,988 | ₹71,988 | ₹95,988 |
Plans differ in storage, live hours, seats and iOS, so recommend by **needs first, then cost**: a solo educator starting out → yearly Starter; growing past ~₹4–5 lakh a year → a monthly plan (0%, keep 100%); needs iOS + 4K + bigger team → Pro (monthly if sales are high, yearly if lower). Always label such tables "illustrative".

## Where each plan is bought
- **Studio** (studio.allcoaching.in): all six plans; monthly via Razorpay autopay mandate.
- **allcoaching.in landing checkout** (`assets/checkout.js`, on `/landing/*` and `/start`): the three **yearly** plans (fees 699900 / 1299900 / 2499900 paise) and the 7-day trial; monthly buttons (`starter_m`, `growth_m`, `pro_m`) link to studio. URL params: `?plan=starter|growth|pro`, `?checkout=1`, `?code=` (coupon), `?ref=`.
- `/plans` 301s to `/pricing`.

## Lifecycle rules
- Trial: 7 days, no card. A trial is not a free tier.
- Monthly: no lock-in; stop any month; runs to the end of the paid month.
- Upgrade any time (unexpired paid value credited); downgrade via support at renewal.
- Monthly → yearly: stop autopay first, then choose yearly.
- Stop / non-renewal: academy offline at end of paid period → **30 days to export content and data or come back** → uploaded videos deleted.

## Competitor framing (pricing pages checked 2026-10-24 — re-check before reuse; cite source + date)
- Own branded Android app at 0%: **Learnyst Premium ₹14,999/month**, **Edmingle Prime ₹17,999/month billed monthly** → AllCoaching **Starter monthly ₹3,999** (own Android app, 0%).
- Own iOS app: **Learnyst Business ₹49,999/month**, **Edmingle Power ₹34,999/month billed monthly** → AllCoaching **Pro monthly ₹7,999** (or any yearly plan).
- Classplus: ₹29,999 for 1 year, ₹39,999 for 2 years (classplusapp.com/new-web, checked 2026-10-17; GST, sales fee, renewal, trial not stated).
- Show the rival's transaction fee next to its fixed price; never round up; never say "cheapest". Full table: `10-competitors.md`.

## Schema (JSON-LD) values
Offers: 3999 / 5999 / 7999 with `unitText: MONTH`; 6999 / 12999 / 24999 with `unitText: ANN`; `priceCurrency: INR`. AggregateOffer: `lowPrice 3999`, `highPrice 24999`, `offerCount 6`.

## Retired pricing (never reuse — history in `12-decision-log.md`)
Free-forever / flat 10% / ₹6,999 one-time (Sep 2026) · Scale ₹99,999/yr 0% (25–27 Oct) · monthly with sales limits ₹50,000 / ₹1.5 lakh (27 Oct) · Growth ₹7,999/mo, Pro ₹14,999/mo, ₹79,990 / ₹1,49,990 yearly, "2 months free", Extend packs ₹499/₹399, ₹7 lakh breakeven, "0% on Growth and Pro" (28 Oct) · 14-day trial (before 27 Oct).
