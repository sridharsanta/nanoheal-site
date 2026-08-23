# Nanoheal — Positioning, Messaging & Site Map

## 1. Competitive read

| | What they're genuinely good at | Where they're weak |
|---|---|---|
| **Nexthink** — "Deliver the digital workplace of the AI era" | Broadest DEX analytics; strong brand; now pushing "autonomous IT agents" | Remediation is still authored logic; campaigns and remote actions need building and maintaining |
| **ControlUp** — "The AI Platform for IT Operations" | Real-time VDI/EUC telemetry; strong ops heritage; "Pulse AI" | Automation is script-and-trigger; deep configuration effort before value |
| **Lakeside** — "The DEX Engineering Platform" | Deepest sensor data and forensics; explicitly positions as *observability* | Openly an analytics/observability play — action is left to other tools |

**The shared shape of the category:** they measure well and act poorly. Three structural weaknesses to attack, none of which requires naming them:

1. **Probe configuration is heavy.** Getting a useful dashboard live takes weeks of sensor/probe definition and tuning.
2. **Automation is script-based.** PowerShell/Bash authored per issue, pushed to the fleet, bloating the payload, breaking on estate drift.
3. **Symptom triggering is expensive or absent.** To fire on a symptom, a script must stay resident and poll — CPU, memory and battery on machines that are mostly fine. So in practice automation is scheduled or manual, not symptom-driven.

## 2. Positioning statement

> For enterprise IT and digital workplace leaders who have already made the workplace measurable, **Nanoheal is the autonomy layer** that resolves issues at the moment the operating system reports them. Unlike DEX platforms whose automation is scripted, deployed and continuously polled, Nanoheal ships **knowledge, not code** — the OS's own signal is the trigger, and a governed capability engine performs the fix. That changes the economics of automation, so coverage compounds past the top call drivers instead of stalling there.

**Category we claim: Digital Experience Automation (DXA)** — the evolution of DEX, not a replacement for it.

> **DEX made the workplace visible. DXA makes it actionable.**
>
> Nanoheal is the AI-driven Digital Experience Automation platform that turns DEX insight into
> autonomous action — from the device to the entire IT ecosystem.

The site must make the visitor think *DEX → DXA* (Digital Experience Management → Digital
Experience Automation), **not** *DEX platform → automation platform*. That distinction is the
whole positioning: DXA is not merely automation, it is automation driven by DEX intelligence and
context. Claiming both halves credibly is what beats "we do DEX" as table stakes.

| DEX — understand the experience | DXA — act on the experience |
|---|---|
| Measure · Forecast · Detect · Diagnose · Prove | Understand · Resolve · Automate · Orchestrate · Improve |

The two halves are joined by the **Intelligence / semantic context layer**, which is what makes
the action safe and specific to *this* estate. **AIM-X** (Automate with Intelligence, Manage the
eXperience) is the internal framework underneath — revealed on `/platform/`, never used as the
first thing a visitor has to learn.

## 3. The message hierarchy

**Level 1 — the wedge (hero).** "We see it coming. Then we fix it without a script."

