"""
Pass 2 — clean up residual old-brand references after the first migration.

Targets:
- <meta name="theme-color" content="#2563EB" ...>  -> brand ochre
- <meta name="theme-color" content="#0B1A3F" ...>  -> brand warm ink
- <meta name="msapplication-*-color" content="#2563EB"  -> ochre
- Inline style="font-family:'Plus Jakarta Sans';" on CTA buttons -> remove (brand.css handles it)
- bg-white text-blue-700 hover:bg-blue-50 (Tailwind blue CTA pill) -> brand-aligned cream/ink
- border-white/30 (CTA secondary border) -> keep but ensure context is brand-warm
- Remaining hard-coded old palette hex in HTML body (excluding inline SVG illustrations)
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# Target both root html and blog html
TARGETS = list(REPO.glob("*.html")) + list((REPO / "blog").glob("*.html"))

REPLACEMENTS = [
    # Theme color meta tags
    ('<meta name="theme-color" content="#2563EB" media="(prefers-color-scheme: light)" />',
     '<meta name="theme-color" content="#C58B43" media="(prefers-color-scheme: light)" />'),
    ('<meta name="theme-color" content="#0B1A3F" media="(prefers-color-scheme: dark)" />',
     '<meta name="theme-color" content="#15110D" media="(prefers-color-scheme: dark)" />'),
    ('<meta name="msapplication-TileColor" content="#2563EB" />',
     '<meta name="msapplication-TileColor" content="#C58B43" />'),
    ('<meta name="msapplication-navbutton-color" content="#2563EB" />',
     '<meta name="msapplication-navbutton-color" content="#C58B43" />'),

    # Inline Plus Jakarta on CTA buttons -> drop (brand.css now drives via .btn)
    ("style=\"font-family:'Plus Jakarta Sans';\"", ""),
    ('style="font-family:\'Plus Jakarta Sans\';"', ""),

    # Tailwind blue CTA pills inside .verdict
    ("bg-white text-blue-700 font-bold text-sm hover:bg-blue-50 transition-colors",
     "bg-white text-[#15110D] font-bold text-sm hover:bg-[#F5E8D2] transition-colors"),

    # The CTA "Book a Demo" secondary uses border-white/30 + text-white — keep but soften
    # (no change needed — it sits on a dark gradient verdict block which is on-brand)
]


def migrate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []
    for old, new in REPLACEMENTS:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes.append(f"{count}x: {old[:60]}...")
    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.name, "changed": True, "actions": changes}
    return {"file": path.name, "changed": False, "actions": []}


def main():
    print(f"Pass 2 - cleaning {len(TARGETS)} HTML files\n")
    for p in sorted(TARGETS):
        r = migrate(p)
        status = "[OK]" if r["changed"] else "[--]"
        print(f"  {status} {p.relative_to(REPO)}")
        for a in r["actions"]:
            print(f"      - {a}")


if __name__ == "__main__":
    main()
