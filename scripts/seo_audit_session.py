"""SEO audit for the 6 session posts — production-readiness check."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

POSTS = [
    'blogs/hinglish/zero-investment-online-teaching-business-india.html',
    'blogs/hinglish/how-to-start-online-upsc-coaching-from-home.html',
    'blogs/en/why-educators-are-leaving-subscription-platforms.html',
    'blogs/en/graphy-alternative-with-organic-marketplace-traffic.html',
    'blogs/en/best-platforms-for-individual-course-creators-vs-institutes.html',
    'blogs/en/free-coaching-app-for-tutors-with-student-traffic.html',
]


def get(rx, html, group=1):
    m = re.search(rx, html, re.DOTALL)
    return m.group(group) if m else None


def audit_post(rel_path):
    p = ROOT / rel_path
    html = p.read_text(encoding='utf-8')
    issues = []
    warnings = []
    info = {}

    # Title
    title = get(r'<title>(.*?)</title>', html) or ''
    info['title_len'] = len(title)
    info['title'] = title
    if len(title) > 70:
        warnings.append(f'Title {len(title)} chars (Google displays ~600px ~ 60 chars; may truncate)')
    if len(title) < 30:
        issues.append(f'Title too short: {len(title)} chars')

    # Meta description
    desc = get(r'<meta name="description" content="(.*?)"', html) or ''
    info['desc_len'] = len(desc)
    if len(desc) > 320:
        warnings.append(f'Description {len(desc)} chars (long but OK with max-snippet:-1)')
    if len(desc) < 100:
        issues.append(f'Description too short: {len(desc)} chars')

    # Canonical
    canonical = get(r'<link rel="canonical" href="(.*?)"', html) or ''
    info['canonical'] = canonical
    if 'allcoaching.in' not in canonical:
        issues.append(f'Canonical missing or wrong: {canonical}')

    # OG title + image
    og_title = get(r'<meta property="og:title" content="(.*?)"', html) or ''
    og_image = get(r'<meta property="og:image" content="(.*?)"', html) or ''
    og_desc = get(r'<meta property="og:description" content="(.*?)"', html) or ''
    if not og_title:
        issues.append('Missing og:title')
    if not og_image:
        issues.append('Missing og:image')
    if not og_desc:
        issues.append('Missing og:description')

    # Twitter card
    tw_card = get(r'<meta name="twitter:card" content="(.*?)"', html) or ''
    if tw_card != 'summary_large_image':
        warnings.append(f'twitter:card = {tw_card} (expected summary_large_image)')

    # Robots
    robots = get(r'<meta name="robots" content="(.*?)"', html) or ''
    info['robots'] = robots
    if 'index, follow' not in robots:
        issues.append(f'Robots not index-follow: {robots}')
    if 'max-snippet:-1' not in robots:
        warnings.append('Robots missing max-snippet:-1 directive')

    # JSON-LD schemas
    schemas_raw = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', html, re.DOTALL)
    parsed_schemas = []
    for i, s in enumerate(schemas_raw):
        try:
            parsed_schemas.append(json.loads(s))
        except json.JSONDecodeError as e:
            issues.append(f'Schema #{i+1} invalid JSON: {e}')
    info['schema_count'] = len(parsed_schemas)
    schema_types = []
    for s in parsed_schemas:
        t = s.get('@type', '')
        if isinstance(t, list):
            schema_types.extend(t)
        else:
            schema_types.append(t)
    info['schema_types'] = schema_types

    required_types = ['Article', 'FAQPage', 'BreadcrumbList']
    for req in required_types:
        if not any(req in str(t) for t in schema_types):
            issues.append(f'Missing required schema: {req}')

    # FAQ DOM vs schema parity
    dom_faq_questions = re.findall(r'<summary>(.*?)</summary>', html, re.DOTALL)
    info['faq_dom_count'] = len(dom_faq_questions)
    schema_faq = None
    for s in parsed_schemas:
        types = s.get('@type', '')
        if 'FAQPage' in str(types):
            schema_faq = s
            break
    if schema_faq:
        schema_q_count = len(schema_faq.get('mainEntity', []))
        info['faq_schema_count'] = schema_q_count
        if schema_q_count != len(dom_faq_questions):
            issues.append(f'FAQ DOM ({len(dom_faq_questions)}) != schema ({schema_q_count})')

    # Glossary dfn count vs DefinedTermSet
    dom_dfn = re.findall(r'<dfn id="([^"]+)">', html)
    info['dfn_dom_count'] = len(dom_dfn)
    schema_dts = None
    for s in parsed_schemas:
        types = s.get('@type', '')
        if 'DefinedTermSet' in str(types):
            schema_dts = s
            break
    if schema_dts:
        schema_dts_count = len(schema_dts.get('hasDefinedTerm', []))
        info['dts_schema_count'] = schema_dts_count
        if schema_dts_count != len(dom_dfn):
            issues.append(f'Glossary DOM ({len(dom_dfn)}) != DefinedTermSet ({schema_dts_count})')

    # TL;DR block
    if 'id="tldr"' not in html:
        issues.append('Missing #tldr block')

    # Author card inline font enforcement
    if "font-family:'JetBrains Mono'" not in html:
        warnings.append("Author card eyebrow may be missing inline JetBrains Mono font")
    if "font-family:'Fraunces','Instrument Serif'" not in html:
        warnings.append("Author card name may be missing inline Fraunces font")

    # Internal links count
    internal_links = re.findall(r'<a [^>]*href="(/blog/[^"#]+|/blogs/[^"#]+)"', html)
    unique_internal = set(internal_links)
    # Exclude obvious nav/footer/related — count only body links
    body_links = re.findall(r'<a style="text-decoration:none" href="(/blog/[^"#]+|/blogs/[^"#]+)"', html)
    info['internal_link_total'] = len(internal_links)
    info['internal_link_body'] = len(body_links)
    info['internal_link_unique'] = len(unique_internal)
    if len(unique_internal) < 5:
        warnings.append(f'Internal links: only {len(unique_internal)} unique (5+ recommended)')

    # Cover image present
    cover_url_present = 'allcoaching-store.b-cdn.net/blog-images/' in html
    if not cover_url_present:
        issues.append('Cover image URL missing')

    # Schema author has sameAs
    article_schema = None
    for s in parsed_schemas:
        t = s.get('@type', '')
        if 'Article' in str(t):
            article_schema = s
            break
    if article_schema:
        author = article_schema.get('author', {})
        same_as = author.get('sameAs', []) if isinstance(author, dict) else []
        info['author_sameas_count'] = len(same_as)
        if len(same_as) < 3:
            warnings.append(f'Author sameAs: {len(same_as)} entries (3+ recommended for E-E-A-T)')

    # hreflang
    hreflangs = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', html)
    info['hreflangs'] = hreflangs

    # H1 count
    h1_count = len(re.findall(r'<h1[\s>]', html))
    if h1_count != 1:
        issues.append(f'H1 count: {h1_count} (expected 1)')

    # GTM
    if 'GTM-T3KFKD3G' not in html:
        issues.append('GTM tracking missing')

    return info, issues, warnings


def check_sitemap(post_slugs):
    sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    missing = []
    for slug in post_slugs:
        if slug not in sitemap:
            missing.append(slug)
    return missing


def check_llms(post_slugs):
    llms = (ROOT / 'llms.txt').read_text(encoding='utf-8')
    missing = []
    for slug in post_slugs:
        if slug not in llms:
            missing.append(slug)
    return missing


def check_feed(post_slugs):
    feed = (ROOT / 'feed.xml').read_text(encoding='utf-8')
    missing = []
    for slug in post_slugs:
        if slug not in feed:
            missing.append(slug)
    return missing


def main():
    print('='*80)
    print('SEO AUDIT — Session Posts (Production-Ready Check)')
    print('='*80)

    total_issues = 0
    total_warnings = 0

    post_slugs = [Path(p).stem for p in POSTS]

    for rel in POSTS:
        info, issues, warnings = audit_post(rel)
        print(f'\n--- {rel}')
        print(f'  Title ({info["title_len"]} chars): {info["title"][:90]}{"..." if len(info["title"]) > 90 else ""}')
        print(f'  Desc: {info["desc_len"]} chars')
        print(f'  Robots: {info["robots"]}')
        print(f'  Canonical: {info["canonical"]}')
        print(f'  Schemas: {info["schema_count"]} ({", ".join(set(t for t in info["schema_types"] if t))})')
        print(f'  FAQ: DOM {info["faq_dom_count"]} / Schema {info.get("faq_schema_count", "n/a")}')
        print(f'  Glossary: DOM {info["dfn_dom_count"]} / Schema {info.get("dts_schema_count", "n/a")}')
        print(f'  Internal links: {info["internal_link_total"]} total, {info["internal_link_unique"]} unique')
        print(f'  Author sameAs: {info.get("author_sameas_count", "n/a")}')
        print(f'  hreflangs: {info["hreflangs"]}')

        if issues:
            print(f'  ISSUES ({len(issues)}):')
            for i in issues:
                print(f'    ! {i}')
            total_issues += len(issues)
        if warnings:
            print(f'  WARNINGS ({len(warnings)}):')
            for w in warnings:
                print(f'    ~ {w}')
            total_warnings += len(warnings)
        if not issues and not warnings:
            print(f'  CLEAN')

    print('\n' + '='*80)
    print('PRODUCTION INDEX CHECK')
    print('='*80)

    sm_missing = check_sitemap(post_slugs)
    print(f'Sitemap missing: {sm_missing if sm_missing else "all 6 present"}')

    llms_missing = check_llms(post_slugs)
    print(f'llms.txt missing: {llms_missing if llms_missing else "all 6 present"}')

    feed_missing = check_feed(post_slugs)
    print(f'feed.xml missing: {feed_missing if feed_missing else "all 6 present"}')

    if sm_missing: total_issues += len(sm_missing)
    if llms_missing: total_issues += len(llms_missing)
    if feed_missing: total_issues += len(feed_missing)

    print('\n' + '='*80)
    print(f'TOTAL: {total_issues} issues, {total_warnings} warnings')
    print('='*80)

    return 0 if total_issues == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
