# Governed Workflow Looping Standard

## Status

Status: Submitted for CDO governance review as part of PR #3.

Governed Workflow Looping is adopted as a **governance accelerator, not an automation shortcut**.

## Purpose

This file defines the operating discipline for every material governed coworker session.

It extends the existing authority files. It does not replace or duplicate them.

- `00_system_control/04_COWORKER_HANDOVER_MODEL.md` remains authoritative for handover field content and handover paths.
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` remains authoritative for knowledge capture and source-of-truth update routing.
- This file (`07`) defines the governed workflow loop, the material session threshold, the proportionality rule, the stage segregation rule, the route-aware closeout rule, the AI permission boundary reminder, the advisory-only QA rule, and the Digital Lead approval gate.

This file does not restate the full contents of `04` or `06`. Where handover fields or knowledge routing are required, apply `04` and `06` directly.

## The Governed Workflow Loop

Every material governed coworker session must operate as:

```text
Input
→ AI-assisted draft / check
→ governance test
→ human decision
→ controlled update
→ evidence retained
→ stage closeout / handover
```

Knowledge capture, CDO QA / self-improvement review, and source-of-truth update recommendations are **components of the stage closeout / handover step**, not separate workflows.

### Pre-Loop Access Confirmation for Claude Opus

Before the loop begins, any Claude Opus-governed review or session must confirm access to the required files or confirm that the prompt itself contains sufficient information. If access is not confirmed, the loop must not proceed. Missing files, missing exports, missing source records, or unclear authority must be reported as access gaps.

This prevents substantive analysis being generated from incomplete context and preserves Digital Lead control over whether the session should proceed.

## AI Permission Boundary Reminder

This reminder restates the operating boundary already governed by `00_system_control/OPERATING_RULES.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. It does not extend AI authority.

AI may:

- draft
- challenge
- compare
- summarise
- identify control gaps
- recommend updates
- produce handover artefacts
- produce knowledge capture items
- produce source-of-truth update recommendations

AI must not:

- approve
- overwrite governed records
- reclassify the final route without Digital Lead approval
- change approved scope
- mutate source-of-truth files without an approved repository change
- update Jira directly unless explicitly authorised
- update SharePoint directly unless explicitly authorised
- start the next stage before the Digital Lead spins it up

## Controlled Systems

The controlled systems for this workflow are:

- Jira
- SharePoint
- GitHub
- Blueworks / Nitro where applicable
- approved source-of-truth documents

Confluence is **not** part of the THREE60 DX governance setup. Do not reference Confluence as a governed system, update target, evidence store, or controlled artefact location.

## Material Session Threshold

A material governed session is any coworker session that involves one or more of the following:

- Hopper Portfolio Readiness Review (governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`; every such session must close with the full looping closeout)
- route decision
- initiation form preparation or approval
- DRB approval
- stage closeout or handover
- live delivery transition
- approved scope, cost, duration, risk, or delivery commitment
- source-of-truth artefact impact
- process artefact creation or controlled process update
- adoption / benefits realisation / closure, when that lifecycle stage is reached
- audit, regulator, Duty Holder, client, or assurance-facing evidence

KPI governance is **excluded** from the Governed Workflow Looping update in this pass. KPI governance must not be referenced as a governed trigger until the KPI governance model is formally defined in its own authority file.

## Proportionality Rule

Closeout effort must be proportionate to the session.

### Full closeout applies to

- initiation approval
- stage closeout
- live delivery handover
- source-of-truth impacting sessions
- process artefact creation or controlled process update
- post-go-live / adoption closure, when that lifecycle stage is reached
- audit, regulator, Duty Holder, client, or assurance-facing evidence

Full closeout uses the **Stage Closeout Handover output model** below and must include, where material: the handover (`04`), Knowledge Capture Review (`06`), the CDO QA / Self-Improvement Check (advisory only), and Source-of-Truth Update Recommendations (advisory only).

### Lightweight closeout applies to

- BAU support
- minor clarification
- routine drafting
- non-governed admin
- exploratory discussion with no decision, approval, route, record, or source-of-truth impact

Lightweight closeout may include only:

- short decision / output summary
- open items
- recommended next action
- any source-of-truth recommendation if identified

## Stage Segregation Rule

Stage Closeout is an **extension of the `04` handover checkpoint, not a replacement**.

Each stage must close by handing over only what that stage agreed, delivered, approved, evidenced, and left open.

The stage closeout **must not include**:

- next-stage checklist
- next-stage delivery plan
- next-stage implementation activities
- next-stage testing plan
- next-stage acceptance plan
- next-stage work breakdown
- instructions that belong to the receiving coworker, except references to existing artefacts and a readiness statement

The stage closeout **may include only**:

- what was agreed in the closing stage
- what was delivered in the closing stage
- what artefacts were produced
- what approvals were received
- what Jira / SharePoint / process artefact references exist
- what open items remain from the closing stage
- what known constraints must be handed over
- what source-of-truth records are impacted
- what knowledge should be captured
- whether the stage is ready for the next stage to be spun up

### Starter-Checklist Timing Rule

Next-stage starter checklists, delivery plans, testing plans, acceptance plans, work breakdowns, and implementation plans are produced **only at spin-up**, by the receiving coworker / stage, **after the Digital Lead explicitly triggers that spin-up**.

A closing stage may state readiness only.

## Digital Lead Approval Gate

The loop does not self-complete. The Digital Lead is the decision and approval authority at every controlled update and at every stage transition.

- AI proposes; the Digital Lead decides.
- No controlled update (repository, Jira, SharePoint, process artefact, source-of-truth) is applied without Digital Lead approval.
- The next stage is not started until the Digital Lead explicitly spins it up.

## Advisory-Only QA Rule

> CDO QA / Self-Improvement findings are recommendations only. They do not update the workflow, source-of-truth, Jira, SharePoint, or repository files unless the Digital Lead approves a controlled update.

No rule in this repository permits Claude or any AI coworker to automatically update workflow files, source-of-truth artefacts, Jira, SharePoint, or repository files from QA / self-improvement findings.

## Route-Aware Closeout Rule

The closeout line and stage naming must be derived from the confirmed route and the controlled vocabulary. Do not invent generic "Stage 1 / Stage 2" wording.

Use the route-correct lifecycle name from:

- `00_system_control/CONTROLLED_VOCABULARY.md`
- `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`
- route-specific authority files

### Canonical closeout paths

**Development Route**

- Stage 1D → Live Delivery
- Closeout line: `Stage 1D is closed. Ready for Live Delivery spin-up.`
- (Stage 1D only progresses to Stage 2 where a Stage 2 exception gate trigger is confirmed under `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.)

