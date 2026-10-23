# /landing — self-serve ad pages

| URL | For | Checkout |
|---|---|---|
| `/landing/launch` | Any educator. "Your own coaching academy, live today" + "What do you teach?" chips, demo-route vs self-serve, FAQ | plans only, no trial |
| `/landing/wordpress-vs-allcoaching` | Educators on (or considering) WordPress | plans + 14-day trial |
| `/landing/skills` | Skill coaches, pay-first | plans only, no trial |
| `/landing/growth-upsc` | UPSC / State PSC educators, sent as a personal invite (`?name=Rahul%20Sir` shows "Prepared for"). Growth plan + premium Rajya Seva theme (₹10,000 value) free. Live preview of `/landing/themes/rajya-seva.html` | Growth only (`plans:['growth']`), no trial |

- Shared styles: `lp2.css` for every page (`landing.css` is the retired v1 sheet; bump `?v=` on every page's `<link>` after editing; CSS is cached for a year).
- Checkout: `/assets/checkout.js` (see `templates/lp/README.md`). Any button with `data-checkout`
  opens it; `data-plan` preselects a plan; `data-vertical` files the studio under a subject.
- URL options on every page: `?code=OFFER` (activation code), `?plan=pro`, `?checkout=1`.
- Tracking: GTM-T3KFKD3G. Pages push `ob_view`, `ob_cta_click`, `ob_scroll`, `ob_teach`; the checkout
  pushes `begin_checkout` (Meta InitiateCheckout), `lead_complete` (Lead), `sign_up`
  (CompleteRegistration), `add_payment_info`, `start_trial`, `purchase_complete` (Purchase).
  /landing paths are not matched by the old "Click - Start Onboarding" trigger, so InitiateCheckout
  fires once, from the checkout.
- No competitor is named on these pages: their prices and claims would need a dated source.
