"""Dedup FAQPage JSON-LD against DOM: remove any JSON-LD Q that doesn't match a DOM <summary> verbatim.

DOM is canonical. After running sync_faq_to_dom.py, near-duplicates may remain
in JSON-LD because normalize was too loose. This script trims back to DOM truth.
"""
import json, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FILES = [
    'edtech-marketplace-india-app-fatigue',
    'migrate-offline-coaching-to-online-zero-cost',
]

def normalize(s):
    s = re.sub(r'<[^>]+>', '', s).strip()
    for ent, ch in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&#39;', "'"), ('&nbsp;', ' ')]:
        s = s.replace(ent, ch)
    return re.sub(r'\s+', ' ', s)

for slug in FILES:
    path = os.path.join(ROOT, 'blog', f'{slug}.html')
    content = open(path, 'r', encoding='utf-8').read()

    dom_qs = [normalize(m) for m in re.findall(r'<summary>(.*?)</summary>', content, re.DOTALL)]

    # Find FAQPage script
    pattern = re.compile(r'<script type="application/ld\+json">\s*(\{[^<]*?"@type":"FAQPage"[^<]*?\})\s*</script>', re.DOTALL)
    m = pattern.search(content)
    if not m:
        print(f"{slug}: no FAQPage found"); continue

    data = json.loads(m.group(1))
    before = len(data['mainEntity'])

    # Keep only entries whose name matches a DOM summary
    new_entities = [q for q in data['mainEntity'] if normalize(q['name']) in dom_qs]
    data['mainEntity'] = new_entities

    after = len(new_entities)
    new_inner = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    new_script = '<script type="application/ld+json">\n' + new_inner + '\n  </script>'

    new_content = content[:m.start()] + new_script + content[m.end():]
    open(path, 'w', encoding='utf-8').write(new_content)
    print(f"{slug}: {before} → {after} questions in JSON-LD (DOM has {len(dom_qs)})")
