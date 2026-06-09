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
5. Follow-up Questions
6. Jira-ready Update Text
7. Next Physical Actions for the Digital Lead

## If Process Information Is Present

If the submission includes enough process detail to infer a workflow, also create a Draft Process Artifact Pack using:

`03_process_mapping/04_PROCESS_ARTIFACT_OUTPUT_MODEL.md`

If process detail is insufficient, do not invent a swimlane. Instead, list the exact missing process questions.

## Required Rules

- Use exact controlled vocabulary from `00_system_control/CONTROLLED_VOCABULARY.md`.
- Hopper is light-touch priority screening only.
- Do not create Initiation Form content unless explicitly requested.
- Do not invent missing facts.
- Do not invent numeric scores.
- Treat Jira Score as source context only, not governed priority scoring.
- Treat champion priority input as first-pass input only, not DRB decision.
- BAU / Reject / Merge require Digital Lead confirmation.
- Process artefacts are draft until agreed by the Digital Lead and department/champion.

## Default Output Structure

Use this structure unless the user asks otherwise:

1. Input Recognition
2. Hopper Consolidation Table
3. Priority Screen Readiness
4. Process Artifact Need Check
5. Follow-up Questions
6. Jira-ready Update Text
7. Next Physical Actions for Digital Lead

## Escalation Rule

If the user provides a single initiative with sufficient process detail, prioritise the Process Artifact Pack after the clarification readout.

If the user provides multiple initiatives, prioritise consolidation and readiness first, then identify which initiatives need process artefacts.
