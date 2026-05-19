"""
Safety Guard — Hard lock on legacy files.

Refuses to touch any file declared in LEGACY_PROTECTED. Used by build.py
and any script that writes to disk. Snapshots baseline hashes so we can
verify nothing changed after a build run.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = ROOT / ".build"
BASELINE_FILE = BUILD_DIR / "legacy-baseline.json"

# ---------------------------------------------------------------------
# LEGACY PROTECTED — these files MUST NOT be modified by the build pipeline.
# Anything listed here will trigger a SafetyError if any script tries to
# write/overwrite/delete it. To "release" a file from protection (e.g. when
# migrating a legacy blog post to markdown), edit this list explicitly.
# ---------------------------------------------------------------------

LEGACY_PROTECTED_DIRS = [
    "assets",
    "dist",
    "author",
    "vs",
    ".claude",
    # NOTE: 'hi' and 'hinglish' were here originally; removed 2026-05-19 when
    # the 2 hinglish posts were migrated to content/hinglish/blog/*.md.
    # The build pipeline now owns these directories.
]

LEGACY_PROTECTED_FILES = [
    # Root marketing pages
    "index.html",
    "about.html",
    "pricing.html",
    "faq.html",
    "contact.html",
    "manifesto.html",
    "press.html",
    "privacy.html",
    "terms.html",
    "404.html",
    # Brand + style + service worker
    "brand.css",
    "styles.css",
    "sw.js",
    "manifest.webmanifest",
    "robots.txt",
    # Verification + misc
    "6bd4d4cb18e72145b1acb8c749fcc075.txt",
    # Apache config (will be augmented via separate mechanism, not overwritten)
    ".htaccess",
]

# Legacy /blog/*.html files are protected by *enumeration*, not glob.
# This snapshot is computed once at module load by scanning the blog dir.
# New posts written by build.py land at /blog/<new-slug>.html (NOT in the
# frozen set) and are therefore allowed; existing 28+ legacy posts are
# permanently frozen — any write attempt to them raises SafetyError.

def _frozen_legacy_blog_files() -> frozenset[str]:
    blog_dir = ROOT / "blog"
    if not blog_dir.is_dir():
        return frozenset()
    return frozenset(
        f"blog/{p.name}" for p in blog_dir.glob("*.html") if p.is_file()
    )


LEGACY_FROZEN_BLOG_FILES = _frozen_legacy_blog_files()


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------

class SafetyError(Exception):
    """Raised when a write would touch a legacy-protected path."""


def is_protected(path: str | Path) -> bool:
    """True if `path` (relative to ROOT) is legacy-protected."""
    p = Path(path)
    if p.is_absolute():
        try:
            p = p.relative_to(ROOT)
        except ValueError:
            return False
    rel = p.as_posix()

    if rel in LEGACY_PROTECTED_FILES:
        return True
    for d in LEGACY_PROTECTED_DIRS:
        if rel == d or rel.startswith(d + "/"):
            return True
    # Only the legacy /blog/*.html files present at module-load are frozen.
    # New posts written to blog/<new-slug>.html are allowed.
    if rel in LEGACY_FROZEN_BLOG_FILES:
        return True
    return False


def assert_safe(path: str | Path, action: str = "write") -> None:
    """Raise SafetyError if `path` is legacy-protected."""
    if is_protected(path):
        raise SafetyError(
            f"REFUSED to {action} legacy-protected path: {path}\n"
            f"To release this file from protection, edit "
            f"scripts/_lib/safety_guard.py explicitly."
        )


def list_legacy_files() -> list[Path]:
    """All legacy-protected files that currently exist on disk."""
    found: list[Path] = []
    # Explicit file list
    for rel in LEGACY_PROTECTED_FILES:
        p = ROOT / rel
        if p.is_file():
            found.append(p)
    # Directories — every file inside
    for d in LEGACY_PROTECTED_DIRS:
        base = ROOT / d
        if base.is_dir():
            for f in base.rglob("*"):
                if f.is_file():
                    found.append(f)
    # Frozen legacy blog HTML files (snapshot at module load)
    for rel in LEGACY_FROZEN_BLOG_FILES:
        p = ROOT / rel
        if p.is_file():
            found.append(p)
    return sorted(set(found))


def _hash_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def capture_baseline() -> dict:
    """Snapshot SHA-256 of every legacy file. Saved to .build/legacy-baseline.json."""
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    snapshot: dict[str, str] = {}
    for f in list_legacy_files():
        snapshot[f.relative_to(ROOT).as_posix()] = _hash_file(f)
    BASELINE_FILE.write_text(json.dumps(snapshot, indent=2, sort_keys=True), encoding="utf-8")
    return snapshot


def verify_against_baseline() -> tuple[list[str], list[str], list[str]]:
    """
    Compare current legacy files against saved baseline.
    Returns (modified, missing, new) — lists of relative paths.
    """
    if not BASELINE_FILE.exists():
        raise FileNotFoundError(
            f"No baseline at {BASELINE_FILE}. Run capture_baseline() first."
        )
    baseline: dict[str, str] = json.loads(BASELINE_FILE.read_text(encoding="utf-8"))
    current = {f.relative_to(ROOT).as_posix(): _hash_file(f) for f in list_legacy_files()}

    modified = sorted([k for k in baseline if k in current and baseline[k] != current[k]])
    missing = sorted([k for k in baseline if k not in current])
    new = sorted([k for k in current if k not in baseline])
    return modified, missing, new


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------

def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python safety_guard.py [snapshot|verify|list]")
        return 2

    cmd = argv[1]

    if cmd == "snapshot":
        snap = capture_baseline()
        print(f"Captured baseline: {len(snap)} legacy files hashed.")
        print(f"Saved to {BASELINE_FILE.relative_to(ROOT)}")
        return 0

    if cmd == "verify":
        try:
            modified, missing, new = verify_against_baseline()
        except FileNotFoundError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        if not modified and not missing:
            print(f"OK — all legacy files byte-identical to baseline ({len(list_legacy_files())} files).")
            if new:
                print(f"Note: {len(new)} new legacy-protected files since baseline (acceptable).")
            return 0
        print("LEGACY VIOLATION:", file=sys.stderr)
        if modified:
            print(f"  Modified ({len(modified)}):", file=sys.stderr)
            for m in modified:
                print(f"    - {m}", file=sys.stderr)
        if missing:
            print(f"  Missing ({len(missing)}):", file=sys.stderr)
            for m in missing:
                print(f"    - {m}", file=sys.stderr)
        return 1

    if cmd == "list":
        files = list_legacy_files()
        print(f"{len(files)} legacy-protected files:")
        for f in files:
            print(f"  {f.relative_to(ROOT).as_posix()}")
        return 0

    print(f"Unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
