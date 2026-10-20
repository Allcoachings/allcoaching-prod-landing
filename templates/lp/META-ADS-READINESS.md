# Meta ads readiness — pixel 391186199904157 (checked 2026-10-20)

## Verified working

| Check | Result |
|---|---|
| One pixel on the site | Only 391186199904157, loaded once through GTM-T3KFKD3G. No hardcoded pixel on any page. |
| PageView | Exactly 1 per page load (pixel's own event counter). |
| InitiateCheckout | Exactly 1 per page view, when the checkout opens, with plan value + eventID. The old click trigger no longer doubles it on /onboarding-* or /landing/*. |
| Lead | 1 per new educator at OTP verify, eventID = user id (same id studio and the server CAPI Lead use). Now fires on every host, not only join.allcoaching.in. EMQ 8.3. |
| CompleteRegistration | 1 per new studio (name + academy saved), eventID `reg_<id>`. EMQ 8.3. |
| AddPaymentInfo | 1 per Razorpay window, eventID `api_<order id>`. |
| StartTrial | 1 per trial, eventID `trial_<id>`, predicted_ltv. |
| Purchase | 1 per verified payment, value + INR + plan, eventID = Razorpay payment id. A repeat push of the same payment is blocked ("Purchase Gate - dedupe"). EMQ 7.8. |
| Server side | "Conversions API with Meta" (Meta-hosted) receives the same events with the same eventID, so Meta merges browser + server. |
| Purchase source | All 39 Purchases in the last 28 days are browser + Meta-hosted. None come from the Go backend, so student course sales are not mixed into the educator Purchase. |
| Domain | allcoaching.in is Verified in Business settings. No traffic allow-list, so no domain is blocked. |
| Advanced matching | Automatic + manual (user_identified → fbq init with external_id, phone, name). |

The sandbox test (all Google/Meta/X requests blocked, so nothing reached the ad accounts) pushed every
funnel event once and confirmed exactly one Meta call per event.

## Fixed today (GTM version 47)

- **GA4 page_view was counted twice** on every page (Google tag + "GA4 Page View" tag, same property).
  "GA4 Page View" is paused.
- **Fake Purchase risk:** "Purchase Gate - dedupe" also fired on studio's old `/thank-you` URL, which would
  send a Purchase with no payment (value 0, no eventID). Those two triggers are removed; it now fires
  only on `purchase_complete`.

## Before you launch

1. **Send ads to the /landing pages.** `/landing/jee-neet`, `/landing/skills`,
   `/landing/wordpress-vs-allcoaching` (live since 2026-10-20). The old `/onboarding-*` pages were
   removed on 2026-10-21 and 301 to these, so old ads keep working.
2. **Optimisation event: start with Lead, not Purchase.** Meta's learning phase needs about 50
   conversions per ad set per week. Purchase has ~16 real payments in 28 days, which keeps ad sets in
   "Learning limited". Lead (new number verified by OTP) comes earlier in the funnel and fires far more
   often. Switch the winning ad sets to Purchase once they reach ~50 purchases a week.
3. **Add UTMs to every ad:** `utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
   fbclid is captured automatically (`_fbc` cookie) and passed to studio.
4. **Attribution setting:** 7-day click, 1-day view (default).
5. **Run one real test** after launch: open the ad URL, do OTP + free trial, and watch Events Manager →
   Test events for Lead, CompleteRegistration, StartTrial (each once).

## For Sumit (backend, not blocking)

- **Server CAPI from Django is not reaching Meta** (no direct "Conversions API" source on any event).
  `META_CAPI_TOKEN` is probably not set in gunicorn and the Celery worker. Meta-hosted CAPI covers
  most of this today; direct server events would also cover visitors who block the pixel.
- **If the Go CAPI is switched on later,** it sends student course sales as `Purchase` to this same pixel.
  That would mix students into the educator Purchase signal. Send them under a different event name
  (or a separate dataset) before turning it on.
- **Diagnostic "duplicate client phone numbers" (PageView, server):** logged-in educators' studio page
  views all carry their phone, so heavy internal use repeats a few numbers. Not harmful for ads; it
  clears as real educator traffic grows.
