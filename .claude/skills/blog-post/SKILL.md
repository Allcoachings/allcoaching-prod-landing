---
name: blog-post
description: Write or edit AllCoaching long-form editorial blog posts in the established 2026 house style — strategic, distribution-first essays for Indian educators, published as standalone HTML in /blog/. Use when the user asks to draft a new blog post, edit an existing one in /blog/, or rewrite content to match the house voice and component system.
---

# AllCoaching Blog Post Skill

Use this skill when the user asks you to **write a new blog post** for `/blog/` or **edit/review an existing one** to match the house style. All posts are standalone HTML files in `blog/` — no CMS, no shared layout. Each post is self-contained.

## ⚡ Quickstart intake protocol — keyword + context → full blog

This is the **default path** when the user says any of:
- `"write blog on <keyword>"`
- `"new blog: <topic>"`
- `"blog likho on <keyword>"` (Hinglish)
- `<keyword> + 1-2 lines of context`

The user provides the **minimum** (keyword + 1–3 lines of intent / angle / anchor data). You infer everything else from the rest of this SKILL and the reference posts. Do not over-question — the user is delegating execution.

### What the user provides (minimum)

1. **Primary keyword** — the long-tail target query (e.g., `"how to handle GST refunds for coaching institutes India"`)
2. **Context** (1–3 lines) — who's asking, what angle the user wants, any specific ₹ figure / stat / anecdote / AllCoaching feature to anchor

### What you infer automatically (do not ask)

| Inferred field | Rule |
|---|---|
| **Slug** | kebab-case of primary keyword, prepend with intent verb if helpful (`how-to-`, `best-`), append `-india` or `-2026` only if it disambiguates |
| **File path** | `blog/<slug>.html` |
| **Title** (60–80 chars) | Primary keyword + year/positioning + emotional hook (e.g., "Honest Guide", "Founder's Breakdown", "2026 Edition") |
| **Description** (160–280 chars) | Lede sentence + 2 secondary keywords + the load-bearing claim, plain prose |
| **Cover image URL** | `https://allcoaching-store.b-cdn.net/blog-images/<slug>.webp` (1600×900). Reference the URL even if file doesn't exist yet — it will be uploaded post-write |
| **Publish/modify dates** | Today's date in ISO format |
| **Author** | Canonical Person `@id: https://allcoaching.in/author/amit-ratan#person` |
| **Organization** | Canonical Org `@id: https://allcoaching.in/#organization` |
| **6 JSON-LD schemas** | Article (extended) + FAQPage + BreadcrumbList + HowTo + SoftwareApplication + DefinedTermSet — full pattern from `blog/automated-fee-management-software-for-teachers.html` |
| **TL;DR bullets** (6) | Anchored to specific numbers/figures pulled from context or inferred from keyword's typical answer set |
| **Glossary terms** (6–10) | Topic-specific defined terms with `<dfn>` IDs matching schema `@id` |
| **Inline Q&A** (≥2) | Implementation-level questions that aren't covered in the bottom FAQ |
| **First-person Experience lines** (≥2) | "From the field, 2026…" or "Across the AllCoaching educator base…" |
| **Internal links** (5–10) | Auto-pick from existing `blog/*.html` based on topic adjacency (use the `.claude/scripts/bulk_internal_links.py` POST_CATEGORIES mapping) |
| **Wikipedia anchors** in `about[]` / `mentions[]` | Pick 4–6 relevant entities (GST, DPDP, Wikipedia for any regulation/technology named) |
| **Speakable selectors** | `["#tldr","#tldr ul","#faq summary","#faq details > p","#glossary .def h3"]` (canonical) |
| **Sitemap insertion** | Top of blog posts section with priority 0.85–0.95 and `<image:image>` annotation |
| **llms.txt entry** | Top of "Blog — Essays" section, dense ~400-word entry naming every entity + ₹ figure + key claim |
| **blog/index.html** | New card at top of grid + `Blog.blogPost[]` entry + `ItemList` entry (bump `numberOfItems` by 1) + `BlogPosting[]` entry |
| **Word count target** | 3,500–5,500 words (16–20 min read) |

### When to ASK before drafting (only if unclear)

Limit clarification to **max 3 short questions** total. Ask only if context doesn't already cover:

