"""Per-post layout/component linter for AllCoaching blog HTML.

Usage: python .claude/scripts/blog_layout_lint.py blog/<slug>.html

Flags, for one file:
  - Undefined component classes (used in HTML but absent from brand.css + styles.css
    and not a recognized Tailwind utility) -> the #1 cause of "broken cards".
  - Duplicate adjacent HTML comments.
  - JSON-LD parse errors / schema count.
  - Stale visible "Updated <Month> <day>" vs Article dateModified.
  - Unclosed-tag heuristic (rough <div> open/close balance in <main>).
"""
import sys, re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def defined_classes():
    classes = set()
    for fn in ['brand.css', 'styles.css']:
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        css = open(p, encoding='utf-8').read()
        for m in re.finditer(r'\.([A-Za-z_][A-Za-z0-9_-]*)', css):
            classes.add(m.group(1))
    return classes

# Broad Tailwind / utility patterns to ignore (these are provided by tw.min.css)
TW = re.compile(r'''^(
    [a-z]+:.*                              # variants md: hover: lg: etc
    |\[.*\]|.*\[.*\]                        # arbitrary values
    |-?(m|p)[trblxy]?-.+                    # margin/padding
    |(w|h|min-w|max-w|min-h|max-h|size)-.+
    |(text|bg|from|via|to|border|ring|fill|stroke|shadow|rounded|gap|space|inset|top|bottom|left|right|z|opacity|leading|tracking|font|grid|col|row|order|flex|items|justify|content|self|place|object|overflow|whitespace|cursor|select|transition|duration|ease|delay|animate|transform|translate|scale|rotate|skew|origin|backdrop|blur|brightness|aspect|columns|gap|divide|decoration|underline|uppercase|lowercase|capitalize|italic|antialiased|truncate|sr|not-sr|container|block|inline|inline-block|inline-flex|hidden|table|contents|float|clear|isolate|relative|absolute|fixed|sticky|static)(-.+)?
    |(sm|md|lg|xl|2xl)
    |grid-cols-.+|col-span-.+|row-span-.+
    )$''', re.VERBOSE)

def is_utility(cls):
    if TW.match(cls):
        return True
    # numeric/fraction utilities like w-1/2 handled by [.*]; bare tokens:
    if re.match(r'^(flex|grid|block|hidden|relative|absolute|fixed|sticky|static|float-y|antialiased)$', cls):
        return True
    return False

def main(path):
    c = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    print(f"=== {name} ===")

    # JSON-LD
    scripts = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', c, re.DOTALL)
    errs = 0
    for s in scripts:
        try:
            json.loads(s)
        except Exception as e:
            errs += 1
            print(f"  [JSON-LD ERROR] {str(e)[:100]}")
    print(f"  JSON-LD: {len(scripts)} scripts, {errs} parse errors")

    # Undefined component classes
    defined = defined_classes()
    used = {}
    for m in re.finditer(r'class="([^"]+)"', c):
        for tok in m.group(1).split():
            used[tok] = used.get(tok, 0) + 1
    undefined = []
    for cls, n in sorted(used.items()):
        if cls in defined:
            continue
        if is_utility(cls):
            continue
        undefined.append((cls, n))
    if undefined:
        print(f"  [UNDEFINED CLASSES] {len(undefined)} suspicious (verify vs Tailwind):")
        for cls, n in undefined:
            print(f"      .{cls}  x{n}")
    else:
        print("  Undefined component classes: none")

    # Duplicate adjacent comments
    comments = re.findall(r'<!--(.*?)-->', c, re.DOTALL)
    dups = 0
    for m in re.finditer(r'<!--\s*([^>]+?)\s*-->\s*<!--\s*([^>]+?)\s*-->', c):
        a, b = m.group(1).strip(), m.group(2).strip()
        if a.split(':')[0].strip().lower() == b.split(':')[0].strip().lower() or a == b:
            dups += 1
    print(f"  Adjacent duplicate-ish comments: {dups}")

    # Stale visible date vs dateModified
    dm = re.search(r'"dateModified":"(\d{4})-(\d{2})-(\d{2})"', c)
    vis = re.findall(r'Updated\s+([A-Z][a-z]+ \d{1,2},? \d{4})', c)
    print(f"  dateModified: {dm.group(0) if dm else 'none'} | visible 'Updated': {vis if vis else 'none'}")

    # Rough div balance inside <main>
    mblock = re.search(r'<main\b.*?</main>', c, re.DOTALL)
    if mblock:
        seg = mblock.group(0)
        opens = len(re.findall(r'<div\b', seg)) + len(re.findall(r'<section\b', seg))
        closes = len(re.findall(r'</div>', seg)) + len(re.findall(r'</section>', seg))
        flag = '' if opens == closes else '  <-- IMBALANCE'
        print(f"  <main> div+section open={opens} close={closes}{flag}")

if __name__ == '__main__':
    main(sys.argv[1])
