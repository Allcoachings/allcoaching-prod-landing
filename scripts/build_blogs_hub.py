"""
Build the blogs hub + per-language filter pages:
  /blogs/index.html           — All posts
  /blogs/en/index.html        — English filter
  /blogs/hi/index.html        — Hindi filter (empty state until posts exist)
  /blogs/hinglish/index.html  — Hinglish filter

Combines:
  - 28 legacy EN posts from data/legacy-manifest.yaml
  - new posts from sources/{en,hi,hinglish}/*.md

USAGE:
    python scripts/build_blogs_hub.py             # write all 4 pages
    python scripts/build_blogs_hub.py --dry-run   # print all-page preview to stdout
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
import yaml
import jinja2

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _lib.safety_guard import assert_safe
from _lib.frontmatter import parse_dir
from _lib.taxonomy import load_site, category_label
from _lib.paths import url_path, asset_url

TEMPLATES_DIR = ROOT / "templates"

# Filter slug → (output path, language code matched, page title suffix)
FILTER_PAGES = {
    "all":      {"path": ROOT / "blogs" / "index.html",          "languages": {"en", "hi", "hinglish"}},
    "en":       {"path": ROOT / "blogs" / "en" / "index.html",   "languages": {"en"}},
    "hi":       {"path": ROOT / "blogs" / "hi" / "index.html",   "languages": {"hi"}},
    "hinglish": {"path": ROOT / "blogs" / "hinglish" / "index.html", "languages": {"hinglish"}},
}

FILTER_META = {
    "all": {
        "page_title":   "AllCoaching Blog — All Languages | EN · हिन्दी · Hinglish",
        "page_description": "Long-form, founder-written guides on educator infrastructure, marketplace economics, AI workflows, EdTech compliance, and the architecture of online teaching in India — across English, हिन्दी, and Hinglish.",
        "pill_label":   "Editorial Archive · 2026",
        "pill_meta":    "All languages",
        "heading_top":  "The AllCoaching",
        "heading_accent": "Blog.",
        "section_kicker": "Newest first",
        "section_heading_top": "All",
        "section_heading_accent": "guides.",
        "canonical_path": "/blogs/",
        "assets_prefix": "../",
    },
    "en": {
        "page_title":   "AllCoaching Blog — English Guides | EdTech Founder's Library",
        "page_description": "Long-form, founder-written English guides on educator infrastructure, marketplace economics, AI workflows, EdTech compliance — for the senior educator who treats their teaching business like a serious operation.",
        "pill_label":   "Editorial Archive · English",
        "pill_meta":    "By the founder",
        "heading_top":  "The AllCoaching",
        "heading_accent": "English Blog.",
        "section_kicker": "Newest first",
        "section_heading_top": "English",
        "section_heading_accent": "guides.",
        "canonical_path": "/blogs/en/",
        "assets_prefix": "../../",
    },
    "hi": {
        "page_title":   "AllCoaching Blog — हिन्दी Guides | Indian Teachers ke liye",
        "page_description": "Indian teachers ke liye long-form हिन्दी guides — educator infrastructure, marketplace economics, AI workflows, EdTech compliance, aur online teaching ka future.",
        "pill_label":   "Editorial Archive · हिन्दी",
        "pill_meta":    "By the founder",
        "heading_top":  "The AllCoaching",
        "heading_accent": "हिन्दी Blog.",
        "section_kicker": "Newest first",
        "section_heading_top": "हिन्दी",
        "section_heading_accent": "guides.",
        "empty_state_title": "हिन्दी guides coming soon",
        "empty_state_desc": "Hindi mein detailed guides abhi launch nahi hue. Naya content milne ke baad yahaan publish honge. Tab tak browse all posts across languages.",
        "canonical_path": "/blogs/hi/",
        "assets_prefix": "../../",
    },
    "hinglish": {
        "page_title":   "AllCoaching Blog — Hinglish Guides | Indian Teachers ke liye",
        "page_description": "Founder-written long-form Hinglish guides — coaching app banane se lekar marketplace economics tak, sab kuch one-place pe.",
        "pill_label":   "Editorial Archive · Hinglish",
        "pill_meta":    "By the founder",
        "heading_top":  "The AllCoaching",
        "heading_accent": "Hinglish Blog.",
        "section_kicker": "Newest first",
        "section_heading_top": "Hinglish",
        "section_heading_accent": "guides.",
        "canonical_path": "/blogs/hinglish/",
        "assets_prefix": "../../",
    },
}

LANG_LABEL = {"en": "English", "hi": "हिन्दी", "hinglish": "Hinglish"}
LANG_HREFLANG = {"en": "en-IN", "hi": "hi-IN", "hinglish": "hi-Latn"}


def _coerce_date(v) -> date:
    if isinstance(v, date) and not isinstance(v, datetime):
        return v
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, str):
        return datetime.strptime(v, "%Y-%m-%d").date()
    raise TypeError(f"can't coerce {v!r} to date")


def _read_time(word_count: int | None) -> int | None:
    """Approx reading time at 230 wpm. Returns None if word_count unknown."""
    if not word_count:
        return None
    return max(1, round(word_count / 230))


def _gather_items() -> list[dict]:
    site = load_site(ROOT)
    items: list[dict] = []

    # 1. Legacy manifest entries
    manifest = ROOT / "data" / "legacy-manifest.yaml"
    if manifest.exists():
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        for p in data.get("posts", []):
            if p.get("status") != "published":
                continue
            lang = p.get("language", "en")
            type_ = p.get("type", "blog")
            slug = p["slug"]
            url = f"/{type_}/{slug}" if lang == "en" else f"/{lang}/{type_}/{slug}"
            cat_slug = p.get("category", "")
            items.append({
                "url": url,
                "title": p["title"],
                "description": p["description"],
                "cover_url": p.get("cover_image_url") or "",
                "section_label": category_label(ROOT, cat_slug, "en") if cat_slug else "Blog",
                "lang_label": LANG_LABEL[lang],
                "language": lang,
                "hreflang": LANG_HREFLANG[lang],
                "published": _coerce_date(p["published"]),
                "modified": _coerce_date(p.get("modified") or p["published"]),
                "read_time": _read_time(p.get("word_count")),
            })

    # 2. Markdown posts under sources/ (published only)
    for post in parse_dir(ROOT / "sources"):
        if post.type != "blog" or post.status != "published":
            continue
        cat_slug = post.category or ""
        items.append({
            "url": url_path(post),
            "title": post.title,
            "description": post.description,
            "cover_url": asset_url(post.cover_image, site.cdn_images_base)
                         if post.cover_image else "",
            "section_label": category_label(ROOT, cat_slug, "en") if cat_slug else "Blog",
            "lang_label": LANG_LABEL[post.language],
            "language": post.language,
            "hreflang": LANG_HREFLANG[post.language],
            "published": post.published,
            "modified": post.modified or post.published,
            "read_time": post.reading_time_min or _read_time(post.word_count),
        })

    # Sort by published date desc, then title
    items.sort(key=lambda x: (x["published"], x["title"]), reverse=True)
    return items


def _build_schemas(site_url: str, page_title: str,
                   page_description: str, items: list[dict],
                   canonical_path: str = "/blogs/") -> list[str]:
    blog_posts = [
        {
            "@type": "BlogPosting",
            "headline": it["title"],
            "url": site_url + it["url"],
            "datePublished": it["published"].isoformat(),
            "inLanguage": it["hreflang"],
        }
        for it in items
    ]
    blog = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": page_title,
        "description": page_description,
        "url": f"{site_url}{canonical_path}",
        "inLanguage": ["en-IN", "hi-IN", "hi-Latn"],
        "publisher": {
            "@type": "Organization",
            "name": "AllCoaching",
            "url": site_url,
            "logo": {
                "@type": "ImageObject",
                "url": f"{site_url}/assets/AllCoaching-logo.webp?v=20260629",
            },
        },
        "blogPost": blog_posts,
    }
    collection = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": f"{site_url}{canonical_path}#webpage",
        "name": page_title,
        "headline": page_title,
        "description": page_description,
        "url": f"{site_url}{canonical_path}",
        "inLanguage": "en-IN",
        "isPartOf": {
            "@type": "WebSite",
            "@id": f"{site_url}/#website",
            "name": "AllCoaching",
            "url": f"{site_url}/",
        },
        "dateModified": max(it["modified"] for it in items).isoformat() if items else date.today().isoformat(),
    }
    breadcrumb_items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{site_url}/"},
        {"@type": "ListItem", "position": 2, "name": "Blogs", "item": f"{site_url}/blogs/"},
    ]
    if canonical_path != "/blogs/":
        # Filter sub-page — add language as 3rd crumb
        lang_name = {"/blogs/en/": "English", "/blogs/hi/": "हिन्दी", "/blogs/hinglish/": "Hinglish"}.get(canonical_path, "Filter")
        breadcrumb_items.append({
            "@type": "ListItem", "position": 3, "name": lang_name,
            "item": f"{site_url}{canonical_path}",
        })
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_items,
    }
    return [
        json.dumps(blog, ensure_ascii=False, separators=(",", ":")),
        json.dumps(collection, ensure_ascii=False, separators=(",", ":")),
        json.dumps(breadcrumb, ensure_ascii=False, separators=(",", ":")),
    ]


def _fmt_date(d: date) -> str:
    """'May 19, 2026' — clean readable format. Windows uses %#d, *nix uses %-d."""
    if sys.platform == "win32":
        return d.strftime("%b %#d, %Y")
    return d.strftime("%b %-d, %Y")


