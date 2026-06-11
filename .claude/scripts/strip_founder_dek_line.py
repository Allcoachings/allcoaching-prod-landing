"""One-off cleanup: remove the stray "Founder Amit Ratan ne khud likha." byline
that leaked into Hinglish blog deks / index cards / JSON-LD / llms.txt.

Author attribution already lives in the author-strip + "About the Author" section,
so this trailing sentence is redundant + inconsistent (Hinglish-only). Byte-level
replace to preserve encoding and line endings exactly — only the ASCII phrase moves.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PATTERNS = [
    # Hinglish dek bylines
    b" Founder Amit Ratan ne khud likha.",
    b" Founder ne khud likha.",
    # English dek bylines (same artifact, blog/ + vs/ + llms-full.txt)
    b" Written by the founder, Amit Ratan.",
    b" Written by founder Amit Ratan.",
    # Longer descriptive byline tails (order: longest first, though periods make
    # them non-overlapping with the bare form below)
    b" Founder Amit Ratan ka step-by-step Hinglish playbook.",
    b" Founder Amit Ratan ka practical pricing framework.",
    b" Founder Amit Ratan ne likha.",
    # llms.txt / index-card / faq machine-facing byline tails
    b" Authored by founder Amit Ratan.",
    b" written by founder Amit Ratan for Indian educators in 2026.",
    # Bare trailing byline (literal '.' after Ratan — never matches the longer
    # forms above which have ' ne'/' ka' after Ratan, nor the kept '50+ mentors'
    # experience signal, nor lowercase 'founder' archive/manifesto descriptions)
    b" Founder Amit Ratan.",
]

EXTS = (".html", ".md", ".txt")
SKIP_DIRS = {".git", "node_modules", ".claude"}

total_removed = 0
files_changed = 0

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.endswith(EXTS):
            continue
        path = os.path.join(dirpath, fn)
        with open(path, "rb") as fh:
            data = fh.read()
        removed = 0
        for pat in PATTERNS:
            removed += data.count(pat)
            data = data.replace(pat, b"")
        if removed:
            with open(path, "wb") as fh:
                fh.write(data)
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            print(f"  -{removed:<2} {rel}")
            total_removed += removed
            files_changed += 1

print(f"\nRemoved {total_removed} occurrence(s) across {files_changed} file(s).")
