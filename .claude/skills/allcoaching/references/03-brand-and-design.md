# 03 · Brand and design system

Live guideline: allcoaching.in/brand (`brand.html`, v2, Oct 2026). Tokens: `brand.css` (v1.1 + "Website look v2 · light blue" override) and `blog-v3.css` (blog guide layout). This file is the summary to design from.

## Essence
- **Headline:** "Build your own LMS. In just a few clicks."
- **Promise:** Launch it yourself — no developer, no sales call.
- **Proof:** Your brand, your money — own domain on every plan, 0% commission on monthly plans.
- **Feeling:** light, calm, trustworthy. Editorial restraint over decoration.

## Colour
| Role | Hex | Use |
|---|---|---|
| Electric Blue (primary, the only accent) | `#2B44FF` | Buttons, links, accent words, featured plan |
| Deep Blue (hover/pressed) | `#1A2FD9` | Hover |
| Light blue | `#5B6CFF` | Gradient start |
| Sky (tint) | `#E8F0FF` | Icon tiles, highlights, soft fills |
| Cyan | `#22C3F5` | Light rays and gradients only |
| Navy | `#0A0F3D`, `#070A26` | Final CTA band, footer |
| Ink | `#14161F` | Headlines |
| Slate | `#4A5063`, `#7A8094` | Body, captions |
| White / Mist / Line | `#FFFFFF`, `#F6F8FC`, `#E6E8F0` (`#D9DCE7`) | Backgrounds, alternate sections, borders |
| Live / paid / connected | `#16A34A` | Status only |
| Pain side of a card | `#D64545` (tint `#FFF6F6`, border `#F3CFCF`) | Problem side only |
Ratio: white 62% · mist 16% · ink 10% · blue 6% · navy 5% · cyan 1%. **Forbidden:** gold, ochre (`#C58B43` retired), cream, purple, rainbow gradients.

Gradients: accent `linear-gradient(135deg,#5B6CFF 0%,#2B44FF 55%,#1A2FD9 100%)` · hero background `linear-gradient(180deg,#F3FBF8 0%,#F4F6FF 55%,#fff 100%)` with soft blobs `#D7F5E9` / `#E4E2FF` (blur 60px, .75) · feature panel `radial-gradient(120% 140% at 0% 0%,#3C55FF 0%,#2337E0 40%,#14209E 100%)` · quote band `linear-gradient(135deg,#E8F0FF,#EEF2FF)`.

**Light rays (signature graphic):** blue-to-cyan rays under a soft white arc with a real studio screenshot on top. Stripes `repeating-linear-gradient(90deg,transparent 0 14px,rgba(255,255,255,.22) 14px 16px,transparent 16px 34px)` over `linear-gradient(90deg,#B9F0FF,#4FD2FA 14%,#2B7BFF 34%,#2B44FF 52%,#2B7BFF 70%,#4FD2FA 86%,#B9F0FF)`; shimmer 14 s.

## Type
| Family | Job | Rules |
|---|---|---|
| **Inter Tight** | UI and headlines | Headlines mix weight **200 (setup) + 700 (payoff)**, tracking −0.03em. Body 400, 15–18px, line-height 1.55–1.6. Buttons 500–600. |
| **Instrument Serif italic 400** | Wordmark "AllCoaching", pull quotes, manifesto lines | Never buttons or body. Emphasis by colour, never bold. |
| **JetBrains Mono** | Eyebrows, numbers, IDs | 12px, caps, 0.14em tracking. |
Scale: display 38–72px · heading 28–48px · card title 17–20px/700 · body 15–18px · eyebrow 12px mono. Hero h1 payoff may use an ink→blue gradient. **Fraunces is not a brand font.** Blog v3 posts use Inter (headlines weight 330) + IBM Plex Mono — see `academy-guide-blog`.

