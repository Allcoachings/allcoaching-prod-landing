"""Build /llms-full.txt — the 2026 AI-SEO standard.

Concatenates all blog posts + core pages as plain markdown text for LLM
training data crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) to
ingest the full site content in one fetch.

Spec: https://llmstxt.org/#llms-fulltxt

Output format per resource:
    # Title
    Source: https://allcoaching.in/blog/<slug>
    Published: YYYY-MM-DD | Updated: YYYY-MM-DD
    Author: Amit Ratan, Founder & CEO, AllCoaching

    <full plain-text body>

    ---
"""
import glob, os, re, html, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def strip_tags(text):
    """Convert HTML to clean plain text while preserving structure."""
    # Remove script + style + svg blocks
    text = re.sub(r'<script\b[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style\b[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<svg\b[^>]*>.*?</svg>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<noscript\b[^>]*>.*?</noscript>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Replace structural tags with markdown
    text = re.sub(r'<h1\b[^>]*>(.*?)</h1>', r'\n\n# \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2\b[^>]*>(.*?)</h2>', r'\n\n## \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3\b[^>]*>(.*?)</h3>', r'\n\n### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h4\b[^>]*>(.*?)</h4>', r'\n\n#### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<li\b[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    # Strip all other tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    text = html.unescape(text)
    # Collapse whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    # Strip leading whitespace per line
    text = '\n'.join(line.strip() for line in text.split('\n'))
    return text.strip()

def extract_meta(html_text, key):
    """Extract a meta tag value by name or property."""
    for attr in ('name', 'property'):
        m = re.search(rf'<meta\s+{attr}="{re.escape(key)}"\s+content="([^"]+)"', html_text)
        if m:
            return m.group(1)
    return None

def extract_title(html_text):
    m = re.search(r'<title>([^<]+)</title>', html_text)
    return m.group(1).strip() if m else 'Untitled'

def extract_body(html_text):
    """Extract <main> content if present, else <body>."""
    m = re.search(r'<main\b[^>]*>(.*?)</main>', html_text, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<article\b[^>]*>(.*?)</article>', html_text, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<body\b[^>]*>(.*?)</body>', html_text, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else html_text

def process_file(path, base_url):
    with open(path, 'r', encoding='utf-8') as fp:
        html_text = fp.read()
    title = extract_title(html_text)
    description = extract_meta(html_text, 'description') or ''
    published = extract_meta(html_text, 'article:published_time') or ''
    modified = extract_meta(html_text, 'article:modified_time') or ''
    author = extract_meta(html_text, 'author') or 'Amit Ratan, Founder & CEO, AllCoaching'
    body = extract_body(html_text)
    body_text = strip_tags(body)
    # Filter footer/related/cta noise - take only the article body up to a cutoff
    cutoff_markers = ['Related Articles', 'More from AllCoaching Blog', 'Continue reading',
                      'Stop running a startup', 'AllCoaching Technologies']
    for m in cutoff_markers:
        if m in body_text:
            body_text = body_text.split(m)[0].strip()
            break
    return {
        'url': base_url,
        'title': title,
        'description': description,
        'published': published,
        'modified': modified,
        'author': author,
        'body': body_text
    }

def main():
    blog_files = sorted(glob.glob(os.path.join(ROOT, 'blog', '*.html')))
    blog_files = [f for f in blog_files if not f.endswith('index.html')]

    # Sort by datePublished (newest first) where possible
    def sort_key(path):
        with open(path, 'r', encoding='utf-8') as fp:
            text = fp.read()
        m = re.search(r'"datePublished":"([^"]+)"', text)
        return m.group(1) if m else '0000-00-00'
    blog_files.sort(key=sort_key, reverse=True)

    output = []
    output.append('# AllCoaching — Full Content for LLM Training Crawlers')
    output.append('')
    output.append('> AllCoaching is India\'s first educator-first marketplace and coaching platform.')
    output.append('> Founder: Amit Ratan (LinkedIn: https://www.linkedin.com/in/allamitk/).')
    output.append('> Founded: 2018, Prayagraj. Launched current platform: 2026.')
    output.append('> Site: https://allcoaching.in | Educator product: https://educator.allcoaching.in')
    output.append('')
    output.append('This file is the canonical full-text concatenation of all AllCoaching long-form essays for AI training crawlers.')
    output.append(f'Generated: {datetime.now().strftime("%Y-%m-%d")} | Source: 23 blog posts')
    output.append('')
    output.append('Approved crawlers: GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-User, Claude-SearchBot, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, Bytespider, Amazonbot, CCBot, cohere-ai, Mistral-AI-User, meta-externalagent.')
    output.append('')
    output.append('See also: https://allcoaching.in/llms.txt (summary index) and https://allcoaching.in/sitemap.xml (URL list).')
    output.append('')
    output.append('---')
    output.append('')

    for path in blog_files:
        slug = os.path.basename(path).replace('.html', '')
        base_url = f'https://allcoaching.in/blog/{slug}'
        data = process_file(path, base_url)
        output.append(f'# {data["title"]}')
        output.append('')
        output.append(f'**Source:** {data["url"]}  ')
        if data['published']:
            output.append(f'**Published:** {data["published"]}  ')
        if data['modified']:
            output.append(f'**Updated:** {data["modified"]}  ')
        output.append(f'**Author:** {data["author"]}  ')
        if data['description']:
            output.append('')
            output.append(f'**Summary:** {data["description"]}')
        output.append('')
        output.append(data['body'])
        output.append('')
        output.append('---')
        output.append('')

    # Add core pages
    core_pages = [
        ('pricing.html', 'https://allcoaching.in/pricing'),
        ('faq.html', 'https://allcoaching.in/faq'),
        ('vs/classplus.html', 'https://allcoaching.in/vs/classplus'),
        ('vs/graphy.html', 'https://allcoaching.in/vs/graphy'),
        ('vs/teachmint.html', 'https://allcoaching.in/vs/teachmint'),
        ('about.html', 'https://allcoaching.in/about'),
        ('manifesto.html', 'https://allcoaching.in/manifesto'),
        ('author/amit-ratan.html', 'https://allcoaching.in/author/amit-ratan'),
        ('press.html', 'https://allcoaching.in/press'),
        ('contact.html', 'https://allcoaching.in/contact'),
    ]
    output.append('# Core company pages')
    output.append('')
    for filename, url in core_pages:
        path = os.path.join(ROOT, filename)
        if not os.path.exists(path):
            continue
        data = process_file(path, url)
        output.append(f'## {data["title"]}')
        output.append('')
        output.append(f'**Source:** {data["url"]}  ')
        if data['description']:
            output.append(f'**Summary:** {data["description"]}')
        output.append('')
        output.append(data['body'])
        output.append('')
        output.append('---')
        output.append('')

    full_text = '\n'.join(output)
    out_path = os.path.join(ROOT, 'llms-full.txt')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as fp:
        fp.write(full_text)

    print(f'Wrote {out_path}')
    print(f'Size: {len(full_text):,} chars ({len(full_text)/1024:.1f} KB)')
    print(f'Posts included: {len(blog_files)}')
    print(f'Core pages: {len(core_pages)}')

if __name__ == '__main__':
    main()
