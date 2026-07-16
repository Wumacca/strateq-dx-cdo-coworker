# Interactive Governed Session Protocol

## Status

Global authority for how material coworker sessions operate interactively. This file extends the existing authority files. It does not replace or duplicate them.

- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` remains authoritative for the governed workflow loop, the material session threshold, proportionality, stage segregation, route-aware closeout, and the Digital Lead approval gate.
- `00_system_control/04_COWORKER_HANDOVER_MODEL.md` remains authoritative for handover field content and handover paths.
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` remains authoritative for knowledge capture and source-of-truth update routing.
- `00_system_control/OPERATING_RULES.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` remain authoritative for the AI permission boundary and source-of-truth control.
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` is the reusable schema for the initiative fields this protocol reconciles, updates and hands over.

This file (`12`) defines the mandatory interactive session sequence, the runtime gates, the Live Session Status Board, the controlled session states, and the closeout write-back rule. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.

## Purpose

This file makes the coworker procedurally accountable, during every material governed session, for:

- recognising the requested stage / session;
- confirming access and current context;
- telling the Digital Lead what inputs are required;
- identifying what is present, missing, stale or unverified;
- maintaining visible session progress;
- identifying approvals and Digital Lead physical actions;
- preventing false stage completion;
- preparing controlled update recommendations;
- recording whether the session is active, suspended, ready for closeout or handed over.

The coworker does not replace human decision authority. It reconciles available controlled sources, facilitates the governed session, prepares recommendations and update text, maintains visible session state, and prepares closeout and handover outputs. It does not invent the live position and does not silently mutate controlled records.

### Build-time access is not this gate

This protocol governs the **runtime** behaviour of a coworker inside a governed client session. It is separate from any build-time repository access check performed by an engineering tool when the repository itself is being edited. The Runtime Access Confirmation Gate below is about the live client session, not about repository write access.

## Applicability

This protocol applies to every material governed session as defined by the material session threshold in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, including Hopper intake, Hopper Portfolio Readiness, Pack 1 / Stage 1D, Implementation / Support initiation, Completed Initiation Form preparation or approval, Capex Request Sessions, material scope or change-control sessions, delivery reviews and closeout, source-of-truth impact reviews, and any adoption / benefits or maturity session once that lifecycle stage is reached.

Lightweight, non-governed exchanges (BAU support, minor clarification, routine drafting, exploratory discussion with no decision, approval, route, record or source-of-truth impact) use the lightweight closeout in `07` and are not required to run the full sequence. The gate depth must be proportionate to the session (see Client Context Gate proportionality below).

## Mandatory Session Sequence

Every material governed session must follow this sequence. A material session must not jump directly to final output before the required gates have been addressed.

1. **Runtime Access Confirmation Gate**
2. **Client Context Gate**
3. **Confirmation-First Status Gate** (present the latest held position; obtain Digital Lead confirmation or correction)
4. **Initiative Reconciliation Gate**
5. **Required Inputs Gate**
6. **Live Session Status Board**
7. **Stage-specific work** (governed by the relevant route / stage authority file)
8. **Governance and evidence test**
9. **Human decision**
10. **Controlled update recommendations**
11. **Closeout, suspension or handover**
12. **Digital Lead actions required**

Gates 1–5 may be addressed together at spin-up in one batched exchange, but the Confirmation-First Status Gate (3) must present the held position and obtain confirmation before that position is used or reconciled as current. The Live Session Status Board (6) is created at spin-up and refreshed on every material exchange thereafter. For reporting sessions, the Confirmation-First Status Gate may be completed as a structured batch confirmation across the initiatives in scope.

---

## 1. Runtime Access Confirmation Gate

This is the runtime gate all material governed sessions must perform. It preserves and applies the existing access-gate rules in `CLAUDE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` and `00_system_control/11_COWORKER_ROUTER.md`. It is not the build-time repository access check.

At spin-up the coworker must state:

- which current repository authority files it can access;
- which supplied exports, snapshots, and evidence records it can access;
- which records are missing;
- whether the prompt alone is sufficient;
- whether any synced project knowledge may be stale.

This gate confirms access only. Accessible current repository authority files and supplied exports, snapshots, and evidence records take precedence over synced project knowledge for authority and content, but this gate must **not** decide that a business position is current — whether the held position is current is settled at the Confirmation-First Status Gate (gate 3) by the Digital Lead. The coworker must answer only with one of the access confirmation responses defined in `CLAUDE.md` (access confirmed / access gap / prompt sufficient) and must not begin substantive stage work until the Digital Lead confirms proceed. Uncertain access is treated as an access gap.

---

## 2. Client Context Gate

> **Client Context Gate** — confirms the applicable client profile, strategic objectives, maturity roadmap alignment, software/process context and relevant governance artefacts. The detailed gate is governed by a forthcoming Client Digital Governance Profile and Maturity Improvement Loop authority model.

The following future files are `Placeholder — lifecycle-recognised, not operationally governed yet.`:

- Client Digital Governance Profile model
- Client Governance Artefact Register model
- Maturity Improvement Loop model
- Formal Re-Benchmark / Maturity Snapshot model

### Grounding rule

The Client Context Gate must be grounded in a controlled client-context source where one is available, such as:

- an approved client profile;
- benchmark assessment;
- maturity register;
- improvement roadmap;
- software ecosystem artefact;
- digital strategy;
- governance artefact register;
- other approved client governance record.

The coworker must **not** reconstruct or declare the client context current from memory, synced project knowledge, previous assistant summaries, chat history, or assumptions based on earlier client work.

Until the full Client Digital Governance Profile and Governance Artefact Register models are implemented, the gate may be satisfied by:

1. a controlled current client-context artefact supplied or accessible in-session; or
2. explicit Digital Lead confirmation of the applicable profile, artefact version and known limitations.

Where neither is available, record:

`Access gap — controlled client context not available.`

The gate must not be reported as complete on the basis of assumed context.

### Accepted gap

Where the Digital Lead explicitly permits the session to proceed, record the missing client context as an accepted gap and identify:

- which context was unavailable;
- which outputs or decisions may be affected;
- what controlled artefact or confirmation is required;
- the owner;
- the review point.

A Client Context Gate access gap does not automatically block every routine session. It must block any claim that strategy, maturity, ecosystem, governance or source-of-truth alignment has been fully assessed.

### Proportionality

The gate depth must be proportionate to the session.

A **full** Client Context Gate is mandatory for:

- Hopper intake;
- Hopper Portfolio Readiness;
- Pack 1 / Stage 1D;
- Implementation / Support initiation;
- Capex Request Sessions;
- material scope or change-control sessions;
- delivery closeout;
- adoption and benefits review;
- source-of-truth impact review;
- maturity review;
- formal re-benchmarking.

**Routine delivery reviews** may use a current-profile confirmation where:

- the applicable controlled profile / version is identified;
- no material strategy, maturity, ecosystem or governance change has occurred;
- the Digital Lead confirms that no deeper review is required.

This workstream does not create the Client Digital Governance Profile model and does not invent the client benchmark scoring methodology.

---

## 3. Confirmation-First Status Gate

Access confirmation (gate 1) and business-status confirmation are separate mandatory controls. Gate 1 confirms whether the coworker can access the required repository files, exports, snapshots, evidence files, or prompt-contained information. It does **not** confirm that the business status is current.

At the start of every material initiative or reporting session, after access is established and before the supplied status is used, the coworker must:

1. present the latest available position it holds;
2. identify the source and date of that position;
3. ask:

> **Is this still accurate? Please confirm or provide any changes since the last recorded update.**

The coworker must not treat any of the following as current without Digital Lead confirmation: prior chat; Claude Project knowledge; assistant memory; an earlier report; an older export; an initiative evidence file; a previously approved historical artefact; a prior status snapshot. A previously approved historical artefact confirms a past decision, not the current status.

Where the position is not confirmed, mark the affected information `Pending confirmation` and state which output, decision, report, or control move is affected.

This gate applies to initiative sessions and to the bi-weekly and monthly reporting sessions. For reporting sessions it may be completed as a structured batch confirmation across the initiatives in scope. It is governed together with `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`.

---

## 4. Initiative Reconciliation Gate

Before substantive stage work begins, the coworker must reconcile the requested initiative and any visible unresolved governance obligations.

### 4.1 Available read-source hierarchy (no live client connection)

Claude has no live connection to Jira, SharePoint, or Omega 365 and must not imply one. Use this hierarchy:

1. The latest confirmed Initiative Evidence and Decision File for the initiative.
2. A current Jira export, snapshot, or report supplied in-session.
3. Another current supplied controlled record (for example a SharePoint export or Omega 365 action extract) where the evidence file does not expose all required control fields.
4. If none is available, declare an Initiative Reconciliation access gap.

The reconciled position is not treated as current until the Confirmation-First Status Gate is satisfied.

The coworker must state:

- which source was used (Initiative Evidence and Decision File, supplied Jira export, SharePoint export, or Omega 365 extract);
- source date and freshness;
- the last Digital Lead confirmation date;
- the scope of records included;
- whether the source covers only the requested initiative or the wider portfolio;
- the filters used for a supplied Jira export;
- whether decisions, evidence and linked delivery records were included;
- the required Initiative Evidence and Decision File update;
- the required Jira, SharePoint, and Omega 365 physical write-backs;
- limitations on the reconciliation performed.

The coworker must **not** reconstruct the initiative-control position from memory, synced project knowledge, prior assistant summaries, chat history, or assumptions about Jira. Conversation search may be used only as a secondary discovery aid; information recovered from a conversation must be reconciled into a controlled record before it is treated as authoritative.

### 4.2 Items to reconcile

Check for:

- active governed sessions;
- suspended sessions;
- pending evidence;
- pending Digital Lead decisions;
- pending external approvals;
- accepted but unresolved gaps;
- accepted but unresolved mobilisation gaps;
- unacknowledged handovers;
- stage gates awaiting evidence;
- candidate changes not yet dispositioned;
- records whose freshness requires revalidation;
- unresolved source-of-truth impacts;
- internal delivery, go-live, adoption, benefits, or closeout stage transitions not completed.

Unresolved items from other initiatives must be reported. They must not automatically block unrelated work.

### 4.3 Reconciliation waiver

Where no valid reconciliation source is available, pause and report an access gap. The session may continue only if the Digital Lead explicitly waives the Initiative Reconciliation Gate.

Record the waiver as:

`Accepted gap — Initiative Reconciliation not completed.`

The waiver record must include:

- initiative / session affected;
- reason no source was available;
- scope of reconciliation not completed;
- risk created by proceeding;
- source required later;
- owner;
- review point;
- effect on outputs and decisions.

A waived session must not claim:

- full portfolio reconciliation;
- absence of conflicting sessions;
- absence of pending obligations;
- that the initiative status is current beyond the available evidence.

The waiver must appear in the Live Session Status Board, in Digital Lead actions required, and in the closeout write-back.

---

## 5. Required Inputs Gate

At stage spin-up, produce one consolidated input table:

| Required item | Status | Source / evidence | Owner | Freshness position | Blocker / consequence | Required action |
|---|---|---|---|---|---|---|

Approved statuses:

- Present
- Missing
- Stale
- Pending confirmation
- Accepted gap
- Not applicable

Freshness position uses the freshness statuses in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` (Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable).

