# Automatic Hopper Clarification Handler

## Purpose

This file tells the Strateq DX CDO Coworker what to do when the Digital Lead submits Hopper Clarification data without a detailed prompt.

## Trigger

If the user provides any of the following, treat it as a Hopper Clarification submission:

- Jira Product Discovery export
- Hopper Clarification Form fields
- Jira idea fields from the Hopper view
- one populated initiative record
- one process cluster record
- meeting notes from a champion clarification session
- pasted table containing current problem, current process, future requirement, expected benefit, impacted systems, and priority/risk fields

The user does not need to provide a full task prompt.

## Default Action

When Hopper Clarification data is submitted, automatically produce:

1. Hopper Clarification Readout
2. Updated Hopper Consolidation Table
3. Priority Screen Readiness Assessment
4. Process Artifact Need Check
5. Source-of-Truth Artefact Impact
6. Follow-up Questions
7. Jira-ready Update Text
8. Next Physical Actions for the Digital Lead

## Route Classification at Intake

For every candidate item that reaches Priority Screen readiness, identify the likely route before producing the Hopper Consolidation Table.

Use the Route Classification table from `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`:

| Signal | Likely Route |
|---|---|
| Internal development (Chronos Dev, Omega Dev, SharePoint build, Power BI build, in-house tool) | Development Route → Stage 1D |
| Third-party implementation, supplier-led, SaaS onboarding, option appraisal, business case required | Implementation / Support Route → Stage 1 + Stage 2 |
| Unclear | Flag as TBC — ask Digital Lead before assigning route |

Record the Recommended Route in the Hopper Consolidation Table.

Do not load Stage 1D workflow rules unless the Digital Lead confirms a Development Route item is ready to proceed to Stage 1D.

## If Process Information Is Present

If the submission includes enough process detail to infer a workflow, also create a Draft Process Artifact Pack using:

`03_process_mapping/04_PROCESS_ARTIFACT_OUTPUT_MODEL.md`

If process detail is insufficient, do not invent a swimlane. Instead, list the exact missing process questions.

## Source-of-Truth Artefact Impact

For every Hopper Clarification output, apply:

`05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

Claude must identify which organisational digital artefacts are created, affected, missing, or require update.

At minimum, consider:

- A to Z enterprise process flow
- department process flow
- workflow / functionality-level process flow
- software ecosystem diagram
- software ecosystem register
- digital maturity register
- benchmark assessment archive
- integration register
- dashboard / reporting register
- process artefact register
- initiative register / Hopper history

## Required Rules

- Use exact controlled vocabulary from `00_system_control/CONTROLLED_VOCABULARY.md`.
- Hopper is light-touch priority screening only.
- Do not create Initiation Form content unless explicitly requested.
- Do not create Stage 1D content unless the Digital Lead confirms the route and requests it.
- Do not invent missing facts.
- Do not invent numeric scores.
- Treat Jira Score as source context only, not governed priority scoring.
- Treat champion priority input as first-pass input only, not DRB decision.
- BAU / Reject / Merge require Digital Lead confirmation.
- Process artefacts are draft until agreed by the Digital Lead and department/champion.
- Source-of-truth artefact updates are draft recommendations until confirmed by the Digital Lead.

## Default Output Structure

Use this structure unless the user asks otherwise:

1. Input Recognition
2. Hopper Consolidation Table
3. Priority Screen Readiness
4. Process Artifact Need Check
5. Source-of-Truth Artefact Impact
6. Follow-up Questions
7. Jira-ready Update Text
8. Next Physical Actions for Digital Lead

### Hopper Consolidation Table Format

| Item | Apparent Type | Duplicate / Related Items | Business Area | System / Process Link | Issue Clarity | Missing Basic Info | Recommended Route | Suggested Consolidation Outcome | Department Questions | Jira Update |
|---|---|---|---|---|---|---|---|---|---|---|

The Recommended Route column uses: `Development Route → Stage 1D`, `Implementation / Support Route → Stage 1 + Stage 2`, or `TBC`.

## Reminder Rule

If source-of-truth files have not been provided, remind the Digital Lead to upload or link the latest A to Z process flow, process maps, software ecosystem register, maturity register, benchmark assessment outputs, integration register, reporting register, and any current artefact register.

## Escalation Rule

If the user provides a single initiative with sufficient process detail, prioritise the Process Artifact Pack after the clarification readout.

If the user provides multiple initiatives, prioritise consolidation and readiness first, then identify which initiatives need process artefacts.
