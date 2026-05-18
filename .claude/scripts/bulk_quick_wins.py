"""Bulk Quick Wins: idempotent fixes across all blog posts.

Fixes applied:
1. <span class="grad-text">X</span>  →  <em>X</em>   (ONLY inside <h1>/<h2>/<h3>)
2. Add Newsreader to Google Fonts preload <link> if missing

Skips files where the fix is already applied. Safe to re-run.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLOG = os.path.join(ROOT, 'blog')

# Pattern A: grad-text inside h1/h2/h3 only
HEADING_RE = re.compile(r'(<h[123][^>]*>)(.*?)(</h[123]>)', re.DOTALL)
SPAN_RE = re.compile(r'<span class="grad-text">([^<]+)</span>')

# Pattern B: Newsreader preload
OLD_FONT = 'family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono'
NEW_FONT = 'family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,700&family=JetBrains+Mono'

def fix_heading_grad(content):
    """Replace grad-text spans inside h1/h2/h3 only."""
    def replace(m):
        opener, inner, closer = m.group(1), m.group(2), m.group(3)
        new_inner = SPAN_RE.sub(r'<em>\1</em>', inner)
        return opener + new_inner + closer
    return HEADING_RE.sub(replace, content)

def fix_newsreader_preload(content):
    """Inject Newsreader into Google Fonts URL if missing."""
    if 'Newsreader' in content[:6000]:
        return content
    return content.replace(OLD_FONT, NEW_FONT)

files = sorted(glob.glob(os.path.join(BLOG, '*.html')))
files = [f for f in files if 'index.html' not in f]

print(f"Scanning {len(files)} blog posts...\n")
print(f"{'Slug':<55} {'grad→em':<10} {'+Newsreader':<12}")
print('-' * 80)

for path in files:
    name = os.path.splitext(os.path.basename(path))[0]
    orig = open(path, 'r', encoding='utf-8').read()
    new = orig

    new = fix_heading_grad(new)
    grad_changed = new != orig

    after_grad = new
    new = fix_newsreader_preload(new)
    news_changed = new != after_grad

    if new != orig:
        open(path, 'w', encoding='utf-8').write(new)

    g = 'yes' if grad_changed else '-'
    n = 'yes' if news_changed else '-'
    print(f"{name[:55]:<55} {g:<10} {n:<12}")

print("\nDone.")