Questions must be batched. Do not drip-feed one question at a time unless an answer creates a genuinely new dependency.

No substantive stage output may be treated as controlled-ready until mandatory inputs are Present or explicitly accepted as gaps by the Digital Lead.

---

## 6. Live Session Status Board

Every material exchange must create or refresh a visible session board:

| Item | Category | Status | Owner | Source / evidence | Blocker | Next action |
|---|---|---|---|---|---|---|

Categories must include where relevant:

- initiative position;
- artefact / document;
- evidence;
- decision;
- approval;
- Digital Lead action;
- external action;
- Jira update;
- SharePoint update;
- source-of-truth impact;
- client-context impact;
- maturity impact;
- handover.

Approved item statuses:

- Not started
- In progress
- Awaiting Digital Lead
- Awaiting external input
- Pending evidence
- Complete
- Accepted gap
- Not applicable

---

## 7. Stage-specific work

Stage-specific work is governed by the relevant route / stage authority file (for example `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`, `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`, `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`, or `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`). This protocol does not redefine that work; it wraps it in the interactive gates, the status board, and the closeout write-back.

Stage segregation applies: a closing stage hands over only what it agreed, delivered, approved, evidenced and left open. Next-stage checklists and plans are produced only at spin-up of the next stage after the Digital Lead explicitly triggers it.