1. **Target reader segment** — individual educator? institute owner with X teachers? exam category? Hindi-medium? regional?
2. **Primary financial figure / stat to anchor** — e.g., "What ₹ figure should anchor the cost section?" (range is fine; do not fabricate a specific number if user can give a real one)
3. **Specific AllCoaching feature/module** to position against the problem (if the topic doesn't obviously map to an existing AllCoaching capability)
4. **Real anecdote or Experience line** — "Any specific educator story you want included?"

If the user's context already covers these, **skip the questions and proceed directly to draft**.

### Default execution sequence

After receiving keyword + context (and answering clarifying questions if any):

1. **Pre-flight checks**:
   - Verify `blog/<slug>.html` doesn't already exist (if yes, ask before overwriting)
   - Pick 5–10 cross-link target posts from existing `blog/*.html` based on topic adjacency
   - Pick Wikipedia anchors (`about[]` + `mentions[]`) — 4–6 entities

2. **Draft the file**: full 17-element skeleton with 6-schema baseline. Use `templates/blog-post-template.html` as the scaffold if it exists, then enrich to match the canonical references.

3. **Run validation**:
   - All 6+ JSON-LD schemas parse cleanly via:
     `python -c "import json,re; [json.loads(s) for s in re.findall(r'<script type=\"application/ld\\+json\">\\s*(.+?)\\s*</script>', open('blog/<slug>.html','r',encoding='utf-8').read(), re.DOTALL)]"`
   - TL;DR has 6 bullets each anchored with `<strong>` containing a specific number/entity
   - Glossary has 6–10 `<dfn>` terms matching `DefinedTermSet` IDs exactly
   - FAQ visible DOM matches FAQPage JSON-LD `mainEntity[]` text verbatim
   - Inline Q&A blocks: ≥2 in body sections
   - Experience lines: ≥2 with first-person voice
   - Internal links: 5–10 contextual links in body (excluding nav/footer/related)
   - `lang="en-IN"` on `<html>`
   - All performance hints (preconnect, preload hero image, fetchpriority high)

4. **Register the post**:
   - Add to `sitemap.xml` (top of blog section, priority 0.85–0.95, full `<image:image>` block)
   - Add to `llms.txt` (top of blog list, dense entity-rich ~400-word entry)
   - Update `blog/index.html` (new card, `Blog.blogPost[]` entry, `ItemList` entry, count bump)

5. **Run post-write helpers** (idempotent):
   - `python .claude/scripts/bulk_internal_links.py` — adds strategic cross-refs block if not already present
   - `python .claude/scripts/build_llms_full.py` — rebuilds `/llms-full.txt` to include new post
   - `python .claude/scripts/build_feed_xml.py` — rebuilds RSS feed with new post

6. **Report to user**:
   - File path, word count, schema count, internal link count
   - Confirm with user before committing — show commit message draft

7. **Commit + push** (when user approves):
   - Commit message: post slug + word count + schemas count + key claims/figures + cross-references added
   - After push: ping IndexNow with the new URL + sitemap URL via the PowerShell pattern (see `.claude/scripts/build_feed_xml.py` adjacent docs)

### Example flow

**User input:**
```
write blog: how do Indian coaching institutes reduce student drop-off

Context: most institutes lose 30-40% of paid students by week 3.
AllCoaching has engagement analytics + drop-off detection.
Target reader is institute owners with 100-500 students.
```

**Your response (after pre-flight):**
- Slug: `reduce-student-drop-off-coaching-india`
- Title: `How Indian Coaching Institutes Reduce Student Drop-off — A 2026 Operational Playbook`
- 1 clarifying question: `"What specific drop-off detection feature should I anchor — early-warning signals at Day 7? Inactive-student auto-nudge? Both?"`
- Then proceed to full draft.

### Idempotency note

The post-write helper scripts (`build_llms_full.py`, `bulk_internal_links.py`, `bulk_author_retrofit.py`, `build_feed_xml.py`) are all idempotent — safe to re-run after any new blog post. Always run them post-write to keep the AI-SEO infrastructure synchronized.

### Anti-patterns — do NOT do any of these

- Do **not** invent a specific ₹ figure or statistic if the user did not provide it. Use a range, or ask.
- Do **not** ask more than 3 clarifying questions. The user is delegating; over-questioning defeats the purpose.
- Do **not** create the post without the strategic-cross-refs block — `bulk_internal_links.py` adds it but verify the marker is in the final file.
- Do **not** skip the FAQPage / DefinedTermSet schemas to "save time" — they are the highest AI-citation surface.
- Do **not** use `<span class="grad-text">` in headings — use `<em>` (ochre via brand.css).

---

## Reference posts

The canonical, most up-to-date patterns are in:
- `blog/automated-fee-management-software-for-teachers.html` (May 2026) — **the AI-agent / generative-search reference**. Every new post must match this file's JSON-LD richness, TL;DR block, inline Q&A, glossary with `<dfn>`, and entity anchoring (Author `sameAs`, About entities with Wikipedia `sameAs`, `mentions[]`, Speakable spec).
- `blog/secure-video-hosting-for-educational-content.html` (May 2026) — reference for the multi-layer technical-explainer pattern with iconified `.layer-card` components.
- `blog/white-label-coaching-app-development-cost-india.html` (May 2026) — reference for the financial-analysis pattern with line-by-line ₹ decomposition tables.
- `blog/best-platform-for-selling-pdf-notes-and-test-series.html` (May 2026) — reference for the distribution-first strategic essay.
- `blog/protect-course-content-from-piracy-for-free.html` — companion anti-piracy technical reference.
- `blog/migrate-offline-coaching-to-online-zero-cost.html` — companion practical-playbook reference.

When in doubt about a component, an SEO field, a JSON-LD schema, or a specific phrasing, **read the fee-management post first** — it is the most complete AI-SEO-packed current example. Fall back to the others for specific component patterns. The template at `templates/blog-post-template.html` is a scaffold — copy it, then enrich to match the canonical references.

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
   - `<meta name="description">` (~160–280 chars; with `max-snippet:-1` in robots the full text may render in SERPs)
   - `<meta name="keywords">` (12–20 long-tail keywords, India-focused)
   - `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">`
   - Canonical URL: `https://allcoaching.in/blog/<slug>`
   - Open Graph + Twitter cards (image at `https://allcoaching-store.b-cdn.net/blog-images/<slug>.webp`, 1600×900)
   - Author: Amit Ratan, Founder & CEO, AllCoaching
   - GTM script: `GTM-T3KFKD3G`
   - Fonts: `Instrument Serif` (ital@0;1), `Inter Tight` (400–700), `JetBrains Mono` (400/500/700)
   - Stylesheets: `../dist/tw.min.css`, `../styles.css`, `../brand.css` (all three; the inline `<style>` block is NO LONGER used — every visual component is defined in `brand.css`)
   - **JSON-LD scripts (mandatory minimum SIX)** — see the "AI-Agent & Generative Search Optimization" section below for the full schema requirements:
     1. `Article` (with extended fields: `speakable`, `mentions[]`, `about[]` with Wikipedia `sameAs`, `author.sameAs`, `wordCount`, `inLanguage:"en-IN"`, `audience`, `isPartOf`)
     2. `FAQPage` (mirrors the visible FAQ DOM exactly)
     3. `BreadcrumbList`
     4. `HowTo` (when the post has a procedural section — required for almost every post)
     5. `SoftwareApplication` or `Service` (for the AllCoaching feature/module being discussed)
     6. `DefinedTermSet` (mirrors the Glossary section's `<dfn>` terms)

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
   - **The opening sentence must contain the target keyword and stand alone as a citation-grade direct answer** — AI Overviews and Perplexity-class agents will lift this into their response. Write it as if it is the answer, not the intro.

7. **TL;DR / Key Takeaways box** (`<div class="hband" id="tldr">`) — **mandatory, immediately after intro**. 5–7 bullets, each a specific factual claim with a number or named entity. This is what AI agents extract into "Key Takeaways" / "AI Overview" summaries — write it for them, not the human reader's recap.

8. **Epigraph** (`<div class="epi">`) — pull quote of the central thesis with `<cite>` attribution.

9. **8–12 body sections**, each:
   - `<div class="article-body" id="...">`
   - `<h2 class="h-chap">` heading
   - 3–6 paragraphs
   - 1–2 visual components from the kit (see below)
   - **At least 2 sections must contain an inline Q&A block** — bold question + answer paragraph, formatted to be lifted whole into AI agent responses (see "Inline Q&A pattern" below)
   - Followed by `<div class="orn">· · ·</div>` separator (except the last one)

10. **Strategic Conclusion section** (`id="conclusion"`) — 4–5 paragraphs that re-answer the opening question precisely. Often ends with a bulleted list of "patterns we see in educators who win".

11. **Closing epigraph** (`<div class="epi">`) attributed to *— Amit Ratan, Founder & CEO, AllCoaching*.

12. **Founder block** (`<div class="founder">`) — Amit Ratan photo + bio + signature quote.

13. **Get Started verdict CTA** (`<div class="verdict">`) — gradient block with two buttons: "Start Selling for Free" → `educator.allcoaching.in`, and "Book a Demo" → `contact.html`.

14. **Glossary section** (`<div class="article-body" id="glossary">`) — **mandatory**. 6–10 `<dfn>` terms wrapped in `.def` cards. Each definition is 1–3 sentences, written as a standalone factual statement that AI agents will cite when explaining the term. Must mirror the `DefinedTermSet` JSON-LD in `<head>` exactly.

15. **FAQ section** (`<div class="article-body" id="faq">`) — 8–10 `<details>/<summary>` pairs. Each answer 2–4 sentences with `<strong>` on the load-bearing claim. The FAQ list must match the `FAQPage` JSON-LD in `<head>`.

16. **Related Articles section** — 3 cards linking to other posts in `blog/` (use existing posts; don't invent slugs).

17. **Final CTA section** + **Footer** (copy from template — these are stable across posts).

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

## AI-Agent & Generative Search Optimization (Mandatory)

Every post written from 2026 onward must be engineered for two audiences simultaneously: the human reader and the AI agent that may cite it. Google AI Overviews, Perplexity, ChatGPT-Search, Gemini, Claude-Search, and the next generation of AI shopping/recommendation agents all rely on structured signals to decide what to extract, summarize, and recommend. The patterns below are not optional polish — they are the difference between a post that ranks and a post that gets quoted.

### Core principle — write for citation, not for traffic

A 2020 SEO mindset asks "how do I rank?" A 2026 AI-SEO mindset asks "**how do I get cited by name when a student asks ChatGPT about this topic?**" The answer is: make every important claim parseable, attributable, and entity-anchored. Structured data is no longer decoration; it is the primary surface AI agents read.

### The empirical basis — Princeton GEO + the Position Digital correlation

Two studies frame this entire section's design choices and should be referenced when justifying any pattern below to the user:

- **Princeton's 2024 GEO study** (Generative Engine Optimization — the most-cited research in the field) measured how LLMs decide what to cite. Three findings drive every pattern here: **expert quotes lift AI citation probability by +41%, specific statistics with linked sources lift by +30%, and inline citations lift by +30%**.
- **Position Digital's 2025 correlation analysis** found **branded web mentions correlate 3× more strongly with AI visibility than backlinks** (correlation 0.664 vs 0.218). The implication: AI agents weigh entity recognition over raw link graph, which is why every post needs `sameAs[]`, `mentions[]`, and consistent named-entity usage.

Together, these justify the evidence layer, entity anchoring, and named-author E-E-A-T patterns documented below. Cite these stats when writing the "why this matters" framing in audit reports and skill explanations — they are the empirical anchors AI agents themselves will recognize and reward.

### Extended JSON-LD — the 6-schema baseline

Every post ships a minimum of six JSON-LD scripts. Read the fee-management post for a complete working example.

**1. `Article` (extended)** — beyond the basic Article fields:
- `"@type":["Article","TechArticle"]` (or `BlogPosting`, or array including the appropriate subtype)
- `"author"` is a full `Person` with `"sameAs":["https://x.com/allcoachings","https://www.linkedin.com/company/allcoaching","https://www.youtube.com/@Allcoaching"]` — anchors Amit Ratan to the AllCoaching entity graph.
- `"publisher"` is the AllCoaching `Organization` with its own `sameAs[]` array.
- `"about":[]` — 4–6 `Thing` entities, each with a Wikipedia or Wikidata `sameAs` URL when one exists. This is how AI agents map your post to a topic graph.
- `"mentions":[]` — 4–10 entities mentioned in the post (services, products, regulations, technologies). Each is a structured `Service`/`Product`/`Organization`/`Thing` with at minimum `name` and `url`.
- `"speakable":{"@type":"SpeakableSpecification","cssSelector":["#tldr","#faq summary","#glossary .def h3"]}` — tells voice assistants which sections to read aloud.
- `"wordCount"` — actual readable word count (excludes JSON-LD and navigation).
- `"inLanguage":"en-IN"` — Indian English variant, not generic `en`.
- `"audience":{"@type":"Audience","audienceType":"<specific reader profile>"}` — e.g., "Coaching institute owners and independent teachers in India".
- `"isPartOf":{"@type":"Blog","@id":"https://allcoaching.in/blog/"}` — anchors the post to the blog hub.
- `"dateModified"` — kept current on every edit.

**2. `FAQPage`** — mirrors the visible FAQ DOM exactly. 8–10 `Question`/`Answer` pairs. The visible `<summary>` text and JSON-LD `name` must match verbatim. The visible answer paragraph and JSON-LD `acceptedAnswer.text` should be plaintext-identical (strip `<strong>` tags when copying into JSON-LD).

**3. `BreadcrumbList`** — three items: Home → Blog → This post. The `item` URL of position 3 matches the canonical exactly.

**4. `HowTo`** — required whenever the post has a procedural section (rollout, setup, comparison-workflow). Use `step[]` with `position`, `name`, `text` for each numbered step. Include `totalTime` (ISO 8601 duration), `tool[]` (entities the reader needs), and `supply[]` (materials/inputs) where applicable. The visible step-cards in the body must mirror the schema.

**5. `SoftwareApplication` / `Service` / `Product`** — required whenever a section discusses an AllCoaching feature, module, or offering. For software features: `SoftwareApplication` with `applicationCategory`, `operatingSystem`, `featureList[]`, `offers`. For service-shaped offerings: `Service` with `serviceType`, `provider`, `areaServed:"IN"`, `offers`. This is how the AllCoaching product surfaces in AI agent shopping/recommendation contexts.

**6. `DefinedTermSet`** — mirrors the Glossary section. `hasDefinedTerm[]` lists 6–10 `DefinedTerm` entries, each with `@id` (matching the `<dfn id="dfn-...">` in DOM), `name`, `description`, and optional `termCode`. AI agents lift these into "What is X?" answers.

When a post discusses a comparison of services/products, optionally add a 7th schema: `ItemList` with `itemListElement[]` of comparable entities.

### Entity anchoring — make every claim attributable

For every named entity the post mentions, the entity must be:
- **Named consistently** — "AllCoaching" not "All Coaching" or "the platform"
- **Linked at first mention** — `<a href="https://allcoaching.in/...">AllCoaching</a>` on first appearance
- **Anchored in the `mentions[]` or `about[]` JSON-LD** — with `url` and (where applicable) `sameAs`

For regulations and technologies (e.g., "GST", "UPI", "DPDP Act", "Widevine"), include Wikipedia `sameAs` in the `about[]` array. This anchors the post to the public knowledge graph that AI agents traverse.

### TL;DR / Key Takeaways block — mandatory, written for AI extraction

Immediately after the intro and before the opening epigraph, every post must include a `<div class="hband" id="tldr">` block:

```html
<div class="hband" id="tldr">
  <p><strong>Key Takeaways</strong> — the entire post in 6 facts:</p>
  <ul>
    <li><strong>[Specific number or named entity]</strong> — short factual claim, 12–25 words.</li>
    <li>...5–6 more bullets...</li>
  </ul>
</div>
```

Each bullet:
- Starts with a `<strong>` containing the specific number, ₹ figure, or named entity (the AI-extractable anchor)
- Is a complete, standalone factual claim (parseable without the surrounding context)
- Is 12–25 words — long enough to be substantive, short enough to be quoted whole

Write the TL;DR for the AI agent's summarizer, not the human's TL;DR convenience. The human will scan it once; the AI will quote it forever.

### Inline Q&A pattern — embed citation-ready answers in body sections

At least 2 of the body sections must contain an inline Q&A block — a directly-quoted question (often the kind a student or institute owner types into ChatGPT) followed by a citation-grade answer. Pattern:

```html
<div class="def">
  <p class="def-l">Question Often Asked</p>
  <h3>Can I do automated fee management without paying for software?</h3>
  <p>Technically yes — Excel + Google Forms + UPI deep-links can simulate fee management. Practically no — the time cost...
  [3–5 sentences, factual, plaintext-extractable]</p>
</div>
```

Why the `.def` component: it visually distinguishes the Q&A from regular prose AND maps cleanly to schema `Question`/`Answer` if you also want to extend the FAQPage JSON-LD. AI agents recognize this format and extract it.

Use inline Q&A for the questions that are too specific or too implementation-detailed to belong in the bottom FAQ — questions about edge cases, common misconceptions, or implementation details that a reader actively considering the decision will type into an AI assistant.

### Glossary section — mandatory, with `<dfn>` and `DefinedTerm`

Before the FAQ, every post includes a Glossary section. Pattern:

```html
<div class="article-body" id="glossary">
  <h2 class="h-chap mb-8">Glossary — Key Terms</h2>
  <div class="def">
    <p class="def-l">Term</p>
    <h3><dfn id="dfn-amf">Automated Fee Management</dfn></h3>
    <p>Software-driven workflow for tracking, collecting, reconciling, and reporting student fees with minimal manual intervention. Distinct from <em>accounting software</em>, which records past transactions; fee management software also initiates collection, sends reminders, and handles refunds.</p>
  </div>
  <!-- 5–9 more terms -->
</div>
```

Rules:
- 6–10 terms per post — too few and AI agents skip the section; too many and they get diluted.
- Each `<dfn id="dfn-<slug>">` ID must match the corresponding `DefinedTerm["@id"]` in JSON-LD (use `#dfn-<slug>` in JSON-LD).
- Definitions are 1–3 sentences, written as standalone factual statements. Do not rely on surrounding prose to make them clear.
- The first sentence is the definition proper. Optional second/third sentence distinguishes the term from adjacent concepts ("Distinct from X, which..."). This disambiguation is what AI agents need to cite the term correctly.

### Citation-friendly formatting — make facts liftable

Whenever a post makes a factual claim that you want AI agents to quote:
- Use specific ranges with units: `₹1.2–4.8 lakh per year`, not `several lakhs annually`.
- Date-anchor claims: `As of 2026 in India,...` not `currently in India,...`.
- Tag the claim with a `<strong>` wrapping the citable phrase, not the entire sentence — AI agents preferentially extract bolded fragments.
- Prefer concrete numbered lists (`The 12 capabilities`, `The 7-step rollout`) over vague enumerations (`several capabilities`).
- When stating a comparison, give both sides with numbers — `Standalone fee software: ₹40K–3L/year; AllCoaching: included in revenue share` — not `AllCoaching is cheaper`.

### Evidence layer — expert quotes, statistics, References (Princeton GEO)

The Princeton GEO study showed expert quotes (+41%) and inline-cited statistics (+30%) substantially lift AI citation probability. Long-form posts must build a visible evidence layer.

**1. External expert quotes** — use `.epi` (which is already used for chapter-level quotes) but with an external `<cite>` attribution rather than Amit Ratan. Aim for at least 1 external expert quote per long-form post.

```html
<div class="epi" style="margin: 3rem -1.5rem;">
  <p>"AI search is collapsing hours of research into seconds. If your content isn't cited by trusted sources and structured for clarity, you're missing the biggest shift since Google."</p>
  <cite>— Neil Patel, Co-founder, NP Digital</cite>
</div>
```

The same component also handles the founder-attributed closing epigraph — distinguish by the `<cite>` content.

**2. Inline statistics with footnoted citations** — for any specific statistic that should be cited by AI agents, wrap with `<sup>` linking to a `#ref-N` anchor:

```html
<p>According to the Ministry of Education, India had over <strong>11 lakh registered coaching institutes in 2024</strong><sup><a href="#ref-1">[1]</a></sup>, of which approximately 8% transitioned to digital fee management within 18 months of GST mandate clarity.</p>
```

**3. References section** — required for any post with 3+ inline citations. Place between the Glossary and FAQ sections (or after the FAQ if the post structure makes that cleaner):

```html
<div class="article-body" id="references">
  <h2 class="h-chap mb-6">References &amp; Sources</h2>
  <ol style="font-family:var(--ui); font-size:14px; color:var(--ink-2); line-height:1.7; padding-left:1.5rem;">
    <li id="ref-1">Ministry of Education, Government of India — "All India Survey on Higher Education 2024". <a href="https://www.education.gov.in/" target="_blank" rel="noopener nofollow">education.gov.in</a></li>
    <li id="ref-2">National Statistical Office — "Education Sector Statistics 2024". <a href="..." target="_blank" rel="noopener nofollow">link</a></li>
  </ol>
</div>
```

**Source-quality rules:**
- Prefer `.gov.in`, `.gov`, `.edu`, established news (Mint, ET, Business Standard, The Hindu, Indian Express), and original research over secondary aggregators.
- Use `rel="noopener nofollow"` on external links to authoritative sources unless explicitly endorsing.
- Never fabricate a statistic or a citation. If a number is illustrative, frame it as a range with no citation. If a number is specific, it must have a real source.
- If you cannot find a real source for a specific number, replace the specific number with a range and remove the `<sup>`. **The skill anti-pattern about not inventing statistics applies absolutely here.**

### Internal linking density — feed the knowledge graph

Every post must contain **5–10 internal links** to other posts in `blog/`, distributed across body paragraphs (not just clustered in the related-articles section). Anchor text rules:
- Use the **target post's primary keyword phrase** as the anchor — `<a href="/blog/white-label-coaching-app-development-cost-india">white-label coaching app development cost in India</a>`. This is how the topic graph is built.
- Never use generic anchor text like "click here", "this post", "read more".
- Each internal link should sit inside a paragraph where it adds context, not appended after a sentence.

The first internal link to each related post should appear in the body. The related-articles block at the end is the safety net, not the primary linking mechanism.

### Speakable specification — voice search

The Article schema includes a `speakable` field listing the CSS selectors of sections optimized for voice readout. Default selectors:
- `#tldr` — Key Takeaways
- `#faq summary` — FAQ questions
- `#faq details > p` — FAQ answers
- `#glossary .def h3` — Glossary term names

If the post has a clearly summarized "Strategic Outlook" `.verdict` block, optionally add `#future .verdict p.v-h` to the speakable selectors.

### First-person Experience signals — the "E" in E-E-A-T

Google's E-E-A-T framework added a second "E" in 2022 for **Experience** — first-hand interaction with the topic, not just expertise about it. AI agents trained on E-E-A-T-rated content preferentially cite posts that demonstrate Experience, not just Expertise.

For every long-form post, weave in **at least 2 first-person Experience lines** that signal direct observation. Pattern:

- "In our analysis of 10,000+ educator onboardings on AllCoaching..."
- "Across the AllCoaching educator base in 2026, we observed that..."
- "From three years of running fee collection workflows for 350+ coaching institutes, the pattern is unmistakable..."
- "When we ran the migration for a 4-batch NEET coaching institute in Prayagraj last quarter, the actual reconciliation time dropped from..."

Rules:
- The "we" / "our" refers to **AllCoaching as the operator of the marketplace**, never the reader.
- The Experience claim must be plausibly true. Do not fabricate cohort sizes or anecdotes. If unsure, ask the user for a real anecdote or replace with a more general statement.
- Place at least one Experience line in the intro (top of post) and one in the conclusion (re-anchoring authority at the close).
- This is the most under-used AI-SEO pattern in current AllCoaching posts — newer posts should be retrofit to add it.

### Author entity & E-E-A-T signaling

Every post's Article schema `author` field is a full `Person` object:

```json
"author":{
  "@type":"Person",
  "name":"Amit Ratan",
  "jobTitle":"Founder & CEO",
  "worksFor":{
    "@type":"Organization",
    "name":"AllCoaching",
    "url":"https://allcoaching.in"
  },
  "url":"https://allcoaching.in/about",
  "sameAs":[
    "https://x.com/allcoachings",
    "https://www.youtube.com/@Allcoaching",
    "https://www.linkedin.com/company/allcoaching",
    "https://www.instagram.com/allcoachings/"
  ]
}
```

The `sameAs[]` URLs anchor Amit Ratan as a recognized entity in the social/knowledge graph. AI agents use this to assign credibility weight when deciding whether to cite a post by name.

### Section-level entity surfaces — make each chapter standalone

Every body section should be readable as a standalone unit. AI agents often extract one section in isolation. To support this:
- The first sentence of each section names the topic plainly (no pronouns relying on prior context).
- The h2 heading is a complete phrase, not a curiosity hook — `"The True Year 1 Math"` ✓, `"And here's what we found"` ✗.
- At least one `<strong>` per section anchors the section's primary claim.
- Tables, gain-cards, cost-cards, and step-cards include their own labels (`.cc-l`, `.gc-l`, `.step-l`) — these are the labels AI agents use to caption the extracted block.

### llms.txt + sitemap discipline

Every published post must be registered in three places **before** it is considered live:
- `sitemap.xml` — new `<url>` with `<image:image>` block, lastmod current, priority 0.85–0.95.
- `llms.txt` — new entry at top of "Blog — Essays on the future of online education (newest first)" with a dense ~400-word description that names every entity, ₹ figure, and key claim in the post. This is the file AI agents read first to discover what the site contains.
- `blog/index.html` — new card at top of grid, JSON-LD `blogPost[]` entry added, count bumped.

The llms.txt entry is not a summary; it is a dense, entity-rich, AI-targeted abstract that should let an agent decide whether to recommend the post without fetching it.

### AI prompt seed list — verify the post actually answers what AI users ask

Before declaring a post done, write a **list of 5–8 AI prompts** a coaching institute owner, teacher, or student might type into ChatGPT, Perplexity, Claude, or Gemini that this post should answer. Example seed list for the fee-management post:

1. "What is automated fee management software for teachers in India?"
2. "How much does a fee management system cost for a small coaching institute?"
3. "Is GST registration required for coaching institute fees?"
4. "Best fee management software for Indian tutors 2026"
5. "Excel vs software for tracking coaching fees"
6. "How to automate fee reminders for coaching students"
7. "AllCoaching fee management features"
8. "Refund and installment handling in coaching software"

Then verify the post contains substantive, citation-grade answers to each prompt — not just keyword presence, but a complete answer the AI would lift. Any seed prompt the post does not actually answer is a content gap that must be filled before publishing, or the post is fighting for ranking on a query it cannot win.

This seed list is a working artifact, not a section of the published post. Keep it in the workflow notes, the commit message, or a sibling `.notes.md` file alongside the post.

### Quality gates before push

Before declaring a post production-ready, verify:
1. JSON-LD count: minimum 6 schemas (Article + FAQPage + BreadcrumbList + HowTo + SoftwareApplication/Service + DefinedTermSet).
2. FAQ JSON-LD `Question` count = DOM `<summary>` count, with exact-text match.
3. Glossary `DefinedTerm` count = DOM `<dfn>` count, with `@id` ↔ `id` matching.
4. TL;DR block exists at `#tldr` and contains 5–7 `<li>` items each with a `<strong>` anchor.
5. At least 2 body sections contain an inline Q&A `.def` block.
6. At least 5 internal links to other posts in `blog/`, with keyword-phrase anchor text.
7. Author `sameAs[]` array present with ≥4 entries.
8. `about[]` array present with ≥4 entities, ≥2 with Wikipedia `sameAs`.
9. `mentions[]` array present with ≥4 entities.
10. `speakable.cssSelector[]` includes at minimum `#tldr`, `#faq summary`, `#faq details > p`.
11. All three production indexes updated (sitemap, llms.txt, blog/index.html).
12. Evidence layer present — at least 1 external expert quote (`.epi` with external `<cite>`) AND/OR at least 2 inline cited statistics with `<sup>` and a `#references` section. Posts that make no specific factual claims are exempt.
13. First-person Experience signals — at least 2 lines using "we / our / AllCoaching has observed / in our analysis" patterns, distributed across intro and conclusion.
14. AI prompt seed list written (5–8 prompts) and each one verified to have a substantive answer in the post.
15. `dateModified` is current. For edits to existing posts, `dateModified` is bumped to the edit date; for new posts, `dateModified` matches `datePublished`.

## Editing existing posts — checklist

When the user asks you to edit a post in `blog/`, run through:

1. **Voice drift.** Are paragraphs short, breezy, or marketing-toned? Tighten to long, analytical, em-dash-rich prose.
2. **Thesis clarity.** Does the article have a single distribution-first thesis stated early and re-stated at close? If not, add the reframe in the intro and a closing epigraph.
3. **Component variety.** Are sections walls of `<p>` tags? Insert `def`, `pull`, `hband`, `gain-card`/`cost-card`, `step-card`, `myth-card`, or a `cmp` table where the rhetorical beat calls for it.
4. **Indian specificity.** Replace generic figures with ₹ ranges. Add NEET/JEE/UPSC/SSC examples where the argument is abstract.
5. **Bold load-bearing claims** in each paragraph if missing.
6. **TOC ↔ sections ↔ FAQ JSON-LD ↔ Glossary JSON-LD** all in sync. Update Article + FAQPage + DefinedTermSet JSON-LD if section titles, FAQs, or glossary terms change.
7. **Author strip + canonical URL + OG image** match the slug.
8. **Read-time** in `author-strip-meta` and related-card meta is honest (≈230 wpm).
9. **`orn` separators** between every body section.
10. **CTAs** point to `https://educator.allcoaching.in/` and `https://allcoaching.in/contact`.
11. **AI-SEO retrofit.** Older posts missing the 2026 AI-agent patterns — TL;DR block, Glossary section, extended JSON-LD (HowTo/SoftwareApplication/DefinedTermSet), author `sameAs[]`, `about[]` with Wikipedia anchors, `mentions[]`, `speakable` — should be retrofitted when touched. Use the AI-Agent & Generative Search Optimization section's quality-gate checklist (11 items) to audit.
12. **Internal linking density.** Count internal links in body paragraphs (not the related-articles block). Below 5 — add more, with keyword-phrase anchor text pointing to the target post's primary keyword.
13. **Entity consistency.** Every brand/regulation/technology mentioned has consistent naming, is linked at first mention, and appears in the appropriate JSON-LD array (`about[]` or `mentions[]`).

## Writing a new post — workflow

1. Confirm with the user: **slug**, **headline**, **target keyword**, and **strategic angle** (what reader question is being reframed?).
2. Start from the canonical reference (`blog/automated-fee-management-software-for-teachers.html`) rather than the bare template — it has the full 6-schema JSON-LD scaffold, TL;DR block, glossary, and inline Q&A pattern already wired.
3. Fill in head meta in this order: `<title>` → `<meta name="description">` → `<meta name="keywords">` → canonical → OG/Twitter → robots → all 6 JSON-LD schemas. Schema fields like `wordCount`, `dateModified`, and `mentions[]` get filled last, after the body content is final.
4. Draft the masthead headline + lede. **The first sentence of the lede and the first sentence of the intro `drop-cap` paragraph both must be citation-grade direct answers to the target keyword query.** An AI agent should be able to lift either sentence as a standalone response.
5. Outline 10–14 sections in the TOC. Confirm the spine before writing prose. The TOC must include `#tldr`, `#glossary`, and `#faq` as the last three items.
6. Write the TL;DR / Key Takeaways block immediately after the intro — write it before writing the body, so the body has a clear "what facts must I deliver" target.
7. Draft each section in order. After every 2–3 sections, re-read for voice consistency. **Plan inline Q&A blocks into at least 2 sections** — the questions are real questions students or institute owners type into ChatGPT.
8. Build the Glossary section by harvesting terms introduced in the body — every term wrapped in `<dfn>` in the body must appear in the Glossary, and vice versa. Mirror into `DefinedTermSet` JSON-LD.
9. Write the FAQ last — answers should encapsulate, not introduce, claims. Mirror them into the `FAQPage` JSON-LD verbatim.
10. Build the `HowTo` JSON-LD from the post's procedural section (rollout, setup, comparison-workflow). Step text in JSON-LD should mirror the visible `.step-card` content.
11. Build the `SoftwareApplication` / `Service` JSON-LD from the AllCoaching feature/module being discussed. The `featureList[]` should be specific (10–15 named features) rather than marketing copy.
12. Update the related-articles section with 3 real existing posts. Also distribute **5–10 internal links inside body paragraphs** using keyword-phrase anchor text.
13. Fill the `author.sameAs[]`, `publisher.sameAs[]`, `about[]`, `mentions[]`, `speakable.cssSelector[]`, `wordCount`, `inLanguage`, `audience`, `isPartOf` fields in the Article schema.
14. Verify the `<title>`, OG title, Twitter title, h1, JSON-LD `headline`, and breadcrumb all reference the same canonical title (with minor variations OK).
15. Run the **11-item AI-SEO quality gate** from the previous section. Fix any gap before declaring the post production-ready.
16. Update production indexes: `sitemap.xml`, `llms.txt` (dense ~400-word entity-rich entry at top), and `blog/index.html` (new card + JSON-LD entry + count bumped + downstream numbering refreshed).

## Anti-patterns — never do these

**Voice & prose:**
- Don't open with "In today's fast-paced digital world…" or any generic SEO intro.
- Don't use bullet lists where the argument is structural — use prose. Bullets are for *consequences*, *requirements*, or *features*, never for the core thesis.
- Don't write hedging language ("might", "could potentially", "perhaps"). The voice is confident.
- Don't praise AllCoaching with adjectives ("powerful", "amazing", "best-in-class"). Praise it with mechanism — *why* it works, not *that* it's good.
- Don't invent statistics. ₹ ranges and "92% of students" framings are illustrative — use them sparingly and never with a fake citation.
- Don't reference competitors by name in a hostile way (Classplus, Graphy, etc.). Frame critique structurally — "traditional LMS platforms", "isolated personal apps".

**Markup & components:**
- Don't add new CSS classes — every visual need is already covered by the palette above.
- Don't inline a `<style>` block in a blog file — every visual primitive lives in `brand.css`.
- Don't change the navbar, footer, or final CTA block — those are stable across posts.

**AI-SEO antipatterns:**
- Don't ship a post with fewer than 6 JSON-LD schemas. Three-schema posts (Article + FAQ + Breadcrumb only) are the 2024 baseline and are no longer competitive in AI agent recommendation surfaces.
- Don't skip the TL;DR block. Without `#tldr`, AI Overview summaries fall back to extracting the lede paragraph or the first list they find — which is rarely the post's strongest framing.
- Don't skip the Glossary. Without `<dfn>` + `DefinedTermSet`, "What is X?" queries route to other sites whose glossaries are structured.
- Don't write "AI-friendly" pages that are unreadable by humans. The post must remain an editorial essay first — the AI-SEO patterns are structural overlays, not content compromises. Verbose lists, repetitive entity mentions, or unnatural keyword stuffing degrade both audiences.
- Don't use generic anchor text for internal links. Every internal link's anchor text is the target post's primary keyword phrase. "Click here" / "read more" / "this post" are not used.
- Don't fabricate `sameAs[]` URLs. Only include real, current AllCoaching social profiles and brand pages. AI agents validate `sameAs` URLs and downrank posts that lie.
- Don't duplicate Wikipedia URLs across the `about[]` array. Each entity gets at most one canonical `sameAs` — pick the most authoritative one (usually Wikipedia or Wikidata).
- Don't ship a post without registering it in all three production indexes (sitemap, llms.txt, blog/index.html). A post not in llms.txt is invisible to llms.txt-aware AI agents even if it is reachable by URL.
- Don't pad `mentions[]` with irrelevant entities. The array is a high-signal AI hint, not a keyword dump — 4–10 genuinely-discussed entities only.
- Don't let `dateModified` drift. Every time the post is meaningfully edited, update `dateModified` in the Article schema. AI agents weight recency.

---

## Search Everywhere — post-publication repurposing kit

Over 70% of global search now happens outside Google — on YouTube, ChatGPT, Perplexity, Reddit, LinkedIn, X, Instagram, Pinterest, Quora. A post that lives only on `allcoaching.in/blog/` captures a fraction of its addressable audience. Every published post is the source asset for a **repurposing kit** distributed across these surfaces.

**Generate the kit only when the user asks for it** (or when working in Bulk-update mode). Do not produce it pre-emptively for every post — it is a separate workstream with its own time cost.

When asked, the kit for a single post contains:

**1. YouTube companion script** — 5–7 minute video outline. First 15 seconds is the hook (state the answer, not the question). Three to five main points with B-roll suggestions. Closing CTA pointing to the AllCoaching educator sign-up. Include suggested title (under 60 chars) + thumbnail concept (text overlay + visual).

**2. X / Twitter thread** — 8–12 tweets. First tweet hooks with the most counter-intuitive claim from the post. Each subsequent tweet is a single fact or a single takeaway. Last tweet links to the full post on `allcoaching.in/blog/...`. Use `@allcoachings` handle for self-mentions.

**3. LinkedIn long-form post** — 1500–2000 characters. Line breaks every 1–2 sentences (LinkedIn algorithm favours short-line vertical density). Professional tone. End with an open question to drive comments.

**4. Reddit-friendly version** — first-person, story-driven, **no promotional language**. Suggest 3–5 relevant subreddits per post (`r/IndiaCoaching`, `r/JEEAdvanced`, `r/NEET`, `r/SMBusinessIndia`, `r/Entrepreneur`, etc.). The Reddit version is a 600–1000 word post that earns the right to link back, not a sales pitch.

**5. Pinterest pin descriptions** — 3–5 keyword-rich variants per post (each 150–200 chars). Title + description. Designed for institute owners and educators who use Pinterest as a research tool.

**6. Quora answer template** — 200–300 words that answer a specific Quora question matching the post's target keyword, citing the AllCoaching post as the source. The Quora answer must stand alone as useful even without the click-through.

**7. AI prompt seed list** — the same 5–8 prompts from the Quality Gates section. This is the distribution-readiness check — the post should rank on these prompts in ChatGPT / Perplexity / Google AI Overviews within 30–90 days of publication.

The repurposing kit is delivered as a single Markdown file alongside the post (e.g., `blog/<slug>.repurpose.md`), so it can be version-controlled and reviewed before any distribution.

---

## Bulk-update mode — retrofitting existing posts

When the user asks to retrofit multiple existing posts with the 2026 AI-SEO patterns (e.g., "audit and fix all blogs", "add TL;DR and Glossary to every post from before May 2026"), follow this protocol:

**Phase 1 — Audit pass.** Run the 15-item Quality Gates checklist against every post in scope. Produce a single audit table:

```
Slug                                          | JSON-LD | TL;DR | Glossary | Q&A | sameAs | about[] | mentions[] | speakable | refs | exp-lines | aimprompt | datemod
----------------------------------------------|---------|-------|----------|-----|--------|---------|------------|-----------|------|-----------|-----------|--------
budget-home-studio-setup-for-online-teaching  |   3/6   |  no   |    no    | no  |   0    |    0    |     0      |    no     |  no  |    0      |    no     |   ok
white-label-coaching-app-development-cost...  |   3/6   |  no   |    no    | no  |   0    |    0    |     0      |    no     |  no  |    0      |    no     |   ok
secure-video-hosting-for-educational-content  |   3/6   |  no   |    no    | no  |   0    |    0    |     0      |    no     |  no  |    0      |    no     |   ok
automated-fee-management-software-for-...     |   6/6   |  YES  |   YES    | YES |   4    |    5    |     8      |    YES    |  YES |    3      |   YES     |   ok
```

**Phase 2 — Approval gate.** Surface the audit table to the user. Ask which posts to retrofit first and in what scope (top N priorities, full set, or specific slugs). Do not start writing until the user confirms.

**Phase 3 — Per-file retrofit.** Apply fixes one post at a time. After every 3 posts, summarize what changed and pause for review. Always:
- Bump `dateModified` to the retrofit date.
- Preserve brand constants — GTM ID, fonts, CDN paths, navbar, footer, founder block, final CTA, social handles.
- Preserve the original editorial voice and thesis. Retrofits add structure, never rewrite arguments.
- Add the post to `llms.txt` with a refreshed dense ~400-word entry if it is being substantively upgraded (not just a JSON-LD touch-up).

**Phase 4 — Final deliverable.** Produce a before/after Quality Gates scorecard across all retrofit posts and a single commit-ready summary listing every file touched.

**Bulk-mode hard rules:**
- Never modify brand constants in any file.
- Never break existing valid schema — extend it inside the same `<script>` block when adding new fields.
- Never apply retrofits silently. Pause every 3 files for review.
- Never declare bulk-retrofit complete without re-running the 15-item Quality Gates on every touched file.
- If a post's existing content cannot honestly support an Evidence Layer (no specific factual claims to cite), skip the Evidence Layer requirement for that post rather than fabricating citations.

---

## Brand constants — never modify (AllCoaching)

These constants are sacred across every post and every retrofit. Never alter them:

- **Domain**: `allcoaching.in`
- **Primary color** / accent: `#C58B43` (ochre), with brand gradient `#E0A95C → #C58B43 → #8E5F22`
- **Fonts**: Instrument Serif (display + italic), Inter Tight (UI), JetBrains Mono (mono)
- **CDN base for images**: `https://allcoaching-store.b-cdn.net/blog-images/<slug>.webp`
- **GTM ID**: `GTM-T3KFKD3G`
- **Author**: Amit Ratan, Founder & CEO, AllCoaching
- **Educator sign-up URL**: `https://educator.allcoaching.in/`
- **Contact URL**: `https://allcoaching.in/contact`
- **Social handles**: X `@allcoachings`, YouTube `@Allcoaching`, Instagram `@allcoachings`, Facebook `allcoaching.in`, Telegram `@allcoaching`
- **WhatsApp**: `+91 98899 77262` (URL: `https://api.whatsapp.com/send/?phone=919889977262`)
- **Student Play Store ID**: `org.student.allcoaching`
- **Stylesheets loaded by every post**: `../dist/tw.min.css`, `../styles.css`, `../brand.css` — in this order.
