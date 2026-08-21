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
    on a live endpoint &mdash; with no script written, and nothing left running to watch for them.</p>
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
 "title": "Nanoheal — Automation that triggers on the symptom, not a script",
 "desc": "DEX made the digital workplace measurable. Nanoheal makes it autonomous — "
         "resolution triggered the moment the operating system reports the symptom.",
 "scripts": '<script src="/assets/plaster.js"></script>',
 "body": """
<section class="hero">
  <div class="hero-l"><div class="in">
    <h1>Automation that triggers on the symptom, <span class="q">not on a script.</span></h1>
    <p class="sub">DEX made the digital workplace measurable. Nanoheal makes it autonomous &mdash;
    resolving issues the moment the operating system reports them. No scripts to write.
    Nothing left running to watch.</p>
    <div class="acts">
      <a class="btn btn-solid" href="/#demo">Schedule a Demo</a>
      <a class="btn btn-line" href="/why-nanoheal/why-not-scripts/">See how it triggers</a>
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

<section class="band" id="difference">
  <div class="wrap">
    <div class="head">
      <p class="label">The difference</p>
      <h2 class="h2">Scripts have to go looking for a problem. Nanoheal is told.</h2>
      <p class="lede">Every operating system already announces its own failures &mdash; event logs,
      service states, crashes, the error the user is staring at. Script-based automation ignores
      that channel and rebuilds detection from scratch. Nanoheal listens to it.</p>
    </div>

    <div class="vs">
      <div class="pane">
        <p class="tag">Script-based automation</p>
        <h3>Write code, ship it, hope it holds.</h3>
        <p class="note">The prevailing model across the category.</p>
        <ul class="steps">
          <li><span class="ic"></span><span><b>An engineer writes a script.</b>New code for every
          symptom, and every variation of it.</span></li>
          <li><span class="ic"></span><span><b>It is pushed to the fleet.</b>Payloads accumulate.
          Every new fix adds weight to every endpoint.</span></li>
          <li><span class="ic"></span><span><b>It has to keep polling.</b>To catch a symptom the
          script stays resident and re-checks on an interval &mdash; burning CPU, memory and
          battery on machines that are mostly fine.</span></li>
          <li><span class="ic"></span><span><b>Then the estate moves.</b>A patch, a policy, a new
          OS build &mdash; and it fails silently until somebody notices.</span></li>
        </ul>
        <p class="verdict neg"><b>The real cost:</b> detection you paid to build, and pay again
        to run, on every device, all the time.</p>
      </div>
      <div class="pane now">
        <p class="tag">Nanoheal &middot; symptom-triggered</p>
        <h3>The symptom is the trigger. No script exists.</h3>
        <p class="note">Detection is free, because the OS already did it.</p>
        <ul class="steps">
          <li><span class="ic"></span><span><b>The OS reports the symptom.</b>An event log entry,
          a service failure, a crash, an error surfaced to the user.</span></li>
          <li><span class="ic"></span><span><b>Intelligence reads the context.</b>What this symptom
          means <em>here</em> &mdash; against DEX signals, your SOPs, ITSM history and CMDB.</span></li>
          <li><span class="ic"></span><span><b>It selects a capability, not code.</b>The engine
          exposes an API for what a device can do. Intelligence picks the right capability and
          supplies its parameters.</span></li>
          <li><span class="ic"></span><span><b>The engine executes it.</b>Sealed, versioned,
          guardrailed. Knowledge is what ships &mdash; small and portable.</span></li>
        </ul>
        <p class="verdict pos"><b>The result:</b> no script authored, no payload bloat, nothing
        probing in the background &mdash; and a fix that arrives the moment the symptom does.</p>
      </div>
    </div>

    <div style="margin-top:32px">
      <a class="btn btn-line" href="/why-nanoheal/why-not-scripts/">The full technical case &mdash;
      why not scripts</a>
    </div>
  </div>
</section>

<section class="band bone2">
  <div class="wrap">
    <div class="head">
      <p class="label">The framework</p>
      <h2 class="h2">AIM-X. One loop, and the whole point is that it doesn't stop.</h2>
      <p class="lede">Automate with Intelligence. Manage the eXperience. Every outcome becomes
      intelligence; every insight creates the next opportunity for autonomy.</p>
    </div>
    """ + nextcards([
      ("A", "Automate", "/platform/automate/",
       "Resolution without a script, delivered three ways."),
      ("I", "Intelligence", "/platform/intelligence/",
       "The semantic context layer that decides what a symptom means here."),
      ("M", "Manage &amp; evolve", "/platform/manage/",
       "How coverage compounds instead of stalling at the top call drivers."),
    ]) + """
    <div style="margin-top:22px">
      <a class="btn btn-line" href="/platform/">See the whole AIM-X loop</a>
    </div>
  </div>
</section>

<section class="band" id="value">
  <div class="wrap">
    <div class="head">
      <p class="label">Proven in production</p>
      <h2 class="h2">Most platforms start empty. Nanoheal starts with 1,200+.</h2>
      <p class="lede">Pre-built remediations, IT tasks and compliance configurations ship on day
      one, and your own team extends them in plain language.</p>
    </div>
    <p class="label" style="margin-top:44px">Fortune 100 manufacturer</p>
    <div class="stats">
      <div class="st"><div class="v">~200K</div><div class="l">endpoints under management</div></div>
      <div class="st"><div class="v">150+</div><div class="l">automations live</div></div>
      <div class="st"><div class="v">17%</div><div class="l">of tickets autohealed &mdash; nobody involved</div></div>
      <div class="st"><div class="v">35%</div><div class="l">overall ticket avoidance</div></div>
    </div>
    <p class="label" style="margin-top:32px">Worth &mdash; per 10,000 employees per year</p>
    <div class="stats">
      <div class="st hi"><div class="v">$1.0M</div><div class="l">service-desk cost avoided</div></div>
      <div class="st hi"><div class="v">$8.6M</div><div class="l">productivity recovered, on a 10-point DEX gain</div></div>
      <div class="st"><div class="v">0</div><div class="l">scripts written, deployed or maintained</div></div>
      <div class="st"><div class="v">0</div><div class="l">background probes running to detect symptoms</div></div>
    </div>
    <p class="fine">Illustrative model. Cost avoided: 35% overall ticket avoidance on 1.0
    ticket/employee/month at $25 blended cost (HDI / MetricNet range). Productivity: industry
    research indicates a 10-point DEX Score gain returns approximately 22 minutes per employee
    per week, valued at $45/hour fully loaded. DEX Score methodology patented &mdash; US 9,477,573.</p>
  </div>
</section>

<section class="band bone2" id="markets">
  <div class="wrap">
    <div class="head">
      <p class="label">Who runs on Nanoheal</p>
      <h2 class="h2">Same engine, whether you run 500 endpoints or 200,000.</h2>
    </div>
    <div class="g3">
      <div class="tile"><h3>Enterprise IT.</h3><p>Fortune 1000 estates across manufacturing,
      technology services and SaaS &mdash; typically replacing a DEX tool that measures well and
      acts poorly.</p></div>
      <div class="tile"><h3>Global system integrators.</h3><p>Delivered inside an existing managed
      workplace service. Your contract, your client, your delivery model &mdash; with an autonomy
      layer your competitors cannot price.</p></div>
      <div class="tile"><h3>OEMs, support channels and SMB.</h3><p>Multi-tenant from the ground up,
      so the same automation library serves a support channel's whole book of business.</p></div>
    </div>
    <div class="chips">
      <span class="chip">Windows</span><span class="chip">macOS</span><span class="chip">Linux</span>
      <span class="chip">VDI</span><span class="chip">iOS</span><span class="chip">Android</span>
      <span class="chip">IoT</span><span class="chip">Cloud</span><span class="chip">On-prem</span>
      <span class="chip">Airgapped</span><span class="chip">Multi-tenant or dedicated</span>
    </div>
  </div>
</section>

<section class="band" id="partners">
  <div class="wrap split">
    <div class="head">
      <p class="label">For service providers</p>
      <h2 class="h2">You already run the digital workplace. We make it autonomous.</h2>
      <p class="lede">Delivered inside your existing service &mdash; your contract, your client,
      your delivery model.</p>
    </div>
    <div>
      <div class="linkrow"><b>A differentiated bid</b><span>An autonomy commitment your competitors cannot price.</span></div>
      <div class="linkrow"><b>Margin, kept</b><span>Deflection comes from resolution, not from thinning the support team.</span></div>
      <div class="linkrow"><b>A contractable outcome</b><span>Patented DEX measurement makes the improvement provable.</span></div>
      <div class="linkrow"><b>Day-one content</b><span>1,200+ configurations your engineers extend in plain language.</span></div>
    </div>
  </div>
</section>
""" + CTA}

