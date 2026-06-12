# Development Route Stage 1D Model

## Purpose

This file defines the governed route for internal development initiatives through Development Stage 1D.

Internal development initiatives — such as Chronos, Omega, SharePoint internal builds, Power BI internal builds, or other in-house tools — may be approved to commence the live development job by DRB review of a Completed Initiation Form, without requiring the full two-stage Implementation Route.

Stage 2 review may still be triggered where exception conditions apply. See Stage 2 Exception Gate.

Development Route model: Completed Initiation Form approved by DRB, unless a Stage 2 exception trigger applies.

Implementation Route model: Stage 1 + Stage 2, governed by `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

For the three-route model rules, see `01_governance_lifecycle/05_ROUTE_RULES.md`.

## Route Classification

Before launching any session, Claude must classify the initiative route from the Jira screenshot or Initiative Type field.

### Development Route examples

- Chronos Dev
- Omega Dev
- SharePoint internal build
- Power BI internal build
- any other in-house development tool or internal platform enhancement

### Implementation Route examples

- third-party implementation
- supplier-led delivery
- external platform implementation
- option appraisal / quote comparison route
- business case / funding route

### Support Route examples

- BAU support request
- minor operational fix
- small internal process workaround
- operational improvement below risk / cost / control thresholds

If the route is unclear, Claude must ask the Digital Lead before producing any outputs.

If the Initiative Type is clearly a Development Route, Claude must load and apply this file as the primary governing file.

## Stage 1D Trigger

When the Digital Lead says `spin up stage 1 session` and the initiative is a Development Route, Claude must:

1. Confirm the route is Development Route.
2. Immediately produce the Development Stage 1D Session Start Checklist.
3. Run the Stage 1D session under this file.

Do not apply the Stage 1 workflow from `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` to a Development Route initiative unless the Stage 2 exception gate is triggered.

## Development Stage 1D Session Start Checklist

At the opening of every Stage 1D session, Claude must produce this checklist for the Digital Lead.

### A. Session Objective

Produce a Completed Initiation Form sufficient for DRB to approve commencement of the live internal development job, unless a Stage 2 exception trigger applies.

The Completed Initiation Form requires:

- Section 1 completed by the requesting department / initiator
- Digital Team additions: confirmed development route, scope, deliverables, exclusions, duration, risk assessment, system / process impact, source-of-truth artefact impact, and project charter information

Full content standard: `01_governance_lifecycle/06_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`

### B. Required Documentation and Attachments

Claude must ask the Digital Lead to provide or confirm the following:

- Jira screenshot / field export
- Initiative Type screenshot / value (confirming Development Route)
- Section 1 completion from requesting department (or confirmation it will be supplied)
- Existing scope notes
- Current process notes
- Process steps, if known
- Bottlenecks / control gaps
- Required enhancements
- Screenshots of current system or proposed screen
- Developer notes / estimate / task breakdown
- Department-provided scope (confirming requirements)
- Rejected workaround / client requirement evidence if applicable
- Dependency items or linked initiatives
- Target date / internal deadline
- Known exclusions
- Process Flow Capture Sheet (blank workbook, issued by Claude if process mapping is required or likely required — see Section C)

### C. Process Flow Capture Sheet

The Process Flow Capture Sheet is a session input tool, not a final output.

If process steps are missing or incomplete and process mapping is required or likely required, Claude must issue the blank single-sheet Process Flow Capture Sheet to the Digital Lead at session opening. The Digital Lead completes the sheet and uploads it. Claude then reads the completed sheet and produces the process flow outputs from that data.

If process steps are already provided in session documents, notes, or prior uploads, Claude may work from those directly.

Once the completed sheet is returned, Claude must produce:

- process flow swimlane specification (see Development Route Final Outputs)
- Jira scope structure items
- process bottlenecks and required enhancements
- process summary for inclusion in the Completed Initiation Form

The Process Flow Capture Sheet must be a single-sheet workbook. It must not include Stage 2 tabs, requirements tabs, source-of-truth impact tabs, risk registers, or approval summaries.

Required capture columns:

| Process Milestone | Process Step | RACI / role columns | Input / Trigger | Output | System | Process Bottlenecks | Future-State Requirement | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|

### D. Question Ledger

Claude must produce a question ledger covering all information required to reach 95% confidence before producing final outputs.

| # | Question | Source / evidence | Status | Answer |
|---|---|---|---|---|

Claude must cross-check the question ledger against all supplied files, screenshots, prior messages, and attachments before presenting remaining questions.

Claude must close any question that has already been answered in the session evidence.

## Stage 1D Required Inputs

Claude must capture and confirm:

- Jira ID and initiative name
- Initiative Type (confirming Development Route)
- Department / function
- Owner / champion
- Development objective
- Current process / workflow (as-is)
- Process bottlenecks and control gaps
- Required enhancements
- Impacted systems
- Developer notes / estimate (if available)
- Department-provided scope confirming requirements (required before Completed Initiation Form can be finalised)
- Known exclusions
- Dependencies and linked initiatives
- Target date / internal deadline
- Safety / Duty Holder risk
- Regulatory / reputational risk
- Commercial risk
- Operational impact
- Process Mapping Required?

## Completed Initiation Form: Development Route Content

The Completed Initiation Form for Development Route is structured as follows.

### Section 1 — Department / Initiator (department-owned)

- initiative title
- background and context
- problem statement
- current process / workflow
- future requirement
- expected benefit
- impacted systems
- operational impact
- risk flags

### Digital Team Additions

- confirmed development route
- confirmed scope
- agreed deliverables
- exclusions
- development owner / developer
- linked Jira task where known
- estimated duration
- target date where known
- system impact assessment
- process impact assessment
- security / data / integration considerations
- success measures
- risks and mitigations
- stakeholders and communications plan
- supporting documents list
- source-of-truth artefact impact summary

Apply `01_governance_lifecycle/06_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md` for the full content standard and DRB approval wording.

## Development Route Final Outputs

Claude must produce:

1. **Completed Initiation Form** — the formal DRB approval artefact, populated to the Development Route content standard above
2. **Development Scope / Deliverables Brief** — confirmed scope, agreed deliverables, exclusions, duration, and project charter items (see Development Scope / Deliverables Brief section below)
3. **Process flow swimlane specification** — produced from the completed Process Flow Capture Sheet where Process Mapping Required = Yes. Apply `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` and `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md`.
4. **Source-of-truth artefact impact check and handover note** — required where the initiative affects process flows, registers, ecosystem diagrams, integration records, maturity records, governance artefacts, or other controlled documentation. Apply `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.
5. **Jira Initiation Summary / Delivery Context** — paste-ready Jira field update recording the approved route, scope, key deliverables, duration, risks, and next action

