# -*- coding: utf-8 -*-
"""Smart-trim <meta name="description"> to <=170 chars at a clean sentence/clause boundary.
Only touches the name="description" tag (the SERP-critical one). Prints before/after."""
import re, glob, os, html

LIMIT = 168
def pages():
    out = glob.glob('*.html')
    for d in ['blog', 'blogs', 'blogs/en', 'blogs/hi', 'blogs/hinglish', 'author']:
        out += glob.glob(d + '/*.html')
    return sorted(set(out))

def trim(d, limit=LIMIT):
    d = d.strip()
    if len(d) <= limit:
        return d
    # 1) last sentence end (. ! ?) followed by space/end, at or before limit, not too short
    best = -1
    for m in re.finditer(r'[.!?](?=\s|$)', d):
        if m.end() <= limit:
            best = m.end()
        else:
            break
    if best >= 90:
        return d[:best].strip()
    # 2) last clause boundary (em/en-dash, ;, :, comma+space) before limit, not too short
    cut = -1
    for m in re.finditer(r'\s[—–]\s|;|:\s|,\s', d):
        if m.start() <= limit - 1:
            cut = m.start()
        else:
            break
    if cut >= 100:
        return d[:cut].strip().rstrip('—–;:, ')
    # 3) last word boundary before limit
    sp = d.rfind(' ', 0, limit)
    if sp < 60:
        sp = limit
    return d[:sp].strip().rstrip('—–;:, ')

changed = 0
checks = []
for p in pages():
    c = open(p, encoding='utf-8').read()
    m = re.search(r'(<meta\s+name="description"\s+content=")([^"]*)(")', c, re.I)
    if not m:
        continue
    cur = html.unescape(m.group(2))
    if len(cur) <= 170:
        continue
    new = trim(cur)
    new_esc = new.replace('&', '&amp;')
    c2 = c[:m.start()] + m.group(1) + new_esc + m.group(3) + c[m.end():]
    open(p, 'w', encoding='utf-8').write(c2)
    changed += 1
    end_ok = new.rstrip()[-1:] in '.!?'
    flag = 'OK ' if end_ok else 'CHK'
    if not end_ok:
        checks.append(p.replace(os.sep, '/'))
    print(f"[{flag}] {len(cur)}->{len(new)}  {p.replace(os.sep,'/')}")
    print(f"      {new}")
print(f"\nTrimmed {changed} descriptions to <=170c.")
print(f"Non-sentence-final endings to eyeball ({len(checks)}): {checks}")
