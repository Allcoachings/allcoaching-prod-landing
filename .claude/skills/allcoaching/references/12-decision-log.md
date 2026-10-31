# 12 · Owner decision log

Newest first. A newer line always overrides an older one. Add a dated line whenever the owner confirms or changes something, then update `SKILL.md`, the matching reference file and `CLAUDE.md`.

## 2026-10-31 (handover — state at end of session)
- **Blogs live:** roadmap #7 `/blog/how-to-write-a-course-description`, #8 `/blog/domain-name-for-coaching-institute`, #9 `/blog/coaching-institute-website-without-wordpress` (PR #48). Next on the roadmap: #10 white-label app, #11 institute name ideas, #14 30-day launch plan.
- **Open owner questions on those posts:** can educators edit course-page title/description/price; which DNS records the studio asks for and is HTTPS automatic; which pages payment gateways ask for; OK to say "free sample lesson" instead of "demo lesson". Sales playbook also says "we help upload the first course in the trial" — confirm the team does this.
- **Meta (Allcoaching Ads, act 990094238714767):** campaign "AC | Purchase | CBO | Oct30 | Price vs NoDev" (id 120250214534230298), Sales/Purchase, CBO ₹1,500/day, PAUSED. Ad sets: AS1 Broad India 23-50 (120250214628760298) → creative "Price" (dark, Apna LMS ₹3,999/month, Buy Now); AS2 Teacher/Tutor/Professor (120250214639110298) → creative "No developer" (white). Ads NOT yet created (images need a public URL; interests for AS2 not added). Plan: add the 9:16 video as a 3rd ad to the winning ad set after 5 days. Best historic ad: LMS-08 (₹6,999 one-time copy — retired; do not rerun as is).
- **Creative rules learned:** owner likes dark navy + blue-line backgrounds, real MacBook + iPhone mockups with real studio/academy screens, yellow price highlight, logo top-right, "No developer · No agency · No third-party LMS", "Your website live today" (never "live in 10 minutes"). Purchase ads: CTA "Buy Now", no trial lines.
- **Studio speed:** PageSpeed mobile 57. Main JS 1.3 MB, CSS 578 KB, fonts via CSS @import (includes non-brand Outfit), GTM not delayed. Fix list given to the owner for Sumit (lazy-load branding/integrations/upload, fonts, CSS, delay GTM, cookie banner).
- **Docs made (not in repo):** Sales Playbook PDF (14 pages, Hinglish) for new sales executives; Educator brochure PDF in Hinglish ("Apna LMS") and English ("Your own LMS"), 8 pages, QR to studio with utm_source=brochure.
- Logo/brand for third-party tools: theme colour #2B44FF, navy #0A0F3D, 256×256 logo PNG/JPG from `assets/logo/allcoaching-logo.webp`.

## 2026-10-30
- **Old context cleared:** `CLAUDE.md` now holds only current facts (superseded pricing/positioning bullets removed; their history stays in this log). `blog-post` skill's retired "ecosystem, never an LMS", "Start Selling for Free", "Book a Demo" and revenue-share lines replaced.
- **Blog skill:** `academy-guide-blog` is THE skill to apply whenever the owner says "blog likho"; it loads this master skill first. Also uploaded to the owner's claude.ai account (repo copy is the master; re-upload the zip after changes).
- **Live demo retired.** `/demo/` pages redirect to `/start` (noindex); no "live demo", "free demo" or "click-through demo" anywhere. Use the 7-day trial and /pricing.
- **No AI question generation** in the studio (yet). Educators draft with general AI tools, review, then upload.
- **Real features confirmed:** test series all-India rank and percentile; certificates (branded, auto-issued, unique ID); bulk student import (Excel/Google Sheet); full-screen anti-cheat lock; randomised question order; course page with SEO, schema and checkout created automatically on save; founder bio as written.
- **Unsourced performance stats removed** ("10–20x faster authoring", "60–110% more repeat attempts", hallucination percentages). Describe benefits qualitatively.
- Owner asked for this master skill so every task (site, design, ads, social, scale) stays consistent. Uploaded to the owner's claude.ai account the same day (skill "allcoaching"); repo copy is the master, re-upload the zip after every change.