A standalone Jira comment is optional and must only be produced when explicitly requested by the Digital Lead.

The Process Flow Capture Sheet is a session input tool, not a final output. Claude must not include the blank or completed capture sheet as a final output.

## Development Scope / Deliverables Brief

The Development Scope / Deliverables Brief is a formal deliverable included in or attached to the Completed Initiation Form.

### Required Content

- Initiative / Epic level summary
- Development objective
- Confirmed scope
- Known exclusions
- Milestones / task-level build areas
- Activities / subtask-level detail where known and provided
- Process bottlenecks addressed
- Required enhancements
- Developer estimate / duration where provided
- Dependencies
- Acceptance / completion expectations
- Items explicitly not to be built
- Stage 2 exception gate decision

### Hierarchy Rule

| Level | Jira equivalent | When to include |
|---|---|---|
| Initiative | Epic | Always |
| Milestones | Tasks | Always where known |
| Activities | Subtasks | Only where explicitly provided |

Claude must not invent subtasks, milestones, or developer estimates.

If activity-level detail is not furnished, task-level milestones are sufficient.

## Stage 2 Exception Gate

Before finalising the Completed Initiation Form, Claude must ask:

"Based on the current evidence, is the Completed Initiation Form with confirmed scope and duration sufficient for DRB to approve commencement of the live development job, or is further Stage 2 due diligence required before approval?"

Claude must explicitly test these exception triggers:

- Scope is not confirmed (requesting department has not confirmed requirements)
- Development team has not confirmed duration or feasibility
- Material architecture, security, or integration risk remains unresolved
- Material third-party cost or vendor decision is required
- Third-party supplier selection is required
- Business case or funding approval is required
- DRB requests further due diligence

If any exception trigger applies, Claude must recommend Stage 2 before live job approval.

Claude must not suppress or downplay a trigger to avoid Stage 2.

