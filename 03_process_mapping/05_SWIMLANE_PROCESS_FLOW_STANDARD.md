# Swimlane Process Flow Standard

## Purpose

This file defines the standard visual and export format for swimlane process flows created by the Strateq DX CDO Coworker.

## Target Look and Feel

The target format is a horizontal business swimlane diagram with:

- role or team lanes stacked vertically
- lane names shown on the left
- process moving primarily left to right
- rounded rectangles for activities
- document shapes for forms, reports, or generated outputs
- diamonds for decisions
- arrows showing sequence, handoff, and decision routes
- short labels on decision branches
- clean executive presentation suitable for business users

This should look like a professional process-flow diagram, not a raw markdown diagram.

## Core Rule

If an initiative changes how work is physically done, Claude must produce a draft swimlane process flow when enough process detail is available.

If enough process detail is not available, Claude must state that the swimlane cannot yet be drafted and list the missing process questions.

## Development Route Stage 1D Swimlane

For Development Route Stage 1D initiatives where Process Mapping Required = Yes and the Digital Lead has returned a completed Process Flow Capture Sheet, Claude must produce a draft swimlane process flow specification as a Stage 1D output.

This is not deferred to Stage 2 by default.

The swimlane specification must be produced from confirmed capture sheet data.

It remains DRAFT until confirmed by the Digital Lead and department / process owner.

If the completed capture sheet has not been returned, Claude must state that the swimlane cannot be drafted until the sheet is received and ask the Digital Lead to complete and upload it.

## Systems Are Not Lanes

Systems, platforms, and software applications must not be represented as swimlane lanes.

A swimlane lane represents a person, role, team, or accountable operational group that performs or owns a step.

The system used to perform a step must be recorded in the System column of the capture table or as a system touchpoint annotation on the relevant activity in the diagram.

Examples of what must not be swimlane lanes:

- Chronos (system)
- Kefron (system)
- Amazon S3 (storage service)
- any other named platform, application, integration, or automated system

If a step is automated or system-triggered with no human actor, place the step in the lane of the role or team responsible for the process area or system governance, and annotate it as a system action.

## Same-Person Role Consolidation

Where the Digital Lead confirms that two named roles are performed by the same person, Claude must consolidate them into one lane and one role column.

Claude must not maintain separate lanes for role titles confirmed to be one person.

This applies to:

- capture sheet RACI columns
- swimlane specification
- process step ownership
- Development Scope / Deliverables Brief
- Completed Initiation Form / DRB artefact role references

Example:
If “Materials Controller” and “Materials Coordinator” are confirmed as the same person, use one consolidated role:

Materials Controller / Coordinator

Claude must ask the Digital Lead to confirm role consolidation before applying it if it is not already stated in the session evidence.

## Required Outputs

For each process flow, produce:

1. Process scope statement
2. Lane / role table
3. Current-state swimlane, if current process is known
4. Future-state swimlane
5. Controls / approvals / evidence points
6. System touchpoints
7. Open process questions
8. Agreement status
9. Export instructions

## Lane / Role Table

Use this format:

| Lane | Role / Team | Responsibility in Process | Confirmed? |
|---|---|---|---|

## Preferred Editable Output

Preferred editable formats are:

1. diagrams.net / draw.io XML
2. Microsoft Visio VSDX if available through the user's tooling
3. PowerPoint PPTX process diagram
4. Excel workbook with process table and diagram reference

The minimum acceptable output is a structured swimlane table plus a visual diagram specification that can be recreated in diagrams.net, Visio, PowerPoint, or Excel.

## PDF Output

PDF is required for controlled sharing and sign-off, but PDF is not the editable master.

The editable master should be stored alongside the PDF.

Recommended storage pair:

- Editable master: .drawio or .vsdx or .pptx
- Read-only issue/DRB copy: .pdf

## Mermaid Use

Mermaid may be used only as a quick draft or technical intermediate.

Mermaid is not the preferred final business artefact because it does not match the required executive swimlane look and feel.

## Diagram Specification Output

Where Claude cannot directly generate an editable diagram file, it must produce a diagram build specification with:

- canvas orientation: landscape
- lane order
- lane colours
- step IDs
- step text
- shape type
- source lane
- target lane
- connector labels
- decision branches
- documents/forms/reports
- notes for manual adjustment

## Shape Standard

Use:

- Rounded rectangle: activity or status
- Diamond: decision
- Document shape: form, report, record, or generated document
- Database/cylinder if required: data store
- Annotation box: note, assumption, or open issue

## Table Fallback

If a visual file cannot be generated, provide this table:

| Step | Lane / Role | Activity | System | Input | Output | Shape | Next Step | Control / Evidence |
|---:|---|---|---|---|---|---|---|---|

## Current-State Swimlane

Only create current-state flow where the current process is known.

If the process is undefined, state:

Current-state process is not formally defined. Known current handling is described narratively only.

## Future-State Swimlane

Future-state flow should show the agreed or proposed operating process.

Where approval, evidence, or system control points exist, show them explicitly.

## Process Agreement Status

Every process flow must show one of:

- Draft - for department review
- Revised - after department feedback
- Agreed - confirmed by department/champion
- Superseded - replaced by later version

## Storage

Agreed process flows should be exported as PDF and stored with the editable master file in SharePoint or the agreed controlled file location. The Jira initiative must link to the stored artefact.

## Boundary

A process flow does not approve the initiative. It supports clarification, DRB review, initiation form development, vendor/developer scoping, and adoption planning.
