---
name: ai-search-geo
description: The current (mid-2026) playbook for making AllCoaching content get CITED and RECOMMENDED across AI Overviews, Google AI Mode, ChatGPT-Search, Perplexity, Gemini, and Claude — i.e. Generative Engine Optimization (GEO) / Answer Engine Optimization (AEO). Use when the user wants a blog post (or any page) optimized to "show up in AI recommendations", audited for AI-citability, or when justifying AI-search content decisions. This skill encodes official Google guidance + the latest 2026 core-update reality; the blog-post skill handles the actual HTML house style and component system.
---

# AI Search & GEO Optimization Skill (mid-2026)

This skill makes AllCoaching content **get quoted by name** when a student, teacher, or institute owner asks an AI engine a question. It is the *strategy + rules* layer. The [`blog-post`](../blog-post/SKILL.md) skill is the *execution* layer (house voice, HTML components, the 6-schema scaffold, sitemap/llms.txt registration). When writing a post, use both: this skill decides **what makes it citable**, `blog-post` decides **how it's built**.

> **One-line thesis:** In 2026, "ranking" is no longer the goal — **being the source an AI engine lifts into its answer** is. Google's own ranking systems still decide which pages feed AI Overviews and AI Mode, so there is no separate "AI SEO" — there is excellent, people-first, entity-anchored, citation-shaped SEO. This skill is how we shape it.

---

## 1. The 2026 reality — what actually changed (dated, sourced)

Use these facts to frame decisions and to write the "why this matters" rationale in audits. Distinguish **official Google statements** from **observed/third-party data** — never present a third-party stat as Google's word.

### Official Google changes (developers.google.com/search) — verify before citing
- **AI features are standard Search, not a separate channel.** Google: *"The best practices for SEO remain relevant for AI features in Google Search (such as AI Overviews and AI Mode)… There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."* → There is **no secret schema, no special AI file, no markup** that "gets you into" AI Overviews. Eligibility = indexed + eligible for a snippet + meets technical requirements.
- **15 May 2026 — new generative-AI guidance.** Google expanded the *AI features and your website* doc with guidance on **non-commodity (unique, hard-to-find) content**, local/shopping/image/video optimization, and guidance for AI agents — and restated that **SEO best practices remain relevant**.
- **27 May 2026 — Preferred sources expanded to AI Overviews and AI Mode** (previously Top Stories only). Users can mark preferred publishers; brand familiarity now feeds AI surfaces directly.
- **7 May 2026 — FAQ rich results DEPRECATED.** The FAQ rich result *no longer renders in Google Search.* **Implication for us:** keep `FAQPage` JSON-LD and the visible FAQ — they remain a top AI-extraction surface (AI Overviews/LLMs still parse Q&A) — but **do not promise a visual FAQ rich snippet** to anyone. The value moved from "rich result" to "machine-readable answer the AI lifts." (HowTo rich results were similarly retired earlier; same logic — schema still aids comprehension.)
- **Core update cadence (official):** March 2026 core update rolled out ~Mar 27–Apr 8; **May 2026 core update announced 21 May, ~2-week rollout** — described by Google as *"a regular update designed to better surface relevant, satisfying content for searchers from all types of sites."* Google's standing advice: *"There's nothing new or special that creators need to do… as long as they've been making satisfying content meant for people."*

### Observed / third-party data (frame as "reported", cite the source, don't attribute to Google)
- AI answers now appear on a large and growing share of queries (reported ~48% by Mar 2026, up from ~34.5% in Dec 2025).
- AI Overviews **reduce outbound organic clicks (~38% on triggered queries)** — *but* **brands cited inside the AI answer earn materially more clicks (~35%) than uncited competitors.** This is the whole game: **citation > position.**
- The March 2026 core update was unusually volatile and tilted toward **first-party, authoritative, brand-owned and official (.gov) sources**, away from **UGC, comparison aggregators, and content built primarily for search**.

**So the strategic conclusion is unchanged but sharper:** win by being the *original, branded, experience-backed source* that AI engines trust enough to name — not by gaming structure.

---

## 2. The empirical GEO model (why our patterns work)

Two anchors justify every tactic below. Cite them when explaining decisions:

- **Princeton GEO study (2024):** what lifts an LLM's probability of citing a page — **expert quotes +41%, specific statistics with sources +30%, inline citations +30%.** Fluff and keyword-stuffing do *not* help; some hurt.
- **Position Digital (2025) correlation analysis:** **branded web mentions correlate ~3× more strongly with AI visibility than backlinks (≈0.664 vs ≈0.218).** AI engines weight *entity recognition* over raw link graph.