---

## 8. Governance and evidence test

Apply the governance test and evidence / freshness model before any output is treated as controlled-ready. Freshness is event / cadence based (see `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`); there is no universal arbitrary staleness period. A stale item must identify the reason it is stale, the output or decision blocked, the owner, the evidence required, and the next review point.

---

## 9. Human decision

The Digital Lead is the decision and approval authority at every controlled update and stage transition. AI proposes; the Digital Lead decides. No controlled update (repository, Jira, SharePoint, process artefact, source-of-truth) is applied without Digital Lead approval, and the next stage is not started until the Digital Lead explicitly spins it up.

---

## 10. Controlled update recommendations

Prepare update text as recommendations only, using the label that matches the target:

- **Client-system updates (Jira, SharePoint, Omega 365):** `Recommended update — requires Digital Lead approval and physical update in the client system.` Claude cannot mutate Jira, SharePoint, or Omega 365; the Digital Lead or an authorised user performs the physical update and confirms completion.
- **Reusable GitHub authority-file updates and the AI-readable Initiative Evidence and Decision File:** `Recommended update — requires Digital Lead approval.` These are not client-system physical write-backs; the Initiative Evidence and Decision File is maintained only within Claude's approved AI-readable workspace role and only when the Digital Lead approves the update or instructs Claude to make it.

