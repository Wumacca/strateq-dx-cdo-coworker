# Hopper Portfolio Readiness Review Model

## Status

Governing model for the Hopper Portfolio Readiness Review. This file is the single source of the full review workflow. Other files hold short routing pointers only and must not duplicate the workflow logic in this file.

## Purpose

The Hopper Portfolio Readiness Review prepares the existing Hopper for a leadership / Digital Review Board (DRB) priority discussion.

It organises the minimum meeting information and scores for known Hopper ideas and initiatives so leadership can discuss priority for the next programme window.

The meeting surface is the **Jira Initiative View / Hopper priority view** in Jira / Jira Product Discovery — the organised Hopper / Initiative View screens. The review prepares those screens for discussion.

## What This Review Is Not

The Hopper Portfolio Readiness Review:

- does **not** create a separate DRB Priority Screen document by default
- does **not** create a separate DRB pack or leadership paper by default
- does **not** produce Pack 1, Initiation Forms, delivery plans, costings, process maps, or source-of-truth updates
- does **not** approve, defer, reject, or commit anything
- does **not** automatically update Jira, SharePoint, GitHub, Hopper records, workflows, or source-of-truth artefacts

Where the term "Priority Screen" appears in older files, it means the **Jira Initiative View / Hopper priority view** unless the Digital Lead explicitly requests a separate artefact.

A separate DRB Priority Screen document, DRB pack, or leadership paper is produced **only** when the Digital Lead explicitly requests it.

## Governance Sequence

The Hopper Portfolio Readiness Review sits here, and only here, in the lifecycle:

```text
Hopper
↓
Organise minimum meeting information and scores in the Jira Initiative View / Hopper priority view
↓
Leadership / DRB priority discussion
↓
Approved route trigger
↓
Initiation Form / Pack 1 / Implementation Route as applicable (per route)
```

The review must **not** be collapsed into any of the following:

- Hopper → Pack 1
- Hopper → Initiation Form
- Hopper → delivery planning
- Hopper → costing
- Hopper → source-of-truth update

The Hopper Portfolio Readiness Review is **pre-initiation and pre-Pack 1**. Initiation Forms, Pack 1, and Stage 1D begin only **after** leadership / DRB approval and an explicit route trigger.

## Authority and Subordination

This model operates under, and does not override:

- `CLAUDE.md`
- `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`
- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `00_system_control/04_COWORKER_HANDOVER_MODEL.md`
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/CONTROLLED_VOCABULARY.md`
- `01_governance_lifecycle/05_ROUTE_RULES.md`
- `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md`
- `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

`00_system_control/11_COWORKER_ROUTER.md` resolves jurisdiction and points to this file. Where the router and this file appear to differ on the review process, this file governs the process and the conflict must be surfaced to the Digital Lead before final output.

## Controlled Systems

Use only the approved environment:

- **Jira / Jira Product Discovery** — Hopper and work item visibility, the Jira Initiative View / Hopper priority view meeting surface
- **SharePoint** — client documents / controlled artefact storage where applicable
- **GitHub** — coworker repo / source-of-truth markdown files where applicable

Confluence is **not** part of the THREE60 / Strateq DX digital governance setup. Do not reference Confluence as a governed system, meeting surface, update target, evidence store, or controlled artefact location.

---

## Part 0 — Access Confirmation Gate

Before any substantive review, confirm access under the Claude Opus Access Confirmation Gate in `CLAUDE.md` and the pre-loop access confirmation in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

Confirm availability of, or flag as missing:

- Hopper export / screenshot / Jira Initiative View
- Digital Benchmark Assessment Report
- Digital Maturity Register snapshot
- current repo governance files from main
- initiation forms, adoption records, or prior handovers where supplied
- relevant in-flight delivery records where overlap is likely

Respond only with one of the access confirmation responses defined in `CLAUDE.md` (access confirmed / access gap / prompt sufficient). Do not start Part 1 until the Digital Lead confirms proceed. Treat uncertain access as an access gap.

---

## Part 1 — Grouping Review

### Purpose

Group existing Hopper ideas into:

- development epics
- implementation / support grouped initiatives
- standalone items
- hold items
- clarification items
- in-flight / dependency items

### Output: Grouped Initiative / Epic Table

One row per proposed group or standalone item.

| Proposed Grouped Initiative / Epic | Included Initiatives | Why grouped | Proposed Route | Proposed Treatment | Key Dependencies / Exclusions | Confidence | Digital Lead Decision |
|---|---|---|---|---|---|---|---|

The Digital Lead Decision column must be left blank or set to "To confirm".

### Grouping Logic

Group by:

- department
- workflow
- system / tool
- source-of-truth impact
- approval route
- dependency chain
- benchmark driver

### Rules

- Do not create one row per initiative unless the item should remain standalone, requires clarification, or is a dependency / overlap item.
- Do not mark anything as approved.
- Do not update Jira, SharePoint, GitHub, Hopper records, workflows, or source-of-truth records automatically.
- Do not create Pack 1 scope, process maps, cost estimates, delivery plans, DRB packs, or Initiation Forms during Part 1.

### Cross-Initiative Impact Check

Grouping in Part 1 must be supported by the Cross-Initiative Impact Check governed by `01_governance_lifecycle/01_HOPPER_CONSOLIDATION_MODEL.md`. Every new or materially changed initiative in the review is compared against systems, processes, departments, existing / approved / live-delivery initiatives, functionality, integrations, data flows, source-of-truth artefacts, shared vendors / resources, delivery timing, feature / scope overlap, and strategic / maturity / roadmap objectives. Use the approved outcomes (Absorb into existing initiative / Merge / duplicate / Controlled change to live initiative / Create dependency / Sequence separately / Retain as separate initiative / No material impact / Clarification required). Any recommendation to modify a live initiative becomes a **candidate change control**: scope must not be silently absorbed, the affected initiative and its approval basis must be identified, and the Digital Lead decides the final treatment. Cross-Initiative Impact Check outcomes and candidate change controls must be carried into the mandatory closeout.

---

## Part 2 — Minimum Hopper Information

### Purpose

Populate the minimum information required for the Jira Initiative View / Hopper priority view. No detailed scope is required at this stage.

### Minimum Fields

- Initiative / grouped initiative name
- Included items
- Department / owner function
- Route
- Business reason / why raised
- Enterprise risk / assurance driver
- Duty Holder / regulatory driver where relevant
- Operating model impact
- System / tool impact
- Indicative duration
- Duration basis
- Dependency / sequencing note
- Proposed priority
- Confidence
- Status
- Open clarification
- Digital Lead decision / note

### Indicative Duration Rule

Indicative duration means estimated delivery duration from approved initiation / funding decision to controlled go-live or implementation completion.

- It is **not** a committed delivery date.
- It is **not** a capitalisation estimate.

### Allowed Duration Bands

- 0–4 weeks
- 4–8 weeks
- 8–12 weeks
- 12–16 weeks
- 16+ weeks

---

## Part 3 — Scoring / Priority Preparation

### Purpose

Prepare the Jira Initiative View / Hopper priority view for leadership discussion.

### Scoring Axes

Use the agreed scoring axes:

- Operational Impact
- Safety
- Regulatory / Reputational
- Commercial

### Rules

- Development epics may use department charters to gather task detail and scoring input.
- Implementation and Support grouped initiatives are scored by the Digital Lead unless department input is required.
- Scores support leadership prioritisation only.
- Scores do **not** approve, commit scope, commit budget, or create delivery work.

The Hopper Portfolio Readiness priority values in `00_system_control/11_COWORKER_ROUTER.md` (P1 / P2 / P3 / Clarify / Group / Hold / Retire) remain available as proposal-stage portfolio prioritisation values. They do not replace the canonical DRB priority decisions or consolidation outcomes in `00_system_control/CONTROLLED_VOCABULARY.md`, which remain authoritative at their stages.

---

## Initiative Charter Rule

The initiative charter is a **pre-initiation input tool only**.

### Charter Purpose

- gather business reason
- gather sub-task detail
- gather deliverables / expected benefit
- gather current method
- gather priority score input from the department

