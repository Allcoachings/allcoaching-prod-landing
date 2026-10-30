# 07 · SEO, AI search and content

## Content system at a glance
| Area | Path | Notes |
|---|---|---|
| Guide blog (v3, default for new posts since 2026-10-24) | `blog/<slug>.html` built from `.claude/skills/academy-guide-blog/content/<slug>.json` | Shopify-style layout (`blog-v3.css`), branded graphics. Use the `academy-guide-blog` skill. |
| Legacy essay posts | `blog/*.html` | `blog-post` skill for structure/JSON-LD reference |
| English library | `blogs/en/*.html` | Long-form; index `blogs/en/index.html` |
| Hinglish | `blogs/hinglish/*.html` | Existing posts maintained; **no new Hinglish posts planned** |
| Sources (markdown twins) | `sources/**/*.md` | Some posts have twins; edit both. Don't run `scripts/build.py` on v3 posts (it overwrites them with the legacy layout). |
| Compare pages | `vs/*.html` | Sourced competitor prices with check dates |
| Discovery files | `sitemap.xml`, `llms.txt`, `llms-full.txt`, `feed.xml`, `robots.txt` | AI crawlers allowed; data-resale scrapers blocked |

Content mix (guide blog): 60% how-to, 20% definitions, 10% tools, 10% comparisons. Pillars 3,000–5,500 words; how-tos 1,800–3,000. Byline **Amit Ratan, Founder & CEO** (`/author/amit-ratan`). Roadmap: `.claude/skills/academy-guide-blog/roadmap.md` (21 topics in 6 phases: academy building, course creation, brand & website, payments & selling, marketing, growth & income). Site plan (product pages, `/sell/<exam>` use-case pages, more `/vs/`, free tools like a price/income calculator): `.claude/skills/academy-guide-blog/site-plan.md`.

## On-page rules (every page and post)
- Title ≤ 65 characters (aim ≤ 60), meta description 50–175 (aim 140–170), one H1, canonical, `max-image-preview:large`, OG/Twitter tags, `en-IN` (Hinglish `hi-Latn`).
- Answer first: the first sentence of the lede answers the query on its own; each H2 is a question-shaped follow-up with a 40–60-word answer capsule.
- Product claims only from the claims register; prices only from `02-pricing.md`; mention AllCoaching as the structural fix, not hype.
- Real sources in `#references`; never fabricate stats, quotes or studies. Illustrative numbers labelled.
- Internal links: 3–6 to related guides + `/pricing` or `/start`. No links to `/demo/`.
- Images: 1600×900 cover (CDN `allcoaching-store.b-cdn.net/blog-images/` or local `assets/blog/<slug>/`), descriptive alt text, real studio screenshots.

## Structured data
Standard set: Article/TechArticle (author Person `https://allcoaching.in/author/amit-ratan#person`, publisher Organization, `datePublished`, honest `dateModified`), BreadcrumbList, FAQPage, HowTo (from visible steps), SoftwareApplication (AggregateOffer low 3999, high 24999, offerCount 6, INR), DefinedTermSet (glossary). **FAQ and glossary JSON-LD must match the visible text word for word** (same count, same text). Organization (homepage): legalName "AllCoaching Technology", slogan "The Operating System of Education", sameAs = YouTube, Instagram, Facebook, X, Telegram, Play Store, App Store.

## AI search / GEO (summary — full playbook in the `ai-search-geo` skill)
Be the source an AI answer cites: entity-anchored (AllCoaching = own-academy LMS for Indian educators), citation-shaped sentences (specific ₹ ranges with year), schema 1:1 with visible text, `llms.txt` entry per page whose description equals the page meta description, all AI crawlers allowed. `behavioral-search` picks real situational educator queries ("I made my coaching app but no students download it") and mirrors them in the H1.

## Publishing pipeline (v3 post)
1. Keyword is distinct from existing posts (`blog/`, `blogs/en/`, `blogs/hinglish/`).
2. Write the content JSON; render graphics (`graphics/<slug>.py`, `scripts/export_graphics.py assets/blog/<slug>`).
3. `python3 .claude/scripts/build_v3_post.py <json>`.
4. Register: sitemap, `llms.txt`, `blog/index.html` (`register_new_v3.py` / `refresh_v3_registrations.py`).
5. Refresh: `refresh_blogs_index.py`, `refresh_blogs_en_index.py`, `build_llms_full.py`, `build_feed_xml.py`.
6. Validate: `verify_meta_opt.py` (0 invalid JSON-LD, title/description limits), `qa_v3_posts.py`, FAQ parity, `blog_layout_lint.py`; screenshot at 1440 and 390 px.
7. Commit/push only when the owner asks.

## When facts change (pricing, features, promises)
Update every surface: pages, blogs, `sources/`, content JSONs (rebuild v3 posts), graphics specs (re-export), `llms.txt` (re-sync descriptions to meta), `llms-full.txt`, `feed.xml`, schema offers, `dateModified` + `article:modified_time` + sitemap `<lastmod>` **only on pages whose content actually changed**.

## Baseline (for growth tracking)
Blog clicks Jul → Sep 2026: 183 → 1,094/month; Sep 2026: 1,094 clicks, 66,487 impressions (Google Search Console). Use these as the only first-party SEO numbers unless the owner shares newer ones.
