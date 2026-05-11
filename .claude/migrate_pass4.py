"""
Pass 4 — final blue elimination + remaining Plus Jakarta Sans cleanup.

After passes 1-3 the only residuals are:
- Plus Jakarta Sans font references in manifesto.html inline <style>
  and in SVG illustrations inside 4 blog files (educational diagrams)
- Two stubborn light-blue fills in SVG illustrations (#2BA6E0, #0EA5E9)
  used as decorative variety colors among rainbow app icons
- #DCE5F4 (info-soft) in brand.css — light blue token that's no longer used

Strategy:
- Swap ALL Plus Jakarta Sans -> Inter Tight (the brand UI font).
  Display contexts inside SVG don't render Instrument Serif italic
  well at small sizes — Inter Tight Bold reads cleanly as a label.
- Replace #2BA6E0 -> #8E5F22 (deep ochre) and #0EA5E9 -> #92400E
  (warm brown) to preserve illustration variety while removing blue.
- Replace brand.css info-soft -> warm soft tone.

Idempotent.
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGETS = list(REPO.glob("*.html")) + list((REPO / "blog").glob("*.html")) + [
    REPO / "styles.css", REPO / "brand.css",
]
TARGETS = [t for t in TARGETS if t.exists()]

REPLACEMENTS = [
    # Remaining blues in SVG illustrations
    ("#2BA6E0", "#8E5F22"),
    ("#0EA5E9", "#92400E"),
    # info-soft in brand.css
    ("#DCE5F4", "#F4EAD0"),
    # Any leftover plus jakarta
    ("'Plus Jakarta Sans', Inter, sans-serif", "'Inter Tight', sans-serif"),
    ("'Plus Jakarta Sans', sans-serif", "'Inter Tight', sans-serif"),
    ("'Plus Jakarta Sans',Inter,sans-serif", "'Inter Tight',sans-serif"),
    ("'Plus Jakarta Sans',sans-serif", "'Inter Tight',sans-serif"),
    ('"Plus Jakarta Sans, sans-serif"', '"Inter Tight, sans-serif"'),
    ('"Plus Jakarta Sans,sans-serif"', '"Inter Tight,sans-serif"'),
    ('font-family="Plus Jakarta Sans, sans-serif"', 'font-family="Inter Tight, sans-serif"'),
    ('font-family="Plus Jakarta Sans,sans-serif"', 'font-family="Inter Tight,sans-serif"'),
    ('font-family="Plus Jakarta Sans"', 'font-family="Inter Tight, sans-serif"'),
    ("font-family:'Plus Jakarta Sans';", "font-family:'Inter Tight',sans-serif;"),
    ("font-family:'Plus Jakarta Sans'", "font-family:'Inter Tight',sans-serif"),
    ("Plus+Jakarta+Sans", "Inter+Tight"),  # in any URL leftovers
    ("'Plus Jakarta Sans'", "'Inter Tight'"),  # final catch-all
]


def migrate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []
    for old, new in REPLACEMENTS:
        if old in text:
            n = text.count(old)
            text = text.replace(old, new)
            changes.append(f"{n}x  {old[:50]}")
    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.relative_to(REPO), "changed": True, "actions": changes}
    return {"file": path.relative_to(REPO), "changed": False, "actions": []}


def main():
    print(f"Pass 4 - final cleanup across {len(TARGETS)} files\n")
    total = 0
    for p in sorted(TARGETS, key=lambda x: str(x)):
        r = migrate(p)
        status = "[OK]" if r["changed"] else "[--]"
        if r["changed"]:
            total += 1
        print(f"  {status} {r['file']}")
        for a in r["actions"]:
            print(f"      - {a}")
    print(f"\n{total} files modified")


if __name__ == "__main__":
    main()
