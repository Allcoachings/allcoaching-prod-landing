# Competitor claims audit (checked 2026-10-24)

Scope: `blog/*alternative*.html`, `blog/appx-vs-classplus.html`, `blog/classplus-vs-graphy-vs-allcoaching.html`, `blogs/en/graphy-alternative-with-organic-marketplace-traffic.html`, `blogs/hinglish/*classplus*.html`. Evidence: `competitors.json` in this folder (official pages only).

Verdicts: **confirmed** (the official page supports it today), **contradicted** (the official page says otherwise), **unsupported** (no official source found or reachable; rewrite, attribute or remove). Claims about AllCoaching itself are out of scope, except where they break CLAUDE.md (noted at the end).

## Classplus

| Post | Claim | Verdict |
|---|---|---|
| appx-vs-classplus; classplus-alternative-for-coaching-institutes; classplus-vs-graphy-vs-allcoaching; hinglish/classplus-ka-best-alternative-kaunsa-hai; hinglish/teachmint-vs-classplus-konsa-best-hai | Classplus lists ₹29,999 for 1 year and ₹39,999 for 2 years; GST, fee on sales and renewal price not stated; no free plan mentioned | confirmed (classplusapp.com/new-web). The page also shows struck-through ₹34,999 / ₹44,999 |
| appx-vs-classplus | Plans cover Android app, website, admin portal, unlimited recorded courses, live classes, enrolments, storage | confirmed |
| classplus-alternative-for-coaching-institutes | Above about ₹2.3 lakh/yr in sales, Classplus's flat price is lower on paper | confirmed as arithmetic from published prices (Starter ₹6,999 + 10% vs ₹29,999), as long as the "before any fees it may charge" caveat stays |
| hinglish/classplus-ka-best-alternative-kaunsa-hai | "purane user reviews me live-class credits aur paid add-ons ka zikr hai" | unsupported (third-party reviews, not an official source) |
| hinglish/classplus-ka-best-alternative-kaunsa-hai | "Classplus commonly subscription + usage credits + add-ons bataya jaata hai" | unsupported (the official page lists no usage credits or add-ons) |

## Graphy / Spayee

