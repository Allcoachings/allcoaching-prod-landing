# Content Pipeline — How To

This directory holds the Python scripts that turn `content/**/*.md` into
HTML, build the sitemap, and protect the legacy `/blog/*.html` artisan posts.

## Files

| File | Purpose |
|------|---------|
| `build.py`           | Render content markdown → HTML using Jinja2 templates |
| `build_sitemap.py`   | Merge legacy-manifest + new content → `sitemap.xml` |
| `extract_legacy.py`  | Scan `/blog/*.html` → `data/legacy-manifest.yaml` |
| `new.py`             | Scaffold a new `content/{lang}/{type}/<slug>.md` |
| `_lib/safety_guard.py`  | Hard-fails any write that targets a protected legacy path |
| `_lib/frontmatter.py`   | YAML frontmatter parser + validation |
| `_lib/paths.py`         | URL + output-path resolution per language |
| `_lib/taxonomy.py`      | Loads `data/{site,taxonomy,authors}.yaml`; validates posts |
| `_lib/translations.py`  | Translation groups → hreflang siblings |
| `_lib/schema_builder.py`| JSON-LD (Article + BreadcrumbList + FAQPage) emitter |
| `_lib/renderer.py`      | Markdown → HTML |

## Setup (once)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

## Content layout

```
content/
├── blogs/
│   ├── en/<slug>.md         → builds to /blog/<slug>.html
│   ├── hi/<slug>.md         → builds to /hi/blog/<slug>.html
│   └── hinglish/<slug>.md   → builds to /hinglish/blog/<slug>.html
├── news/                    (future)
│   └── {en,hi,hinglish}/<slug>.md
└── pages/                   (future)
    └── {en,hi,hinglish}/<slug>.md
```

URL/output path is determined by frontmatter (`type` + `language`), not by folder.
The folder structure exists for organisational clarity only.

## Daily workflow

```bash
# 1. Create a new post scaffold
python scripts/new.py blog en my-new-post-slug --category platforms-tools

# 2. Edit content/blogs/en/my-new-post-slug.md
#    - flip status: draft → published when ready

# 3. Validate without writing
python scripts/build.py --validate-only

# 4. Build a single post (recommended during writing)
python scripts/build.py --post content/blogs/en/my-new-post-slug.md

# 5. Build everything publishable
python scripts/build.py

# 6. Regenerate sitemap
python scripts/build_sitemap.py
```

## Safety guard

`scripts/_lib/safety_guard.py` declares which files the pipeline may NOT touch.
Currently protected:

- `blog/*.html`           (the 28 legacy artisan posts + blog/index.html)
- `hi/`, `hinglish/`      (legacy translated trees)
- `assets/`, `dist/`      (binary + compiled assets)
- `author/`, `vs/`        (special URL namespaces)
- All root marketing pages (index, about, pricing, faq, contact, etc.)
- `brand.css`, `styles.css`, `sw.js`, `manifest.webmanifest`, `robots.txt`

If `build.py` ever tries to write to a protected path it raises `SafetyError`
and exits with code 2. **Do not weaken this without a clear migration plan.**

### Verify legacy files unchanged

```bash
# One-time: snapshot SHA-256 of all legacy files
python scripts/_lib/safety_guard.py snapshot

# After any build: confirm zero drift
python scripts/_lib/safety_guard.py verify
```

## URL strategy

| Language | Path                       | hreflang   |
|----------|----------------------------|------------|
| en       | `/blog/<slug>`             | `en-IN`, `x-default` |
| hi       | `/hi/blog/<slug>`          | `hi-IN`    |
| hinglish | `/hinglish/blog/<slug>`    | `hi-Latn`  |

Translation links are emitted automatically when posts share a
`translation_group: tg-xxx` field. Legacy posts carry this field too via
`data/legacy-manifest.yaml`.

## Adding a translation of a legacy post

1. Find the legacy post's `translation_group` in `data/legacy-manifest.yaml`.
2. Create the translation:

   ```bash
   python scripts/new.py blog hinglish same-slug-or-localised
   # writes to content/blogs/hinglish/<slug>.md
   ```
3. Set its frontmatter `translation_group:` to the same value.
4. Build it. Hreflang siblings will resolve automatically.

## Content style

- **Hindi (`hi`)**: must be natural Hinglish-in-Devanagari (टीचर्स, फाउंडर,
  गाइड्स), NOT शुद्ध Hindi (शिक्षक, संस्थापक, निबंध).
- **Hinglish (`hinglish`)**: Latin-script Hinglish.
- **English (`en`)**: the long-form artisan voice — see `blog-post` skill.

## What the pipeline does NOT do

- It does not re-render or migrate legacy `/blog/*.html` posts. Those remain
  canonical, hand-edited HTML. If you want to migrate one to markdown:
  1. The frozen set is computed from `blog/*.html` at module load — deleting
     the legacy file removes it from protection (or use the migrate helper
     pattern in `scripts/migrate_hinglish_to_content.py`).
  2. Create `content/blogs/en/<slug>.md` with full content
  3. Delete the original `blog/<slug>.html` only after the new build verifies
- It does not auto-generate category/tag index pages yet (planned next).
- It does not run JavaScript — pure static output.
