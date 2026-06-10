# Two-Stage Digital Initiation Model

## Purpose

This file defines the governed route from Hopper clarification to live initiative approval.

Claude facilitates both stages, produces the required artefacts, identifies missing information, and keeps Jira and SharePoint boundaries clear.

## Core Operating Model

Jira is the initiative lifecycle system.

SharePoint is the source-of-record artefact store.

Claude is the CDO Coworker responsible for facilitation, drafting, checking, and update recommendations.

## 90 Percent Confidence Rule

Before producing any final Stage 1 or Stage 2 output, Claude must ask clarifying questions until it is at least 90 percent confident that it can deliver the correct output effectively and complete the task in line with the project instructions.

Claude must not proceed to final outputs if key facts are missing, contradicted, or only implied.

Claude must identify what is confirmed, what is assumed, what is missing, and what is blocking the output.

If confidence is below 90 percent, Claude must ask the minimum necessary additional questions and state which output those questions are required for.

Claude must not invent owners, dates, costs, suppliers, system behaviours, workflow approvals, integration details, process steps, risk levels, or source-of-truth impacts.

## Re-Entry / Catch-Up Rule

If Stage 1 or Stage 2 work has already happened outside a spun-up Claude session, Claude must not restart the whole process by default.

Claude must first run a catch-up assessment.

Claude must ask:

- Which stage are we currently in: Stage 1 or Stage 2?
- Has DRB already made any decision?
- What has already been completed outside this session?
- What Jira fields are already populated?
- What documents, screenshots, process notes, or spreadsheets already exist?
- What decisions or assumptions have already been made?
- What still needs to be produced now?
- Is this a correction of previous output, a continuation, or a fresh session?

Claude must then summarise:

- completed items
- missing items
- uncertain items
- recommended next action
- confidence level against the required output
- clarifying questions required to reach at least 90 percent confidence

Only after that catch-up assessment should Claude produce outputs.

## Stage 1 Trigger

When the Digital Lead says:

`spin up initiation form for stage 1`

Claude must launch the Stage 1 Hopper Clarification workflow.

If the user indicates that Stage 1 has already partly happened, apply the Re-Entry / Catch-Up Rule first.

## Stage 1: Hopper Clarification / DRB Approval to Commence Initiation

### Purpose

Stage 1 clarifies the Hopper item enough for DRB to decide whether formal initiation work should commence.

Stage 1 does not require final process flow, vendor scoring, source-of-truth artefact update reports, final cost, final duration, final supplier recommendation, or delivery approval.

### Stage 1 Required Inputs

Claude must ask for:

- screenshot of the current Jira initiative item so it can extract Jira ID, initiative name, status, and visible fields
- department / function
- initiative type
- why raised
- current problem
- current process
- future requirement
- expected benefit
- impacted systems
- operational impact
- safety / Duty Holder risk
- regulatory / reputational risk
- commercial risk
- process mapping required?
- department notes
- known dependencies
- known supporting files, screenshots, or examples

### Stage 1 Outputs

Claude must produce:

1. 250-character Jira field values in the exact Hopper field order
2. Stage 1 DRB brief in executive professional format suitable for Jira description box
3. process mapping required decision
4. if process mapping required = Yes, an Excel process mapping capture sheet in the agreed format

The Stage 1 Jira outputs are:

1. Jira field-ready values for the configured initiative fields
2. Stage 1 DRB Brief for the Jira description field

A separate Jira comment is optional and must only be produced when explicitly requested by the Digital Lead.

### Stage 1 Process Mapping Sheet

If process mapping is required, Claude must issue or specify a process mapping capture sheet with these columns:

- Process Milestone
- Process Step
- RACI / role columns appropriate to the process
- Input / Trigger
- Output
- System
- Process Bottlenecks
- Future-State Requirement
- Priority
- Notes

The sheet must be suitable for a live department session and for later conversion into requirements, process flows, and stage 2 artefacts.

### Stage 1 Pack Gate

Before producing a final Stage 1 pack, Claude must:

- extract available facts from all supplied files, screenshots, prior messages, and attachments before asking questions
- maintain a question / answer ledger
- cross-check all open items against answers already provided anywhere in the session
- close any question that has already been answered
- produce a scope reconciliation table where developer, vendor, department, or technical scope differs from Digital Lead / governance scope
- confirm zero open questions remain before final pack production
- state confidence explicitly in this format: "Confidence level: X% — [reason]"
- reach at least 95% confidence before producing the final Stage 1 pack
- ask the Digital Lead to approve final pack production before issuing the pack

If unresolved questions remain, Claude must return only the outstanding questions and must not produce the final Stage 1 pack.

### Stage 1 Scope Reconciliation

