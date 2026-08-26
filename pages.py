# -*- coding: utf-8 -*-
"""Page bodies. Edit here, then run `python3 build.py`."""

# ── the AIM-X loop ───────────────────────────────────────────────────────────
# A closed cycle with Intelligence at the hub. The deck's version reads
# left-to-right, which undercuts the "continuous loop" claim; this one shows
# the loop actually closing, and the hub feeding every stage.
AIMX_DIAGRAM = """
<div class="loopwrap">
<svg class="loop" viewBox="0 0 760 600" role="img"
     aria-label="The AIM-X loop. Automate executes the fix on the endpoint. The outcome is
     measured as Experience. Experience reveals the next autonomy opportunity, which Manage
     and evolve prioritises. That produces new capability, which returns to Automate. At the
     centre, Intelligence — the semantic context layer — reads from and writes to every stage.">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7"
            orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="var(--teal)"/>
    </marker>
  </defs>

  <!-- ring arcs -->
  <g fill="none" stroke="var(--teal)" stroke-width="1.6" marker-end="url(#ah)" opacity=".85">
    <path d="M451.2 138.8 A190 190 0 0 1 568.2 341.4"/>
    <path d="M497.0 464.7 A190 190 0 0 1 263.0 464.7"/>
    <path d="M191.8 341.4 A190 190 0 0 1 308.8 138.8"/>
  </g>

  <!-- hub spokes -->
  <g stroke="var(--tx-3)" stroke-width="1.2" stroke-dasharray="3 4" opacity=".6">
    <line x1="380" y1="237" x2="380" y2="179"/>
    <line x1="447.5" y1="354" x2="497.7" y2="383"/>
    <line x1="312.5" y1="354" x2="262.3" y2="383"/>
  </g>

  <!-- arc labels -->
  <g font-size="12.5" fill="var(--tx-2)" text-anchor="middle"
     stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">
    <text x="577.5" y="201">the outcome is measured</text>
    <text x="380" y="543">measurement reveals the next gap</text>
    <text x="182.5" y="201">new capability, no code</text>
  </g>

  <!-- A -->
  <circle cx="380" cy="125" r="54" fill="var(--paper)" stroke="var(--teal)" stroke-width="1.6"/>
  <text x="380" y="140" text-anchor="middle" font-family="Instrument Serif, Georgia, serif"
        font-size="42" fill="var(--teal)">A</text>
  <text x="380" y="36" text-anchor="middle" font-size="15" font-weight="600"
        fill="var(--tx)" letter-spacing=".04em" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">AUTOMATE</text>
  <text x="380" y="55" text-anchor="middle" font-size="12.5" fill="var(--tx-2)" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">the fix runs on the endpoint</text>

  <!-- X -->
  <circle cx="544.5" cy="410" r="54" fill="var(--paper)" stroke="var(--teal)" stroke-width="1.6"/>
  <text x="544.5" y="425" text-anchor="middle" font-family="Instrument Serif, Georgia, serif"
        font-size="42" fill="var(--teal)">X</text>
  <text x="544.5" y="492" text-anchor="middle" font-size="15" font-weight="600"
        fill="var(--tx)" letter-spacing=".04em" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">EXPERIENCE</text>
  <text x="544.5" y="511" text-anchor="middle" font-size="12.5" fill="var(--tx-2)" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">scored, not asserted</text>

  <!-- M -->
  <circle cx="215.5" cy="410" r="54" fill="var(--paper)" stroke="var(--teal)" stroke-width="1.6"/>
  <text x="215.5" y="425" text-anchor="middle" font-family="Instrument Serif, Georgia, serif"
        font-size="42" fill="var(--teal)">M</text>
  <text x="215.5" y="492" text-anchor="middle" font-size="15" font-weight="600"
        fill="var(--tx)" letter-spacing=".04em" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">MANAGE &amp; EVOLVE</text>
  <text x="215.5" y="511" text-anchor="middle" font-size="12.5" fill="var(--tx-2)" stroke="var(--paper)" stroke-width="7" paint-order="stroke" stroke-linejoin="round">what to automate next</text>

  <!-- I hub -->
  <circle cx="380" cy="315" r="78" fill="var(--teal)"/>
  <text x="380" y="303" text-anchor="middle" font-family="Instrument Serif, Georgia, serif"
        font-size="44" fill="var(--paper)">I</text>
  <text x="380" y="332" text-anchor="middle" font-size="12" font-weight="600"
        fill="var(--paper)" letter-spacing=".08em">INTELLIGENCE</text>
  <text x="380" y="351" text-anchor="middle" font-size="11" fill="var(--paper)" opacity=".8">semantic context layer</text>
</svg>

<div class="loop-legend">
  <div><span class="l">A</span><b>Automate</b><span>The symptom triggers a capability. Nothing is scripted, nothing polls.</span></div>
  <div><span class="l">I</span><b>Intelligence</b><span>Reads DEX signals, your SOPs, ITSM history and CMDB to decide what this symptom means here.</span></div>
  <div><span class="l">M</span><b>Manage &amp; evolve</b><span>Finds the next thing worth automating, and proves it was worth it.</span></div>
  <div><span class="l">X</span><b>Experience</b><span>The patented DEX score — the number the loop is optimising.</span></div>
</div>
</div>
"""

# ── scope: what a DEX platform covers vs where Nanoheal goes beyond ──────────
# Written as literal HTML, not built from helper functions. The in-page editor
# saves back by text-matching pages.py's own source, so any content it can
# reach has to already exist here as literal text -- a value only produced at
# render time (e.g. from a Python function call) can never be found and every
# save on it 404s. Same reason each <path>/<circle>/<rect> below is spelled
# with an explicit closing tag rather than self-closed: that's the form the
# browser's own HTML serializer normalizes a live edit to, so the source has
# to match that or the very first save rewrites it out of sync with itself.
SCOPE_FLOW = """
<div class="scope-flow">
  <div class="scope-group">
    <p class="scope-glabel">What every <b>DEX platform</b> covers</p>
    <div class="scope-row">
      <div class="scope-card"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h3.5l2-6 3 12 2-9 1.5 3H21"></path></svg><div class="scope-card-text"><h4>Measure</h4><p>Track performance, application and network experience</p></div><span class="scope-pill">Parity</span></div>
      <span class="scope-arrow"><svg viewBox="0 0 16 10" width="16" height="10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5h13M9 1l5 4-5 4"></path></svg></span>
      <div class="scope-card"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V6M16 20v-8M22 20v-4"></path></svg><div class="scope-card-text"><h4>Forecast</h4><p>Predict degradation before users feel it</p></div><span class="scope-pill good">Ahead</span></div>
      <span class="scope-arrow"><svg viewBox="0 0 16 10" width="16" height="10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5h13M9 1l5 4-5 4"></path></svg></span>
      <div class="scope-card"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"></circle><path d="M20 20l-4.8-4.8"></path></svg><div class="scope-card-text"><h4>Detect</h4><p>Surface anomalies and trace to root cause</p></div><span class="scope-pill good">Ahead</span></div>
    </div>
  </div>
  <div class="scope-group beyond">
    <p class="scope-glabel">Where <b>Nanoheal</b> goes beyond</p>
    <div class="scope-row">
      <div class="scope-card hi"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="11" rx="1.4"></rect><path d="M2 19h20M10 15l2 2 4-4" stroke-width="1.8"></path></svg><div class="scope-card-text"><h4>Resolve at the device</h4><p>Triggered by the symptom the OS reports.</p></div><span class="scope-pill only">Only Nanoheal</span></div>
      <span class="scope-arrow"><svg viewBox="0 0 16 10" width="16" height="10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5h13M9 1l5 4-5 4"></path></svg></span>
      <div class="scope-card"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"></ellipse><path d="M4.5 5.5V12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8V5.5"></path><path d="M4.5 12v6.5c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8V12"></path></svg><div class="scope-card-text"><h4>Run IT operations</h4><p>Software distribution, patch and more &mdash; same engine, no scripts</p></div><span class="scope-pill only">Only Nanoheal</span></div>
      <span class="scope-arrow"><svg viewBox="0 0 16 10" width="16" height="10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5h13M9 1l5 4-5 4"></path></svg></span>
      <div class="scope-card"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7.5 18a4.5 4.5 0 0 1-.7-8.94 5.5 5.5 0 0 1 10.6-1.9A4.5 4.5 0 0 1 17 18H7.5z"></path><rect x="9" y="20.2" width="2.6" height="2.6" rx=".4" stroke-width="1.4"></rect><rect x="12.4" y="20.2" width="2.6" height="2.6" rx=".4" stroke-width="1.4"></rect></svg><div class="scope-card-text"><h4>Orchestrate the ecosystem</h4><p>ServiceNow, AD, any system with a standard API</p></div><span class="scope-pill only">Only Nanoheal</span></div>
    </div>
  </div>
</div>
<div class="scope-brackets">
  <div class="scope-bracket"><span>Device visibility</span></div>
  <div class="scope-bracket teal"><span>Device to entire IT ecosystem</span></div>
</div>
<div class="scope-stats">
  <div class="scope-stat"><span class="ic"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l4 4 10-10"></path></svg></span><span class="scope-stat-label">No scripts to write</span></div>
  <div class="scope-stat"><span class="ic"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20M2 12a10 10 0 0 1 20 0M2 12a10 10 0 0 0 20 0" stroke-width="1.4"></path><path d="M4 4l16 16" stroke-width="1.4"></path></svg></span><span class="scope-stat-label">Real-time issue resolution</span></div>
  <div class="scope-stat"><span class="ic"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3.2 2"></path></svg></span><span class="scope-stat-label">Compliance ad IT automated</span></div>
  <div class="scope-stat"><span class="ic"><svg class="scope-ic" viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.6-3 7.8-7 9-4-1.2-7-4.4-7-9V6z"></path></svg></span><span class="scope-stat-label">IT operations, always on</span></div>
</div>
"""

# ── shared fragments ─────────────────────────────────────────────────────────
CONSOLE = """
<div class="card" role="img" aria-label="A Windows event log entry for a failed print spooler
is recognised, matched to a knowledge entry, and remediated by engine capabilities in 1.6
seconds, with no script deployed and no background probing.">
  <div class="card-top"><span><span class="dot"></span>Endpoint &middot; live</span><span>No polling</span></div>
  <div class="log">
    <div class="ev"><span class="t">00.00</span><span class="m">OS emits <b>Event 7031</b> &mdash; Print Spooler terminated unexpectedly</span></div>
    <div class="ev"><span class="t">00.03</span><span class="m">Engine recognises the symptom <i>as reported</i> &mdash; no probe, no scan</span></div>
    <div class="ev"><span class="t">00.41</span><span class="m">Intelligence matches knowledge <i>KB &middot; spooler-corrupt-queue</i></span></div>
    <div class="ev"><span class="t">00.88</span><span class="m">Capabilities selected: <b>stop service &middot; purge queue &middot; repair key &middot; restart</b></span></div>
    <div class="ev"><span class="t">01.62</span><span class="m">Resolved. Ticket never raised. <i>Knowledge reused fleet-wide</i></span></div>
  </div>
  <div class="card-foot">0 lines of script shipped &middot; 0 background probes</div>
</div>
"""

CTA = """
<section class="band ink" id="demo">
  <div class="wrap"><div class="head">
    <h2 class="h2">See a symptom resolve itself.</h2>
    <p class="lede">Bring us your top three call drivers. We'll show you the same three resolving
 on a live endpoint — with no script written, and nothing left running to watch for them</p>
    <div class="cta">
      <a class="btn btn-solid" href="/#demo">Schedule a Demo</a>
      <a class="btn btn-line" href="/why-nanoheal/why-not-scripts/">Read the technical case</a>
    </div>
  </div></div>
</section>
"""


def phero(crumb, kicker, h1, sub, acts=""):
    return f"""<section class="phero"><div class="wrap">
<p class="crumb">{crumb}</p><p class="k">{kicker}</p>
<h1>{h1}</h1><p class="sub">{sub}</p>{acts}</div></section>"""


def nextcards(items):
    a = "".join(
        f'<a href="{h}"><span class="k">{k}</span><b>{t}</b><span>{d}</span></a>'
        for k, t, h, d in items)
    return f'<div class="next">{a}</div>'


def shot(bar, label, caption, src=None):
    """Product screenshot frame.

    Pass ``src`` (a file in /assets/shots/) to render the real capture; the
    captures are focused crops of the AEX console, not full-window shots, so
    they stay legible at column width. Without ``src`` the grid placeholder
    stands in and ``label`` names what the capture will show.
    """
    alt = label.replace("Screenshot &mdash; ", "").replace("Screenshot — ", "")
    inner = (f'<div class="shot-img"><img src="/assets/shots/{src}" '
             f'alt="Nanoheal console: {alt}" loading="lazy" decoding="async"></div>'
             if src else f'<div class="shot-frame"><span>{label}</span></div>')
    return f"""<figure class="shot">
<div class="shot-bar"><i></i><i></i><i></i><span>{bar}</span></div>
{inner}
<figcaption>{caption}</figcaption>
</figure>"""


def cards(items, three=False):
    a = "".join(
        f'<a href="{h}"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p>'
        f'<span class="more">{m} &rarr;</span></a>' for k, t, h, d, m in items)
    return f'<div class="cards{" three" if three else ""}">{a}</div>'


def metrics(items):
    a = "".join(f'<div class="metric"><em>{e}</em><b>{n}</b><span>{d}</span></div>'
                for e, n, d in items)
    return f'<div class="metrics">{a}</div>'


PAGES = {}

