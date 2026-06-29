"""
Build feed.xml — RSS 2.0 feed combining legacy posts + new pipeline posts.

  - Reads data/legacy-manifest.yaml (28 EN legacy posts)
  - Reads sources/*.md (new pipeline posts, published only)
  - Emits clean RSS 2.0 with channel + items sorted newest-first
  - Description comes from frontmatter description / manifest description

USAGE:
    python scripts/build_feed.py             # write feed.xml
    python scripts/build_feed.py --dry-run   # print to stdout
"""
from __future__ import annotations
import argparse
import sys
from datetime import datetime, date, timezone, timedelta
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _lib.frontmatter import parse_dir
from _lib.paths import HTML_LANG, url_path
from _lib.taxonomy import load_site, category_label

OUT = ROOT / "feed.xml"
IST = timezone(timedelta(hours=5, minutes=30))


def _coerce_date(v) -> date:
    if isinstance(v, date) and not isinstance(v, datetime):
        return v
    if isinstance(v, datetime):
        return v.date()
    return datetime.strptime(str(v), "%Y-%m-%d").date()


def _rfc822(d: date) -> str:
    """RFC 822 date format for RSS pubDate (e.g. 'Tue, 19 May 2026 12:00:00 +0530')."""
    dt = datetime.combine(d, datetime.min.time().replace(hour=12), tzinfo=IST)
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def _xml_escape(s: str) -> str:
    if not s:
        return ""
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&apos;"))


def _gather_items() -> list[dict]:
    items: list[dict] = []

    # Legacy manifest
    manifest = ROOT / "data" / "legacy-manifest.yaml"
    if manifest.exists():
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        for p in data.get("posts", []):
            if p.get("status") != "published":
                continue
            lang = p.get("language", "en")
            type_ = p.get("type", "blog")
            slug = p["slug"]
            url = (f"/{type_}/{slug}" if lang == "en"
                   else f"/{lang}/{type_}/{slug}")
            items.append({
                "title": p["title"],
                "url": url,
                "description": p["description"],
                "pub_date": _coerce_date(p["published"]),
                "language": lang,
                "html_lang": HTML_LANG.get(lang, "en-IN"),
                "category": category_label(ROOT, p.get("category", ""), "en")
                            if p.get("category") else "Blog",
                "image_url": p.get("cover_image_url"),
            })

    # Markdown sources
    for post in parse_dir(ROOT / "sources"):
        if post.type != "blog" or post.status != "published":
            continue
        site = load_site(ROOT)
        cover_filename = post.cover_image or ""
        if cover_filename and not cover_filename.startswith("http"):
            image_url = f"{site.cdn_images_base}/{cover_filename}"
        else:
            image_url = cover_filename
        items.append({
            "title": post.title,
            "url": url_path(post),
            "description": post.description,
            "pub_date": post.published,
            "language": post.language,
            "html_lang": HTML_LANG.get(post.language, "en-IN"),
            "category": category_label(ROOT, post.category or "", "en")
                        if post.category else "Blog",
            "image_url": image_url,
        })

    # Sort by pub_date desc
    items.sort(key=lambda x: x["pub_date"], reverse=True)
    return items


def build_feed() -> str:
    site = load_site(ROOT)
    items = _gather_items()
    site_url = site.url
    now = datetime.now(IST).strftime("%a, %d %b %Y %H:%M:%S %z")

    item_xml = []
    for it in items:
        url = site_url + it["url"]
        enc = f'    <enclosure url="{_xml_escape(it["image_url"])}" type="image/webp" length="0" />\n' if it["image_url"] else ""
        item_xml.append(
            "  <item>\n"
            f'    <title>{_xml_escape(it["title"])}</title>\n'
            f'    <link>{_xml_escape(url)}</link>\n'
            f'    <guid isPermaLink="true">{_xml_escape(url)}</guid>\n'
            f'    <description>{_xml_escape(it["description"])}</description>\n'
            f'    <pubDate>{_rfc822(it["pub_date"])}</pubDate>\n'
            f'    <dc:creator>Amit Ratan</dc:creator>\n'
            f'    <dc:language>{it["html_lang"]}</dc:language>\n'
            f'    <category>{_xml_escape(it["category"])}</category>\n'
            f"{enc}"
            "  </item>"
        )
    items_block = "\n".join(item_xml)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:sy="http://purl.org/rss/1.0/modules/syndication/">
  <channel>
    <title>{_xml_escape(site.name)} Blog — Long-form Guides on the Future of Online Education in India</title>
    <link>{site_url}/blogs/</link>
    <atom:link href="{site_url}/feed.xml" rel="self" type="application/rss+xml" />
    <description>{_xml_escape(site.description)}</description>
    <language>en-IN</language>
    <copyright>© {datetime.now().year} {_xml_escape(site.raw["site"]["legal_name"])}</copyright>
    <managingEditor>{_xml_escape(site.contact["email"])} (Amit Ratan)</managingEditor>
    <webMaster>{_xml_escape(site.contact["email"])} (Amit Ratan)</webMaster>
    <pubDate>{now}</pubDate>
    <lastBuildDate>{now}</lastBuildDate>
    <category>Education</category>
    <category>EdTech</category>
    <category>India</category>
    <generator>AllCoaching feed builder · scripts/build_feed.py</generator>
    <docs>https://www.rssboard.org/rss-specification</docs>
    <ttl>1440</ttl>
    <image>
      <url>{site_url}/assets/AllCoaching-logo.webp?v=20260629</url>
      <title>{_xml_escape(site.name)}</title>
      <link>{site_url}/</link>
      <width>200</width>
      <height>50</height>
    </image>
{items_block}
  </channel>
</rss>
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    xml = build_feed()
    if args.dry_run:
        sys.stdout.buffer.write(xml.encode("utf-8"))
        return 0
    OUT.write_text(xml, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} "
          f"({OUT.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