# ── /platform/ ───────────────────────────────────────────────────────────────
PAGES["/platform/"] = {
 "title": "The AIM-X Platform — Nanoheal",
 "desc": "Automate with Intelligence. Manage the eXperience. One closed loop where every "
         "outcome becomes intelligence and every insight creates the next automation.",
 "body": phero(
   '<a href="/">Home</a> &nbsp;/&nbsp; Platform',
   "The framework",
   "One loop, and the whole point is that it doesn&rsquo;t stop.",
   "Most platforms are a catalogue of modules you assemble yourself. AIM-X is a cycle: the fix "
   "runs, the outcome is measured, the measurement reveals the next gap, and that becomes new "
   "capability. Intelligence sits at the centre of all four.") + """

<section class="band">
  <div class="wrap">""" + AIMX_DIAGRAM + """</div>
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
      ("&rarr;", "Why not scripts", "/why-nanoheal/why-not-scripts/",
       "The technical case, in full."),
      ("&rarr;", "Runs everywhere", "/#markets",
       "Windows, macOS, Linux, VDI, mobile, IoT. Cloud, on-prem or airgapped."),
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
   "That cost is why automation coverage stops at the top call drivers everywhere else.") + """

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
        <p class="n">03 &mdash; Delivery</p>
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
        <p class="n">04 &mdash; Day one</p>
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
   "The signal is identical. The right action is not.") + """

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
        <p class="n">02 &mdash; What it decides</p>
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
        <p class="n">03 &mdash; Where it acts</p>
        <h3>The endpoint is one destination, not the only one.</h3>
        <p class="lead">Reasoning across the estate is only useful if it can act across the estate.</p>
        <div class="g3" style="margin-top:26px">
          <div class="tile"><h3>Device.</h3><p>Endpoint actions and remediation through the engine's capability API.</p></div>
          <div class="tile"><h3>ITSM.</h3><p>Creates and updates tickets and changes, and closes them when the fix lands.</p></div>
          <div class="tile"><h3>IT &amp; workplace platforms.</h3><p>Patches, software, configuration, directory, collaboration, identity, network.</p></div>
        </div>
      </div>

      <div class="issue">
        <p class="n">04 &mdash; What governs it</p>
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
      ("&rarr;", "For service providers", "/#partners", "Contracting on an outcome."),
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
