# GTM changes for the full Meta funnel (GTM-T3KFKD3G)

Do these in the **Default Workspace**, check in **Preview**, then **Submit → Publish**.
Nothing here goes live until you publish.

## 1. Import the new tags (15 items, nothing existing is touched)

Admin → **Import Container**
- Select file: `templates/lp/gtm-funnel-import.json`
- Workspace: **Default Workspace**
- Import option: **Merge** → **Rename conflicting tags, triggers and variables**
  (NOT Overwrite: Overwrite deletes the 78 existing items)
- The preview must say **0 Modified, 15 Added, 0 Deleted**. Only then press **Confirm**.

Adds: Meta Pixel InitiateCheckout (checkout), CompleteRegistration, AddPaymentInfo, StartTrial;
GA4 begin_checkout, sign_up, add_payment_info, start_trial; triggers CE - begin_checkout,
CE - sign_up, CE - add_payment_info, CE - start_trial; variables DLV - content_name,
DLV - content_ids, DLV - predicted_ltv.

## 2. Trigger "Click - Start Onboarding": stop the double InitiateCheckout

Triggers → **Click - Start Onboarding** → add a condition:
`Page Path` · `does not match RegEx` · `^/onboarding-`

(The new /onboarding-* pages send InitiateCheckout from the checkout itself. /onboarding and
/onboarding2 keep using this click trigger.)

Optional, for X: Tags → **X Pixel - Checkout start** → add firing trigger **CE - begin_checkout**.

## 3. Tag "Meta Pixel - Lead": fire on every site, with the dedup id

Done in the Default Workspace on 2026-10-19. The tag now runs on every hostname (the old code
returned early unless the hostname was join.allcoaching.in), takes its eventID from the latest
`lead` or `lead_complete` event in the dataLayer (the user id, same as the server CAPI Lead),
re-inits the pixel with the latest `user_identified` fields for advanced matching, and sends
`Lead` with content_category 'General'.

## 4. Tag "Meta Pixel - Purchase": send the plan with the value

Replace the whole HTML with:

```html
<script>
(function () {
  if (typeof fbq !== 'function') {
    !function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
    fbq('init', '391186199904157');
  }
  var p = { value: Number({{DLV - value}}) || 0, currency: 'INR', content_category: {{DLV - content_category}}, content_type: 'product', num_items: 1 };
  var ids = {{DLV - content_ids}}; if (ids && ids.length) p.content_ids = ids;
  var n = {{DLV - content_name}}; if (n) p.content_name = n;
  fbq('track', 'Purchase', p, { eventID: {{DLV - transaction_id}} });
})();
</script>
```

The eventID stays the Razorpay payment id, as before.

## 5. Test before publishing

Preview → open `https://allcoaching.in/onboarding-skills?checkout=1` and in Meta Events Manager
→ Test events check, one each:
- InitiateCheckout (one, not two) when the checkout opens
- Lead after OTP on a new number (Browser + Server shown as deduplicated)
- CompleteRegistration after name + academy
- StartTrial (trial) or AddPaymentInfo + Purchase (payment)

## Duplicate check (why each fires once)

| Event | Guard |
|---|---|
| InitiateCheckout | checkout pushes it once per page view; click trigger excluded on /onboarding-* |
| Lead | eventID = user id on browser, studio and server CAPI → Meta merges |
| CompleteRegistration | once per educator (localStorage guard), eventID `reg_<id>` |
| AddPaymentInfo | eventID `api_<order id>` |
| StartTrial | once per educator, eventID `trial_<id>` |
| Purchase | eventID = payment id; "Purchase Gate - dedupe" blocks a refresh re-fire |
