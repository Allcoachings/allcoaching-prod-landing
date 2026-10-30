# 08 · Tracking and measurement

Full developer brief: `templates/lp/TRACKING-FIX-FOR-DEVELOPER.md` (checked 2026-10-28). Also `templates/lp/META-ADS-READINESS.md`, `templates/lp/GTM-CHANGES.md`, `templates/lp/README.md`.

**Golden rule: never send test events to production Meta or Google.** Verify with GTM Preview, Meta Test Events (test code) and Google Tag Assistant only.

## IDs
| What | ID | Where |
|---|---|---|
| GTM (marketing + studio) | **GTM-T3KFKD3G** (published v48) | allcoaching.in, studio.allcoaching.in |
| GTM (student/learn + educator sites) | GTM-K3C28Z7T (v4) | learn.allcoaching.in, educators' domains |
| GA4 | G-8V1GJFC7WS (marketing + studio) · G-0KCYQJSSJ3 (learn) | via GTM |
| Meta dataset (educator funnel) | **391186199904157** "AllCoaching Pixel" | via GTM-T3KFKD3G only |
| Meta pixel (students/learn) | 776849551172060 | learn app |
| Google Ads | **AW-11343265505** · Lead `0sOMCPfuvMkcEOH98aAq` · Purchase `VHMxCJzRlskcEOH98aAq` | via GTM |
| Also in container | Microsoft Clarity, X pixel `rgpox` | |
GTM loads on first interaction or after 3.5 s (`delay_gtm.py`). Each educator can add their own GTM and Meta Pixel in studio ▸ Own branding ▸ Marketing tools.

## Event contract (educator funnel)
| # | dataLayer event | When | event_id | Key params | Fires |
|---|---|---|---|---|---|
| 1 | `begin_checkout` | Plan/checkout screen opens | `ic_<uuid>` | value ex-GST, currency INR, `content_ids:[plan]`, `content_name` | Meta InitiateCheckout, GA4 begin_checkout |
| 2 | `lead_complete` | New mobile number OTP-verified | user id (= `lead_id`) | `user_email`, `user_phone` | Meta Lead, GA4 generate_lead, Ads Lead |
| 3 | `sign_up` | Name + academy saved | `reg_<educator id>` | `method:'phone_otp'`, `content_name:'Studio created'`, value 0 | Meta CompleteRegistration, GA4 sign_up |
| 4 | `add_payment_info` | Razorpay window opens | `api_<razorpay order id>` | value, currency, plan, `tax` | Meta AddPaymentInfo, GA4 |
| 5 | `start_trial` | Trial starts | `trial_<educator id>` | `plan` (real), value 0, `predicted_ltv` (3999/5999/7999 monthly; 6999/12999/24999 yearly) | Meta StartTrial, GA4 |
| 6 | `purchase_complete` | Server-verified payment | Razorpay payment id (= `transaction_id`) | value ex-GST, `tax`, plan, `external_id`, `user_email`, `user_phone` | Gate → Meta Purchase, GA4 purchase, Ads Purchase |
| 7 | `user_identified` | After login | — | `external_id`, `em`, `ph` (91XXXXXXXXXX), `fn`, `ln`, `country:'in'` | Meta advanced matching |
Other events: `lp_checkout` (step = open, otp_sent, otp_verified, details_saved, coupon_applied, payment_open, payment_dismissed, done, error) from `assets/checkout.js`; `studio_signup_complete`; `cta_signup_click`, `contact_click`, `view_pricing` (`assets/track.js`); `ac_attribution` (`assets/attribution.js`); `whatsapp_click`; landing `ob_view`, `ob_cta_click`, `ob_scroll`, `ob_teach`. Cookies: `ac_attribution`, `ac_first_touch` (90 d, `.allcoaching.in`), `ac_attr`, `ac_ck_v1`, `ac_ref`, `ac_consent`.

Values: send ex-GST `value` and a separate `tax`. Dedup Meta browser/CAPI on `event_id`.

## Open fixes (owner/developer; status 2026-10-30)
- **P1 (critical):** learn app initialises the educator dataset 391186199904157 → student purchases counted as educator Purchases (8 of 16 in 28 days). Fix in learn app (init only 776849551172060 / `trackSingle`), then set the dataset's traffic allow-list to allcoaching.in + studio.allcoaching.in.
- P2–P4 (studio ids, real plan, begin_checkout/add_payment_info) and the "14 days" copy appear fixed in the 29 Oct studio build — **verify live**.
- **P5:** consent mode on studio defaults to denied (loses Ads conversions); allcoaching.in has none. Owner decision: Option A grant by default in India, deny in EEA/UK (recommended), or Option B deny until accept on both domains + Meta consent.
- **P6:** Google Ads enhanced conversions off; Lead needs an order id; add secondary actions "Studio created", "Start trial".
- **P7:** ex-GST value + `tax` everywhere.
- **P8:** GA4 scroll at 50/90 only; limit the click tag.
- Backend: Django CAPI not reaching Meta (`META_CAPI_TOKEN`); a future CAPI must not send student sales as Purchase to the educator dataset.

## 28-day snapshot (to 2026-10-28, for context only)
PageView 17,164 · InitiateCheckout 532 · ViewContent 121 · CTAClick 35 · CompleteRegistration 24 · Lead 24 · StartTrial 20 · Purchase 16 (half were student sales, P1) · AddPaymentInfo 6. EMQ: Lead 8.3, CompleteRegistration 8.3, Purchase 7.8.

## Checklist for any new page, landing page or funnel step
1. GTM-T3KFKD3G present (via the delayed loader) and no hard-coded pixels.
2. CTAs carry `data-checkout` / tracked attributes; events match the contract names exactly.
3. UTMs preserved into checkout (`ac_attribution`).
4. Test in GTM Preview + Meta Test Events with a test code; nothing to production.
5. Document new events in the developer brief.
