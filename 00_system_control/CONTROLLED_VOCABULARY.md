# Controlled Vocabulary

## Purpose

This file defines the canonical vocabulary for the governed lifecycle from Hopper through live delivery and closeout.

Every approved AI Coworker must use these exact labels when drafting governed records, client-system update text, and optional DRB meeting-support text where explicitly requested by the Digital Lead. `DRB Brief` is not a default or final Hopper review artefact.

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

The Coworker must not invent numeric scores, weightings, or a 1–5 scale. Where a Digital Lead-approved scoring model, team-returned charter score, or client-system-entered score exists, the Coworker may organise, display, summarise, and challenge the score, but must not create or alter scores without Digital Lead approval.

Scored fields in future request-intake models do not authorise Claude to create scores. Current Hopper review scoring may use Digital Lead-approved, team-returned, or Jira-entered scores only.

## Approved Hopper Statuses

Use these method labels unless the bound client profile provides the actual controlled-system status names:

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

The Digital Lead confirms before any controlled status change, item removal, or merge action.

## Approved Stage 1D Status

Use this current workflow label for Development Route Stage 1D work:

- Stage 1D In Progress

## Approved Route Labels

Use these exact labels when classifying initiative route:

- Development Route
- Implementation Route
- Support Route
- TBC

"Hybrid route" is not an approved route label and must not be used as an active route classification.

