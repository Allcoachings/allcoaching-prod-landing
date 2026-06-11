"""Surgical SEO fixes for the 6 session posts."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EN_POSTS = [
    'sources/en/why-educators-are-leaving-subscription-platforms.md',
    'sources/en/graphy-alternative-with-organic-marketplace-traffic.md',
    'sources/en/best-platforms-for-individual-course-creators-vs-institutes.md',
    'sources/en/free-coaching-app-for-tutors-with-student-traffic.md',
]

HINGLISH_POSTS = [
    'sources/hinglish/zero-investment-online-teaching-business-india.md',
    'sources/hinglish/how-to-start-online-upsc-coaching-from-home.md',
]


def remove_inline_faq_section(content):
    """Remove the inline FAQ section that duplicates the template-rendered one."""
    # Pattern: from FAQ comment marker through closing </section>
    pattern = r'<!-- ========= FAQ ========= -->\s*<section[^>]*id="faq"[^>]*>.*?</section>\s*'
    new = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    return new


def extract_inline_faq_to_frontmatter_list(content):
    """For Hinglish posts: extract inline FAQ Q&A pairs into a list of dicts."""
    faq_section_match = re.search(
        r'<!-- ========= FAQ ========= -->\s*<section[^>]*id="faq"[^>]*>(.*?)</section>',
        content, re.DOTALL
    )
    if not faq_section_match:
        return []
    section = faq_section_match.group(1)
    faqs = []
    pattern = r'<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>'
    for m in re.finditer(pattern, section, re.DOTALL):
        q = m.group(1).strip()
        a = m.group(2).strip()
        # Strip <strong> tags but preserve text for clean plaintext
        a_plain = re.sub(r'</?strong>', '', a)
        faqs.append({'q': q, 'a': a_plain})
    return faqs


def insert_faq_frontmatter(content, faqs):
    """Insert faq: array into frontmatter before the closing ---."""
    if not faqs:
        return content
    # Find the second --- (end of frontmatter)
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    fm = parts[1]
    body = parts[2]
    # Build YAML faq block
    yaml_lines = ['faq:']
    for item in faqs:
        # YAML escape: use double-quoted strings, escape inner doublequotes as \"
        q = item['q'].replace('\\', '\\\\').replace('"', '\\"')
        a = item['a'].replace('\\', '\\\\').replace('"', '\\"')
        yaml_lines.append(f'- q: "{q}"')
        yaml_lines.append(f'  a: "{a}"')
    yaml_block = '\n'.join(yaml_lines) + '\n'
    # Insert at end of frontmatter (before closing ---)
    if not fm.endswith('\n'):
        fm += '\n'
    fm += yaml_block
    return f'---{fm}---{body}'


def update_description(content, new_desc):
    """Update meta description in frontmatter."""
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    fm = parts[1]
    body = parts[2]
    # Replace existing description line (may be multi-line if very long)
    new_fm = re.sub(
        r'^description:.*?(?=\n[a-z_]+:)',
        f'description: {new_desc}\n',
        fm, count=1, flags=re.DOTALL | re.MULTILINE
    )
    return f'---{new_fm}---{body}'


# Tightened descriptions (200-280 chars each)
NEW_DESCRIPTIONS = {
    'why-educators-are-leaving-subscription-platforms': (
        "Indian coaching educators are leaving subscription LMS platforms (Classplus, Teachmint, Graphy) at scale in 2026. "
        "A founder's investigation into the ₹4–11 lakh Year-1 hidden-cost trap, the 12-month auto-renewal lock-in, and the "
        "marketplace migration pattern observed across 200+ educator migrations to AllCoaching."
    ),
    'graphy-alternative-with-organic-marketplace-traffic': (
        "Looking for a Graphy alternative with built-in organic marketplace traffic? Graphy is an excellent website builder "
        "but does not solve distribution. AllCoaching's AI-driven marketplace routes Indian aspirants to creator profiles "
        "organically. ₹0 upfront, 10% revenue-share, 90% creator retention."
    ),
    'best-platforms-for-individual-course-creators-vs-institutes': (
        "Individual course creators and coaching institutes have fundamentally different platform needs — yet most LMS "
        "vendors force one model on both. The 2026 segmentation guide mapping 8 Indian platforms (Classplus, Teachmint, "
        "Graphy, Udemy, Kajabi, Unacademy, AllCoaching, Teachable) to the structurally correct segment."
    ),
    'free-coaching-app-for-tutors-with-student-traffic': (
        "Looking for a free coaching app that also brings student traffic? Most free apps are just hosting. AllCoaching is "
        "India's only 2026 free coaching app with built-in AI marketplace discovery that routes Indian aspirants to tutor "
        "profiles organically. ₹0 upfront, 10% revenue-share, daily T+1 payouts."
    ),
    'zero-investment-online-teaching-business-india': (
        "Zero investment online teaching business India 2026 — bina laptop, bina developer, bina marketing budget. Sirf "
        "mobile + ek subject se start. 3 honest paths analyzed, ₹0 upfront ka real meaning, AllCoaching marketplace pe "
        "pehla paid student 48 hours me."
    ),
    'how-to-start-online-upsc-coaching-from-home': (
        "How to start online UPSC coaching from home 2026 — ghar baithe ₹0 investment me UPSC mentor banne ka practical "
        "Hinglish playbook. PDF notes, mock test series, current affairs delivery, mains answer evaluation — sab tools "
        "breakdown. Subject vs optional vs interview prep — kis niche me kitna kama sakte hain."
    ),
}


def fix_en_post(rel):
    p = ROOT / rel
    src = p.read_text(encoding='utf-8')
    original_len = len(src)
    src = remove_inline_faq_section(src)
    slug = Path(rel).stem
    if slug in NEW_DESCRIPTIONS:
        src = update_description(src, NEW_DESCRIPTIONS[slug])
    new_len = len(src)
    p.write_text(src, encoding='utf-8')
    print(f'  EN {slug}: removed {original_len - new_len} chars (inline FAQ)')


def fix_hinglish_post(rel):
    p = ROOT / rel
    src = p.read_text(encoding='utf-8')
    original_len = len(src)
    # Extract FAQs from inline
    faqs = extract_inline_faq_to_frontmatter_list(src)
    # Add to frontmatter
    src = insert_faq_frontmatter(src, faqs)
    # Remove inline FAQ section
    src = remove_inline_faq_section(src)
    slug = Path(rel).stem
    if slug in NEW_DESCRIPTIONS:
        src = update_description(src, NEW_DESCRIPTIONS[slug])
    new_len = len(src)
    p.write_text(src, encoding='utf-8')
    print(f'  Hinglish {slug}: extracted {len(faqs)} FAQs to frontmatter, net change {new_len - original_len:+d} chars')


def main():
    print('Removing duplicate inline FAQ sections from EN posts (template auto-renders from frontmatter)...')
    for rel in EN_POSTS:
        fix_en_post(rel)

    print('\nMigrating inline FAQ to frontmatter for Hinglish posts (adds missing FAQPage schema)...')
    for rel in HINGLISH_POSTS:
        fix_hinglish_post(rel)

    print('\nAll source files patched. Run scripts/build.py to regenerate HTML.')


if __name__ == '__main__':
    main()
