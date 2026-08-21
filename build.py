#!/usr/bin/env python3
"""
Generates the static site from shared templates so nav, footer and head
stay identical across pages. Run `python3 build.py` after editing, then
commit the generated .html files — GitHub Pages serves them directly.

Page bodies live in pages.py. This file owns the shell only.
"""
import os, pathlib
from pages import PAGES, AIMX_DIAGRAM

ROOT = pathlib.Path(__file__).parent

NAV = [
    ("Platform", "/platform/", [
        ("Overview — AIM-X", "/platform/", "The whole framework in one loop"),
        ("Automate", "/platform/automate/", "Resolution without a script"),
        ("Intelligence", "/platform/intelligence/", "The semantic context layer"),
        ("Manage &amp; evolve", "/platform/manage/", "Where autonomy goes next"),
        ("Experience", "/platform/deliverexperience/", "The patented DEX score"),
    ]),
    ("Why not scripts", "/why-nanoheal/why-not-scripts/", None),
    ("Outcomes", "/#value", None),
    ("Partners", "/#partners", None),
]

FOOTER_COLS = [
    ("Platform", [
        ("AIM-X overview", "/platform/"),
        ("Automate", "/platform/automate/"),
        ("Intelligence", "/platform/intelligence/"),
        ("Manage &amp; evolve", "/platform/manage/"),
        ("Experience", "/platform/deliverexperience/"),
    ]),
    ("Why Nanoheal", [
        ("Why not scripts", "/why-nanoheal/why-not-scripts/"),
        ("Time to value", "/#value"),
        ("Analyst recognition", "/#proof"),
        ("Business case", "/#value"),
    ]),
    ("Solutions", [
        ("Ticket deflection", "/platform/automate/"),
        ("Self-service &amp; assisted", "/platform/automate/"),
        ("Policy compliance", "/platform/manage/"),
        ("IT task automation", "/platform/automate/"),
    ]),
    ("Company", [
        ("Partners", "/#partners"),
        ("About", "/#demo"),
        ("Careers", "/#demo"),
        ("Contact", "/#demo"),
    ]),
]

MARK = ('<svg viewBox="0 0 20 20" fill="none" aria-hidden="true">'
        '<path d="M2 11h3.4l2-4.8 2.6 9L12.4 11H18" stroke="#EFEDEB" stroke-width="1.9" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def nav_html(path):
    out = []
    for label, href, menu in NAV:
        cur = ' aria-current="page"' if href == path else ""
        if menu:
            items = "".join(
                f'<a href="{h}">{t}<span>{d}</span></a>' for t, h, d in menu)
            out.append(
                f'<li class="has-menu"><a href="{href}"{cur}>{label}</a>'
                f'<div class="menu">{items}</div></li>')
        else:
            out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(out)


def footer_html():
    cols = []
    for head, links in FOOTER_COLS:
        a = "".join(f'<a href="{h}">{t}</a>' for t, h in links)
        cols.append(f"<div><h4>{head}</h4>{a}</div>")
    return f"""<footer><div class="wrap"><div class="fg">
<div><a class="brand" href="/"><span class="box">{MARK}</span>Nanoheal</a>
<p style="font-size:13px;color:var(--tx-3);max-width:32ch;margin-top:12px">Turning the digital
workplace autonomous. Utah &middot; Bangalore &middot; Manila.</p></div>
{''.join(cols)}</div>
<div class="fbot"><span>&copy; 2026 Nanoheal. DEX Score methodology patented &mdash; US 9,477,573.</span>
<span>Privacy &middot; Terms &middot; Trust Center</span></div></div></footer>"""


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="canonical" href="https://nanoheal.com{path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header><div class="wrap nav">
<a class="brand" href="/"><span class="box">{mark}</span>Nanoheal</a>
<ul>{nav}</ul>
<a class="btn btn-ink" href="/#demo">Schedule a Demo</a>
</div></header>
<main>
{body}
</main>
{footer}
{scripts}
</body>
</html>
"""


def build():
    written = []
    for path, page in PAGES.items():
        body = page["body"].replace("{{AIMX}}", AIMX_DIAGRAM)
        html = SHELL.format(
            title=page["title"], desc=page["desc"], path=path, mark=MARK,
            nav=nav_html(path), body=body, footer=footer_html(),
            scripts=page.get("scripts", ""))
        out = ROOT / (path.lstrip("/") + "index.html")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        written.append(str(out.relative_to(ROOT)))
    for w in sorted(written):
        print("wrote", w)


if __name__ == "__main__":
    build()
