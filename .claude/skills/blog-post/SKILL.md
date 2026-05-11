---
name: blog-post
description: Write or edit AllCoaching long-form editorial blog posts in the established 2026 house style — strategic, distribution-first essays for Indian educators, published as standalone HTML in /blog/. Use when the user asks to draft a new blog post, edit an existing one in /blog/, or rewrite content to match the house voice and component system.
---

# AllCoaching Blog Post Skill

Use this skill when the user asks you to **write a new blog post** for `/blog/` or **edit/review an existing one** to match the house style. All posts are standalone HTML files in `blog/` — no CMS, no shared layout. Each post is self-contained.

## Reference posts

The canonical, most up-to-date pattern is in:
- `blog/best-platform-for-selling-pdf-notes-and-test-series.html` (May 2026)
- `blog/protect-course-content-from-piracy-for-free.html`
- `blog/migrate-offline-coaching-to-online-zero-cost.html`

When in doubt about a component, an SEO field, or a specific phrasing, **read one of these files** rather than guessing. The template at `templates/blog-post-template.html` in this skill folder is a scaffold — copy it, then enrich.

## Brand system — load brand.css

Every blog file references `../brand.css` which provides all design tokens, fonts (Instrument Serif italic + Inter Tight + JetBrains Mono), and component classes (.kicker, .h-mast, .h-chap, .article-body, .pull, .pull-red, .epi, .def, .scale-box, .hband, .verdict, .gain-card, .cost-card, .step-card, .myth-card, .stat-row, .cmp, .layer-card, .founder, .author-strip, .toc, .faq, .blog-card, etc.). **Never inline a `<style>` block in a blog file** — extend brand.css instead.

Headlines use Instrument Serif italic — when emphasizing a phrase, use `<em>` inside the h-mast/h-chap (this colors the italic word ochre via brand.css). Do NOT use `<span class="grad-text">` anymore — just use `<em>`.

## House voice — non-negotiable

Every post sounds like the founder, Amit Ratan, writing a strategic essay — not a marketing brochure. Specifically:

- **Diagnostic, not promotional.** Open by reframing the reader's question into a more honest one. Refuse the surface framing the reader walked in with.
- **Distribution-first thesis.** Almost every post argues that infrastructure/storage/tools is a solved problem; the real bottleneck is discoverability, distribution, and network effects. AllCoaching is positioned as an *ecosystem*, never a *tool* or *LMS*.
- **Tool vs. ecosystem** is the central rhetorical contrast. Use it explicitly.
- **Editorial, not corporate.** Warm cream canvas, italic display, ochre as the only spotlight. Match the brand guidelines feel — restrained, considered, hand-built.
- **Long, dense paragraphs.** 4–7 sentences each, 17px body, line-height ~1.85. No fluff sentences. Every paragraph advances the argument.
- **Em-dashes liberally** — for asides, contrasts, and shifts mid-sentence. This is the single most recognizable rhythmic tic of the house style.
- **Bold key phrases** inside paragraphs (`<strong>`) — usually the load-bearing claim of the paragraph. Aim for 1–2 bolded fragments per paragraph max.
- **Italics** (`<em>`) for the reader's *unspoken* question or to mark a phrase as a label being examined ("the *real* problem", "*where will my notes actually be found?*"). In headlines, `<em>` colors the word ochre.
- **Direct address.** "You", "the educator", "your content". Never "users" or "customers". We say *educator*, not *creator*. *Studio*, not *dashboard*. *Your students*, not *audience*.
- **Indian context throughout.** ₹ figures with ranges (e.g. *₹6–27 lakh/year*). Lakhs & crores — `4.8L`, `1.2Cr`. Exam categories: NEET, JEE, UPSC, SSC, banking, state board. Hindi-medium, regional language, India-specific economics. Never US/global framing. Never `$` or `INR` or "rupees".
- **Year-anchored.** "In 2026", "the next decade", "by 2030". Concrete temporal framing.
- **Authority through structural argument.** Persuade by explaining *why* something is true at the architecture/economics layer — not by adjective stacking.
- **Concede, then sharpen.** "This is not a critique of LMS platforms. They do exactly what they advertise." Then: "The misalignment is between what they provide and what most independent educators actually need."
- **No emojis. No exclamation marks. No clickbait. No "maximize". No "onboard" verb. No "unlock features".** Tone is calm, opinionated, senior-operator.
- **Word count: ~3,500–5,500 words** (reads 16–20 minutes). Posts under 14 min are too thin for this format.

