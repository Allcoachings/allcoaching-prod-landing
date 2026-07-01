# -*- coding: utf-8 -*-
"""Repoint every LOGIN-labeled link from studio.allcoaching.in/ to studio.allcoaching.in/login.
Only the 4 known login-anchor variants are touched; 'Join Now'/'Join now'/signup links that
share the bare href are left unchanged (they are not login-labeled)."""
import os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OLD = "https://studio.allcoaching.in/"
NEW = "https://studio.allcoaching.in/login"

# Exact login-anchor strings (old -> new). Each is unique and safe.
PAIRS = [
    ('<a href="https://studio.allcoaching.in/" class="login">Log in</a>',
     '<a href="https://studio.allcoaching.in/login" class="login">Log in</a>'),
    ('<a href="https://studio.allcoaching.in/" target="_blank" rel="noopener" class="btn btn-ghost hidden md:inline-flex">Login</a>',
     '<a href="https://studio.allcoaching.in/login" target="_blank" rel="noopener" class="btn btn-ghost hidden md:inline-flex">Login</a>'),
    ('<a href="https://studio.allcoaching.in/" target="_blank" rel="noopener" class="hover:text-[#15110D]">Login</a>',
     '<a href="https://studio.allcoaching.in/login" target="_blank" rel="noopener" class="hover:text-[#15110D]">Login</a>'),
    ('<a href="https://studio.allcoaching.in/">Login</a>',
     '<a href="https://studio.allcoaching.in/login">Login</a>'),
]

files = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
total_files = 0
total_repl = 0
per_pattern = [0, 0, 0, 0]
for f in files:
    t = open(f, encoding="utf-8").read()
    orig = t
    n_file = 0
    for i, (old, new) in enumerate(PAIRS):
        c = t.count(old)
        if c:
            t = t.replace(old, new)
            per_pattern[i] += c
            n_file += c
    if t != orig:
        open(f, "w", encoding="utf-8", newline="\n").write(t)
        total_files += 1
        total_repl += n_file

print(f"Files changed: {total_files}")
print(f"Total login links repointed: {total_repl}")
for i, p in enumerate(PAIRS):
    print(f"  pattern {i+1}: {per_pattern[i]:4d}  ({p[0][:60]}...)")

# safety: confirm no login-labeled anchor still points to bare '/'
import re
left = 0
for f in files:
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<a href="https://studio\.allcoaching\.in/"[^>]*>(Log ?in|Login)</a>', t, re.I):
        left += 1
print(f"\nRemaining login links on bare '/': {left}  (should be 0)")
