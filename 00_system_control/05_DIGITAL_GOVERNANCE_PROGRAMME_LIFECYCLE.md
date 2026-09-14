# Digital Governance Programme Lifecycle

## Purpose

This file defines the full Strateq DX digital governance programme lifecycle, the responsible coworker at each stage, the required stage intent, the required handover points, and the repository files that should govern detailed execution.

This file is the programme-level lifecycle map.

Detailed workflow execution remains governed by the relevant stage-specific files.

## Operating Principles

The public GitHub repository is the client-agnostic method authority. Each private client repository and its `SOURCE_OF_TRUTH.md` define that client's live working records, delivery systems and manual publication destinations. Client data is prohibited from this repository.

There are exactly two client-project lifecycle coworkers — the Hopper Lifecycle Coworker and the Live Delivery Coworker. The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker, at authority to commence delivery. Adoption, benefits, source-of-truth impact, and closeout are internal Live Delivery stage transitions inside the same continuous initiative thread. DRB, source-of-truth artefact control, adoption, benefits, capitalisation, maturity review, and programme / leadership reporting are governed stages, controls, or modes, not separate coworkers. Digital Governance & Strategy is a programme governance and control function, not a client-project coworker. The client workspace model is governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`; zero-crossover control is governed by `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

An approved Initiation Form is one entry basis to Live Delivery, not the only one. An approved transition/enterprise mandate, contract/procurement approval, leadership instruction or existing-project adoption may also authorise mobilisation. `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md` governs this entry logic.

Coworkers facilitate, draft, check, route, and prepare controlled artefacts.

Coworkers do not approve initiatives, accept risk, approve cost, commit suppliers or bypass the client's approved decision / signing route.

The principal coworker handover (Hopper Lifecycle → Live Delivery) requires a handover checkpoint under `00_system_control/04_COWORKER_HANDOVER_MODEL.md`. Internal stage transitions within a coworker's ownership are recorded in the Initiative Evidence and Decision File and do not require a coworker handover.

