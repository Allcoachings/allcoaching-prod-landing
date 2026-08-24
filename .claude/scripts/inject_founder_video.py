"""
Inject the founder video (facade embed + VideoObject JSON-LD) into a set of pages.

Idempotent: re-running replaces the existing block, so swapping in a
page-specific video later is a one-line change to VIDEOS below.

Marker: <!-- AUTO: founder-video --> ... <!-- /AUTO: founder-video -->
Insertion point: immediately after the #tldr block.
"""
import json, os, re, sys

# ---- video registry -------------------------------------------------------
# Default video used for every page unless a page-specific override is added.
DEFAULT = {
    'id': 'EbJTiKAlwH0',
    'title': 'Coaching App Banane Ka Kharcha Kitna Hai? | 2026 Ka Asli Hisaab',
    'channel': 'Amit Ratan',
    'channel_url': 'https://www.youtube.com/@allamitratan',
    # values below pulled from the YouTube watch page, not assumed
    'upload_date': '2026-08-23T21:48:09-07:00',
    'duration_sec': 277,
    'duration_iso': 'PT4M37S',
    'description': (
        'Coaching app banwane ka kharcha ₹0 bhi ho sakta hai, aur ₹30 lakh bhi. '
        'Is video me wahi real cost dikhaya hai jo koi bhi app company khulkar nahi batati '
        '— custom app pricing, subscription app ka chhupa hisaab, Android-only apps ka trap, '
        'aur marketing budget wala asli kharcha jiski baat koi nahi karta.'
    ),
}
# per-page overrides: {'blog/foo.html': {...}}
VIDEOS = {}

TARGETS = [
    # exact keyword match for this video (app cost) — these two also carry
    # the <video:video> entry in sitemap.xml
    'blogs/hinglish/coaching-app-banane-me-kitna-paisa-lagta-hai.html',
    'blog/white-label-coaching-app-development-cost-india.html',
    # platform-comparison cluster
    'blog/appx-vs-classplus.html',
    'blog/classplus-alternative-for-coaching-institutes.html',
    'blog/classplus-vs-graphy-vs-allcoaching.html',
    'blog/graphy-alternative-for-course-creators-india.html',
    'blogs/en/graphy-alternative-with-organic-marketplace-traffic.html',
    'blogs/hinglish/classplus-ka-best-alternative-kaunsa-hai.html',
    'blogs/hinglish/teachmint-vs-classplus-konsa-best-hai.html',
    'vs/classplus.html',
    'vs/graphy.html',
]

START = '<!-- AUTO: founder-video -->'
END = '<!-- /AUTO: founder-video -->'

BLOCK = '''{start}
<div class="vid-embed" id="founder-video">
<p class="vid-l">Founder ka video</p>
<button class="vid-frame" type="button" data-yt="{vid}" aria-label="Play: {title_attr}">
  <img src="https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" alt="{title_attr} — video by {channel}" loading="lazy" width="1280" height="720" decoding="async" />
  <span class="vid-play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>
  <span class="vid-cap">
    <span class="vid-t">{title_html}</span>
    <span class="vid-m">{channel} · YouTube</span>
  </span>
</button>
</div>
{end}'''

SCRIPT = '''<script data-founder-video="1">
(function(){
  var WARM=0;
  function warm(){
    if(WARM) return; WARM=1;
    ['https://www.youtube-nocookie.com','https://i.ytimg.com'].forEach(function(u){
      var l=document.createElement('link'); l.rel='preconnect'; l.href=u; l.crossOrigin='';
      document.head.appendChild(l);
    });
  }
  function play(b){
    if(b.classList.contains('is-playing')) return;
    var f=document.createElement('iframe');
    f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0&playsinline=1&modestbranding=1';
    f.title=(b.getAttribute('aria-label')||'YouTube video').replace(/^Play:\\s*/,'');
    f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.allowFullscreen=true;
    f.addEventListener('load',function(){ f.classList.add('ready'); });
    b.classList.add('is-playing');
    b.setAttribute('aria-label','Now playing');
    b.appendChild(f);
  }
  document.addEventListener('pointerover',function(e){
    var b=e.target.closest&&e.target.closest('.vid-frame'); if(b&&b.dataset.yt) warm();
  },{passive:true});
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.vid-frame');
    if(b&&b.dataset.yt) play(b);
  },false);
})();
</script>'''


def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def esc_html(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def video_schema(v, page_url):
    return {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": v['title'],
        "description": v.get('description', v['title']),
        "thumbnailUrl": ["https://i.ytimg.com/vi/%s/maxresdefault.jpg" % v['id']],
        "uploadDate": v['upload_date'],
        "duration": v.get('duration_iso'),
        "contentUrl": "https://www.youtube.com/watch?v=%s" % v['id'],
        "embedUrl": "https://www.youtube-nocookie.com/embed/%s" % v['id'],
        "inLanguage": "hi-IN",
        "creator": {"@type": "Person", "name": v['channel'], "url": v['channel_url']},
        "publisher": {"@id": "https://allcoaching.in/#organization"},
        "isPartOf": {"@type": "WebPage", "@id": page_url},
    }


def canonical_of(h):
    m = re.search(r'rel="canonical" href="([^"]+)"', h)
    return m.group(1) if m else None


def strip_existing(h):
    h = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', h, flags=re.DOTALL)
    h = re.sub(r'<script type="application/ld\+json">\s*\{[^<]*?"@type":\s*"VideoObject".*?</script>\n?', '', h, flags=re.DOTALL)
    h = re.sub(r'<script data-founder-video="1">.*?</script>\n?', '', h, flags=re.DOTALL)
    h = re.sub(r'<script>\s*\(function\(\)\{\s*document\.addEventListener\(.click.,function\(e\)\{\s*var b=e\.target\.closest.*?</script>\n?', '', h, flags=re.DOTALL)
    return h


def process(path, apply=True):
    h = open(path, encoding='utf-8').read()
    v = VIDEOS.get(path, DEFAULT)
    h = strip_existing(h)

    canon = canonical_of(h)
    if not canon:
        return path, 'SKIP (no canonical)'

    block = BLOCK.format(
        start=START, end=END, vid=v['id'],
        title_attr=esc_attr(v['title']),
        title_html=esc_html(v['title']),
        channel=esc_html(v['channel']),
    )

    # insert right after the #tldr container closes
    m = re.search(r'(<div class="(?:hband|tldr-strip)" id="tldr">.*?</div>\s*\n)', h, flags=re.DOTALL)
    if not m:
        return path, 'SKIP (no #tldr block)'
    h = h[:m.end(1)] + '\n' + block + '\n' + h[m.end(1):]

    # VideoObject schema before </head>
    schema = '<script type="application/ld+json">%s</script>\n' % json.dumps(
        video_schema(v, canon), ensure_ascii=False, separators=(',', ':'))
    h = h.replace('\n</head>', '\n' + schema + '</head>', 1)

    # click-to-load script before </body>
    if 'data-founder-video="1"' not in h:
        h = h.replace('</body>', SCRIPT + '\n</body>', 1)

    if apply:
        open(path, 'w', encoding='utf-8').write(h)
    return path, 'OK'


if __name__ == '__main__':
    apply = '--dry-run' not in sys.argv
    for t in TARGETS:
        if not os.path.exists(t):
            print('%-62s MISSING' % t)
            continue
        p, status = process(t, apply)
        print('%-62s %s' % (p, status))
    print('\napplied' if apply else '\ndry run only')