## Layout and components
- Container 1180px, side padding 24px (16px under 640px). Sections 88px vertical (64px mobile), 1px top border `#E6E8F0`. Grid gaps 14–16px.
- Nav 64px, sticky, `rgba(255,255,255,.85)` + 16px blur. Nav: Features · Academies · Pricing · Blog · FAQ · Log in · **Start free trial**.
- Radii: buttons 10px · cards 20px · panels 18px · tiles 14px · pills 999px · logo mark circle.
- Shadow `0 1px 2px rgba(20,22,31,.05),0 10px 30px -14px rgba(20,22,31,.18)`; deep `0 40px 80px -36px rgba(23,40,160,.35),0 12px 30px -16px rgba(20,22,31,.2)`; focus ring `0 0 0 3px rgba(43,68,255,.22)`. Easing `cubic-bezier(.22,.85,.25,1)`.
- Buttons: `.b-blue` solid (#2B44FF, white, glow shadow) · `.b-line` outline · `.b-white` on navy · `.b-ghost` on blue. **One solid blue button per section**, outline for the second action. Labels: "Start free trial", "Start free for 7 days", "See plans and pricing", "Ask on WhatsApp". No demo buttons.
- Pill badge: "7-day free trial · no card needed" with a green dot.
- Floating "product moment" cards: "youracademy.in · Connected", "Paid by UPI ₹4,999" (real product moments only).
- Pain → fix card: red-tint pain side, white fix side.
- Monthly · 0% commission / Yearly **toggle** (same as studio): monthly default, `aria-pressed`, synced across sections.
- Icons: line icons, 24px viewBox, `stroke="currentColor"`, round caps/joins, stroke 1.8.
- Footer (navy): Product · Company · Educators · Students columns; line "© 2026 AllCoaching · Made in India · The Operating System of Education".

## Logo
Round gradient mark (`assets/logo/allcoaching-logo.webp`) + "AllCoaching" in Instrument Serif italic. Versions: on white (default), on navy (footer), on blue (social/ads). Clear space ≥ mark height; minimum mark 24px. Don't: bold sans wordmark, recolour, stretch, rotate, effects, busy photos.

## Imagery
- **Real studio screenshots** (2x, light mode) in MacBook/iPhone frames; caption sample data "Studio preview · sample data". Never mock up features that don't exist.
- Showcase academies: only Biology Lessons, CHEMPSI, DigiteKM screenshots/logos (no numbers, no quotes).
- No stock photos of "happy students"; prefer product, educator-at-work, real UI.
- Third-party logos (Google, YouTube, Instagram, WhatsApp, Razorpay, Zoom) are fine as real marks with "Logos belong to their owners" where needed.

## Ads / social creative style (from the owner's creatives)
Lavender canvas (`#FBFBFE → #F3F4FC → #E8EBFF`), heavy Inter Tight headline with **one electric-blue phrase**, white pill cards, real studio screenshot in a device frame, round logo + "AllCoaching / The academy platform for educators" lockup, one CTA ("Start free trial" / "Apni academy banaiye"), badge pills ("0% commission · on monthly plans", "7 din free · card nahi chahiye"). Problem/solution split: grey problem half (`#F2F2F4 → #E6E6EA`, optional Caveat handwriting) vs lavender solution half. Sizes: 1080×1080 (feed), 1080×1350 (4:5 feed), 1080×1920 (stories/reels, keep 250px safe zones top/bottom), 1200×628 (link/Google), 1600×900 (blog cover). Existing set: `assets/ads/2026-10/` (`ad-apna-lms`, `ad-ek-login`, SVG source + PNG).

## Motion
Drifting blobs 18 s, floating cards ±8px over 7 s, ray shimmer 14 s, fade-up on scroll. Always honour `prefers-reduced-motion` (no animation). Never animate prices or legal text.

## Accessibility
AA contrast (blue `#2B44FF` on white passes for text ≥ 14px bold / buttons), visible focus ring, alt text that describes the screen, 44px touch targets, works at 320px with no horizontal scroll.

## Ten-second brand check
1. White/pastel background, one blue accent, navy footer. 2. Headline mixes 200 + 700, payoff bold. 3. Instrument Serif italic wordmark beside the round mark. 4. "Build your own LMS" and the 7-day free trial visible. 5. One solid blue button per section → free trial. 6. Real screenshot or real product moment. 7. Prices match `02-pricing.md`; 0% only on monthly. 8. No "!", no "cheapest", no invented numbers. 9. Works at 320px. 10. Contact contact@allcoaching.in · WhatsApp +91 98899 77262.
