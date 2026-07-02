# -*- coding: utf-8 -*-
"""Apply audit fixes:
H1  broken link /blog/using-generative-ai... -> /blogs/en/... (best-ai-tools blog + llms.txt)
H2  author page #essays -> #guides
M2a brand.css/styles.css font-weight 800/900 -> 700 (fonts load max 700)
M2b Instrument Serif faux-bold: brand.css .founder-name 700->400 + inline copies in blogs
M1  CSS cache version: ?v=20260603d -> ?v=20260702 site-wide + version the 4 unversioned pages
Leaves Fraunces pages' own 800/900 alone (Fraunces 900 actually loads there; migration is a separate task).
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
log = []

def edit(path, pairs, must=True):
    t = open(path, encoding="utf-8").read()
    orig = t
    for old, new, count_exp in pairs:
        n = t.count(old)
        if n == 0 and must:
            log.append(f"  !! NOT FOUND in {path}: {old[:70]}")
            continue
        t = t.replace(old, new)
        log.append(f"  {path}: {n}x  {old[:52]!r} -> {new[:40]!r}")
    if t != orig:
        open(path, "w", encoding="utf-8", newline="").write(t)
    return t != orig

print("== H1: broken link fix ==")
edit("blog/best-ai-tools-for-teachers-india.html", [
    ("https://allcoaching.in/blog/using-generative-ai-for-automated-quiz-creation",
     "https://allcoaching.in/blogs/en/using-generative-ai-for-automated-quiz-creation", 1)])
edit("llms.txt", [
    ("allcoaching.in/blog/using-generative-ai-for-automated-quiz-creation",
     "allcoaching.in/blogs/en/using-generative-ai-for-automated-quiz-creation", 1)])

print("== H2: author anchor fix ==")
edit("author/amit-ratan.html", [('<a href="#essays">', '<a href="#guides">', 1)])

print("== M2a: font-weight 800/900 -> 700 in stylesheets ==")
css_repl = []
t = open("brand.css", encoding="utf-8").read()
n8 = len(re.findall(r'font-weight\s*:\s*800\b', t))
n9 = len(re.findall(r'font-weight\s*:\s*900\b', t))
t = re.sub(r'font-weight(\s*):(\s*)(?:800|900)\b', r'font-weight\1:\g<2>700', t)
open("brand.css", "w", encoding="utf-8", newline="").write(t)
print(f"  brand.css: {n8}x 800 + {n9}x 900 -> 700")
t = open("styles.css", encoding="utf-8").read()
n = len(re.findall(r'font-weight\s*:\s*(?:800|900)\b', t))
t = re.sub(r'font-weight(\s*):(\s*)(?:800|900)\b', r'font-weight\1:\g<2>700', t)
open("styles.css", "w", encoding="utf-8", newline="").write(t)
print(f"  styles.css: {n}x -> 700")

print("== M2b: Instrument Serif faux-bold -> 400 ==")
# brand.css .founder-name (Instrument Serif is 400-only)
t = open("brand.css", encoding="utf-8").read()
t2 = t.replace(
    "  font-family:var(--display); font-style:italic; font-weight:700;\n  font-size:clamp(1.95rem, 3.2vw, 2.5rem);",
    "  font-family:var(--display); font-style:italic; font-weight:400;\n  font-size:clamp(1.95rem, 3.2vw, 2.5rem);")
if t2 != t:
    open("brand.css", "w", encoding="utf-8", newline="").write(t2)
    print("  brand.css .founder-name: 700 -> 400")
else:
    print("  !! brand.css .founder-name pattern not found")

# inline copies: any style="...Instrument Serif...font-weight:700..."
pat = re.compile(r'(style="[^"]*Instrument Serif[^"]*?)font-weight:\s*700')
count_files = 0
count_fixes = 0
for f in glob.glob("**/*.html", recursive=True):
    if f.startswith((".claude", ".git")): continue
    t = open(f, encoding="utf-8").read()
    t2, n = pat.subn(lambda m: m.group(1) + "font-weight:400", t)
    if n:
        open(f, "w", encoding="utf-8", newline="").write(t2)
        count_files += 1
        count_fixes += n
print(f"  inline Instrument-Serif 700->400: {count_fixes} fixes across {count_files} files")

print("== M1: CSS cache version bump ==")
bumped_files = 0
for f in glob.glob("**/*.html", recursive=True):
    if f.startswith((".claude", ".git")): continue
    t = open(f, encoding="utf-8").read()
    orig = t
    t = t.replace("?v=20260603d", "?v=20260702")
    # version the unversioned stylesheet refs (author + vs pages)
    for css in ("dist/tw.min.css", "styles.css", "brand.css"):
        t = re.sub(r'href="((?:\.\./)*' + re.escape(css) + r')"', r'href="\1?v=20260702"', t)
    if t != orig:
        open(f, "w", encoding="utf-8", newline="").write(t)
        bumped_files += 1
print(f"  cache-version updated in {bumped_files} files")

print("\n".join(log))
print("\nDONE")