## 2026-10-29
- **Studio pricing is FINAL** ("studio wala pricing final hai"): monthly 0% Starter ₹3,999 / Growth ₹5,999 / Pro ₹7,999; yearly Starter ₹6,999 + 10% / Growth ₹12,999 + 7.5% / Pro ₹24,999 + 5%; details per studio compare table; iOS on Pro monthly and every yearly plan; no sales limit. Pricing starts at ₹3,999.
- **Exit rule:** offline at end of paid period → 30 days to export or come back → uploaded videos deleted.
- Studio-like **Monthly/Yearly toggle** on /pricing and homepage; positioning **full control**, never cheap.
- Remove every old model and false promise site-wide (done: PRs #39–#43).

## 2026-10-28 (superseded 10-29)
Three plans: Starter ₹6,999/yr + 10%, Growth ₹7,999/mo 0%, Pro ₹14,999/mo 0%; ₹79,990 / ₹1,49,990 yearly ("2 months free"); Extend packs ₹499 / ₹399; ₹7 lakh breakeven.

## 2026-10-27
- Trial changed from **14 to 7 days**, no card.
- Monthly 0% plans introduced (with sales limits ₹50,000 / ₹1.5 lakh — later removed); Scale paused.
- Monthly plans: no lock-in, stop any month.
- Showcase approved: Biology Lessons, CHEMPSI, DigiteKM (no numbers, no quotes).
- Apps published on the educator's own Play Console / App Store, by the educator or by AllCoaching with API access.

## 2026-10-25
Scale ₹99,999/yr at 0% (contact-us only) added; iOS limited to Pro (later superseded by the studio table). Scale now retired.

## 2026-10-24
- Positioning: **Shopify for educators**, "The academy platform for educators"; enemy = complexity.
- Blog v3 (Shopify-style) layout and branded graphics become the default for new posts; English only for new posts.
- Competitor pricing pages checked (Learnyst, Edmingle, others) — see `10-competitors.md`.
- Studio v5 design shared (sample data; unconfirmed modules not to be claimed).

## 2026-10-21
Old `/onboarding*` pages removed (301) in favour of the on-page checkout; built-in live classroom hours later defined by plan.

## 2026-10-20
Positioning "like Shopify, for coaching" (sign up → plan → upload → domain → sell). Every plan: own Android app, unlimited YouTube video and live via YouTube Live/Zoom, plugins, Pixel + GTM. Removed "₹1 lakh sold → ₹90,000 yours" examples from pricing.

## 2026-10-17
Payouts: automatic via Razorpay — never sell payout speed. Classplus prices checked (₹29,999 / ₹39,999).

## 2026-10-15
Manifesto rewritten ("Every educator deserves their own academy, built by themselves"). Traction line: **500+ educators** (never "thousands").

## 2026-10-12 / 10-09
Website look: light theme, electric blue `#2B44FF`, cyan light rays, Inter Tight 200/700, Instrument Serif italic wordmark; ochre retired. LMS positioning: "Build your own LMS. In just a few clicks."

## 2026-10-08
"Sell your courses online. Your way." (superseded). No founding year/city on marketing pages.

## 2026-10-07
Trial needs no card. Free-forever / flat 10% / one-time models retired.

## 2026-09-28
Three annual plans (₹6,999 / ₹12,999 / ₹24,999 at 10 / 7.5 / 5%) replace the one-time model (yearly plans still live today).

## 2026-07-08
Public email becomes **contact@allcoaching.in** (old gmail must never reappear).

## Company facts (stable)
Legal entity **AllCoaching Technology** (not "Pvt. Ltd."). Founded 2018, Prayagraj (keep year/city off marketing pages; legal/about/contact may show the registered location). Founder & CEO **Amit Ratan**. Phone/WhatsApp +91 98899 77262. Grievance officer: Amit Ratan (48 h acknowledgement).
