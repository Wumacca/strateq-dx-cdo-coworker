# Controlled Vocabulary

## Purpose

This file defines the canonical vocabulary for the current Hopper-to-Initiation workflow.

Claude must use these exact labels when drafting Hopper consolidation outputs, Priority Screens, Jira-ready text, and optional DRB meeting-support text where explicitly requested by the Digital Lead. DRB Brief is not a default or final Hopper review artefact.

## Canonical DRB Priority Decisions

Use these exact labels:

- Progress to Approved Route Trigger
- Clarify Before Progression
- Merge / Duplicate
- Defer
- Reject
- Move to BAU Support
- Hold for Future Review

**Progress to Approved Route Trigger** — approved by leadership / DRB to move to the next route-correct stage: Pack 1 / Stage 1D for Development Epics, Initiation Form / Implementation Route for Implementation items, selection/support route for Support items, or existing delivery control for in-flight items.

Do not invent variants.

## Canonical Consolidation Outcomes

Use these exact labels:

- Ready for Priority Screen
- Clarify with Department
- Merge / Duplicate
- Move to BAU Support
- Hold for Future Review
- Reject

## Business Priority Signal

Use these exact labels:

- High
- Medium
- Low
- Unclear

Each signal must include a short reason.

The signal is qualitative only.

Claude must not invent numeric scores, weightings, or a 1–5 scale. Where a Digital Lead-approved scoring model, team-returned charter score, or Jira-entered score exists, Claude may organise, display, summarise, and challenge the score, but must not create or alter scores without Digital Lead approval.

Scored fields in future request-intake models do not authorise Claude to create scores. Current Hopper review scoring may use Digital Lead-approved, team-returned, or Jira-entered scores only.

## Approved Jira Statuses: Current Workflow

Use these current workflow labels unless the Digital Lead provides the actual Jira status names:

- Hopper - Unscreened
- Hopper - Clarify
- Ready for Priority Screen
- At DRB
- Initiation Form In Progress
- BAU Support
- Deferred
- Rejected
- Merged

## Confirmation Rule

BAU, Reject, and Merge are AI recommendations only.

The Digital Lead confirms before any Jira status change, item removal, or merge action.

## Approved Jira Statuses: Stage 1D

Use this current workflow label for Development Route Stage 1D work:

- Stage 1D In Progress

## Approved Route Labels

Use these exact labels when classifying initiative route:

- Development Route
- Implementation / Support Route
- TBC

"Hybrid route" is not an approved route label and must not be used as an active route classification.

> **Route-vocabulary split dependency.** Splitting the combined `Implementation / Support Route` label into separate `Implementation Route` and `Support Route` labels is owned by the initiation-form-route-hardening workstream and is not performed here. `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` describes provisional Implementation Route and Support Route closeout behaviour that must be reconciled with these controlled labels once that split lands.

## Hopper Portfolio Readiness Review Terminology

The full Hopper Portfolio Readiness Review workflow is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. Use these defined terms:

- **Hopper Portfolio Readiness Review** — the pre-initiation, pre-Pack 1 review that organises minimum meeting information and scores so the Hopper is ready for a leadership / DRB priority discussion.
- **Jira Initiative View / Hopper priority view** — the organised Hopper / Initiative View screens in Jira / Jira Product Discovery. This is the **default meeting surface** for the leadership / DRB priority discussion. The term "Priority Screen" means this view unless the Digital Lead explicitly requests a separate artefact. A separate DRB Priority Screen document is **not** produced by default.
- **Development Epic** — a Chronos Dev, Omega Dev, CRM Dev, or equivalent build on an existing THREE60-owned platform. May use a department charter for detail / scoring. After approval, routes to Pack 1 / Stage 1D.
- **Grouped Initiative** — an implementation or support item grouped for leadership review. Not called an epic unless it is a development route. No charter by default.
- **Initiative Charter** — a pre-initiation input tool only. Gathers business reason, sub-task detail, deliverables / expected benefit, current method, and department priority score input. A charter is **not** an Initiation Form and does not approve or commit anything.
- **Implementation Route** (Hopper-review treatment term) — the tool / system exists or the route is sufficiently known; after approval, routes to Initiation Form / Implementation Route.
- **Support Route** (Hopper-review treatment term) — the tool does not yet exist or the solution route is not selected; the team needs Digital support to select then implement.
- **In-flight item** — an item already under initiation, delivery, adoption, or support control. Visible in the Hopper review but not regrouped as new backlog work unless the Digital Lead confirms.
- **Controlled update recommendation** — a proposed change to a controlled record (Jira, SharePoint, GitHub, Hopper, source-of-truth) that requires Digital Lead approval before it is applied.
- **Report-only recommendation** — an advisory output (CDO QA / self-improvement, knowledge capture, Jira / Hopper update, source-of-truth update) that must not automatically change any controlled record.

