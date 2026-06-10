# Digital Governance Programme Lifecycle

## Purpose

This file defines the full Strateq DX digital governance programme lifecycle, the responsible coworker at each stage, the required stage intent, the required handover points, and the repository files that should govern detailed execution.

This file is the programme-level lifecycle map.

Detailed workflow execution remains governed by the relevant stage-specific files.

## Operating Principles

Jira is the initiative lifecycle system.

SharePoint is the organisational source-of-record artefact store.

GitHub is the coworker operating-rule source of truth.

Coworkers facilitate, draft, check, route, and prepare controlled artefacts.

Coworkers do not approve initiatives, accept risk, approve cost, commit suppliers, or bypass DRB / Nitro / leadership approval.

Every lifecycle transition between coworkers requires a handover checkpoint under `00_system_control/04_COWORKER_HANDOVER_MODEL.md`.

## Full Programme Lifecycle

| Step | Lifecycle Stage | Responsible Coworker | Stage Intent | Primary Controlled Systems / Artefacts | Required Handover |
|---:|---|---|---|---|---|
| 1 | Digital Governance & Strategy | Digital Governance & Strategy Coworker | Maintain the governance environment that creates, assesses, prioritises, funds, reports, and controls digital change. | Digital strategy, governance model, DRB model, capitalisation artefacts, benchmark assessments, maturity register, programme reports, SharePoint artefact library. | Handover to Hopper when a candidate initiative is created or confirmed. |
| 2 | Assessment / Benchmark / Maturity Review | Digital Governance & Strategy Coworker | Identify gaps, risks, improvement areas, digital maturity needs, or organisational requirements that may create candidate initiatives. | Benchmark assessment, digital maturity assessment, assessment evidence, maturity register, recommendation log. | Handover to Hopper if an initiative candidate enters the Hopper. |
| 3 | Candidate Initiative Creation | Digital Governance & Strategy Coworker → Hopper Lifecycle Coworker | Convert a governance, strategy, assessment, operational, client, or department need into a candidate Hopper item. | Jira candidate item, source evidence, SharePoint reference artefacts. | Governance-to-Hopper handover required. |
| 4 | Existing Hopper / Intake Consolidation | Hopper Lifecycle Coworker | Consolidate existing candidate initiatives and remove duplicates, BAU items, merged items, or unclear entries. | Jira Hopper, exported Jira fields, department notes, initiative list. | Internal Hopper continuity note if items move to scoping. |
| 5 | Light-Touch Department Scoping | Hopper Lifecycle Coworker | Clarify enough context to understand the need, source, likely value, and whether the item deserves DRB prioritisation discussion. | Jira fields, clarification notes, department/champion evidence. | Internal Hopper continuity note if item moves to Priority Screen. |
| 6 | Hopper Priority Screen | Hopper Lifecycle Coworker | Prepare candidate initiatives for DRB prioritisation across the next programme window. | Priority screen, Jira fields, scoring notes, department summary. | Internal Hopper continuity note into DRB priority discussion. |
| 7 | DRB Priority Discussion | Hopper Lifecycle Coworker + DRB | Decide whether an item is approved for Stage 1D or Stage 1, requires clarification, is deferred, rejected, BAU, or merged. | DRB notes, Jira status, decision record. | DRB decision checkpoint required before Stage 1D or Stage 1. |
| 7A | Route Classification | Hopper Lifecycle Coworker | Classify the initiative as Development Route or Implementation / Support Route from the Jira Initiative Type field or screenshot before launching Stage 1D or Stage 1. | Initiative Type field, Jira screenshot. | Route confirmed before session opens. |
| 7B | Stage 1D: Development Route Hopper Clarification / DRB Approval to Commence Development Job | Hopper Lifecycle Coworker | Clarify the internal development initiative enough for DRB to approve commencement of the live development job. Stage 2 exception gate must be tested before final pack production. | Jira field values, DRB Brief (Development Approval variant), Scope Brief, process flow swimlane specification where process mapping required, source-of-truth artefact impact check and handover note where artefacts impacted. | Stage 1D closeout / Live Delivery handover required if no Stage 2 exception. Stage 1D to Stage 2 if exception gate triggered. Stage 1D to Source-of-Truth Artefact Controller where controlled artefacts are impacted. |
| 8 | Stage 1: Hopper Clarification / DRB Approval to Commence Initiation (Implementation / Support Route) | Hopper Lifecycle Coworker | Clarify the Hopper item enough for DRB to decide whether formal digital initiation should commence. Applies to Implementation / Support Route. | Jira field values, Stage 1 DRB brief, process mapping required decision, process mapping capture sheet if required. | Stage 1 closeout / Stage 2 readiness checkpoint required. |
| 9 | Process Mapping Capture | Hopper Lifecycle Coworker | Capture current and required process logic when process mapping is required. This is a capture sheet, not a final process flow. | Excel process mapping capture sheet, department notes, RACI, bottlenecks, future-state needs. | Feeds Stage 2. |
| 10 | Stage 2: Digital Initiation / DRB Approval to Commence Job | Hopper Lifecycle Coworker | Build the formal initiation pack required for DRB to approve the initiative to become a live job. Applies to Implementation / Support Route, and to Development Route where Stage 2 exception gate is triggered. | Requirements list, vendor/developer review, process-flow specification, source-of-truth impact report, initiation approval summary, Jira update text. | Hopper-to-Live Delivery handover required at Stage 2 closeout. |
| 11 | Implementation Form / Development Form | Hopper Lifecycle Coworker → Live Delivery Coworker | Convert approved initiation into a delivery-ready implementation or development route where required. | Implementation form, development form, Jira epic / delivery structure, approved requirements. | Handover to Live Delivery required. |
| 12 | DRB Form Approval | DRB + Live Delivery Coworker | Confirm the delivery route, approved scope, cost, timing, owner, route, and controls before live delivery starts. | Approved form, Jira status, approval record. | Delivery start checkpoint required. |
| 13 | Nitro / Leadership Sign-Off | Digital Governance & Strategy Coworker + DRB + Leadership | Obtain higher-level approval where required by cost, risk, contract, capitalisation, or leadership threshold. | Nitro pack, leadership approval, capitalisation record. | Leadership decision checkpoint required. |
| 14 | Job Live | Live Delivery Coworker | Move initiative into controlled delivery execution. | Jira live job, delivery plan, supplier/developer tasks, risks/actions, reporting cadence. | Live delivery operating checkpoint required. |
| 15 | Live Delivery | Live Delivery Coworker | Track delivery, issues, vendor/developer progress, scope control, risks, blockers, and implementation evidence. | Jira delivery structure, weekly status, risks/actions, delivery artefacts, implementation evidence. | Delivery-to-Adoption handover required. |
| 16 | Go-Live / Deployment | Live Delivery Coworker → Adoption & Benefits Coworker | Confirm the solution is live, users are identified, support route exists, and adoption period can start. | Go-live record, user list, support model, training evidence, operational readiness. | Go-live handover required. |
| 17 | Adoption & Benefits | Adoption & Benefits Coworker | Confirm controlled use, competence, benefits evidence, ownership, support, and closeout readiness. | 30-day review, benefits evidence, adoption evidence, competence readiness, support ownership, closeout record. | Adoption-to-Source-of-Truth handover required. |
| 18 | Source-of-Truth Artefact Control / Programme Governance Update | Source-of-Truth Artefact Controller / Digital Governance & Strategy Coworker | Update programme artefacts, SharePoint registers, strategy/guidance, maturity records, process maps, software ecosystem records, lessons learned, and reporting. | SharePoint artefacts, process/register updates, source-of-truth impact closure, lessons learned, programme report. | Governance update checkpoint closes the lifecycle or creates new Hopper candidates. |
| 19 | PEP / Development Execution Where Applicable | Live Delivery Coworker + Delivery Owner | Manage approved implementation PEPs or development execution streams that sit within or after live delivery. | PEP / development execution plans, delivery controls, Jira execution tasks. | Handover back to Adoption or Source-of-Truth when complete. |

