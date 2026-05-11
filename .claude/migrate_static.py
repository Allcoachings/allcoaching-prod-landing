"""
Migrate static pages (index, manifesto, about, contact, privacy, terms, 404)
to the new brand system.

Per file:
1. Swap Google Fonts URL from Inter+Plus Jakarta to Instrument Serif+Inter Tight+JetBrains Mono
2. Add <link rel="stylesheet" href="./brand.css" /> after the styles.css link

Idempotent — running twice is safe. Does NOT strip inline <style> blocks
because static pages have page-specific layout that we want preserved;
styles.css and brand.css cascade is enough to swing the palette.
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

STATIC_FILES = ["index.html", "manifesto.html", "about.html", "contact.html",
                "privacy.html", "terms.html", "404.html"]

FONT_OLD = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@700;800;900&display=swap"
FONT_NEW = "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"

STYLES_LINK = '<link rel="stylesheet" href="./styles.css" />'
BRAND_LINK_INSERT = '<link rel="stylesheet" href="./styles.css" />\n  <link rel="stylesheet" href="./brand.css" />'

# Theme color updates (favicon meta)
THEME_SWAPS = [
    ('content="#2563EB" media="(prefers-color-scheme: light)"', 'content="#C58B43" media="(prefers-color-scheme: light)"'),
    ('content="#0B1A3F" media="(prefers-color-scheme: dark)"', 'content="#15110D" media="(prefers-color-scheme: dark)"'),
    ('content="#2563EB"', 'content="#C58B43"'),
]


def migrate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    if FONT_OLD in text:
        text = text.replace(FONT_OLD, FONT_NEW)
        changes.append("swapped Google Fonts URL")

    if "./brand.css" not in text and STYLES_LINK in text:
        text = text.replace(STYLES_LINK, BRAND_LINK_INSERT, 1)
        changes.append("added brand.css link")

    for old, new in THEME_SWAPS:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"swapped theme color")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.name, "changed": True, "actions": changes}
    return {"file": path.name, "changed": False, "actions": []}


def main():
    print(f"Migrating {len(STATIC_FILES)} static pages\n")
    for fname in STATIC_FILES:
        p = REPO / fname
        if not p.exists():
            print(f"  [SKIP] {fname} (not found)")
            continue
        r = migrate(p)
        status = "[OK]" if r["changed"] else "[--]"
        print(f"  {status} {fname}")
        for a in r["actions"]:
            print(f"      - {a}")


if __name__ == "__main__":
    main()
