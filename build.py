#!/usr/bin/env python3
"""
Generates the static site from shared templates so nav, footer and head
stay identical across pages. Run `python3 build.py` after editing, then
commit the generated .html files — GitHub Pages serves them directly.

Page bodies live in pages.py. This file owns the shell only.
"""
import datetime, os, re, pathlib
from pages import PAGES, AIMX_DIAGRAM

ROOT = pathlib.Path(__file__).parent

NAV = [
    ("Platform", "/platform/", [
        ("Platform overview", "/platform/", "Measure, understand, act, improve — on one engine"),
        ("Observe &amp; predict", "/platform/observe-predict/", "Analytics, forecasting, anomaly detection"),
        ("Intelligence", "/platform/intelligence/", "The context layer between knowing and doing"),
        ("Automate", "/platform/automate/", "Resolution without a script"),
        ("IT operations", "/platform/it-operations/", "Software, patch and policy on the same engine"),
        ("Orchestration", "/platform/orchestration/", "Any IT system, integrated without code"),
        ("Workflows &amp; natural language", "/platform/workflows/", "Describe it, don't build it"),
        ("Manage &amp; evolve", "/platform/manage/", "Where autonomy goes next"),
        ("Experience", "/platform/deliverexperience/", "The patented DEX score"),
    ]),
    ("Digital Experience", "/digital-experience/", None),
    ("Automation", "/digital-experience-automation/", None),
    ("Why Nanoheal", "/why-nanoheal/why-dxa/", [
        ("Why DXA", "/why-nanoheal/why-dxa/", "Why DEX alone isn't enough"),
        ("Why not scripts", "/why-nanoheal/why-not-scripts/", "The technical case, in full"),
        ("Created once, reused everywhere", "/digital-experience-automation/", "Why coverage compounds"),
        ("Ecosystem automation", "/platform/orchestration/", "Beyond the device, without code"),
    ]),
    ("Solutions", "/#solutions", None),
    ("Outcomes", "/#value", None),
]

FOOTER_COLS = [
    ("Platform", [
        ("Platform overview", "/platform/"),
        ("Digital Experience", "/digital-experience/"),
        ("Intelligence", "/platform/intelligence/"),
        ("Automate", "/platform/automate/"),
        ("IT operations", "/platform/it-operations/"),
        ("Orchestration", "/platform/orchestration/"),
    ]),
    ("Digital Experience Automation", [
        ("What is DXA", "/digital-experience-automation/"),
        ("Why DXA", "/why-nanoheal/why-dxa/"),
        ("Why not scripts", "/why-nanoheal/why-not-scripts/"),
        ("Workflows in plain language", "/platform/workflows/"),
        ("Manage &amp; evolve", "/platform/manage/"),
        ("Experience scoring", "/platform/deliverexperience/"),
    ]),
    ("Solutions", [
        ("Internal IT", "/#solutions"),
        ("Service providers", "/#solutions"),
        ("Ticket deflection", "/platform/automate/"),
        ("Software &amp; patch", "/platform/it-operations/"),
        ("ITSM &amp; directory orchestration", "/platform/orchestration/"),
    ]),
    ("Company", [
        ("Outcomes", "/#value"),
        ("Analyst recognition", "/#proof"),
        ("About", "/#demo"),
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
<script src="/assets/devmarks.js"></script>
</body>
</html>
"""


def relativise(html, depth):
    """Rewrite root-absolute hrefs/srcs to depth-relative ones.

    GitHub Pages serves a project repo from /<repo>/, so "/assets/site.css"
    resolves to the domain root and 404s. Relative paths work under a subpath
    AND at a domain root, so the same build serves both.
    """
    prefix = "../" * depth

    def rep(m):
        attr, path = m.group(1), m.group(2)
        return '%s="%s"' % (attr, (prefix + path) or "./")

    return re.sub(r'\b(href|src)="/([^"]*)"', rep, html)


def priority(path):
    """Home first, then the three category pillars, then everything else."""
    if path == "/":
        return "1.0"
    if path in ("/platform/", "/digital-experience/",
                "/digital-experience-automation/"):
        return "0.9"
    return "0.8"


def build_sitemap():
    """Generated from PAGES so it can't drift out of sync with the site."""
    today = datetime.date.today().isoformat()
    rows = "\n".join(
        '  <url><loc>https://nanoheal.com%s</loc>'
        '<lastmod>%s</lastmod><priority>%s</priority></url>'
        % (path, today, priority(path))
        for path in sorted(PAGES, key=lambda p: (priority(p) != "1.0",
                                                 priority(p) != "0.9", p)))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           "<!--\n  XML sitemap for nanoheal.com.\n"
           "  GENERATED by build.py from pages.py - do not edit by hand.\n"
           "  Submit at: https://search.google.com/search-console\n-->\n"
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + rows + "\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(xml)
    return "sitemap.xml"


def build():
    written = [build_sitemap()]
    for path, page in PAGES.items():
        body = page["body"].replace("{{AIMX}}", AIMX_DIAGRAM)
        html = SHELL.format(
            title=page["title"], desc=page["desc"], path=path, mark=MARK,
            nav=nav_html(path), body=body, footer=footer_html(),
            scripts=page.get("scripts", ""))
        stripped = path.strip("/")
        depth = stripped.count("/") + 1 if stripped else 0
        html = relativise(html, depth)
        out = ROOT / (path.lstrip("/") + "index.html")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        written.append(str(out.relative_to(ROOT)))
    for w in sorted(written):
        print("wrote", w)


if __name__ == "__main__":
    build()
