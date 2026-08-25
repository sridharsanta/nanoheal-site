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
  <p class="lab">Recognised across the DEX category.</p>
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
            </div>
          </div>
          <div class="os-acc-item">
            <label for="ostab-1" class="os-acc-label">Automate Issues</label>
            <div class="os-acc-body" id="obody-1">
              <p class="os-cap-title">Turn every symptom into a reusable capability</p>
              <p class="os-cap-desc">The context layer gives intelligence the knowledge needed to extend its capabilities to new symptoms across the OS, applications, and resources — without code. Validate once, then make it available through Autoheal, Self-service, or Assisted IT</p>
            </div>
          </div>
          <div class="os-acc-item">
            <label for="ostab-2" class="os-acc-label">Compliance &amp; Governance</label>
            <div class="os-acc-body" id="obody-2">
              <p class="os-cap-title">IT management automated. Compliance continuously enforced</p>
              <p class="os-cap-desc">The context layer gives intelligence the knowledge to extend its capabilities without code — automating software, patches, security updates and policies by persona, while continuously detecting and restoring drift to keep the fleet compliant.</p>
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
    </div>
    <p class="label" style="margin-top:44px">Who runs on Nanoheal &mdash; same engine, whether you run 500 endpoints or 200,000</p>
    <div class="g3" style="margin-top:20px">
      <div class="tile"><h3>Enterprise IT.</h3><p>Fortune 1000 estates across manufacturing,
      technology services and SaaS &mdash; typically replacing a DEX tool that measures well and
      acts poorly.</p></div>
      <div class="tile"><h3>Global system integrators.</h3><p>Delivered inside an existing managed
      workplace service. Your contract, your client, your delivery model &mdash; with an autonomy
      layer your competitors cannot price.</p></div>
      <div class="tile"><h3>OEMs, support channels and SMB.</h3><p>Multi-tenant from the ground up,
      so the same automation library serves a support channel's whole book of business.</p></div>
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
      </div>
      <div class="forwho">
        <p class="label">For service providers</p>
        <h3>Deliver more value from the service you already run.</h3>
        <div class="linkrow"><b>Differentiate your service</b><span>Add autonomy without changing your delivery model.</span></div>
        <div class="linkrow"><b>Protect margin</b><span>Deflection comes from automation and resolution, not reducing the team.</span></div>
        <div class="linkrow"><b>Prove outcomes</b><span>Measure the improvement and make autonomy an outcome you can stand behind.</span></div>
        <div class="linkrow"><b>Expand coverage</b><span>Start with pre-built capabilities and continuously add more without an engineering backlog.</span></div>
      </div>
    </div>
  </div>
