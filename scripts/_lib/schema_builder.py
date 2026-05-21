"""
JSON-LD builder — emits Article, BreadcrumbList, FAQPage schemas matching
the pattern used by the legacy posts. Schema fields that the author wants
hand-tuned (HowTo, DefinedTermSet, SoftwareApplication) can be passed
through frontmatter's `schema_extra` list.
"""
from __future__ import annotations
import json
from pathlib import Path

from .frontmatter import Post
from .paths import HTML_LANG, canonical_url, asset_url
from .taxonomy import (
    SiteConfig, load_authors, load_site, category_label, get_category,
)


def _author_block(author: dict) -> dict:
    return {
        "@id": author["schema_id"],
        "@type": "Person",
        "name": author["name"],
        "jobTitle": author.get("job_title"),
        "worksFor": {"@id": f"{author['url'].rsplit('/author/', 1)[0]}/#organization"},
        "url": author["url"],
        "image": author["image"]
            if author["image"].startswith("http")
            else f"https://allcoaching.in{author['image']}",
        "sameAs": author.get("same_as", []),
    }


def _publisher_block(site: SiteConfig) -> dict:
    return {
        "@type": "Organization",
        "name": site.name,
        "url": site.url,
        "logo": {
            "@type": "ImageObject",
            "url": f"{site.url}/assets/AllCoaching-logo.webp",
            "width": 200, "height": 50,
        },
        "sameAs": [
            site.social["twitter_url"],
            site.social["youtube_url"],
            site.social["instagram_url"],
            site.social["facebook_url"],
            site.social["telegram_url"],
            site.social["play_store_url"],
        ],
    }


def build_article(post: Post, root: Path) -> dict:
    site = load_site(root)
    author = load_authors(root)[post.author]
    cover = asset_url(post.cover_image, site.cdn_images_base) if post.cover_image else None
    cw, ch = site.cover_size

    schema: dict = {
        "@context": "https://schema.org",
        "@type": ["Article", "TechArticle"] if post.type == "blog" else "NewsArticle"
            if post.type == "news" else "Article",
        "headline": post.title,
        "description": post.description,
        "author": _author_block(author),
        "publisher": _publisher_block(site),
        "datePublished": post.published.isoformat(),
        "dateModified": (post.modified or post.published).isoformat(),
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": canonical_url(post, site.url),
        },
        "inLanguage": HTML_LANG[post.language],
        "isPartOf": {
            "@type": "Blog" if post.type == "blog" else "WebSite",
            "@id": f"{site.url}/{post.type}/" if post.type != "page" else site.url,
            "name": f"{site.name} {post.type.title()}" if post.type != "page" else site.name,
        },
    }
    if cover:
        schema["image"] = {
            "@type": "ImageObject", "url": cover,
            "width": cw, "height": ch,
        }
    if post.category:
        cat = get_category(root, post.category)
        if cat:
            schema["articleSection"] = category_label(root, post.category, "en")
    if post.keywords:
        schema["keywords"] = ", ".join(post.keywords)
    if post.word_count:
        schema["wordCount"] = post.word_count
    if post.schema_about:
        schema["about"] = post.schema_about
    if post.schema_mentions:
        schema["mentions"] = post.schema_mentions
    if post.schema_speakable:
        schema["speakable"] = {
            "@type": "SpeakableSpecification",
            "cssSelector": post.schema_speakable,
        }
    if post.schema_audience:
        schema["audience"] = {
            "@type": "Audience",
            "audienceType": post.schema_audience,
        }
    return schema


def build_breadcrumb(post: Post, root: Path) -> dict:
    site = load_site(root)
    items: list[dict] = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{site.url}/"},
    ]
    pos = 2
    if post.type != "page":
        type_label = post.type.title()
        items.append({
            "@type": "ListItem", "position": pos, "name": type_label,
            "item": f"{site.url}/{post.type}/",
        })
        pos += 1
    items.append({
        "@type": "ListItem", "position": pos, "name": post.title,
        "item": canonical_url(post, site.url),
    })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def build_faq(post: Post) -> dict | None:
    if not post.faq:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in post.faq
        ],
    }


def render_all_schemas(post: Post, root: Path) -> list[str]:
    """Return list of JSON-LD strings ready to drop into <script> blocks."""
    blocks: list[dict] = [build_article(post, root), build_breadcrumb(post, root)]
    faq = build_faq(post)
    if faq:
        blocks.append(faq)
    blocks.extend(post.schema_extra or [])
    return [json.dumps(b, ensure_ascii=False, separators=(",", ":")) for b in blocks]
