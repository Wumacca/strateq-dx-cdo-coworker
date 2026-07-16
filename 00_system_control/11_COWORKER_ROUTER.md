# Coworker Router

## Purpose

This file defines the request-to-jurisdiction routing layer for material governed coworker sessions.

For a material governed coworker session, the router helps resolve, before work begins:

- the correct coworker jurisdiction
- the lifecycle stage
- the authority files that govern the work
- the permitted outputs
- the prohibited outputs
- the approval gates

The router is a routing aid. It points to the governing files. It does not contain or replace the detailed workflow logic those files hold.

## Claude Opus Access Confirmation Gate

Where the routed task is intended for Claude Opus, the first output must be an access confirmation response only. The Opus session must confirm whether it can access the authority files, source files, snapshots, exports, or prompt-contained information required for the task. It must not start the substantive coworker session until the Digital Lead confirms proceed.

This applies to Hopper Portfolio Readiness Reviews, Pack 1 readiness reviews, delivery reviews, adoption/benefits reviews, source-of-truth reviews, programme reporting reviews, and any other material governed review.

The router must not be used to bypass this gate.

## Subordination

The router is subordinate to, and must not override, the following authority files:

- `CLAUDE.md`
- `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`
- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/04_COWORKER_HANDOVER_MODEL.md`
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/CONTROLLED_VOCABULARY.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `01_governance_lifecycle/05_ROUTE_RULES.md`
- `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`
- `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`
- `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

There are exactly two client-project lifecycle coworkers — the Hopper Lifecycle Coworker and the Live Delivery Coworker. DRB, source-of-truth artefact control, adoption, benefits, capitalisation, maturity review, and programme / leadership reporting are governed stages, controls, or modes, not separate coworkers. Digital Governance & Strategy is a programme governance and control function, not a client-project coworker. Claude has no live connection to Jira, SharePoint, or Omega 365.

Where the router and any authority file appear to conflict, the authority file governs and the conflict must be surfaced to the Digital Lead before final output.

## Router Boundaries

The router must not:

- replace the lifecycle map
- replace the governed workflow looping standard
- duplicate operating rules
- duplicate route rules
- duplicate source-of-truth governance
- create new route labels
- split route vocabulary
- rename governance model files (including the Completed Initiation Form and DRB meeting-support text model files)
- introduce KPI governance as a default trigger
- introduce Confluence
- create a pickup/handoff protocol
- create skillset lens files
- create programme-memory files or a programme-status ledger
- create additional coworkers, additional client-project threads, or additional reporting cycles
- imply a live connection to Jira, SharePoint, or Omega 365

The router resolves jurisdiction and points to governing files. The governing files define what is produced and how.

## How To Use The Router

For a material governed coworker session:

1. Load `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.
2. Use this router to resolve coworker jurisdiction, lifecycle stage, authority files, permitted outputs, prohibited outputs, and approval gates.
3. Confirm the lifecycle position against `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`.
4. Apply the governing stage / route files exactly as written.
5. Run the session under the governed workflow loop, with the Digital Lead approval gate at every controlled update and stage transition.

The material session threshold and the proportionality rule are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. The router does not redefine them.

## Global Interactive Session Rule

Every material stage / session trigger invokes the Interactive Governed Session Protocol (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`) **before** stage-specific execution. Whatever jurisdiction the router resolves, the coworker first runs the Runtime Access Confirmation Gate, the proportionate Client Context Gate, the Initiative Reconciliation Gate, and the Required Inputs Gate, maintains the Live Session Status Board, ends substantive responses with the Digital Lead actions block, and closes only after a controlled write-back has been approved, deferred, or its gap accepted. The router resolves jurisdiction; `12` governs the interactive sequence. This rule creates no new coworker route.

## Coworker Jurisdictions

The router recognises exactly two client-project lifecycle coworkers — the Hopper Lifecycle Coworker and the Live Delivery Coworker. Source-of-truth artefact control and adoption / benefits are governed modes / stages within those coworkers, not separate coworkers.

### 1. Hopper Lifecycle Coworker

Owns the full pre-live lifecycle, including:

- Hopper Portfolio Readiness
- Hopper snapshot review
- Hopper triage
- initiative minimum-information completion
- benchmark-aligned proposed priority
- grouping / epic recommendation
- Initiation Form / Pack 1 spin-up
- Development Route Stage 1D
- Stage 1D closeout / handover

