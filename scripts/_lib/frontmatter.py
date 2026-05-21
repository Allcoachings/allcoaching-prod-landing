"""
Frontmatter parser — reads YAML-frontmatter Markdown files used by the
content pipeline (content/{lang}/{type}/<slug>.md).

Returns a Post dataclass with validated fields. Hard-fails on missing
required fields so a typo never silently ships to production.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any
import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)

REQUIRED_FIELDS = {
    "slug", "language", "type", "status",
    "author", "title", "description",
    "published",
}

VALID_LANGUAGES = {"en", "hi", "hinglish"}
VALID_TYPES = {"blog", "news", "page"}
VALID_STATUSES = {"draft", "scheduled", "published"}


class FrontmatterError(Exception):
    pass


@dataclass
class Post:
    # ---- required ----
    slug: str
    language: str
    type: str
    status: str
    author: str
    title: str
    description: str
    published: date

    # ---- optional ----
    modified: date | None = None
    category: str | None = None
    subcategory: str | None = None
    tags: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    translation_group: str | None = None
    cover_image: str | None = None
    cover_image_alt: str | None = None
    word_count: int | None = None
    reading_time_min: int | None = None
    # Editorial extras
    kicker: str | None = None
    epigraph: str | None = None
    epigraph_attribution: str | None = None
    # Article schema extras (optional pass-through, hand-tuned by author)
    schema_about: list[dict] = field(default_factory=list)
    schema_mentions: list[dict] = field(default_factory=list)
    schema_speakable: list[str] = field(default_factory=list)
    schema_audience: str | None = None
    schema_extra: list[dict] = field(default_factory=list)
    # FAQ entries (list of {q, a})
    faq: list[dict] = field(default_factory=list)
    # Internal
    body_markdown: str = ""
    source_path: Path | None = None

    def __post_init__(self) -> None:
        if self.language not in VALID_LANGUAGES:
            raise FrontmatterError(
                f"{self.source_path}: invalid language '{self.language}' "
                f"(must be one of {sorted(VALID_LANGUAGES)})"
            )
        if self.type not in VALID_TYPES:
            raise FrontmatterError(
                f"{self.source_path}: invalid type '{self.type}' "
                f"(must be one of {sorted(VALID_TYPES)})"
            )
        if self.status not in VALID_STATUSES:
            raise FrontmatterError(
                f"{self.source_path}: invalid status '{self.status}' "
                f"(must be one of {sorted(VALID_STATUSES)})"
            )
        if self.modified is None:
            self.modified = self.published


def _coerce_date(v: Any, field_name: str, path: Path) -> date:
    if isinstance(v, date) and not isinstance(v, datetime):
        return v
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, str):
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError as e:
            raise FrontmatterError(
                f"{path}: {field_name} '{v}' not in YYYY-MM-DD format"
            ) from e
    raise FrontmatterError(f"{path}: {field_name} has invalid type {type(v).__name__}")


def parse_file(path: Path) -> Post:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise FrontmatterError(
            f"{path}: missing YAML frontmatter (file must start with '---')"
        )
    fm_raw, body = m.group(1), m.group(2)
    try:
        meta = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError as e:
        raise FrontmatterError(f"{path}: frontmatter YAML parse error: {e}") from e

    if not isinstance(meta, dict):
        raise FrontmatterError(f"{path}: frontmatter must be a YAML mapping")

    missing = REQUIRED_FIELDS - set(meta.keys())
    if missing:
        raise FrontmatterError(
            f"{path}: missing required frontmatter fields: {sorted(missing)}"
        )

    meta["published"] = _coerce_date(meta["published"], "published", path)
    if "modified" in meta and meta["modified"] is not None:
        meta["modified"] = _coerce_date(meta["modified"], "modified", path)

    if "tags" in meta and meta["tags"] is None:
        meta["tags"] = []
    if "keywords" in meta and meta["keywords"] is None:
        meta["keywords"] = []

    known_fields = {f.name for f in Post.__dataclass_fields__.values()}
    extra_keys = set(meta.keys()) - known_fields - {"body_markdown", "source_path"}
    if extra_keys:
        raise FrontmatterError(
            f"{path}: unknown frontmatter fields: {sorted(extra_keys)} "
            f"(typo? Add to Post dataclass if intentional)"
        )

    return Post(
        body_markdown=body.strip() + "\n",
        source_path=path,
        **meta,
    )


def parse_dir(root: Path) -> list[Post]:
    posts: list[Post] = []
    for md in sorted(root.rglob("*.md")):
        posts.append(parse_file(md))
    return posts
