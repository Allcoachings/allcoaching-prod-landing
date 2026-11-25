#!/usr/bin/env python3
"""One font everywhere (owner, 2026-11-25): Inter Tight for headings and text, JetBrains Mono for mono,
Instrument Serif italic ONLY for the AllCoaching wordmark. Devanagari fonts are kept for Hindi glyphs.

Rewrites CSS rule by rule in the shared CSS files and in every page's <style> blocks and inline styles:
- serif / display / reading families (Instrument Serif, Fraunces, Newsreader, var(--display), var(--reading), var(--dp))
  -> Inter Tight, and font-style:italic in the same rule -> normal (unless the selector is a wordmark)
- Inter, IBM Plex Mono, var(--v3-font) -> Inter Tight / JetBrains Mono
- Google Fonts links -> one canonical link
Idempotent. Skips landing/ (ad pages), demo/, dist/ except tw.min.css, and brand.html (the brand guide documents fonts)."""
import glob, os, re, time

def write(f, n):
    for i in range(8):
        try:
            open(f, 'w', encoding='utf-8', newline='').write(n); return True
        except OSError:
            time.sleep(0.5)
    print('COULD NOT WRITE', f); return False

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

UI = "'Inter Tight','Inter',system-ui,sans-serif"
MONO = "'JetBrains Mono',ui-monospace,monospace"
WORDMARK = re.compile(r'word|lockup|logo|wordmark|brand-name|xft-tag|signature', re.I)
SERIF = re.compile(r"font-family\s*:\s*(?:[^;}\"]*(?:Instrument Serif|Fraunces|Newsreader|Times New Roman|Georgia)[^;}\"]*|var\(--(?:display|reading|dp|serif)\)[^;}\"]*)", re.I)
INTER = re.compile(r"font-family\s*:\s*(?:'Inter'|\"Inter\"|Inter)\s*(?:,[^;}\"]*)?(?=[;}\"]|$)")
PLEX = re.compile(r"'IBM Plex Mono'|\"IBM Plex Mono\"")
V3 = re.compile(r"font-family\s*:\s*var\(--v3-font\)")

def fix_block(selector, body):
    keep = bool(WORDMARK.search(selector or ''))
    if not keep and SERIF.search(body):
        imp = '!important' if '!important' in SERIF.search(body).group(0) else ''
        body = SERIF.sub('font-family:' + UI, body)
        body = body.replace('font-family:' + UI + '!important', 'font-family:' + UI)
        if imp:
            body = body.replace('font-family:' + UI, 'font-family:' + UI + '!important')
        body = re.sub(r'font-style\s*:\s*italic', 'font-style:normal', body)
    body = INTER.sub('font-family:' + UI, body)
    body = PLEX.sub("'JetBrains Mono'", body)
    body = V3.sub('font-family:' + UI, body)
    return body

def fix_css(css):
    # variables first
    css = re.sub(r"(--(?:ui|display|reading|dp|v3-font|font-sans|serif)\s*:\s*)[^;}]+", lambda m: m.group(1) + UI, css)
    css = re.sub(r"(--(?:mono|v3-mono)\s*:\s*)[^;}]+", lambda m: m.group(1) + MONO, css)
    return re.sub(r'([^{}]*)\{([^{}]*)\}', lambda m: m.group(1) + '{' + fix_block(m.group(1), m.group(2)) + '}', css)

FONT_LINK = ('<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:ital,wght@0,100..900;1,100..900'
             '&family=JetBrains+Mono:wght@400;500;700{extra}&display=swap" rel="stylesheet" />')

def fix_font_link(html):
    def rep(m):
        url = m.group(0)
        extra = ''
        for fam in ('Noto+Sans+Devanagari', 'Tiro+Devanagari+Hindi', 'Mukta'):
            mm = re.search(r'family=' + re.escape(fam) + r'[^&"]*', url)
            if mm: extra += '&' + mm.group(0)
        return FONT_LINK.format(extra=extra)
    return re.sub(r'<link[^>]+href="https://fonts\.googleapis\.com/css2\?[^"]*"[^>]*>', rep, html)

files_css = ['brand.css', 'styles.css', 'blog-v3.css', 'dist/tw.min.css']
for f in files_css:
    if os.path.exists(f):
        s = open(f, encoding='utf-8').read(); n = fix_css(s)
        if n != s: write(f, n); print('css', f)

changed = 0
for f in glob.glob('**/*.html', recursive=True):
    f = f.replace(os.sep, '/')
    if f.startswith(('dist/', 'node_modules/', 'landing/', 'demo/', 'templates/', 'assets/')) or f == 'brand.html':
        continue
    s = open(f, encoding='utf-8').read()
    n = re.sub(r'(<style[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + fix_css(m.group(2)) + m.group(3), s, flags=re.S)
    n = re.sub(r'style="([^"]*)"', lambda m: 'style="' + fix_block('', m.group(1).replace("&#x27;", "'")).replace("'", "&#x27;" if "&#x27;" in m.group(1) else "'") + '"', n)
    n = fix_font_link(n)
    # Tailwind italic serif utility pairs: no serif left, so no italic either
    if n != s:
        changed += write(f, n)
print('pages changed:', changed)