Development Stage 1D is not a separate coworker. It is work owned by the Hopper Lifecycle Coworker under `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

Stage closeout is not a separate coworker. It is the closing step of the owning coworker's stage under `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` and `00_system_control/04_COWORKER_HANDOVER_MODEL.md`.

### 2. Live Delivery Coworker

Owns the approved live job after Stage 1D / Stage 2 / form approval, including delivery mobilisation, delivery tracking, delivery risk and status, implementation evidence, scope control, and delivery closeout readiness, governed by `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` and `00_system_control/04_COWORKER_HANDOVER_MODEL.md`.

The label is **Live Delivery Coworker**. Do not use "Initiative Delivery Coworker".

### Source-of-truth artefact control (governed mode)

This is a controlled mode within the Live Delivery Coworker's ownership, not a separate coworker or a separate thread. It is invoked when source-of-truth artefact integrity is the subject of the work (artefact registers, process flow / ecosystem / maturity registers, decision records, superseded / active artefact control), governed by `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. It is applied inside the continuous initiative thread.

### Adoption / benefits (internal Live Delivery stage)

Adoption and benefits are internal stages of the Live Delivery Coworker, applied only when that lifecycle stage is reached and handled inside the continuous initiative thread. The detailed adoption / benefits model remains future scope until its own model file is created, consistent with `00_system_control/OPERATING_RULES.md`. It is not a separate coworker or thread.

## Hopper Portfolio Readiness

> **Governing model.** The full Hopper Portfolio Readiness Review workflow — Access Confirmation Gate, Part 1 Grouping Review, Part 2 Minimum Hopper Information, Part 3 Scoring / Priority Preparation, the Initiative Charter rule, the route rules, the post-DRB route triggers, and the mandatory looping closeout — is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. This section is a routing summary subordinate to that model. The review is pre-initiation and pre-Pack 1, its default meeting surface is the **Jira Initiative View / Hopper priority view**, and it does **not** create a separate DRB Priority Screen artefact unless the Digital Lead explicitly requests one. Where this section and `09` appear to differ on the review process, `09` governs.

Hopper Portfolio Readiness is the standing responsibility to keep the Hopper capable of producing a leadership-ready minimum viable initiative portfolio at any time. The purpose is to ensure that all known Hopper items and initiatives are listed, understood at minimum-information level, benchmark-aligned where possible, proposed for priority, assessed for grouping or epic logic, and ready for leadership review or Pack 1 spin-up decision.

Required strategic reason: The Hopper must be capable of answering leadership requests for the next six months of proposed digital initiatives across implementation, development, and support, with minimum viable business reason, proposed priority, route indication, readiness, and next control move.

Hopper Portfolio Readiness is owned by the Hopper Lifecycle Coworker.

### Snapshot / Upload Trigger

Where a Hopper screenshot, image, export, or snapshot is uploaded, the router must route the request to the Hopper Lifecycle Coworker and ask:

> "A Hopper snapshot has been uploaded. Do you want to spin up a Hopper Portfolio Readiness Review session?"

The coworker must wait for Digital Lead approval before proceeding. It must not start the review until the Digital Lead confirms.

### Recalibrated File-Based Source-Read Rule

If Digital Lead approval is given, the coworker must not review the screenshot in isolation and must not start from a blank workshop. It must pre-populate a proposed Hopper review table using all available approved source information.

The source-read hierarchy is:

1. Current Hopper screenshot / export / snapshot
2. Current Initiative Evidence and Decision Files where they exist
3. Digital Benchmark Assessment / benchmark source files
4. Phase 2 update / roadmap / summary files
5. Approved initiation forms
6. Adoption / benefits / closure records
7. AIRB / QPR / assurance materials where relevant
8. Prior coworker handovers and update files where available
9. Source-of-truth artefact files where relevant

Claude has no live connection to Jira, SharePoint, or Omega 365; it reads only supplied or accessible controlled records. If Initiative Evidence and Decision Files do not exist, the coworker must state this as a limitation and use the available source files. It must not create a programme-memory or programme-status ledger. Cross-initiative status is read from the confirmed Initiative Evidence and Decision Files.

The coworker must use all available approved information to propose answers for Digital Lead review.

It must clearly distinguish:

- known facts from source files
- inferred position
- proposed priority
- open clarification
- items already in delivery, live, closed, superseded, or duplicated

Every proposed answer must show:

- **Confidence:** High / Medium / Low
- **Source Basis:** Snapshot / Initiative Evidence / Benchmark / Phase 2 / Initiation Form / Adoption-Benefits / AIRB-QPR / Prior Handover / Source-of-Truth / Inference

### Hopper Portfolio Readiness Review Output

The session must return:

1. Snapshot Control Statement
2. Sources Considered
3. Data Quality / Completeness Review
4. Proposed Hopper Review Table
5. Benchmark Alignment
6. Proposed Priority
7. Grouping / Epic Recommendations
8. Leadership Six-Month View
9. Pack 1 Readiness
10. Open Clarifications
11. Recommended Hopper Updates for Digital Lead Approval
12. Recommended Initiative Evidence and Decision File updates for Digital Lead Approval

### Proposed Hopper Review Table Fields

The Proposed Hopper Review Table must include these fields:

- Initiative
- Current Hopper Status
- Department
- Proposed Business Reason
- Source Basis
- Benchmark Alignment
- Route Indication
- Proposed Priority
- Grouping Recommendation
- Suggested Epic / Group
- Readiness
- Next Control Move
- Confidence
- Digital Lead Decision

The Digital Lead Decision field must be left blank or set to "To confirm".

### Minimum Information Standard

Each Hopper item must have, or be flagged as missing:

- initiative name
- business reason
- department / function
- route indication
- proposed priority
- readiness
- next control move

No detailed scope is required at Hopper Portfolio Readiness stage.

### Priority Logic

Priority must be proposed using this hierarchy:

1. Enterprise risk / assurance
2. Duty Holder / regulatory relevance
3. Operating model / governance impact
4. Benchmark gap alignment
5. Commercial / delivery value
6. Feasibility / readiness
7. Grouping leverage

Priority values:

- **P1:** candidate for next 0–3 months / Pack 1 preparation
- **P2:** candidate for next 3–6 months
- **P3:** retain in Hopper / sequence later
- **Clarify:** not enough information
- **Group:** should be combined before prioritisation
- **Hold:** not currently justified
- **Retire:** no longer valid / superseded / already closed

These Hopper Portfolio Readiness priority values are proposal-stage portfolio prioritisation values. They do not replace the canonical DRB priority decisions or consolidation outcomes in `00_system_control/CONTROLLED_VOCABULARY.md`, which remain authoritative at their stages.

### Benchmark Alignment Values

Benchmark alignment values should include:

- Digital Strategy
- Process
- Organisational Culture & Change
- Service Delivery
- People
- Technology & Infrastructure
- External Assessment
- Digital Collaboration
- Software Ecosystem
- Data / Visibility
- Governance / Change
- Action Management
- User Tools

### Grouping Logic

The coworker must actively identify when initiatives should be grouped into an epic or combined initiative.

Grouping triggers:

- same department
- same workflow
- same system
- same source-of-truth impact
- same business problem
- same approval route
- dependency chain
- same benchmark driver

Grouping values:

- Standalone
- Candidate Epic
- Linked Dependency
- Merge Candidate
- Already In Delivery
- Closed / Operational

### Pack 1 Boundary

> Hopper Portfolio Readiness Review = portfolio prioritisation readiness.
> Pack 1 session = detailed initiative shaping and DRB preparation.

The Hopper Portfolio Readiness Review must not create:

- detailed scope
- process flow
- cost estimate
- implementation plan
- DRB pack
- delivery plan
- Jira execution structure

Those outputs require explicit Digital Lead spin-up of Pack 1.

### Leadership Six-Month View

The coworker must be able to produce a leadership-ready view grouped by:

- 0–3 months
- 3–6 months
- clarify / hold / retire
- implementation candidates
- development candidates
- support candidates

## No Automatic Update Authority

The coworker may recommend Hopper updates, but must not update Jira, SharePoint, GitHub, source-of-truth files, Initiative Evidence and Decision Files, or controlled records without Digital Lead approval.

Where updates are needed, the coworker must present them as:

> "Recommended update — requires Digital Lead approval."

