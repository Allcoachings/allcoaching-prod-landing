"""One-off: register the 2 missing-index posts into blog/index.html.

Adds:
1. BlogPosting entries at top of Blog.blogPost[]
2. ItemList entries at top, renumber existing positions, bump numberOfItems
3. Blog cards at top of grid
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH = os.path.join(ROOT, 'blog', 'index.html')

c = open(PATH, 'r', encoding='utf-8').read()

# ---- 1. BlogPosting entries (top of blogPost[]) ----
new_blog_posts = '''      {"@type":"BlogPosting","headline":"How to Create Interactive Mock Tests Online — The 2026 Engagement Playbook for Indian Educators","url":"https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online","datePublished":"2026-05-18"},
      {"@type":"BlogPosting","headline":"Student Progress Tracking & Analytics Tools — The 2026 India Manager's Operational Guide","url":"https://allcoaching.in/blog/student-progress-tracking-analytics-tools-coaching-india","datePublished":"2026-05-18"},
'''

c = c.replace(
    '    "blogPost":[\n      {"@type":"BlogPosting","headline":"Multi-Language LMS',
    '    "blogPost":[\n' + new_blog_posts + '      {"@type":"BlogPosting","headline":"Multi-Language LMS'
)

# ---- 2. ItemList: insert 2 at position 1-2, renumber rest 3-28, bump numberOfItems ----
# numberOfItems: 26 → 28
c = c.replace('"numberOfItems":26,', '"numberOfItems":28,')

# Find the ItemList items block and renumber
def renumber_items(match):
    block = match.group(1)
    # Each line: {"@type":"ListItem","position":N,...}
    lines = block.strip().split('\n')
    new_lines = [
        '      {"@type":"ListItem","position":1,"url":"https://allcoaching.in/blog/how-to-create-interactive-mock-tests-online","name":"How to Create Interactive Mock Tests Online — The 2026 Engagement Playbook"},',
        '      {"@type":"ListItem","position":2,"url":"https://allcoaching.in/blog/student-progress-tracking-analytics-tools-coaching-india","name":"Student Progress Tracking & Analytics Tools — The 2026 India Manager\'s Operational Guide"},',
    ]
    # Renumber existing lines
    for i, line in enumerate(lines):
        original_pos_match = re.search(r'"position":(\d+)', line)
        if original_pos_match:
            new_pos = int(original_pos_match.group(1)) + 2
            new_line = re.sub(r'"position":\d+', f'"position":{new_pos}', line)
            new_lines.append(new_line)
    return '    "itemListElement":[\n' + '\n'.join(new_lines) + '\n    ]'

c = re.sub(
    r'    "itemListElement":\[\n(.*?)\n    \]',
    renumber_items,
    c,
    count=1,
    flags=re.DOTALL
)

# ---- 3. Blog cards at top of grid ----
new_cards = '''    <!-- 01 — How to Create Interactive Mock Tests Online (May 18) -->
    <a href="/blog/how-to-create-interactive-mock-tests-online" class="blog-card" aria-label="Read: How to Create Interactive Mock Tests Online">
      <div class="blog-card-img">
        <img src="https://allcoaching-store.b-cdn.net/blog-images/how-to-create-interactive-mock-tests-online.webp" alt="How to Create Interactive Mock Tests Online — AllCoaching 2026 engagement playbook for Indian educators" loading="lazy" width="1600" height="900" decoding="async" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Test Portal · 2026</span>
        <h3>How to Create Interactive Mock Tests Online</h3>
        <p>Static PDF tests are quietly killing engagement. The 2026 playbook for interactive online mock tests — auto-grading under 2 seconds, AI question generation, live all-India leaderboards, topic-wise analytics, and the test portal that turns testing from a chore into a habit.</p>
        <div class="blog-card-meta"><span>By Amit Ratan</span><span class="dot"></span><span>18 min read</span></div>
        <div class="blog-card-cta">Read playbook</div>
      </div>
    </a>

    <!-- 02 — Student Progress Tracking & Analytics Tools (May 18) -->
    <a href="/blog/student-progress-tracking-analytics-tools-coaching-india" class="blog-card" aria-label="Read: Student Progress Tracking & Analytics Tools for Coaching India">
      <div class="blog-card-img">
        <img src="https://allcoaching-store.b-cdn.net/blog-images/student-progress-tracking-analytics-tools-coaching-india.webp" alt="Student Progress Tracking and Analytics Tools for Coaching India — AllCoaching 2026 manager's guide" loading="lazy" width="1600" height="900" decoding="async" />
      </div>
      <div class="blog-card-body">
        <span class="blog-card-tag">Analytics · 2026</span>
        <h3>Student Progress Tracking &amp; Analytics Tools</h3>
        <p>The longitudinal signals that actually predict exam-day performance — engagement metrics, mastery trajectory, drop-off risk scoring — and the integrated analytics architecture that turns mock-test attempts and content engagement into a retention signal.</p>
        <div class="blog-card-meta"><span>By Amit Ratan</span><span class="dot"></span><span>16 min read</span></div>
        <div class="blog-card-cta">Read guide</div>
      </div>
    </a>

'''

c = c.replace(
    '    <!-- 01 — Multi-Language LMS for Regional Indian Languages (May 17) -->',
    new_cards + '    <!-- 03 — Multi-Language LMS for Regional Indian Languages (May 17) -->'
)

open(PATH, 'w', encoding='utf-8').write(c)
print("blog/index.html updated:")
print("  - 2 BlogPosting entries added at top")
print("  - 2 ItemList entries inserted at positions 1-2, existing renumbered 3-28")
print("  - numberOfItems: 26 → 28")
print("  - 2 blog cards added at top of grid")
