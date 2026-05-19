"""
Main build script — renders sources/<lang>/<slug>.md to blogs/<lang>/<slug>.html.

USAGE:
    python scripts/build.py                 # build everything
    python scripts/build.py --validate-only # validate, no write
    python scripts/build.py --post <path>   # build a single post
    python scripts/build.py --listing       # also rebuild listing/index pages

Safety guarantees:
    1. Will NEVER overwrite a legacy-protected path (safety_guard.py).
    2. Will NEVER touch /blog/*.html (the 28 legacy artisan posts).
    3. Refuses to write to non-content-derived paths.

Exit codes:
    0 — success
    1 — validation errors (no write attempted)
    2 — safety violation / unexpected failure
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from typing import Iterable

import jinja2

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _lib.safety_guard import assert_safe, SafetyError
from _lib.frontmatter import Post, parse_dir, parse_file, FrontmatterError
from _lib.paths import (
    HTML_LANG, OG_LOCALE, canonical_url, url_path, output_path, asset_url,
)
from _lib.taxonomy import (
    load_site, load_authors, validate_post, category_label, get_category,
)
from _lib.translations import collect_groups, hreflang_links_for
from _lib.schema_builder import render_all_schemas
from _lib.renderer import render_with_toc


CONTENT_DIR = ROOT / "sources"   # markdown sources (hidden from public tree)
TEMPLATES_DIR = ROOT / "templates"
IS_WINDOWS = sys.platform == "win32"


def _jinja_env() -> jinja2.Environment:
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=jinja2.select_autoescape(["html", "j2"]),
        trim_blocks=False,
        lstrip_blocks=False,
        keep_trailing_newline=True,
    )


def _assets_prefix(out_rel: Path) -> str:
    """How many '../' to reach project root from output_path."""
    depth = len(out_rel.parts) - 1  # minus the file itself
    return "../" * depth if depth > 0 else ""


def _render_post(env: jinja2.Environment, post: Post,
                 groups: dict) -> tuple[Path, str]:
    site = load_site(ROOT)
    authors = load_authors(ROOT)
    author = authors[post.author]

    out_path = output_path(post, ROOT)
    out_rel = out_path.relative_to(ROOT)
    assets_prefix = _assets_prefix(out_rel)

    cover_url = asset_url(post.cover_image, site.cdn_images_base) if post.cover_image else None
    canonical = canonical_url(post, site.url)
    hreflangs = hreflang_links_for(post, groups, site.url)
    schemas = render_all_schemas(post, ROOT)

    body_html, toc_html = render_with_toc(post.body_markdown)

    section_label = None
    if post.category:
        section_label = category_label(ROOT, post.category, post.language)

    template_name = "article.html.j2"
    tpl = env.get_template(template_name)
    html = tpl.render(
        post=post,
        author=author,
        site=site,
        canonical=canonical,
        hreflangs=hreflangs,
        schemas=schemas,
        cover_url=cover_url,
        html_lang=HTML_LANG[post.language],
        og_locale=OG_LOCALE[post.language],
        assets_prefix=assets_prefix,
        body_html=body_html,
        toc_html=toc_html,
        section_label=section_label,
        is_windows=IS_WINDOWS,
    )
    return out_path, html


def _gather_posts(single: Path | None) -> list[Post]:
    if single:
        return [parse_file(single)]
    return parse_dir(CONTENT_DIR)


def _validate_all(posts: list[Post]) -> list[str]:
    errors: list[str] = []
    for p in posts:
        for err in validate_post(ROOT, p):
            errors.append(f"{p.source_path}: {err}")
    return errors


def _safe_write(out_path: Path, html: str) -> None:
    assert_safe(out_path, action="write")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="AllCoaching content build")
    p.add_argument("--post", type=Path, help="Build a single markdown file")
    p.add_argument("--validate-only", action="store_true", help="Validate, no write")
    p.add_argument("--include-drafts", action="store_true",
                   help="Also build status=draft posts (default: skip)")
    args = p.parse_args(argv)

    try:
        all_posts = _gather_posts(args.post)
    except FrontmatterError as e:
        print(f"FRONTMATTER ERROR: {e}", file=sys.stderr)
        return 1

    if not all_posts:
        print("No posts found under sources/. Nothing to build.")
        return 0

    errors = _validate_all(all_posts)
    if errors:
        print("VALIDATION ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    publishable: list[Post] = [
        p for p in all_posts
        if p.status == "published" or args.include_drafts
    ]
    if not publishable:
        print(f"No publishable posts (found {len(all_posts)} total, all drafts).")
        return 0

    if args.validate_only:
        print(f"OK — validated {len(all_posts)} post(s), {len(publishable)} publishable.")
        return 0

    env = _jinja_env()
    groups = collect_groups(ROOT, all_posts)

    written = 0
    for post in publishable:
        try:
            out_path, html = _render_post(env, post, groups)
            _safe_write(out_path, html)
            print(f"  wrote  {out_path.relative_to(ROOT)}  <-  {post.source_path.relative_to(ROOT)}")
            written += 1
        except SafetyError as e:
            print(f"SAFETY VIOLATION: {e}", file=sys.stderr)
            return 2
        except Exception as e:
            print(f"FAILED rendering {post.source_path}: {e}", file=sys.stderr)
            return 2

    print(f"Done. Rendered {written} post(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
