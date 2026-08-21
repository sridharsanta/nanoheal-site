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

**Category we claim:** DEX is the measurement half; Nanoheal is *Digital Experience Automation* — the improving half. Framed by **AIM-X**: Automate with Intelligence, Manage the eXperience.

## 3. The message hierarchy

**Level 1 — the wedge (hero).** Seeing the problem is the easy half. Nanoheal ends it. No scripts to write; nothing left running to watch.

**Level 2 — the mechanism (the section that must convert).** *Scripts have to go looking for a problem. Nanoheal is told.*

| Script-based | Nanoheal |
|---|---|
| Engineer authors a script per symptom | The OS emits the symptom — event log, service failure, crash, user-facing error |
| Payload pushed to every endpoint; bloats over time | Nothing shipped but knowledge — kilobytes |
| Must stay resident and poll to detect | Zero probing; detection already happened, for free |
| Breaks on patch / policy / OS drift | Engine owns *how*; knowledge owns *what* — survives drift |
| Cost paid twice: build it, then run it forever | Fix arrives the moment the symptom does |

**Level 3 — why it's possible.** The engine exposes device operations as a governed capability API (files, registry, services and processes, config and policy, software and patch, network, identity, plus ITSM and IT-management orchestration). The intelligence doesn't generate code — it *selects a capability and supplies its parameters* from the knowledge base. Small, sealed, versioned, guardrailed.

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

```
● Home                              the USP only: symptom-vs-script, proof, routes inward

  Platform
  ● /platform/                      AIM-X overview — the closed loop, Intelligence at the hub
  ● /platform/automate/             A — "Remediation is a software project. It shouldn't be."
  ● /platform/intelligence/         I — "Telemetry says what happened, not what you do about it."
  ● /platform/manage/               M — "Coverage stalls at the top call drivers. It doesn't have to."
  ● /platform/deliverexperience/    X — "Improvement gets asserted. Yours will be scored."
  ● /platform/innovate/             301 → /platform/intelligence/ (legacy URL)
    /platform/knowledge-library/    the 1,200+ configurations, and how they grow
    /platform/coverage/             OS, VDI, mobile, IoT; cloud / on-prem / airgapped
    /platform/integrations/         ITSM, CMDB, identity, IT management, collaboration

  Why Nanoheal
  ● /why-nanoheal/why-not-scripts/  the technical case, in full
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

**Primary nav:** Platform (dropdown) · Why not scripts · Outcomes · Partners + *Schedule a Demo*.

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

The homepage no longer carries the whole story — detail moved to the inner pages, and
what remains is the differentiator plus routes inward.

1. Hero — the wedge, with a live symptom→resolution console
2. Analyst proof strip
3. **The difference** — script-based vs symptom-triggered *(the page's centre of gravity)* → /why-not-scripts/
4. AIM-X, three cards → /platform/
5. Outcomes — production proof and economics
6. Who runs on Nanoheal — enterprise / SI / OEM-channel, and platform coverage
7. For service providers
8. CTA + footer

Removed from the homepage and relocated: the capability API grid (→ /platform/automate/),
the four AIM-X panels (→ /platform/ and the four pillar pages), the path-to-value timeline
(→ /why-nanoheal/time-to-value/, not yet built), and "how the library grows"
(→ /platform/manage/).
