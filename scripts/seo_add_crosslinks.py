"""Insert one additional contextual cross-link per post to reach 5+ unique internal links."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Map: source_post → (search_text_in_body, replacement_with_link)
# Each replacement adds ONE new contextual cross-link with keyword-phrase anchor text
PATCHES = {
    'sources/hinglish/zero-investment-online-teaching-business-india.md': [
        (
            'Real Hinglish Guide" — trust signal',
            None  # placeholder; we will use distinct edits below
        )
    ],
    'sources/hinglish/how-to-start-online-upsc-coaching-from-home.md': [],
    'sources/en/why-educators-are-leaving-subscription-platforms.md': [],
    'sources/en/graphy-alternative-with-organic-marketplace-traffic.md': [],
    'sources/en/best-platforms-for-individual-course-creators-vs-institutes.md': [],
    'sources/en/free-coaching-app-for-tutors-with-student-traffic.md': [],
}

# Direct surgical patches — each adds one or two new contextual cross-links
# in a paragraph where the anchor text fits naturally
SURGICAL = [
    (
        'sources/hinglish/zero-investment-online-teaching-business-india.md',
        'Yeh model dominate isliye kar raha hai',
        '<a style="text-decoration:none" href="/blogs/en/free-coaching-app-for-tutors-with-student-traffic">free coaching app with built-in student traffic</a> model dominate isliye kar raha hai',
    ),
    (
        'sources/hinglish/zero-investment-online-teaching-business-india.md',
        'Year-2 me established educators ₹2-8L/month tak ja rahe hain',
        'Year-2 me established educators ₹2-8L/month tak ja rahe hain — kyunki <a style="text-decoration:none" href="/blogs/en/best-platforms-for-individual-course-creators-vs-institutes">creator-segment platform fit</a> compounding deta hai',
    ),
    (
        'sources/hinglish/how-to-start-online-upsc-coaching-from-home.md',
        'Across the AllCoaching UPSC mentor base, <strong>mentors jo 4-tier funnel ko strict follow karte hain',
        'Across the <a style="text-decoration:none" href="/blogs/en/free-coaching-app-for-tutors-with-student-traffic">AllCoaching free tutor app</a> UPSC mentor base, <strong>mentors jo 4-tier funnel ko strict follow karte hain',
    ),
    (
        'sources/hinglish/how-to-start-online-upsc-coaching-from-home.md',
        'AllCoaching ke marketplace + toolkit ne is gap',
        '<a style="text-decoration:none" href="/blogs/en/why-educators-are-leaving-subscription-platforms">AllCoaching ke marketplace + toolkit</a> ne is gap',
    ),
    (
        'sources/en/why-educators-are-leaving-subscription-platforms.md',
        'these all become profit-maximising investments.',
        'these all become profit-maximising investments. The same alignment is why <a style="text-decoration:none" href="/blogs/en/free-coaching-app-for-tutors-with-student-traffic">free coaching apps with built-in student traffic</a> exist as a structural category in 2026.',
    ),
    (
        'sources/en/why-educators-are-leaving-subscription-platforms.md',
        'reflects this structural insight, not vendor dissatisfaction.',
        'reflects this structural insight, not vendor dissatisfaction. The <a style="text-decoration:none" href="/blogs/en/best-platforms-for-individual-course-creators-vs-institutes">creator-vs-institute segmentation</a> guide develops the related structural framework.',
    ),
    (
        'sources/en/graphy-alternative-with-organic-marketplace-traffic.md',
        'Graphy structurally cannot solve this bottleneck because website quality does not produce traffic.',
        'Graphy structurally cannot solve this bottleneck because website quality does not produce traffic. The same logic applies to most <a style="text-decoration:none" href="/blogs/en/why-educators-are-leaving-subscription-platforms">subscription LMS platforms creators are leaving</a> in 2026.',
    ),
    (
        'sources/en/graphy-alternative-with-organic-marketplace-traffic.md',
        'Graphy fits, AllCoaching does not. Legitimate strategic choice.',
        'Graphy fits, AllCoaching does not. Legitimate strategic choice. The <a style="text-decoration:none" href="/blogs/en/best-platforms-for-individual-course-creators-vs-institutes">creator-vs-institute segmentation</a> guide develops the boundary cases further.',
    ),
    (
        'sources/en/best-platforms-for-individual-course-creators-vs-institutes.md',
        'Cross-segment platforms (AllCoaching) are the structurally cleanest answer',
        '<a style="text-decoration:none" href="/blogs/en/free-coaching-app-for-tutors-with-student-traffic">Cross-segment platforms with built-in student traffic</a> (AllCoaching) are the structurally cleanest answer',
    ),
    (
        'sources/en/best-platforms-for-individual-course-creators-vs-institutes.md',
        'AllCoaching is one of the few platforms in 2026 India explicitly architected with dual-mode capability',
        '<a style="text-decoration:none" href="/blogs/en/graphy-alternative-with-organic-marketplace-traffic">AllCoaching is one of the few platforms in 2026 India</a> explicitly architected with dual-mode capability',
    ),
    (
        'sources/en/free-coaching-app-for-tutors-with-student-traffic.md',
        'Most other free apps for tutors (or freemium offerings',
        'Most other <a style="text-decoration:none" href="/blogs/en/graphy-alternative-with-organic-marketplace-traffic">free apps for tutors</a> (or freemium offerings',
    ),
    (
        'sources/en/free-coaching-app-for-tutors-with-student-traffic.md',
        'AllCoaching has institute-mode for this — different operational surface',
        'AllCoaching has <a style="text-decoration:none" href="/blogs/en/best-platforms-for-individual-course-creators-vs-institutes">institute-mode for this</a> — different operational surface',
    ),
]


def apply():
    by_file = {}
    for (rel, search, replace) in SURGICAL:
        by_file.setdefault(rel, []).append((search, replace))

    for rel, patches in by_file.items():
        p = ROOT / rel
        src = p.read_text(encoding='utf-8')
        applied = 0
        for (search, replace) in patches:
            if search in src:
                src = src.replace(search, replace, 1)
                applied += 1
            else:
                print(f'  WARN: search text not found in {rel}: "{search[:60]}..."')
        p.write_text(src, encoding='utf-8')
        print(f'  {rel}: {applied}/{len(patches)} cross-links inserted')


if __name__ == '__main__':
    apply()