> **Route-vocabulary split — complete.** The former combined route label has been retired. `Implementation Route` and `Support Route` are separate controlled labels, and the closeout behaviour in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` is authoritative.

## Stage 3 Live Delivery Labels

Use these lifecycle labels:

- Authorised
- Mobilising
- In Delivery
- Adoption / Handover
- Operational / Live
- Paused (On Hold)
- Closed / Retired

Use these entry-basis labels:

- Digital Initiation Form
- Transition / Enterprise Mandate
- Contract / Procurement Approval
- Leadership Instruction
- Existing Live Project Adoption
- Exception — Authority Not Evidenced
- TBC

`No Digital Initiation Form` does not mean `No authority to proceed`. Where no approved authority is evidenced, setup may remain draft but the initiative must not move to `In Delivery`.

Use these delivery-model labels:

- Development-led Delivery
- Digital-led Implementation / Support
- Vendor-led Implementation with Digital Client-side Assurance
- TBC

Capex, Opex and transition / programme funding are funding classifications, not delivery models.

Use these Digital financial-reporting-basis labels:

- Full Cost Tracking
- Summary Supplied by Budget Owner
- Approved Variations Only
- Emerging Cost Impacts / Exceptions Only
- No Financial Reporting by Digital
- TBC

The following ownership fields must be resolved independently: Detailed Plan Owner; Client Control Plan Owner; Budget / Cost Owner; Operational Acceptance Owner; Go-live Approval Authority; Reporting Owner.

- **Initiative Delivery Setup** — the controlled mobilisation record that establishes entry basis, authority, scope, delivery model, ownership, governance, PEP/control structure, evidence requirements and readiness. This exact title replaces earlier extended titles.
- **PEP / client-control plan** — the bound client's authoritative view of client-side milestones, obligations, interfaces, acceptance gates and required evidence where the client profile selects it. It does not duplicate a supplier's detailed plan.
- **Detailed owner plan** — the developer-, Digital- or supplier-owned execution detail. For vendor-led delivery, supplier detail remains with the supplier while the client-control plan governs the client interface and acceptance.
- **Mobilisation handover reference** — the one-time reference from the first Artefact 1 record after approval of `Mobilising` to `In Delivery` back to the approved Initiative Delivery Setup.
- **Digital Programme Workbook** — the governed human-facing programme/portfolio interface and working snapshot governed by `02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md`, covering contract-level and initiative-level management, lifecycle/current-step visibility, delivery milestones and open/overdue actions. It is an interface and snapshot, not a controlled record: an uploaded workbook is a supplied snapshot subject to the confirmation-first status rule, and it never replaces the Initiative Evidence and Decision File, PEP/control record, approved action system, formal approval records, evidence registers or source-of-truth artefact governance. The single canonical blank, client-agnostic template is `02_coworker_artifact_interface/blank_templates/Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx`.
- **Workbook difference classification** — the controlled set used when reconciling an uploaded Digital Programme Workbook against the controlled records: `Unchanged`, `Proposed update`, `New record`, `Missing record`, `Conflict`, `Stale value`, `Unresolved identity`. Differences are surfaced for Digital Lead decision and never silently applied.

## Hopper Portfolio Readiness Review Terminology

The full Hopper Portfolio Readiness Review workflow is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. Use these defined terms:

- **Hopper Portfolio Readiness Review** — the pre-initiation, pre-Pack 1 review that organises minimum meeting information and scores so the Hopper is ready for a leadership / DRB priority discussion.
- **Jira Initiative View / Hopper priority view** — the organised Hopper / Initiative View screens in Jira / Jira Product Discovery. This is the **default meeting surface** for the leadership / DRB priority discussion. The term "Priority Screen" means this view unless the Digital Lead explicitly requests a separate artefact. A separate DRB Priority Screen document is **not** produced by default.
- **Development Epic** — a build or enhancement on an existing client-owned platform. May use a department charter for detail / scoring. After approval, routes to Pack 1 / Stage 1D.
- **Grouped Initiative** — an implementation or support item grouped for leadership review. Not called an epic unless it is a development route. No charter by default.
- **Initiative Charter** — a pre-initiation input tool only. Gathers business reason, sub-task detail, deliverables / expected benefit, current method, and department priority score input. A charter is **not** an Initiation Form and does not approve or commit anything.
- **Implementation Route** (Hopper-review treatment term) — the tool / system exists or the route is sufficiently known; after approval, routes to Initiation Form / Implementation Route.
- **Support Route** (Hopper-review treatment term) — the tool does not yet exist or the solution route is not selected; the team needs Digital support to select then implement.
- **In-flight item** — an item already under initiation, delivery, adoption, or support control. Visible in the Hopper review but not regrouped as new backlog work unless the Digital Lead confirms.
- **Controlled update recommendation** — a proposed change to a governed record that requires Digital Lead approval before it is applied.
- **Report-only recommendation** — an advisory output (CDO QA / self-improvement, knowledge capture, controlled-system update, source-of-truth update) that must not automatically change any controlled record.

> **Hopper-review treatment terms now match the controlled labels.** "Implementation Route" and "Support Route" above were previously Hopper-review treatment / route-indication terms held distinct from the (then-combined) controlled route classification label. Following the route-vocabulary split, these terms are now the same active controlled route classification labels used in the Approved Route Labels section above.

## Formal Approval Artefact Terminology

The formal approval-artefact naming rules are governed by `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`. Use these defined terms:

- **Completed Initiation Form** — the formal DRB-facing approval document, for both the Development Route (Stage 1D / Pack 1, Development Approval) and the Implementation Route / Support Route (two-stage initiation). This is the only name for the formal approval artefact. Do not use "DRB Brief" as the name of a final pack deliverable or formal approval artefact.
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

## Client Coworker and Workspace Terminology

The client workspace, coworker, thread and reporting model is governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. Use these defined terms.

- **Hopper Lifecycle Coworker** — the first of the two client-project lifecycle coworkers. Owns each initiative from origin and intake through Hopper consolidation, clarification, prioritisation, route determination, initiation (Stage 1D or two-stage initiation), DRB preparation, decision capture, and approval to commence delivery.
- **Live Delivery Coworker** — the second of the two client-project lifecycle coworkers. Owns the same initiative after approval through mobilisation, delivery, implementation, delivery health and scope control, evidence, acceptance, handover, adoption, benefits checks where applicable, source-of-truth impact, and closeout.
- **Client-project lifecycle coworkers** — there are exactly two: Hopper Lifecycle Coworker and Live Delivery Coworker. The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker. No other client-project coworker exists.
- **Lifecycle stage** — a controlled step within a coworker's ownership (for example Hopper consolidation, Stage 1D, delivery, closeout). A stage is not a coworker and does not require its own thread.
- **Governed mode / control** — a governed activity applied within the initiative or reporting threads (DRB, source-of-truth artefact control, adoption, benefits review, capitalisation, maturity review, programme reporting, leadership reporting, closeout). A mode is not a client-project coworker and does not require its own thread.
- **Digital Governance & Strategy** — a programme governance and control function, not a client-project coworker, client-project thread, additional lifecycle owner, or mandatory coworker handover. Its functions are handled through the Hopper Lifecycle Coworker (initiative governance), the reporting modes (cross-initiative governance), and the Digital Lead's governance authority.
- **Client binding** — the fail-closed act of resolving exactly one client ID, one private client repository, one allowed method repository and the permitted external destinations before any client source is read or written.
- **Method repository** — the public, client-agnostic Strateq DX authority. It is read-only during client work and must contain no client facts, evidence or artefacts.
- **Client working authority** — the one private repository named in the bound client's profile. It contains client context, live records, evidence indexes, PEP/control records and released artefacts.
- **Initiative thread** — one continuous AI-workspace thread per initiative, renamed according to the bound client's naming convention. A thread is an interface and continuity aid; it is never the controlled record.
- **Reporting thread** — one bi-weekly programme-reporting thread and one monthly leadership-reporting thread, named according to the bound client profile. No parallel reporting ledger or additional programme-status thread is created.
- **Initiative Evidence and Decision File** — the single AI-readable per-initiative continuity record, the client-copy implementation of the `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` schema, governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` and templated at `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`. It records the latest Digital Lead-confirmed position and required write-backs. It is not a duplicate execution backlog, action register, programme-memory file or automatically the external organisational record.
- **Permitted connection** — a repository, file source or system explicitly allowlisted by the bound client profile. The Coworker must not infer access from technical availability.
- **Manual external publication** — an approved artefact is released in the private client repository, then uploaded by an authorised user to the external client store. The Coworker records the publication only after the user confirms it occurred.
- **Confirmation-first status rule** — at the start of every material initiative or reporting session, after access is established and before the supplied status is used, the Coworker presents the latest available position it holds, identifies the source and date of that position, and asks: «Is this still accurate? Please confirm or provide any changes since the last recorded update.» Prior chat, project knowledge, assistant memory, an earlier report, an older export, an initiative evidence file, a previously approved historical artefact, or a prior status snapshot is not current without Digital Lead confirmation.
- **Pending confirmation** — the status applied to any position that has not been confirmed as current by the Digital Lead. When used, state which output, decision, report, or control move is affected.
- **Physical client-system write-back** — a required update to a client system outside the private working repository. Only the Digital Lead or an authorised user performs it unless the client profile explicitly authorises a governed integration. The Coworker prepares the text and labels it `Recommended update — requires Digital Lead approval and physical update in the client system.`
- **Update-once rule** — a confirmed update received in any initiative, bi-weekly, or monthly session must first be reconciled into the affected Initiative Evidence and Decision File and PEP/control record before a report is generated. No material fact may remain only in chat, project knowledge, assistant memory or a report.
- **Client action-management system** — the action system, if any, named in the bound client profile. The Coworker must not assume a specific product globally.
- **Weekly delivery-control touchpoint** — an internal delivery-control / operational delivery cadence term. It does not create a weekly programme report, a weekly reporting thread, an additional programme-status record, or an additional coworker. The only formal reporting cycles are bi-weekly programme reporting and monthly leadership reporting.

