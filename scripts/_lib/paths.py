"""
Path / URL resolution — single source of truth for where a Post is written
to disk and what its canonical URL becomes.

URL strategy (2026-05-19 update — hi/hinglish unified under /blogs/):
    en blog       →  /blog/<slug>             → blog/<slug>.html       (legacy, untouched)
    hi blog       →  /blogs/hi/<slug>         → blogs/hi/<slug>.html
    hinglish blog →  /blogs/hinglish/<slug>   → blogs/hinglish/<slug>.html
    en news       →  /news/<slug>             → news/<slug>.html
    hi news       →  /blogs/hi/news/<slug>    (TBD — same pattern as blog)
    en page       →  /<slug>                  → <slug>.html
"""
from __future__ import annotations
from pathlib import Path
from .frontmatter import Post

HTML_LANG = {"en": "en-IN", "hi": "hi-IN", "hinglish": "hi-Latn"}
HREFLANG = {"en": "en-IN", "hi": "hi-IN", "hinglish": "hi-Latn"}
OG_LOCALE = {"en": "en_IN", "hi": "hi_IN", "hinglish": "hi_IN"}


def url_path(post: Post) -> str:
    """Site-relative URL path (no domain).
       EN blog stays at /blog/<slug> (legacy).
       Non-EN blog posts live under /blogs/<lang>/<slug>.
    """
    if post.type == "page":
        return f"/{post.slug}" if post.language == "en" else f"/{post.language}/{post.slug}"
    if post.type == "blog":
        if post.language == "en":
            return f"/blog/{post.slug}"
        return f"/blogs/{post.language}/{post.slug}"
    # news / other types
    if post.language == "en":
        return f"/{post.type}/{post.slug}"
    return f"/{post.language}/{post.type}/{post.slug}"


def canonical_url(post: Post, site_url: str) -> str:
    return site_url.rstrip("/") + url_path(post)


def output_path(post: Post, root: Path) -> Path:
    """Where the rendered HTML goes on disk, relative to project root.
       Mirrors url_path exactly (URL = path on disk).
    """
    rel = url_path(post).lstrip("/")
    return root / f"{rel}.html"


def asset_url(filename: str, cdn_base: str) -> str:
    """Resolve a cover_image filename against the CDN base."""
    if filename.startswith(("http://", "https://", "/")):
        return filename
    return f"{cdn_base.rstrip('/')}/{filename.lstrip('/')}"
