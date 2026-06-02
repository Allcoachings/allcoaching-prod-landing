"""Build /feed.xml — RSS 2.0 feed of all 23 blog posts.

Generates a standards-compliant RSS feed for reader audiences (Feedly,
NetNewsWire, Substack-style readers) and for search engine signal
boost. RSS feed URLs are picked up by Google as additional discovery
surface.

Posts are sorted by datePublished descending (newest first).
Rebuild via: python .claude/scripts/build_feed_xml.py
"""
import glob, os, re, html
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def extract_meta(html_text, key):
    for attr in ('name', 'property'):
        m = re.search(rf'<meta\s+{attr}="{re.escape(key)}"\s+content="([^"]+)"', html_text)
        if m:
            return m.group(1)
    return None

def extract_title(html_text):
    m = re.search(r'<title>([^<]+)</title>', html_text)
    return m.group(1).strip() if m else 'Untitled'

def date_to_rfc822(date_str):
    """Convert YYYY-MM-DD to RFC 822 (e.g., Sat, 16 May 2026 10:00:00 +0530)."""
    if not date_str:
        return ''
    try:
        d = datetime.strptime(date_str[:10], '%Y-%m-%d')
        d = d.replace(tzinfo=timezone.utc)
        return d.strftime('%a, %d %b %Y %H:%M:%S +0000')
    except Exception:
        return ''

def xml_escape(text):
    return html.escape(text or '', quote=False)

def main():
    # Scan both the legacy /blog/ tree and the /blogs/en/ tree.
    sources = [
        (os.path.join(ROOT, 'blog', '*.html'), 'https://allcoaching.in/blog/'),
        (os.path.join(ROOT, 'blogs', 'en', '*.html'), 'https://allcoaching.in/blogs/en/'),
    ]

    posts = []
    seen = set()
    for pattern, url_prefix in sources:
        for path in sorted(glob.glob(pattern)):
            if path.endswith('index.html'):
                continue
            slug = os.path.basename(path).replace('.html', '')
            if slug in seen:
                continue
            seen.add(slug)
            with open(path, 'r', encoding='utf-8') as fp:
                text = fp.read()
            m = re.search(r'"datePublished":"([^"]+)"', text)
            pub_date = m.group(1) if m else '2026-01-01'
            m2 = re.search(r'"dateModified":"([^"]+)"', text)
            mod_date = m2.group(1) if m2 else pub_date
            posts.append({
                'slug': slug,
                'url': f'{url_prefix}{slug}',
                'title': extract_title(text).replace(' | AllCoaching', '').strip(),
                'description': extract_meta(text, 'description') or '',
                'image': extract_meta(text, 'og:image') or '',
                'date_published': pub_date,
                'date_modified': mod_date
            })

    posts.sort(key=lambda p: p['date_published'], reverse=True)

    now_rfc = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')

    items_xml = []
    for p in posts:
        items_xml.append(f'''    <item>
      <title>{xml_escape(p['title'])}</title>
      <link>{p['url']}</link>
      <guid isPermaLink="true">{p['url']}</guid>
      <description>{xml_escape(p['description'])}</description>
      <pubDate>{date_to_rfc822(p['date_published'])}</pubDate>
      <dc:creator><![CDATA[Amit Ratan]]></dc:creator>
      <atom:author><name>Amit Ratan</name></atom:author>
      <category>EdTech</category>
      <category>Indian Online Education</category>
      <category>Educator Marketplace</category>{f"""
      <enclosure url="{p['image']}" type="image/webp" />""" if p['image'] else ''}
    </item>''')

    feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:sy="http://purl.org/rss/1.0/modules/syndication/">
  <channel>
    <title>AllCoaching Blog — Essays on the Future of Online Education in India</title>
    <link>https://allcoaching.in/blog/</link>
    <atom:link href="https://allcoaching.in/feed.xml" rel="self" type="application/rss+xml" />
    <description>Long-form, founder-written essays on educator infrastructure, marketplace economics, AI workflows, EdTech compliance, and the architecture of online teaching in India. By Amit Ratan, Founder &amp; CEO of AllCoaching — India's first educator-first marketplace, founded 2018 in Prayagraj.</description>
    <language>en-IN</language>
    <copyright>© 2026 AllCoaching Technologies Pvt. Ltd.</copyright>
    <managingEditor>allcoachingss@gmail.com (Amit Ratan)</managingEditor>
    <webMaster>allcoachingss@gmail.com (Amit Ratan)</webMaster>
    <pubDate>{date_to_rfc822(posts[0]['date_published']) if posts else now_rfc}</pubDate>
    <lastBuildDate>{now_rfc}</lastBuildDate>
    <category>Education</category>
    <category>EdTech</category>
    <category>India</category>
    <generator>AllCoaching feed builder · build_feed_xml.py</generator>
    <docs>https://www.rssboard.org/rss-specification</docs>
    <ttl>1440</ttl>
    <image>
      <url>https://allcoaching.in/assets/AllCoaching-logo.webp</url>
      <title>AllCoaching</title>
      <link>https://allcoaching.in/</link>
      <width>200</width>
      <height>50</height>
    </image>
    <sy:updatePeriod>weekly</sy:updatePeriod>
    <sy:updateFrequency>1</sy:updateFrequency>

{chr(10).join(items_xml)}
  </channel>
</rss>
'''

    out_path = os.path.join(ROOT, 'feed.xml')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as fp:
        fp.write(feed)
    print(f'Wrote {out_path}')
    print(f'Posts: {len(posts)} | Size: {len(feed):,} chars')

if __name__ == '__main__':
    main()
