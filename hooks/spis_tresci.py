"""Hook MkDocs: wstawia automatyczny spis treści w miejsce znacznika <!-- SPIS-TRESCI -->.

Spis powstaje z sekcji `nav` w mkdocs.yml oraz nagłówków `##` każdej strony,
więc nowe rozdziały i podrozdziały pojawiają się w nim same po dodaniu do nav.
"""
import os
import re

from markdown.extensions.toc import slugify

MARKER = "<!-- SPIS-TRESCI -->"
_nav = None


def on_nav(nav, config, files):
    global _nav
    _nav = nav
    return nav


def _read(page):
    path = page.file.abs_src_path
    if not path or not os.path.exists(path):
        return ""
    text = open(path, encoding="utf-8").read()
    return re.sub(r"```.*?```", "", text, flags=re.S)


def _title(page):
    if page.title:
        return page.title
    m = re.search(r"^# (.+)$", _read(page), flags=re.M)
    return m.group(1).strip() if m else page.file.name


def _headings(page):
    return [h.strip() for h in re.findall(r"^## (.+)$", _read(page), flags=re.M)]


def _link(from_page, to_page, anchor=""):
    rel = os.path.relpath(to_page.file.src_uri, os.path.dirname(from_page.file.src_uri) or ".")
    return rel.replace(os.sep, "/") + anchor


def _render(items, current, depth=0):
    lines = []
    indent = "    " * depth
    for item in items:
        if item.is_section:
            children = list(item.children)
            first = children[0] if children else None
            if first is not None and first.is_page and first.is_index:
                lines.append(f"{indent}- **[{item.title}]({_link(current, first)})**")
                children = children[1:]
            else:
                lines.append(f"{indent}- **{item.title}**")
            lines += _render(children, current, depth + 1)
        elif item.is_page:
            if item.file.src_uri == current.file.src_uri:
                continue
            lines.append(f"{indent}- [{_title(item)}]({_link(current, item)})")
            for h in _headings(item):
                plain = re.sub(r"[*_`]", "", h)
                lines.append(f"{indent}    - [{plain}]({_link(current, item, '#' + slugify(plain, '-'))})")
    return lines


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown or _nav is None:
        return markdown
    return markdown.replace(MARKER, "\n".join(_render(_nav.items, page)))