> **Hopper-review treatment vs active route classification.** "Implementation Route" and "Support Route" above are Hopper-review treatment / route-indication terms. They do **not** split or replace the active controlled route classification label `Implementation / Support Route` in the Approved Route Labels section. The formal split of that label is owned by the initiation-form-route-hardening workstream and is not performed here.

## Formal Approval Artefact Terminology

The formal approval-artefact naming rules are governed by `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`. Use these defined terms:

- **Completed Initiation Form** — the formal DRB-facing approval document, for both the Development Route (Stage 1D / Pack 1, Development Approval) and the Implementation / Support Route (two-stage initiation). This is the only name for the formal approval artefact. Do not use "DRB Brief" as the name of a final pack deliverable or formal approval artefact.
- **Optional DRB meeting-support text** — short executive decision-support / Jira-ready text produced only when the Digital Lead explicitly requests it, governed by `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`. It is not a formal approval artefact, does not replace the Completed Initiation Form, and does not replace the Jira Initiative View / Hopper priority view as the default Hopper meeting surface.
- The term **DRB** remains valid for: DRB meeting, DRB approval, DRB decision required, DRB approval status, DRB-ready pack, DRB decision text, and optional DRB meeting-support text.

## Capex Request Session Terminology

The full Capex Request Session workflow is governed by `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`. Use these defined terms:

- **Capex Request Session** — a governed Hopper Portfolio Readiness mode used to prepare a programme-level capitalisation request: previous capex closeout, next capex portfolio request, evidence-safe Board narrative, client-review Board-draft deck, and controlled Hopper-to-Delivery handover. Owned by the Hopper Lifecycle Coworker.
- **Portfolio Capex Request Pack** — the formal output artefact of a Capex Request Session. It consolidates the readiness tracker, evidence, claim safety table, and Board narrative into the capitalisation request. Do not use "Bulk Initiation Pack" as the name of this artefact; "bulk initiation" may only describe how the process operates.
- **Capex Readiness Tracker** — the working control document that tracks, per initiative and evidence requirement, what is known, what is missing, and what is an accepted Digital-Lead-confirmed gap.
- **Capital Efficiency Evidence** — the mandatory evidence section covering baseline cost, revised cost, avoided cost, recurring avoided cost where applicable, arithmetic check, evidence basis, claim status, finance validation status, and Board-safe wording for each cost-avoidance / value case.
- **Plan Attainment Evidence** — the mandatory evidence section covering committed initiatives, delivered / live / controlled / next-phase status, date movement reason, budget position, unsupported claims, and Board-safe closeout wording.
- **Claim Safety Table** — the claim-safety control table for Board-facing outputs, covering claim, evidence source, claim status, Board-safe wording, blocker / dependency, owner, and confidence basis. Confidence basis is a source-read judgement in words, never an invented numeric confidence score.
- **Client-Review Board-Draft Deck** — a Board-safe, claim-safe, decision-led draft deck produced for client / Digital Lead review, with open dependencies visible as placeholders. It is not the Board-final deck.
- **Board-Final Deck** — the final Board-facing deck issued for formal approval. It must not be produced by the Hopper Lifecycle Coworker while a Board-final blocker remains open.
- **Board-final blocker** — an open finance, maturity, or other dependency that must clear before a Board-final deck or final approval wording may be issued.
- **Mobilisation gap** — an item on the Hopper → Live Delivery Handover Checklist that is missing at handover and has been explicitly accepted by the Digital Lead rather than resolved before mobilisation.

## Interactive Governed Session Terminology

The interactive session model is governed by `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`, the reusable initiative schema by `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`, and the freshness and maturity-impact vocabulary by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. Use these defined terms. They do not conflict with, and do not replace, the existing controlled vocabulary above.

