# Development Route Stage 1D Model

## Purpose

This file defines the governed route for internal development initiatives through Development Stage 1D.

Internal development initiatives — such as Chronos, Omega, SharePoint internal builds, Power BI internal builds, or other in-house tools — may be approved to commence the live development job from a strengthened Development Stage 1D Pack, without requiring the full two-stage initiation route.

Stage 2 must still be triggered where complexity, external supplier involvement, cost, security, architecture, immature scope, or DRB requirements demand deeper initiation.

Development Route model: Stage 1D only, unless a Stage 2 exception trigger applies.

Implementation / Support Route model: Stage 1 + Stage 2, governed by `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

## Route Classification

Before launching any session, Claude must classify the initiative route from the Jira screenshot or Initiative Type field.

### Development Route examples

- Chronos Dev
- Omega Dev
- SharePoint internal build
- Power BI internal build
- any other in-house development tool or internal platform enhancement

### Implementation / Support Route examples

- third-party implementation
- supplier-led support request
- external platform implementation
- option appraisal / quote comparison route
- business case / funding route

If the route is unclear, Claude must ask the Digital Lead before producing any outputs.

If the Initiative Type is clearly a Development Route, Claude must load and apply this file as the primary governing file, not `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

## Stage 1D Trigger

When the Digital Lead says `spin up stage 1 session` and the initiative is a Development Route, Claude must:

1. Confirm the route is Development Route.
2. Immediately produce the Development Stage 1D Session Start Checklist.
3. Run the Stage 1D session under this file.

Do not apply the Stage 1 Hopper Clarification workflow from `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` to a Development Route initiative unless the Stage 2 exception gate is triggered.

## Development Stage 1D Session Start Checklist

At the opening of every Stage 1D session, Claude must produce this checklist for the Digital Lead.

### A. Session Objective

Confirm whether Pack 1 (the Development Stage 1D Pack) is sufficient to seek DRB approval to commence the live development job, or whether Stage 2 is required before approval.

### B. Required Documentation and Attachments

Claude must ask the Digital Lead to provide or confirm the following:

- Jira screenshot / field export
- Initiative Type screenshot / value (confirming Development Route)
- Existing scope notes
- Current process notes
- Process steps, if known
- Bottlenecks / control gaps
- Required enhancements
- Screenshots of current system or proposed screen
- Developer notes / estimate / task breakdown
- Department-provided scope
- Rejected workaround / client requirement evidence if applicable
- Dependency items or linked initiatives
- Target date / internal deadline
- Known exclusions
- Process Flow Capture Sheet (blank workbook, issued by Claude if process mapping is required or likely required — see Section C)

### C. Process Flow Capture Sheet

The Process Flow Capture Sheet is a session input tool, not a pack deliverable.

If process steps are missing or incomplete and process mapping is required or likely required, Claude must issue the blank single-sheet Process Flow Capture Sheet to the Digital Lead at session opening. The Digital Lead completes the sheet and uploads it. Claude then reads the completed sheet and produces the governed Stage 1D outputs from that data.

If process steps are already provided in session documents, notes, or prior uploads, Claude may work from those directly without requiring the capture sheet to be completed separately.

Once the completed sheet is returned, Claude must produce:

- process flow swimlane specification (see Stage 1D Pack Deliverables)
- Jira scope structure items
- requirements / scope items
- process bottlenecks and required enhancements
- DRB-ready process summary

The Process Flow Capture Sheet must be a single-sheet workbook.

It must not include Stage 2 handover tabs, requirements tabs, source-of-truth impact tabs, risk registers, or approval summaries.

Required capture columns:

| Process Milestone | Process Step | RACI / role columns | Input / Trigger | Output | System | Process Bottlenecks | Future-State Requirement | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|

### D. Question Ledger

Claude must produce a question ledger covering all information required to reach 95% confidence before pack production.

| # | Question | Source / evidence | Status | Answer |
|---|---|---|---|---------|

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
- Department-provided scope (if available)
- Known exclusions
- Dependencies and linked initiatives
- Target date / internal deadline
- Safety / Duty Holder risk
- Regulatory / reputational risk
- Commercial risk
- Operational impact
- Process Mapping Required?

## Development Stage 1D Pack Deliverables

Claude must produce:

1. Jira field-ready values for the configured initiative fields (250-character limit per `04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md`)
2. DRB Brief — Development Approval variant (using `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`)
3. Scope Brief (see Scope Brief section below)
4. Process flow swimlane specification — produced from the completed Process Flow Capture Sheet where Process Mapping Required = Yes. The Digital Lead must have returned the completed capture sheet before Claude produces the swimlane. Apply `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` and `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md`.
5. Source-of-truth artefact impact check and handover note — required where the initiative affects process flows, registers, ecosystem diagrams, integration records, maturity records, governance artefacts, or other controlled documentation. See Source-of-Truth Artefact Impact Check and Handover section below. Apply `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.

A separate Jira comment is optional and must only be produced when explicitly requested by the Digital Lead.

The Process Flow Capture Sheet is a session input tool, not a pack deliverable. Claude must not include the blank or completed capture sheet as a final Stage 1D Pack output.

Detailed diagram specifications, process step registers, and bottleneck registers beyond the swimlane specification are not default Stage 1D deliverables unless the Digital Lead explicitly requests them.

## Scope Brief

The Scope Brief is a formal deliverable of the Development Stage 1D Pack.

### Scope Brief Required Content

- Initiative / Epic level summary
- Development objective
- Confirmed scope
- Known exclusions
- Milestones / task-level build areas
- Activities / subtask-level detail where known and provided
- Process bottlenecks
- Required enhancements
- Developer estimate / duration where provided
- Dependencies
- Acceptance / completion expectations
- Items explicitly not to be built
- Stage 2 exception gate decision

### Scope Brief Hierarchy Rule

| Level | Jira equivalent | When to include |
|---|---|---|
| Initiative | Epic | Always |
| Milestones | Tasks | Always where known |
| Activities | Subtasks | Only where explicitly provided |

Claude must not invent subtasks, milestones, or developer estimates.

If activity-level detail is not furnished, task-level milestones are sufficient.

## Stage 2 Exception Gate

Before producing the final Development Stage 1D Pack, Claude must ask:

"Based on the current evidence, are you happy for Pack 1 to be used to seek DRB approval to commence the live job, or is a more detailed Stage 2 required before approval?"

Claude must explicitly test these exception triggers:

- Third-party supplier selection is required
- Quotes / options must be compared
- Business case or funding approval is required
- Material cost approval is needed
- Technical architecture is uncertain
- Security / data / integration risk is high
- Development scope is too immature for approval
- DRB requests or is likely to require further initiation detail

If any exception trigger applies, Claude must recommend Stage 2 before live job approval.

Claude must not suppress or downplay a trigger to avoid Stage 2.

If no exception trigger applies and the Digital Lead confirms Pack 1 is sufficient, Claude may proceed to final pack production once all questions are answered and confidence is at least 95%.

## Stage 1D Pack Gate

Claude must not produce the final Development Stage 1D Pack until:

- all blocking questions are answered, excluded, or explicitly deferred outside the approval decision
- the process flow capture requirement is resolved (blank sheet issued and completed sheet returned by the Digital Lead, or process mapping confirmed not required)
- developer / department scope has been reconciled if provided (see Scope Reconciliation below)
- the Stage 2 exception gate has been answered
- Claude has cross-checked the question ledger against all session evidence
- Claude reaches at least 95% confidence
- the Digital Lead explicitly approves pack production

If confidence is below 95%, Claude must return only:

- missing uploads
- outstanding questions
- assumptions requiring approval
- what blocks pack production

Claude must state confidence in this format: "Confidence level: X% — [reason]"

## Scope Reconciliation

If developer, department, or technical scope is provided during Stage 1D, Claude must reconcile it against the Digital Lead / governance scope before producing the DRB Brief or final pack.

| Source / party | Developer / department scope | Digital Lead / governance scope | Agreed scope | Status | Required confirmation |
|---|---|---|---|---|---|

Claude must not finalise the Stage 1D Pack until the Agreed scope column is confirmed by the Digital Lead.

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
- Jira key
- initiative name
- lifecycle status
- decisions already made
- decisions still required
- approved scope
- out of scope
- impacted artefacts
- required updates
- timing
- assumed or known SharePoint location
- Jira link / reference
- known risks / constraints
- open questions for receiving coworker
- files or outputs the receiving coworker must inspect
- required next action

The handover must be generated before or at DRB approval where artefact impacts are known, and updated after go-live where final artefact updates depend on delivery completion.

Apply `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` when producing this section.

## Stage 1D to Stage 2 Exception Route

If any Stage 2 exception trigger applies, Claude must:

1. State clearly which trigger applies.
2. Recommend Stage 2 initiation before live job approval.
3. Begin a Stage 2 session under `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.
4. Not produce a Pack 1 approval brief in place of Stage 2.

## Stage 1D to Live Development (No Exception)

If no Stage 2 exception trigger applies and the Digital Lead confirms Pack 1 is sufficient:

1. Claude produces the final Development Stage 1D Pack.
2. The Digital Lead takes the pack to DRB for approval to commence the live development job.
3. On DRB approval, a Stage 1D closeout / Live Delivery handover checkpoint is required under `00_system_control/04_COWORKER_HANDOVER_MODEL.md`.
4. Where the initiative affects controlled artefacts, Claude must produce a Source-of-Truth Artefact Impact Check and Handover note for the Digital Governance & Strategy Coworker / Source-of-Truth Artefact Controller before or at DRB approval.

## Boundary Rules

Claude must not approve the development job.

Claude must not invent scope, milestones, activities, developer estimates, dependencies, or technical facts.

Claude must not assume the route is Implementation / Support if the Initiative Type indicates a Development Route.

Claude must not assume Stage 2 is required for Development Route unless an exception trigger applies.

Claude must not skip the Stage 2 exception gate test before producing the final pack.

Claude must not include the blank Process Flow Capture Sheet as a final Stage 1D Pack deliverable.

Claude must ask the Digital Lead to confirm the route if it is unclear before producing any outputs.
