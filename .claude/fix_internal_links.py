"""
Fix all internal .html links to use canonical slug-only URLs.
.htaccess strips .html, so every link with .html triggers a 301 redirect.
SEO best practice: link directly to canonical URL.

Transformations:
  href="./index.html"      → href="/"
  href="../index.html"     → href="/"
  href="./about.html"      → href="/about"
  href="../about.html"     → href="/about"
  href="./blog/foo.html"   → href="/blog/foo"
  href="../blog/foo.html"  → href="/blog/foo"
  href="foo.html"          (within /blog/) → href="/blog/foo"
  href="about.html"        (root) → href="/about"
  Preserves #anchors and ?query strings.
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROOT_HTML = list(REPO.glob("*.html"))
BLOG_HTML = list((REPO / "blog").glob("*.html"))

ROOT_SLUGS = {p.stem for p in ROOT_HTML}    # about, contact, manifesto, ...
BLOG_SLUGS = {p.stem for p in BLOG_HTML}    # blog post slugs


def normalize_href(href: str, is_blog_page: bool) -> str:
    """Convert any internal .html href to canonical slug-only URL."""
    # Split anchor / query
    suffix = ""
    m = re.search(r'([#?].*)$', href)
    if m:
        suffix = m.group(1)
        path = href[: -len(suffix)]
    else:
        path = href

    # Already absolute non-.html? leave alone
    if not path.endswith(".html"):
        return href

    # Strip leading ./ ../ /
    p = path.lstrip("./")
    p = p.lstrip("/")

    # Determine target
    if p == "index.html" or p.endswith("/index.html"):
        return "/" + suffix

    # blog/xxx.html → /blog/xxx
    if p.startswith("blog/"):
        slug = p[len("blog/"):-len(".html")]
        return f"/blog/{slug}{suffix}"

    # Root-level page: about.html → /about
    if p.endswith(".html") and "/" not in p:
        slug = p[:-len(".html")]
        if slug in ROOT_SLUGS:
            return f"/{slug}{suffix}"

    # Path like ../blog/foo.html was already handled above due to lstrip
    # ../something.html
    if p.endswith(".html"):
        slug = p[:-len(".html")]
        slug = slug.split("/")[-1]
        if slug in ROOT_SLUGS:
            return f"/{slug}{suffix}"
        if slug in BLOG_SLUGS:
            return f"/blog/{slug}{suffix}"

    # In-blog relative: when inside /blog/, href="foo.html" resolves there
    if is_blog_page and p.endswith(".html") and "/" not in p:
        slug = p[:-len(".html")]
        if slug in BLOG_SLUGS:
            return f"/blog/{slug}{suffix}"

    return href


HREF_RE = re.compile(r'href="([^"]+)"')


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    is_blog = path.parent.name == "blog"
    swaps = 0

    def repl(m):
        nonlocal swaps
        orig = m.group(1)
        # skip external/mailto/tel/javascript/anchor-only
        if orig.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#")):
            return m.group(0)
        new = normalize_href(orig, is_blog)
        if new != orig:
            swaps += 1
            return f'href="{new}"'
        return m.group(0)

    new_text = HREF_RE.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return swaps


def main():
    total = 0
    files_changed = 0
    for p in sorted(ROOT_HTML + BLOG_HTML, key=str):
        n = fix_file(p)
        rel = p.relative_to(REPO)
        flag = "[OK]" if n else "[--]"
        print(f"  {flag} {str(rel):<70} {n:>4} links")
        total += n
        if n:
            files_changed += 1
    print(f"\n{files_changed} files modified, {total} internal links rewritten")


if __name__ == "__main__":
    main()
