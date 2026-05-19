"""
Inject 301/302 redirects from data/redirects.yaml into .htaccess between
BEGIN-AUTO-REDIRECTS / END-AUTO-REDIRECTS markers.

  - Preserves ALL manual rules in .htaccess (touches only the marker block).
  - Idempotent — repeated runs produce the same output.
  - Inserted right after the "old slugs → new blog slugs" section, before
    the trailing-.html strip block.

This script intentionally bypasses safety_guard for .htaccess because
.htaccess is the documented "augment via separate mechanism" exception
(see safety_guard.py LEGACY_PROTECTED_FILES note).

USAGE:
    python scripts/build_redirects.py             # update .htaccess
    python scripts/build_redirects.py --dry-run   # print the block only
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
HTACCESS = ROOT / ".htaccess"
REDIRECTS_YAML = ROOT / "data" / "redirects.yaml"

BEGIN = "  # BEGIN-AUTO-REDIRECTS — managed by scripts/build_redirects.py (do not edit between markers)"
END = "  # END-AUTO-REDIRECTS"
ANCHOR = "  # Strip trailing .html"   # block goes immediately before this


def _escape_regex_path(p: str) -> str:
    """Strip leading/trailing slashes and escape regex specials.
    Trailing slash matching handled separately via /?$ suffix.
    """
    return re.escape(p.strip("/")).replace(r"\/", "/")


def build_block(redirects: list[dict]) -> str:
    if not redirects:
        return f"{BEGIN}\n  # (no auto-redirects defined)\n{END}"
    lines = [BEGIN]
    for r in redirects:
        frm = _escape_regex_path(r["from"])
        to = r["to"]
        code = r.get("code", 301)
        note = r.get("note", "")
        if note:
            lines.append(f"  # {note}")
        lines.append(f"  RewriteRule ^{frm}/?$ {to} [R={code},L,NE]")
    lines.append(END)
    return "\n".join(lines)


def update_htaccess(text: str, block: str) -> str:
    """Replace existing marker block, or insert before the trailing-.html anchor."""
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL
    )
    if pattern.search(text):
        return pattern.sub(block, text)
    # First-time insertion
    if ANCHOR in text:
        return text.replace(ANCHOR, block + "\n\n" + ANCHOR, 1)
    # Last resort: insert before closing IfModule
    return text.replace("</IfModule>", block + "\n</IfModule>", 1)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    data = yaml.safe_load(REDIRECTS_YAML.read_text(encoding="utf-8"))
    redirects = data.get("redirects") or []
    block = build_block(redirects)

    if args.dry_run:
        sys.stdout.buffer.write(block.encode("utf-8"))
        return 0

    text = HTACCESS.read_text(encoding="utf-8")
    new_text = update_htaccess(text, block)
    if new_text == text:
        print("No change — .htaccess already in sync.")
        return 0
    HTACCESS.write_text(new_text, encoding="utf-8")
    print(f"Wrote {len(redirects)} redirect rule(s) into .htaccess "
          f"between BEGIN/END markers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
