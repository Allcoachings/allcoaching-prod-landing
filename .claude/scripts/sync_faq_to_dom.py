"""Sync FAQPage JSON-LD to match DOM <details>/<summary>/<p> blocks.

For each blog post: parse DOM FAQ entries, parse JSON-LD FAQPage entries.
If DOM has more entries, append missing ones to JSON-LD.
DOM is source of truth.

Strips HTML tags from answer text when copying to JSON-LD.
Escapes JSON quotes/backslashes.
"""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLOG = os.path.join(ROOT, 'blog')

def parse_dom_faqs(content):
    """Return list of (question, answer_plaintext) from DOM."""
    out = []
    # Find FAQ container (could be #faq or class="faq")
    faq_section = re.search(r'id="faq"[^>]*>(.*?)</section>|class="faq"[^>]*>(.*?)</div>', content, re.DOTALL)
    # Actually safer: find all <details>...</details> in the whole document
    details = re.findall(r'<details[^>]*>\s*<summary>(.*?)</summary>\s*<p[^>]*>(.*?)</p>\s*</details>', content, re.DOTALL)
    for q, a in details:
        # Strip HTML tags from q and a
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        q_clean = re.sub(r'\s+', ' ', q_clean)
        a_clean = re.sub(r'<[^>]+>', '', a).strip()
        a_clean = re.sub(r'\s+', ' ', a_clean)
        # Unescape common HTML entities
        for ent, ch in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'), ('&#39;', "'"), ('&nbsp;', ' ')]:
            q_clean = q_clean.replace(ent, ch)
            a_clean = a_clean.replace(ent, ch)
        out.append((q_clean, a_clean))
    return out

def parse_jsonld_faqs(content):
    """Return (script_block_index, faqs_list, script_text) for FAQPage."""
    scripts = list(re.finditer(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', content, re.DOTALL))
    for idx, m in enumerate(scripts):
        try:
            data = json.loads(m.group(1))
        except Exception:
            continue
        if data.get('@type') == 'FAQPage':
            faqs = []
            for q in data.get('mainEntity', []):
                name = q.get('name', '')
                ans = q.get('acceptedAnswer', {}).get('text', '')
                faqs.append((name, ans))
            return idx, faqs, m.group(0), m.start(), m.end(), data
    return None, [], None, None, None, None

def normalize_q(s):
    """Loose normalization for matching."""
    return re.sub(r'[^\w]', '', s.lower())

def sync_file(path):
    name = os.path.splitext(os.path.basename(path))[0]
    content = open(path, 'r', encoding='utf-8').read()

    dom_faqs = parse_dom_faqs(content)
    idx, jl_faqs, script_text, s_start, s_end, jl_data = parse_jsonld_faqs(content)

    if jl_data is None or len(dom_faqs) <= len(jl_faqs):
        return None  # No drift to fix

    jl_qs_norm = {normalize_q(q) for q, a in jl_faqs}

    missing = []
    for dq, da in dom_faqs:
        if normalize_q(dq) not in jl_qs_norm:
            missing.append((dq, da))

    if not missing:
        return None

    # Append missing entries to JSON-LD mainEntity
    new_entities = []
    for dq, da in missing:
        new_entities.append({
            "@type": "Question",
            "name": dq,
            "acceptedAnswer": {"@type": "Answer", "text": da}
        })
    jl_data['mainEntity'].extend(new_entities)

    # Rebuild the script text — preserve outer wrapper
    new_inner = json.dumps(jl_data, separators=(',', ':'), ensure_ascii=False)
    new_script = '<script type="application/ld+json">\n' + new_inner + '\n  </script>'

    new_content = content[:s_start] + new_script + content[s_end:]
    open(path, 'w', encoding='utf-8').write(new_content)

    return (name, len(jl_faqs), len(dom_faqs), len(missing))

files = sorted(glob.glob(os.path.join(BLOG, '*.html')))
files = [f for f in files if 'index.html' not in f]

print("Syncing FAQ JSON-LD to DOM:\n")
print(f"{'Slug':<58} {'Before':<8} {'After':<7} {'Added':<5}")
print('-' * 80)

fixed = 0
for path in files:
    result = sync_file(path)
    if result:
        name, before, after, added = result
        print(f"{name[:58]:<58} {before:<8} {after:<7} {added:<5}")
        fixed += 1

print(f"\nFixed {fixed} files.")
