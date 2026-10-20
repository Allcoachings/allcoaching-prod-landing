# Campaign landing pages with on-page checkout

Educators land on an allcoaching.in page, sign up and buy a studio plan **without leaving the
page**, and are then sent to studio.allcoaching.in. Every conversion fires on allcoaching.in,
through our own GTM container.

```
ad → allcoaching.in/landing/<page>
     → CTA opens the checkout (/assets/checkout.js): plan on the left, checkout on the right
        1. mobile number + OTP          (POST login/, login/verify)
        2. name + academy name          (PATCH login/update)
        3. plan → Razorpay, or 14-day trial
                                        (claim → pay/checkout → Razorpay → pay/verify, or claim → trial)
     → studio.allcoaching.in (signed in via /handoff once that studio build is live, else /login)
```

## Files

| File | What it is |
|---|---|
| `landing/*.html` | The campaign pages (JEE/NEET, Skills, WordPress). Hand-written, see `landing/README.md`. |
| `landing/lp2.css`, `landing/plans.js`, `landing/page.js` | Shared styles, live plan cards, funnel events. |
| `assets/checkout.js` | The checkout. Shared by every campaign page. |
| `acapi/proxy.php` | Same-origin pass-through to the educator API (the API only allows studio.allcoaching.in in CORS). |

The old `/onboarding-*`, `/onboarding` and `/onboarding2` pages were removed on 2026-10-21.
`.htaccess` sends them with a 301 (query string kept) to `/landing/jee-neet`, `/landing/skills`
or `/pricing`.

## New campaign or offer

1. Copy a page in `landing/`, change the copy and `window.AC_CHECKOUT.page`.
2. For an offer, create an activation code in the admin and put it in `coupon`. It is applied
   automatically and the price is re-checked by the server before payment.

No edit needed for these URL options, on any page:
- `?code=OFFER50` applies an activation code
- `?plan=starter|growth|pro` preselects the plan
- `?checkout=1` opens the checkout straight away
- `?ref=CODE` passes a referral code to the new studio

After **any change to `assets/checkout.js`** or a `landing/` asset, bump its `?v=` on every page
that loads it: `/assets/*` is served with a one-year immutable cache, so browsers keep the old file.

Any other page can use the checkout too: load `/assets/checkout.js` and add `data-checkout`
(and optionally `data-plan="growth"`) to a link.

## Tracking: what reaches Meta, Google Ads and GA4

The checkout pushes **studio's own events with studio's own fields**, so the tags already built
for studio fire here unchanged. What the live container (GTM-T3KFKD3G, checked 2026-10-19) does:

| dataLayer event | Fired when | Meta Pixel | Google Ads | GA4 |
|---|---|---|---|---|
| (page load) | page opens | PageView | remarketing | page_view |
| click on a CTA | checkout opens | InitiateCheckout (paths with `/onboarding`) | | onboarding_cta_click |
| `user_identified` | after OTP, after name | advanced matching (`fbq init` with external_id, ph, fn, ln) | | |
| `purchase_complete` | payment verified by the server | **Purchase**, value + `eventID` = Razorpay payment id | purchase conversion with value and order id | purchase |
| `lead_complete` | new studio opened (paid or trial) | **none yet** (see below) | lead conversion | generate_lead |

`purchase_complete` uses the Razorpay **payment id** as `transaction_id`/`event_id`, the same id
studio uses and the server-side Conversions API sends, so Meta counts each sale once. The container
also stores it in localStorage so a refresh can't fire it twice.

Also pushed (no tags in the container yet, available for reports): `lp_checkout` (step = open,
otp_sent, otp_verified, details_saved, coupon_applied, payment_open, payment_dismissed, done,
error), `sign_up`, `studio_signup_complete`, `start_trial`, `add_payment_info`, and the page's
`ob_*` events.

### One GTM change needed for Meta Lead
Tag "Meta Lead" (custom HTML, fires on `lead_complete` and `lead`) only runs when the hostname
contains `join.allcoaching.in`, and it reads `event_id` from a `lead` event. So no Meta Lead fires
from studio or allcoaching.in today. To fix, in that tag:
1. change the hostname check to also allow `allcoaching.in` (or remove it), and
2. read the id from `lead_complete` too (`a.event==="lead"||a.event==="lead_complete"`).
Test in GTM Preview before publishing.

## After deploying: test once with a real number

1. Open `https://allcoaching.in/acapi/proxy.php?p=login/onboarding/pricing` → JSON with plans.
   If you see PHP source or a 404, PHP is not running for that folder; tell Claude.
2. Open a page with `?utm_source=test&utm_campaign=lp_test`, start the checkout with your own
   number, get the OTP, enter name + academy, choose the **free trial** (no money moves).
3. You should land on studio. Before the studio `/handoff` build is live, sign in there once more.
4. In GTM Preview / Meta Events Manager → Test events: check InitiateCheckout on the CTA click.
5. For a paid test, use a 100%-off activation code (no Razorpay window opens) or a real payment
   you refund from Razorpay.

## Known limits

- The proxy forwards the visitor's IP to the API (`X-Forwarded-For`). If the API's OTP per-IP
  limit uses the connecting IP instead, all visitors share this server's IP for that limit.
  Watch for "too many requests" on OTP in the first days; the durable fix is adding
  `https://allcoaching.in` to the API's CORS list and setting `API_DIRECT` in `checkout.js`.
- An educator who verifies on this page but finishes in studio later is treated by studio as
  returning, so no `lead_complete` fires for them. Same as studio's own resume today.