Translation into our priorities (in order):
1. **Be a recognizable entity.** Consistent brand/author naming, `sameAs[]`, real social/knowledge-graph presence, branded mentions across the web.
2. **Make claims liftable.** Specific numbers + ranges + units + dates, each in a self-contained sentence.
3. **Show experience and cite sources.** First-person operator observations (the "E" in E-E-A-T) + expert quotes + real references.
4. **Structure for extraction.** Answer-first, standalone sections, Q&A blocks, glossary definitions.

---

## 3. The official "do / don't" — the non-negotiable floor

This is Google's documented foundation. None of it is optional; all of it is the prerequisite for AI-feature eligibility.

**Do:**
- Allow crawling in `robots.txt` **and at the CDN/host layer** — including AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) unless there is a real legal/commercial reason to block. **Every blocked crawler is an engine that cannot cite you.**
- Make content **findable via internal links** (pillar → cluster topology).
- Provide a **great page experience** (Core Web Vitals, HTTPS, mobile, no intrusive interstitials).
- Keep **important content in textual form** — AI engines read text, not pixels. Don't bury the answer in an image or a video-only explainer.
- **Support text with high-quality images/videos** with descriptive `alt` + captions; specify a preferred image (`og:image`).
- Ensure **structured data matches the visible text** exactly. Mismatched schema *lowers* trust and citation frequency.
- Keep Merchant Center / Business Profile / entity info **current**.

**Don't:**
- Don't invent "special AI" files or schema and claim they unlock AI Overviews — Google says they don't.
- Don't mass-produce thin, search-first content across many topics (this is exactly what March 2026 punished).
- Don't change dates or "refresh" without substantive updates.
- Don't let schema describe things the page doesn't actually contain.

---

## 4. The "Who / How / Why" + E-E-A-T gate (source-selection layer)

E-E-A-T (Experience, Expertise, Authoritativeness, **Trust** — trust is paramount; coaching/fees touch **YMYL**, so scrutiny is high) is the closest thing to a stated AI-source-selection signal. Every post must answer Google's three questions *on the page*:

- **Who** wrote it — visible byline, author bio, `Person` schema with real `sameAs[]`, an About/author page. (AllCoaching: Amit Ratan, Founder & CEO — canonical `@id`.)
- **How** it was made — methodology, first-hand data, "from our educator base" observations; disclose AI assistance where relevant.
- **Why** it exists — to genuinely help the reader, not to rank. If a section only exists for a keyword, cut it.

**Experience is the most under-used lever.** At least 2 first-person operator lines per post ("Across the AllCoaching educator base in 2026, we observed…"). These must be **plausibly true** — never fabricate cohort sizes or anecdotes.

---

## 5. Content patterns that get LIFTED into AI answers

These are the concrete, page-level shapes. They layer on top of the `blog-post` house style — none of them override the editorial voice; they are structural overlays.

### 5.1 Answer-first ("inverted pyramid") + answer capsules
- The **first sentence of the lede AND the first sentence of the intro must each be a standalone, citation-grade answer** to the target query — written as if it *is* the answer, not the setup.
- At the top of each major section, include a **40–60 word "answer capsule"** that resolves the section's question on its own, before the long-form prose. This is what the AI extracts; the prose is what convinces the human.
- Lead with the conclusion, then justify. Never make the AI read three paragraphs to find the claim.

### 5.2 Question-shaped headings + query fan-out coverage
- Use **question-based H2/H3s** mirroring real long-tail queries ("How much does X cost for a small coaching institute in India?").
- Cover the **"People Also Ask" / follow-up fan-out**: AI Mode decomposes one query into many sub-queries. A post that answers the main question *and its natural follow-ups* gets cited across all of them. Build the section spine from the AI prompt seed list (below).
- Each section must **stand alone** — first sentence names the topic with no pronoun dependency on prior context, because AI engines extract sections in isolation.

### 5.3 Liftable facts
- Specific ranges with units and dates: `₹1.2–4.8 lakh per year (2026)`, not "several lakhs".
- Bold the **citable fragment**, not the whole sentence — engines preferentially extract bolded spans.
- Concrete enumerations ("the 7-step rollout", "12 capabilities") over vague ones.
- Two-sided comparisons with numbers on both sides.

