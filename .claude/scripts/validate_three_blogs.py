"""Validate the 3 new blogs: JSON-LD parse, FAQ DOM<->FAQPage verbatim, glossary<->DefinedTermSet, structure."""
import re, json, os, html
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

SLUGS = [
    "how-to-teach-yoga-fitness-classes-online-india",
    "online-ugc-net-coaching-platform-for-educators",
]

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

allok = True
for slug in SLUGS:
    p = f"blog/{slug}.html"
    t = open(p, encoding='utf-8').read()
    print(f"\n=== {slug} ===")
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', t, re.S)
    schemas = {}
    for b in blocks:
        try:
            obj = json.loads(b)
        except Exception as e:
            print("  JSON-LD PARSE FAIL:", e); allok = False; continue
        ty = obj.get("@type")
        ty = ty[0] if isinstance(ty, list) else ty
        schemas[ty] = obj
    print("  schemas:", len(blocks), "types:", sorted(schemas.keys()))
    need = {"Article","BreadcrumbList","HowTo","SoftwareApplication","FAQPage","DefinedTermSet"}
    miss = need - set(schemas.keys())
    if miss:
        print("  MISSING SCHEMAS:", miss); allok = False

    # FAQ: DOM <details> vs FAQPage mainEntity
    faq = schemas.get("FAQPage", {})
    me = faq.get("mainEntity", [])
    details = re.findall(r'<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>', t, re.S)
    print("  FAQ schema Qs:", len(me), "| DOM <details>:", len(details))
    if len(me) != len(details):
        print("  FAQ COUNT MISMATCH"); allok = False
    # verbatim match answer text
    dom_map = {strip_tags(q): strip_tags(a) for q, a in details}
    for q in me:
        qn = strip_tags(q["name"])
        ans = strip_tags(q["acceptedAnswer"]["text"])
        if qn not in dom_map:
            print("  FAQ Q not in DOM:", qn[:60]); allok = False
        elif dom_map[qn] != ans:
            print("  FAQ ANSWER MISMATCH for:", qn[:50])
            print("    schema:", ans[:90])
            print("    dom   :", dom_map[qn][:90])
            allok = False

    # Glossary: DefinedTermSet vs <dfn>
    dts = schemas.get("DefinedTermSet", {})
    terms = dts.get("hasDefinedTerm", [])
    dfn_ids = re.findall(r'<dfn id="([^"]+)">', t)
    dts_ids = [d.get("@id","").lstrip("#") for d in terms]
    print("  DefinedTermSet:", len(terms), "| <dfn>:", len(dfn_ids))
    if set(dfn_ids) != set(dts_ids):
        print("  GLOSSARY ID MISMATCH dfn:", dfn_ids, "dts:", dts_ids); allok = False

    # structure
    print("  cross-refs marker:", t.count('AUTO: strategic-cross-refs'),
          "| x-refs-also:", t.count('x-refs-also'),
          "| tldr bullets:", len(re.findall(r'<li><strong>', t.split('id="tldr"')[1].split('</ul>')[0])) if 'id="tldr"' in t else 0)
    print("  lang en-IN:", 'lang="en-IN"' in t,
          "| delayed-GTM:", 'w.__gtm' in t,
          "| versioned-logo:", t.count('fevicon.webp?v=20260629'),
          "| publisher-logo-v:", 'AllCoaching-logo.webp?v=20260629' in t)
    # internal links in body (exclude nav/footer/related/x-refs)
    body = t.split('id="real-problem"')[1].split('<!-- ================= RELATED ARTICLES')[0] if 'id="real-problem"' in t else ""
    inbody = len(re.findall(r'href="https://allcoaching\.in/blog', body)) + len(re.findall(r'href="https://allcoaching\.in/blogs/', body))
    print("  in-body internal links:", inbody)

print("\nALL OK" if allok else "\n*** VALIDATION FAILURES ABOVE ***")