If no exception trigger applies and the Digital Lead confirms the Completed Initiation Form is sufficient, Claude may proceed to final output production once all questions are answered and confidence is at least 95%.

## Development Route Initiation Pack Gate

Claude must not produce the final Development Route outputs until:

- all blocking questions are answered, excluded, or explicitly deferred outside the approval decision
- Section 1 completion from the requesting department is received or confirmed as available
- the process flow capture requirement is resolved (blank sheet issued and completed sheet returned, or process mapping confirmed not required)
- developer / department scope has been reconciled if provided (see Scope Reconciliation below)
- the Stage 2 exception gate has been answered
- Claude has cross-checked the question ledger against all session evidence
- Claude reaches at least 95% confidence
- the Digital Lead explicitly approves output production

If confidence is below 95%, Claude must return only:

- missing uploads
- outstanding questions
- assumptions requiring approval
- what blocks output production

Claude must state confidence in this format: "Confidence level: X% — [reason]"

## Scope Reconciliation

If developer, department, or technical scope is provided during Stage 1D, Claude must reconcile it against the Digital Lead / governance scope before producing the Completed Initiation Form.

| Source / party | Developer / department scope | Digital Lead / governance scope | Agreed scope | Status | Required confirmation |
|---|---|---|---|---|---|

Claude must not finalise the Development Route outputs until the Agreed scope column is confirmed by the Digital Lead.

## Source-of-Truth Artefact Impact Check and Handover

This section is required when the initiative creates or changes any controlled artefact, including:

- process flow
- parent process map
- A to Z enterprise process flow
- software ecosystem diagram
- software ecosystem register
- integration record
- integration register
- maturity register
- process artefact register
- initiative / Hopper history
- decision / approval record
- SharePoint controlled document
- governance register

Claude must produce a Source-of-Truth Artefact Impact Check:

| Artefact | Impact | Status | Required Update | Timing | SharePoint Location | Jira Link / Key |
|---|---|---|---|---|---|---|

The handover note must identify:

- originating coworker / stage: Hopper Lifecycle Coworker / Stage 1D
- receiving coworker / stage: Digital Governance & Strategy Coworker / Source-of-Truth Artefact Controller
- Jira key, initiative name, lifecycle status
- decisions already made and decisions still required
- approved scope and out of scope
- impacted artefacts and required updates
- timing, SharePoint location, Jira link
- known risks / constraints and open questions
- files or outputs the receiving coworker must inspect
- required next action

Apply `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` when producing this section.

## Stage 1D to Stage 2 Exception Route

If any Stage 2 exception trigger applies, Claude must:

1. State clearly which trigger applies.
2. Recommend Stage 2 initiation before live job approval.
3. Begin a Stage 2 session under `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.
4. Not produce a Completed Initiation Form as a substitute for required Stage 2 due diligence.

## Stage 1D to Live Development (No Exception)

If no Stage 2 exception trigger applies and the Digital Lead confirms the Completed Initiation Form is sufficient:

1. Claude produces the final Development Route outputs.
2. The Digital Lead submits the Completed Initiation Form to DRB for approval.
3. DRB approval wording: "Approve [initiative name] to proceed as a live internal development job under the Development Route, based on the confirmed scope, exclusions, duration, risk controls, and supporting artefacts recorded in the Completed Initiation Form."
4. On DRB approval, a Stage 1D closeout / Live Delivery handover checkpoint is required under `00_system_control/04_COWORKER_HANDOVER_MODEL.md`.
5. Where the initiative affects controlled artefacts, Claude must produce a Source-of-Truth Artefact Impact Check and Handover note for the Digital Governance & Strategy Coworker / Source-of-Truth Artefact Controller before or at DRB approval.

## Boundary Rules

Claude must not approve the development job.

Claude must not invent scope, milestones, activities, developer estimates, dependencies, or technical facts.

Claude must not assume the route is Implementation Route if the Initiative Type indicates a Development Route.

Claude must not assume Stage 2 is required for Development Route unless an exception trigger applies.

Claude must not skip the Stage 2 exception gate test before producing final outputs.

Claude must not include the blank Process Flow Capture Sheet as a final output.

Claude must not finalise the Completed Initiation Form without department confirmation of requirements (Section 1).

Claude must ask the Digital Lead to confirm the route if it is unclear before producing any outputs.