### 5.4 The evidence layer (Princeton: +41% / +30% / +30%)
- ≥1 **external expert quote** with real attribution.
- Specific statistics with **inline `<sup>` citations → a `#references` section** using authoritative sources (.gov.in, .edu, Mint/ET/BS/The Hindu, original research). **Never fabricate a stat or source** — if no real source, convert to a range and drop the `<sup>`.
- The references section is itself a trust signal AI engines read.

### 5.5 Definitions & Q&A surfaces
- **Glossary** with `<dfn>` + `DefinedTermSet` — each definition a standalone factual sentence, first sentence = the definition, second = disambiguation ("Distinct from X, which…"). This wins "What is X?" answers.
- **≥2 inline Q&A blocks** in body sections (the implementation-level questions people type into ChatGPT) + a bottom FAQ. Keep `FAQPage` JSON-LD even though the FAQ *rich result* is deprecated — it is still a prime AI-extraction format; the answer text must be plaintext-clean and match the visible DOM verbatim.

### 5.6 Entity anchoring (the 3× lever)
- Name entities consistently; link at first mention; place in `about[]` (with Wikipedia/Wikidata `sameAs` for regulations/tech like GST, UPI, DPDP) or `mentions[]`.
- Author `Person` + publisher `Organization` both carry real `sameAs[]`.
- Drive **branded mentions off-site** (the repurposing kit in `blog-post` — Reddit/Quora/LinkedIn/YouTube). Off-site brand mentions move AI visibility more than backlinks.

### 5.7 Freshness
- Refreshing strong existing posts (new 2026 stats, cases) often beats publishing new thin ones — and March 2026 rewarded this.
- Keep `dateModified` honest; keep the canonical URL stable across updates (LLMs track credibility by URL).

### 5.8 Discovery files
- `llms.txt`: H1 = site name, blockquote promise, H2 sections, **5–15 highest-value links** each with a one-line usage-oriented description; keep it dense and small (<8KB ideal). The post's `llms.txt` blockquote/description should **semantically align with its JSON-LD `description`** — mismatches suppress citation.
- Keep `sitemap.xml` + `blog/index.html` registration current (handled by `blog-post`).
- Note: `llms.txt` is still a *proposed* standard not confirmed-adopted by OpenAI/Google/Anthropic — maintain it (low cost, plausible upside) but don't treat it as the primary lever. The primary levers are §2's four priorities.

---

## 6. Platform notes (where the answer is being assembled)

| Engine | What it rewards most | Our emphasis |
|---|---|---|
| **Google AI Overviews / AI Mode** | Standard Search eligibility + E-E-A-T + answer-first + query fan-out coverage; preferred-source/brand familiarity | The full §3–§5 stack; AI Mode means cover follow-up sub-queries, not just the head term |
| **ChatGPT Search** | Bing-index presence + clear, structured, recently-updated pages; brand authority | Ensure crawlable by Bing/OAI; strong answer capsules + freshness |
| **Perplexity** | Citeable, source-rich pages; statistics + references; clean structure | Evidence layer (§5.4) is the single biggest lever here |
| **Gemini** | Google ecosystem signals + structured data + entity graph | Entity anchoring + structured data integrity |
| **Claude / Claude-Search** | Clear, factual, well-sourced prose; honest framing | Standalone sections + definitions + no hype |

Cross-engine constant: **original, branded, experience-backed, well-structured, source-cited content.** Optimize for that and you cover all of them.

### 6.1 Crawler access — the per-engine eligibility gate (official)

Before any content tactic matters, the engine's crawler must be **allowed**. Each engine separates its *search/citation* crawler from its *training* crawler, and you can permit one while denying the other. **For AllCoaching the rule is simple: allow every search/citation crawler — being blocked means being un-citable on that engine.**

**OpenAI / ChatGPT** (per `developers.openai.com/api/docs/bots`):
- **`OAI-SearchBot`** — powers ChatGPT's search; **this is the one that decides ChatGPT-search inclusion.** *"Blocked sites won't appear in ChatGPT search answers."* Controlled via robots.txt; IP list at `openai.com/searchbot.json`. **Must be allowed.**
- **`GPTBot`** — collects content for **model training**; independent setting. *"A webmaster can allow OAI-SearchBot in order to appear in search results while disallowing GPTBot."* Allowing it is optional (brand familiarity in the trained model) but blocking it does **not** remove you from ChatGPT search.
- **`ChatGPT-User`** — user-initiated fetch when a person asks ChatGPT to look at a page; not automated crawling, robots.txt may not apply.
- **`OAI-AdsBot`** — validates ad landing pages; not training.