# ── / ────────────────────────────────────────────────────────────────────────
PAGES["/"] = {
 "title": "Nanoheal — The Operating System for the Digital Workplace",
 "desc": "Nanoheal is AI for the digital workplace: one intelligence layer that automates "
         "issues, enforces compliance and governance, and orchestrates the IT ecosystem — "
         "built on DEX intelligence, triggered by the symptom, not a script.",
 "scripts": '<script src="/assets/plaster.js"></script>',
 "body": """
<section class="hero" id="hero">
  <div class="hero-l"><div class="in">
    <p class="k">AI for the digital workplace</p>
    <h1>AI&nbsp;for the digital workplace.</h1>
    <p class="sub">Turning every insight into autonomous action — using context to create the right knowledge and capabilities, acting where the work belongs, and continuously measuring the experience to drive what happens next</p>
    <div class="acts">
      <a class="btn btn-solid" href="/#demo">Schedule a Demo</a>
      <a class="btn btn-line" href="#os">See how it works</a>
    </div>
  </div></div>
  <div class="hero-r">
    <canvas class="plaster" id="plaster" aria-hidden="true"></canvas>
    <div class="in">""" + CONSOLE + """</div>
  </div>
</section>

<div class="trust" id="proof"><div class="wrap trust-in">
  <p class="lab"><a href="/resources/analysts/">Recognised across the DEX category.</a></p>
  <div class="badges">
    <span class="badge"><b>Gartner</b>27+ mentions &middot; 4.6/5 Peer Insights</span>
    <span class="badge"><b>ISG Provider Lens&trade;</b>Rising Star, DEX</span>
    <span class="badge"><b>Forrester</b>DEX Landscape, Q2 2026</span>
    <span class="badge"><b>Patented</b>DEX scoring &middot; US 9,477,573</span>
  </div>
</div></div>

<section class="band bone2" id="os">
  <div class="wrap">
    <div class="head">
      <p class="label">The category</p>
      <h2 class="h2">The operating system for the digital workplace.</h2>
      <p class="lede">Intelligence continuously measures experience, gathers context, identifies new opportunities to automate, resolves issues as they emerge, keeps devices and environments compliant, and orchestrates work across the IT ecosystem</p>
    </div>

    <div class="ostabs">
      <input type="radio" name="ostab" id="ostab-0" class="ostabs-radio" checked>
      <input type="radio" name="ostab" id="ostab-1" class="ostabs-radio">
      <input type="radio" name="ostab" id="ostab-2" class="ostabs-radio">
      <input type="radio" name="ostab" id="ostab-3" class="ostabs-radio">

      <div class="os-layout">
        <div class="os-accordion">
          <div class="os-acc-item">
            <label for="ostab-0" class="os-acc-label">DEX Intelligence</label>
            <div class="os-acc-body" id="obody-0">
              <p class="os-cap-title">DEX intelligence doesn&rsquo;t end in a dashboard</p>
              <p class="os-cap-desc">Continuously measure the digital workplace across devices,
              applications, networks and employee experience. Surface anomalies, trends and
              emerging issues, understand their impact, and turn every insight into an
              opportunity to improve and automate.</p>
              <div style="margin-top:16px">
                <a class="btn btn-line" href="/platform/dex-intelligence/">Inside DEX Intelligence</a>
              </div>
            </div>
          </div>
          <div class="os-acc-item">
            <label for="ostab-1" class="os-acc-label">Automate Issues</label>
            <div class="os-acc-body" id="obody-1">
              <p class="os-cap-title">Turn every symptom into a reusable capability</p>
              <p class="os-cap-desc">The context layer gives intelligence the knowledge needed to extend its capabilities to new symptoms across the OS, applications, and resources — without code. Validate once, then make it available through Autoheal, Self-service, or Assisted IT</p>
              <div style="margin-top:16px">
                <a class="btn btn-line" href="/platform/automate/">How automation works</a>
              </div>
            </div>
          </div>
          <div class="os-acc-item">
            <label for="ostab-2" class="os-acc-label">Compliance &amp; Governance</label>
            <div class="os-acc-body" id="obody-2">
              <p class="os-cap-title">IT management automated. Compliance continuously enforced</p>
              <p class="os-cap-desc">The context layer gives intelligence the knowledge to extend its capabilities without code — automating software, patches, security updates and policies by persona, while continuously detecting and restoring drift to keep the fleet compliant.</p>
              <div style="margin-top:16px">
                <a class="btn btn-line" href="/platform/compliance-governance/">Compliance &amp; governance</a>
              </div>
            </div>
          </div>
          <div class="os-acc-item">
            <label for="ostab-3" class="os-acc-label">Orchestrate the IT Ecosystem</label>
            <div class="os-acc-body" id="obody-3">
              <p class="os-cap-title">The device is just the beginning. The work extends across IT</p>
              <p class="os-cap-desc">Intelligence extends beyond the device — giving human agents and automation the context to act. SOPs, how-to guides and knowledge help IT serve better, while APIs, MCP servers, data and system capabilities become no-code building blocks for analysis, action and orchestration across the IT ecosystem.</p>
              <div style="margin-top:16px">
                <a class="btn btn-line" href="/platform/orchestration/">How orchestration works</a>
              </div>
            </div>
          </div>
        </div>

        <div class="os-visual">
          <div class="os-visual-panel" id="opanel-0"><span>Screenshot &mdash; DEX Intelligence</span></div>
          <div class="os-visual-panel" id="opanel-1"><span>Screenshot &mdash; Automate Issues</span></div>
          <div class="os-visual-panel" id="opanel-2"><span>Screenshot &mdash; Compliance &amp; Governance</span></div>
          <div class="os-visual-panel" id="opanel-3"><span>Screenshot &mdash; Orchestrate the IT Ecosystem</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band" id="scope">
  <div class="wrap">
    <div class="head">
      <p class="label">The foundation underneath</p>
      <h2 class="h2">Solving the Knowing and Doing in DEX</h2>
      <p class="lede">DEX gives IT the intelligence to understand the experience. Nanoheal closes the gap between insight and action — using context to create the knowledge that extends capabilities without code</p>
    </div>
    """ + SCOPE_FLOW + """
    <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-line" href="/digital-experience/">The DEX side</a>
      <a class="btn btn-line" href="/digital-experience-automation/">The DXA side</a>
    </div>
  </div>
</section>

<section class="band bone2" id="value">
  <div class="wrap">
    <div class="head">
      <p class="label">Proven in production</p>
      <h2 class="h2">Most platforms start empty. Nanoheal starts with 1,200+.</h2>
      <p class="lede">Pre-built remediations, IT tasks and compliance configurations ship on day
      one, and your own team extends them in plain language.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn btn-line" href="/platform/automation-library/">Inside the library</a>
        <a class="btn btn-line" href="/resources/outcomes/">Outcomes &amp; business case</a>
      </div>
    </div>
    <p class="label" style="margin-top:44px">Who runs on Nanoheal &mdash; same engine, whether you run 500 endpoints or 200,000</p>
    <div class="g3" style="margin-top:20px">
      <div class="tile"><h3>Enterprise IT.</h3><p>Fortune 1000 estates across manufacturing,
      technology services and SaaS &mdash; typically replacing a DEX tool that measures well and
      acts poorly. <a href="/solutions/internal-it/" style="color:var(--teal)">Internal IT &rarr;</a></p></div>
      <div class="tile"><h3>Global system integrators.</h3><p>Delivered inside an existing managed
      workplace service. Your contract, your client, your delivery model &mdash; with an autonomy
      layer your competitors cannot price.
      <a href="/solutions/service-providers/" style="color:var(--teal)">Service providers &rarr;</a></p></div>
      <div class="tile"><h3>OEMs, support channels and SMB.</h3><p>Multi-tenant from the ground up,
      so the same automation library serves a support channel's whole book of business.
      <a href="/solutions/oem-channel/" style="color:var(--teal)">OEM &amp; channel &rarr;</a></p></div>
    </div>
  </div>
</section>

<section class="band" id="solutions">
  <div class="wrap">
    <div class="head">
      <p class="label">Who it&rsquo;s for</p>
      <h2 class="h2">One platform. different value, depending who’s running it.</h2>
      <p class="lede">Whether IT sits inside your company or you deliver it as a service, it&rsquo;s
      the same autonomous platform &mdash; positioned for how you work.</p>
    </div>
    <div class="forwho-grid">
      <div class="forwho">
        <p class="label">For internal IT</p>
        <h3>Do more with the team you have.</h3>
        <div class="linkrow"><b>Fewer tickets</b><span>Resolve issues before they reach the service desk.</span></div>
        <div class="linkrow"><b>Less manual work</b><span>Automate IT tasks across devices and systems.</span></div>
        <div class="linkrow"><b>Better experience</b><span>Improve DEX continuously, not just measure it.</span></div>
        <div class="linkrow"><b>A more autonomous workplace</b><span>Every resolved symptom becomes reusable knowledge, so the estate needs less firefighting over time.</span></div>
        <div style="margin-top:22px"><a class="btn btn-line" href="/solutions/internal-it/">For internal IT</a></div>
      </div>
      <div class="forwho">
        <p class="label">For service providers</p>
        <h3>Deliver more value from the service you already run.</h3>
        <div class="linkrow"><b>Differentiate your service</b><span>Add autonomy without changing your delivery model.</span></div>
        <div class="linkrow"><b>Protect margin</b><span>Deflection comes from automation and resolution, not reducing the team.</span></div>
        <div class="linkrow"><b>Prove outcomes</b><span>Measure the improvement and make autonomy an outcome you can stand behind.</span></div>
        <div class="linkrow"><b>Expand coverage</b><span>Start with pre-built capabilities and continuously add more without an engineering backlog.</span></div>
        <div style="margin-top:22px"><a class="btn btn-line" href="/solutions/service-providers/">For service providers</a></div>
      </div>
    </div>
  </div>
</section>
""" + CTA}

