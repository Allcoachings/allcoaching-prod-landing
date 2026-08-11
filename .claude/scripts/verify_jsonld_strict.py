#!/usr/bin/env python3
"""Strict JSON-LD validation — catches what json.loads() silently forgives.

Google Search Console reported "Duplicate unique property" on /about on
2026-05-19 and the repo's own validators never saw it, because `json.loads()`
accepts duplicate keys and keeps the last one. The page had `"about"` twice: the
Amit Ratan Person reference was being dropped on every parse, and Google marked
the whole item invalid and ineligible for rich results.

This checks the three failure modes a normal parse cannot see:

  1. Duplicate keys inside one JSON-LD object   -> GSC "Duplicate unique property"
  2. The same @id declared by two entities on one page (conflicting definitions)
  3. An @id referenced on the page that nothing defines (dangling reference,
     reported as a warning — cross-page references are legitimate)

Usage
-----
    python .claude/scripts/verify_jsonld_strict.py             # whole site
    python .claude/scripts/verify_jsonld_strict.py blog/x.html # given files

Exits non-zero if any error-level problem is found, so it can gate a commit.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LD_BLOCK = re.compile(r'<script type="application/ld\+json">\s*(.+?)\s*</script>', re.DOTALL)

# Site-wide entities defined on the core pages (index, about, pricing, faq, …).
# Referencing these from a blog post is correct JSON-LD practice, not a dangling
# pointer — Google resolves them from the site graph.
CROSS_PAGE_IDS = {
    'https://allcoaching.in/#organization',
    'https://allcoaching.in/#website',
    'https://allcoaching.in/author/amit-ratan#person',
    'https://allcoaching.in/blog/',
}


def duplicate_key_hook(found: list[str]):
    def hook(pairs):
        seen: dict = {}
        for key, value in pairs:
            if key in seen:
                found.append(key)
            seen[key] = value
        return seen
    return hook


def walk(node, defined: dict, referenced: set, depth: int = 0):
    """Collect @ids that define an entity vs @ids that merely reference one.

    A node is a definition if it carries @type alongside @id; a bare {"@id": ...}
    is a reference.
    """
    if isinstance(node, dict):
        node_id = node.get('@id')
        if isinstance(node_id, str):
            if '@type' in node:
                defined.setdefault(node_id, []).append(node)
            else:
                referenced.add(node_id)
        for value in node.values():
            walk(value, defined, referenced, depth + 1)
    elif isinstance(node, list):
        for item in node:
            walk(item, defined, referenced, depth + 1)


def id_collision(nodes: list) -> str | None:
    """Describe a genuine @id conflict, or None if the nodes merge safely.

    Repeating an @id across script blocks is legitimate — JSON-LD merges them into
    one graph node, and the repo does this deliberately for #organization and
    #website. It is only an error when the merge would produce a contradiction:
    two different @types, or the same property with two different values.
    """
    types = {json.dumps(n.get('@type'), sort_keys=True) for n in nodes}
    if len(types) > 1:
        readable = sorted(json.loads(t) if t != 'null' else None for t in types)
        return f'conflicting @type: {readable}'

    values: dict = {}
    for node in nodes:
        for key, value in node.items():
            if key in ('@context', '@type', '@id'):
                continue
            values.setdefault(key, set()).add(json.dumps(value, sort_keys=True, ensure_ascii=False))
    clashing = sorted(k for k, v in values.items() if len(v) > 1)
    if clashing:
        return f'same @id declares conflicting values for: {", ".join(clashing)}'
    return None


def targets(argv: list[str]) -> list[str]:
    files = [a for a in argv if not a.startswith('--')]
    if files:
        return files
    found: list[str] = []
    for pattern in ('*.html', 'blog/*.html', 'blogs/**/*.html', 'vs/*.html',
                    'author/**/*.html', 'institute/**/*.html'):
        found += glob.glob(os.path.join(ROOT, pattern), recursive=True)
    return sorted(set(found))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    scanned = 0

    for path in targets(sys.argv[1:]):
        with open(path, encoding='utf-8') as fh:
            page = fh.read()
        blocks = LD_BLOCK.findall(page)
        if not blocks:
            continue
        scanned += 1
        rel = os.path.relpath(path, ROOT).replace('\\', '/')

        defined: dict = {}
        referenced: set = set()

        for index, raw in enumerate(blocks):
            dupes: list[str] = []
            try:
                obj = json.loads(raw, object_pairs_hook=duplicate_key_hook(dupes))
            except ValueError as exc:
                errors.append(f'{rel} block[{index}] INVALID JSON: {exc}')
                continue
            if dupes:
                errors.append(
                    f'{rel} block[{index}] DUPLICATE PROPERTY: '
                    + ', '.join(sorted(set(dupes)))
                    + '  (GSC reports this as "Duplicate unique property")'
                )
            walk(obj, defined, referenced)

        for node_id, nodes in defined.items():
            if len(nodes) > 1:
                clash = id_collision(nodes)
                if clash:
                    errors.append(f'{rel} @id COLLISION {node_id} — {clash}')

        for node_id in sorted(referenced - set(defined) - CROSS_PAGE_IDS):
            warnings.append(f'{rel} dangling @id reference (nothing defines it): {node_id}')

    print(f'Pages with JSON-LD scanned: {scanned}')
    print(f'Errors:   {len(errors)}')
    for line in errors:
        print(f'   ERROR  {line}')
    print(f'Warnings: {len(warnings)}')
    for line in warnings[:20]:
        print(f'   warn   {line}')
    if len(warnings) > 20:
        print(f'   ... and {len(warnings) - 20} more')

    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
