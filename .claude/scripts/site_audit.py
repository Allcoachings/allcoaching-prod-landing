# -*- coding: utf-8 -*-
"""Comprehensive static audit of the AllCoaching marketing site.
Checks: broken internal links (file + fragment), duplicate IDs, img alt/dimensions,
target=_blank rel, JSON-LD parse, meta basics, http:// refs, font-weight>700,
inline event handlers, CSS brace balance + url() assets, and inventories inline JS.
Writes full detail JSON to scratchpad; prints an aggregated summary."""
import os, re, json, html, hashlib, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
SCRATCH = sys.argv[1] if len(sys.argv) > 1 else "."

issues = defaultdict(list)   # category -> list of dicts

def add(cat, file, detail):
    issues[cat].append({"file": file, "detail": detail})

# ---------- inventory ----------
html_files, css_files, js_files = [], [], []
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = [d for d in dirnames if d not in (".git", ".claude", "node_modules")]
    for fn in filenames:
        p = os.path.join(dirpath, fn).replace("\\", "/").lstrip("./")
        if fn.endswith(".html"): html_files.append(p)
        elif fn.endswith(".css"): css_files.append(p)
        elif fn.endswith(".js"): js_files.append(p)

print(f"Inventory: {len(html_files)} HTML, {len(css_files)} CSS, {len(js_files)} JS")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//", "#")

def resolve_internal(base_file, url):
    """Return True if an internal URL resolves to a file (handles extensionless + index)."""
    u = url.split("#")[0].split("?")[0]
    if not u: return True
    if u.startswith("/"):
        cand = u.lstrip("/")
    else:
        cand = os.path.normpath(os.path.join(os.path.dirname(base_file), u)).replace("\\", "/")
    if cand == "" or cand == ".": return True
    for c in (cand, cand + ".html", cand.rstrip("/") + "/index.html", cand.rstrip("/") + ".html"):
        if os.path.isfile(c): return True
    if os.path.isdir(cand): return True
    return False

