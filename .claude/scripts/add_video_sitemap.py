"""
Add Google video-sitemap entries for the founder video.

Deliberately limited to pages where the video is the exact topical match.
Google indexes a video against ONE primary page; listing the same video on
every page it is embedded in is an anti-pattern that dilutes or gets ignored.
Idempotent.
"""
import re

SITEMAP = 'sitemap.xml'
NS_VIDEO = 'xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"'

VIDEO = {
    'id': 'EbJTiKAlwH0',
    'title': 'Coaching App Banane Ka Kharcha Kitna Hai? | 2026 Ka Asli Hisaab',
    'description': (
        'Coaching app banwane ka kharcha 0 rupaye bhi ho sakta hai, aur 30 lakh bhi. '
        'Is video me wahi real cost dikhaya hai jo koi bhi app company khulkar nahi batati '
        '- custom app pricing, subscription app ka chhupa hisaab, Android-only apps ka trap, '
        'aur marketing budget wala asli kharcha jiski baat koi nahi karta.'
    ),
    'duration': 277,
    'publication_date': '2026-08-23T21:48:09-07:00',
    'uploader': 'Amit Ratan',
    'uploader_url': 'https://www.youtube.com/@allamitratan',
}

# only the exact-topic pages get a video sitemap entry
PAGES = [
    'https://allcoaching.in/blogs/hinglish/coaching-app-banane-me-kitna-paisa-lagta-hai',
    'https://allcoaching.in/blog/white-label-coaching-app-development-cost-india',
]


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def block(v):
    return '''    <video:video>
      <video:thumbnail_loc>https://i.ytimg.com/vi/{id}/maxresdefault.jpg</video:thumbnail_loc>
      <video:title>{title}</video:title>
      <video:description>{desc}</video:description>
      <video:player_loc>https://www.youtube-nocookie.com/embed/{id}</video:player_loc>
      <video:duration>{dur}</video:duration>
      <video:publication_date>{pub}</video:publication_date>
      <video:uploader info="{uurl}">{uploader}</video:uploader>
      <video:family_friendly>yes</video:family_friendly>
      <video:live>no</video:live>
      <video:requires_subscription>no</video:requires_subscription>
    </video:video>
'''.format(id=v['id'], title=esc(v['title']), desc=esc(v['description']),
           dur=v['duration'], pub=v['publication_date'],
           uploader=esc(v['uploader']), uurl=esc(v['uploader_url']))


def main():
    h = open(SITEMAP, encoding='utf-8').read()

    # 1) namespace
    if NS_VIDEO not in h:
        h = h.replace(
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n  ' + NS_VIDEO + '>',
            1)
        print('added video namespace')
    else:
        print('video namespace already present')

    # 2) strip any existing video blocks (idempotent re-run)
    h = re.sub(r'    <video:video>.*?</video:video>\n', '', h, flags=re.DOTALL)

    # 3) insert into the target <url> blocks, before </url>
    added = 0
    for page in PAGES:
        m = re.search(r'(  <url>\s*\n\s*<loc>' + re.escape(page) + r'</loc>.*?)(  </url>)',
                      h, flags=re.DOTALL)
        if not m:
            print('NOT FOUND in sitemap:', page)
            continue
        h = h[:m.end(1)] + block(VIDEO) + h[m.end(1):]
        added += 1

    open(SITEMAP, 'w', encoding='utf-8').write(h)
    print('video entries added:', added)


if __name__ == '__main__':
    main()