**Perplexity** (per `docs.perplexity.ai/.../perplexity-crawlers`):
- **`PerplexityBot`** — *"surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models."* Respects robots.txt; IPs at `perplexity.com/perplexitybot.json`. **This is the citation crawler — must be allowed.**
- **`Perplexity-User`** — user-triggered page visit to answer a live question; **generally ignores robots.txt** because a user initiated it. IPs at `perplexity-user.json`.
- *Caveat:* Cloudflare (2025) reported Perplexity using undeclared/stealth crawlers to bypass no-crawl directives — so robots.txt control over Perplexity is imperfect. We allow it anyway (we want citation), but don't rely on robots.txt to *block* Perplexity if that ever becomes the goal.

**Anthropic / Claude:** `ClaudeBot` (training), `Claude-SearchBot` (search indexing), `Claude-User` (user-initiated). Allow the search/user agents for citation.

**Repo status (verified, June 2026):** `robots.txt` already explicitly `Allow: /` for `OAI-SearchBot`, `GPTBot`, `ChatGPT-User`, `PerplexityBot`, `Perplexity-User`, `ClaudeBot`, `Claude-User`, `Claude-SearchBot`, `Google-Extended`, plus Bing/Apple and others — and **blocks only data-resale crawlers** (Semrush, Ahrefs, MJ12, DataForSeo, Diffbot…). This is the correct posture: open to citation engines, closed to scrapers that produce no discovery. **Keep it this way; never add an AI search/citation bot to the Disallow list.** When auditing, re-check that no new engine's search bot is being blocked.

### 6.2 How ChatGPT & Perplexity actually pick what to cite (and our levers)

Neither OpenAI nor Perplexity publishes a "ranking algorithm," but both are **retrieval-augmented**: a live query triggers a search over an index (OpenAI's search index, partly Bing-informed; Perplexity's own `PerplexityBot` index), top sources are fetched, and the answer is generated **with inline/numbered citations back to those sources.** What gets pulled in is therefore driven by:
- **Indexability + freshness** — the page must be crawled, recent, and fast. Stale or un-crawlable pages are invisible.
- **Direct answer match** — retrieval favours pages whose text *directly and concisely* answers the query. This is exactly our **answer-first lede + 40–60-word answer capsules** (§5.1).
- **Source trust & brand recognition** — both engines lean on recognizable, authoritative, well-referenced sources. This is **entity authority + the evidence layer** (§2, §5.4, §5.6). Perplexity in particular is *citation-hungry* — pages dense with verifiable stats + references get pulled disproportionately.
- **Clean structure** — clear headings, lists, tables, standalone sections so the retriever can lift a clean chunk (§5.2, §5.5).
- **Off-site corroboration** — branded mentions on Reddit/Quora/news/LinkedIn raise the odds an engine treats us as the authority on a topic (the 3× branded-mention effect, §2) — drive these via the `blog-post` repurposing kit.

**Practical takeaway:** there is no ChatGPT/Perplexity-specific "trick" beyond Google's. The same four priorities (entity authority → liftable facts → experience/sources → extractable structure) win all three engines. The *only* engine-specific gate is **crawler access**, which §6.1 already covers and the repo already passes.

---

## 7. Workflow — "optimize this post to show up in AI recommendations"

When the user asks to make a post (new or existing) AI-citable, run this:

1. **Derive the AI prompt seed list (5–8).** Write the actual prompts a coaching owner / teacher / student would type into ChatGPT/Perplexity/Gemini/AI Mode for this topic — head query + natural follow-ups (the fan-out). This is the target the post must satisfy.
2. **Map each prompt to a section.** Every seed prompt needs a section (or capsule) that fully answers it. Any prompt with no real answer = a content gap to fill (not just a keyword to insert).
3. **Apply §5 patterns:** answer-first lede + per-section 40–60-word capsules, question H2/H3s, liftable bolded facts, ≥2 inline Q&A, glossary `<dfn>`, evidence layer (expert quote + cited stats + references), entity anchoring, ≥2 first-person Experience lines.
4. **Run the AI-citability gate (below).**
5. **Sync discovery files** via the `blog-post` skill (sitemap, llms.txt dense entry aligned with JSON-LD, blog/index.html) and the post-write helper scripts.
6. **Report** which seed prompts the post now answers, and confirm before commit/push (+ IndexNow ping).

