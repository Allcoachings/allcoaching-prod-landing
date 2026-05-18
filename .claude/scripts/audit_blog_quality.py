"""Bulk audit: 15-item Quality Gates across all blog posts.

Outputs a markdown table showing pass/fail per gate per post.
Use to identify which posts need retrofits to match 2026 AI-SEO standard.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLOG_DIR = os.path.join(ROOT, 'blog')

INDEX_FILES = {
    'sitemap': os.path.join(ROOT, 'sitemap.xml'),
    'llms':    os.path.join(ROOT, 'llms.txt'),
    'llmsfull':os.path.join(ROOT, 'llms-full.txt'),
    'blogidx': os.path.join(ROOT, 'blog', 'index.html'),
    'feed':    os.path.join(ROOT, 'feed.xml'),
}

def load(p):
    return open(p, 'r', encoding='utf-8').read()

INDEX_CONTENT = {k: load(v) for k, v in INDEX_FILES.items()}

def audit(path):
    name = os.path.splitext(os.path.basename(path))[0]
    c = load(path)
    out = {'slug': name}

    # JSON-LD parse
    scripts = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', c, re.DOTALL)
    parsed = []
    parse_errs = 0
    for s in scripts:
        try:
            parsed.append(json.loads(s))
        except Exception:
            parse_errs += 1

    types = []
    for p in parsed:
        t = p.get('@type', '')
        if isinstance(t, list):
            types.extend(t)
        else:
            types.append(t)

    # Gate 1: 6+ schemas
    out['g1_schemas'] = f"{len(parsed)}/6" + ("✓" if len(parsed) >= 6 and parse_errs == 0 else "✗")
    out['g1_pass'] = len(parsed) >= 6 and parse_errs == 0

    # Find the Article schema for further checks
    article = next((p for p in parsed if 'Article' in (p.get('@type') if isinstance(p.get('@type'), list) else [p.get('@type','')])), {})

    # Gate 2: FAQ DOM = JSON-LD count
    faq_dom = len(re.findall(r'<details>\s*<summary>', c))
    faqpage = next((p for p in parsed if p.get('@type') == 'FAQPage'), None)
    faq_jsonld = len(faqpage.get('mainEntity', [])) if faqpage else 0
    out['g2_faq'] = f"{faq_dom}={faq_jsonld}" if faq_dom == faq_jsonld and faq_dom > 0 else f"{faq_dom}≠{faq_jsonld}"
    out['g2_pass'] = faq_dom == faq_jsonld and faq_dom >= 8

    # Gate 3: Glossary dfn = DefinedTerm
    dfn_dom = len(re.findall(r'<dfn id="dfn-[^"]+">', c))
    dts = next((p for p in parsed if p.get('@type') == 'DefinedTermSet'), None)
    dt_jsonld = len(dts.get('hasDefinedTerm', [])) if dts else 0
    out['g3_gloss'] = f"{dfn_dom}={dt_jsonld}" if dfn_dom == dt_jsonld and dfn_dom > 0 else f"{dfn_dom}≠{dt_jsonld}"
    out['g3_pass'] = dfn_dom == dt_jsonld and dfn_dom >= 6

    # Gate 4: TL;DR with 6+ <li> each with <strong>
    tldr = re.search(r'id="tldr"[^>]*>(.+?)</div>', c, re.DOTALL)
    tldr_lis = 0
    tldr_strong = 0
    if tldr:
        tldr_lis = len(re.findall(r'<li[^>]*>', tldr.group(1)))
        tldr_strong = len(re.findall(r'<li[^>]*>\s*<strong>', tldr.group(1)))
    out['g4_tldr'] = f"{tldr_strong}/{tldr_lis}" if tldr else "✗"
    out['g4_pass'] = bool(tldr) and tldr_lis >= 5 and tldr_strong >= tldr_lis - 1

    # Gate 5: ≥2 inline Q&A blocks
    qna = len(re.findall(r'Question Often Asked|class="def-l">Question', c))
    out['g5_qa'] = str(qna)
    out['g5_pass'] = qna >= 2

    # Gate 6: ≥5 body internal /blog/ links — approx by counting all /blog/ hrefs minus related-articles + cross-refs
    all_blog_links = re.findall(r'href="/blog/([a-z0-9-]+)"', c)
    unique_targets = set(all_blog_links) - {name}
    # rough heuristic: total occurrences - approximate 6 cross-ref + 3 related = body links
    body_link_est = len(all_blog_links) - 9
    out['g6_links'] = f"~{max(0,body_link_est)}({len(unique_targets)}u)"
    out['g6_pass'] = body_link_est >= 5

    # Gate 7: author.sameAs ≥4
    author = article.get('author', {})
    same_as = author.get('sameAs', []) if isinstance(author, dict) else []
    out['g7_auth'] = str(len(same_as))
    out['g7_pass'] = len(same_as) >= 4

    # Gate 8: about[] ≥4, ≥2 Wikipedia
    about = article.get('about', [])
    wiki = sum(1 for a in about if 'wikipedia' in (a.get('sameAs', '') or '').lower())
    out['g8_about'] = f"{len(about)}({wiki}wiki)"
    out['g8_pass'] = len(about) >= 4 and wiki >= 2

    # Gate 9: mentions[] ≥4
    mentions = article.get('mentions', [])
    out['g9_ment'] = str(len(mentions))
    out['g9_pass'] = len(mentions) >= 4

    # Gate 10: speakable cssSelector
    sp = article.get('speakable', {})
    sel = sp.get('cssSelector', []) if isinstance(sp, dict) else []
    has_tldr = any('tldr' in s for s in sel)
    has_faq = any('faq' in s for s in sel)
    out['g10_speak'] = f"{len(sel)}" + (("✓" if has_tldr and has_faq else "✗"))
    out['g10_pass'] = has_tldr and has_faq and len(sel) >= 3

    # Gate 11: registered in 4 indexes
    in_sitemap  = name in INDEX_CONTENT['sitemap']
    in_llms     = name in INDEX_CONTENT['llms']
    in_llmsfull = name in INDEX_CONTENT['llmsfull']
    in_blogidx  = name in INDEX_CONTENT['blogidx']
    in_feed     = name in INDEX_CONTENT['feed']
    reg = sum([in_sitemap, in_llms, in_llmsfull, in_blogidx, in_feed])
    out['g11_idx'] = f"{reg}/5"
    out['g11_pass'] = reg == 5

    # Gate 12: Evidence layer — external expert quote or sup refs
    # Look for .epi blocks with cite NOT containing "Amit Ratan"
    epis = re.findall(r'<div class="epi"[^>]*>.*?<cite>([^<]+)</cite>', c, re.DOTALL)
    ext_quotes = [e for e in epis if 'Amit Ratan' not in e and 'Amit' not in e and 'principle behind' not in e.lower() and 'strategic principle' not in e.lower()]
    sup_refs = len(re.findall(r'<sup><a href="#ref-', c))
    out['g12_evid'] = f"{len(ext_quotes)}q+{sup_refs}r"
    out['g12_pass'] = len(ext_quotes) >= 1 or sup_refs >= 2

    # Gate 13: Experience lines ≥2
    exp_pat = r'(Across the AllCoaching educator base|From the field, 2026|In our analysis of|we have observed|AllCoaching has observed|From three years|We ran the migration|When we ran)'
    exp_count = len(re.findall(exp_pat, c))
    out['g13_exp'] = str(exp_count)
    out['g13_pass'] = exp_count >= 2

    # Gate 14: AI prompt seed — working artifact, skip

    # Gate 15: dateModified present (we treat current = within last 30 days as N/A — just check present and ≥ datePublished)
    dm = article.get('dateModified', '')
    dp = article.get('datePublished', '')
    out['g15_dm'] = dm if dm else "✗"
    out['g15_pass'] = bool(dm) and dm >= dp

    # Also flag grad-text anti-pattern in headings
    grad = len(re.findall(r'<h[12][^>]*>.*?class="grad-text".*?</h[12]>', c, re.DOTALL))
    out['grad'] = grad

    # Newsreader preload
    out['news'] = 'Newsreader' in c[:5000]

    return out

posts = sorted(glob.glob(os.path.join(BLOG_DIR, '*.html')))
posts = [p for p in posts if 'index.html' not in p]

results = [audit(p) for p in posts]

# Print summary
print(f"# Bulk Audit — {len(results)} blog posts")
print()
print(f"Legend: g1=schemas, g2=FAQ, g3=Glossary, g4=TL;DR, g5=Q&A, g6=BodyLinks, g7=Author.sameAs, g8=about[], g9=mentions, g10=Speakable, g11=Indexes, g12=Evidence, g13=Experience, g15=dateMod, grad=grad-text-bugs, news=Newsreader-preloaded")
print()
print(f"{'Slug':<55} {'g1':<5} {'g2':<5} {'g3':<5} {'g4':<5} {'g5':<3} {'g6':<10} {'g7':<3} {'g8':<8} {'g9':<3} {'g10':<5} {'g11':<5} {'g12':<7} {'g13':<3} {'g15':<11} {'grad':<5} {'news':<5}")
print('-' * 200)
for r in results:
    print(f"{r['slug'][:55]:<55} {r['g1_schemas']:<5} {r['g2_faq']:<5} {r['g3_gloss']:<5} {r['g4_tldr']:<5} {r['g5_qa']:<3} {r['g6_links']:<10} {r['g7_auth']:<3} {r['g8_about']:<8} {r['g9_ment']:<3} {r['g10_speak']:<5} {r['g11_idx']:<5} {r['g12_evid']:<7} {r['g13_exp']:<3} {r['g15_dm']:<11} {r['grad']:<5} {str(r['news']):<5}")

# Summary scorecard
print()
print(f"## Gate-pass summary (out of {len(results)} posts)")
gates = ['g1_pass','g2_pass','g3_pass','g4_pass','g5_pass','g6_pass','g7_pass','g8_pass','g9_pass','g10_pass','g11_pass','g12_pass','g13_pass','g15_pass']
labels = ['6+ schemas','FAQ sync','Glossary sync','TL;DR 6 bullets','≥2 inline Q&A','≥5 body links','author.sameAs ≥4','about[] ≥4,≥2 wiki','mentions ≥4','speakable','indexes registered','evidence layer','≥2 experience','dateModified ≥ datePublished']
for g, lab in zip(gates, labels):
    passed = sum(1 for r in results if r[g])
    print(f"  {lab:<30}: {passed}/{len(results)}")

# Anti-pattern summary
print()
print(f"## Anti-patterns")
grad_bugs = [r for r in results if r['grad'] > 0]
no_news = [r for r in results if not r['news']]
print(f"  Posts with grad-text in headings: {len(grad_bugs)}")
for r in grad_bugs: print(f"    - {r['slug']}")
print(f"  Posts missing Newsreader preload: {len(no_news)}")
for r in no_news: print(f"    - {r['slug']}")
