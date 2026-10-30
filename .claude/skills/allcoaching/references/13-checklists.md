# 13 · Checklists (run before handing anything over)

## Any copy (page, post, ad, caption, email, WhatsApp)
- [ ] Prices/% exactly as `02-pricing.md`; monthly 0% vs yearly fee not mixed; "+ GST" nearby.
- [ ] Trial = "7-day free trial, no card needed"; no free plan language.
- [ ] Nothing from the FALSE list; nothing UNVERIFIED stated as fact (`04-voice-and-claims.md`).
- [ ] Lead with own academy / full control; marketplace only as extra.
- [ ] educator / studio; no "!"; no hype or banned words; illustrative numbers marked.
- [ ] CTA → Start free trial (studio.allcoaching.in) or /pricing; no demo links.
- [ ] Competitor facts sourced with date.
- [ ] Contact: contact@allcoaching.in · WhatsApp +91 98899 77262.

## Design (page, poster, ad, graphic)
- [ ] White/mist canvas, `#2B44FF` the only accent, navy only for final band/footer.
- [ ] Inter Tight 200 + 700 headline; Instrument Serif italic only for wordmark/quotes; JetBrains Mono eyebrows.
- [ ] One solid blue button per section.
- [ ] Real studio screenshot / product moment; "Studio preview · sample data" where needed.
- [ ] Logo: round mark + italic wordmark, clear space, right version for the background.
- [ ] Mobile 320 px OK, AA contrast, reduced-motion respected, alt text.

## New web page / landing page
- [ ] Title ≤65, description 50–175, canonical, OG/Twitter, one H1.
- [ ] JSON-LD valid; FAQ/glossary schema = visible text verbatim; offers per `02-pricing.md`.
- [ ] GTM via delayed loader; events per `08-tracking.md`; UTMs carried into checkout.
- [ ] Registered in sitemap + `llms.txt` (description = meta); `llms-full.txt` rebuilt.
- [ ] Smoke-tested at 1366 and 390 px, no console errors.

## Blog post
Follow the `academy-guide-blog` skill pipeline, plus: keyword distinct from existing posts; answer-first lede; HowTo from visible steps; author Amit Ratan; 3–6 internal links; graphics exported; indexes, feed, llms refreshed; `verify_meta_opt.py`, `qa_v3_posts.py`, FAQ parity pass.

## Ad campaign
- [ ] Angle chosen; copy from/consistent with the copy bank; price line exact.
- [ ] Landing page matches the ad's promise and price.
- [ ] UTMs set; optimisation event chosen (Lead first); no test events to production.
- [ ] Creative specs and safe zones; Meta personal-attributes rule respected.
- [ ] Old drafts checked for 14 days / old prices before publishing.

## Social post
- [ ] Pillar and format chosen; hook in first line / first 2 seconds.
- [ ] Hinglish/English fits the channel; captions on video.
- [ ] Link with UTMs; no client numbers or unapproved logos.

## Pricing or feature change (owner decision)
- [ ] Decision logged in `12-decision-log.md` with date.
- [ ] `SKILL.md` §2/§3 + reference files + `CLAUDE.md` updated.
- [ ] Consistency sweep run across the whole repo (`09-website-and-repo.md`).
- [ ] Studio copy/API checked to match; developer brief updated if studio must change.
- [ ] Ads, posters, graphics, `llms.txt`, schema updated; dates bumped only where content changed.

## Before commit / deploy (only when the owner asks)
- [ ] `git status` reviewed; no `.claude/settings.local.json`.
- [ ] Validators pass; smoke test clean.
- [ ] Commit → push → PR → merge → verify live with cache-buster.