def build_page(filter_key: str) -> str:
    """Render the hub page for the given filter ('all', 'en', 'hi', 'hinglish')."""
    site = load_site(ROOT)
    all_items = _gather_items()
    counts = {
        "total":    len(all_items),
        "en":       sum(1 for i in all_items if i["language"] == "en"),
        "hi":       sum(1 for i in all_items if i["language"] == "hi"),
        "hinglish": sum(1 for i in all_items if i["language"] == "hinglish"),
    }

    cfg = FILTER_PAGES[filter_key]
    meta = FILTER_META[filter_key]
    visible = [it for it in all_items if it["language"] in cfg["languages"]]

    # Add year + formatted display fields, mutate a copy
    items_display = []
    for it in visible:
        d = dict(it)
        d["year"] = it["published"].year
        d["published"] = _fmt_date(it["published"])
        items_display.append(d)

    counts["visible"] = len(visible)

    schemas = _build_schemas(
        site.url, meta["page_title"], meta["page_description"], visible,
        canonical_path=meta["canonical_path"],
    )

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=jinja2.select_autoescape(["html", "j2"]),
        keep_trailing_newline=True,
    )
    tpl = env.get_template("blogs_hub.html.j2")
    return tpl.render(
        site=site,
        canonical=site.url + meta["canonical_path"],
        page_title=meta["page_title"],
        page_description=meta["page_description"],
        pill_label=meta["pill_label"],
        pill_meta=meta["pill_meta"],
        heading_top=meta["heading_top"],
        heading_accent=meta["heading_accent"],
        section_kicker=meta["section_kicker"],
        section_heading_top=meta["section_heading_top"],
        section_heading_accent=meta["section_heading_accent"],
        items=items_display,
        counts=counts,
        active_filter=filter_key,
        empty_state_title=meta.get("empty_state_title", "No posts in this language yet"),
        empty_state_desc=meta.get("empty_state_desc", "Naya content jaldi aayega. Tab tak baaki languages browse karo."),
        schemas=schemas,
        assets_prefix=meta["assets_prefix"],
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true",
                   help="Print the 'all' page to stdout, no files written")
    args = p.parse_args(argv)

    if args.dry_run:
        sys.stdout.buffer.write(build_page("all").encode("utf-8"))
        return 0

    total_bytes = 0
    for key, cfg in FILTER_PAGES.items():
        out = cfg["path"]
        assert_safe(out, action="write")
        html = build_page(key)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        size = out.stat().st_size
        total_bytes += size
        print(f"  wrote  {out.relative_to(ROOT)}  ({size:,} bytes)")
    print(f"Done. {len(FILTER_PAGES)} pages, {total_bytes:,} bytes total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