> **Corrected framing.** The earlier hero ("DEX made the workplace measurable, Nanoheal makes it
> autonomous") conceded the measuring half to competitors and positioned Nanoheal as a bolt-on to
> a DEX tool. Nanoheal has analytics parity *plus* forecasting and anomaly detection, so the hero
> must claim both halves. The wedge still leads — breadth defends, the differentiator wins — with
> a parity table immediately below so scope is never a disqualifier.

**Level 2 — the mechanism (the section that must convert).** *Scripts have to go looking for a problem. Nanoheal is told.*

| Script-based | Nanoheal |
|---|---|
| Engineer authors a script per symptom | The OS emits the symptom — event log, service failure, crash, user-facing error |
| Payload pushed to every endpoint; bloats over time | Nothing shipped but knowledge — kilobytes |
| Must stay resident and poll to detect | Zero probing; detection already happened, for free |
| Breaks on patch / policy / OS drift | Engine owns *how*; knowledge owns *what* — survives drift |
| Cost paid twice: build it, then run it forever | Fix arrives the moment the symptom does |

**Level 3 — why it's possible.** The engine exposes device operations as a governed capability API (files, registry, services and processes, config and policy, software and patch, network, identity, plus ITSM and IT-management orchestration). Intelligence doesn't generate code — it works out which capabilities a situation needs and **authors the knowledge entry** for it, which a human validates once. Small, sealed, versioned, guardrailed.

**Level 3b — scope.** The same engine and the same knowledge layer run three classes of work: *resolve* (remediation), *run* (software distribution, patch, IT tasks) and *enforce* (device compliance policy). And the context layer spans the IT ecosystem — ServiceNow, Active Directory, anything with a standard API, integrated by description rather than by code. Competitors need a separate product, or a separate integration project, for each of these.

**Level 4 — proof and economics.** 1,200+ configurations on day one · patented DEX score (US 9,477,573) · Fortune 100 manufacturer, ~200K endpoints, 150+ automations, 17% autohealed, 35% overall ticket avoidance · $1.0M cost avoided + $8.6M productivity per 10,000 employees/year (illustrative model) · Gartner, ISG Rising Star, Forrester DEX Landscape Q2 2026.

**Level 5 — compounding.** Create once, run every time (autoheal / self-service / assisted), grow continuously. The long tail finally gets built because the next automation costs almost nothing.

### Phrases to own
- "Knowledge, not code."
- "The symptom is the trigger."
- "Nothing left running to watch."
- "Solve an issue once and it is solved forever."
- "Most platforms start empty. Nanoheal starts with 1,200+."
- "DEX became a dashboard. The tickets kept coming."

### Retire from the old site
"Future of work is AI and Automation", "Experience Automated", "Do more with less", "One Platform, Limitless Possibilities" — generic, indistinguishable from the category. Keep the Automate / Innovate / Manage / Deliver Experience spine, but re-cut it as **AIM-X**.

## 4. Site map

Built and live in this repo are marked **●**; the rest is the planned IA.

The underlying mental model the IA has to communicate:

```
                         NANOHEAL
                            │
                  DIGITAL EXPERIENCE
                     AUTOMATION (DXA)
                            │
        ┌───────────────────┼───────────────────┐
       DEX             INTELLIGENCE          ACTION
   Measure              Context              Resolve
   Forecast             Reason               Automate
   Detect               Understand           Orchestrate
   Score                                     Improve
        └───────────────────┼───────────────────┘
                            │
                    IT ECOSYSTEM
             Device · ITSM · IT Ops
             Workplace · Human agent
```

```
● Home                              DEX → DXA, the gap, the loop, then routes inward

  Category pillars
  ● /digital-experience/            the DEX half — measure, forecast, detect, diagnose, prove
  ● /digital-experience-automation/ the DXA half — insight → context → action → outcome
  ● /why-nanoheal/why-dxa/          why DEX alone isn't enough; why scripted automation stalls

  Platform
  ● /platform/                      DXA platform overview — measure, understand, act, improve
                                    (AIM-X revealed here as the framework underneath)
  ● /platform/observe-predict/      analytics parity, forecasting, anomaly detection, root cause
  ● /platform/intelligence/         I — the context layer that AUTHORS the knowledge entry
  ● /platform/automate/             A — resolve / run / enforce, on one capability engine
  ● /platform/it-operations/        software distribution, patch, device compliance policy
  ● /platform/orchestration/        ServiceNow, AD, any standard API — integrated without code
  ● /platform/workflows/            plain-language authoring; symptom / forecast / request / schedule triggers
  ● /platform/manage/               M — where autonomy goes next
  ● /platform/deliverexperience/    X — the patented DEX score
  ● /platform/innovate/             301 → /platform/intelligence/ (legacy URL)
    /platform/knowledge-library/    the 1,200+ configurations, and how they grow
    /platform/coverage/             OS, VDI, mobile, IoT; cloud / on-prem / airgapped

  Why Nanoheal
  ● /why-nanoheal/why-dxa/          why DEX alone isn't enough — the category argument
  ● /why-nanoheal/why-not-scripts/  the technical case, in full
    /why-nanoheal/created-once/     created once, reused everywhere (currently on the DXA page)
    /why-nanoheal/ecosystem/        ecosystem automation (currently on /platform/orchestration/)
    /why-nanoheal/time-to-value/    day one → first weeks → every quarter
    /why-nanoheal/compare/          named comparison vs Nexthink / ControlUp / Lakeside
    /why-nanoheal/analysts/         Gartner, ISG, Forrester

  Solutions — by outcome
    /solutions/ticket-deflection/   /autoheal/  /self-service/
    /solutions/policy-compliance/   /it-task-automation/  /dex-programme/
  Solutions — by segment
    /solutions/enterprise/          Fortune 1000: manufacturing, tech services, SaaS
    /solutions/service-providers/   global SIs and MSPs — the autonomy layer
    /solutions/oem-channel/         OEMs and support channels, multi-tenant
    /solutions/smb/
  Solutions — by role
    /solutions/cio/  /digital-workplace/  /end-user-services/  /service-desk/

  Resources
    /resources/customer-stories/    /business-case/  /whitepapers/  /blog/
    docs.nanoheal.com               product documentation · learning portal

  Company
    /partners/  /aboutus/  /careers/  /contact/  /trust/
```

**Primary nav (built):** Platform (dropdown) · Digital Experience · Automation ·
Why Nanoheal (dropdown) · Solutions · Outcomes + *Schedule a Demo*.

`Digital Experience` and `Automation` sit in the top nav as peers deliberately: that is what
teaches the DEX/DXA split to a visitor who never reads a word of body copy. A `Resources`
section is in the planned IA but is not built — there is no content behind it yet.

### Why this IA, and how it differs from the competition

Nexthink, ControlUp and Lakeside all organise Platform as a **catalogue of modules** —
"Workplace Experience", "ControlUp for Desktops", "Help Desk". That structure describes
what the vendor built, and it invites a feature-by-feature comparison Nanoheal will not
always win on breadth of analytics.

This IA organises Platform as a **loop of problems solved**. Each pillar page opens with
the issue as the buyer experiences it, then shows the mechanism. It is a harder structure
to comparison-shop against, and it puts the differentiator — cost of the next automation —
on every page rather than only on the homepage.

One number worth keeping visible: Lakeside publishes 1,300+ sensors and 220+ automations.
Sensors measure; configurations act. Nanoheal's 1,200+ configurations against 220 is the
single cleanest quantitative contrast available, and it is used on /platform/automate/.

## 5. Homepage section order (built)

The homepage teaches the category first, then routes inward. The narrative is a single
argument — *visible → not resolved → here is the mechanism → here is its scope* — and each
section hands off to a pillar page rather than trying to finish the story itself.

| # | Section | Anchor | Job |
|---|---|---|---|
| 1 | Hero — **DEX made the workplace visible. DXA makes it actionable.** | `#hero` | Name the category in the first three seconds; live symptom→resolution console as proof |
| 2 | Analyst proof strip | `#proof` | Credibility before the argument starts |
| 3 | **Knowing was solved. Doing wasn't.** | `#gap` | The gap, stated fairly — DEX gets full credit for the half it solved |
| 4 | **This is Digital Experience Automation.** | `#framework` | The reveal. Measure → Understand → Act → Improve, tagged DEX / Intelligence / DXA / Outcome |
| 5 | **Everything DEX does. Then the part that closes the loop.** | `#scope` | Parity table so scope is never a disqualifier → both pillar pages |
| 6 | **DXA doesn't stop at the device.** | `#ecosystem` | Device → ITSM → IT management → workplace → human agent |
| 7 | Most platforms start empty. Nanoheal starts with 1,200+ | `#value` | Time to value; who runs on Nanoheal |
| 8 | One engine, different value — internal IT / service providers | `#solutions` | Buyer self-selection |
| 9 | See a symptom resolve itself | `#demo` | CTA |

Section 4 is the page's centre of gravity: the layer tags on the pipeline (DEX, Intelligence,
DXA, Outcome) are what make the hierarchy legible without a paragraph of explanation.

Removed from the homepage and relocated: the script-vs-symptom comparison
(→ /why-nanoheal/why-not-scripts/ and /why-nanoheal/why-dxa/), the ROI stat grids
(→ /outcomes/, not yet built), the capability API grid (→ /platform/automate/), the AIM-X
loop diagram (→ /platform/), and the path-to-value timeline
(→ /why-nanoheal/time-to-value/, not yet built).

## 6. What is not built yet

The category repositioning is complete across the pages that exist. Still open from the
planned IA, in rough priority order:

1. `/outcomes/` — the ROI and production-proof numbers pulled off the homepage need a home.
2. `/solutions/internal-it/` and `/solutions/service-providers/` — currently a single
   homepage section (`#solutions`); the nav points there rather than to real pages.
3. `/resources/` — no content behind it, so it is deliberately absent from the nav.
4. The DEX sub-pages (employee / device / application experience) and the DXA sub-pages
   (autoheal, self-service, assisted IT, automation library) — the pillar pages currently
   carry that material in summary form.