ID_RE = re.compile(r'\bid="([^"]+)"')
HREF_RE = re.compile(r'(?:href|src)="([^"]+)"')
IMG_RE = re.compile(r'<img\b[^>]*>', re.I)
A_BLANK_RE = re.compile(r'<a\b[^>]*target="_blank"[^>]*>', re.I)
JSONLD_RE = re.compile(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', re.S)
SCRIPT_RE = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', re.S | re.I)
FRAG_RE = re.compile(r'href="#([^"]+)"')
EVENT_RE = re.compile(r'\bon(?:click|mouseover|mouseout|load|error)="')
FW_RE = re.compile(r'font-weight\s*:\s*(800|900)\b')

inline_scripts = {}  # hash -> (code, [files])
allc_abs = re.compile(r'^https://allcoaching\.in(/[^"]*)?$')

for f in html_files:
    try:
        t = open(f, encoding="utf-8").read()
    except Exception as e:
        add("read-error", f, str(e)); continue

    # strip script/style bodies for id/link scans where needed
    t_noscript = re.sub(r'<script\b.*?</script>', lambda m: " " * len(m.group(0)), t, flags=re.S | re.I)

    # --- basics ---
    if '<html' in t and 'lang=' not in t.split('>', 2)[0] + t.split('>', 2)[1] if t.count('>') > 2 else False:
        pass
    mhtml = re.search(r'<html\b[^>]*>', t)
    if mhtml and 'lang=' not in mhtml.group(0):
        add("missing-lang", f, mhtml.group(0)[:60])
    if 'name="viewport"' not in t:
        add("missing-viewport", f, "no viewport meta")
    if 'rel="canonical"' not in t and f not in ("404.html",):
        add("missing-canonical", f, "no canonical link")
    if t.count("<title>") == 0:
        add("missing-title", f, "no <title>")
    elif t.count("<title>") > 1:
        add("dup-title", f, f'{t.count("<title>")} <title> tags')

    # --- duplicate ids (visible DOM only) ---
    ids = ID_RE.findall(t_noscript)
    seen, dups = set(), set()
    for i in ids:
        if i in seen: dups.add(i)
        seen.add(i)
    for d in sorted(dups):
        add("dup-id", f, d)

    # --- links ---
    for url in set(HREF_RE.findall(t)):
        u = html.unescape(url)
        m = allc_abs.match(u)
        if m:
            path = m.group(1) or "/"
            if not resolve_internal(f, path):
                add("broken-link", f, u)
            continue
        if u.startswith(SKIP_SCHEMES):
            if u.startswith("http://"):
                add("http-ref", f, u)
            continue
        if not resolve_internal(f, u):
            add("broken-link", f, u)

    # --- fragment anchors (same-page) ---
    for frag in set(FRAG_RE.findall(t)):
        if f'id="{frag}"' not in t:
            add("broken-fragment", f, "#" + frag)

    # --- images ---
    for tag in IMG_RE.findall(t):
        if ' alt=' not in tag:
            add("img-no-alt", f, tag[:90])
        if ('width=' not in tag or 'height=' not in tag):
            add("img-no-dims", f, tag[:90])

    # --- target=_blank rel ---
    for tag in A_BLANK_RE.findall(t):
        if 'noopener' not in tag and 'noreferrer' not in tag:
            add("blank-no-noopener", f, tag[:110])

    # --- JSON-LD ---
    for block in JSONLD_RE.findall(t):
        try:
            json.loads(block)
        except Exception as e:
            add("jsonld-parse", f, str(e)[:120])

    # --- inline scripts inventory (dedupe) ---
    for code in SCRIPT_RE.findall(t):
        code = code.strip()
        if not code or code.startswith("{"):  # ld+json handled above; type attr filtered below anyway
            continue
        h = hashlib.md5(code.encode()).hexdigest()[:10]
        if h not in inline_scripts:
            inline_scripts[h] = [code, []]
        inline_scripts[h][1].append(f)

    # --- inline event handlers (CSP smell) ---
    n_ev = len(EVENT_RE.findall(t))
    if n_ev:
        add("inline-event-handlers", f, f"{n_ev} on*= handlers")

    # --- font-weight 800/900 ---
    for m in FW_RE.finditer(t):
        add("font-weight-gt700", f, m.group(0))

    # --- Instrument Serif with bold weight (font has only 400) ---
    for m in re.finditer(r"style=\"[^\"]*Instrument Serif[^\"]*\"", t):
        s = m.group(0)
        fw = re.search(r"font-weight\s*:\s*(\d+)", s)
        if fw and int(fw.group(1)) > 400:
            add("instrument-serif-fauxbold", f, f"font-weight:{fw.group(1)} on Instrument Serif (font ships 400 only)")
            break  # once per file

# ---------- CSS ----------
for f in css_files:
    if "tw.min" in f:  # minified tailwind — skip deep checks
        t = open(f, encoding="utf-8", errors="replace").read()
        if t.count("{") != t.count("}"):
            add("css-brace-imbalance", f, f'{{={t.count("{")} }}={t.count("}")}')
        continue
    t = open(f, encoding="utf-8", errors="replace").read()
    if t.count("{") != t.count("}"):
        add("css-brace-imbalance", f, f'{{={t.count("{")} }}={t.count("}")}')
    for m in FW_RE.finditer(t):
        # find selector context (rough)
        start = t.rfind("}", 0, m.start())
        ctx = t[start+1:m.start()]
        sel = ctx.split("{")[0].strip().split("\n")[-1][:60]
        add("font-weight-gt700-css", f, f"{sel} -> {m.group(0)}")
    for m in re.finditer(r'url\((["\']?)([^)"\']+)\1\)', t):
        u = m.group(2)
        if u.startswith(("http", "data:", "//")): continue
        cand = u.lstrip("/") if u.startswith("/") else os.path.normpath(os.path.join(os.path.dirname(f), u)).replace("\\", "/")
        cand = cand.split("?")[0].split("#")[0]
        if not os.path.isfile(cand):
            add("css-missing-asset", f, u)

# ---------- write inline scripts for node --check ----------
os.makedirs(os.path.join(SCRATCH, "js_checks"), exist_ok=True)
manifest = {}
for h, (code, files) in inline_scripts.items():
    p = os.path.join(SCRATCH, "js_checks", f"inline_{h}.js")
    open(p, "w", encoding="utf-8").write(code)
    manifest[h] = {"count": len(files), "sample": files[:3]}
json.dump(manifest, open(os.path.join(SCRATCH, "js_manifest.json"), "w"))
print(f"Inline scripts: {len(inline_scripts)} unique variants written for node --check")

# ---------- summary ----------
json.dump({k: v for k, v in issues.items()}, open(os.path.join(SCRATCH, "audit_detail.json"), "w"), indent=1)
print("\n================ SUMMARY (count by category) ================")
for cat in sorted(issues, key=lambda c: -len(issues[c])):
    files_affected = len(set(x["file"] for x in issues[cat]))
    print(f"{len(issues[cat]):5d} findings | {files_affected:4d} files | {cat}")
    for x in issues[cat][:3]:
        print(f"        e.g. {x['file']}: {x['detail'][:90]}")
print("\nFull detail: audit_detail.json")
