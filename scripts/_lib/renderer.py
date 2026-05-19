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
    """Return (html_body, toc_html)."""
    md = markdown.Markdown(extensions=_EXTENSIONS, extension_configs=_EXT_CONFIG)
    body = md.convert(md_text)
    toc = getattr(md, "toc", "")
    return body, toc