This restates the AI permission boundary already governed by `00_system_control/OPERATING_RULES.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. It does not extend AI authority.

## Router Table

| # | Trigger | Route To | Lifecycle Stage | Authority Files | Permitted Outputs | Prohibited Outputs | Approval Gate |
|---:|---|---|---|---|---|---|---|
| 1 | Hopper screenshot / export / snapshot uploaded | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` | Ask the spin-up question; wait | Starting the review before approval | Digital Lead must approve spin-up |
| 2 | Hopper Portfolio Readiness Review approved | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `01_governance_lifecycle/05_ROUTE_RULES.md`; `00_system_control/CONTROLLED_VOCABULARY.md` | Pre-populated Proposed Hopper Review Table and the readiness review outputs, using the source-read hierarchy | Detailed scope, process flow, cost estimate, implementation plan, DRB pack, Jira execution structure | Recommendations only; Digital Lead approves any update |
| 3 | Leadership asks for next six months of proposed initiatives | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` | Leadership Six-Month View grouped as specified | Pack 1 / DRB detail | Recommendations only |
| 4 | User asks whether an item is ready for Pack 1 | Hopper Lifecycle Coworker | Hopper Portfolio Readiness → Pack 1 boundary | This file; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; relevant route / initiation authority files under `01_governance_lifecycle/` | Pack 1 Readiness assessment | Pack 1 outputs without explicit spin-up | Digital Lead must spin up Pack 1 |
| 5 | User asks to group initiatives into epics | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` | Grouping / Epic Recommendations using grouping values | Building the epic / delivery structure | Recommendations only |
| 6 | User asks to update Hopper after review | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`; `00_system_control/OPERATING_RULES.md` | "Recommended update — requires Digital Lead approval." | Direct update to Jira / SharePoint / Hopper; implying live client-system access | Digital Lead approves; coworker does not apply |
| 7 | User asks to update the confirmed initiative position after a review | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`; `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` | Recommended Initiative Evidence and Decision File updates and required Jira / SharePoint / Omega 365 physical write-backs, labelled as recommendations | Creating a programme-memory or programme-status ledger; mutating client systems | Digital Lead approves; coworker does not apply |
| 8 | User uploads completed / live / closed initiative evidence that affects Hopper status | Hopper Lifecycle Coworker for portfolio-status reflection; the initiative is owned by the Live Delivery Coworker once approved (internal stage, same thread) | Hopper Portfolio Readiness with delivery/closure status read | This file; `04_COWORKER_HANDOVER_MODEL.md`; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` | Reflect items as in delivery / live / closed / superseded / duplicated, with Source Basis and Confidence | Reopening, restructuring, or modifying delivery/adoption records without explicit spin-up and Digital Lead approval | Recommendations only; principal handover checkpoint only at Hopper → Live Delivery |
| 9 | User asks for a development epic charter or department scoring input | Hopper Lifecycle Coworker | Hopper Portfolio Readiness | This file; `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md` | Initiative Charter (pre-initiation input tool only) using the charter columns in `09` | Treating the charter as an Initiation Form; committing scope or budget; producing Pack 1 / Stage 1D before approval | Recommendations only; charter feeds the Jira Initiative View / Hopper priority discussion |
| 10 | Leadership / DRB approves a route trigger after the priority discussion | Hopper Lifecycle Coworker | Hopper Portfolio Readiness → route trigger | This file; `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`; `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md` | Per-initiative route trigger: development epic → Pack 1 / Stage 1D; implementation → Initiation Form / Implementation Route; support → selection/support route then Initiation Form; in-flight → continue under existing record | Batching unrelated initiatives into one Pack 1; starting any stage before explicit Digital Lead spin-up | Digital Lead approves and spins up each receiving stage |
| 11 | Digital Lead opens a capex request / capitalisation closeout-and-next-request session | Hopper Lifecycle Coworker | Hopper Portfolio Readiness — Capex Request Mode | `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `00_system_control/CONTROLLED_VOCABULARY.md`; `00_system_control/OPERATING_RULES.md`; `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`; `01_governance_lifecycle/05_ROUTE_RULES.md`; `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`; `00_system_control/04_COWORKER_HANDOVER_MODEL.md`; `docs/presentation-standards/communication-and-framing-standard.md` where present | Access gate; source-read status reflection; Capex Readiness Tracker; Portfolio Capex Request Pack; Capital Efficiency Evidence; Plan Attainment Evidence; Claim Safety Table; Board slide brief / storyboard; client-review Board-draft deck; Hopper → Live Delivery Handover Checklist | Final spend approval; maturity approval; benefits approval; a Board-final deck while blockers remain open; initiative-level delivery mobilisation; Pack 1 / Stage 1D / Stage 1 / Stage 2 detail before route-specific spin-up; Jira delivery / epic build; unsupported Board claims; controlled updates without Digital Lead approval | Digital Lead approval required for spin-up, readiness, output use, and every controlled update |

## No Programme-Memory Ledger

The router must not create, or recommend the creation of, a programme-memory or programme-status ledger (for example generic `PROGRAMME_STATUS.md`, `HOPPER_STATUS.md`, `INITIATIVE_INDEX.md`, `SESSION_HANDOVER.md`, `DECISION_LOG.md`, `DELIVERY_STATUS.md`, or `ADOPTION_CLOSURE_STATUS.md` files) or any differently named equivalent. Cross-initiative status is read from the confirmed Initiative Evidence and Decision Files governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. GitHub holds reusable methods and schemas only and must not become a parallel live client initiative-management system.

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
