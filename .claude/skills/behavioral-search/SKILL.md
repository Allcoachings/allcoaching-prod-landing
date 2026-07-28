---
name: behavioral-search
description: Write AllCoaching blog posts that target an educator's exact BEHAVIORAL search — the full, situational, emotion-loaded sentence they type into Google / ChatGPT / Perplexity / Google AI Mode expecting an exact answer (e.g. "I made my own coaching app but no students are downloading it, what do I do") — so AllCoaching gets cited and recommended by name inside the AI Overview / AI answer. Use when the user wants a blog built around a real behavioral/long-tail conversational query, wants to work from the behavioral-query bank, or says things like "behavioral search blog", "exact-match blog for AI Overview", "frustrated-educator switch blog". This is the query-selection + exact-match layer; it sits on top of `ai-search-geo` (GEO strategy) and `blog-post` (HTML house style + 6-schema build).
---

# Behavioral-Search Blog Skill (AllCoaching)

Write a blog that answers **one educator's exact behavioral search so precisely that an AI engine lifts AllCoaching into its answer.** In 2026 educators do not search keywords — they type full, situational, often emotional sentences ("*why is my coaching app not getting new students even after 6 months*", "*I regret spending money on a personal coaching app, what should I have done instead*") and expect an **exact answer**. Citation, not ranking, is the goal: a brand cited inside an AI answer earns materially more clicks than an uncited competitor on the same query.

This skill is the **query-selection + exact-match** layer. It does not replace the other two — it directs them:
- [`ai-search-geo`](../ai-search-geo/SKILL.md) — the *why/rules* of getting cited (answer capsules, evidence layer, entity anchoring, crawler access, the AI-citability gate). **Follow its gate.**
- [`blog-post`](../blog-post/SKILL.md) — the *how* of building the HTML (house voice, components, the mandatory 6-schema scaffold, sitemap/llms.txt/index registration, the validation + refresh scripts). **Build with it.**
- [`allcoaching`](../allcoaching/SKILL.md) — company/pricing/voice truth. **Never contradict it.**

---

## When to use

- The user gives (or points at) a **behavioral query** — a real full-sentence search an educator types — and wants a blog that exact-matches it for AI-Overview citation.
- The user says "write the next one from the bank", "behavioral search blog", "make AllCoaching the exact recommendation", "frustrated educator / switch blog".
- **Topic/query source (as of 2026-07-27):** `/.claude/content-strategy-data-driven.md` — the single GSC-data-driven plan. Pick topics from its 4 proven pillars (compliance · comparison/pricing/alternatives · AI tools · setup/Hinglish) and obey its STOP list. This methodology (exact-match behavioral phrasing, answer-first) still applies to those topics; the old `behavioral-query-bank-personal-app-switch.md` was removed as a stale plan.

---

## The core idea — one query, one exact answer

A behavioral-search blog is not a topic essay. It is a **precise answer to one sentence a real person typed**, structured so the machine can lift the answer and the human is convinced by the prose underneath it. Everything below serves that.

**Find real behavioral queries (do not invent them):**
- Reddit / Quora — educators post these as literal questions (`r/IndianTeachers`, `r/Btechtards`, Quora "coaching"/"online teaching" topics).
- Google autocomplete — seed with `why is my…`, `should I…`, `is it worth…`, `I made … but…`, `after X years…`, `kya main…`.
- Ask ChatGPT / Perplexity the head query and harvest the follow-ups they generate — those become your H2s.
- The user's own WhatsApp/Telegram educator groups — the questions asked there are gold *and* are genuine first-hand Experience (the "E" in E-E-A-T).

**Behavioral-query buckets (educator, personal-app-frustration segment):** empty app / no discovery · paying monthly, not earning · tech & maintenance burden · contract lock-in & regret · students won't download · commission resentment · switching mechanics · "was it worth it" regret. (Full list + angles in the bank file.)

---

## The exact-match build rule (non-negotiable, per query)