## Required structural skeleton

Every post must have, in order:

1. **`<head>`** — full SEO meta block:
   - `<title>` (60–80 chars, includes year/positioning)
   - `<meta name="description">` (~160 chars, distribution-angle)
   - `<meta name="keywords">` (12–20 long-tail keywords, India-focused)
   - Canonical URL: `https://allcoaching.in/blog/<slug>`
   - Open Graph + Twitter cards (image at `https://allcoaching-bucket.b-cdn.net/Blog/<slug>.webp`, 1600×900)
   - Author: Amit Ratan, Founder & CEO, AllCoaching
   - GTM script: `GTM-T3KFKD3G`
   - Fonts: `Instrument Serif` (ital@0;1), `Inter Tight` (400–700), `JetBrains Mono` (400/500/700)
   - Stylesheets: `../dist/tw.min.css` and `../styles.css`
   - Inline `<style>` block with all blog-specific component CSS (copy from template)
   - Three JSON-LD scripts: `Article`, `FAQPage`, `BreadcrumbList`

2. **Fixed top navbar** — minimal, with `Login` and `Join Now` buttons (copy from template).

3. **Masthead** (`<header class="mast-dark">`):
   - `<span class="brand-pill">2026 Edition</span>` + editorial category label
   - `<p class="kicker">` — three short topic tags separated by `·`
   - `<h1 class="h-mast">` — broken across 2–3 lines, with last line in `<span class="grad-text">`
   - Lede paragraph (1–2 sentences, 1.18rem, max-w-2xl) that compresses the thesis
   - `<div class="author-strip">` — Amit Ratan + role + date + read-time + category

4. **Cover image** (`<div class="cover-shell">`) with `<figcaption>` strategic line.

5. **Table of Contents** (`<nav class="toc">`) — numbered `<ol>` linking to each `#section-id`. 10–14 items.

6. **Intro section** with `id="real-problem"` (or similar):
   - First paragraph uses `class="drop-cap"` — opens by reframing the reader's question.
   - 2–3 paragraphs total establishing the problem-as-actually-stated.

7. **Epigraph** (`<div class="epi">`) immediately after intro — pull quote of the central thesis with `<cite>` attribution.

8. **8–12 body sections**, each:
   - `<div class="article-body" id="...">`
   - `<h2 class="h-chap">` heading
   - 3–6 paragraphs
   - 1–2 visual components from the kit (see below)
   - Followed by `<div class="orn">· · ·</div>` separator (except the last one)

9. **Strategic Conclusion section** (`id="conclusion"`) — 4–5 paragraphs that re-answer the opening question precisely. Often ends with a bulleted list of "patterns we see in educators who win".

10. **Closing epigraph** (`<div class="epi">`) attributed to *— Amit Ratan, Founder & CEO, AllCoaching*.

11. **Founder block** (`<div class="founder">`) — Amit Ratan photo + bio + signature quote.

12. **Get Started verdict CTA** (`<div class="verdict">`) — gradient block with two buttons: "Start Selling for Free" → `educator.allcoaching.in`, and "Book a Demo" → `contact.html`.

13. **FAQ section** (`<div class="article-body" id="faq">`) — 8–10 `<details>/<summary>` pairs. Each answer 2–4 sentences with `<strong>` on the load-bearing claim. The FAQ list must match the `FAQPage` JSON-LD in `<head>`.