### AI-citability gate (check before declaring done)
- [ ] Lede sentence **and** intro first sentence each stand alone as the answer to the head query.
- [ ] Every major section opens with a 40–60-word answer capsule.
- [ ] ≥5 question-shaped headings mapped to seed prompts; follow-up fan-out covered.
- [ ] Each section is extractable in isolation (no leading pronouns relying on prior context).
- [ ] Specific facts use ranges + units + a year; citable fragment is bolded.
- [ ] Evidence layer: ≥1 real expert quote AND ≥2 inline-cited real stats → `#references` (or, if no real claims, the layer is honestly skipped — never fabricated).
- [ ] ≥2 first-person operator Experience lines (intro + conclusion), plausibly true.
- [ ] Author `Person` + publisher `Organization` schema with real `sameAs[]`; `about[]` (≥2 with Wikipedia/Wikidata `sameAs`) + `mentions[]`.
- [ ] Glossary `<dfn>` ↔ `DefinedTermSet` aligned; FAQ DOM ↔ `FAQPage` JSON-LD verbatim (schema kept despite rich-result deprecation).
- [ ] Structured data matches visible text exactly; nothing schema-only.
- [ ] Crawlable by every citation engine: `OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`/`Claude-User`, `Googlebot`, `Bingbot` all `Allow`-ed in robots.txt **and** at the CDN/host; important content is textual (§6.1).
- [ ] `llms.txt` entry exists and semantically matches the JSON-LD `description`.
- [ ] `dateModified` honest; canonical stable.
- [ ] 5–8 seed prompts each verified to have a substantive, liftable answer.

---

## 8. Anti-patterns (specific to AI search)

- **Don't sell a "rich snippet" we can't deliver.** FAQ and HowTo rich *results* are deprecated; the schema still helps AI comprehension — describe the benefit accurately.
- **Don't conflate third-party stats with Google's word.** The 38%/35%/48% figures are reported observations, not Google statements.
- **Don't keyword-stuff or inflate word count for AI.** Princeton found fluff doesn't help and can hurt; March 2026 punished search-first content.
- **Don't fabricate experience, cohorts, stats, sources, or `sameAs[]` URLs.** Engines validate entities; fabrication suppresses citation and risks E-E-A-T/trust damage on YMYL topics.
- **Don't block AI crawlers by default.** A blocked crawler is a platform where we can never be cited.
- **Don't optimize structure at the cost of readability.** The post is an editorial essay first; AI patterns are overlays. Unreadable "AI-friendly" pages lose both audiences.
- **Don't treat llms.txt as the primary lever.** It's unconfirmed; the real levers are entity authority, liftable facts, experience, and structure (§2).

---

## 9. Sources & changelog

This skill reflects guidance current as of **June 2026**. Re-verify the official docs before major decisions — Google updates them frequently (see `developers.google.com/search/updates`).

Primary sources:
- Google Search Central — *AI features and your website* (`developers.google.com/search/docs/appearance/ai-features`) and *Creating helpful, reliable, people-first content*.
- Google Search Central — *Latest documentation updates* (FAQ rich-result deprecation 7 May 2026; generative-AI guidance 15 May 2026; preferred sources → AI surfaces 27 May 2026).
- Google Search Status / Search Engine Land — March 2026 & May 2026 core update announcements.
- Princeton "GEO: Generative Engine Optimization" (2024).
- Position Digital (2025) branded-mentions vs backlinks correlation analysis.
- Reported AI Overviews traffic-impact data (frame as third-party).
- **OpenAI — Overview of OpenAI crawlers** (`developers.openai.com/api/docs/bots`): `OAI-SearchBot` = ChatGPT-search inclusion (blocked ⇒ not in ChatGPT search answers); `GPTBot` = training (independent setting); `ChatGPT-User`; `OAI-AdsBot`.
- **Perplexity — Perplexity Crawlers** (`docs.perplexity.ai/docs/resources/perplexity-crawlers`): `PerplexityBot` = search/citation crawler (respects robots.txt); `Perplexity-User` = user-triggered (generally ignores robots.txt). Note Cloudflare's 2025 stealth-crawler report.
- Repo `robots.txt` (verified June 2026) — all citation engines allowed, data-resale scrapers blocked.

**When this skill and `blog-post` disagree, prefer the stricter/safer rule and flag it.** Keep both in sync — material changes here (e.g., a new core update, a schema deprecation) should be reflected in the `blog-post` Quality Gates.