## Reusable Artefact Registry Terminology

The reusable-artefact registry and revision handshake are governed by `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md`. Use these defined terms.

- **Method Artefact Registry** — the authoritative list in `16` of reusable Strateq DX artefacts (templates, schemas, interfaces, workbooks), each with an Artefact ID, canonical path, interface/specification path, current approved revision, approving method commit, status, superseded revisions, compatibility notes and whether client adoption requires an explicit baseline update.
- **Artefact ID** — the stable, unique identifier for a reusable artefact (for example `ART-PROGRAMME-WORKBOOK`). It does not change across revisions.
- **Approved revision** — the `Current approved revision` (`r<N>`) of an artefact recorded in the registry at the approved method commit. "Latest" always means the latest approved revision, never an unpinned branch tip or an uploaded file.
- **Approving method commit** — the commit on the method repository default branch at which an artefact revision was approved.
- **Revision handshake** — the deterministic resolution in `16` performed before any generated refresh or populated artefact: bind one client → read the client `METHOD_BASELINE.md` → read the registry → resolve the canonical artefact at the approved method commit → confirm revision and interface/specification version match, approved and not superseded → record the resolved ID/revision/commit → fail closed on a stale, missing, ambiguous or incompatible baseline.
- **Client baseline pin** — the per-artefact revision a client has adopted, recorded in that client's `METHOD_BASELINE.md`. It changes only through a Digital-Lead-approved baseline update, never automatically by the Coworker.
- **Populated output** — the client-specific artefact produced from a resolved reusable artefact. It is client data, stored only in the bound client repository; it is never written back into the method repository, and it is not a duplicate of the reusable blank template.

## Interactive Governed Session Terminology

The interactive session model is governed by `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`, the reusable initiative schema by `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`, and the freshness and maturity-impact vocabulary by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. Use these defined terms. They do not conflict with, and do not replace, the existing controlled vocabulary above.