# ── /platform/ ───────────────────────────────────────────────────────────────
PAGES["/platform/"] = {
 "title": "Platform \u2014 the operating system for the digital workplace \u2014 Nanoheal",
 "desc": "One platform that measures the digital workplace, automates the issues it finds, "
         "keeps the estate compliant and orchestrates the rest of IT \u2014 on one engine, "
         "one context layer and one knowledge library.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Platform',
   "Platform overview",
   "The operating system for the digital workplace.",
   "Intelligence continuously measures experience, gathers context, identifies new opportunities "
   "to automate, resolves issues as they emerge, keeps devices and environments compliant, and "
   "orchestrates work across the IT ecosystem \u2014 all on one engine, one context layer and "
   "one knowledge library.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/digital-experience-automation/">How it works, end to end</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">What the platform does</p>
      <h2 class="h2">Four things, and they are not four products.</h2>
      <p class="lede">Each one is the input to the next. Measurement finds the opportunity,
      automation closes it, governance keeps it closed, and orchestration carries the work into
      the systems where the rest of it lives.</p>
    </div>
    """ + cards([
      ("01", "DEX Intelligence", "/platform/dex-intelligence/",
       "Continuously measure devices, applications, networks and employee experience. Surface "
       "anomalies, trends and emerging issues, understand their impact, and turn every insight "
       "into an opportunity to improve and automate.",
       "DEX intelligence doesn't end in a dashboard"),
      ("02", "Automate Issues", "/platform/automate/",
       "The context layer gives intelligence the knowledge to extend its capabilities to new "
       "symptoms across the OS, applications and resources &mdash; without code. Validate once, "
       "then deliver through autoheal, self-service or assisted IT.",
       "Turn every symptom into a reusable capability"),
      ("03", "Compliance &amp; Governance", "/platform/compliance-governance/",
       "Software, patches, security updates and policies automated by persona, with drift "
       "continuously detected and restored &mdash; on the same engine that heals the device, "
       "not a second agent.",
       "IT management automated, compliance enforced"),
      ("04", "Orchestrate the IT Ecosystem", "/platform/orchestration/",
       "The device is where the symptom shows up, rarely where the work ends. APIs, MCP servers, "
       "data and system capabilities become no-code building blocks for analysis, action and "
       "orchestration across IT.",
       "The device is just the beginning"),
    ]) + """
    """ + shot("nanoheal &middot; console",
               "Screenshot &mdash; Experience — report catalog",
               "<b>One console, four jobs.</b> Automate, Manage, Experience and "
               "Administration are branches of the same navigation rather than four "
               "products sharing a login — here, the Experience branch and its report "
               "catalog. The estate you measure is the estate you act on.",
               "console-experience.png") + """
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">What makes it possible</p>
      <h2 class="h2">The layer under all four.</h2>
      <p class="lede">Every pillar above runs on the same three things: a context layer that
      decides what a symptom means <em>here</em>, a fixed capability engine that already knows how
      to act, and a knowledge library that starts full and keeps growing.</p>
    </div>
    """ + nextcards([
      ("I", "Intelligence &amp; context", "/platform/intelligence/",
       "How the right capability gets chosen, and why it isn't generated code."),
      ("NL", "Workflows in plain language", "/platform/workflows/",
       "Describe the task. The context layer compiles it."),
      ("1,200+", "Automation library", "/platform/automation-library/",
       "What ships on day one, and how it grows without an engineering backlog."),
    ]) + nextcards([
      ("X", "Experience score", "/platform/experience-score/",
       "The patented DEX score \u2014 the number the whole loop optimises."),
      ("M", "Continuous improvement", "/platform/manage/",
       "What to automate next, ranked by what it would actually return."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/",
       "The technical case for symptom-triggered automation, in full."),
    ]) + """
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The framework underneath</p>
      <h2 class="h2">AIM-X. Automate with Intelligence. Manage the eXperience.</h2>
      <p class="lede">Internally the four pillars run as a closed loop we call AIM-X. Nobody has to
      learn the acronym to buy the platform &mdash; but if you want to know why coverage compounds
      instead of stalling, this is the mechanism.</p>
    </div>
    """ + AIMX_DIAGRAM + """
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Why a loop and not a module list</p>
      <h2 class="h2">A catalogue of parts doesn&rsquo;t compound. A loop does.</h2>
    </div>
    <div class="prose" style="margin-top:32px">
      <p>Every DEX platform on the market is organised the same way: a set of named modules you
      buy and wire together. That structure tells you what the vendor built. It doesn't tell you
      what happens on day ninety, when the estate has drifted and the automations somebody wrote
      in month one have started failing.</p>
      <p>AIM-X is organised around what happens <strong>after</strong> an automation exists,
      because that is where the economics actually live. An automation that runs once is a
      script. An automation whose outcome is measured, whose measurement reveals the next gap,
      and whose next gap becomes new capability without an engineering project &mdash; that is a
      system that gets cheaper to extend over time.</p>
      <p class="pull">Coverage compounds when the next automation costs almost nothing. That is
      the entire argument, and every part of AIM-X exists to serve it.</p>
      <p>The four pillars are not four products. They are four things that have to be true at the
      same time for the loop to close, and they run on one engine, one context layer and one
      knowledge library.</p>
    </div>
  </div>
</section>
""" + CTA}

# ── /digital-experience/ ─────────────────────────────────────────────────────
PAGES["/digital-experience/"] = {
 "title": "Digital Experience (DEX) — Nanoheal",
 "desc": "Everything DEX should tell you: measure, forecast, detect, diagnose and prove. The "
         "measurement foundation Digital Experience Automation is built on.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Digital Experience',
   "Digital Experience",
   "Everything DEX should tell you.",
   "Measurement is the foundation, not the finish line. Nanoheal scores the digital workplace on "
   "a patented DEX methodology — devices, applications, network and the experience the "
   "employee actually has — and that measurement is what makes autonomous action safe to "
   "trust.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/digital-experience-automation/">Then see what DXA adds</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The five questions</p>
      <h2 class="h2">What a DEX platform has to answer.</h2>
    </div>
    <div class="tl">
      <div><p class="w">Measure</p><h3>What&rsquo;s happening?</h3><p>Fleet-wide performance,
      stability, application and network experience, scored on a patented methodology.</p></div>
      <div><p class="w">Forecast</p><h3>What&rsquo;s likely to happen?</h3><p>Capacity, drift and
      failure patterns building across the estate, before the employee feels them.</p></div>
      <div><p class="w">Detect</p><h3>What&rsquo;s changed?</h3><p>Anomalies nobody wrote a rule
      for, surfaced as they emerge rather than after the call volume moves.</p></div>
      <div><p class="w">Diagnose</p><h3>Why is it happening?</h3><p>The signal traced back to a
      root cause an engineer can act on &mdash; or that the context layer can act on itself.</p></div>
    </div>
    <div class="tl" style="margin-top:34px">
      <div><p class="w">Prove</p><h3>Did the experience actually improve?</h3><p>The DEX Score is
      the number the whole loop optimises, so improvement is measured rather than asserted.
      Patented &mdash; US 9,477,573.</p></div>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">What gets measured</p>
      <h2 class="h2">The whole digital workplace, not just the endpoint.</h2>
    </div>
    <div class="g4" style="margin-top:34px">
      <div class="tile"><h3>Device experience</h3><p>Performance, stability, boot and login,
      battery, crashes and the hardware refresh signal.</p></div>
      <div class="tile"><h3>Application experience</h3><p>Responsiveness, failures and adoption
      across the applications people actually work in.</p></div>
      <div class="tile"><h3>Network &amp; collaboration</h3><p>Connectivity, latency and meeting
      quality &mdash; wherever the employee happens to be working.</p></div>
      <div class="tile"><h3>Employee experience</h3><p>Sentiment and reported friction, scored
      alongside the telemetry rather than in a separate survey tool.</p></div>
    </div>
    """ + shot("nanoheal &middot; dashboards",
               "Screenshot &mdash; report catalog",
               "<b>Twenty-four finished reports, not a query builder.</b> Leadership summary, "
               "endpoint scorecards, application health, network quality, workforce sentiment, "
               "industry benchmarks and the IT-service numbers &mdash; categorised, searchable "
               "and live on day one.",
               "dex-reports.png") + """
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The bridge</p>
      <h2 class="h2">DEX tells you what needs attention. DXA does something about it.</h2>
      <p class="lede">Every capability on this page is table stakes for a serious DEX platform,
      and we hold that table. The difference begins in the seconds after the dashboard would
      have raised an alert &mdash; when the symptom becomes a trigger instead of a ticket.</p>
    </div>
    """ + nextcards([
      ("&rarr;", "Digital Experience Automation", "/digital-experience-automation/",
       "What happens after the insight: context, action and outcome."),
      ("&rarr;", "Observe &amp; predict", "/platform/dex-intelligence/",
       "Analytics, forecasting and anomaly detection in depth."),
      ("&rarr;", "Experience scoring", "/platform/experience-score/",
       "The patented DEX score, and why improvement is scored not claimed."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /digital-experience-automation/ ──────────────────────────────────────────
PAGES["/digital-experience-automation/"] = {
 "title": "Digital Experience Automation (DXA) — Nanoheal",
 "desc": "DEX tells you. DXA acts. Digital Experience Automation connects experience "
         "intelligence to autonomous action, so problems don't just get detected — they get "
         "resolved, from the device to the entire IT ecosystem.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Digital Experience Automation',
   "Digital Experience Automation",
   "DEX tells you. DXA acts.",
   "Digital Experience Automation connects experience intelligence to contextual understanding "
   "and autonomous action — so problems don’t just get detected, they get resolved. It "
   "is not automation bolted onto analytics. It is automation driven by what the analytics mean.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/why-nanoheal/why-dxa/">Why DEX alone isn&rsquo;t enough</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The loop</p>
      <h2 class="h2">Insight becomes action. Action becomes the next insight.</h2>
      <p class="lede">This is the part a dashboard cannot do on its own. Each stage feeds the
      next, and the outcome of every action re-enters the loop as evidence.</p>
    </div>
    <div class="tl">
      <div><p class="w">Insight</p><h3>The signal arrives</h3><p>The OS reports a symptom, or DEX
      measurement surfaces a pattern nobody wrote a rule for.</p></div>
      <div><p class="w">Context</p><h3>What it means here</h3><p>The semantic context layer reads
      it against DEX signals, your SOPs, ITSM history and CMDB.</p></div>
      <div><p class="w">Action</p><h3>The right capability runs</h3><p>Not a script &mdash; a
      sealed, versioned capability the engine already exposes, with parameters supplied.</p></div>
      <div><p class="w">Outcome</p><h3>The experience is scored</h3><p>The result is measured
      against the DEX score, and that measurement becomes the next insight.</p></div>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Why it compounds</p>
      <h2 class="h2">Created once. Reused everywhere.</h2>
      <p class="lede">A new symptom becomes a capability, validated once, then available to the
      whole estate through every delivery mode. This is why coverage grows instead of stalling
      at the top few call drivers.</p>
    </div>
    <div class="tl" style="margin-top:44px">
      <div><p class="w">Step one</p><h3>New symptom appears</h3><p>Something the estate has not
      seen before, surfaced as it happens.</p></div>
      <div><p class="w">Step two</p><h3>Intelligence creates capability</h3><p>The context layer
      assembles it from what a device can already do. No engineering project.</p></div>
      <div><p class="w">Step three</p><h3>Validated once</h3><p>Reviewed and sealed. Guardrailed,
      versioned, and safe to run at fleet scale.</p></div>
      <div><p class="w">Step four</p><h3>Reused everywhere</h3><p>Autoheal, self-service or
      assisted IT &mdash; the same knowledge, delivered whichever way suits.</p></div>
    </div>
    <div class="ps" style="margin-top:44px">
      <div class="fix">
        <p class="t">On the device</p>
        <h3>Autoheal &middot; self-service &middot; assisted IT</h3>
        <p>The same validated capability, delivered silently, offered to the employee, or handed
        to an agent with the fix already assembled.</p>
      </div>
      <div class="fix">
        <p class="t">Beyond the device</p>
        <h3>ITSM &middot; IT management &middot; workplace platforms</h3>
        <p>When resolution needs a ticket updated, a licence assigned or a group changed, the
        same context layer acts there too &mdash; without code.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">Go deeper</p>
      <h2 class="h2">The mechanism, in detail.</h2>
    </div>
    """ + nextcards([
      ("&rarr;", "Why DXA", "/why-nanoheal/why-dxa/",
       "Why DEX alone isn&rsquo;t enough, and why scripted automation stalls."),
      ("&rarr;", "Intelligence", "/platform/intelligence/",
       "The semantic context layer that decides what a symptom means."),
      ("&rarr;", "Automate", "/platform/automate/",
       "Resolution without a script, delivered three ways."),
    ]) + nextcards([
      ("&rarr;", "Orchestration", "/platform/orchestration/",
       "Acting across ITSM, directory and any system with a standard API."),
      ("&rarr;", "IT operations", "/platform/compliance-governance/",
       "Software, patch and policy on the same engine."),
      ("&rarr;", "Digital Experience", "/digital-experience/",
       "The DEX measurement foundation underneath all of it."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /why-nanoheal/why-dxa/ ───────────────────────────────────────────────────
PAGES["/why-nanoheal/why-dxa/"] = {
 "title": "Why DEX alone isn't enough — Nanoheal",
 "desc": "DEX solved knowing. Traditional automation only partly solved doing, because every "
         "fix became a software project. Digital Experience Automation closes the gap.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/digital-experience-automation/">DXA</a> '
   '&nbsp;/&nbsp; Why DXA',
   "The argument",
   "Why DEX alone isn&rsquo;t enough.",
   "DEX solved the first half of the problem: knowing what is happening. Automation was supposed "
   "to solve the second half. It mostly didn’t — because in the prevailing model, every "
   "fix is a software project with a maintenance tail.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/why-nanoheal/why-not-scripts/">The full technical case</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">Two halves</p>
      <h2 class="h2">One was solved. One was outsourced to your engineers.</h2>
    </div>
    <div class="ps" style="margin-top:44px">
      <div>
        <p class="t">The first half &mdash; solved</p>
        <h3>Know what is happening.</h3>
        <p>DEX platforms measure, forecast, detect and diagnose across the digital workplace.
        This part genuinely works, and the category deserves the credit for it.</p>
      </div>
      <div>
        <p class="t">The second half &mdash; still open</p>
        <h3>Do something about it.</h3>
        <p>Resolution stayed manual, or became automation that somebody has to author. The
        knowing got cheaper every year. The doing didn&rsquo;t.</p>
      </div>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Why automation stalled</p>
      <h2 class="h2">Every fix became a software project.</h2>
      <p class="lede">The economics are what stop coverage expanding. Each new automation carries
      the same cycle, so teams rationally stop at the highest-return issues and leave the long
      tail to the service desk.</p>
    </div>
    <div class="tl" style="margin-top:44px">
      <div><p class="w">Script</p><h3>Someone writes code</h3><p>New code for every symptom, and
      every variation of it.</p></div>
      <div><p class="w">Test &amp; deploy</p><h3>Ship it to the fleet</h3><p>Payloads accumulate;
      every fix adds weight to every endpoint.</p></div>
      <div><p class="w">Maintain</p><h3>Keep it alive</h3><p>It polls to catch the symptom, burning
      resources on machines that are mostly fine.</p></div>
      <div><p class="w">Break</p><h3>Then the estate moves</h3><p>A patch, a policy, a new OS build
      &mdash; and it fails silently until somebody notices.</p></div>
    </div>
    <p class="pull" style="margin-top:36px">Coverage stalls not because teams lack ambition, but
    because the next automation costs almost as much as the last one.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The resolution</p>
      <h2 class="h2">DXA closes the gap.</h2>
      <p class="lede">When the symptom itself is the trigger and capability is assembled from
      context rather than authored as code, the cost of the next automation approaches zero
      &mdash; and coverage compounds instead of plateauing.</p>
    </div>
    <div class="tl">
      <div><p class="w">Insight</p><h3>The symptom is reported</h3><p>By the OS, or by DEX
      measurement. Detection costs nothing extra.</p></div>
      <div><p class="w">Context</p><h3>Meaning is resolved</h3><p>Against your SOPs, ITSM history
      and CMDB &mdash; what this means <em>here</em>.</p></div>
      <div><p class="w">Capability</p><h3>Action is assembled</h3><p>From what the engine can
      already do, not from newly authored code.</p></div>
      <div><p class="w">Experience</p><h3>The outcome is scored</h3><p>And the score reveals the
      next gap worth closing.</p></div>
    </div>
    """ + nextcards([
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/",
       "The full technical case against script-based automation."),
      ("&rarr;", "Digital Experience Automation", "/digital-experience-automation/",
       "The category, the loop and the reusable-capability model."),
      ("&rarr;", "Manage &amp; evolve", "/platform/manage/",
       "How coverage compounds instead of stalling."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/automate/ ──────────────────────────────────────────────────────
PAGES["/platform/automate/"] = {
 "title": "Automate Issues — resolution without a script — Nanoheal",
 "desc": "Every remediation is normally a bespoke software project. Nanoheal triggers on the "
         "symptom the OS already reports and executes governed capabilities instead of code.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Automate Issues',
   "02 &mdash; Automate Issues",
   "Remediation is a software project. It shouldn&rsquo;t be.",
   "Specify, script, test, approve, publish &mdash; then maintain it forever as the estate drifts. "
   "That cost is why automation coverage stops at the top call drivers everywhere else \u2014 and "
   "why the routine work of running an estate never gets automated at all.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">The economics decide what gets automated &mdash; not the need.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Weeks of engineering per fix.</h3>
      <p>A ticket pattern is identified. An engineer writes a script. It's tested against a
      handful of builds, security-reviewed, approved, packaged and published. Weeks later, one
      issue is covered &mdash; and the clock starts on maintaining it.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Knowledge, validated once.</h3>
      <p>The fix is described in plain language and compiled into sealed knowledge. No code is
      written or generated, so there is nothing to security-review line by line, and nothing that
      breaks when a build changes underneath it.</p></div>
    </div>

    """ + shot("nanoheal &middot; workflow builder",
               "Screenshot &mdash; Workflow timeline — trigger",
               "<b>The symptom is the first line of the automation.</b> A workflow opens "
               "with WHEN, and WHEN is a condition the operating system already reports — "
               "here, a high disk usage alert. Nothing was deployed to go looking for it.",
               "workflow-timeline.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Detection</p>
        <h3>The operating system already told you. Everything else asks again.</h3>
        <p class="lead">A script cannot know a service died unless something checks. So it stays
        resident and polls &mdash; spending CPU, memory and battery on machines that are fine, to
        catch the small fraction that aren't.</p>
        <div class="prose" style="margin-top:20px">
          <p>Nanoheal takes the signal the OS emits anyway: the event log entry, the service
          state change, the crash, the error dialog the user is looking at. The symptom
          <strong>is</strong> the trigger. There is nothing to schedule and nothing left running
          in the background, which is why the endpoint footprint doesn't grow as coverage does.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Execution</p>
        <h3>The engine already knows how. Intelligence only has to choose.</h3>
        <p class="lead">Device operations are exposed as a governed capability API. The knowledge
        layer describes <em>what</em> to do; the engine owns <em>how</em>.</p>
        <div class="caps">
          <div class="cap"><span class="k">FS</span><b>Files &amp; folders</b><span>Delete, move, copy, repair permissions, reclaim space</span></div>
          <div class="cap"><span class="k">REG</span><b>Registry &amp; plists</b><span>Create, modify, remove and restore keys, with rollback</span></div>
          <div class="cap"><span class="k">SVC</span><b>Services &amp; processes</b><span>Stop, start, reset, terminate, re-register, repair dependencies</span></div>
          <div class="cap"><span class="k">CFG</span><b>Config &amp; policy</b><span>Settings, profiles, drift correction, compliance enforcement</span></div>
          <div class="cap"><span class="k">APP</span><b>Software &amp; patch</b><span>Install, repair, roll back, version control, licence reclaim</span></div>
          <div class="cap"><span class="k">NET</span><b>Network</b><span>Adapters, DNS, proxy, VPN, Wi-Fi profile repair</span></div>
          <div class="cap"><span class="k">USR</span><b>Identity &amp; profile</b><span>Directory actions, profile repair, credential and session tasks</span></div>
          <div class="cap"><span class="k">ORCH</span><b>Beyond the device</b><span>ITSM tickets and changes, IT management platforms, workplace enablers</span></div>
        </div>
        <div class="prose" style="margin-top:24px">
          <p>Because the capability set is fixed and signed, the variable part of an automation is
          just its parameters. That is why a new fix is kilobytes of knowledge rather than a
          codebase, and why pushing a thousand of them doesn't bloat the agent.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Scope</p>
        <h3>Three classes of work. One engine.</h3>
        <p class="lead">Healing a device and running a device are the same primitive operations
        against files, registry, services and configuration. Nanoheal does not separate them into
        different products, because the engine does not distinguish between them.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Resolve.</h3><p>Remediation triggered by the symptom the OS
          reports, or by a forecast before the symptom arrives.</p></div>
          <div class="tile"><h3>Run.</h3><p>Software distribution, patch management and routine IT
          tasks &mdash; the day-to-day operation of the estate.
          <a href="/platform/compliance-governance/" style="color:var(--teal)">IT operations &rarr;</a></p></div>
          <div class="tile"><h3>Enforce.</h3><p>Device compliance policy, with drift treated as a
          symptom that triggers its own correction rather than a line in a report.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; Delivery</p>
        <h3>One fix, three ways to deliver it.</h3>
        <p class="lead">The same validated knowledge serves all three paths. You don't rebuild it
        per channel.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Autoheal.</h3><p>It resolves before anyone notices. No ticket, no
          contact, no employee interruption &mdash; this is the 17% in production at a Fortune 100
          manufacturer.</p></div>
          <div class="tile"><h3>Self Help.</h3><p>The employee is offered the fix at the moment
          of failure and applies it themselves. Deflection without the service desk touching it.</p></div>
          <div class="tile"><h3>Remote Execution.</h3><p>The service desk runs the same capability
          against a device, a group or a whole site in a single action &mdash; no runbook to
          follow, no elevation risk.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">05 &mdash; Day one</p>
        <h3>1,200+ configurations, before you build anything.</h3>
        <p class="lead">Remediations, IT tasks and policy compliance, matched against your existing
        top call drivers on the first day &mdash; not an empty canvas.</p>
        <div class="prose" style="margin-top:20px">
          <p>Worth a direct comparison: the closest published figure in the category is roughly
          220 automations alongside 1,300 sensors. Sensors measure. Configurations act. The gap
          between those two numbers is the gap this page is about.
          <a href="/platform/automation-library/" style="color:var(--teal)">See what ships on day
          one &rarr;</a></p>
        </div>
      </div>

      <div class="issue">
        <p class="n">06 &mdash; Change control</p>
        <h3>Autonomy the change board can sign.</h3>
        <p class="lead">The objection to unattended action is never the technology. It is the
        question of who authorised it, against which population, and how it is reversed. That is
        answered by structure, not by assurances.</p>
        <div class="tblwrap" style="margin-top:22px">
          <table class="spec">
            <thead><tr><th>Step</th><th>What happens</th><th>What is recorded</th></tr></thead>
            <tbody>
              <tr><td>Author</td><td>The workflow is written and validated once</td><td>Author, version, capability set, action risk per step</td></tr>
              <tr><td>Link scope</td><td>It is attached to a device classification &mdash; a site, a persona, a business unit</td><td>Which populations, linked by whom</td></tr>
              <tr><td>Stage</td><td>The link becomes a pending change, not a live one</td><td>Change count per group, base version, last modified by</td></tr>
              <tr><td>Publish</td><td>Staged changes are released to the estate together</td><td>Publish event, group, operator, time</td></tr>
              <tr><td>Execute</td><td>The engine runs it when the trigger fires</td><td>Per-device outcome &mdash; success, failed, pending</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>Nothing goes live because someone edited a profile. Linking an automation to a group
          <em>stages</em> a change; a separate publish step releases it. That gap is deliberate: it
          is where review, batching and a change window fit, and it is why the estate does not move
          under you while an operator is still thinking.</p>
          <p>Every step also carries an action-risk classification, so the difference between
          clearing a cache and touching a service is visible at authoring time rather than
          discovered at run time.</p>
          <p class="pull">Unattended does not mean unaccounted for. Every execution resolves to an approved version, a scoped population and a named operator.</p>
        </div>
        """ + shot("nanoheal &middot; execution history",
               "Screenshot &mdash; execution history",
               "<b>The record the chain leaves.</b> Each execution carries the automation, the "
               "machine, the capability behind it, the class of work &mdash; remediation, "
               "software distribution, inventory &mdash; and the outcome. Success, failed and "
               "pending all stay on the same record.",
               "exec-history.png") + """
      </div>
    </div>

    """ + nextcards([
      ("I", "Intelligence", "/platform/intelligence/", "How the right capability gets chosen."),
      ("M", "Manage &amp; evolve", "/platform/manage/", "How coverage keeps growing."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/", "The full technical case."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/intelligence/ ──────────────────────────────────────────────────
PAGES["/platform/intelligence/"] = {
 "title": "Intelligence — the semantic context layer — Nanoheal",
 "desc": "Telemetry tells you what happened. It doesn't know how your organisation resolves it. "
         "The semantic context layer reads DEX signals, SOPs, ITSM history and CMDB together.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Intelligence',
   "I &mdash; Intelligence",
   "Telemetry says what happened. Not what your organisation does about it.",
   "Two identical crashes on two machines are not the same incident. One is a known driver "
   "conflict on a build you're retiring; the other is a finance laptop three days from an audit. "
   "The signal is identical. The right action is not \u2014 and working out the difference is what "
   "the context layer is for.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Every DEX platform has the signal. Almost none have the context.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Analytics, then a human.</h3>
      <p>The dashboard flags an anomaly and raises an alert. From there a person reads the
      knowledge base, checks the CMDB, recalls what the team did last time, and decides. That
      judgement never becomes part of the system &mdash; it leaves when they do.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Judgement, encoded.</h3>
      <p>The semantic context layer holds what your organisation knows alongside what the fleet is
      reporting, so the decision about what a symptom means <em>here</em> can be made without a
      person in the loop &mdash; and made the same way every time.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; What it reads</p>
        <h3>Four sources, resolved against each other.</h3>
        <div class="tblwrap">
          <table class="spec">
            <thead><tr><th>Source</th><th>What it contributes</th><th>Without it</th></tr></thead>
            <tbody>
              <tr><td>DEX analytics</td><td>Performance, crashes, drift, availability, behaviour across the fleet</td><td>You can't tell a one-off from a pattern</td></tr>
              <tr><td>IT knowledge &amp; SOPs</td><td>How your organisation actually resolves this, including the steps that aren't written down anywhere else</td><td>Every fix is generic, not yours</td></tr>
              <tr><td>ITSM history</td><td>Incidents, problems, changes, what was tried before and whether it held</td><td>You repeat resolutions that already failed</td></tr>
              <tr><td>CMDB &amp; policy</td><td>Asset, owner, role, entitlement, compliance obligation, change freeze</td><td>You act correctly on a machine you shouldn't have touched</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; What it writes</p>
        <h3>It doesn&rsquo;t pick from a library. It authors the entry.</h3>
        <p class="lead">This is the part that is easiest to miss and hardest to copy. Intelligence
        does not merely match a symptom to a pre-existing fix &mdash; it works out which engine
        capabilities the situation requires, in what order, with what parameters, and writes that
        as a new knowledge entry.</p>
        <div class="prose" style="margin-top:20px">
          <p>So the library is not a fixed catalogue that ships and then ages. It is the
          accumulating output of the context layer meeting situations it has not seen before. A
          human validates each new entry once; from then on it is permanent, reusable capability.</p>
          <p class="pull">The competition ships a library and hopes it covers you. Nanoheal ships
          the thing that writes the library.</p>
          <p>The same mechanism produces every class of work on this platform &mdash;
          <a href="/platform/automate/" style="color:var(--teal)">remediation</a>,
          <a href="/platform/compliance-governance/" style="color:var(--teal)">software, patch and policy</a>,
          and <a href="/platform/orchestration/" style="color:var(--teal)">actions in ITSM, directory
          and other IT systems</a>. One authoring mechanism, not four.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What it decides</p>
        <h3>Which capability, with which parameters.</h3>
        <p class="lead">This is the part that replaces scripting. The intelligence doesn't
        generate code &mdash; it selects from the engine's capability set and supplies the
        variation.</p>
        <div class="prose" style="margin-top:20px">
          <p>A corrupt print queue needs a service stopped, a specific path purged, a specific
          registry key repaired, and the service restarted. On a different build the path and the
          key differ. Script-based automation handles that with branching logic that somebody has
          to maintain. Nanoheal handles it as parameters supplied by the knowledge base against a
          fixed, signed capability &mdash; so the variation lives in data, not in code.</p>
          <p class="pull">The capability set is what a device can do. The knowledge base is what
          your organisation would do. Intelligence is the join.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; Where it acts</p>
        <h3>The endpoint is one destination, not the only one.</h3>
        <p class="lead">Reasoning across the estate is only useful if it can act across the estate.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Device.</h3><p>Endpoint remediation, plus
          <a href="/platform/compliance-governance/" style="color:var(--teal)">software, patch and policy</a>
          &mdash; all on the one capability engine.</p></div>
          <div class="tile"><h3>ITSM and directory.</h3><p>Creates, updates and closes tickets and
          changes; acts in Active Directory and identity platforms.</p></div>
          <div class="tile"><h3>Anything with a standard API.</h3><p>Integrated by description
          rather than by code &mdash; see
          <a href="/platform/orchestration/" style="color:var(--teal)">Orchestration</a>.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">05 &mdash; What governs it</p>
        <h3>Policies, priorities and guardrails, checked before anything runs.</h3>
        <div class="prose" style="margin-top:20px">
          <p>Autonomy without constraint is not a feature anyone in a regulated estate wants.
          Every action resolves against the policy set first: what may be touched, on which
          assets, under whose approval, during which windows, and what happens if it fails.
          Capabilities are sealed and versioned, so what ran is always reconstructable after the
          fact.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("A", "Automate", "/platform/automate/", "What the capability API can actually do."),
      ("M", "Manage &amp; evolve", "/platform/manage/", "Turning outcomes into the next automation."),
      ("X", "Experience", "/platform/experience-score/", "Proving any of it worked."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/manage/ ────────────────────────────────────────────────────────
PAGES["/platform/manage/"] = {
 "title": "Manage & evolve — where autonomy goes next — Nanoheal",
 "desc": "Automation coverage stalls at the top call drivers because each new fix costs as much "
         "as the last. Manage & evolve is how coverage compounds into the long tail instead.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Manage &amp; evolve',
   "M &mdash; Manage &amp; evolve",
   "Coverage stalls at the top call drivers. It doesn&rsquo;t have to.",
   "Every automation programme starts with the same twenty issues, because those are the only "
   "ones that justify the build cost. The long tail behind them is most of the ticket volume, "
   "and it never gets built.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">The second hundred automations are the hard part.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Maintenance eats the roadmap.</h3>
      <p>Coverage grows for two quarters, then flattens. The team that was building new
      automations is now keeping the existing ones alive through OS updates, policy changes and
      estate drift. Net new coverage approaches zero while the backlog keeps growing.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>The next one costs almost nothing.</h3>
      <p>Because a fix is validated knowledge against a signed capability set rather than code,
      there is no per-automation maintenance burden. The team's capacity goes into finding the
      next opportunity instead of defending the last one.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Identify</p>
        <h3>The system knows where the manual work still is.</h3>
        <p class="lead">Ticket patterns, repeated diagnostics, recurring symptoms with no matching
        knowledge entry &mdash; these are autonomy opportunities, and they surface from the data
        rather than from a workshop.</p>
      </div>
      <div class="issue">
        <p class="n">02 &mdash; Prioritise</p>
        <h3>Ranked by what it would actually return.</h3>
        <p class="lead">Volume, handling cost, employee impact and DEX score contribution, weighed
        together. The output is an ordered list of what to automate next and what it is worth
        &mdash; which is the conversation IT leadership is usually missing.</p>
      </div>
      <div class="issue">
        <p class="n">03 &mdash; Expand</p>
        <h3>Created once, then permanent.</h3>
        <p class="lead">AI drafts the knowledge from plain intent. IT validates it once. It is
        compiled, sealed and becomes reusable fleet-wide capability &mdash; available to autoheal,
        self-service and the service desk simultaneously.</p>
        <div class="prose" style="margin-top:20px">
          <p class="pull">Solve an issue once and it is solved forever. That sentence is only true
          if maintaining the solution is free, which is the whole reason the fix isn't code.</p>
        </div>
      </div>
      <div class="issue">
        <p class="n">04 &mdash; Govern</p>
        <h3>Autonomy you can hand to an auditor.</h3>
        <div class="prose" style="margin-top:16px">
          <p>Every capability is versioned and sealed; every execution is attributable. Approval
          workflows, change windows, blast-radius limits and rollback are properties of the
          platform rather than conventions the team is trusted to follow. In an airgapped or
          regulated estate this is usually the first question, not the last.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("X", "Experience", "/platform/experience-score/", "The score that proves the expansion worked."),
      ("A", "Automate", "/platform/automate/", "What gets created, and how it runs."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/", "Why maintenance is the real cost."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/experience-score/ ─────────────────────────────────────────────
PAGES["/platform/experience-score/"] = {
 "title": "Experience — the patented DEX score — Nanoheal",
 "desc": "Digital experience improvement is usually asserted. Nanoheal measures it on a patented "
         "scoring methodology (US 9,477,573), so the outcome can be proven and contracted on.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Experience',
   "X &mdash; eXperience",
   "Improvement gets asserted. Yours will be scored.",
   "Every vendor in this category will tell you experience improved. Very few can hand the CFO a "
   "number that moved, on a methodology that was fixed before the work started.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">If the measure moves with the vendor, it isn&rsquo;t a measure.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>A score you can't audit.</h3>
      <p>Proprietary indices get re-weighted between releases. The number goes up, and nobody can
      say how much of that was the estate improving versus the definition changing. It becomes a
      dashboard artefact rather than evidence.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>A fixed, patented methodology.</h3>
      <p>The DEX Score methodology is patented under US 9,477,573. It is defined independently of
      any given release, so a ten-point gain in Q3 means the same thing it meant in Q1.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; What it measures</p>
        <h3>The experience the employee actually had.</h3>
        <p class="lead">Not device health in isolation. Performance, stability, application
        behaviour, availability and the friction a person met while trying to work &mdash; rolled
        into one score that survives being shown to a non-technical audience.</p>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; What it&rsquo;s worth</p>
        <h3>A ten-point gain, priced.</h3>
        <div class="stats" style="margin-top:24px">
          <div class="st hi"><div class="v">$8.6M</div><div class="l">productivity recovered per 10,000 employees per year, at a 10-point DEX gain</div></div>
          <div class="st hi"><div class="v">$1.0M</div><div class="l">service-desk cost avoided per 10,000 employees per year</div></div>
          <div class="st"><div class="v">22 min</div><div class="l">returned per employee per week, per industry research</div></div>
          <div class="st"><div class="v">35%</div><div class="l">overall ticket avoidance, in production at ~200K endpoints</div></div>
        </div>
        <p class="fine">Illustrative model. Cost avoided: 35% overall ticket avoidance on 1.0
        ticket/employee/month at $25 blended cost (HDI / MetricNet range). Productivity: industry
        research indicates a 10-point DEX Score gain returns approximately 22 minutes per employee
        per week, valued at $45/hour fully loaded. DEX Score methodology patented &mdash; US 9,477,573.</p>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What it closes</p>
        <h3>The loop, and the commercial conversation.</h3>
        <div class="prose" style="margin-top:16px">
          <p>The score is not a report at the end. It is the input to
          <a href="/platform/manage/" style="color:var(--teal)">Manage &amp; evolve</a> &mdash; the
          measurement that reveals which gap is worth closing next. That is what makes AIM-X a
          loop rather than a pipeline.</p>
          <p>It also changes what you can sign. A managed workplace service with a measured,
          patented experience score can be contracted on outcomes instead of headcount, which is
          the difference between selling effort and selling a result.</p>
          <p class="pull">If the improvement can't be scored, it can't be contracted. If it can,
          the whole commercial model changes.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("M", "Manage &amp; evolve", "/platform/manage/", "Where the score sends you next."),
      ("I", "Intelligence", "/platform/intelligence/", "What decides the action in between."),
      ("&rarr;", "For service providers", "/#solutions", "Contracting on an outcome."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /why-nanoheal/why-not-scripts/ ───────────────────────────────────────────
PAGES["/why-nanoheal/why-not-scripts/"] = {
 "title": "Why not scripts — Nanoheal",
 "desc": "The technical case for symptom-triggered automation over PowerShell-based remediation: "
         "detection cost, payload growth, estate drift and the maintenance curve.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Why Nanoheal &nbsp;/&nbsp; Why not scripts',
   "The technical case",
   "Scripts have to go looking for a problem. Nanoheal is told.",
   "This is the argument in full, for the person who will actually have to believe it: the "
   "endpoint engineer who has written these scripts and maintained them.") + """

<section class="band">
  <div class="wrap">
    <div class="prose">
      <p>Script-based remediation is not a bad idea. It was the only available idea. If the
      platform gives you a way to run arbitrary code on an endpoint, then every fix becomes a
      program, and everything that follows &mdash; the review cycle, the packaging, the version
      matrix, the breakage &mdash; follows from that one decision.</p>
      <p>The argument here is not that scripts don't work. It is that <strong>they carry three
      costs that don't show up in a demo</strong>, and all three scale with the thing you actually
      want, which is coverage.</p>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">Cost one</p>
        <h3>You pay to build detection the OS already performed.</h3>
        <div class="prose" style="margin-top:16px">
          <p>Consider a print spooler that has died. Windows knows. It writes Event 7031 to the
          system log at the moment it happens, without being asked, at no cost to anybody.</p>
          <p>A script cannot receive that. To act on it, something has to be watching &mdash; a
          scheduled task that wakes and re-reads the log, a resident process that subscribes and
          stays alive, a management agent that sweeps on an interval. Whichever you choose, you
          have rebuilt a detector for information that was already published, and you now run it
          on every machine in the fleet forever.</p>
          <p class="pull">The polling interval is a straight trade between how fast you detect and
          how much you burn. There is no setting that is good at both.</p>
          <p>Set it tight and you pay in CPU, memory and battery on the overwhelming majority of
          machines that are healthy. Set it loose and the employee has already opened a ticket
          before the automation notices. Nanoheal doesn't sit anywhere on that trade-off, because
          it consumes the signal the OS emits rather than going to look for it. Detection latency
          is milliseconds and the idle cost is nil.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">Cost two</p>
        <h3>Every fix adds permanent weight to every endpoint.</h3>
        <div class="prose" style="margin-top:16px">
          <p>One script is nothing. Two hundred scripts, each with its own detection logic,
          logging, error handling and scheduling, is an agent that has quietly become a
          significant workload &mdash; and it lands hardest on VDI, where the cost is multiplied
          by session density, and on laptops, where it shows up as battery life.</p>
          <p>This is the mechanism behind a pattern most IT leaders will recognise: automation
          coverage that plateaus not because the team ran out of ideas, but because nobody wants
          to push more weight onto the fleet.</p>
          <p>Nanoheal's execution capabilities are a fixed, signed set that ships once. Adding the
          two-hundredth automation adds a knowledge entry measured in kilobytes. The engine's
          footprint at 1,200 configurations is the engine's footprint at twelve.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">Cost three</p>
        <h3>Code assumes an estate that has already changed.</h3>
        <div class="prose" style="margin-top:16px">
          <p>A script encodes the environment as it was on the day it was written: this path, this
          key, this service name, this OS build. Every one of those is a dependency on something
          outside your control. A feature update relocates the path. A GPO change removes the
          permission. A vendor renames the service.</p>
          <p>The failure mode is the expensive part &mdash; scripts usually fail <em>silently</em>.
          The automation stops working, the tickets quietly return, and it surfaces weeks later in
          a ticket review as a mystery regression.</p>
          <p>Separating <strong>what</strong> from <strong>how</strong> is what avoids this. The
          knowledge entry says "repair the spooler's queue state." The engine owns how that is done
          on each platform and build, and is updated centrally as one component rather than as two
          hundred independent scripts.</p>
        </div>
      </div>
    </div>

    <div class="head" style="margin-top:64px">
      <p class="label">Side by side</p>
      <h2 class="h2">The same fix, both ways.</h2>
    </div>
    <div class="tblwrap">
      <table class="spec">
        <thead><tr><th>&nbsp;</th><th>Script-based</th><th>Nanoheal</th></tr></thead>
        <tbody>
          <tr><td>Detection</td><td class="bad">Rebuilt per fix; polls on an interval</td><td class="good">The OS event is the trigger</td></tr>
          <tr><td>Idle cost</td><td class="bad">CPU, memory and battery on every device, continuously</td><td class="good">None &mdash; nothing is watching</td></tr>
          <tr><td>Detection latency</td><td class="bad">Up to one polling interval</td><td class="good">Milliseconds</td></tr>
          <tr><td>What ships</td><td class="bad">Executable code, per fix</td><td class="good">Sealed knowledge, kilobytes</td></tr>
          <tr><td>Agent growth</td><td class="bad">Linear with automation count</td><td class="good">Flat</td></tr>
          <tr><td>Time to first fix</td><td class="bad">Weeks &mdash; specify, script, test, approve, publish</td><td class="good">Day one, from 1,200+ pre-built configurations</td></tr>
          <tr><td>On estate drift</td><td class="bad">Fails silently until someone notices</td><td class="good">Engine updated centrally; knowledge unaffected</td></tr>
          <tr><td>Security review</td><td class="bad">Per script, line by line, every revision</td><td class="good">Capability set reviewed once; entries carry no code</td></tr>
          <tr><td>Who can create one</td><td class="bad">An engineer who writes PowerShell</td><td class="good">Anyone in IT who can describe the task</td></tr>
          <tr><td>Cost of the next one</td><td class="bad">Roughly the same as the last</td><td class="good">Approaching zero</td></tr>
        </tbody>
      </table>
    </div>

    <div class="prose" style="margin-top:52px">
      <h3>The fair objection</h3>
      <p>A reasonable engineer will point out that a script can do <em>anything</em>, and a fixed
      capability set cannot. That is true, and it is the actual trade being made.</p>
      <p>The answer is that the capability set covers the operations endpoint remediation genuinely
      consists of &mdash; files, registry, services, processes, configuration, software, network,
      identity &mdash; and that the long tail of real tickets is overwhelmingly recombination of
      those primitives with different parameters, not novel computation. Where something truly
      exceptional is required, orchestration to an external system remains available. What you
      give up is the ability to write arbitrary code on the endpoint. What you get back is that
      nobody has to maintain arbitrary code on the endpoint.</p>
      <p class="pull">Coverage stalls in script-based estates for a reason that has nothing to do
      with ambition. Change the cost of the next automation and the ceiling moves.</p>
    </div>

    """ + nextcards([
      ("A", "Automate", "/platform/automate/", "The capability API, in detail."),
      ("I", "Intelligence", "/platform/intelligence/", "How the parameters get chosen."),
      ("&rarr;", "The AIM-X loop", "/platform/", "Where this sits in the whole framework."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/dex-intelligence/ ───────────────────────────────────────────────
PAGES["/platform/dex-intelligence/"] = {
 "title": "DEX Intelligence — measure, forecast, detect, act — Nanoheal",
 "desc": "Continuously measure devices, applications, networks and employee experience — then "
         "turn every anomaly, trend and emerging issue into an opportunity to automate.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; DEX Intelligence',
   "01 &mdash; DEX Intelligence",
   "DEX intelligence doesn&rsquo;t end in a dashboard.",
   "Continuously measure the digital workplace across devices, applications, networks and "
   "employee experience. Surface anomalies, trends and emerging issues, understand their impact, "
   "and turn every insight into an opportunity to improve and automate.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/platform/automate/">Then see what it triggers</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Observability that ends in an alert is a cost centre.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>The dashboard is the destination.</h3>
      <p>Sensors are configured, tuned, and eventually a dashboard goes live. It shows what is
      wrong across the fleet with real precision &mdash; and then the work of doing something
      about it starts, somewhere else, with someone else, in a different tool.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Detection is the first half of one motion.</h3>
      <p>The same platform that measured the degradation holds the knowledge to resolve it and the
      engine to execute. There is no handoff, because there is nowhere to hand off to.</p></div>
    </div>

    """ + shot("nanoheal &middot; experience score",
               "Screenshot &mdash; DEX trend — fleet",
               "<b>Fleet DEX as a number that moves.</b> Tracked continuously against a "
               "methodology fixed before the work started, so a change in the line is a "
               "change in the estate rather than a change in how it was counted.",
               "dex-score.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Measure</p>
        <h3>What the employee actually experienced.</h3>
        <p class="lead">Device performance and stability, application behaviour, network and
        connectivity quality, boot and logon times, crash and hang patterns, resource pressure,
        configuration drift &mdash; across Windows, macOS, Linux, VDI, mobile and IoT.</p>
        <div class="prose" style="margin-top:20px">
          <p>It resolves to a single <a href="/platform/experience-score/" style="color:var(--teal)">DEX
          Score</a> on a patented methodology, which matters for a reason most scores don't survive:
          it is defined independently of any release, so a ten-point gain means the same thing in
          Q3 that it meant in Q1.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Forecast</p>
        <h3>The failure that hasn&rsquo;t happened yet.</h3>
        <p class="lead">Degradation is rarely sudden. Disks fill on a curve, memory pressure builds
        over weeks, a driver starts failing on one build before it reaches the rest of the fleet,
        certificates and licences expire on a known date.</p>
        <div class="prose" style="margin-top:20px">
          <p>Forecasting turns those curves into a dated, ranked list of what will break and
          roughly when. On its own that is a better alert. Wired to an engine that can already fix
          it, it becomes something else entirely: the remediation runs before the employee has a
          bad day, and the ticket that would have been raised never exists.</p>
          <p class="pull">Prediction without execution just tells you what is coming. The value is in the estate where nobody had to be told.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Detect anomalies</p>
        <h3>The problems nobody wrote a rule for.</h3>
        <p class="lead">Threshold alerting only catches what someone anticipated. Anomaly detection
        catches the rest &mdash; the behaviour that is abnormal for this fleet, this device class,
        this population, this time of week.</p>
        <div class="prose" style="margin-top:20px">
          <p>This matters most in the two situations that generate the worst incidents: a change
          that behaves differently in production than it did in test, and a slow regression that
          never crosses a threshold but degrades thousands of people at once. Neither has a rule
          written for it, because neither was foreseen.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; Trace to root cause</p>
        <h3>The cause, not the symptom that reached the desk.</h3>
        <p class="lead">A slow laptop is a report, not a diagnosis. Correlating device, application,
        network, configuration and change history isolates what actually caused it.</p>
        <div class="prose" style="margin-top:20px">
          <p>The root cause is also what makes automation reusable. A fix bound to a symptom helps
          one person; a fix bound to a cause becomes knowledge that resolves the same condition
          everywhere it exists, including on the machines where nobody has complained yet.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">05 &mdash; Coverage</p>
        <h3>The whole digital workplace, not just the endpoint.</h3>
        <p class="lead">Four domains, measured against the same score, so a regression in one is
        comparable to a regression in another.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Device experience.</h3><p>Boot and logon, CPU, memory and disk
          pressure, battery, crashes and hangs, driver and firmware health, configuration drift
          &mdash; Windows, macOS, Linux, VDI, mobile and IoT.</p></div>
          <div class="tile"><h3>Application experience.</h3><p>Launch and response times, crash
          and hang rates, version spread, licence usage and reclaim candidates, adoption of the
          apps you have paid for.</p></div>
          <div class="tile"><h3>Network &amp; collaboration.</h3><p>Connectivity quality, Wi-Fi and
          VPN behaviour, latency to the services that matter, and meeting and call quality as the
          employee actually experienced it.</p></div>
        </div>
        <div class="g3" style="margin-top:14px">
          <div class="tile"><h3>Employee experience.</h3><p>Sentiment collected in context rather
          than in an annual survey, tied to the device and application evidence from the same
          moment.</p></div>
          <div class="tile"><h3>Change and campaign impact.</h3><p>What a rollout did to the
          score, per population, so a migration can be stopped at 5% instead of explained at
          100%.</p></div>
          <div class="tile"><h3>Persona and population.</h3><p>Segment by role, site, device
          class or business unit &mdash; the unit an automation is later targeted at.</p></div>
        </div>
        """ + shot("nanoheal &middot; inventory",
               "Screenshot &mdash; managed estate",
               "<b>One estate, several operating systems.</b> Windows, macOS and Linux "
               "endpoints sit in the same inventory with the same health, agent and "
               "last-seen columns &mdash; so a population is defined by who uses it, not "
               "by which console can see it.",
               "inventory.png") + """
      </div>

      <div class="issue">
        <p class="n">06 &mdash; What ships as standard</p>
        <h3>Twenty-four reports, live on day one.</h3>
        <p class="lead">Not a canvas and a query builder. A catalogue of finished analytics that
        answers the questions an IT organisation already has &mdash; grouped the way the
        conversation actually splits, from the leadership summary down to the endpoint.</p>
        <div class="tblwrap" style="margin-top:22px">
          <table class="spec">
            <thead><tr><th>Category</th><th>Reports</th></tr></thead>
            <tbody>
              <tr><td>Digital experience</td><td>DEX Score Overview &middot; What Changed &mdash; Device &amp; DEX Drivers &middot; IT Leadership &mdash; Experience Summary &middot; Device Friction &rarr; Productivity Loss</td></tr>
              <tr><td>Device fleet &amp; endpoints</td><td>Endpoint Experience Scorecard &middot; Boot &amp; Logon Performance &middot; Device Lifecycle &amp; Refresh Readiness &middot; CPU, Memory &amp; Right-Sizing</td></tr>
              <tr><td>Applications on endpoints</td><td>Business Application Health &middot; App Crashes &amp; Instability &middot; Software Inventory &amp; License Use &middot; Teams, Outlook &amp; Meeting Apps</td></tr>
              <tr><td>Network &amp; remote access</td><td>Network, Wi-Fi &amp; VPN Quality &middot; Device Degradation &amp; Anomalies</td></tr>
              <tr><td>Workforce experience</td><td>Employee Device Satisfaction &middot; Top Employee Complaints (IT)</td></tr>
              <tr><td>Benchmarks &amp; fleet planning</td><td>DEX vs Industry Benchmark &middot; DEX by Site, Persona &amp; Working Style &middot; Predictive Device Risk</td></tr>
              <tr><td>IT service &amp; remediation</td><td>Endpoint Auto-Remediation &middot; Device-Related Ticket Volume &middot; Endpoint Incident MTTR &middot; Device Ops &mdash; Cost &amp; ROI &middot; Endpoint Compliance &amp; Posture</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>Two of those categories are worth pausing on, because they are the ones a pure
          observability product cannot fill. <em>IT service &amp; remediation</em> reports on
          auto-remediation volume, ticket deflection, MTTR and cost &mdash; numbers that only
          exist if the platform is also the thing doing the fixing. <em>Benchmarks &amp; fleet
          planning</em> puts your score next to an industry baseline and a predicted risk curve,
          which is what turns a measurement into a plan.</p>
          <p class="pull">Analytics parity is the price of entry, not the argument. It is on this page so that scope is never the reason a conversation ends.</p>
        </div>
        """ + shot("nanoheal &middot; dashboards",
               "Screenshot &mdash; report catalog",
               "<b>The catalogue, not a blank canvas.</b> Every report is categorised, "
               "searchable and one click from a view &mdash; and it sits in the same "
               "navigation as the automation library, the policy catalogue and the "
               "execution record.",
               "console-experience.png") + """
      </div>

      <div class="issue">
        <p class="n">07 &mdash; The handoff that isn&rsquo;t one</p>
        <h3>Every insight is an automation opportunity.</h3>
        <p class="lead">This is the part that separates intelligence from reporting. A finding
        here does not become a JIRA ticket for the automation team &mdash; it becomes a candidate
        the platform can already act on.</p>
        <div class="prose" style="margin-top:20px">
          <p>When a condition is detected on a population, Nanoheal already knows which
          capabilities would correct it, how many employees are affected, and what the score would
          be worth if it were fixed. If knowledge for that condition exists in the library, it can
          be targeted immediately. If it doesn't, the
          <a href="/platform/intelligence/" style="color:var(--teal)">context layer authors the
          entry</a> and a human validates it once.</p>
          <p class="pull">The measurement doesn't hand you a finding. It hands you a fix, priced by how many people it helps.</p>
        </div>
        """ + shot("nanoheal &middot; experience drivers",
                   "Screenshot &mdash; Score drivers by location and cause",
                   "<b>Which populations, and which cause.</b> The score is decomposed by site "
                   "and by driver — connectivity leads here at 32% — so the next automation is "
                   "chosen by what it would return, not by what is easiest to build.",
                   "dex-drivers.png") + """
      </div>
    </div>

    """ + nextcards([
      ("I", "Intelligence", "/platform/intelligence/", "What turns a finding into an action."),
      ("A", "Automate", "/platform/automate/", "The engine that executes it."),
      ("X", "Experience", "/platform/experience-score/", "The score all of it moves."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/compliance-governance/ ─────────────────────────────────────────────────
PAGES["/platform/compliance-governance/"] = {
 "title": "Compliance & Governance — IT management automated — Nanoheal",
 "desc": "Software, patches, security updates and policy automated by persona, with drift "
         "continuously detected and restored — on the same engine that heals the device.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Compliance &amp; Governance',
   "03 &mdash; Compliance &amp; Governance",
   "IT management automated. Compliance continuously enforced.",
   "The context layer gives intelligence the knowledge to extend its capabilities without code "
   "&mdash; automating software, patches, security updates and policies by persona, while "
   "continuously detecting and restoring drift to keep the fleet compliant.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/solutions/compliance-audit/">The audit-readiness case</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Nobody set out to run four agents. It just happened.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>A tool per job.</h3>
      <p>One platform measures experience. Another distributes software. A third handles patch. A
      fourth enforces policy. Each ships an agent, each keeps its own inventory, each has its own
      idea of what a device is &mdash; and reconciling them is somebody's full-time job.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>One engine, many kinds of work.</h3>
      <p>Installing software, applying a patch, enforcing a policy and repairing a broken service
      are the same underlying operations against files, registry, services and configuration. One
      capability set covers all of it.</p></div>
    </div>

    """ + shot("nanoheal &middot; policy templates",
               "Screenshot &mdash; ADMX policy catalog",
               "<b>Desired state, from the catalog you already know.</b> 4,080 ADMX policy "
               "templates are first-class objects: pick the template, scope it to a device "
               "classification, and the engine holds the estate there. No settings "
               "hand-authored one at a time.",
               "gpo-admx.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Software distribution</p>
        <h3>Deploy, repair, roll back, reclaim.</h3>
        <p class="lead">Install and update across the fleet or a targeted population, with repair
        for failed installs and rollback when a version misbehaves. Usage data from the analytics
        side identifies licences nobody is using.</p>
        <div class="prose" style="margin-top:18px">
          <p>Because distribution shares the engine with remediation, a failed install isn't a
          report you chase &mdash; it is a symptom, and it can trigger its own repair.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Patch management</p>
        <h3>Compliance you can evidence, on the estate you actually have.</h3>
        <p class="lead">Assess, stage, deploy and verify across operating systems and third-party
        applications, with rings, windows and rollback. Verification is measured on the device, not
        inferred from a deployment record.</p>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Device compliance policy</p>
        <h3>Policy that corrects drift instead of reporting it.</h3>
        <p class="lead">Define the desired state &mdash; settings, profiles, security configuration,
        encryption, required software &mdash; in the same plain-language knowledge layer as
        everything else.</p>
        <div class="prose" style="margin-top:18px">
          <p>If you run Intune or a comparable MDM, the familiar gap is between what policy says
          and what the device does: a profile fails to apply, drift accumulates, and the console
          reports non-compliance without resolving it. Nanoheal treats non-compliance as a symptom
          like any other &mdash; the drift itself triggers the correction, on the same engine, with
          no script involved.</p>
          <p class="pull">Reporting a device out of policy is a finding. Putting it back in policy
          is the job.</p>
        </div>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Policy templates.</h3><p>4,080 ADMX templates, browsable by
          category and subcategory. The Windows policy vocabulary your team already knows,
          available as objects to scope rather than settings to re-author.</p></div>
          <div class="tile"><h3>Protection profiles.</h3><p>Lockdown baselines expressed as
          policies over registry, services, application control, filesystem paths and removable
          media &mdash; Defender real-time protection, BitLocker on the OS volume, machine
          inactivity limits.</p></div>
          <div class="tile"><h3>Collection profiles.</h3><p>What the agent gathers in the first
          place: performance, storage, user activity and network. The measuring half is itself a
          scoped, published configuration &mdash; not a fixed sensor set you inherit.</p></div>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>All three are the same kind of object as an automation, and they travel the same
          route: attach to a device classification, stage the change, publish it. One change-control
          path covers remediation, software, telemetry and hardening, which is the reason a
          compliance conversation here does not need a second tool to finish.</p>
        </div>
        """ + shot("nanoheal &middot; data collection",
               "Screenshot &mdash; collection profiles",
               "<b>What you measure is a published configuration too.</b> Performance, storage, "
               "network and user-activity collection are profiles you attach to a group and "
               "release &mdash; so a persona can be measured differently from a kiosk without "
               "a separate deployment.",
               "data-collection.png") + """
      </div>

      <div class="issue">
        <p class="n">04 &mdash; IT tasks and requests</p>
        <h3>The routine work that still lands on a human.</h3>
        <p class="lead">Profile resets, printer and peripheral setup, drive mapping, certificate
        renewal, disk cleanup, onboarding and offboarding sequences, VPN and Wi-Fi reconfiguration.</p>
        <div class="prose" style="margin-top:18px">
          <p>These are what a large share of service-desk contacts actually consist of, and they
          are the clearest case for the economics argument: individually small, collectively
          enormous, and never worth a bespoke automation project. When the next automation costs
          almost nothing, they finally get built.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">05 &mdash; Governance</p>
        <h3>Autonomy you can hand to an auditor.</h3>
        <p class="lead">Automation that runs unattended has to be governable, or it does not get
        approved. Every capability is signed and versioned, every action is scoped by policy, and
        every execution is recorded.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Validated once.</h3><p>A human approves the knowledge entry before
          it is ever trusted, and the approval is versioned with it. Nothing self-authors its way
          into production.</p></div>
          <div class="tile"><h3>Scoped by policy.</h3><p>Which populations, which maintenance
          windows, which blast radius, which actions require a human in the loop &mdash; checked
          before anything runs, not asserted afterwards.</p></div>
          <div class="tile"><h3>Evidenced.</h3><p>What ran, where, when, under which version and
          with what result &mdash; exportable as the evidence pack an audit asks for, not
          reconstructed from logs.</p></div>
        </div>
        """ + shot("nanoheal &middot; activity log",
                   "Screenshot &mdash; Activity log",
                   "<b>Who changed what, on the record.</b> Every config edit, publish and "
                   "link is logged with the module it touched, the account that made it and "
                   "the outcome — the console&rsquo;s own change history, kept separate from "
                   "the device telemetry stream.",
                   "audit-log.png") + """
      </div>
    </div>

    """ + nextcards([
      ("&rarr;", "Orchestration", "/platform/orchestration/", "Acting in systems beyond the device."),
      ("A", "Automate", "/platform/automate/", "The capability engine underneath all of this."),
      ("&rarr;", "Workflows", "/platform/workflows/", "Describing a task in plain language."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/orchestration/ ─────────────────────────────────────────────────
PAGES["/platform/orchestration/"] = {
 "title": "Orchestration — any IT system, integrated without code — Nanoheal",
 "desc": "The context layer spans the IT ecosystem. ServiceNow, Active Directory and any system "
         "with a standard API are integrated without writing code.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Orchestrate the IT Ecosystem',
   "04 &mdash; Orchestrate the IT Ecosystem",
   "Most fixes don&rsquo;t end on the device.",
   "A stale credential is resolved in the directory. A resolved incident has to be closed in "
   "ITSM. A licence is reclaimed in a SaaS console. Automation confined to the endpoint stops "
   "halfway through most of the work.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Integration is where automation projects quietly die.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Every connector is a project.</h3>
      <p>Connecting to ServiceNow means an integration build. Active Directory means another.
      Each has its own authentication, its own error handling, its own field mapping, and its own
      maintenance burden when either side changes. Integration backlog becomes the reason
      automation stalls &mdash; not the automation itself.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Describe the system, not the code.</h3>
      <p>Any system exposing a standard API interface is integrated by describing what it offers.
      The context layer handles authentication, calls, mapping and error handling. No connector is
      written, so no connector is maintained.</p></div>
    </div>

    """ + shot("nanoheal &middot; connectors",
               "Screenshot &mdash; Ecosystem connectors",
               "<b>The ecosystem, described rather than coded.</b> ServiceNow for incident "
               "and CMDB sync, Teams and Slack for escalation, BMC Helix for asset "
               "reconciliation, Autotask for PSA tickets — each scoped to a site, each a "
               "statement of intent rather than an integration project.",
               "connectors.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; What it connects</p>
        <h3>The systems the work actually lives in.</h3>
        <div class="tblwrap">
          <table class="spec">
            <thead><tr><th>System class</th><th>Examples</th><th>What Nanoheal does there</th></tr></thead>
            <tbody>
              <tr><td>ITSM</td><td>ServiceNow and comparable platforms</td><td>Reads incident, problem and change history for context; creates, updates and closes tickets as work completes</td></tr>
              <tr><td>Directory &amp; identity</td><td>Active Directory, Entra ID, identity providers</td><td>Group membership, account state, credential and session actions, access requests</td></tr>
              <tr><td>IT management</td><td>MDM, endpoint management, patch and software platforms</td><td>Reads and reconciles state; acts where the platform is authoritative</td></tr>
              <tr><td>CMDB &amp; asset</td><td>Configuration and asset systems</td><td>Resolves ownership, role, entitlement and compliance obligation before acting</td></tr>
              <tr><td>Workplace &amp; collaboration</td><td>Collaboration, network, cloud and SaaS platforms</td><td>Configuration, licence reclaim, connectivity and access remediation</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; How it connects</p>
        <h3>No code, and therefore no connector backlog.</h3>
        <div class="prose" style="margin-top:16px">
          <p>The mechanism is the same one that removes scripting from remediation. The context
          layer holds a description of what a system exposes &mdash; its operations, its objects,
          its fields. Intelligence selects the operation and supplies the parameters. Nothing is
          generated and nothing is compiled into a custom connector.</p>
          <p>This is why adding a system is measured in the time it takes to describe and approve
          it, rather than in engineering sprints, and why the integration doesn't break the next
          time either side ships a release.</p>
          <p class="pull">The reason integration is normally slow is that somebody has to write
          the integration. Remove that and the schedule changes shape.</p>
        </div>
        <div class="tblwrap" style="margin-top:24px">
          <table class="spec">
            <thead><tr><th>Surface</th><th>Direction</th><th>What it is for</th></tr></thead>
            <tbody>
              <tr><td>Connectors</td><td>Nanoheal &rarr; a product</td><td>Named, per-site links to the systems the work lives in &mdash; ITSM, CMDB, PSA, collaboration</td></tr>
              <tr><td>Event subscriptions</td><td>Nanoheal &rarr; any URL</td><td>Pushing device and remediation events into whatever you already run, without a connector for it</td></tr>
              <tr><td>API keys &amp; catalog</td><td>A product &rarr; Nanoheal</td><td>Scoped programmatic access for the systems that need to read or drive the estate</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>Connectors are scoped to a site rather than to the tenant, which matters more than it
          sounds: a regional CMDB, a business unit&rsquo;s own ServiceNow instance and a partner&rsquo;s
          PSA can coexist under one console without anybody having to pick a winner.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What it makes possible</p>
        <h3>One resolution, across four systems, unattended.</h3>
        <p class="lead">A worked example, in the order it happens:</p>
        <div class="tblwrap">
          <table class="spec">
            <thead><tr><th>Step</th><th>Where</th><th>What happens</th></tr></thead>
            <tbody>
              <tr><td>Symptom</td><td>Endpoint</td><td>Repeated authentication failures surface in the OS event log</td></tr>
              <tr><td>Context</td><td>Directory + CMDB</td><td>Account state and group membership read; device owner, role and compliance obligation resolved</td></tr>
              <tr><td>History</td><td>ITSM</td><td>Two similar incidents in the last quarter; the known resolution is retrieved</td></tr>
              <tr><td>Action</td><td>Device + directory</td><td>Cached credential cleared and profile repaired on the device; the stale directory object corrected</td></tr>
              <tr><td>Close</td><td>ITSM</td><td>Ticket created and closed with what was done, so the record exists without a human writing it</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>Every one of those steps is available to a scripted approach. What isn't available is
          doing it without five integrations, a scheduler and somebody maintaining all of it.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; What governs it</p>
        <h3>Guardrails travel with the action.</h3>
        <div class="prose" style="margin-top:16px">
          <p>Acting in ITSM or a directory is higher-consequence than acting on one endpoint, and
          it is governed accordingly: scoped credentials per system, explicit allow-lists of
          permitted operations, approval gates, change windows, blast-radius limits and full
          attribution of what ran, where, and on whose authority.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("I", "Intelligence", "/platform/intelligence/", "The context layer this runs on."),
      ("&rarr;", "Workflows", "/platform/workflows/", "Building it in plain language."),
      ("&rarr;", "IT operations", "/platform/compliance-governance/", "The device-side half."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/workflows/ ─────────────────────────────────────────────────────
PAGES["/platform/workflows/"] = {
 "title": "Workflows & natural language — describe it, don't build it — Nanoheal",
 "desc": "Describe a task in plain language and the context layer compiles the workflow. Trigger "
         "it from a symptom, a schedule, a conversation or an IT agent request.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Workflows &amp; natural language',
   "Workflows &amp; natural language",
   "Describe the task. Don&rsquo;t build it.",
   "The people who know what needs automating are rarely the people who can build it. That gap "
   "is the reason automation backlogs exist, and closing it is worth more than any individual "
   "workflow in the queue.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">The backlog isn&rsquo;t a list of ideas. It&rsquo;s a list of things waiting for an engineer.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>A request, then a queue.</h3>
      <p>A service-desk lead knows exactly which repetitive task should be automated. They raise
      a request. It joins a backlog behind work with a bigger business case, and by the time it is
      picked up the details have changed. Most of what should be automated is never refused
      &mdash; it is just never reached.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>The person who knows, writes it.</h3>
      <p>They describe the task in plain English. The context layer resolves it against the
      engine's capabilities and compiles a workflow. IT validates it once. No engineering ticket
      is ever raised.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Authoring</p>
        <h3>Plain language in. Sealed capability out.</h3>
        <div class="prose" style="margin-top:16px">
          <p>Intelligence reads the description, resolves it against what the engine can do and
          what the context layer knows about your estate, and produces a workflow with its
          parameters, conditions and failure handling made explicit for review.</p>
          <p>Worth being precise about what does <em>not</em> happen: no code is generated. The
          output is knowledge against a fixed, signed capability set. That is what makes it
          reviewable by someone who doesn't write PowerShell, and what means it doesn't rot when
          the estate moves underneath it.</p>
          <p class="pull">If the output were generated code, you would have moved the engineering
          problem rather than removed it &mdash; and inherited code nobody wrote but somebody
          still maintains.</p>
        </div>
        """ + shot("nanoheal &middot; workflow builder",
               "Screenshot &mdash; plain-language authoring",
               "<b>Described, not built.</b> One field, in plain English. The context layer "
               "resolves the description against what the engine can already do and returns "
               "a workflow to review &mdash; and the quick starts underneath are capabilities, "
               "not code samples.",
               "workflow-nl.png") + """
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Triggering</p>
        <h3>Four ways the same workflow starts.</h3>
        <p class="lead">In the console this is a single choice on the workflow&rsquo;s
        <em>Details</em> step &mdash; three intents that cover four operational patterns, because
        a symptom and a forecast arrive through the same door.</p>
        <div class="tblwrap" style="margin-top:22px">
          <table class="spec">
            <thead><tr><th>Trigger</th><th>Starts when</th><th>Set in the builder as</th><th>Typical use</th></tr></thead>
            <tbody>
              <tr><td>Symptom</td><td>The OS reports the condition &mdash; event, service state, crash, error</td><td>Event trigger</td><td>Autoheal, before anyone notices</td></tr>
              <tr><td>Forecast</td><td>Prediction or anomaly detection flags a condition building</td><td>Event trigger</td><td>Prevention &mdash; the ticket never exists</td></tr>
              <tr><td>Request</td><td>An employee, a service-desk agent or an IT agent asks</td><td>On demand</td><td>Self Help and Remote Execution</td></tr>
              <tr><td>Schedule or policy</td><td>A window, a compliance obligation, a drift threshold</td><td>Schedule</td><td>Patch rings, policy enforcement, routine tasks</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>An event trigger is bound to a named condition the operating system already
          publishes &mdash; a Windows event, a service state, a disk or memory threshold &mdash;
          with a comparison and a value. Nothing is deployed to the endpoint to watch for it,
          because the endpoint is already reporting it.</p>
          <p>One authored workflow serves all four rows. This is the part that compounds: the
          effort is spent once and recovered every time the condition recurs, through whichever
          channel it arrives.</p>
        </div>
        """ + shot("nanoheal &middot; workflow builder",
               "Screenshot &mdash; intent",
               "<b>Three intents, four patterns.</b> On demand is the one worth reading twice: "
               "the same automation reaches employees through Self Help and technicians through "
               "Remote Execution, without being rebuilt for either.",
               "workflow-trigger.png") + """
      </div>

      <div class="issue">
        <p class="n">03 &mdash; The conversational interface</p>
        <h3>Ask the estate a question. Then ask it to act.</h3>
        <p class="lead">The context layer already holds DEX signals, ITSM history, CMDB and your
        SOPs. Natural language is simply the most direct way to interrogate that.</p>
        <div class="prose" style="margin-top:18px">
          <p>"Which devices are showing the memory pattern that preceded last month's crashes?"
          is a question. "Fix them" is the next sentence, and it runs through exactly the same
          guardrails, approvals and attribution as any other execution path &mdash; conversational
          input does not mean relaxed governance.</p>
          <p>For the service desk this replaces the runbook. The agent describes the outcome
          rather than following twelve steps, and the same validated capability runs that would
          have run unattended.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; Validation</p>
        <h3>Once, by a human, before it is trusted.</h3>
        <div class="prose" style="margin-top:16px">
          <p>Nothing authored this way executes on its own authority. A workflow is reviewed and
          approved once; it is then compiled, sealed and versioned, and every subsequent execution
          is attributable to that approved version. Plain-language authoring changes who can
          propose an automation. It does not change who signs it off.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("&rarr;", "Orchestration", "/platform/orchestration/", "Where these workflows can act."),
      ("I", "Intelligence", "/platform/intelligence/", "What compiles the description."),
      ("M", "Manage &amp; evolve", "/platform/manage/", "Deciding what to author next."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /platform/automation-library/ ────────────────────────────────────────────
PAGES["/platform/automation-library/"] = {
 "title": "Automation library — 1,200+ configurations on day one — Nanoheal",
 "desc": "Most automation platforms start empty. Nanoheal ships 1,200+ pre-built remediations, "
         "IT tasks and compliance configurations, and your own team extends them in plain "
         "language.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Automation library',
   "The library",
   "Most platforms start empty. Nanoheal starts with 1,200+.",
   "Pre-built remediations, IT tasks and compliance configurations ship on day one, matched "
   "against your existing top call drivers &mdash; not an empty canvas with a tutorial.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/platform/workflows/">How your team adds to it</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">An empty platform is a project, not a product.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Day one is a blank canvas.</h3>
      <p>The platform arrives with a framework and a best-practice guide. Everything that will
      ever run on it has to be identified, authored, tested and approved by your team &mdash; so
      the first measurable outcome is a quarter away, and the business case is a promise.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Day one is coverage.</h3>
      <p>1,200+ validated configurations are already there. We map them against your top call
      drivers before you sign anything, so the conversation is about which ones you switch on
      first, not about how long the build takes.</p></div>
    </div>

    """ + shot("nanoheal &middot; automation library",
               "Screenshot &mdash; Linked automations",
               "<b>Browse, target, run.</b> Linked automations grouped by category, each "
               "showing its delivery mode, its state and the population it is scoped to — "
               "and a <em>Run now</em> that puts the same validated knowledge in a "
               "technician&rsquo;s hands on demand.",
               "remote-exec.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; What&rsquo;s in it</p>
        <h3>Three classes of work, one library.</h3>
        <p class="lead">The library is not a remediation catalogue with IT tasks bolted on. All
        three classes are the same kind of object, because the engine underneath does not
        distinguish between them.</p>
        <div class="tblwrap">
          <table class="spec">
            <thead><tr><th>Class</th><th>Examples</th><th>Trigger</th></tr></thead>
            <tbody>
              <tr><td>Resolve</td><td>Service failures, application crashes and hangs, profile corruption, print and peripheral faults, connectivity and VPN repair, disk pressure, certificate problems</td><td>The symptom the OS reports, or a forecast before it arrives</td></tr>
              <tr><td>Run</td><td>Software install, repair and rollback, patch rings and verification, drive and printer mapping, onboarding and offboarding sequences, licence reclaim</td><td>Request, schedule or campaign</td></tr>
              <tr><td>Enforce</td><td>Security configuration, encryption state, required software, profile and policy baselines, persona-specific standards</td><td>Drift, treated as a symptom of its own</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:24px">
          <p>In the console every entry carries the same four facets, whichever class it belongs
          to: the <strong>category</strong> it sits under &mdash; apps, collaboration, devices,
          network &mdash; the <strong>delivery mode</strong> it is licensed for, the
          <strong>state</strong> it is in, and the <strong>population</strong> it is scoped to.
          &ldquo;Chrome Cleanup &middot; autoheal &middot; active &middot; scoped for Clinical&rdquo;
          is the whole record: what it fixes, how it reaches the device, whether it is live, and
          who gets it.</p>
          <p>That uniformity is what makes the library browsable at 1,200 entries rather than
          merely large. You are not reading scripts to work out what something does; you are
          filtering objects that describe themselves.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Why the number matters</p>
        <h3>Sensors measure. Configurations act.</h3>
        <p class="lead">The closest published figure in the category is roughly 220 automations
        alongside 1,300 sensors. That ratio is the category's shape in one line: enormous
        investment in seeing, modest investment in doing.</p>
        <div class="prose" style="margin-top:20px">
          <p>The gap is not an oversight. Sensors are cheap to add because they are declarative;
          automations are expensive because each one is authored code that has to be maintained
          forever. Nanoheal's library is large for the same structural reason the competition's is
          small: here, an automation is also declarative.</p>
          <p class="pull">Ask any vendor how many automations ship on day one, and how many of
          them you will have to maintain.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; How it grows</p>
        <h3>Your estate&rsquo;s long tail, not just the common cases.</h3>
        <p class="lead">The 1,200+ cover what every estate has. What no library can ship is the
        line-of-business application your industry runs, the bespoke VPN profile, the internal
        tool that half the company depends on.</p>
        <div class="prose" style="margin-top:20px">
          <p>Those get added the same way the built-in entries were: someone describes the symptom
          and the fix in plain language, the
          <a href="/platform/intelligence/" style="color:var(--teal)">context layer authors the
          entry</a>, a human validates it once, and it joins the library for the whole estate.
          Because there is no code, the cost of the two-hundredth addition is roughly the cost of
          the second.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; Multi-tenant</p>
        <h3>Built once, available across every tenant you run.</h3>
        <p class="lead">For service providers and support channels, the library is the asset. A
        configuration validated for one client can be published across the book of business
        without rebuilding it per tenant, with tenant-level scoping and guardrails intact.</p>
      </div>
    </div>

    """ + nextcards([
      ("A", "Automate Issues", "/platform/automate/", "What an entry is, and how it runs."),
      ("NL", "Workflows", "/platform/workflows/", "Adding your own in plain language."),
      ("M", "Continuous improvement", "/platform/manage/", "What to add next, and why."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/ ──────────────────────────────────────────────────────────────
PAGES["/solutions/"] = {
 "title": "Solutions — one platform, different value depending who runs it — Nanoheal",
 "desc": "Ticket deflection, self-service, IT task automation and compliance — for internal IT "
         "teams, service providers and support channels.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Solutions',
   "Who it&rsquo;s for",
   "One platform. Different value, depending who&rsquo;s running it.",
   "Whether IT sits inside your company or you deliver it as a service, it is the same autonomous "
   "platform &mdash; the same engine, the same library, the same guardrails. What changes is what "
   "you are trying to get out of it.") + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">By outcome</p>
      <h2 class="h2">Start from the number you have been asked to move.</h2>
      <p class="lede">Each of these is the same mechanism pointed at a different problem. They are
      not modules, and none of them is priced separately.</p>
    </div>
    """ + cards([
      ("01", "Ticket deflection &amp; autoheal", "/solutions/ticket-deflection/",
       "Resolve the top call drivers at the moment the OS reports them, before the employee "
       "notices there was anything to call about.",
       "Fewer tickets, without a smaller team"),
      ("02", "Employee self-service", "/solutions/self-service/",
       "Offer the validated fix at the moment of failure and let the employee apply it &mdash; "
       "deflection without the service desk touching it.",
       "The fix, offered in context"),
      ("03", "IT task automation", "/solutions/it-task-automation/",
       "Software, patch, onboarding, peripherals, profile work &mdash; the routine operation of "
       "an estate, on the engine that already heals it.",
       "The work that never justified a project"),
      ("04", "Compliance &amp; audit readiness", "/solutions/compliance-audit/",
       "Policy that corrects drift instead of reporting it, and an evidence pack you can hand to "
       "an auditor without reconstructing it from logs.",
       "Enforced, not asserted"),
    ]) + """
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">By who you are</p>
      <h2 class="h2">Same engine, whether you run 500 endpoints or 200,000.</h2>
      <p class="lede">Multi-tenant from the ground up, so the commercial shape of your IT
      organisation is a configuration question rather than a different product.</p>
    </div>
    """ + cards([
      ("IT", "Internal IT", "/solutions/internal-it/",
       "Fortune 1000 estates across manufacturing, technology services and SaaS &mdash; typically "
       "replacing a DEX tool that measures well and acts poorly.",
       "Do more with the team you have"),
      ("MSP", "Service providers &amp; GSIs", "/solutions/service-providers/",
       "Delivered inside an existing managed workplace service. Your contract, your client, your "
       "delivery model &mdash; with an autonomy layer your competitors cannot price.",
       "Differentiate the service you already run"),
      ("OEM", "OEMs, channel &amp; SMB", "/solutions/oem-channel/",
       "Multi-tenant from the ground up, so the same automation library serves a support "
       "channel's whole book of business.",
       "One library, every tenant"),
    ], three=True) + """
  </div>
</section>
""" + CTA}


# ── /solutions/ticket-deflection/ ────────────────────────────────────────────
PAGES["/solutions/ticket-deflection/"] = {
 "title": "Ticket deflection & autoheal — Nanoheal",
 "desc": "Deflection that comes from resolving issues, not from making it harder to raise a "
         "ticket. Triggered by the symptom the OS reports, with no script and nothing polling.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; Ticket deflection',
   "By outcome",
   "Deflection should mean resolved, not discouraged.",
   "Most deflection programmes work by putting something between the employee and the service "
   "desk &mdash; a portal, a bot, a form. Autoheal works by removing the reason for the contact "
   "before the employee has one.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Bring us your top three call drivers</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Every deflection number is really two different numbers.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Contacts moved, not removed.</h3>
      <p>A chatbot answers, a portal article is read, a form is submitted. The contact is recorded
      somewhere cheaper, which is worth something &mdash; but the employee still lost the time,
      and the underlying fault is still on the device tomorrow.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>The fault is gone before the call.</h3>
      <p>The OS reports the symptom, knowledge matches it, capabilities correct it. There is no
      contact to route because there is nothing left to report &mdash; and the same knowledge now
      covers every other machine in the estate with the same condition.</p></div>
    </div>

    """ + metrics([
      ("In production", "17%", "of tickets autohealed at a Fortune 100 manufacturer running "
       "~200,000 endpoints"),
      ("In production", "35%", "overall ticket avoidance across autoheal, self-service and "
       "assisted resolution"),
      ("Day one", "1,200+", "pre-built configurations mapped against your existing call drivers "
       "before you build anything"),
      ("Per endpoint", "0", "background probes &mdash; detection is the signal the OS already "
       "emits"),
    ]) + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Where the volume actually is</p>
        <h3>The top ten drivers, then a very long tail.</h3>
        <p class="lead">Most estates can name their top ten call drivers, and most automation
        programmes cover them. Then coverage stops, because the eleventh costs as much to automate
        as the first and returns a tenth as much.</p>
        <div class="prose" style="margin-top:20px">
          <p>That is the arithmetic that caps deflection in the thirty-percent range everywhere
          else. When an automation is knowledge rather than code, the eleventh costs almost
          nothing &mdash; and so does the hundredth. The tail is where the remaining deflection
          lives, and it only gets built if the unit cost collapses first.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Three ways the same fix lands</p>
        <h3>One validated entry, three delivery modes.</h3>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Autoheal.</h3><p>Resolved before anyone notices. No ticket, no
          contact, no interruption &mdash; and no employee had to describe a technical problem in
          their own words.</p></div>
          <div class="tile"><h3>Self-service.</h3><p>The employee is offered the fix at the moment
          of failure and applies it themselves.
          <a href="/solutions/self-service/" style="color:var(--teal)">More &rarr;</a></p></div>
          <div class="tile"><h3>Assisted.</h3><p>The agent executes the same capability in a single
          action &mdash; no runbook to follow, no elevation risk, no variation between agents.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What it does to the desk</p>
        <h3>The team doesn&rsquo;t shrink. The work changes.</h3>
        <p class="lead">Deflection that comes from automation frees capacity rather than removing
        it. The contacts that remain are the ones that genuinely need a human, and the ones that
        don't stop arriving.</p>
        <div class="prose" style="margin-top:20px">
          <p>For service providers this distinction is commercial, not philosophical: margin
          improves because the same team covers more estate, and the outcome is defensible in a
          QBR because the DEX score moved with it.
          <a href="/solutions/service-providers/" style="color:var(--teal)">The service provider
          case &rarr;</a></p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("A", "Automate Issues", "/platform/automate/", "The mechanism underneath this outcome."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/", "Why the unit cost collapses."),
      ("$", "Outcomes", "/resources/outcomes/", "The numbers and the model behind them."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/self-service/ ─────────────────────────────────────────────────
PAGES["/solutions/self-service/"] = {
 "title": "Employee self-service — the fix offered in context — Nanoheal",
 "desc": "Self-service that offers the validated fix at the moment of failure, rather than a "
         "search box and a knowledge article.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; Employee self-service',
   "By outcome",
   "Self-service fails when it asks the employee to diagnose.",
   "A portal search box assumes the person can name their problem in your vocabulary. The device "
   "already knows what went wrong &mdash; so the fix can be offered rather than looked up.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Adoption is low because the interaction is backwards.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Search, read, give up, call.</h3>
      <p>The employee has to notice something is wrong, decide it is IT's problem, find the
      portal, guess the right words, read an article written for a technician, and follow it
      correctly. Each step loses people. The last step is the phone.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>The fix appears where the failure did.</h3>
      <p>The symptom is already known, so the offer is specific: one action, in context, at the
      moment it happened. No diagnosis is asked of the employee, and no article has to be written
      for them to misread.</p></div>
    </div>

    """ + shot("nanoheal &middot; workflow builder",
               "Screenshot &mdash; Intent — how it runs",
               "<b>Self Help is a delivery mode, not a separate product.</b> One authored "
               "automation is marked <em>On demand</em> and becomes available to employees "
               "through Self Help and to the service desk through Remote Execution. Nobody "
               "rewrites it for the portal.",
               "workflow-trigger.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Why the content problem disappears</p>
        <h3>Nobody writes an article. The knowledge already exists.</h3>
        <p class="lead">Traditional self-service has a permanent content backlog: every new issue
        needs an article, every article needs an owner, and accuracy decays with every OS release.</p>
        <div class="prose" style="margin-top:20px">
          <p>Here, the self-service offer is the same validated knowledge entry that autoheal and
          the service desk use. There is one artefact, maintained once, delivered three ways
          &mdash; so self-service coverage grows automatically as the
          <a href="/platform/automation-library/" style="color:var(--teal)">library</a> grows.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Where you would choose it over autoheal</p>
        <h3>When the employee should be in the loop.</h3>
        <p class="lead">Not everything should happen silently. A fix that restarts an application,
        interrupts a call, forces a reboot or touches personal data is better offered than
        imposed.</p>
        <div class="prose" style="margin-top:20px">
          <p>The delivery mode is a property of the knowledge entry and its guardrails, set once
          when it is validated. The same condition can autoheal on a kiosk and prompt on an
          executive laptop, without a second automation being built.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What it does to the score</p>
        <h3>Deflection that shows up in the experience number.</h3>
        <p class="lead">Every self-service resolution is an outcome the platform measured
        end-to-end: the condition before, the action taken, the condition after, and its effect on
        the <a href="/platform/experience-score/" style="color:var(--teal)">DEX score</a> for that
        population.</p>
        <div class="prose" style="margin-top:20px">
          <p>The employee&rsquo;s own read on it is collected the same way. A sentiment campaign can
          be attached to run <em>after</em> a remediation rather than once a year, so the answer to
          &ldquo;did that actually help?&rdquo; arrives while the incident is still recent and is
          tied to the device evidence from the same moment.</p>
          <p class="pull">An annual survey tells you how the year felt. A prompt after the fix tells you whether the fix worked.</p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("&rarr;", "Ticket deflection", "/solutions/ticket-deflection/", "The wider deflection picture."),
      ("A", "Automate Issues", "/platform/automate/", "The one entry behind all three modes."),
      ("X", "Experience score", "/platform/experience-score/", "How the improvement is proven."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/it-task-automation/ ───────────────────────────────────────────
PAGES["/solutions/it-task-automation/"] = {
 "title": "IT task automation — software, patch and the routine work — Nanoheal",
 "desc": "Software distribution, patch, onboarding, peripherals and profile work automated on the "
         "same engine that heals the device — no second agent, no scripts.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; IT task automation',
   "By outcome",
   "The work that never justified an automation project.",
   "Individually small, collectively enormous: drive mappings, printer setup, profile resets, "
   "certificate renewal, disk cleanup, onboarding sequences, software repair. Nobody funds a "
   "project for any one of them, so a human keeps doing all of them.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Routine work is automated last, and it is most of the work.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Prioritised out, every quarter.</h3>
      <p>Automation capacity goes to the biggest call drivers, which is rational. The routine
      request queue is never the biggest single driver &mdash; it is fifty small ones &mdash; so
      it never reaches the top of the list, and the estate keeps paying for it in agent minutes.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Small tasks stop being expensive.</h3>
      <p>Describing a task in plain language and validating it once is cheap enough that the
      fifty small ones are worth doing. That is the whole reason this category of work finally
      gets automated.</p></div>
    </div>

    """ + shot("nanoheal &middot; workflow builder",
               "Screenshot &mdash; Plain-language authoring",
               "<b>Described, not built.</b> The task is typed in plain English; the "
               "context layer resolves it against what the engine can do and returns a "
               "workflow to review. The quick starts are capabilities, not code samples.",
               "workflow-nl.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Software and patch</p>
        <h3>Deploy, repair, roll back, reclaim.</h3>
        <p class="lead">Install and update across the fleet or a targeted population, with repair
        for failed installs and rollback when a version misbehaves. Patch is assessed, staged,
        deployed and then <em>verified on the device</em> rather than inferred from a deployment
        record.</p>
        <div class="prose" style="margin-top:20px">
          <p>Because distribution shares the engine with remediation, a failed install is not a
          report you chase &mdash; it is a symptom, and it triggers its own repair.
          <a href="/platform/compliance-governance/" style="color:var(--teal)">Compliance &amp;
          Governance &rarr;</a></p>
        </div>
        """ + shot("nanoheal &middot; software distribution",
               "Screenshot &mdash; software profiles",
               "<b>Install and uninstall are the same object.</b> A distribution profile is "
               "authored, scoped and published on the same path as a remediation &mdash; which "
               "is why removing a superseded agent needs no more ceremony than rolling one out.",
               "swd.png") + """
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Requests and lifecycle</p>
        <h3>Onboarding, offboarding, and everything in between.</h3>
        <p class="lead">A joiner sequence touches the device, the directory, the ITSM record and
        several SaaS consoles. Automating only the device half leaves the coordination &mdash; and
        the errors &mdash; with a human.</p>
        <div class="prose" style="margin-top:20px">
          <p>Because the context layer reaches the rest of IT without a connector build, the whole
          sequence runs as one governed action across systems.
          <a href="/platform/orchestration/" style="color:var(--teal)">Orchestration &rarr;</a></p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Who authors them</p>
        <h3>The person who knows the task writes it.</h3>
        <p class="lead">Plain language in, sealed capability out. The service desk lead who knows
        exactly how a printer gets reconfigured does not need an engineer to translate it, and no
        code is produced that somebody then owns.</p>
        <div class="prose" style="margin-top:20px">
          <p>Four ways the same workflow can start: a symptom, a forecast, a request, or a
          schedule.
          <a href="/platform/workflows/" style="color:var(--teal)">Workflows in plain language
          &rarr;</a></p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("&rarr;", "Compliance &amp; Governance", "/platform/compliance-governance/", "Software, patch and policy in depth."),
      ("NL", "Workflows", "/platform/workflows/", "How a task gets described."),
      ("1,200+", "Automation library", "/platform/automation-library/", "What already exists on day one."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/compliance-audit/ ─────────────────────────────────────────────
PAGES["/solutions/compliance-audit/"] = {
 "title": "Compliance & audit readiness — Nanoheal",
 "desc": "Policy that corrects drift instead of reporting it, with a per-device evidence trail "
         "you can hand to an auditor.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; Compliance &amp; audit readiness',
   "By outcome",
   "A non-compliance report is a finding. Putting the device back is the job.",
   "Most estates can tell you exactly how many devices are out of policy. Far fewer can correct "
   "them without a project, and fewer still can evidence what happened afterwards.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Between what policy says and what the device does.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Detected, reported, remediated by hand.</h3>
      <p>A profile fails to apply. Encryption is off on a laptop that reimaged badly. A required
      agent is missing. The console reports it accurately &mdash; and then somebody works through
      the list, or the list is quietly accepted as background noise.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Drift is a symptom, so it triggers a fix.</h3>
      <p>Desired state is described in the same knowledge layer as everything else. When actual
      state diverges, the divergence is the trigger &mdash; the correction runs on the same engine
      that heals the device, with no script and no separate remediation tool.</p></div>
    </div>

    """ + shot("nanoheal &middot; classification",
               "Screenshot &mdash; device classifications",
               "<b>A baseline is only as good as the population it is scoped to.</b> Sites, "
               "regions and business units are first-class groups &mdash; what a policy links "
               "to, what a publish releases against, and the unit an auditor asks about.",
               "classification.png") + """

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Continuous, not periodic</p>
        <h3>Compliance measured the way experience is measured.</h3>
        <p class="lead">A quarterly scan tells you the state of the estate on the day of the scan.
        Continuous evaluation tells you the state now, and how long each device spent outside
        policy &mdash; which is the number an auditor is actually asking about.</p>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Persona-aware</p>
        <h3>One baseline per population, not one per estate.</h3>
        <p class="lead">A developer workstation, a call-centre desktop, a shared clinical device
        and an executive laptop cannot share a single standard without the standard becoming
        meaningless.</p>
        <div class="prose" style="margin-top:20px">
          <p>Baselines are defined per persona and enforced per persona, and the same condition
          can be corrected silently on one population and prompted on another &mdash; a property
          of the guardrails, not a second automation.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Governed autonomy</p>
        <h3>Unattended action that survives review.</h3>
        <p class="lead">Automation that corrects production devices without a human present only
        gets approved if it can be constrained and evidenced.</p>
        <div class="prose" style="margin-top:20px">
          <p>Every capability is signed and versioned; every knowledge entry is validated by a
          human once and the approval is versioned with it; every action is scoped by policy for
          population, window and blast radius, checked <em>before</em> execution; every run is
          recorded with its result.
          <a href="/platform/compliance-governance/" style="color:var(--teal)">How governance
          works &rarr;</a></p>
          <p class="pull">If you cannot show an auditor what ran and who approved it, autonomy
          never leaves the pilot.</p>
        </div>
        """ + shot("nanoheal &middot; activity log",
               "Screenshot &mdash; activity log",
               "<b>The evidence already exists.</b> Config edits, publishes and links are "
               "recorded as they happen, with the module touched, the account that made the "
               "change and the outcome. An audit pack is a filter over this &mdash; not a "
               "reconstruction from logs after the fact.",
               "audit-log.png") + """
      </div>
    </div>

    """ + nextcards([
      ("03", "Compliance &amp; Governance", "/platform/compliance-governance/", "The platform pillar in full."),
      ("&rarr;", "IT task automation", "/solutions/it-task-automation/", "Patch, software and the routine work."),
      ("I", "Intelligence", "/platform/intelligence/", "Guardrails, and how they are checked."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/internal-it/ ──────────────────────────────────────────────────
PAGES["/solutions/internal-it/"] = {
 "title": "Internal IT — do more with the team you have — Nanoheal",
 "desc": "For enterprise IT and digital workplace teams: fewer tickets, less manual work, and a "
         "digital experience that improves continuously instead of being measured continuously.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; Internal IT',
   "For internal IT",
   "Do more with the team you have.",
   "Fortune 1000 estates across manufacturing, technology services and SaaS &mdash; typically "
   "replacing a DEX tool that measures well and acts poorly, or sitting alongside one until the "
   "renewal conversation makes the choice obvious.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/resources/outcomes/">See the business case</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">What changes</p>
      <h2 class="h2">Four things a digital workplace team gets asked for.</h2>
      <p class="lede">None of these are new asks. What is new is being able to move them without
      more headcount and without an automation engineering function.</p>
    </div>
    <div class="forwho-grid">
      <div class="forwho">
        <p class="label">The ask</p>
        <h3>What you are measured on.</h3>
        <div class="linkrow"><b>Fewer tickets</b><span>Resolve issues before they reach the service desk &mdash; 17% autohealed and 35% overall avoidance in production at ~200,000 endpoints.</span></div>
        <div class="linkrow"><b>Less manual work</b><span>Automate IT tasks across devices and the systems around them, including the long tail nobody funded.</span></div>
        <div class="linkrow"><b>Better experience</b><span>Improve DEX continuously rather than reporting it monthly, on a score that is defined independently of any release.</span></div>
        <div class="linkrow"><b>A more autonomous workplace</b><span>Every resolved symptom becomes reusable knowledge, so the estate needs less firefighting each quarter than the last.</span></div>
      </div>
      <div class="forwho">
        <p class="label">The constraint</p>
        <h3>Why it usually stalls.</h3>
        <div class="linkrow"><b>No automation team</b><span>Automation lands on the people already running the estate, so it happens between incidents or not at all.</span></div>
        <div class="linkrow"><b>Coverage caps out</b><span>The top ten drivers get automated. The eleventh costs the same and returns a tenth as much, so it never happens.</span></div>
        <div class="linkrow"><b>Drift breaks what exists</b><span>Scripts written against last year's build fail quietly after a patch, and maintenance eats the roadmap.</span></div>
        <div class="linkrow"><b>Proof is contested</b><span>Improvement is asserted from a vendor-defined score that moves when the vendor changes it.</span></div>
      </div>
    </div>

    """ + shot("nanoheal &middot; experience score",
               "Screenshot &mdash; DEX trend — programme view",
               "<b>One number a programme can be run on.</b> Fleet DEX tracked "
               "continuously on a fixed methodology, so the line moving is the estate "
               "improving — which is what makes an autonomy programme reportable quarter "
               "on quarter.",
               "dex-score.png") + """
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Where teams start</p>
      <h2 class="h2">Your top three call drivers, on a live endpoint.</h2>
      <p class="lede">Because 1,200+ configurations ship on day one, the first proof point does
      not require a build. The usual sequence looks like this.</p>
    </div>
    <div class="issues">
      <div class="issue">
        <p class="n">Week one</p>
        <h3>Match the library against the drivers you already have.</h3>
        <p class="lead">Your ticket categories are mapped against existing configurations. What is
        already covered gets switched on and targeted; what is not becomes the first authoring
        candidates.</p>
      </div>
      <div class="issue">
        <p class="n">First quarter</p>
        <h3>Autoheal on the common cases, self-service on the disruptive ones.</h3>
        <p class="lead">The same validated knowledge serves both, so the choice is a guardrail
        setting per population rather than two pieces of work.</p>
      </div>
      <div class="issue">
        <p class="n">Every quarter after</p>
        <h3>The tail, ranked by return.</h3>
        <p class="lead">The platform surfaces where manual work still is and what closing it would
        be worth, so the roadmap comes from the estate rather than from a workshop.
        <a href="/platform/manage/" style="color:var(--teal)">Continuous improvement &rarr;</a></p>
      </div>
    </div>

    """ + nextcards([
      ("$", "Outcomes &amp; business case", "/resources/outcomes/", "The numbers, and the model behind them."),
      ("&rarr;", "Ticket deflection", "/solutions/ticket-deflection/", "The deflection argument in full."),
      ("&rarr;", "Why DEX alone isn't enough", "/why-nanoheal/why-dxa/", "If you already own a DEX tool."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/service-providers/ ────────────────────────────────────────────
PAGES["/solutions/service-providers/"] = {
 "title": "Service providers & GSIs — an autonomy layer inside your delivery model — Nanoheal",
 "desc": "Add autonomy to a managed workplace service without changing how you deliver it. Your "
         "contract, your client, your delivery model — multi-tenant from the ground up.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; Service providers &amp; GSIs',
   "For service providers",
   "Deliver more value from the service you already run.",
   "Delivered inside an existing managed workplace service. Your contract, your client, your "
   "delivery model &mdash; with an autonomy layer your competitors cannot price.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Talk to us about a deal</a>'
   '<a class="btn btn-line" href="/company/partners/">Partner model</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Deflection promises are priced in, and then delivered by hand.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Margin comes out of the team.</h3>
      <p>A workplace deal is won on a deflection commitment. The automation to deliver it is a
      services line item, built per client, maintained per client. When the numbers get tight, the
      only lever left is the size of the team on the account.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>Margin comes out of the work.</h3>
      <p>1,200+ configurations arrive with the platform and the rest are authored without an
      engineering team. Deflection comes from resolving issues, so the same headcount covers more
      estate rather than the estate covering fewer people.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Multi-tenant by design</p>
        <h3>Build once, publish across the book of business.</h3>
        <p class="lead">A configuration validated for one client can be published to others with
        tenant-level scoping and guardrails intact. The library becomes an asset of your practice
        rather than a per-account cost.</p>
        <div class="prose" style="margin-top:20px">
          <p>That is also what makes small accounts economic: the same automation library serves a
          500-seat client and a 200,000-seat client, and the marginal cost of onboarding the small
          one is close to zero.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Inside your delivery model</p>
        <h3>Not a product you resell. A layer you deliver.</h3>
        <p class="lead">Your contract, your service desk, your SLAs, your brand in front of the
        client. Nanoheal runs underneath, and the outcome it produces is attributable to your
        service.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Differentiate.</h3><p>Add autonomy without changing your delivery
          model or retraining the account team.</p></div>
          <div class="tile"><h3>Protect margin.</h3><p>Deflection comes from automation and
          resolution, not from reducing the team the client is paying for.</p></div>
          <div class="tile"><h3>Prove outcomes.</h3><p>A patented, vendor-independent score means
          the improvement in the QBR is measured rather than asserted.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; What you can commit to</p>
        <h3>Bid autonomy you can actually deliver.</h3>
        <p class="lead">Deflection commitments are only safe if the cost of hitting them is
        predictable. When automations are knowledge rather than code, the cost of the next hundred
        is knowable at bid time.</p>
        <div class="prose" style="margin-top:20px">
          <p>Expand coverage continuously without an engineering backlog: start with the pre-built
          library on day one of the transition, and keep adding through the life of the contract
          without a change request for each addition.
          <a href="/resources/outcomes/" style="color:var(--teal)">The numbers &rarr;</a></p>
        </div>
      </div>
    </div>

    """ + nextcards([
      ("1,200+", "Automation library", "/platform/automation-library/", "The asset your practice compounds."),
      ("&rarr;", "OEMs, channel &amp; SMB", "/solutions/oem-channel/", "If your book is many small tenants."),
      ("&rarr;", "Partners", "/company/partners/", "How we work with GSIs and channels."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /solutions/oem-channel/ ──────────────────────────────────────────────────
PAGES["/solutions/oem-channel/"] = {
 "title": "OEMs, channel & SMB — multi-tenant from the ground up — Nanoheal",
 "desc": "One automation library serving a support channel's whole book of business, with "
         "tenant-level scoping — the same engine at 500 endpoints as at 200,000.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/solutions/">Solutions</a> &nbsp;/&nbsp; OEMs, channel &amp; SMB',
   "For OEMs and support channels",
   "One library. Every tenant you support.",
   "Multi-tenant from the ground up, so the same automation library serves a support channel's "
   "whole book of business &mdash; and a 500-endpoint client gets the same engine as a "
   "200,000-endpoint one.") + """

<section class="band">
  <div class="wrap">
    <div class="head"><p class="label">The issue</p>
      <h2 class="h2">Small accounts can&rsquo;t carry a per-account automation build.</h2></div>
    <div class="ps">
      <div><p class="t">What normally happens</p><h3>Automation is for the big logos only.</h3>
      <p>Enterprise-grade automation requires an enterprise-grade project. The economics never
      work below a certain seat count, so the long tail of the channel is supported the way it
      always was: by people, on the phone, one device at a time.</p></div>
      <div class="fix"><p class="t">What Nanoheal does</p><h3>The build is amortised across the book.</h3>
      <p>Author once, publish to every tenant that needs it. The marginal cost of extending
      coverage to another client is a targeting decision, not a project &mdash; which is what
      makes autonomy viable at SMB scale.</p></div>
    </div>

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Tenancy</p>
        <h3>Isolation where it matters, sharing where it pays.</h3>
        <p class="lead">Data, policy and guardrails are scoped per tenant. Knowledge is shareable
        across tenants by choice, so an entry proven on one estate strengthens the whole book
        without leaking anything between clients.</p>
      </div>

      <div class="issue">
        <p class="n">02 &mdash; For device OEMs</p>
        <h3>Support the hardware after it ships.</h3>
        <p class="lead">Driver and firmware faults, thermal and battery degradation, imaging
        defects and returns driven by software problems all show up as symptoms the OS already
        reports.</p>
        <div class="prose" style="margin-top:20px">
          <p>Resolving them in place reduces support contacts and no-fault-found returns, and the
          same telemetry shows which build, model or component is generating them &mdash; on the
          fleet, before the pattern reaches a warranty report.</p>
        </div>
      </div>

      <div class="issue">
        <p class="n">03 &mdash; Onboarding a tenant</p>
        <h3>Day one is coverage, not configuration.</h3>
        <p class="lead">A new client starts with the 1,200+ pre-built configurations plus whatever
        your practice has already added. There is no per-tenant authoring phase before the first
        outcome.</p>
      </div>
    </div>

    """ + nextcards([
      ("&rarr;", "Service providers &amp; GSIs", "/solutions/service-providers/", "The managed-service case."),
      ("1,200+", "Automation library", "/platform/automation-library/", "What every tenant starts with."),
      ("&rarr;", "Partners", "/company/partners/", "How the partnership works."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /resources/ ──────────────────────────────────────────────────────────────
PAGES["/resources/"] = {
 "title": "Resources — understand the category, and the proof — Nanoheal",
 "desc": "The DEX and DXA category explained, the technical case for symptom-triggered "
         "automation, production outcomes and analyst recognition.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Resources',
   "Resources",
   "The argument, and the evidence for it.",
   "Two things are worth your time before a demo: understanding why measuring the workplace "
   "turned out not to be enough, and seeing what happens to the numbers when the doing gets "
   "solved as well.") + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">Understand the category</p>
      <h2 class="h2">DEX made the workplace visible. DXA makes it actionable.</h2>
      <p class="lede">Digital Experience Automation is the evolution of DEX, not a replacement for
      it. These four pages make that case from first principles.</p>
    </div>
    """ + cards([
      ("01", "What is DEX", "/digital-experience/",
       "Measure, forecast, detect, diagnose, prove &mdash; the five questions a digital "
       "experience platform has to answer, and what gets measured to answer them.",
       "The measuring half"),
      ("02", "What is DXA", "/digital-experience-automation/",
       "Insight becomes action, and action becomes the next insight. The loop a dashboard "
       "cannot close on its own.",
       "The acting half"),
      ("03", "Why DEX alone isn't enough", "/why-nanoheal/why-dxa/",
       "One half of the problem was solved. The other half was outsourced to your engineers, "
       "one script at a time.",
       "The category argument"),
      ("04", "Why not scripts", "/why-nanoheal/why-not-scripts/",
       "The technical case for symptom-triggered automation over PowerShell remediation &mdash; "
       "detection cost, payload weight, and what estate drift does to authored code.",
       "The technical case"),
    ]) + """
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Proof</p>
      <h2 class="h2">What it did, and who has looked at it.</h2>
    </div>
    """ + cards([
      ("$", "Outcomes &amp; business case", "/resources/outcomes/",
       "Production numbers from a Fortune 100 estate, and the model for turning ticket "
       "avoidance and recovered employee time into a figure a CFO will accept.",
       "The numbers"),
      ("&#9733;", "Analyst recognition", "/resources/analysts/",
       "Gartner Peer Insights, ISG Provider Lens Rising Star for DEX, Forrester's DEX "
       "landscape, and the patented scoring methodology.",
       "Third-party view"),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /resources/outcomes/ ─────────────────────────────────────────────────────
PAGES["/resources/outcomes/"] = {
 "title": "Outcomes & business case — Nanoheal",
 "desc": "Production results from a Fortune 100 estate of ~200,000 endpoints, and the model for "
         "valuing ticket avoidance and recovered employee time.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/resources/">Resources</a> &nbsp;/&nbsp; Outcomes',
   "Proof",
   "What autonomy is worth, and how the number is built.",
   "Two separate things are worth separating: what has actually happened in production, and what "
   "a model projects for an estate of a given size. Both are below, labelled.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Model it for your estate</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">In production</p>
      <h2 class="h2">Fortune 100 manufacturer, ~200,000 endpoints.</h2>
      <p class="lede">These are measured results from a live estate, not a projection.</p>
    </div>
    """ + metrics([
      ("Measured", "150+", "automations live in production"),
      ("Measured", "17%", "of tickets resolved by autoheal, with no human contact"),
      ("Measured", "35%", "overall ticket avoidance across autoheal, self-service and assisted"),
      ("Measured", "~200K", "endpoints on one engine, one library, one context layer"),
    ]) + """
    <div class="prose" style="margin-top:34px">
      <p>The 17% and the 35% are worth reading together. Autoheal is the share where nobody was
      involved at all &mdash; no ticket, no contact, no employee time lost. The wider figure adds
      the contacts that were resolved at first touch by self-service or by an agent executing a
      single validated capability instead of following a runbook.</p>
      <p class="pull">Deflection that comes from resolution is durable. Deflection that comes from
      friction is a queue somewhere else.</p>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Illustrative model</p>
      <h2 class="h2">Per 10,000 employees, per year.</h2>
      <p class="lede">This is a model, not a measured result. It is shown with its inputs so you
      can replace them with yours &mdash; the arithmetic matters more than our defaults.</p>
    </div>
    """ + metrics([
      ("Modelled", "$1.0M", "IT cost avoided &mdash; contacts that never reach a human, at your "
       "blended cost per ticket"),
      ("Modelled", "$8.6M", "employee productivity recovered &mdash; disruption time returned to "
       "the people being paid for it"),
      ("Input", "Ticket mix", "your top call drivers, matched against the 1,200+ pre-built "
       "configurations before anything is built"),
      ("Input", "Rates", "your cost per contact and your loaded employee cost &mdash; both "
       "numbers you already have"),
    ]) + """
    <div class="prose" style="margin-top:34px">
      <p>The productivity figure is nearly nine times the IT saving, and that ratio is the honest
      argument for autonomy. The service desk cost of a broken VPN profile is one contact. The
      business cost is the hour before the contact, the interruption after it, and the same
      condition sitting unreported on a few thousand other machines.</p>
      <p>Which is also why the <a href="/platform/experience-score/" style="color:var(--teal)">DEX
      score</a> matters commercially: a patented methodology defined independently of any release
      means a ten-point gain means the same thing in Q3 as it did in Q1, so the improvement can be
      priced rather than argued about.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">Where the numbers come from</p>
      <h2 class="h2">Four levers, one loop.</h2>
    </div>
    """ + nextcards([
      ("&rarr;", "Ticket deflection", "/solutions/ticket-deflection/", "Contacts that never happen."),
      ("&rarr;", "IT task automation", "/solutions/it-task-automation/", "Agent minutes returned."),
      ("&rarr;", "Compliance &amp; audit", "/solutions/compliance-audit/", "Remediation effort and audit cost."),
    ]) + nextcards([
      ("X", "Experience score", "/platform/experience-score/", "The number the improvement is measured on."),
      ("M", "Continuous improvement", "/platform/manage/", "How the next opportunity is ranked and priced."),
      ("1,200+", "Automation library", "/platform/automation-library/", "Why value starts on day one."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /resources/analysts/ ─────────────────────────────────────────────────────
PAGES["/resources/analysts/"] = {
 "title": "Analyst recognition — Nanoheal",
 "desc": "Gartner Peer Insights, ISG Provider Lens Rising Star for DEX, Forrester's DEX "
         "landscape, and the patented DEX scoring methodology.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/resources/">Resources</a> &nbsp;/&nbsp; Analyst recognition',
   "Proof",
   "Recognised across the DEX category.",
   "Nanoheal is assessed as a digital experience platform by the analysts who cover the category, "
   "and rated by the practitioners who run it.") + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">Third-party view</p>
      <h2 class="h2">Where we appear, and what for.</h2>
    </div>
    """ + metrics([
      ("Gartner", "4.6/5", "Peer Insights rating across 27+ mentions from verified practitioners"),
      ("ISG", "Rising Star", "ISG Provider Lens\\u2122, Digital Experience"),
      ("Forrester", "Q2 2026", "Included in the DEX landscape"),
      ("Patent", "US 9,477,573", "DEX scoring methodology, held by Nanoheal"),
    ]) + """
    <div class="prose" style="margin-top:34px">
      <p>Analyst coverage of this category is organised around measurement, which is where the
      category started. It is a fair way to be assessed and we hold that table &mdash;
      <a href="/platform/dex-intelligence/" style="color:var(--teal)">measurement, forecasting,
      anomaly detection and root cause</a> are all present, and the score underneath them is
      patented rather than proprietary-and-adjustable.</p>
      <p>The part the category's evaluation criteria do not yet weight heavily is what happens
      after a finding: whether the platform can resolve it, run the estate, enforce policy and
      orchestrate the systems around the device on the same engine, without shipping code to every
      endpoint. That is the comparison worth making in a bake-off, and it is the one we ask for.</p>
      <p class="pull">Ask each vendor how many automations ship on day one &mdash; and how many of
      them you will have to maintain.</p>
    </div>
    """ + nextcards([
      ("$", "Outcomes", "/resources/outcomes/", "Production numbers and the ROI model."),
      ("X", "Experience score", "/platform/experience-score/", "What the patent actually covers."),
      ("&rarr;", "Why DEX alone isn't enough", "/why-nanoheal/why-dxa/", "The category argument."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /company/ ────────────────────────────────────────────────────────────────
PAGES["/company/"] = {
 "title": "About Nanoheal — turning the digital workplace autonomous",
 "desc": "Nanoheal builds the operating system for the digital workplace: DEX intelligence wired "
         "to a governed capability engine, so insight becomes action without code.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Company',
   "About",
   "We build the half of DEX that was left to your engineers.",
   "Nanoheal is a digital experience automation platform. It measures the digital workplace the "
   "way a DEX tool does, and then does something a dashboard cannot: it resolves what it finds, "
   "runs and governs the estate, and orchestrates the systems around the device \\u2014 without "
   "shipping code to a single endpoint.",
   '<div class="acts"><a class="btn btn-solid" href="/#demo">Schedule a Demo</a>'
   '<a class="btn btn-line" href="/platform/">See the platform</a></div>') + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">What we believe</p>
      <h2 class="h2">Knowledge, not code.</h2>
      <p class="lede">One conviction shapes every design decision in the product, and it is worth
      stating plainly because it is testable.</p>
    </div>
    <div class="prose" style="margin-top:32px">
      <p>An automation should not be a piece of software. The moment a fix is authored as code,
      somebody owns it forever: it has to be reviewed, deployed to every endpoint, kept resident
      to detect the thing it fixes, and rewritten when the estate moves underneath it. That cost
      is why automation coverage across this entire category stops at the top call drivers.</p>
      <p>So Nanoheal ships knowledge instead. The operating system already reports the symptom, so
      nothing has to poll for it. The engine already exposes the capabilities, so nothing has to
      be generated. What a new automation adds is a small, sealed, versioned description of what
      to do &mdash; validated once by a human, then reusable across the estate.</p>
      <p class="pull">Coverage compounds when the next automation costs almost nothing. Everything
      else in the product follows from that.</p>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">Who runs on Nanoheal</p>
      <h2 class="h2">Same engine, whether you run 500 endpoints or 200,000.</h2>
    </div>
    <div class="g3" style="margin-top:20px">
      <div class="tile"><h3>Enterprise IT.</h3><p>Fortune 1000 estates across manufacturing,
      technology services and SaaS &mdash; typically replacing a DEX tool that measures well and
      acts poorly. <a href="/solutions/internal-it/" style="color:var(--teal)">More &rarr;</a></p></div>
      <div class="tile"><h3>Global system integrators.</h3><p>Delivered inside an existing managed
      workplace service. Your contract, your client, your delivery model.
      <a href="/solutions/service-providers/" style="color:var(--teal)">More &rarr;</a></p></div>
      <div class="tile"><h3>OEMs, support channels and SMB.</h3><p>Multi-tenant from the ground up,
      so one automation library serves a whole book of business.
      <a href="/solutions/oem-channel/" style="color:var(--teal)">More &rarr;</a></p></div>
    </div>

    <p class="label" style="margin-top:52px">Where we are</p>
    <div class="g3" style="margin-top:20px">
      <div class="tile"><h3>Utah.</h3><p>North America.</p></div>
      <div class="tile"><h3>Bangalore.</h3><p>Engineering and platform.</p></div>
      <div class="tile"><h3>Manila.</h3><p>Service delivery and support.</p></div>
    </div>

    """ + nextcards([
      ("&rarr;", "Partners", "/company/partners/", "GSIs, OEMs and support channels."),
      ("&#9733;", "Analyst recognition", "/resources/analysts/", "Gartner, ISG, Forrester."),
      ("$", "Outcomes", "/resources/outcomes/", "What it has done in production."),
    ]) + """
  </div>
</section>
""" + CTA}


# ── /company/partners/ ───────────────────────────────────────────────────────
PAGES["/company/partners/"] = {
 "title": "Partners — GSIs, OEMs and support channels — Nanoheal",
 "desc": "Nanoheal is delivered inside existing managed workplace services. Multi-tenant, "
         "white-labelled under your delivery model, with an automation library your practice owns.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/company/">Company</a> &nbsp;/&nbsp; Partners',
   "Partners",
   "An autonomy layer inside the service you already deliver.",
   "Most Nanoheal estates reach the client through a partner. The platform is built for that: "
   "multi-tenant, delivered under your contract and your brand, with the automation library "
   "accruing to your practice rather than to us.") + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">How it works</p>
      <h2 class="h2">Three things partners ask first.</h2>
    </div>
    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Ownership</p>
        <h3>Your contract, your client, your delivery model.</h3>
        <p class="lead">Nanoheal sits underneath the workplace service you already run. The service
        desk stays yours, the SLAs stay yours, and the improvement is attributable to your service
        rather than to a tool the client bought separately.</p>
      </div>
      <div class="issue">
        <p class="n">02 &mdash; The library is an asset</p>
        <h3>Author once, publish across the book of business.</h3>
        <p class="lead">Configurations validated on one account can be published to others with
        tenant-level scoping intact. What your practice builds compounds across every client you
        support, instead of being rebuilt per engagement.
        <a href="/platform/automation-library/" style="color:var(--teal)">The library &rarr;</a></p>
      </div>
      <div class="issue">
        <p class="n">03 &mdash; The commercial case</p>
        <h3>Bid deflection you can price.</h3>
        <p class="lead">Deflection commitments are only safe when the cost of hitting them is
        predictable. Knowledge-based automation makes the cost of the next hundred automations
        knowable at bid time, which is what lets autonomy appear in the proposal rather than in
        the transformation roadmap.
        <a href="/solutions/service-providers/" style="color:var(--teal)">The service provider
        case &rarr;</a></p>
      </div>
    </div>

    """ + nextcards([
      ("MSP", "Service providers &amp; GSIs", "/solutions/service-providers/", "The full argument."),
      ("OEM", "OEMs, channel &amp; SMB", "/solutions/oem-channel/", "Many tenants, one library."),
      ("&rarr;", "Talk to us", "/#demo", "Partner conversations start the same way: a live endpoint."),
    ]) + """
  </div>
</section>
""" + CTA}
