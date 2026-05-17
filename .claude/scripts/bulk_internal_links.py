"""Bulk-add Strategic Cross-References block to each blog post.

Inserts a curated 5-8 contextual link block before the related-articles
section in every blog post. Each block uses the target post's primary
keyword as the anchor text (Google's recommended pattern).

Strategy: topic-driven mapping — each post gets links to 5-7 same/adjacent
category posts plus canonical /pricing + /faq references. This brings every
blog post to 8-13 total internal links (target per SKILL.md: 5-10 per post),
strengthening topical authority compounding for AI engines and search.

Insertion anchor: looks for "<!-- ================= RELATED ARTICLES" or
"Related Articles" h2 — places block immediately before.

If anchor not found, inserts before closing </article> or </main>.

Idempotent: skips files that already contain the cross-refs marker.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARKER = '<!-- AUTO: strategic-cross-refs -->'

# Post titles + anchor keywords (anchor text = primary keyword phrase)
POSTS = {
    'how-to-create-landing-page-for-online-course': 'how to create a landing page for an online course',
    'best-upi-payment-gateway-for-online-courses': 'best UPI payment gateway for online courses in India',
    'automated-fee-management-software-for-teachers': 'automated fee management software for teachers',
    'secure-video-hosting-for-educational-content': 'secure video hosting for educational content',
    'white-label-coaching-app-development-cost-india': 'white label coaching app development cost in India',
    'monetize-youtube-teaching-channel-via-personal-app': 'monetize your YouTube teaching channel',
    'how-to-conduct-live-classes-on-mobile-apps': 'how to conduct live classes on mobile apps',
    'budget-home-studio-setup-for-online-teaching': 'budget home studio setup for online teaching',
    'using-chatgpt-for-course-curriculum-design': 'using ChatGPT for course curriculum design',
    'indian-edtech-laws-and-regulations-for-teachers': 'Indian EdTech laws and regulations for teachers',
    'how-to-get-first-500-students-for-coaching-app': 'how to get your first 500 students',
    'seo-strategies-for-online-course-creators': 'SEO strategies for online course creators',
    'best-free-tools-for-teachers-to-record-lectures': 'best free tools for teachers to record lectures',
    'how-to-start-online-academy-in-5-steps': 'how to start an online academy in 5 steps',
    'online-coaching-business-plan-2026': '2026 online coaching business plan',
    'automate-student-onboarding-for-coaching-app': 'automate student onboarding for coaching app',
    'best-platform-for-selling-pdf-notes-and-test-series': 'best platform for selling PDF notes and test series',
    'migrate-offline-coaching-to-online-zero-cost': 'migrate offline coaching to online at zero cost',
    'protect-course-content-from-piracy-for-free': 'protect course content from piracy for free',
    'best-zero-commission-teaching-platform-india': 'zero-commission teaching platform in India',
    'sell-online-courses-without-monthly-subscription': 'sell online courses without monthly subscription',
    'affordable-lms-for-independent-educators': 'most affordable LMS for independent educators',
    'classplus-vs-graphy-vs-allcoaching': 'Classplus vs Graphy vs AllCoaching comparison',
    'edtech-marketplace-india-app-fatigue': 'EdTech marketplace and app fatigue in India',
    'online-coaching-academy-without-coding': 'online coaching academy without coding',
}

# Topic categories → posts (used to pick contextually-related cross-refs)
CATEGORIES = {
    'architecture': ['edtech-marketplace-india-app-fatigue', 'classplus-vs-graphy-vs-allcoaching', 'online-coaching-business-plan-2026'],
    'economics': ['white-label-coaching-app-development-cost-india', 'best-zero-commission-teaching-platform-india', 'affordable-lms-for-independent-educators', 'sell-online-courses-without-monthly-subscription', 'best-upi-payment-gateway-for-online-courses'],
    'operations': ['automated-fee-management-software-for-teachers', 'automate-student-onboarding-for-coaching-app', 'migrate-offline-coaching-to-online-zero-cost', 'how-to-start-online-academy-in-5-steps', 'how-to-get-first-500-students-for-coaching-app', 'best-upi-payment-gateway-for-online-courses', 'how-to-create-landing-page-for-online-course'],
    'infrastructure': ['secure-video-hosting-for-educational-content', 'protect-course-content-from-piracy-for-free', 'how-to-conduct-live-classes-on-mobile-apps', 'best-free-tools-for-teachers-to-record-lectures', 'budget-home-studio-setup-for-online-teaching'],
    'growth': ['monetize-youtube-teaching-channel-via-personal-app', 'best-platform-for-selling-pdf-notes-and-test-series', 'seo-strategies-for-online-course-creators', 'using-chatgpt-for-course-curriculum-design', 'how-to-create-landing-page-for-online-course'],
    'compliance': ['indian-edtech-laws-and-regulations-for-teachers', 'online-coaching-academy-without-coding'],
}

# Map each post → its primary + adjacent categories
POST_CATEGORIES = {
    'how-to-create-landing-page-for-online-course': ['operations', 'growth'],
    'best-upi-payment-gateway-for-online-courses': ['economics', 'operations'],
    'automated-fee-management-software-for-teachers': ['operations', 'economics'],
    'secure-video-hosting-for-educational-content': ['infrastructure', 'compliance'],
    'white-label-coaching-app-development-cost-india': ['economics', 'architecture'],
    'monetize-youtube-teaching-channel-via-personal-app': ['growth', 'architecture'],
    'how-to-conduct-live-classes-on-mobile-apps': ['infrastructure', 'operations'],
    'budget-home-studio-setup-for-online-teaching': ['infrastructure', 'operations'],
    'using-chatgpt-for-course-curriculum-design': ['growth', 'operations'],
    'indian-edtech-laws-and-regulations-for-teachers': ['compliance', 'economics'],
    'how-to-get-first-500-students-for-coaching-app': ['operations', 'growth'],
    'seo-strategies-for-online-course-creators': ['growth', 'architecture'],
    'best-free-tools-for-teachers-to-record-lectures': ['infrastructure', 'operations'],
    'how-to-start-online-academy-in-5-steps': ['operations', 'architecture'],
    'online-coaching-business-plan-2026': ['architecture', 'economics'],
    'automate-student-onboarding-for-coaching-app': ['operations', 'infrastructure'],
    'best-platform-for-selling-pdf-notes-and-test-series': ['growth', 'economics'],
    'migrate-offline-coaching-to-online-zero-cost': ['operations', 'architecture'],
    'protect-course-content-from-piracy-for-free': ['infrastructure', 'compliance'],
    'best-zero-commission-teaching-platform-india': ['economics', 'architecture'],
    'sell-online-courses-without-monthly-subscription': ['economics', 'growth'],
    'affordable-lms-for-independent-educators': ['economics', 'architecture'],
    'classplus-vs-graphy-vs-allcoaching': ['architecture', 'economics'],
    'edtech-marketplace-india-app-fatigue': ['architecture', 'growth'],
    'online-coaching-academy-without-coding': ['compliance', 'operations'],
}

def pick_cross_refs(slug):
    """Pick 6 cross-refs: 3 from primary category + 2 from adjacent + 1 from comparison."""
    cats = POST_CATEGORIES.get(slug, ['architecture'])
    primary_cat = cats[0]
    adjacent_cat = cats[1] if len(cats) > 1 else primary_cat

    primary_picks = [p for p in CATEGORIES[primary_cat] if p != slug][:3]
    adjacent_picks = [p for p in CATEGORIES[adjacent_cat] if p != slug and p not in primary_picks][:2]
    # Add one comparison if not already
    comparison = ['classplus-vs-graphy-vs-allcoaching', 'edtech-marketplace-india-app-fatigue']
    comp_pick = [c for c in comparison if c != slug and c not in primary_picks and c not in adjacent_picks][:1]

    return primary_picks + adjacent_picks + comp_pick

def build_block(slug):
    refs = pick_cross_refs(slug)
    items = []
    for r in refs:
        anchor = POSTS.get(r, r)
        items.append(f'      <li><a href="/blog/{r}">{anchor}</a> — deep dive on the same architectural layer.</li>')

    return f'''
  {MARKER}
  <div class="article-body" id="strategic-cross-refs" style="margin: 3rem 0 1.5rem; padding: 1.5rem 1.75rem; background: linear-gradient(180deg, #FBF6EA 0%, #FFFFFF 100%); border-left: 4px solid #C58B43; border-radius: 0 14px 14px 0; box-shadow: 0 4px 14px -8px rgba(197,139,67,.25);">
    <p style="font-family:'Inter',sans-serif; font-size:.7rem; letter-spacing:.28em; text-transform:uppercase; font-weight:800; color:#C58B43; margin:0 0 0.85rem;">Strategic cross-references</p>
    <p style="margin:0 0 1rem; font-size:15.5px; line-height:1.65; color:#4F4840;">If this essay was useful, these companion pieces extend the same argument — economics, infrastructure, compliance, and discovery across the AllCoaching system.</p>
    <ul style="margin:0 0 1.25rem; padding-left:1.15rem; list-style:disc; font-size:14.5px; line-height:1.85; color:#4F4840;">
{chr(10).join(items)}
    </ul>
    <p style="margin:0; font-family:'JetBrains Mono',monospace; font-size:10.5px; letter-spacing:.14em; font-weight:700; color:#8E5F22; text-transform:uppercase;">
      Also see: <a href="/pricing" style="color:#8E5F22; text-decoration:underline;">Pricing</a> &nbsp;·&nbsp; <a href="/faq" style="color:#8E5F22; text-decoration:underline;">FAQ Hub (40 Q/A)</a> &nbsp;·&nbsp; <a href="/author/amit-ratan" style="color:#8E5F22; text-decoration:underline;">Founder profile</a>
    </p>
  </div>
'''

def process_file(path):
    slug = os.path.basename(path).replace('.html', '')
    if slug not in POSTS:
        return f'SKIP (not in POSTS map)'

    with open(path, 'r', encoding='utf-8') as fp:
        text = fp.read()

    if MARKER in text:
        return 'SKIP (already has marker)'

    block = build_block(slug)

    # Try inserting before related-articles section markers
    anchors = [
        r'(<!-- ===+ Related Articles ===+ -->)',
        r'(<!-- ===+ RELATED ARTICLES ===+ -->)',
        r'(<section[^>]*>\s*<div[^>]*max-w-7xl[^>]*>\s*<p[^>]*class="kicker"[^>]*>More from AllCoaching)',
        r'(<h2[^>]*>Continue\s*<span[^>]*>reading</span></h2>)',
        r'(</article>\s*</main>)',
        r'(</main>)'
    ]

    inserted = False
    for pattern in anchors:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            text = text[:m.start()] + block + '\n  ' + text[m.start():]
            inserted = True
            break

    if not inserted:
        return 'FAIL (no insertion anchor found)'

    with open(path, 'w', encoding='utf-8', newline='\n') as fp:
        fp.write(text)
    return f'OK (added {len(block)}B)'

if __name__ == '__main__':
    blog_files = sorted(glob.glob(os.path.join(ROOT, 'blog', '*.html')))
    blog_files = [f for f in blog_files if not f.endswith('index.html')]

    print(f'Processing {len(blog_files)} blog posts\n')
    for f in blog_files:
        result = process_file(f)
        print(f'  {os.path.basename(f):60s} {result}')