- **Interactive Governed Session** — a material governed coworker session run under the mandatory interactive sequence in `12`: Runtime Access Confirmation Gate → Client Context Gate → Initiative Reconciliation Gate → Required Inputs Gate → Live Session Status Board → stage work → governance / evidence test → human decision → controlled update recommendations → closeout / suspension / handover → Digital Lead actions required.
- **Runtime Access Confirmation Gate** — the in-session gate at which the coworker states which live repository files and client records it can and cannot access, whether the prompt alone is sufficient, whether synced knowledge may be stale, and which source is treated as current. It is not the build-time repository access check performed by an engineering tool.
- **Client Context Gate** — the proportionate gate confirming the applicable controlled client-context source (profile, benchmark, maturity register, roadmap, ecosystem, strategy, governance artefact register, or other approved client record). It must not be satisfied from memory, synced knowledge, or chat history. Its detailed model is a future placeholder.
- **Initiative Reconciliation Gate** — the gate at which the coworker reconciles the requested initiative and unresolved governance obligations against the physical read-source hierarchy (live Jira integration → current Jira export → interim client Initiative Control Register → access gap).
- **Required Inputs Gate** — the gate producing one consolidated, batched input table (statuses: Present / Missing / Stale / Pending confirmation / Accepted gap / Not applicable) before any substantive stage output is treated as controlled-ready.
- **Live Session Status Board** — the visible session board created at spin-up and refreshed on every material exchange (item statuses: Not started / In progress / Awaiting Digital Lead / Awaiting external input / Pending evidence / Complete / Accepted gap / Not applicable).
- **Digital Lead actions required** — the standing action block (Action / Owner / Required by or trigger / Consequence if not completed) that ends every substantive governed-session response. Where none applies, state `No Digital Lead action required at this point.`
- **Initiative Control Record** — the reusable schema (`13`) for initiative control fields. The target-state live record is Jira; approved artefacts and evidence are in SharePoint / the controlled client workspace; GitHub holds the schema only. No permanent live per-initiative ledger is permitted in GitHub.
- **Session state** — the controlled state of a governed session: Not started / Active / Suspended — awaiting evidence / Pending Digital Lead decision / Pending external approval / Ready for closeout / Closed and handed over. "Open chat thread" is not a governance status.
- **Suspended — awaiting evidence** — a controlled session state in which the session is paused pending evidence; it remains visible at future Initiative Reconciliation Gates and does not automatically block unrelated work.
- **Accepted gap** — a missing input, context, reconciliation, or evidence item that the Digital Lead has explicitly accepted so the session may proceed, recorded with the affected outputs, required artefact, owner, and review point.
- **Initiative Reconciliation waiver** — an explicit, risk-bounded Digital Lead waiver of the Initiative Reconciliation Gate when no valid reconciliation source is available, recorded as `Accepted gap — Initiative Reconciliation not completed.` A waived session cannot claim full reconciliation.
- **Cross-Initiative Impact Check** — the mandatory check at Hopper intake and material change that compares a new or materially changed initiative against systems, processes, departments, existing / approved / live initiatives, functionality, integrations, data flows, source-of-truth artefacts, shared vendors / resources, delivery timing, feature / scope overlap, and strategic / maturity / roadmap objectives. Outcomes: Absorb into existing initiative / Merge / duplicate / Controlled change to live initiative / Create dependency / Sequence separately / Retain as separate initiative / No material impact / Clarification required.
- **Candidate change control** — a recommendation to modify a live initiative arising from the Cross-Initiative Impact Check or a scope change. Scope must not be silently absorbed into a live initiative; the Digital Lead decides the final treatment. The coworker may recommend but cannot change scope or route.
- **Freshness status** — the event / cadence-based status of an information item: Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable. There is no universal arbitrary staleness period; freshness rules are event / cadence based per `07`.
- **Revalidation due** — a freshness status indicating that a cadence or event (for example a fortnightly delivery cycle or a material change) requires the item to be revalidated before it is relied on.
- **Controlled write-back** — the proposed controlled update produced at closeout covering the initiative's lifecycle position, gate status, decision outcome, evidence, actions, accepted gaps, linked artefacts, and required Jira / interim-register / SharePoint updates. It is a form of controlled update recommendation, labelled `Recommended update — requires Digital Lead approval.` No material governed session is closed until it has been proposed and the Digital Lead has approved, deferred, or accepted the gap.
- **Expected maturity impact** — the intended capability improvement identified during Hopper, initiation or approval.
- **Provisional maturity impact** — an evidence-led maturity movement proposed at delivery closeout from delivered capability, acceptance, go-live and ownership evidence; not yet a confirmed live update where adoption or embedded-use evidence is required.
- **Pending adoption evidence** — delivery evidence exists but operational use, ownership, adoption or benefit evidence remains outstanding.
- **Confirmed maturity impact** — question-level and roadmap-track maturity movement approved after the required adoption, benefits and evidence review.
- **Rejected — insufficient evidence** — a proposed maturity movement not supported by sufficient evidence.

> These maturity-impact terms are schema and boundary vocabulary only. The coworker does not calculate maturity scores or update any live maturity position in the current workstream; the Maturity Improvement Loop model is a future placeholder.

## Stage Closeout Naming

Stage closeout lines and stage naming must be route-correct and derived from this vocabulary and `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`. Do not invent generic "Stage 1 / Stage 2" wording. The canonical closeout paths and lines are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. For a Development Route initiative with no Stage 2 exception, the closeout line is: `Stage 1D is closed. Ready for Live Delivery spin-up.`