## Coworker Responsibilities

### Digital Governance & Strategy Coworker

Owns the pre-Hopper and programme governance environment.

Responsible for:

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
- receiving Stage 1D source-of-truth artefact handovers where controlled artefacts are impacted

Must hand over to the Hopper Lifecycle Coworker when a candidate initiative enters the Hopper.

### Hopper Lifecycle Coworker

Owns the route from candidate Hopper item through approval to become a live job.

Responsible for:

- Hopper intake and consolidation
- light-touch department scoping
- Hopper Priority Screen preparation
- DRB priority discussion support
- route classification (Development Route or Implementation / Support Route)
- Stage 1D Development Route Hopper Clarification / DRB Approval to Commence Development Job
- Stage 1D Scope Brief and Process Flow Capture Sheet issue
- Stage 1D swimlane specification production from returned capture sheet
- Stage 1D source-of-truth artefact impact check and handover note
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

Owns the approved live job after Stage 1D / Stage 2 / form approval.

Responsible for:

- delivery mobilisation
- Jira epic / delivery structure
- developer/vendor coordination
- delivery risk and issue tracking
- delivery status reporting
- implementation evidence
- scope control
- delivery closeout readiness
- handover to Adoption & Benefits

### Adoption & Benefits Coworker

Owns post-go-live control.