14. **Related Articles section** — 3 cards linking to other posts in `blog/` (use existing posts; don't invent slugs).

15. **Final CTA section** + **Footer** (copy from template — these are stable across posts).

## Component palette (CSS classes)

The inline `<style>` block defines these — never invent new ones; pick the right one for the rhetorical job.

| Component | Class | When to use |
|---|---|---|
| Topic tracker label | `.kicker` | Above any h1/h2 to tag the topic |
| Drop-cap intro | `.drop-cap` | Only on the very first body paragraph |
| Pull quote (positive) | `.pull` | Purple left-border block — for a thesis re-statement |
| Pull quote (warning) | `.pull-red` | Red left-border — for a hard truth or caution |
| Epigraph | `.epi` | Centered purple gradient — for chapter-level quotes; opens & closes the article |
| Definition box | `.def` | Grey card — when introducing a strategic term ("Tool vs. Ecosystem") |
| Strategic reframe | `.scale-box` | Blue card — when the section's job is to reframe the reader's mental model |
| Yellow takeaway band | `.hband` | Yellow band — for "Industry reality" data callouts or section takeaways |
| Verdict / CTA hero | `.verdict` | Dark gradient — for "Strategic Outlook" boxes and the closing CTA block |
| Gain card (green) | `.gain-card` | What AllCoaching does well — list 3–4 in a row |
| Cost card (red) | `.cost-card` | Hidden costs / honest calculation — usually with ₹ figures |
| Numbered step | `.step-card` | When walking through a 3–5 step process or list of features |
| Myth split (red/green) | `.myth-card` + `.myth-row` + `.myth-half` | Side-by-side "old reality vs. AllCoaching reality" |
| Stat row | `.stat-row` + `.stat-cell` | 3–6 numbers across — `.stat-num`, `.stat-num-red`, `.stat-num-green` |
| Comparison table | `.cmp` (5-col `.cmp-h5`/`.cmp-r5` or 4-col `.cmp-h4`/`.cmp-r4`) | Wrap in `.cmp-scroll`. Use `.ic-y` (green check), `.ic-n` (red X), `.ic-p` (yellow partial) |
| Architecture layer | `.layer-card` + `.layer-tag` | When breaking down system layers |
| Section separator | `.orn` (`· · ·`) | Between every body section, not after the last one |

## Editing existing posts — checklist

When the user asks you to edit a post in `blog/`, run through:

1. **Voice drift.** Are paragraphs short, breezy, or marketing-toned? Tighten to long, analytical, em-dash-rich prose.
2. **Thesis clarity.** Does the article have a single distribution-first thesis stated early and re-stated at close? If not, add the reframe in the intro and a closing epigraph.
3. **Component variety.** Are sections walls of `<p>` tags? Insert `def`, `pull`, `hband`, `gain-card`/`cost-card`, `step-card`, `myth-card`, or a `cmp` table where the rhetorical beat calls for it.
4. **Indian specificity.** Replace generic figures with ₹ ranges. Add NEET/JEE/UPSC/SSC examples where the argument is abstract.
5. **Bold load-bearing claims** in each paragraph if missing.
6. **TOC ↔ sections ↔ FAQ JSON-LD** all in sync. Update Article + FAQPage JSON-LD if section titles or FAQs change.
7. **Author strip + canonical URL + OG image** match the slug.
8. **Read-time** in `author-strip-meta` and related-card meta is honest (≈230 wpm).
9. **`orn` separators** between every body section.
10. **CTAs** point to `https://educator.allcoaching.in/` and `https://allcoaching.in/contact.html`.

## Writing a new post — workflow

1. Confirm with the user: **slug**, **headline**, **target keyword**, and **strategic angle** (what reader question is being reframed?).
2. Copy `templates/blog-post-template.html` → `blog/<slug>.html`.
3. Fill in head meta (title, description, keywords, canonical, OG/Twitter, JSON-LD schemas).
4. Draft the masthead headline + lede that states the thesis in 1 sentence.
5. Outline 10–14 sections in the TOC. Confirm the spine before writing prose.
6. Draft each section in order. After every 2–3 sections, re-read for voice consistency.
7. Write the FAQ last — answers should encapsulate, not introduce, claims. Mirror them into the FAQPage JSON-LD.
8. Update the related-articles section with 3 real existing posts.
9. Verify the `<title>`, OG title, Twitter title, h1, JSON-LD `headline`, and breadcrumb all reference the same canonical title (with minor variations is OK).

## Anti-patterns — never do these

- Don't open with "In today's fast-paced digital world…" or any generic SEO intro.
- Don't use bullet lists where the argument is structural — use prose. Bullets are for *consequences*, *requirements*, or *features*, never for the core thesis.
- Don't write hedging language ("might", "could potentially", "perhaps"). The voice is confident.
- Don't praise AllCoaching with adjectives ("powerful", "amazing", "best-in-class"). Praise it with mechanism — *why* it works, not *that* it's good.
- Don't invent statistics. ₹ ranges and "92% of students" framings are illustrative — use them sparingly and never with a fake citation.
- Don't reference competitors by name in a hostile way (Classplus, Graphy, etc.). Frame critique structurally — "traditional LMS platforms", "isolated personal apps".
- Don't add new CSS classes — every visual need is already covered by the palette above.
- Don't change the navbar, footer, or final CTA block — those are stable across posts.