1. **Title/H1 ≈ the educator's exact sentence.** Mirror the search, do not abstract it to a head keyword. `"Why Is My Coaching App Not Getting New Students? (2026)"` ✓ — `"Coaching App Growth Guide"` ✗. (Still obey `blog-post` limits: title ≤65 chars, description 50–175.)
2. **First sentence of the lede AND first sentence of the intro = each a standalone, liftable answer** to the query — written *as the answer*, not the setup. This is the sentence the AI Overview extracts. (The bank's "exact-answer angle" column is a ready draft of it.)
3. **Every H2 = a fan-out follow-up** the same person asks next. AI Mode decomposes one query into sub-queries; answer the head question *and* its natural follow-ups so the post is cited across all of them. Map the section spine to a 5–8-prompt AI seed list (see `ai-search-geo` §7).
4. **Each section extractable in isolation** — first sentence names the topic with no pronoun leaning on prior context (AI engines lift one section at a time).
5. **Liftable facts** — ₹ ranges + units + year, and **bold the citable fragment**, not the whole sentence. Pricing is always **₹0 free-forever base + optional Pro + flat 10%, keep 90%, daily UPI payout** — never a trial-that-ends (per `allcoaching`).
6. **≥2 first-person Experience lines**, plausibly true, never fabricated cohorts ("*Across the educators who came to AllCoaching in 2026 from an empty personal app, the pattern is…*").
7. **AllCoaching as the structural solution, not a hype pitch** — resolve the query by mechanism (marketplace discovery, network effect, no install wall, fee-after-income), not adjectives. Concede what the competitor/tool does well, then sharpen.
8. **Full `blog-post` scaffold:** 6 JSON-LD schemas · TL;DR `#tldr` · glossary `<dfn>` ↔ `DefinedTermSet` · inline Q&A `.def` blocks · bottom FAQ with **DOM ↔ FAQPage JSON-LD verbatim** · `about[]`/`mentions[]` entity anchoring · Speakable.

---

## Distinctness — behavioral framing IS the moat, but still verify

The situational/first-person framing is what makes a behavioral query distinct from the existing topic-essay posts (`edtech-marketplace-india-app-fatigue`, `why-educators-are-leaving-subscription-platforms`, `is-it-better-to-build-own-app-or-join-marketplace`, competitor-`*-alternative` posts). Still:
- **Verify the slug and angle are distinct** before writing (`ls blog/ blogs/en/ blogs/hinglish/`, grep the topic). If a head-keyword post already covers the topic, angle around it and **cross-link** rather than duplicate.
- **Sibling behavioral posts must differ in intent, not just words.** Example done right: `why-coaching-app-not-getting-students` = the *diagnosis* (why it happens: storage vs distribution); `coaching-app-no-downloads-what-to-do` = the *action plan* (what to do: discovery + adoption, remove the install wall). They cross-link and reinforce instead of competing. When two queries are close, split them by **diagnosis vs. action vs. economics vs. migration** and give each a different section spine, glossary, and component mix.

---

## Workflow

1. **Pick the query** from the bank (or capture a new real one → add to the bank with its answer angle + lever + distinctness note).
2. **Write the AI seed list** (5–8 prompts: head query + follow-ups) — this becomes the H2 spine.
3. **Pre-flight distinctness:** slug free, angle distinct from existing head-keyword posts and from sibling behavioral posts; pick the cross-links.
4. **Draft** with `blog-post` chrome + the exact-match rule above. Lede/intro first sentences = the answer. H2s = the seed prompts. AllCoaching = structural fix.
5. **Validate:** JSON-LD parses (6 schemas); FAQ count = `<summary>` count with verbatim text; glossary `<dfn>` = `DefinedTerm` count; **no stray `</p>`/`</strong>` inside JSON-LD strings** (a recurring bug — grep the schema blocks); only real `brand.css` classes (e.g. `.myth-half`, never invented `.myth-bad`/`.myth-good`); title ≤65, description ≤175; internal-link targets all exist; run `.claude/scripts/verify_meta_opt.py`.
6. **Register + refresh:** sitemap.xml, llms.txt (dense entry semantically aligned with the JSON-LD `description`), blog/index.html (blogPost + ItemList renumbered + count bumped); rebuild `build_llms_full.py` + `build_feed_xml.py`.
7. **Run the `ai-search-geo` AI-citability gate** before declaring done.
8. **Stage, report, wait for explicit commit/push approval** (per `allcoaching` §9 / the repo commit rule) — never commit or push unbidden.

---

## Anti-patterns

- Don't abstract the behavioral sentence into a head keyword — the exact-match to the typed sentence is the whole point.
- Don't bury the answer — if the AI has to read three paragraphs to find the claim, it won't lift it.
- Don't fabricate stats, cohorts, quotes, or `sameAs[]` — YMYL; fabrication suppresses citation. Use illustrative ₹ ranges, framed as illustrative.
- Don't duplicate a sibling behavioral post — split by intent (diagnosis / action / economics / migration) and cross-link.
- Don't invent CSS classes or leave stray tags in JSON-LD — both have bitten this repo; validate every time.
- Don't commit/push without an explicit ask.