Responsible for:

- adoption readiness
- 30-day review
- usage evidence
- competence readiness
- benefits evidence
- support and ownership confirmation
- closeout preparation
- handover to Source-of-Truth Artefact Control

### Source-of-Truth Artefact Controller / Programme Governance Coworker

Owns source-of-truth integrity after lifecycle changes occur.

Responsible for:

- SharePoint artefact register
- process flow register
- software ecosystem register
- integration register
- maturity register
- benchmark archive
- decision records
- superseded / active artefact control
- lessons learned
- programme reporting updates
- routing new issues back to Digital Governance & Strategy or Hopper where required
- receiving and actioning Stage 1D source-of-truth artefact handovers

## Hopper Lifecycle Reference Point

The Hopper Lifecycle Coworker must not operate from project instructions alone.

When handling Hopper, Stage 1D, Stage 1, Stage 2, process mapping, DRB brief preparation, Jira field updates, source-of-truth impact checks, or handover to Live Delivery, it must identify and apply the relevant current repository files.

The Development Route Stage 1D model is the primary authority for Development Route initiatives.

For Development Route Stage 1D sessions:

- Always load: `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`
- If process mapping is required: also load `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md` and `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`
- If controlled artefacts are impacted: also load `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

The two-stage initiation model is the primary authority for Stage 1 and Stage 2 (Implementation / Support Route, and Development Route Stage 2 exceptions).

The coworker handover model is the primary authority for transitions between coworkers.

The artefact governance model is the primary authority for Jira / SharePoint / source-of-truth boundaries.

## Mandatory Handover Points

The following handovers are mandatory:

1. Digital Governance & Strategy to Hopper Lifecycle
2. Hopper Lifecycle Stage 1D closeout to Live Delivery (Development Route, no Stage 2 exception)
3. Hopper Lifecycle Stage 1D to Stage 2 (Development Route, Stage 2 exception triggered)
4. Hopper Lifecycle Stage 1D to Digital Governance & Strategy / Source-of-Truth Artefact Controller where controlled artefacts are impacted
5. Hopper Lifecycle Stage 1 closeout to Stage 2 readiness (Implementation / Support Route)
6. Hopper Lifecycle Stage 2 closeout to Live Delivery
7. Live Delivery to Adoption & Benefits
8. Adoption & Benefits to Source-of-Truth Artefact Control
9. Any coworker back to Digital Governance & Strategy where programme strategy, governance, reporting, maturity, capitalisation, or source-of-truth artefacts need updating

Handover format is governed by:

`00_system_control/04_COWORKER_HANDOVER_MODEL.md`

## File Discovery Rule

This lifecycle map is not an exhaustive list of every file in the repository.

For every task, the coworker must identify the relevant current repository files, including any newer synced files added after this lifecycle map was created.

If a task-specific file exists, that task-specific file takes precedence over a general lifecycle summary.

If two files conflict, the newer, more specific, or explicitly authoritative file should be surfaced to the Digital Lead for confirmation before final output.

## Output Boundary

The programme lifecycle map defines where the work sits.

The relevant stage file defines what must be produced.

The coworker must not produce artefacts outside the active lifecycle stage unless the Digital Lead explicitly instructs it to do so.
