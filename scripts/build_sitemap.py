"""
Sitemap builder — merges:
  1. data/legacy-manifest.yaml (the 28+ legacy /blog/*.html posts)
  2. sources/{lang}/*.md (new pipeline)
  3. A small set of static surface pages (home, about, pricing, etc.)
into sitemap.xml at project root.

Hreflang alternates are emitted per translation_group.

IMPORTANT: sitemap.xml IS regenerated (it's not in safety_guard's protected
list — that's intentional). To freeze the sitemap, add it to LEGACY_PROTECTED_FILES.

USAGE:
    python scripts/build_sitemap.py             # write sitemap.xml
    python scripts/build_sitemap.py --dry-run   # print to stdout
"""
from __future__ import annotations
import argparse
import sys
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _lib.frontmatter import parse_dir
from _lib.paths import HREFLANG, url_path
from _lib.taxonomy import load_site
from _lib.translations import collect_groups


# Static surface pages — manually curated. Each entry: (path, changefreq, priority).
STATIC_PAGES = [
    ("/",          "weekly",  "1.0"),
    ("/about",     "monthly", "0.8"),
    ("/pricing",   "monthly", "0.9"),
    ("/contact",   "monthly", "0.7"),
    ("/faq",       "monthly", "0.8"),
    ("/manifesto", "yearly",  "0.7"),
    ("/press",     "yearly",  "0.5"),
    ("/privacy",   "yearly",  "0.3"),
    ("/terms",     "yearly",  "0.3"),
    ("/blog/",          "weekly",  "0.9"),
    ("/blogs/",         "weekly",  "0.9"),    # unified trilingual hub
    ("/blogs/en/",      "weekly",  "0.8"),    # English filter
    ("/blogs/hi/",      "monthly", "0.6"),    # Hindi filter (empty state)
    ("/blogs/hinglish/", "weekly",  "0.8"),   # Hinglish filter
]


@dataclass
class SitemapEntry:
    loc: str
    lastmod: str           # ISO 8601 with timezone
    changefreq: str
    priority: str
    image_url: str | None = None
    image_title: str | None = None
    hreflangs: list[dict] | None = None     # [{hreflang, href}]


def _iso_lastmod(d: date | datetime | str | None) -> str:
    if d is None:
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S+05:30")
    if isinstance(d, datetime):
        return d.strftime("%Y-%m-%dT%H:%M:%S+05:30")
    if isinstance(d, date):
        return f"{d.isoformat()}T12:00:00+05:30"
    # String (e.g. from legacy-manifest.yaml)
    s = str(d)
    if "T" in s:
        return s  # already ISO with time
    return f"{s}T12:00:00+05:30"


def _hreflang_for(tg: str | None, groups: dict, site_url: str) -> list[dict] | None:
    if not tg or tg not in groups:
        return None
    base = site_url.rstrip("/")
    return [
        {"hreflang": HREFLANG[lang], "href": base + path}
        for lang, path in groups[tg].items()
    ]


def _legacy_entries(site_url: str, groups: dict) -> list[SitemapEntry]:
    manifest = ROOT / "data" / "legacy-manifest.yaml"
    if not manifest.exists():
        return []
    with open(manifest, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    entries: list[SitemapEntry] = []
    for p in data.get("posts", []):
        if p.get("status") != "published":
            continue
        lang = p.get("language", "en")
        type_ = p.get("type", "blog")
        slug = p["slug"]
        loc = (
            f"{site_url}/{type_}/{slug}" if lang == "en"
            else f"{site_url}/{lang}/{type_}/{slug}"
        )
        entries.append(SitemapEntry(
            loc=loc,
            lastmod=_iso_lastmod(p.get("modified") or p.get("published")),
            changefreq="monthly",
            priority="0.8",
            image_url=p.get("cover_image_url"),
            image_title=p.get("title"),
            hreflangs=_hreflang_for(p.get("translation_group"), groups, site_url),
        ))
    return entries


def _content_entries(site_url: str, groups: dict,
                     posts: list) -> list[SitemapEntry]:
    entries: list[SitemapEntry] = []
    for p in posts:
        entries.append(SitemapEntry(
            loc=site_url.rstrip("/") + url_path(p),
            lastmod=_iso_lastmod(p.modified or p.published),
            changefreq="monthly",
            priority="0.8",
            hreflangs=_hreflang_for(p.translation_group, groups, site_url),
        ))
    return entries


def _static_entries(site_url: str) -> list[SitemapEntry]:
    return [
        SitemapEntry(
            loc=site_url.rstrip("/") + path,
            lastmod=_iso_lastmod(None),
            changefreq=cf,
            priority=pr,
        )
        for path, cf, pr in STATIC_PAGES
    ]


def _xml_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
         .replace("'", "&apos;").replace('"', "&quot;")
    )


def _entry_xml(e: SitemapEntry) -> str:
    lines = [
        "  <url>",
        f"    <loc>{_xml_escape(e.loc)}</loc>",
        f"    <lastmod>{e.lastmod}</lastmod>",
        f"    <changefreq>{e.changefreq}</changefreq>",
        f"    <priority>{e.priority}</priority>",
    ]
    if e.hreflangs:
        for hl in e.hreflangs:
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{hl["hreflang"]}" href="{_xml_escape(hl["href"])}" />'
            )
    if e.image_url:
        lines.append("    <image:image>")
        lines.append(f"      <image:loc>{_xml_escape(e.image_url)}</image:loc>")
        if e.image_title:
            lines.append(f"      <image:title>{_xml_escape(e.image_title)}</image:title>")
        lines.append("    </image:image>")
    lines.append("  </url>")
    return "\n".join(lines)


def build_sitemap() -> str:
    site = load_site(ROOT)
    content_posts = [p for p in parse_dir(ROOT / "sources") if p.status == "published"]
    groups = collect_groups(ROOT, content_posts)

    entries: list[SitemapEntry] = []
    entries.extend(_static_entries(site.url))
    entries.extend(_legacy_entries(site.url, groups))
    entries.extend(_content_entries(site.url, groups, content_posts))

    seen: set[str] = set()
    deduped: list[SitemapEntry] = []
    for e in entries:
        if e.loc in seen:
            continue
        seen.add(e.loc)
        deduped.append(e)

    body = "\n".join(_entry_xml(e) for e in deduped)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset\n'
        '  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '  xmlns:xhtml="http://www.w3.org/1999/xhtml"\n'
        '  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        f'\n  <!-- Auto-generated by scripts/build_sitemap.py @ {datetime.now().isoformat(timespec="seconds")} -->\n'
        f'  <!-- {len(deduped)} URLs ({len(entries) - len(deduped)} duplicates removed) -->\n\n'
        f"{body}\n"
        '\n</urlset>\n'
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    xml = build_sitemap()
    if args.dry_run:
        # Use binary stdout to avoid Windows cp1252 issues with currency / unicode
        sys.stdout.buffer.write(xml.encode("utf-8"))
        return 0
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
