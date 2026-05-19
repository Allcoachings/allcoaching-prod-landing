"""
Build llms.txt — concise AI-discovery TOC for AllCoaching content.

  Merge strategy: preserves the rich per-post descriptions that already exist
  in llms.txt for legacy posts (those are hand-curated, multi-paragraph).
  For NEW posts not yet in the file, appends with the short frontmatter
  description. This way:
    - Existing rich content is NEVER overwritten.
    - URLs that have moved (e.g. hinglish migration) are updated in place.
    - Missing entries are added.

USAGE:
    python scripts/build_llms.py             # update llms.txt in place
    python scripts/build_llms.py --dry-run   # show diff summary
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _lib.frontmatter import parse_dir
from _lib.paths import url_path
from _lib.taxonomy import load_site

LLMS_FILE = ROOT / "llms.txt"
ENTRY_RE = re.compile(
    r"^- \[(?P<title>[^\]]+)\]\((?P<url>[^)]+)\):\s*(?P<desc>.+)$",
    re.MULTILINE,
)


def _gather_known() -> dict[str, dict]:
    """Return {slug: {url, title, description}} from manifest + sources."""
    out: dict[str, dict] = {}
    site = load_site(ROOT)

    manifest = ROOT / "data" / "legacy-manifest.yaml"
    if manifest.exists():
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        for p in data.get("posts", []):
            if p.get("status") != "published":
                continue
            lang = p.get("language", "en")
            type_ = p.get("type", "blog")
            slug = p["slug"]
            url = (f"{site.url}/{type_}/{slug}" if lang == "en"
                   else f"{site.url}/{lang}/{type_}/{slug}")
            out[slug] = {
                "title": p["title"],
                "url": url,
                "description": p["description"],
            }

    for post in parse_dir(ROOT / "sources"):
        if post.type != "blog" or post.status != "published":
            continue
        out[post.slug] = {
            "title": post.title,
            "url": site.url + url_path(post),
            "description": post.description,
        }
    return out


def _slug_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def update_llms(text: str, known: dict[str, dict]) -> tuple[str, list[str], list[str]]:
    """Merge known posts into existing llms.txt.

    Rules:
      - If a slug exists in llms.txt: update URL (only), preserve description.
      - If a slug is missing: append a new entry with short description.

    Returns: (new_text, updated_slugs, added_slugs)
    """
    updated: list[str] = []
    added: list[str] = []

    # Find all existing entries
    existing = {}
    for m in ENTRY_RE.finditer(text):
        slug = _slug_from_url(m.group("url"))
        existing[slug] = m

    # Update URLs in place for slugs that are known
    def _replace(m: re.Match) -> str:
        slug = _slug_from_url(m.group("url"))
        if slug not in known:
            return m.group(0)
        k = known[slug]
        if k["url"] != m.group("url"):
            updated.append(slug)
            return f"- [{m.group('title')}]({k['url']}): {m.group('desc')}"
        return m.group(0)

    new_text = ENTRY_RE.sub(_replace, text)

    # Append missing entries
    missing_slugs = [s for s in known if s not in existing]
    if missing_slugs:
        appended_lines = ["\n## Recently added\n"]
        for slug in missing_slugs:
            k = known[slug]
            appended_lines.append(f"- [{k['title']}]({k['url']}): {k['description']}")
            added.append(slug)
        if not new_text.endswith("\n"):
            new_text += "\n"
        new_text += "\n".join(appended_lines) + "\n"

    return new_text, updated, added


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    text = LLMS_FILE.read_text(encoding="utf-8")
    known = _gather_known()
    new_text, updated, added = update_llms(text, known)

    if args.dry_run:
        print(f"Would update {len(updated)} entries:")
        for s in updated: print(f"  - {s}")
        print(f"Would add {len(added)} entries:")
        for s in added: print(f"  + {s}")
        return 0

    if new_text == text:
        print("No change — llms.txt already in sync.")
        return 0

    LLMS_FILE.write_text(new_text, encoding="utf-8")
    print(f"Wrote llms.txt: {len(updated)} URLs updated, {len(added)} entries appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