</section>
""" + CTA}

# ── /platform/ ───────────────────────────────────────────────────────────────
PAGES["/platform/"] = {
 "title": "The Digital Experience Automation platform \u2014 Nanoheal",
 "desc": "Everything you expect from DEX. Then the ability to act on what it tells you. "
         "Measurement, intelligence, autonomous action and proof, on one engine.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Platform',
   "Platform overview",
   "The Digital Experience Automation platform.",
   "Everything you expect from DEX. Then the ability to act on what it tells you. Measurement "
   "feeds a context layer, the context layer decides what a symptom means here, action runs "
   "wherever the work belongs, and the outcome is scored \u2014 which reveals the next gap "
   "worth closing.") + """

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The four layers</p>
      <h2 class="h2">Measure. Understand. Act. Improve.</h2>
      <p class="lede">Not four products you assemble &mdash; four things that have to be true at
      the same time, running on one engine, one context layer and one knowledge library.</p>
    </div>
    <div class="tl">
      <div><p class="w">DEX</p><h3>Measure the experience</h3><p>Devices, applications, network,
      collaboration and employee experience, scored on a patented methodology.</p></div>
      <div><p class="w">Intelligence</p><h3>Understand the context</h3><p>DEX signals, IT
      knowledge, SOPs, ITSM history, CMDB and workplace context.</p></div>
      <div><p class="w">DXA</p><h3>Act on the experience</h3><p>Resolve, autoheal, self-service,
      IT tasks, workflows and orchestration across the ecosystem.</p></div>
      <div><p class="w">Outcome</p><h3>Measure the result</h3><p>DEX score, ticket avoidance,
      productivity and automation coverage &mdash; proof, not assertion.</p></div>
    </div>
    <div style="margin-top:30px;display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-line" href="/digital-experience/">Digital Experience</a>
      <a class="btn btn-line" href="/digital-experience-automation/">Digital Experience Automation</a>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">The framework underneath</p>
      <h2 class="h2">AIM-X. Automate with Intelligence. Manage the eXperience.</h2>
      <p class="lede">Internally the four layers run as a closed loop we call AIM-X. Nobody has to
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
      <p>The four stages are not four products. They are four things that have to be true at the
      same time for the loop to close, and they run on one engine, one context layer and one
      knowledge library.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="label">The four stages</p>
      <h2 class="h2">What each stage solves.</h2>
    </div>
    """ + nextcards([
      ("A", "Automate", "/platform/automate/",
       "Remediation is a software project. It shouldn't be."),
      ("I", "Intelligence", "/platform/intelligence/",
       "Telemetry says what happened. Not what your organisation does about it."),
      ("M", "Manage &amp; evolve", "/platform/manage/",
       "Coverage stalls at the top call drivers. Here's why it doesn't have to."),
    ]) + nextcards([
      ("X", "Experience", "/platform/deliverexperience/",
       "Improvement gets asserted. Yours will be scored."),
      ("&rarr;", "Observe &amp; predict", "/platform/observe-predict/",
       "Analytics, forecasting and anomaly detection &mdash; the input to all of it."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/",
       "The technical case, in full."),
    ]) + nextcards([
      ("&rarr;", "IT operations", "/platform/it-operations/",
       "Software distribution, patch and device policy on the same engine."),
      ("&rarr;", "Orchestration", "/platform/orchestration/",
       "ServiceNow, Active Directory, anything with a standard API. No code."),
      ("&rarr;", "Workflows &amp; natural language", "/platform/workflows/",
       "Describe the task; the context layer compiles it."),
    ]) + """
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
      ("&rarr;", "Observe &amp; predict", "/platform/observe-predict/",
       "Analytics, forecasting and anomaly detection in depth."),
      ("&rarr;", "Experience scoring", "/platform/deliverexperience/",
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
      ("&rarr;", "IT operations", "/platform/it-operations/",
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
 "title": "Automate — resolution without a script — Nanoheal",
 "desc": "Every remediation is normally a bespoke software project. Nanoheal triggers on the "
         "symptom the OS already reports and executes governed capabilities instead of code.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Automate',
   "A &mdash; Automate",
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
          <a href="/platform/it-operations/" style="color:var(--teal)">IT operations &rarr;</a></p></div>
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
          <div class="tile"><h3>Self-service.</h3><p>The employee is offered the fix at the moment
          of failure and applies it themselves. Deflection without the service desk touching it.</p></div>
          <div class="tile"><h3>Assisted.</h3><p>The service desk executes the same capability in a
          single action, with no runbook to follow and no elevation risk.</p></div>
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
          between those two numbers is the gap this page is about.</p>
        </div>
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
          <a href="/platform/it-operations/" style="color:var(--teal)">software, patch and policy</a>,
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
          <a href="/platform/it-operations/" style="color:var(--teal)">software, patch and policy</a>
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
      ("X", "Experience", "/platform/deliverexperience/", "Proving any of it worked."),
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
      ("X", "Experience", "/platform/deliverexperience/", "The score that proves the expansion worked."),
      ("A", "Automate", "/platform/automate/", "What gets created, and how it runs."),
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/", "Why maintenance is the real cost."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/deliverexperience/ ─────────────────────────────────────────────
PAGES["/platform/deliverexperience/"] = {
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

# ── /platform/observe-predict/ ───────────────────────────────────────────────
PAGES["/platform/observe-predict/"] = {
 "title": "Observe & predict — analytics, forecasting, anomaly detection — Nanoheal",
 "desc": "Everything a DEX platform measures, plus forecasting and anomaly detection — and it "
         "feeds an engine that can act on what it finds.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Observe &amp; predict',
   "Observe &amp; predict",
   "Analytics is table stakes. We hold the table.",
   "Fleet-wide measurement, forecasting and anomaly detection &mdash; scored on a patented DEX "
   "methodology. The difference is not what Nanoheal sees. It is that what Nanoheal sees is wired "
   "to something that can act on it.") + """

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

    <div class="issues">
      <div class="issue">
        <p class="n">01 &mdash; Measure</p>
        <h3>What the employee actually experienced.</h3>
        <p class="lead">Device performance and stability, application behaviour, network and
        connectivity quality, boot and logon times, crash and hang patterns, resource pressure,
        configuration drift &mdash; across Windows, macOS, Linux, VDI, mobile and IoT.</p>
        <div class="prose" style="margin-top:20px">
          <p>It resolves to a single <a href="/platform/deliverexperience/" style="color:var(--teal)">DEX
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
    </div>

    """ + nextcards([
      ("I", "Intelligence", "/platform/intelligence/", "What turns a finding into an action."),
      ("A", "Automate", "/platform/automate/", "The engine that executes it."),
      ("X", "Experience", "/platform/deliverexperience/", "The score all of it moves."),
    ]) + """
  </div>
</section>
""" + CTA}

# ── /platform/it-operations/ ─────────────────────────────────────────────────
PAGES["/platform/it-operations/"] = {
 "title": "IT operations — software, patch and policy on one engine — Nanoheal",
 "desc": "Software distribution, patch management and device compliance policy run on the same "
         "capability engine and knowledge layer as remediation — not a separate tool.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; IT operations',
   "IT operations",
   "The same engine that heals the device also runs it.",
   "Software distribution, patch management, device compliance policy. Not a second product and "
   "not a second agent &mdash; the same capability engine, driven by the same knowledge layer.") + """

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
   '<a href="/">Home</a> &nbsp;/&nbsp; <a href="/platform/">Platform</a> &nbsp;/&nbsp; Orchestration',
   "Orchestration &amp; integration",
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
      ("&rarr;", "IT operations", "/platform/it-operations/", "The device-side half."),
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
      </div>

      <div class="issue">
        <p class="n">02 &mdash; Triggering</p>
        <h3>Four ways the same workflow starts.</h3>
        <div class="tblwrap">
          <table class="spec">
            <thead><tr><th>Trigger</th><th>Starts when</th><th>Typical use</th></tr></thead>
            <tbody>
              <tr><td>Symptom</td><td>The OS reports the condition &mdash; event, service state, crash, error</td><td>Autoheal, before anyone notices</td></tr>
              <tr><td>Forecast</td><td>Prediction or anomaly detection flags a condition building</td><td>Prevention &mdash; the ticket never exists</td></tr>
              <tr><td>Request</td><td>An employee, a service-desk agent or an IT agent asks</td><td>Self-service and assisted resolution</td></tr>
              <tr><td>Schedule or policy</td><td>A window, a compliance obligation, a drift threshold</td><td>Patch rings, policy enforcement, routine tasks</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose" style="margin-top:22px">
          <p>One authored workflow serves all four. This is the part that compounds: the effort is
          spent once and recovered every time the condition recurs, through whichever channel it
          arrives.</p>
        </div>
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
