"""
CLI scaffold helper — creates a new markdown source file with frontmatter.

Layout (sources hidden under sources/, outputs rendered into public dirs):
    blog  → sources/<lang>/<slug>.md
            renders to /blog/<slug>.html        (en, legacy URL)
                       /blogs/<lang>/<slug>.html (hi, hinglish)

USAGE:
    python scripts/new.py blog hinglish meri-nayi-post --category platforms-tools
"""
from __future__ import annotations
import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = """\
---
slug: {slug}
language: {language}
type: {type}
status: draft
author: amit-ratan
category: {category}
subcategory:
tags: []
keywords: []
translation_group:
title: "{title_placeholder}"
description: "{desc_placeholder}"
cover_image:
cover_image_alt:
published: {today}
modified: {today}
kicker:
epigraph:
epigraph_attribution:
reading_time_min:
word_count:
faq: []
---

# {title_placeholder}

Write your content here in Markdown.

## Section 1

...
"""

VALID_TYPES = {"blog", "news", "page"}
VALID_LANGS = {"en", "hi", "hinglish"}

# All markdown sources live under sources/, regardless of type.
SOURCES_DIR = "sources"  # markdown source-of-truth (not served as URLs)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("type", choices=sorted(VALID_TYPES))
    p.add_argument("language", choices=sorted(VALID_LANGS))
    p.add_argument("slug", help="URL slug — lowercase, hyphens only")
    p.add_argument("--category", default="", help="Required for blog type")
    p.add_argument("--force", action="store_true", help="Overwrite if exists")
    args = p.parse_args(argv)

    if not args.slug.replace("-", "").isalnum() or args.slug != args.slug.lower():
        print(f"Invalid slug '{args.slug}'. Use lowercase letters/digits/hyphens only.",
              file=sys.stderr)
        return 1

    out = ROOT / SOURCES_DIR / args.language / f"{args.slug}.md"
    if out.exists() and not args.force:
        print(f"REFUSED: {out.relative_to(ROOT)} already exists. Use --force to overwrite.",
              file=sys.stderr)
        return 1
    out.parent.mkdir(parents=True, exist_ok=True)

    title = args.slug.replace("-", " ").title()
    content = TEMPLATE.format(
        slug=args.slug,
        language=args.language,
        type=args.type,
        category=args.category,
        title_placeholder=title,
        desc_placeholder="Write a 1–2 sentence description here (used for meta + OG).",
        today=date.today().isoformat(),
    )
    out.write_text(content, encoding="utf-8")
    print(f"Created {out.relative_to(ROOT)}")
    print(f"  - fill in frontmatter, write markdown body")
    print(f"  - run: python scripts/build.py --post {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