### Charter Columns

| Initiative | Tasks | Task Description (sub-tasks) | Deliverables & Expected Benefit | Current Method | Priority (1–5 per legend) |
|---|---|---|---|---|---|

### Charter Rules

- One charter per development epic where needed.
- Support and Implementation grouped initiatives do not need a charter by default.
- Charters are **not** Initiation Forms.
- Charters do **not** approve anything.
- Charters do **not** commit scope.
- Charters do **not** commit budget.
- Charters feed the Jira Initiative View / Hopper priority discussion only.

---

## Route Rules

These route definitions classify the **treatment / route indication** for an item inside the Hopper Portfolio Readiness Review. They do not split or replace the active controlled route classification label `Implementation / Support Route` in `00_system_control/CONTROLLED_VOCABULARY.md`; the formal route-label split is owned by the initiation-form-route-hardening workstream and is not performed here.

### Development Epic

- Chronos Dev, Omega Dev, CRM Dev, or equivalent build on an existing THREE60-owned platform.
- Requires a department charter where detail / scoring is needed.
- After leadership / DRB approval, route to Pack 1 / Stage 1D spin-up under `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

### Grouped Initiative

- Implementation or Support item grouped for leadership review.
- Not called an epic unless it is a development route.
- Does not require a department charter by default.

### Implementation

- Tool / system exists or route is sufficiently known.
- After approval, route to Initiation Form / Implementation Route.

### Support

- Tool does not yet exist or the solution route is not selected.
- Team needs Digital support to select then implement.
- After approval, route to selection / support route, then Initiation Form when appropriate.

### In-flight item

- Already under initiation, delivery, adoption, or support control.
- Should be visible in the Hopper review but not regrouped as new backlog work unless the Digital Lead confirms.

---

## Post-DRB Route Trigger

After leadership / DRB approval, each approved initiative gets its **own** route trigger. Do not batch unrelated initiatives into one Pack 1.

| Outcome of leadership / DRB discussion | Route trigger |
|---|---|
| Development epic approved | Individual Pack 1 / Stage 1D session under `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md` |
| Implementation grouped initiative approved | Initiation Form / Implementation Route under `01_governance_lifecycle/04_INITIATION_FORM_INTAKE_MODEL.md` |
| Support grouped initiative approved | Selection / support route, then Initiation Form when ready |
| Already in-flight item | Continue under existing initiation / delivery record; handover checkpoint where responsibility moves |
| Hold / defer / reject item | Remain in Hopper with correct status |
| Clarify item | Clarification loop before any Pack 1 or Initiation Form |

Each route trigger requires explicit Digital Lead spin-up of the receiving stage. The Hopper Portfolio Readiness Review states readiness only; it does not produce next-stage checklists or plans (see `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`).

---

## Looping Compliance — Mandatory Closeout

Every Hopper Portfolio Readiness Review session is a material governed session and must close with the governed workflow-looping closeout under `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, using the field authority in `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.

### Mandatory Closeout Sections

- Session Handover Record
- Inputs Used / Evidence Base
- Delivered / Agreed Artefacts
- Decisions Made
- Cross-Initiative Impact Check outcomes / candidate change controls
- Open Items / Constraints
- Jira / Hopper Update Recommendations
- Knowledge Capture Review
- CDO QA / Self-Improvement Check
- Source-of-Truth Update Recommendations
- Controlled Update Approval Status
- Ready for Next Stage statement

The Ready for Next Stage statement reports readiness only and does not start the next stage.

### Report-Only Boundary

The CDO QA / Self-Improvement Check, Knowledge Capture Review, Jira / Hopper Update Recommendations, and Source-of-Truth Update Recommendations are **report-only recommendations**.

Claude / GPT must not automatically update files, workflows, Jira, SharePoint, GitHub, Hopper records, or source-of-truth artefacts. All controlled updates require Digital Lead approval. Present any update as:

> "Recommended update — requires Digital Lead approval."

This restates the AI permission boundary already governed by `00_system_control/OPERATING_RULES.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. It does not extend AI authority.

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
