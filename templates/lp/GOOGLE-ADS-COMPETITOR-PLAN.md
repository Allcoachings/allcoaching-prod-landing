# Google Ads: competitor-alternative Search plan (educators)

Prepared 27 Nov 2026 for account AW-11343265505 ("Allcoaching Ads"). Nothing here is live. The account is set up for it (tracking, negatives, assets), the campaign is built by the owner.

## What is already set up in the account
| Area | State |
|---|---|
| Primary conversion | **Purchase - Thank You Page** only (label VHMx…). Account default goal. |
| Secondary conversions | Lead - Join Thank You (0sOM…), Studio created (zIGk…), Start trial (HJDz…), Learning App Play purchase (student app, never for educator bidding) |
| Enhanced conversions | All four web tags send `user_data` (email, +91 phone, name) from `{{UPD - EC user data}}` in GTM. **Publish the GTM workspace first.** |
| Shared negative lists | "Educator only - student, job, free" (47) · "AllCoaching brand (for non-brand campaigns)" (7). Attach both to every competitor campaign. |
| Account-level assets | 6 sitelinks (pricing, trial, compare, JEE/NEET, skills, WordPress), 10 callouts, structured snippet "Types". They show on every new campaign. |
| Auto-apply recommendations | All off. Leave them off. |

## Campaign settings (per the account rules in `references/05-ads-and-performance.md`)
- Type **Search**. Networks: Google Search only. **Search partners off, Display off.**
- Locations: India, **Presence: people in or regularly in** (not "interest").
- Languages: English, Hindi.
- Bidding, weeks 1–2: Maximize clicks with a max CPC cap (start at ₹25–₹40; raise only if impression share is tiny). After 15–30 conversions: Maximize conversions. Target CPA only once Purchase volume is steady.
- Conversion goal: account default (Purchase). If Purchase volume is too low to learn from, the campaign-level goal can temporarily use "Submit lead forms" — owner decision.
- Ad rotation: optimise. Auto-apply: off. AI Max / broad match expansion: off.
- Final URL: the matching `/vs/` page. Sign-up happens on studio.allcoaching.in; same GTM container, so conversions are tracked there too.
- Never use a competitor's trademark in ad text (headlines, descriptions, paths). Bidding on their names as keywords is allowed.

## Ad groups and keywords (phrase "…" and exact […] only, no broad)
| Ad group | Keywords | Final URL |
|---|---|---|
| Classplus | [classplus alternative] · "classplus alternative" · "app like classplus" · "apps like classplus" · "classplus competitor" · "classplus vs" · "classplus pricing" · "classplus price" · "classplus charges" · "classplus plans" | https://allcoaching.in/vs/classplus |
| Graphy | [graphy alternative] · "graphy alternative" · "graphy pricing" · "graphy vs" · "sites like graphy" · "spayee alternative" | https://allcoaching.in/vs/graphy |
| Teachmint | [teachmint alternative] · "teachmint alternative" · "teachmint pricing" · "teachmint vs" | https://allcoaching.in/vs/teachmint |
| AppX | [appx alternative] · "appx alternative" · "appx coaching app price" · "appx vs" | https://allcoaching.in/vs/appx |
| Other LMS | "learnyst alternative" · "edmingle alternative" · "exly alternative" · "tagmango alternative" · "teachable alternative india" · "thinkific alternative india" · "kajabi alternative india" | https://allcoaching.in/vs/ |

Keep each competitor in its own ad group so the ad and the page match the search (the relevance point in the video, hack 5). Check the search terms report every 2–3 days: move converting terms to exact, add non-converting ones to the "Educator only" list.

## RSA copy (no trademarks, no exclamation marks, prices exactly as `02-pricing.md`)
Headlines (≤30):
1. 7-Day Free Trial, No Card — **pin to position 1**
2. Looking for an Alternative?
3. Your Own Coaching App + LMS
4. Yearly from ₹6,999 + GST
5. Or 0% Commission Monthly
6. Own Domain and Android App
7. Compare Prices Side by Side
8. Set It Up Yourself
9. No Setup Fee
10. 500+ Educators on AllCoaching
11. Tests With All-India Rank
12. Bulk Import Your Students
13. Your Brand on Every Screen
14. Switch Without a Sales Call
15. Live Classes, Courses, Tests

Descriptions (≤90):
1. Your own academy: website, Android app, courses, tests and live classes under your name.
2. Yearly from ₹6,999 + GST + fee per sale, or monthly from ₹3,999 + GST at 0% commission.
3. 7-day free trial, no card. Upload a course, connect your domain and start selling.
4. See their public prices next to ours, with the fee per sale shown. Then decide.

Display path: `allcoaching.in/compare/pricing`.

## Before launch (checklist)
- [ ] GTM workspace published (enhanced conversions + Studio created + Start trial tags).
- [ ] `assets/checkout.js` ex-GST change committed and deployed (purchase value without GST, `tax` separate).
- [ ] Studio (separate repo) also sends purchase `value` without GST plus `tax` — developer.
- [ ] Re-check competitor prices on the `/vs/` pages if older than ~30 days (`references/10-competitors.md`).
- [ ] Both shared negative lists attached to the campaign.
- [ ] Consent mode decision (P5 in `references/08-tracking.md`) — affects how many conversions Google can see.
