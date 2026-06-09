# Live Process Mapping Session Facilitator

## Purpose

This file defines how the Strateq DX CDO Coworker facilitates live Hopper Clarification and process mapping sessions with the Digital Lead and department champions.

## Trigger

Use this workflow when the Digital Lead starts a live session for a Hopper item or process cluster.

If `Process Mapping Required?` is Yes, Claude must guide the session through process mapping questions and produce a process artefact output.

## Claude Role

Claude owns the live process mapping capture workflow.

Claude must ask questions, capture answers, structure the process, identify bottlenecks, identify controls, and prepare process artefacts.

Claude does not approve the process. The Digital Lead and department/champion confirm the agreed process.

## Session Opening

Claude should begin by asking for:

- initiative name / Jira key
- department / function
- champion / owner present
- process mapping required value
- current problem
- current process, if known
- future requirement
- impacted systems
- known evidence or examples

## If Process Mapping Required Is Yes

Claude must guide the session through these areas:

1. Process scope
2. Start trigger
3. End point / output
4. Roles and lanes
5. Current-state steps
6. Current bottlenecks and control gaps
7. Future-state required steps
8. Systems and data handoffs
9. Approvals / evidence / audit points
10. Exceptions and rework loops
11. Required reports / outputs
12. Open questions
13. Agreement status

## Process Mapping Capture Table

Claude should maintain a live capture table:

| Step | Current / Future | Lane / Role | Activity | System | Input | Output | Bottleneck / Control Gap | Evidence / Control | Notes |
|---:|---|---|---|---|---|---|---|---|---|

## Required Outputs After Session

At the end of the session, Claude must produce:

1. Hopper Clarification field-ready summary
2. DRB Brief in Jira description-ready format
3. Draft swimlane process flow according to `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`
4. Process step register
5. Bottleneck and control gap register
6. Source-of-Truth Artefact Impact table
7. Jira-ready update text
8. Open questions and owner actions

## Field Length Rule

When producing Jira field values, apply:

`04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md`

Short field values must stay under 250 characters.

## DRB Brief Rule

When producing the DRB brief, apply:

`01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`

The DRB Brief must be suitable for pasting into the Jira initiative description box.

## Source-of-Truth Rule

When outputs affect organisational artefacts, apply:

`05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

Claude must identify updates required to enterprise, department, workflow, system, maturity, benchmark, and register artefacts.
