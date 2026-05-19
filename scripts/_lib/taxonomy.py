"""
Taxonomy validation + lookup.

Loads data/taxonomy.yaml + data/authors.yaml + data/site.yaml once.
Validates that a Post's category/subcategory/tags/author all exist.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import yaml

from .frontmatter import Post


class TaxonomyError(Exception):
    pass


@dataclass
class SiteConfig:
    raw: dict
    @property
    def name(self) -> str: return self.raw["site"]["name"]
    @property
    def url(self) -> str: return self.raw["site"]["url"]
    @property
    def domain(self) -> str: return self.raw["site"]["domain"]
    @property
    def description(self) -> str: return self.raw["site"]["description"]
    @property
    def tagline(self) -> str: return self.raw["site"]["tagline"]
    @property
    def gtm_id(self) -> str: return self.raw["analytics"]["gtm_id"]
    @property
    def cdn_images_base(self) -> str: return self.raw["cdn"]["images_base"]
    @property
    def cover_size(self) -> tuple[int, int]:
        w, h = self.raw["cdn"]["cover_image_size"]
        return int(w), int(h)
    @property
    def languages(self) -> list[dict]: return self.raw["languages"]["available"]
    @property
    def default_language(self) -> str: return self.raw["languages"]["default"]
    @property
    def social(self) -> dict: return self.raw["social"]
    @property
    def contact(self) -> dict: return self.raw["contact"]
    @property
    def ctas(self) -> dict: return self.raw["ctas"]


@lru_cache(maxsize=1)
def load_site(root: Path) -> SiteConfig:
    with open(root / "data" / "site.yaml", encoding="utf-8") as f:
        return SiteConfig(yaml.safe_load(f))


@lru_cache(maxsize=1)
def load_taxonomy(root: Path) -> dict:
    with open(root / "data" / "taxonomy.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@lru_cache(maxsize=1)
def load_authors(root: Path) -> dict[str, dict]:
    with open(root / "data" / "authors.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {a["slug"]: a for a in data["authors"]}


def get_category(root: Path, slug: str) -> dict | None:
    for cat in load_taxonomy(root)["categories"]:
        if cat["slug"] == slug:
            return cat
    return None


def get_subcategory(root: Path, cat_slug: str, sub_slug: str) -> dict | None:
    cat = get_category(root, cat_slug)
    if not cat:
        return None
    for sub in cat.get("subcategories", []):
        if sub["slug"] == sub_slug:
            return sub
    return None


def get_tag(root: Path, slug: str) -> dict | None:
    tax = load_taxonomy(root)
    for _bucket, items in (tax.get("tags") or {}).items():
        for t in items:
            if t["slug"] == slug:
                return t
    return None


def category_label(root: Path, slug: str, lang: str) -> str:
    cat = get_category(root, slug)
    if not cat:
        return slug
    labels = cat.get("label", {})
    return labels.get(lang) or labels.get("en") or slug


def validate_post(root: Path, post: Post) -> list[str]:
    """Return a list of validation errors (empty = OK)."""
    errors: list[str] = []
    if post.author not in load_authors(root):
        errors.append(f"unknown author: '{post.author}'")
    if post.type == "blog":
        if not post.category:
            errors.append("blog posts require 'category'")
        elif not get_category(root, post.category):
            errors.append(f"unknown category: '{post.category}'")
        if post.subcategory and not get_subcategory(
            root, post.category or "", post.subcategory
        ):
            errors.append(
                f"unknown subcategory: '{post.subcategory}' under '{post.category}'"
            )
    for tag in post.tags:
        if not get_tag(root, tag):
            errors.append(f"unknown tag: '{tag}'")
    return errors
