#!/usr/bin/env python3
"""Make every FAQPage JSON-LD block match its visible DOM verbatim.

CLAUDE.md requires FAQ JSON-LD to mirror the visible DOM 1:1 (question count and
text). Google requires the same: FAQ structured data that is not present on the
page is a policy violation and can trigger a manual action.

The DOM is the source of truth. For each page this rebuilds `mainEntity` from the
visible <details><summary>Q</summary>…answer…</details> blocks.

Why this exists alongside sync_faq_to_dom.py
--------------------------------------------
`sync_faq_to_dom.py` only APPENDS questions that are missing from the JSON-LD. It
cannot repair an entry whose text has drifted, and it cannot remove a schema
question that is no longer on the page. That is why 47 files were silently out of
sync until 2026-08-07. This script rewrites the whole array, so drift of any kind
is corrected.

Usage
-----
    python .claude/scripts/sync_faq_schema.py            # fix every page
    python .claude/scripts/sync_faq_schema.py --check    # report only, exit 1 on drift
    python .claude/scripts/sync_faq_schema.py blog/x.html # limit to given files

`--check` is the CI / pre-commit form: it writes nothing and exits non-zero if any
page has drifted.
"""
from __future__ import annotations

import glob
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LD_BLOCK = re.compile(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', re.DOTALL)
DETAILS = re.compile(r'<details[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>', re.DOTALL)


def plain(fragment: str) -> str:
    """DOM fragment -> the plaintext Google compares against."""
    text = re.sub(r'<[^>]+>', '', fragment)
    return re.sub(r'\s+', ' ', html.unescape(text)).strip()


def dom_faqs(page: str) -> list[tuple[str, str]]:
    return [(plain(q), plain(a)) for q, a in DETAILS.findall(page)]


def find_faqpage(page: str):
    """Return (match, parsed_obj) for the FAQPage script block, or (None, None)."""
    for m in LD_BLOCK.finditer(page):
        try:
            obj = json.loads(m.group(1))
        except ValueError:
            continue
        if isinstance(obj, dict) and obj.get('@type') == 'FAQPage':
            return m, obj
    return None, None


def targets(argv: list[str]) -> list[str]:
    files = [a for a in argv if not a.startswith('--')]
    if files:
        return files
    found: list[str] = []
    for pattern in ('blog/*.html', 'blogs/**/*.html', 'vs/*.html', '*.html'):
        found += glob.glob(os.path.join(ROOT, pattern), recursive=True)
    return sorted(set(found))


def main() -> int:
    check_only = '--check' in sys.argv
    drifted = []

    for path in targets(sys.argv[1:]):
        if os.path.basename(path) == 'index.html':
            continue
        with open(path, encoding='utf-8') as fh:
            page = fh.read()

        match, obj = find_faqpage(page)
        if match is None:
            continue

        dom = dom_faqs(page)
        if not dom:
            continue

        ld = [(q.get('name', ''), q.get('acceptedAnswer', {}).get('text', ''))
              for q in obj.get('mainEntity', [])]
        if ld == dom:
            continue

        rel = os.path.relpath(path, ROOT).replace('\\', '/')
        drifted.append((rel, len(ld), len(dom),
                        sum(1 for a, b in zip(ld, dom) if a[0] != b[0]),
                        sum(1 for a, b in zip(ld, dom) if a[1] != b[1])))
        if check_only:
            continue

        obj['mainEntity'] = [
            {'@type': 'Question', 'name': q,
             'acceptedAnswer': {'@type': 'Answer', 'text': a}}
            for q, a in dom
        ]
        rebuilt = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(page[:match.start(1)] + rebuilt + page[match.end(1):])

    verb = 'DRIFTED' if check_only else 'SYNCED'
    print(f'{verb}: {len(drifted)} file(s) with FAQ schema/DOM mismatch')
    for rel, n_ld, n_dom, q_diff, a_diff in drifted:
        print(f'   {rel:60} ld={n_ld:<3} dom={n_dom:<3} Qdiff={q_diff:<3} Adiff={a_diff}')

    return 1 if (check_only and drifted) else 0


if __name__ == '__main__':
    raise SystemExit(main())