- **Interactive Governed Session** — a material governed coworker session run under the mandatory interactive sequence in `12`: Runtime Access Confirmation Gate → Client Context Gate → Confirmation-First Status Gate → Initiative Reconciliation Gate → Required Inputs Gate → Live Session Status Board → stage work → governance / evidence test → human decision → controlled update recommendations → closeout / suspension / handover → Digital Lead actions required.
- **Runtime Access Confirmation Gate** — the in-session gate at which the coworker states which current repository authority files and which supplied exports, snapshots, and evidence records it can and cannot access, whether the prompt alone is sufficient, and whether synced knowledge may be stale. It confirms access only; it does not decide that a business position is current — that is settled at the Confirmation-First Status Gate. It is not the build-time repository access check performed by an engineering tool.
- **Client Context Gate** — the gate that verifies the client binding and reads the applicable controlled client profile, source-of-truth map, method baseline and initiative home. It must not be satisfied from memory, synced knowledge or chat history.
- **Initiative Reconciliation Gate** — the gate at which the Coworker reconciles the requested initiative and unresolved obligations against the bound client's source hierarchy: current Initiative Evidence and Decision File and PEP/control record → current permitted system export or snapshot → other supplied controlled record → access gap. The reconciled position is not current until the confirmation-first status rule is satisfied.
- **Required Inputs Gate** — the gate producing one consolidated, batched input table (statuses: Present / Missing / Stale / Pending confirmation / Accepted gap / Not applicable) before any substantive stage output is treated as controlled-ready.
- **Live Session Status Board** — the visible session board created at spin-up and refreshed on every material exchange (item statuses: Not started / In progress / Awaiting Digital Lead / Awaiting external input / Pending evidence / Complete / Accepted gap / Not applicable).
- **Digital Lead actions required** — the standing action block (Action / Owner / Required by or trigger / Consequence if not completed) that ends every substantive governed-session response. Where none applies, state `No Digital Lead action required at this point.`
- **Initiative Control Record** — the reusable schema (`13`) for initiative control fields. The client profile selects its live implementation. The public method repository holds the schema only; the private client working authority may hold the live record where selected.
- **Session state** — the controlled state of a governed session: Not started / Active / Suspended — awaiting evidence / Pending Digital Lead decision / Pending external approval / Ready for closeout / Closed and handed over. "Open chat thread" is not a governance status.
- **Suspended — awaiting evidence** — a controlled session state in which the session is paused pending evidence; it remains visible at future Initiative Reconciliation Gates and does not automatically block unrelated work.
- **Accepted gap** — a missing input, context, reconciliation, or evidence item that the Digital Lead has explicitly accepted so the session may proceed, recorded with the affected outputs, required artefact, owner, and review point.
- **Initiative Reconciliation waiver** — an explicit, risk-bounded Digital Lead waiver of the Initiative Reconciliation Gate when no valid reconciliation source is available, recorded as `Accepted gap — Initiative Reconciliation not completed.` A waived session cannot claim full reconciliation.
- **Cross-Initiative Impact Check** — the mandatory check at Hopper intake and material change that compares a new or materially changed initiative against systems, processes, departments, existing / approved / live initiatives, functionality, integrations, data flows, source-of-truth artefacts, shared vendors / resources, delivery timing, feature / scope overlap, and strategic / maturity / roadmap objectives. Outcomes: Absorb into existing initiative / Merge / duplicate / Controlled change to live initiative / Create dependency / Sequence separately / Retain as separate initiative / No material impact / Clarification required.
- **Candidate change control** — a recommendation to modify a live initiative arising from the Cross-Initiative Impact Check or a scope change. Scope must not be silently absorbed into a live initiative; the Digital Lead decides the final treatment. The coworker may recommend but cannot change scope or route.
- **Freshness status** — the event / cadence-based status of an information item: Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable. There is no universal arbitrary staleness period; freshness rules are event / cadence based per `07`.
- **Revalidation due** — a freshness status indicating that a cadence or event (for example a fortnightly delivery cycle or a material change) requires the item to be revalidated before it is relied on.
- **Controlled write-back** — the proposed controlled update produced at closeout covering lifecycle position, gate status, decision outcome, evidence, actions, accepted gaps, linked artefacts, the Initiative Evidence and Decision File and PEP/control updates, and any external physical write-backs. No material governed session is closed until it has been proposed and the Digital Lead has approved, deferred or accepted the gap.
- **Expected maturity impact** — the intended capability improvement identified during Hopper, initiation or approval.
- **Provisional maturity impact** — an evidence-led maturity movement proposed at delivery closeout from delivered capability, acceptance, go-live and ownership evidence; not yet a confirmed live update where adoption or embedded-use evidence is required.
- **Pending adoption evidence** — delivery evidence exists but operational use, ownership, adoption or benefit evidence remains outstanding.
- **Confirmed maturity impact** — question-level and roadmap-track maturity movement approved after the required adoption, benefits and evidence review.
- **Rejected — insufficient evidence** — a proposed maturity movement not supported by sufficient evidence.

> These maturity-impact terms are schema and boundary vocabulary only. The coworker does not calculate maturity scores or update any live maturity position in the current workstream; the Maturity Improvement Loop model is a future placeholder.

## Stage Closeout Naming

Stage closeout lines and stage naming must be route-correct and derived from this vocabulary and `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`. Do not invent generic "Stage 1 / Stage 2" wording. The canonical closeout paths and lines are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. For a Development Route initiative with no Stage 2 exception, the closeout line is: `Stage 1D is closed. Ready for Live Delivery spin-up.`
