"""Sync the generated JSON-LD of a v3 (guide-layout) blog post with its visible DOM.

Usage: python .claude/scripts/v3_sync_schema.py blog/<slug>.html

Rebuilds, from the page itself (start from placeholders like {"@type":"FAQPage"}), so schema and DOM can never drift:
  - JSON-LD block typed FAQPage         from  #faq details > summary / p   (verbatim text)
  - JSON-LD block typed HowTo           from  #howto-steps li (b = name, span = text), name = h2 of #steps
  - JSON-LD block typed DefinedTermSet  from  #glossary dt dfn[id] / dd
  - Article wordCount + timeRequired, and every visible ".rt" read-time label (230 wpm)
Idempotent: safe to re-run after every edit.
"""
import json, math, re, sys
from bs4 import BeautifulSoup


def clean(t):
    return re.sub(r'\s+', ' ', t).strip()


def replace_ld(html, sid, obj):
    """Replace the JSON-LD block whose @type matches obj's @type (placeholder or earlier build)."""
    pat = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
    for m in pat.finditer(html):
        try:
            cur = json.loads(m.group(2))
        except ValueError:
            continue
        if cur.get('@type') == obj['@type']:
            return html[:m.start(2)] + '\n  ' + json.dumps(obj, ensure_ascii=False) + '\n  ' + html[m.end(2):]
    sys.exit(f'missing JSON-LD block with "@type":"{obj["@type"]}" ({sid})')


def main(path):
    html = open(path, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    canon = soup.find('link', rel='canonical')['href']

    faq = soup.select('#faq details')
    faq_obj = {"@context": "https://schema.org", "@type": "FAQPage", "@id": canon + '#faq', "mainEntity": [
        {"@type": "Question", "name": clean(d.summary.get_text()),
         "acceptedAnswer": {"@type": "Answer", "text": clean(d.p.get_text())}} for d in faq]}
    html = replace_ld(html, 'ld-faq', faq_obj)

    steps = soup.select('#howto-steps > li')
    h2 = soup.select_one('#steps h2')
    howto = {"@context": "https://schema.org", "@type": "HowTo", "@id": canon + '#howto',
             "name": clean(h2.get_text()) if h2 else 'Steps',
             "description": clean(soup.select_one('#steps p').get_text()) if soup.select_one('#steps p') else '',
             "totalTime": soup.select_one('#howto-steps').get('data-total-time', 'P90D'),
             "step": [{"@type": "HowToStep", "position": i + 1, "name": clean(li.b.get_text()),
                       "text": clean(li.span.get_text()), "url": canon + '#steps'} for i, li in enumerate(steps)]}
    html = replace_ld(html, 'ld-howto', howto)

    gl = soup.select_one('#glossary')
    terms = []
    for dt in gl.select('dt'):
        dfn = dt.find('dfn')
        dd = dt.find_next_sibling('dd')
        terms.append({"@type": "DefinedTerm", "@id": canon + '#' + dfn['id'], "name": clean(dfn.get_text()),
                      "description": clean(dd.get_text()), "inDefinedTermSet": canon + '#glossary'})
    h = gl.find('h2')
    html = replace_ld(html, 'ld-terms', {"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": canon + '#glossary',
                                         "name": clean(h.get_text()) if h else 'Glossary', "hasDefinedTerm": terms})

    art = soup.select_one('article.v3-body')
    for bad in art.select('#references, .v3-author, .v3-toc-m, .v3-sidecta-m, .v3-byline'):
        bad.decompose()
    words = len(clean(art.get_text(' ')).split())
    mins = max(1, math.ceil(words / 230))
    html = re.sub(r'"wordCount":\s*\d+', f'"wordCount":{words}', html, count=1)
    html = re.sub(r'"timeRequired":\s*"PT\d+M"', f'"timeRequired":"PT{mins}M"', html, count=1)
    html = re.sub(r'<span class="rt">[^<]*</span>', f'<span class="rt">{mins} min read</span>', html)

    open(path, 'w', encoding='utf-8').write(html)
    print(f'{path}: FAQ {len(faq)} · HowTo steps {len(steps)} · terms {len(terms)} · {words} words · {mins} min')


if __name__ == '__main__':
    main(sys.argv[1])
