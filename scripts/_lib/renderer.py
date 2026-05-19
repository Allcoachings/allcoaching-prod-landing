"""
Markdown → HTML renderer with the small set of extensions we actually use.

Uses python-markdown with: tables, fenced code, attr_list (for #ids and
.classes), toc (for in-article TOC), smarty (typographic quotes), and
sane-lists.
"""
from __future__ import annotations
import markdown


_EXTENSIONS = [
    "tables", "fenced_code", "attr_list", "toc", "smarty", "sane_lists",
    "footnotes", "abbr", "def_list",
]
_EXT_CONFIG = {
    "toc": {"permalink": False, "toc_depth": "2-3"},
}


def render(md_text: str) -> str:
    md = markdown.Markdown(extensions=_EXTENSIONS, extension_configs=_EXT_CONFIG)
    return md.convert(md_text)


def render_with_toc(md_text: str) -> tuple[str, str]:
    """Return (html_body, toc_html).

    If the markdown body contains raw-HTML headings (legacy pass-through
    content) the markdown TOC extension yields an empty <ul>. In that case
    we fall back to scanning the rendered HTML for <section id="..."><h2>
    pairs and building the TOC from those.
    """
    md = markdown.Markdown(extensions=_EXTENSIONS, extension_configs=_EXT_CONFIG)
    body = md.convert(md_text)
    md_toc = getattr(md, "toc", "") or ""
    # Markdown emits something like '<div class="toc"><ul></ul></div>' when empty
    has_real_md_toc = "<li>" in md_toc
    if has_real_md_toc:
        return body, md_toc
    fallback = extract_toc_from_html(body)
    return body, fallback


def extract_toc_from_html(html: str) -> str:
    """Build a flat TOC <ol> from <section id="..."> + <h2> patterns
    in raw HTML body content. Returns "" if no anchored sections found.
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    items: list[tuple[str, str]] = []
    seen_ids: set[str] = set()
    # Look for any element with an id that contains an h2/h3 inside
    # OR an h2/h3 that has an id directly.
    for elem in soup.find_all(["section", "div", "article"]):
        anchor = elem.get("id")
        if not anchor or anchor in seen_ids:
            continue
        heading = elem.find(["h2", "h3"])
        if not heading:
            continue
        # Replace <br> with space, then strip tags
        for br in heading.find_all("br"):
            br.replace_with(" ")
        text = " ".join(heading.get_text(" ", strip=True).split())
        if not text:
            continue
        seen_ids.add(anchor)
        items.append((anchor, text))
    # Also support direct <h2 id="..."> usage
    for h in soup.find_all(["h2", "h3"]):
        anchor = h.get("id")
        if not anchor or anchor in seen_ids:
            continue
        for br in h.find_all("br"):
            br.replace_with(" ")
        text = " ".join(h.get_text(" ", strip=True).split())
        if not text:
            continue
        seen_ids.add(anchor)
        items.append((anchor, text))
    if not items:
        return ""
    li = "\n".join(
        f'<li><a href="#{anchor}">{text}</a></li>' for anchor, text in items
    )
    return f'<ol class="toc-list">\n{li}\n</ol>'