This restates the AI permission boundary already governed by `00_system_control/OPERATING_RULES.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. It does not extend AI authority.

---

## 11. Closeout, suspension or handover — controlled session states

Add these controlled session states:

- Not started
- Active
- Suspended — awaiting evidence
- Pending Digital Lead decision
- Pending external approval
- Ready for closeout
- Closed and handed over

Do not use "open chat thread" as a governance status. A suspended session must remain visible at future Initiative Reconciliation Gates. A suspended session does not automatically block unrelated initiative work.

### Closeout write-back rule

No material governed session may be treated as closed until a controlled write-back has been proposed. The write-back must cover:

- initiative lifecycle position;
- macro-stage;
- detailed lifecycle stage;
- gate status;
- decision outcome;
- approval conditions;
- evidence added;
- evidence missing;
- actions open;
- accepted gaps;
- linked artefacts;
- required Initiative Evidence and Decision File update;
- required Jira physical write-back, where relevant;
- required SharePoint / evidence physical write-back, where relevant;
- required Omega 365 physical write-back, where relevant;
- client-context impacts;
- source-of-truth impacts;
- maturity-impact position;
- handover state;
- next-stage trigger.

Each recommendation must be labelled to match its target: physical Jira, SharePoint, or Omega 365 write-backs use `Recommended update — requires Digital Lead approval and physical update in the client system.`; the Initiative Evidence and Decision File update and any reusable GitHub authority-file update use `Recommended update — requires Digital Lead approval.` (see Controlled update recommendations above). Claude never implies it can mutate Jira, SharePoint, or Omega 365.

The session is not closed until the Digital Lead has:

- approved the write-back;
- explicitly deferred the write-back; or
- accepted the remaining gap.

The closeout otherwise uses the Stage Closeout Handover Output Model, Knowledge Capture Review, CDO QA / Self-Improvement Check and Source-of-Truth Update Recommendations in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, proportionate to the session.

---

## 12. Digital Lead actions required

Every substantive governed-session response must end with a standing action block:

## Digital Lead actions required

| Action | Owner | Required by / trigger | Consequence if not completed |
|---|---|---|---|

Where no action is required, state:

`No Digital Lead action required at this point.`

Do not use vague wording such as "review as required", "confirm when ready", or "update as appropriate".

---

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. This protocol adds no AI approval authority, no numeric AI confidence scoring, and no uncontrolled Jira, SharePoint, GitHub or source-of-truth mutation authority.
