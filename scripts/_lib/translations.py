"""
Translation groups — find hreflang siblings for a post across en/hi/hinglish.

A `translation_group: tg-foo` field in frontmatter ties posts together.
Legacy posts also carry this field via data/legacy-manifest.yaml.
"""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import yaml

from .frontmatter import Post
from .paths import HREFLANG, url_path


def collect_groups(
    root: Path, posts: list[Post]
) -> dict[str, dict[str, str]]:
    """
    Returns {translation_group: {language: site_relative_url}}
    Includes both new (markdown) posts and legacy-manifest entries.
    """
    groups: dict[str, dict[str, str]] = defaultdict(dict)

    # 1. New markdown posts (status == published only)
    for p in posts:
        if p.status != "published" or not p.translation_group:
            continue
        groups[p.translation_group][p.language] = url_path(p)

    # 2. Legacy posts from manifest
    manifest_file = root / "data" / "legacy-manifest.yaml"
    if manifest_file.exists():
        with open(manifest_file, encoding="utf-8") as f:
            manifest = yaml.safe_load(f) or {}
        for entry in manifest.get("posts", []):
            tg = entry.get("translation_group")
            if not tg or entry.get("status") != "published":
                continue
            lang = entry.get("language", "en")
            slug = entry["slug"]
            type_ = entry.get("type", "blog")
            if lang == "en":
                groups[tg][lang] = f"/{type_}/{slug}"
            else:
                groups[tg][lang] = f"/{lang}/{type_}/{slug}"

    return dict(groups)


def hreflang_links_for(post: Post, groups: dict[str, dict[str, str]],
                       site_url: str) -> list[dict]:
    """
    Build alternate-language link entries for <link rel="alternate" hreflang>.
    Returns [{hreflang, href}, ...]. Always includes x-default → en variant.
    """
    if not post.translation_group:
        return []
    siblings = groups.get(post.translation_group, {})
    if not siblings:
        return []
    out: list[dict] = []
    base = site_url.rstrip("/")
    for lang, path in siblings.items():
        out.append({"hreflang": HREFLANG[lang], "href": base + path})
    # x-default → English variant if present, else self
    default_path = siblings.get("en") or url_path(post)
    out.append({"hreflang": "x-default", "href": base + default_path})
    return out
