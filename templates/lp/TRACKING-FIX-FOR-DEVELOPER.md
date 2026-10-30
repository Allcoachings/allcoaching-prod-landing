# Tracking fixes for Meta Ads and Google Ads (checked 2026-10-28)

For: the studio and learn-app developer. Owner: AllCoaching.

## What was checked

No test events were sent to Meta or Google. Everything below comes from reading live code and live data.

| Source | What was read |
|---|---|
| GTM-T3KFKD3G (allcoaching.in + studio), published version 48 | Every tag, trigger and variable in the live container (`gtm.js`) |
| GTM-K3C28Z7T (learn app + educator sites), version 4 | Every tag |
| Meta dataset 391186199904157 "AllCoaching Pixel" | Last 28 days: events, browser vs server, hosts, Event Match Quality |
| Chrome (Playwright) | allcoaching.in, /pricing, /start, studio.allcoaching.in login, learn.allcoaching.in, biolessons.in, chempsi.com: scripts loaded, pixels initialised, `fbq` calls, `dataLayer`, Google requests |
| Studio code (live build) | `/ac-tracking.js`, `index-DghfFEFK.js`, `OnboardingPage-Dh9roIq4.js` |
| Learn app code (live build) | Next.js chunk `3-nm6d0guptfq.js` (tracking helpers) |
| Marketing checkout | `assets/checkout.js` in this repo, the reference implementation |

## The event contract

Every surface (marketing checkout, studio onboarding, studio billing) must push exactly these `dataLayer` events, with exactly these `event_id` formats.

GTM was cross-checked against this list. The trigger names match the event names exactly. Do not rename them.

