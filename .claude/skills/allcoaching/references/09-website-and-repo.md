# 09 · Website and repo (allcoaching.in)

Repo **Allcoachings/allcoaching-prod-landing** — static HTML/CSS/JS, deployed from GitHub `master` (live ~10 s after merge). Studio is a separate codebase (not in this repo).

## Layout
- Root pages: `index.html`, `pricing.html`, `start.html`, `faq.html` (39 answers), `about.html`, `contact.html`, `press.html`, `manifesto.html`, `brand.html`, `terms.html`, `privacy.html`, `educator-agreement.html`, `404.html`, `author/amit-ratan.html`.
- `landing/` ad landing pages (`lp2.css`), `landing/themes/rajya-seva.html` theme demo page.
- `vs/` compare pages (Classplus, Graphy, Teachmint, AppX, index).
- `blog/`, `blogs/en/`, `blogs/hinglish/`, `blogs/hi/` (index only), `sources/` markdown twins.
- `demo/` — **retired** (all pages redirect to `/start`, noindex; service workers self-unregister). `demo/assets/shots/*.webp` are still used as images.
- `assets/`: `checkout.js` (on-page checkout, `?v=16`), `track.js`, `attribution.js`, `logo/`, `hero/`, `showcase/`, `ads/2026-10/`, `blog/<slug>/`, `manifesto/`.
- `acapi/proxy.php` — same-origin proxy to the studio API.
- `brand.css` (site tokens), `blog-v3.css` (guide blog), `styles.css`.
- `data/site.yaml`, `data/authors.yaml`, `data/legacy-manifest.yaml` (teasers used by index refresh scripts).
- `templates/` (Jinja partials; `templates/lp/*.md` developer docs).
- `.claude/scripts/` (~95 Python helpers), `.claude/skills/` (this skill + `academy-guide-blog`, `ai-search-geo`, `behavioral-search`, `blog-post`).
- `CLAUDE.md` — project instructions (summary of this skill's non-negotiables).

## Key scripts
Build: `build_v3_post.py`, `build_feed_xml.py`, `build_llms_full.py`, `refresh_blogs_index.py`, `refresh_blogs_en_index.py`, `refresh_v3_registrations.py`, `register_new_v3.py`, `scripts/build_sitemap.py`.
Validate: `verify_meta_opt.py` (titles ≤65, descriptions 50–175, JSON-LD parses), `verify_jsonld_strict.py`, `qa_v3_posts.py` (2 known false positives: classplus-ka-best-alternative, classplus-vs-graphy-vs-allcoaching), `blog_layout_lint.py`, `v3_sync_schema.py`, `sync_faq_schema.py`, `link_check.py`, `seo_audit.py`.
Note: `refresh_blogs_index.py` resets the hub's CollectionPage `dateModified` and may add blank lines — check the diff before committing.

## Local preview and QA
`python3 -m http.server 8765` in the repo, then Playwright (`require('playwright')`, `chromium.launch()`) to load key pages at 1366 and 390 px and collect `pageerror` + failed local requests. Pages to smoke-test: `/`, `/pricing`, `/start`, `/faq`, `/landing/*`, `/vs/*`, a blog post, `/blog/`, legal pages.

## Deploy flow (only when the owner says commit/push/live)
1. Start clean: `git fetch origin master && git checkout -B <work-branch> origin/master`.
2. Make changes; validate (meta, JSON-LD, FAQ parity, smoke test).
3. `git add` (never `.claude/settings.local.json`), commit with a clear message, `git push -u origin <work-branch>`.
4. Open a PR to `master` and merge it (GitHub MCP: `create_pull_request`, then `merge_pull_request` with the head SHA).
5. Verify live with `curl "https://allcoaching.in/<path>?cb=$RANDOM"` until the change appears.

## Consistency sweep (run whenever a fact changes)
1. Grep the whole repo for the old value in every form (₹7,999 vs 7999 vs 7,999/mo; "14-day", "14 days", "14 din"; "demo/"; feature names), including `blog/`, `blogs/`, `sources/`, `landing/`, `vs/`, `templates/`, `data/`, `llms.txt`, `.claude/skills/**`, content JSONs and graphics specs.
2. Fix visible text **and** JSON-LD together (FAQ verbatim parity).
3. Rebuild v3 posts and re-export graphics if JSON/specs changed.
4. Sync `llms.txt` descriptions to page meta; rebuild `llms-full.txt`, `feed.xml`, blog indexes.
5. Bump `dateModified`, `article:modified_time` and sitemap `<lastmod>` only on pages whose content changed.
6. Update `CLAUDE.md`, this skill, and the decision log.
7. Validate, smoke-test, then (if asked) deploy and verify live.

## Known housekeeping items
- `data/site.yaml` must use contact@allcoaching.in (not hello@) and the current tagline.
- `brand.html` and `landing/launch.html` must not mention a demo.
- `.claude/skills/behavioral-search/SKILL.md` and `academy-guide-blog` price lines must follow `02-pricing.md`.