Every material governed session at any stage must run under the Governed Workflow Looping Standard in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` and, interactively, under the Interactive Governed Session Protocol in `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`. Stage closeout hands over only what the closing stage agreed, delivered, approved, evidenced, and left open; next-stage checklists and plans are produced only at spin-up after the Digital Lead explicitly triggers the next stage.

## Human Operating View and Controlled Process View

This lifecycle map is the **controlled process view**. The four-stage macro model — (1) Request to Hopper, (2) Hopper to Go / No-Go Decision, (3) Initiative Delivery / Live Implementation Control, (4) Completion and Handover — is the **human operating view**, described for the Digital Lead in the human-facing manual `06_operating_manual/01_DIGITAL_TRANSFORMATION_GOVERNANCE_AND_MANAGEMENT_MANUAL.md`.

- The four-stage macro model is the human operating view and does **not** replace this detailed controlled lifecycle.
- The detailed lifecycle in the table below is the controlled process view.
- The **same initiative** moves across both views at once: the macro-stage is the plain-language position, the detailed lifecycle stage is the controlled process position.
- Client context and maturity links are **future governed layers**, referenced by the manual and by the strategic and maturity alignment fields in the Initiative Control Record schema, but not yet operationally governed.

### Supporting authority pointers

- **Human-facing manual:** `06_operating_manual/01_DIGITAL_TRANSFORMATION_GOVERNANCE_AND_MANAGEMENT_MANUAL.md` — non-authoritative human navigation of this lifecycle.
- **Initiative Control Record schema:** `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` is the reusable schema; the Initiative Evidence and Decision File is its client-copy implementation in the selected private client repository.
- **Interactive Governed Session Protocol:** `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` — the interactive gates and session-state controls applied at every material session.

## Full Programme Lifecycle

| Step | Lifecycle Stage | Responsible Coworker | Stage Intent | Primary Controlled Systems / Artefacts | Required Handover |
|---:|---|---|---|---|---|
| 1 | Digital Governance & Strategy | Digital Governance & Strategy (control function) | Maintain the governance environment that creates, assesses, prioritises, funds, reports, and controls digital change. | Digital strategy, governance model, DRB model, capitalisation artefacts, benchmark assessments, maturity register, programme reports, SharePoint artefact library. | No client-project coworker handover; a confirmed candidate enters the Hopper Lifecycle Coworker directly. |
| 2 | Assessment / Benchmark / Maturity Review | Digital Governance & Strategy (control function) | Identify gaps, risks, improvement areas, digital maturity needs, or organisational requirements that may create candidate initiatives. | Benchmark assessment, digital maturity assessment, assessment evidence, maturity register, recommendation log. | No client-project coworker handover; a candidate enters the Hopper Lifecycle Coworker directly. |
| 3 | Candidate Initiative Creation | Hopper Lifecycle Coworker | Convert a governance, strategy, assessment, operational, client, or department need into a candidate Hopper item. | Jira candidate item, source evidence, SharePoint reference artefacts. | No coworker handover; the candidate is owned by the Hopper Lifecycle Coworker from intake. |
| 4 | Existing Hopper / Intake Consolidation | Hopper Lifecycle Coworker | Consolidate existing candidate initiatives and remove duplicates, BAU items, merged items, or unclear entries. | Jira Hopper, exported Jira fields, department notes, initiative list. | Internal Hopper continuity note if items move to scoping. |
| 5 | Light-Touch Department Scoping | Hopper Lifecycle Coworker | Clarify enough context to understand the need, source, likely value, and whether the item deserves DRB prioritisation discussion. | Jira fields, clarification notes, department/champion evidence. | Internal Hopper continuity note if item moves to Priority Screen. |
| 6 | Hopper Priority Screen / Hopper Portfolio Readiness Review | Hopper Lifecycle Coworker | Prepare candidate initiatives for leadership / DRB prioritisation across the next programme window by organising the Jira Initiative View / Hopper priority view. This is the default meeting surface; no separate DRB Priority Screen document is produced by default. Governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. Pre-initiation and pre-Pack 1. | Jira Initiative View / Hopper priority view, Jira fields, scoring notes, department charter input, department summary. | Internal Hopper continuity note into leadership / DRB priority discussion. |
| 7 | DRB Priority Discussion | Hopper Lifecycle Coworker + DRB | Decide whether an item is approved for Stage 1D or Stage 1, requires clarification, is deferred, rejected, BAU, or merged. | DRB notes, Jira status, decision record. | DRB decision checkpoint required before Stage 1D or Stage 1. |
| 7A | Route Classification | Hopper Lifecycle Coworker | Classify the initiative as Development Route or Implementation / Support Route from the Jira Initiative Type field or screenshot before launching Stage 1D or Stage 1. | Initiative Type field, Jira screenshot. | Route confirmed before session opens. |
| 7B | Stage 1D: Development Route Hopper Clarification / DRB Approval to Commence Development Job | Hopper Lifecycle Coworker | Clarify the internal development initiative enough for DRB to approve commencement of the live development job. Stage 2 exception gate must be tested before final pack production. | Jira field values, Completed Initiation Form (Development Approval) per `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`, Scope Brief, swimlane specification and source-of-truth handover note where applicable, single-sheet Process Flow Capture Sheet if required; optional DRB meeting-support text only on explicit request. | Stage 1D closeout / Live Delivery handover required if no Stage 2 exception. Stage 1D to Stage 2 if exception gate triggered. |
| 8 | Stage 1: Hopper Clarification / DRB Approval to Commence Initiation (Implementation / Support Route) | Hopper Lifecycle Coworker | Clarify the Hopper item enough for DRB to decide whether formal digital initiation should commence. Applies to Implementation / Support Route. | Jira field values, Completed Initiation Form per `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`, process mapping required decision, process mapping capture sheet if required; optional DRB meeting-support text only on explicit request. | Stage 1 closeout / Stage 2 readiness checkpoint required. |
| 9 | Process Mapping Capture | Hopper Lifecycle Coworker | Capture current and required process logic when process mapping is required. This is a capture sheet, not a final process flow. | Excel process mapping capture sheet, department notes, RACI, bottlenecks, future-state needs. | Feeds Stage 2. |
| 10 | Stage 2: Digital Initiation / DRB Approval to Commence Job | Hopper Lifecycle Coworker | Build the formal initiation pack required for DRB to approve the initiative to become a live job. Applies to Implementation / Support Route, and to Development Route where Stage 2 exception gate is triggered. | Requirements list, vendor/developer review, process-flow specification, source-of-truth impact report, initiation approval summary, Jira update text. | Hopper-to-Live Delivery handover required at Stage 2 closeout. |
| 11 | Authority to Commence / Live Delivery Handover | Hopper Lifecycle Coworker → Live Delivery Coworker | Establish the evidenced authority to mobilise. This may be an approved Initiation Form or an approved alternative mandate. | Approval/mandate evidence, scope, handover, known gaps. | Principal handover to Live Delivery required where a Hopper stage exists; inherited projects record an exception entry. |
| 12 | Mobilising / Initiative Delivery Setup | Live Delivery Coworker | Inspect the handover, resolve entry basis, delivery model, ownership, PEP/control structure, evidence and reporting. | `Initiative Delivery Setup`, PEP, Initiative Evidence and Decision File, source index. | Digital Lead approval required for `Mobilising → In Delivery`. |
| 13 | Leadership / Formal Sign-Off | Hopper Lifecycle Coworker (governance / capitalisation mode) + decision body + leadership | Obtain higher-level approval where required by cost, risk, contract, capitalisation or leadership threshold. | Approval pack, leadership approval, capitalisation record. | Leadership decision checkpoint required. |
| 14 | In Delivery | Live Delivery Coworker | Move the initiative into controlled execution after setup approval. | Client PEP/control plan, detailed-owner interface, RAID, decisions, changes, evidence and reporting cadence. | Live delivery operating checkpoint required. |
| 15 | Live Delivery Control | Live Delivery Coworker | Track delivery, vendor/developer progress, scope, dependencies, risks, decisions, readiness and evidence. | PEP, Artefact 1 Rev1, controls, delivery artefacts and implementation evidence. | Internal transition into go-live and adoption/handover. |
| 16 | Go-Live / Deployment | Live Delivery Coworker (go-live stage) | Confirm the solution is live, users are identified, support route exists, and adoption period can start. | Go-live record, user list, support model, training evidence, operational readiness. | Internal Live Delivery stage transition into adoption; recorded in the Initiative Evidence and Decision File. |
| 17 | Adoption / Handover and Benefits | Live Delivery Coworker | Confirm controlled use, competence, ownership, support, benefits evidence and closeout readiness. | Adoption/handover evidence, 30-day review where applicable, support ownership, closeout record. | Digital Lead-approved internal transition toward closure. |
| 18 | Source-of-Truth Impact and Closure | Live Delivery Coworker | Reconcile affected artefacts, residual obligations, lessons, publication/write-back status and closure evidence. | Private client repository, configured external publication records, process/register updates, lessons and final report. | Digital Lead closure decision or new Hopper candidate. |
| 19 | Closed | Live Delivery Coworker | Preserve the final governed record and prevent uncontrolled further updates. | Closed initiative record, final evidence, publication register and archive reference. | No further lifecycle handover. |

## Capex Request Session (Cross-Cutting Portfolio Mode)

The Capex Request Session is a portfolio-level Hopper Portfolio Readiness mode used to prepare a programme-level capitalisation request, covering previous capex closeout, the next capex portfolio request, an evidence-safe Board narrative, a client-review Board-draft deck, and a controlled Hopper-to-Delivery handover. It is governed by `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md` and owned by the Hopper Lifecycle Coworker.

It sits across:

- Digital Governance & Strategy (capitalisation artefacts, programme reporting)
- Hopper Portfolio Readiness (Step 6, `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`)
- DRB / leadership approval (Step 7, DRB Priority Discussion)
- handover to Live Delivery (via the Hopper → Live Delivery Handover Checklist)

The Capex Request Session is not a replacement for single-initiative route controls. Approval of a capex request approves the funding envelope / programme intent only; each initiative still requires its own route trigger, route classification, and Completed Initiation Form or Stage 1D pack where applicable before delivery mobilisation.

## Coworker Responsibilities

### Digital Governance & Strategy (control function)

A programme governance and control function, not a client-project coworker. It concerns the pre-Hopper and programme governance environment; its initiative-creating outputs enter the Hopper Lifecycle Coworker directly, and its cross-initiative governance is handled through the reporting modes and the Digital Lead's governance authority.

Concerns:

- digital strategy
- digital governance model
- DRB operating model
- capitalisation request and approval artefacts
- benchmark assessments
- digital maturity assessments
- maturity register
- programme reporting
- SharePoint artefact library and structure
- organisational interface model
- programme-level source-of-truth registers
- lessons learned and governance improvements
- creation of candidate initiatives from governance, assessment, strategy, or organisational signals

A confirmed candidate initiative enters the Hopper Lifecycle Coworker directly; no separate governance-to-Hopper coworker handover is required.

### Hopper Lifecycle Coworker

Owns the route from candidate Hopper item through approval to become a live job.

Responsible for:

- Hopper intake and consolidation
- light-touch department scoping
- Hopper Priority Screen preparation
- DRB priority discussion support
- route classification (Development Route or Implementation / Support Route)
- Stage 1D Development Route Hopper Clarification / DRB Approval to Commence Development Job
- Stage 1D Scope Brief and Process Flow Capture Sheet
- Stage 1D pack gate and Stage 2 exception gate
- Stage 1D closeout and handover to Live Delivery (Development Route, no Stage 2 exception)
- Stage 1 Hopper Clarification / DRB Approval to Commence Initiation (Implementation / Support Route)
- process mapping capture sheet issue when required
- Stage 2 Digital Initiation / DRB Approval to Commence Job
- requirements list preparation
- vendor/developer review support
- initiation approval pack preparation
- source-of-truth impact reporting for Stage 2
- Jira update text (Stage 2 and where explicitly requested)
- handover to Live Delivery

Detailed Hopper Lifecycle execution is governed by:

- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`
- `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`
- `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`
- `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`
- `04_intake_dispatch/01_AUTOMATIC_HOPPER_CLARIFICATION_HANDLER.md`
- `04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md`
- `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`
- `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md`
- `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`
- any newer synced repository file that supersedes or extends these workflows

