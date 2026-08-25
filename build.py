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
        ("What the platform does", [
            ("DEX Intelligence", "/platform/dex-intelligence/",
             "Measure the workplace, and turn every insight into an opportunity"),
            ("Automate Issues", "/platform/automate/",
             "Resolution triggered by the symptom, not by a script"),
            ("Compliance &amp; Governance", "/platform/compliance-governance/",
             "Software, patch and policy, continuously enforced"),
            ("Orchestrate the IT Ecosystem", "/platform/orchestration/",
             "ITSM, directory and any system with an API"),
        ]),
        ("What makes it possible", [
            ("Intelligence &amp; context layer", "/platform/intelligence/",
             "How the right capability gets chosen"),
            ("Workflows in plain language", "/platform/workflows/",
             "Describe it, don't build it"),
            ("Automation library", "/platform/automation-library/",
             "1,200+ configurations on day one"),
            ("Experience score", "/platform/experience-score/",
             "The patented DEX score \u2014 US 9,477,573"),
            ("Continuous improvement", "/platform/manage/",
             "What to automate next, and the proof it worked"),
        ]),
        ("Start here", [
            ("Platform overview", "/platform/",
             "The whole loop on one engine"),
            ("How it works, end to end", "/digital-experience-automation/",
             "Signal \u2192 context \u2192 action \u2192 outcome"),
        ]),
    ]),
    ("Solutions", "/solutions/", [
        ("By outcome", [
            ("Ticket deflection &amp; autoheal", "/solutions/ticket-deflection/",
             "Resolve before the employee calls"),
            ("Employee self-service", "/solutions/self-service/",
             "The fix offered at the moment of failure"),
            ("IT task automation", "/solutions/it-task-automation/",
             "Software, patch and the routine work"),
            ("Compliance &amp; audit readiness", "/solutions/compliance-audit/",
             "Drift corrected, evidence on demand"),
        ]),
        ("By who you are", [
            ("Internal IT", "/solutions/internal-it/",
             "Do more with the team you have"),
            ("Service providers &amp; GSIs", "/solutions/service-providers/",
             "An autonomy layer inside your delivery model"),
            ("OEMs, channel &amp; SMB", "/solutions/oem-channel/",
             "Multi-tenant from the ground up"),
        ]),
        ("Start here", [
            ("Solutions overview", "/solutions/",
             "One platform, positioned for how you work"),
            ("Outcomes &amp; business case", "/resources/outcomes/",
             "What autonomy is worth, with the model"),
        ]),
    ]),
    ("Resources", "/resources/", [
        ("Understand the category", [
            ("What is DEX", "/digital-experience/",
             "Measure, forecast, detect, diagnose, prove"),
            ("What is DXA", "/digital-experience-automation/",
             "The half a dashboard cannot do"),
            ("Why DEX alone isn't enough", "/why-nanoheal/why-dxa/",
             "The category argument"),
            ("Why not scripts", "/why-nanoheal/why-not-scripts/",
             "The technical case, in full"),
        ]),
        ("Proof", [
            ("Outcomes &amp; business case", "/resources/outcomes/",
             "Production numbers and the ROI model"),
            ("Analyst recognition", "/resources/analysts/",
             "Gartner, ISG, Forrester"),
        ]),
    ]),
    ("Company", "/company/", [
        ("Company", [
            ("About Nanoheal", "/company/", "Who we are and what we build"),
            ("Partners", "/company/partners/",
             "GSIs, OEMs and support channels"),
            ("Contact &amp; demo", "/#demo", "See a symptom resolve itself"),
        ]),
    ]),
]

FOOTER_COLS = [
    ("Platform", [
        ("Platform overview", "/platform/"),
        ("DEX Intelligence", "/platform/dex-intelligence/"),
        ("Automate Issues", "/platform/automate/"),
        ("Compliance &amp; Governance", "/platform/compliance-governance/"),
        ("Orchestrate the IT ecosystem", "/platform/orchestration/"),
        ("Intelligence &amp; context layer", "/platform/intelligence/"),
        ("Automation library", "/platform/automation-library/"),
    ]),
    ("Solutions", [
        ("Ticket deflection &amp; autoheal", "/solutions/ticket-deflection/"),
        ("Employee self-service", "/solutions/self-service/"),
        ("IT task automation", "/solutions/it-task-automation/"),
        ("Compliance &amp; audit readiness", "/solutions/compliance-audit/"),
        ("Internal IT", "/solutions/internal-it/"),
        ("Service providers &amp; GSIs", "/solutions/service-providers/"),
        ("OEMs, channel &amp; SMB", "/solutions/oem-channel/"),
    ]),
    ("Resources", [
        ("What is DEX", "/digital-experience/"),
        ("What is DXA", "/digital-experience-automation/"),
        ("Why DEX alone isn't enough", "/why-nanoheal/why-dxa/"),
        ("Why not scripts", "/why-nanoheal/why-not-scripts/"),
        ("Outcomes &amp; business case", "/resources/outcomes/"),
        ("Analyst recognition", "/resources/analysts/"),
    ]),
    ("Company", [
        ("About Nanoheal", "/company/"),
        ("Partners", "/company/partners/"),
        ("Workflows in plain language", "/platform/workflows/"),
        ("Experience score", "/platform/experience-score/"),
        ("Contact", "/#demo"),
    ]),
]

MARK = ('<svg viewBox="0 0 20 20" fill="none" aria-hidden="true">'
        '<path d="M2 11h3.4l2-4.8 2.6 9L12.4 11H18" stroke="#EFEDEB" stroke-width="1.9" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def nav_html(path):
    """Top-level items, each with an optional grouped mega menu."""
    out = []
    for label, href, groups in NAV:
        cur = ' aria-current="page"' if href == path else ""
        if groups:
            cols = []
            for col_title, items in groups:
                links = "".join(
                    f'<a href="{h}">{t}<span>{d}</span></a>' for t, h, d in items)
                cols.append(f'<div class="mcol"><p class="mh">{col_title}</p>{links}</div>')
            out.append(
                f'<li class="has-menu"><a href="{href}"{cur}>{label}</a>'
                f'<div class="menu mega">{"".join(cols)}</div></li>')
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
<script>(function(){{try{{var t=localStorage.getItem("nh-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();</script>
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
<button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle light and dark theme">
<svg class="ic-sun" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.5v2.4M12 19.1v2.4M4.2 4.2l1.7 1.7M18.1 18.1l1.7 1.7M2.5 12h2.4M19.1 12h2.4M4.2 19.8l1.7-1.7M18.1 5.9l1.7-1.7"></path></svg>
<svg class="ic-moon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5z"></path></svg>
</button>
<a class="btn btn-ink" href="/#demo">Schedule a Demo</a>
</div></header>
<main>
{body}
</main>
{footer}
{scripts}
<script src="/assets/theme.js"></script>
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
    if path in ("/platform/", "/solutions/", "/digital-experience/",
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
