"""
Bulk migration: rebrand 13 blog files to the new AllCoaching brand system.

For each blog file:
1. Strip the entire inline <style>...</style> block (now lives in brand.css)
2. Swap the Google Fonts URL from Inter+Plus Jakarta to Instrument Serif+Inter Tight+JetBrains Mono
3. Add <link rel="stylesheet" href="../brand.css" /> after the styles.css link
4. Remove inline style="color:#2563EB" overrides on .kicker (now brand-driven)
5. Replace hard-coded primary-blue/green hex in inline style attributes with brand tokens

Idempotent — running twice is safe.
"""
import re
import glob
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BLOG_DIR = REPO / "blog"

FONT_OLD = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@700;800;900&display=swap"
FONT_NEW = "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"

STYLES_LINK = '<link rel="stylesheet" href="../styles.css" />'
BRAND_LINK_INSERT = '<link rel="stylesheet" href="../styles.css" />\n  <link rel="stylesheet" href="../brand.css" />'

# Color swaps for inline style="..." attributes that hard-code the old palette
COLOR_SWAPS = [
    ("color:#2563EB", "color:#8E5F22"),  # primary blue → accent deep ochre
    ("color: #2563EB", "color:#8E5F22"),
    ("background:#2563EB", "background:#C58B43"),
    ("background-color:#2563EB", "background-color:#C58B43"),
    ("#1D4ED8", "#8E5F22"),  # primary 700 → accent deep
    ("#2E9E4A", "#2F8F4E"),  # legacy green → positive
    ("#E63935", "#C44232"),  # legacy red → negative
]


def migrate(path: Path) -> dict:
    """Return summary of what changed."""
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    # 1) Strip inline <style> block (greedy single block per file)
    style_re = re.compile(r"  <style>\n.*?\n  </style>\n\n", flags=re.DOTALL)
    if style_re.search(text):
        text = style_re.sub("", text, count=1)
        changes.append("stripped inline <style>")
    else:
        # Try without leading indent fallback
        style_re2 = re.compile(r"<style>\n.*?\n</style>\n\n", flags=re.DOTALL)
        if style_re2.search(text):
            text = style_re2.sub("", text, count=1)
            changes.append("stripped inline <style> (no-indent variant)")

    # 2) Swap font URL
    if FONT_OLD in text:
        text = text.replace(FONT_OLD, FONT_NEW)
        changes.append("swapped Google Fonts URL")

    # 3) Add brand.css link (idempotent)
    if "../brand.css" not in text and STYLES_LINK in text:
        text = text.replace(STYLES_LINK, BRAND_LINK_INSERT, 1)
        changes.append("added brand.css link")

    # 4) Strip inline color overrides on .kicker (let brand.css drive)
    text = re.sub(
        r'<p class="kicker" style="color:#2563EB;">',
        '<p class="kicker">',
        text,
    )

    # 5) Generic color swaps for any remaining inline hex references
    for old, new in COLOR_SWAPS:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"swapped {old} -> {new}")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.name, "changed": True, "actions": changes}
    return {"file": path.name, "changed": False, "actions": []}


def main():
    blogs = sorted(BLOG_DIR.glob("*.html"))
    print(f"Found {len(blogs)} blog files\n")
    summary = []
    for b in blogs:
        result = migrate(b)
        summary.append(result)
        status = "[OK]" if result["changed"] else "[--]"
        print(f"  {status} {result['file']}")
        for a in result["actions"]:
            print(f"      - {a}")
    changed = sum(1 for r in summary if r["changed"])
    print(f"\n{changed}/{len(summary)} files modified")


if __name__ == "__main__":
    main()