### Live Delivery Coworker

Owns the same initiative after approval to commence (Stage 1D / Stage 2 / form approval), through delivery, adoption, benefits, source-of-truth impact, and closeout — all inside the same continuous initiative thread.

Responsible for:

- evidence-led mobilisation and `Initiative Delivery Setup`
- PEP/client-control structure
- developer/vendor coordination
- delivery risk and issue tracking
- delivery status reporting (weekly delivery-control touchpoints)
- implementation evidence
- scope control
- delivery closeout readiness
- adoption and benefits stages (below)
- source-of-truth control mode (below)

#### Adoption and benefits (internal Live Delivery stage)

Post-go-live control handled inside the same initiative thread as an internal stage transition, not a coworker handover:

- adoption readiness
- 30-day review
- usage evidence
- competence readiness
- benefits evidence
- support and ownership confirmation
- closeout preparation

#### Source-of-truth artefact control (governed mode)

A governed control mode applied within the initiative thread when lifecycle changes affect a controlled artefact, governed by `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. It is not a separate coworker. It concerns:

- controlled artefact register
- process flow register
- software ecosystem register
- integration register
- maturity register
- benchmark archive
- decision records
- superseded / active artefact control
- lessons learned
- programme reporting updates
- surfacing new issues to the Digital Governance & Strategy control function or the Hopper Lifecycle Coworker where required

## Hopper Lifecycle Reference Point

The Hopper Lifecycle Coworker must not operate from project instructions alone.

When handling Hopper, Stage 1D, Stage 1, Stage 2, process mapping, DRB brief preparation, Jira field updates, source-of-truth impact checks, or handover to Live Delivery, it loads the governing files for that stage using the deterministic map in `CLAUDE.md` (B2).

The Development Route Stage 1D model is the primary authority for Development Route initiatives.

The two-stage initiation model is the primary authority for Stage 1 and Stage 2 (Implementation / Support Route, and Development Route Stage 2 exceptions).

The coworker handover model is the primary authority for transitions between coworkers.

The artefact governance model and client isolation standard are the primary authorities for method/client/source-of-truth boundaries.

## Mandatory Handover Points

The only mandatory client-project coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker, at approval to commence delivery. It takes one of two route-specific forms:

1. Hopper Lifecycle Stage 1D closeout to Live Delivery (Development Route, no Stage 2 exception)
2. Hopper Lifecycle Stage 2 closeout to Live Delivery (Implementation / Support Route, and Development Route where the Stage 2 exception is triggered)

The following are internal stage transitions or closeouts within a single coworker's ownership, recorded in the Initiative Evidence and Decision File, and are **not** coworker handovers:

- Hopper Lifecycle Stage 1D to Stage 2 (Development Route, Stage 2 exception triggered)
- Hopper Lifecycle Stage 1 closeout to Stage 2 readiness (Implementation / Support Route)
- Live Delivery go-live to adoption and benefits
- Live Delivery adoption/benefits to source-of-truth impact and closeout

Programme strategy, governance, reporting, maturity, capitalisation, or source-of-truth artefact updates are handled through the reporting modes and the Digital Lead's governance authority, not through a coworker handover.

Handover format is governed by:

`00_system_control/04_COWORKER_HANDOVER_MODEL.md`

## File Discovery Rule

This lifecycle map is not an exhaustive list of every file in the repository.

For every task, the coworker loads the governing files for the identified stage using the deterministic stage-to-file map in `CLAUDE.md` (B2). This is a lookup, not a per-task relevance judgement. Any newer or more specific file synced after B2 was written is loaded in addition under `CLAUDE.md` (B3), and the coworker flags that B2 needs amendment; the coworker adds, it never subtracts.

If a task-specific file exists, that task-specific file takes precedence over a general lifecycle summary.

Conflicts are resolved by the precedence order in `CLAUDE.md` (B4). Where a conflict cannot be resolved by that order, or the stage or a required file cannot be identified, the coworker stops and asks the Digital Lead under `CLAUDE.md` (B5) before any output.

## Output Boundary

The programme lifecycle map defines where the work sits.

The relevant stage file defines what must be produced.

The coworker must not produce artefacts outside the active lifecycle stage unless the Digital Lead explicitly instructs it to do so.
