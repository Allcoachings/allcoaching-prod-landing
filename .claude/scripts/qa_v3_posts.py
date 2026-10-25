"""QA gate for rewritten v3 posts.

Usage: python .claude/scripts/qa_v3_posts.py [file.html ...]   (default: every v3 post in blog/, blogs/en/, blogs/hinglish/)

Checks: title <= 65, description 140-175, 6 JSON-LD blocks that parse, FAQ schema count == DOM count,
no leftover {{placeholders}}, banned phrases, Graphy rupee prices, old unsupported figures, own-image
covers (no old CDN blog-images), and that every figure file exists.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANNED = [r'free forever', r'₹0 (?:upfront|up front|to start|base)', r'\bfree plan\b(?! is)', r'one-time fee', r'no subscription',
          r'\bcheapest\b(?![^<]{0,40}(?:LMS for|lms-for))', r'daily payout', r'paid daily', r'flat 10%', r'(?:5|10|15) (?:live[- ]class )?hours',
          r'shared app', r'#1 platform', r'!\s', r'\bunlock', r'\bmaximi[sz]e', r'T\+3', r'per public reports', r'₹4[–-]11 ?(?:L|lakh)',
          r'12[–-]18 day', r'25[–-]65%']
GRAPHY_INR = r'Graphy[^.<]{0,120}₹|₹[\d,]+[^.<]{0,60}\(Graphy|₹24,999 · ₹49,999|₹2,800|₹4,200'


def text_of(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>', ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))


def check(path):
    s = open(path, encoding='utf-8').read()
    issues = []
    title = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
    desc = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    if len(title) > 65:
        issues.append(f'title {len(title)}')
    if not 140 <= len(desc) <= 175:
        issues.append(f'desc {len(desc)}')
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', s, re.S)
    try:
        objs = [json.loads(b) for b in blocks]
    except ValueError as e:
        issues.append(f'json-ld parse {e}')
        objs = []
    if len(blocks) != 6:
        issues.append(f'{len(blocks)} json-ld')
    faq = next((o for o in objs if o.get('@type') == 'FAQPage'), {})
    if len(faq.get('mainEntity', [])) != len(re.findall(r'<details open><summary>', s)):
        issues.append('faq count mismatch')
    if '{{' in s:
        issues.append('placeholder left')
    body = text_of(s[s.find('<body'):])
    for b in BANNED:
        for m in re.finditer(b, body, flags=re.I):
            ctx = body[max(0, m.start() - 50):m.end() + 50]
            if b == r'!\s' and ('<!' in ctx or '!=' in ctx):
                continue
            issues.append(f'banned "{m.group(0)}": …{ctx.strip()}…')
    for m in re.finditer(GRAPHY_INR, body):
        issues.append(f'graphy ₹: …{body[max(0, m.start() - 40):m.end() + 40].strip()}…')
    if 'b-cdn.net/blog-images/' in s.split('<section class="v3-more"')[0]:
        issues.append('old CDN image in post body/head')
    for src in re.findall(r'src="(/assets/blog/[^"]+)"', s):
        if not os.path.exists(os.path.join(ROOT, src.lstrip('/'))):
            issues.append(f'missing {src}')
    words = re.search(r'"wordCount":(\d+)', s)
    return title, len(desc), int(words.group(1)) if words else 0, issues


def main(paths):
    if not paths:
        paths = [p for p in glob.glob(os.path.join(ROOT, 'blog/*.html')) + glob.glob(os.path.join(ROOT, 'blogs/*/*.html'))
                 if 'class="v3"' in open(p, encoding='utf-8').read()]
    bad = 0
    for p in sorted(paths):
        t, dl, w, iss = check(p)
        flag = 'OK ' if not iss else 'FIX'
        bad += bool(iss)
        print(f'{flag} {os.path.relpath(p, ROOT)} | {len(t)}c "{t}" | desc {dl} | {w} words')
        for i in iss[:8]:
            print('     -', i[:220])
    print(f'{len(paths)} posts, {bad} need fixes')


if __name__ == '__main__':
    main(sys.argv[1:])