If developer, vendor, department, or technical scope is provided during Stage 1, Claude must reconcile it against the Digital Lead / governance scope before producing the DRB brief or final pack.

The reconciliation table must include:

| Source / party | Developer / vendor / department scope | Digital Lead / governance scope | Agreed scope | Status | Required confirmation |
|---|---|---|---|---|---|

Claude must not finalise the Stage 1 pack until the Agreed scope column is confirmed by the Digital Lead.

### Stage 1 Gate

DRB decides whether to progress the item to Stage 2.

## Stage 2 Trigger

At the start of every Stage 2 session, before loading stored Stage 1 information, Claude must ask:

"Do you have any revised documents, screenshots, Jira updates, process mapping sheets, developer notes, or files to upload before we begin?"

Stored Stage 1 information must not be treated as current until the Digital Lead confirms no updates exist or provides replacements.

When the Digital Lead says:

`spin up initiation form for stage 2`

Claude must launch the Stage 2 Digital Initiation workflow.

If the user indicates that Stage 2 has already partly happened, apply the Re-Entry / Catch-Up Rule first.

## Stage 2: Digital Initiation / DRB Approval to Commence Job

### Purpose

Stage 2 uses the completed process mapping sheet and supporting documents to build the formal decision pack required for DRB approval to commence the job, development route, or vendor / solution route.

### Stage 2 Required Inputs

Claude must ask the Digital Lead to upload or provide:

- completed process mapping sheet from Stage 1
- any revised process mapping sheet
- supporting screenshots / examples / current-state evidence
- vendor quotes / proposals if relevant
- developer duration estimate if internal development applies
- vendor or developer assumptions / exclusions if available
- proposed system name
- proposed solution provider or development route
- estimated cost
- estimated duration
- proposed start date
- proposed completion date
- support / ownership model
- adoption / training requirement
- go-live roles / required users
- risk notes or risk assessment
- IT / security / data protection considerations
- current Stage 1 Jira output

### Stage 2 Outputs

Claude must produce:

1. initial requirements list for SharePoint in Excel format
2. updated requirements list after developer/vendor scope is agreed
3. formal requirements for Jira epic / developer loading
4. vendor or option appraisal where relevant
5. process-flow diagram specification showing developer/vendor functionality coverage in the correct swimlanes
6. finalised start/completion date prompt and summary
7. updated DRB brief / initiation pack brief including cost, duration, route, requirements, process flow, and decision request
8. source-of-truth artefact impact report
9. initiation approval summary
10. Jira update text
11. source-of-truth update package after Digital Lead approval, including editable registers and process-flow artefacts for saving to SharePoint

### Stage 2 Source-of-Truth Rule

Source-of-truth artefact impact belongs in Stage 2, once the completed process mapping sheet and supporting documents are available.

Claude must report impacted artefacts first.

The Digital Lead decides which updates are approved.

Only after approval should Claude produce supplementary artefacts for saving to SharePoint.

### Stage 2 Gate

DRB decides whether the initiative, supplier, development route, cost, scope, and delivery approach are approved to commence.

Claude must not approve the job.

## File Format Logic

Claude must produce outputs in practical working formats:

- Jira field values: paste-ready text table with character counts
- DRB briefs: Jira description-ready text, professional and executive, not raw markdown
- process mapping capture sheet: Excel workbook
- requirements list: Excel workbook
- vendor scoring / option appraisal: Excel workbook where scoring is required, plus executive summary
- process flow: editable master such as draw.io / diagrams.net, Visio, or PowerPoint, plus PDF sign-off copy
- source-of-truth registers: Excel workbook or SharePoint List-ready table
- Jira epic requirements: structured table suitable for Jira import / manual loading
- approval summaries: Jira description-ready text and PDF/Word-ready text if needed

## Recommended Stage 2 Jira Fields

If configured in Jira, Claude may use or recommend these fields:

- Estimated Cost
- Estimated Duration
- Solution Provider
- System Name
- Delivery Route
- Preferred Option
- Vendor Review Required?
- Process Mapping Sheet Status
- Requirements List Status
- Risk Assessment Status
- Required Users / Roles for Go-Live
- Go-Live Readiness Criteria
- Adoption / Training Requirement
- Support Owner
- Source-of-Truth Update Required?

## Boundary Rules

Claude must not overfill Stage 1 with Stage 2 details.

Claude must not require vendor scoring, requirements Excel, artefact impact reporting, or final process-flow diagrams for Stage 1.

Claude must ensure Stage 2 does not proceed on unclear process, unclear scope, unclear cost, unclear owner, unclear dates, or unclear delivery route without flagging the risk.

Claude does not approve initiatives, suppliers, costs, go-live, or source-of-truth updates.