| Post | Claim | Verdict |
|---|---|---|
| graphy-alternative-for-course-creators-india (many places); classplus-alternative-for-coaching-institutes; classplus-vs-graphy-vs-allcoaching | Graphy: Launch ₹24,999/yr (10%), Grow ₹49,999/yr (7.5%), Rise ₹99,999/yr (5%), or ₹10 per sale if higher | unsupported today. graphy.com/pricing geo-redirects to the US page ($49/$149/$399 a month, 0% fee). The same page's embedded INR data conflicts with these figures (Launch ₹1,999/mo billed annually 10%; Rise ₹9,999/mo billed annually 5%; meta description ₹1,999 / ₹4,200 / ₹8,400 a month). Re-check from an Indian IP before republishing |
| graphy-alternative-for-course-creators-india | "plus a custom Unlimited plan" | unsupported (not on the current page data) |
| graphy-alternative-for-course-creators-india | "₹18,000 to ₹75,000 a year cheaper" at every tier / "same fee rates as Graphy" | unsupported (it depends on the unverified INR prices above; the US page shows 0% fees, so "same fee rates" fails there) |
| graphy-alternative-for-course-creators-india | ₹10 minimum per sale, so about 20% on a ₹49 item | confirmed for the ₹10 minimum (it is in the embedded India block). Treat the exact rates as unsupported |
| graphy-alternative-for-course-creators-india | Graphy "still doesn't bring you a single student" | unsupported as a factual claim (Graphy publishes nothing either way); phrase it as "no built-in student marketplace is described on its pricing page" |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | "Joined Graphy at ₹4,200/month ... in late 2023" | unsupported (₹4,200/month appears only in Graphy's current meta description, not as a dated 2023 price) |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | "entry tier ₹2,800/month" (mid-2024) | unsupported |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | Graphy Year-1 cost "typically ₹4–11 lakh" including custom domain, gateway commission, Play Store build, campaign add-ons | contradicted in part: the US page lists "Free custom domain support" in every plan. The rest is unsupported |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | For ₹15 lakh revenue, Graphy "typically costs ₹4–7 lakh"; Year-2 "₹7-9 lakh" | unsupported |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | Graphy creators "typically run" a 25–65% paid-acquisition take | unsupported |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | "Median migration time from Graphy to AllCoaching is 12–18 days" | unsupported (no source; reads as a fabricated stat) |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | Year-1 trap of ₹4–11 lakh "behind Classplus, Teachmint, and Graphy" | contradicted for Classplus (lists ₹29,999/yr); unsupported for Teachmint and Graphy |
| blogs/en/graphy-alternative-with-organic-marketplace-traffic | Complete the Graphy term "to avoid penalty"; auto-renewal | unsupported (no Graphy term or penalty policy checked) |
| spayee-learnyst-alternative-india | Spayee is a separate, current course LMS on a monthly subscription | contradicted: spayee.com 301-redirects to graphy.com |

## Teachmint

| Post | Claim | Verdict |
|---|---|---|
| teachmint-paid-features-alternative-free; hinglish/teachmint-vs-classplus-konsa-best-hai | Teachmint's pricing page lists no plans; Teachmint focuses on classroom devices for schools | confirmed for what loads from our region (teachmint.com/pricing redirects to the en-us Teachmint X page with no prices). The India page could not be loaded |
| teachmint-paid-features-alternative-free | Educators "pay Teachmint" a subscription for a paid stack (branded app, live classes, tests, payments, CRM, custom domain) | unsupported (no plan or feature list is published) |

## AppX

| Post | Claim | Verdict |
|---|---|---|
| appx-vs-classplus | AppX publishes no prices; demo-led | confirmed (appx.co.in) |

## Learnyst / Edmingle

| Post | Claim | Verdict |
|---|---|---|
| spayee-learnyst-alternative-india | Learnyst "charges a monthly subscription whether or not you sell" | contradicted in part: the Launcher plan is ₹10,000/yr + 10% of sales with "No monthly fee". Subscription plans are ₹8,999 / ₹14,999 / ₹49,999 a month (₹8,099 / ₹13,499 / ₹44,999 a month on annual billing) + taxes |
| spayee-learnyst-alternative-india | A subscription LMS "sometimes with transaction fees on top" (aimed at Learnyst) | contradicted for Learnyst subscription plans (0% transaction fees). The Launcher plan takes 10% instead of a monthly fee |
| spayee-learnyst-alternative-india | Learnyst "brings you no students" / "no marketplace" | unsupported (Learnyst says nothing either way) |
| (CLAUDE.md, not a post) | "Learnyst and Edmingle take 0%" | Learnyst: confirmed for subscription plans, contradicted for Launcher (10%). Edmingle: unsupported (no transaction fee is stated on edmingle.com/in/pricing; plans are ₹7,499 / ₹14,999 / ₹29,999 a month billed annually + taxes) |

## Winuall

| Post | Claim | Verdict |
|---|---|---|
| winuall-alternative-for-coaching-institutes | Winuall-class platforms are a "yearly SaaS subscription" in one place and a "monthly subscription" in another | unsupported. winuall.com now 301-redirects to edify.club (a refurbished-laptop store), so there is no official source. The post also contradicts itself |
| winuall-alternative-for-coaching-institutes | Winuall provides a branded app, live classes, test engine, fee management, student chat | unsupported (cannot be verified today) |

## Exly / Rigi / TagMango

| Post | Claim | Verdict |
|---|---|---|
| exly-rigi-alternative-for-coaches | Exly and Rigi "often charge a subscription or per-transaction fee" | confirmed for Exly (Starter: free upfront + 10% commission; Pro ₹30,000/yr + 6%; Premium ₹1,08,000/yr + 3%). Unsupported for Rigi |
| exly-rigi-alternative-for-coaches | Rigi is a creator-monetisation tool for selling courses and sessions | contradicted: rigi.club is now "Rigi TV - Instant Entertainment", a short-drama app with no creator product shown |
| exly-rigi-alternative-for-coaches | Positions AllCoaching as the option with "no fixed subscription" against Exly | contradicted on the comparison: Exly Starter has no upfront fee, while AllCoaching Starter is ₹6,999/yr |

## Kajabi / Teachable / Thinkific

| Post | Claim | Verdict |
|---|---|---|
| kajabi-alternative-india-for-educators | Kajabi is a USD subscription | confirmed (Basic $179 / Growth $249 / Pro $499 a month, or $143 / $199 / $399 a month billed annually) |
| kajabi-alternative-india-for-educators | Kajabi is a "fixed monthly subscription" / "monthly" cost | confirmed, but incomplete: annual billing is also offered. Kajabi takes 0% revenue share and has a 14-day trial; say so for fairness |
| kajabi-alternative-india-for-educators | Kajabi checkout is "card-first" | unsupported (the page mentions country-specific Kajabi Payments fees, not payment methods) |
| teachable-thinkific-alternative-india | Teachable and Thinkific are sold as monthly subscription tiers in dollars | confirmed (Teachable $39 / $89 / $189 a month, Starter takes a 7.5% fee; Thinkific $109 / $219 / $499 a month; both have annual discounts) |
| teachable-thinkific-alternative-india | "card-first checkout" | unsupported |
| teachable-thinkific-alternative-india | "how is the base free when Teachable charges a subscription for less?" | contradicted: neither base is free. Teachable has a 7-day trial and Starter is $39/mo. AllCoaching Starter is ₹6,999/yr |

## Skool / Circle.so

| Post | Claim | Verdict |
|---|---|---|
| skool-circle-so-alternative-india | Skool and Circle "charge a flat monthly USD subscription ... regardless of revenue" | contradicted for Skool: it also charges a 10% (Hobby) or 2.9% (Pro) transaction fee. For Circle, prices are shown on annual billing; its pricing page states no transaction fee |
| skool-circle-so-alternative-india | "historically in the tens of dollars a month and up" | contradicted / imprecise: Skool Hobby is $9/mo ($7.50 billed yearly) and Pro is $99/mo. Circle is $89 / $199 / $419 a month on annual billing. State the actual figures |
| skool-circle-so-alternative-india | "why would a platform take only 10% when Skool/Circle.so charge a flat fee" | contradicted: Skool Hobby itself takes 10% |

## Udemy / Unacademy / PW / Vedantu / Testbook / Adda247 / Toppr / Extramarks

| Post | Claim | Verdict |
|---|---|---|
| udemy-alternative-for-indian-instructors | Udemy "takes a large cut", "a much larger share, especially on sales it attributes to its own promotion" | unsupported: Udemy's revenue-share page returned 403 and the instructor-terms URL showed "page not found" on 2026-10-24 |
| udemy-alternative-for-indian-instructors | Udemy "controls pricing through platform-wide discounts" | unsupported (no official pricing-policy page retrieved) |
| unacademy-alternative-for-independent-educators | On Unacademy the platform owns the brand, students and pricing | unsupported (no official educator terms found) |
| physics-wallah-alternative-for-educators | A teacher can join PW as faculty but cannot build their own brand on it | unsupported (characterisation; PW publishes no educator terms) |
| physics-wallah-alternative-for-educators | PW "began as one teacher on YouTube" | unsupported by the sources checked here (not on pw.live's homepage) |
| vedantu-alternative-for-online-tuition | Implies joining Vedantu is a franchise-type arrangement ("without joining a franchise", "no franchise fee") | unsupported. Vedantu's become-a-teacher page describes teaching for earnings ("₹25,000+ ... upto ₹75,000+ per month") and mentions no franchise |
| testbook-alternative-for-educators | Testbook sells access "often as a pass or subscription" | confirmed (testbook.com/pass exists) |
| toppr-extramarks-alternative-for-educators | Toppr sold multi-year subscription packages "historically through telecalling sales teams" | unsupported (toppr.com unreachable) |
| toppr-extramarks-alternative-for-educators | Extramarks is a "licensed content shelf" | unsupported characterisation (Extramarks describes school, teacher, student and parent solutions) |

## Cuemath / Aakash

| Post | Claim | Verdict |
|---|---|---|
| cuemath-aakash-franchise-alternative-for-tutors | Cuemath and Aakash franchises carry an "ongoing revenue share, territory restriction, franchisor-owned lead flow" | unsupported. Aakash's only franchise page is a closed 2019 form (₹2,000 application fee). Cuemath publishes no franchise or tutor terms and is now US-focused |

## Internal pricing-rule breaches found while auditing (AllCoaching claims, not competitor claims)

- teachable-thinkific-alternative-india: "pays ₹0 up front" breaks CLAUDE.md (no free tier; Starter is ₹6,999/yr).
- vedantu-, winuall-, kajabi-, spayee-learnyst-, exly-rigi-, skool-circle- posts: "no monthly subscription" / "bills only after you earn" / "pays nothing in a month with no sales" sit awkwardly with the ₹6,999 annual plan. The CLAUDE.md wording is "one predictable annual plan".
- skool-circle-so-alternative-india: "a platform take only 10%" is fine, but "no card required just to sign up" should read "no card needed to start the 7-day trial".

## Tally

- Competitor claim rows from posts: 49 (one row may cover the same claim repeated across several posts)
- Confirmed: 11
- Contradicted (fully or in part): 11
- Unsupported: 27
- Plus 1 CLAUDE.md row (Learnyst/Edmingle "0%"): partly confirmed, partly contradicted, partly unsupported