| # | `dataLayer.push({event: …})` | When (once) | `event_id` | Required fields | GTM sends |
|---|---|---|---|---|---|
| 1 | `begin_checkout` | Checkout or plan screen opens, once per page view | `ic_<uuid>` | `value` (plan price, ex-GST), `currency:'INR'`, `content_ids:[plan]`, `content_name` | Meta **InitiateCheckout** (tag 85), GA4 `begin_checkout` (82) |
| 2 | `lead_complete` | New number verified by OTP (new educator only) | `<user id>` (raw) | `lead_id` (= same id), `user_email`, `user_phone` | Meta **Lead** (48), GA4 `generate_lead` (41), Google Ads **Lead** `AW-11343265505/0sOMCPfuvMkcEOH98aAq` (47) |
| 3 | `sign_up` | Name + academy saved (new studio) | `reg_<educator id>` | `method:'phone_otp'`, `educator_id`, `content_name:'Studio created'`, `value:0` | Meta **CompleteRegistration** (80), GA4 `sign_up` (91) |
| 4 | `add_payment_info` | Razorpay window opens | `api_<razorpay order id>` | `value`, `currency`, `content_ids`, `content_name` | Meta **AddPaymentInfo** (86), GA4 `add_payment_info` (90) |
| 5 | `start_trial` | Trial starts | `trial_<educator id>` | `plan`, `value:0`, `currency:'INR'`, `predicted_ltv` (chosen plan's price) | Meta **StartTrial** (88), GA4 `start_trial` (89) |
| 6 | `purchase_complete` | Server verified the payment | `<razorpay payment id>`, also `transaction_id` = the same id | `value`, `currency`, `content_ids`, `content_name`, `external_id`, `user_email`, `user_phone` | Gate tag 76 → `purchase_verified` → Meta **Purchase** (43, eventID = `transaction_id`), GA4 `purchase` (49), Google Ads **Purchase** `AW-11343265505/VHMxCJzRlskcEOH98aAq` (42, order id = `transaction_id`) |
| 7 | `user_identified` | After login, when user data changes | none | `external_id`, `em`, `ph` (`91XXXXXXXXXX`), `fn`, `ln`, `country:'in'` | Meta advanced matching (56) |

How each `event_id` is used:
- Meta merges a browser event and a server (CAPI) event only when both have the same name and the same `event_id`.
- Any server-side CAPI call must use the same ids as above:
  - Purchase: the **raw** Razorpay payment id. Not `purchase_<id>`, even though gate tag 76 also writes `event_id: "purchase_<id>"`. The Meta Purchase tag reads `transaction_id`.
  - Lead: the raw user id.

## Problems found and the exact fixes

### P1 (critical): the learn app sends students' events into the AllCoaching pixel

**Proof:**
- Meta, last 28 days, `Purchase` by host: learn.allcoaching.in 5, www.biolessons.in 3, studio.allcoaching.in 4, allcoaching.in 4. So **8 of 16 Purchases are student course sales**, not educator plan payments.
- `InitiateCheckout` and `ViewContent` also arrive from learn.allcoaching.in, biolessons.in and digitekm.com.
- Meta optimises and reports ROAS on these.

**Cause:** in the learn app (chunk `3-nm6d0guptfq.js`, module 89469), `setUserId()` runs on every student login and calls:

```js
window.fbq("init", "391186199904157", a)   // AllCoaching's educator pixel, hard-coded
```

After that, every `fbq("track", …)` in the learn app is sent to both pixels: ViewContent, InitiateCheckout and Purchase. The learn app's own GTM (GTM-K3C28Z7T) only inits 776849551172060, which is correct.

**Fix (learn app):** never init 391186199904157 in the learn app. Re-init the pixel the site already uses:

```js
// tracking helper, setUserId()
const LEARN_PIXEL = '776849551172060';          // or the educator's own pixel id, if the site has one
if (typeof window.fbq === 'function' && a.external_id) {
  window.fbq('init', LEARN_PIXEL, a);          // advanced matching for the learn pixel only
}
```

If the learn app ever needs to send one event to one pixel, use `fbq('trackSingle', PIXEL_ID, 'Purchase', …)`, never `fbq('track', …)` with two pixels initialised.

**Owner (Events Manager):**
- After the fix ships, open Dataset 391186199904157 → Settings → **Traffic permissions** → **Allow list**.
- Allow only `allcoaching.in` and `studio.allcoaching.in`.
- This also blocks the 750 test events in 28 days from `127.0.0.1` and `localhost`.

### P2 (high): studio sends CompleteRegistration with a random id

**Cause:** in `OnboardingPage` (`complete()`), `sign_up` is pushed with `{conversion:true}` and no `event_id`. `AC.track` then fills in a random `uuid`.

The contract and `assets/checkout.js` use `reg_<educator id>`. A random id cannot match a server copy, so dedup fails, and CompleteRegistration counts twice when the server also sends it.

**Fix:**

```js
AC.track('sign_up', {
  event_id: 'reg_' + educatorId,               // fixed, not random
  method: 'phone_otp', educator_id: educatorId, subject: vertical,
  content_name: 'Studio created', status: 'registered', currency: 'INR', value: 0,
  user_data: { email, phone }
}, { once: true, dedupKey: educatorId });
```

### P3 (high): studio sends StartTrial with no id and the wrong plan

**Cause:** studio pushes `start_trial` with `{educator_id, plan:'starter', subject, user_data}`.
- There is no `event_id`. GTM tag 88 adds an eventID only when `event_id` starts with `trial_`, so studio's StartTrial goes out with **no eventID** (no dedup).
- `plan` is always `'starter'`.
- `predicted_ltv` is missing, so the tag falls back to 6999.

**Fix:**

```js
AC.track('start_trial', {
  event_id: 'trial_' + educatorId,
  educator_id: educatorId, plan: chosenPlan,          // 'starter' | 'growth' | 'pro'
  value: 0, currency: 'INR',
  predicted_ltv: { starter: 3999, growth: 5999, pro: 7999 }[chosenPlan],   // monthly plan price ex-GST (studio pricing 29 Oct 2026); for a yearly plan use 6999 / 12999 / 24999
  content_ids: [chosenPlan], content_name: planLabel + ' plan trial',
  user_data: { email, phone }
}, { once: true, dedupKey: educatorId });
```

Also fix the toast text in the same function: "Your academy is live — 14 days free, nothing charged." becomes **"7 days free"**. The login page line "Free for your first 14 days" must also say **7 days**.

### P4 (high): studio never sends InitiateCheckout or AddPaymentInfo

**Cause:** the studio bundle has no `begin_checkout` or `add_payment_info` push. Only the marketing checkout (`assets/checkout.js`) sends them. Educators who sign up on studio.allcoaching.in directly are missing two funnel steps in Meta and GA4.

**Fix:** push the same payloads as `assets/checkout.js` (lines 546–555 and 1055–1059):

```js
// plan / pricing step shown (once per page view)
AC.track('begin_checkout', {
  event_id: 'ic_' + AC.uuid(), value: planPriceExGst, currency: 'INR',
  content_ids: [plan], content_name: planLabel + ' plan', content_type: 'product', num_items: 1
}, { once: true, dedupKey: 'ic' });

// right before new Razorpay(...).open()
AC.track('add_payment_info', {
  event_id: 'api_' + order.order_id, value: order.amount / 100, currency: 'INR',
  content_ids: [plan], content_name: planLabel + ' plan', content_type: 'product', num_items: 1
}, { once: true, dedupKey: order.order_id });
```

### P5 (high): consent mode loses Google Ads conversions on studio

**Proof (Chrome, studio login, before clicking Accept):** GA4 hits go out with `gcs=G100`, meaning ads and analytics storage are denied. `/ac-tracking.js` and `index.html` boot every signal to `denied`.

On allcoaching.in there is no consent default at all: hits go out with no `gcs`, so cookies work.

**Effect:**
- Studio is where Lead, sign-up, trial and Purchase happen. For every educator who ignores the banner, Google Ads cannot read the click id (gclid) cookie, so the conversion is lost or only modelled.
- The Meta pixel (GTM tag 21) ignores the banner completely and fires either way. The two ad platforms behave differently.

**Fix: needs the owner's decision.** Pick one option and apply it on both domains:
- **Option A (recommended for an India-only audience):** grant by default in India, deny by default for the EEA/UK. The banner still lets anyone decline. In `index.html`, before GTM:

  ```html
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',
      region:['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IS','IE','IT','LV','LI','LT','LU','MT','NL','NO','PL','PT','RO','SK','SI','ES','SE','CH','GB']});
    gtag('consent','default',{ad_storage:'granted',analytics_storage:'granted',ad_user_data:'granted',ad_personalization:'granted'});
  </script>
  ```

  `AC.consent(false)` (Decline) keeps working as today.
- **Option B:** keep denied until Accept on both domains. Then add the same default to allcoaching.in, and make Meta follow it:
  - `fbq('consent','revoke')` before `fbq('init')`;
  - `fbq('consent','grant')` inside `AC.consent(true)`.

### P6 (medium): Google Ads is missing enhanced conversions and two conversion actions

**Container v48 today:**
- Only **Purchase** (tag 42) and **Lead** (tag 47) exist.
- **Enhanced conversions is off on both** (`enableEnhancedConversions: false`).
- The Lead tag has no order id.

**GTM steps:**
1. Create variable **User-Provided Data – AC** (type User-Provided Data, Manual):
   - email = DLV `user_email`;
   - phone = DLV `user_phone`, format `+91XXXXXXXXXX`.
2. Tag 42 (Purchase) and tag 47 (Lead): tick **Include user-provided data from your website** and pick that variable.
3. Tag 47 (Lead): set **Order ID** = DLV `event_id`. That is the user id, so a reload cannot count twice.
4. In Google Ads, create two **secondary** conversion actions:
   - **Studio created** on `sign_up`;
   - **Start trial** on `start_trial`.

   Add one Google Ads Conversion Tracking tag for each, on triggers `CE - sign_up` and `CE - start_trial`, with Order ID = DLV `event_id`.

   Keep **Purchase** as the only primary action. Lead stays secondary until there are about 30 purchases a month.
5. Turn on **Enhanced conversions for web** in Google Ads → Goals → Settings, and accept the terms.

### P7 (medium): Purchase value and checkout value use different bases

- `begin_checkout` uses the plan price **without GST** (`PLANS[plan].fee`).
- `purchase_complete` uses `amountPaise / 100`, the Razorpay amount, which includes GST when the order includes it.

**Fix:** send `value` **without GST** on every event, and add `tax` with the GST amount, so ROAS in Meta and Google Ads equals real revenue. Check what `order.amount` contains in `institute/plan/checkout/` and use the same base in studio and `assets/checkout.js`.

### P8 (low): GA4 noise in GTM

- Tag 11 (GA4 `scroll`) fired **9 times on one studio page**, once per scroll-depth step.
  - Fix: set the scroll trigger to 50 and 90 only.
- Tag 13 (GA4 `click`) fires on every link click and floods reports.
  - Fix: limit it to outbound links, or pause it. `select_promotion` and `generate_lead` already cover the important clicks.

## After the fixes: test checklist (staging or GTM Preview, not production ads)

Use GTM **Preview**, Meta **Test Events** (Events Manager) and Google **Tag Assistant** with a new test number. Each line should show exactly once:

1. Open the plan screen. Meta **InitiateCheckout** fires once with eventID `ic_…`; GA4 `begin_checkout` fires.
2. Verify the OTP on a new number:
   - Meta **Lead** shows "Browser + Server, deduplicated" with eventID = user id;
   - the Google Ads Lead tag fires with an order id.
3. Save name and academy. Meta **CompleteRegistration** fires with eventID `reg_<id>`.
4. Open Razorpay. Meta **AddPaymentInfo** fires with eventID `api_<order id>`.
5. Pay:
   - Meta **Purchase** fires once with eventID = payment id, value without GST, INR;
   - Google Ads Purchase fires with the order id and user-provided data;
   - a page refresh fires nothing.
6. Instead of paying, start a trial: Meta **StartTrial** fires with eventID `trial_<id>`, the correct plan and `predicted_ltv`.
7. On a learn-app site (for example biolessons.in), log in as a student and buy:
   - **nothing** arrives in dataset 391186199904157;
   - events arrive only in 776849551172060.
8. Meta Events Manager → Overview → each event → **Event deduplication** ≥ 90%, and Event Match Quality for Purchase and Lead ≥ 7.

## Data seen in Meta (28 days, browser + server combined)

| Event | Count | Note |
|---|---|---|
| PageView | 17,164 | 12,822 of all events from studio.allcoaching.in, 7,497 from allcoaching.in |
| InitiateCheckout | 532 | includes learn-app and educator-site hosts (P1) |
| ViewContent | 121 | all from the learn app (P1); the educator funnel does not use ViewContent |
| CTAClick | 35 | |
| CompleteRegistration | 24 | |
| Lead | 24 | |
| StartTrial | 20 | |
| Purchase | 16 | 8 are student sales (P1) |
| AddPaymentInfo | 6 | |

Event Match Quality:

| Event | EMQ |
|---|---|
| ViewContent | 8.6 |
| InitiateCheckout | 7.8 |
| PageView | 7.0 |
| CTAClick | 6.1 (only IP, user agent, fbp; it fires before login, which is expected) |

The dataset is active and the server (CAPI) last fired on 2026-10-28.