**Implementation Route**

- Stage 1 → Stage 2: `Stage 1 is closed. Ready for Stage 2 spin-up.`
- Stage 2 → Live Delivery: `Stage 2 is closed. Ready for Live Delivery spin-up.`

**Support Route**

- Support Route uses lightweight closeout by default and does **not** emit a stage-spin-up readiness line unless the item is converted into the Development Route or Implementation Route.
- On conversion, it inherits the receiving route's canonical lifecycle path and closeout wording.
- Support Route must not force BAU or minor support into full initiation governance.

> **Route-vocabulary dependency.** The controlled route-vocabulary split into separate `Implementation Route` and `Support Route` labels is owned by the initiation-form-route-hardening workstream and is **not** to be performed in this looping standard. On main, the controlled label currently appears as the combined `Implementation / Support Route` (see `00_system_control/CONTROLLED_VOCABULARY.md`). Until the split lands, the Implementation Route and Support Route closeout behaviour above is provisional and must be reconciled against the controlled vocabulary when the route-hardening workstream completes. This standard does not redefine the route model.

## Stage Closeout Handover Output Model

Use the existing `04` handover checkpoint as the field authority. Include the following sections where material.

### 1. Stage Closeout Status

- initiative
- route
- stage being closed
- approval / decision status
- final stage outcome
- next stage readiness statement

### 2. Delivered / Agreed in This Stage

- agreed scope
- agreed exclusions
- agreed route
- agreed duration / estimate
- agreed approval artefact
- agreed supporting artefacts
- agreed dependencies

### 3. Evidence and Traceability

- Jira references
- approval records
- initiation form reference
- process flow reference
- scope / deliverables brief reference
- source-of-truth artefact references
- milestone-to-Jira traceability where applicable

### 4. Open Items / Constraints for Handover

- only unresolved items from the closing stage
- no next-stage planning detail

### 5. Source-of-Truth Artefact Impact

- records impacted
- whether handover to the Source-of-Truth Artefact Controller is required
- references / links to artefacts the next stage will need
- do not describe how to inspect, plan, sequence, test, or deliver them

Apply the Artefact Impact Check format in `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.

### 6. Knowledge Capture Review

Use the knowledge capture authority in `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.

Use table:

| Knowledge item | Proposed target location | Action required | Owner | Status | Source-of-truth impact (Y/N) |
|---|---|---|---|---|---|

### 7. CDO QA / Self-Improvement Check

Use table:

| What worked | What nearly caused ambiguity or scope drift | What governance rule prevented error | What instruction was missing or weak | What should be added or corrected in source-of-truth | Repo update recommended? | Confidence level |
|---|---|---|---|---|---|---|

> CDO QA / Self-Improvement findings are recommendations only. They do not update the workflow, source-of-truth, Jira, SharePoint, or repository files unless the Digital Lead approves a controlled update.

### 8. Closeout Statement

Use:

`[Route-correct stage name] is closed. Ready for [route-correct next stage] spin-up.`

For Development Route with no Stage 2 exception:

`Stage 1D is closed. Ready for Live Delivery spin-up.`

## Source-of-Truth Update Recommendations

Every material governed session must end with Source-of-Truth Update Recommendations, routed under `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.

These are advisory recommendations for Digital Lead action. They do not authorise Claude to update controlled records.

## Interactive Governed Session Protocol Integration

Every material governed session runs interactively under `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`. That protocol wraps the governed workflow loop in a fixed interactive sequence and is mandatory integration, not a separate workflow. This file (`07`) remains authoritative for the loop, proportionality, stage segregation, route-aware closeout, and the Digital Lead approval gate; `12` is authoritative for how those are surfaced interactively.

Mandatory integration points from `12`:

- **Client Context Gate** — proportionate confirmation of the controlled client-context source; never reconstructed from memory, synced knowledge, or chat history.
- **Initiative Reconciliation Gate** — reconcile the initiative and unresolved obligations against a physical read-source hierarchy (live Jira → Jira export → interim register → access gap); waiver is explicit and risk-bounded.
- **Required Inputs Gate** — one consolidated, batched input table before substantive stage output.
- **Live Session Status Board** — created at spin-up and refreshed on every material exchange.
- **Digital Lead actions required** — a standing action block that ends every substantive governed-session response.
- **Controlled session states** — Not started / Active / Suspended — awaiting evidence / Pending Digital Lead decision / Pending external approval / Ready for closeout / Closed and handed over. "Open chat thread" is not a governance status. A suspended session remains visible at future Initiative Reconciliation Gates and does not automatically block unrelated work.
- **Closeout write-back** — no material governed session is closed until a controlled write-back has been proposed (labelled `Recommended update — requires Digital Lead approval.`) and the Digital Lead has approved it, explicitly deferred it, or accepted the remaining gap.

The initiative fields reconciled, updated and handed over are governed by the reusable `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`. GitHub holds the schema only; Jira is the target-state live Initiative Control Record; SharePoint / the controlled client workspace holds approved artefacts and evidence. No permanent live per-initiative ledger is permitted in the GitHub repository.

## Freshness and Evidence Model

Freshness is **event / cadence based**. There is no universal "stale after N days" rule.

| Information category | Freshness rule |
|---|---|
| Live delivery status | Revalidated each fortnightly delivery cycle or material event |
| Delivery RAID | Reviewed each delivery cycle |
| Owner / champion | Confirmed at stage spin-up and when responsibility changes |
| DRB / approval decision | Valid once formally recorded unless superseded |
| Scope / exclusions | Valid until approved change control |
| Cost / vendor quote | Valid until quote expiry, commercial change or revalidation event |
| Schedule / milestones | Revalidated each delivery cycle |
| UAT / acceptance evidence | Valid against approved test scope unless scope changes |
| Benefits evidence | Revalidated at adoption / benefits gates |
| Source-of-truth impact | Rechecked at material change, go-live and closeout |
| Initiative relationships / dependencies | Rechecked at Hopper intake and material change |
| Client strategy / maturity context | Rechecked at the proportionate Client Context Gate |

Approved freshness statuses:

- Current
- Revalidation due
- Stale
- Superseded
- Pending confirmation
- Not applicable

A stale item must identify: the reason it is stale; the output or decision blocked; the owner; the evidence required; the next review point.

## Maturity-Impact Vocabulary and Boundary

These controlled maturity-impact statuses are used by the strategic and maturity alignment fields in `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`. This workstream provides the vocabulary and boundary only; it does not build the Maturity Improvement Loop model, does not calculate maturity scores, and does not update any live maturity position.

Controlled maturity-impact statuses:

- No maturity impact identified
- Expected maturity impact
- Provisional maturity impact
- Pending adoption evidence
- Confirmed maturity impact
- Rejected — insufficient evidence

Definitions:

- **Expected maturity impact** — the intended capability improvement identified during Hopper, initiation or approval.
- **Provisional maturity impact** — an evidence-led movement proposed at delivery closeout based on delivered capability, acceptance, go-live and ownership evidence. It is not yet a confirmed update to the live maturity position where adoption or embedded-use evidence is required.
- **Pending adoption evidence** — delivery evidence exists, but operational use, ownership, adoption or benefit evidence remains outstanding.
- **Confirmed maturity impact** — question-level and roadmap-track movement approved after the required adoption, benefits and evidence review.
- **Rejected — insufficient evidence** — the proposed movement is not supported by sufficient evidence.

Boundary rules:

> Delivery closeout may propose a provisional maturity impact based on delivered capability, acceptance, go-live and ownership evidence. The live maturity position must not be changed solely because delivery is complete where adoption or embedded-use evidence is required.

> The Adoption and Benefits stage confirms, revises or rejects the proposed maturity movement using evidence of operational use, ownership, adoption, benefit and sustained capability.

> Any approved live maturity-register update remains subject to the Source-of-Truth Artefact Controller and Digital Lead or authorised reviewer approval.

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
