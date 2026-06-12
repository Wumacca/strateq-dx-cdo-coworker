# Controlled Vocabulary

## Purpose

This file defines the canonical vocabulary for the current Hopper-to-Initiation workflow.

Claude must use these exact labels when drafting Hopper consolidation outputs, Priority Screens, initiation forms, and Jira-ready text.

## Canonical DRB Priority Decisions

Use these exact labels:

- Progress to Initiation Form
- Clarify Before Progression
- Merge / Duplicate
- Defer
- Reject
- Move to BAU Support
- Hold for Future Review

Do not invent variants.

## Canonical Consolidation Outcomes

Use these exact labels:

- Ready for Priority Screen
- Clarify with Department
- Merge / Duplicate
- Move to BAU Support
- Hold for Future Review
- Reject

## Business Priority Signal

Use these exact labels:

- High
- Medium
- Low
- Unclear

Each signal must include a short reason.

The signal is qualitative only.

Claude must not invent numeric scores, weightings, or a 1-5 scale.

Scored fields in `01_governance_lifecycle/00_REQUEST_INTAKE_MODEL_FUTURE.md` are future scope and are not used in current Hopper screening.

## Approved Jira Statuses: Current Workflow

Use these current workflow labels unless the Digital Lead provides the actual Jira status names:

- Hopper - Unscreened
- Hopper - Clarify
- Ready for Priority Screen
- At DRB
- Initiation Form In Progress
- BAU Support
- Deferred
- Rejected
- Merged

## Confirmation Rule

BAU, Reject, and Merge are AI recommendations only.

The Digital Lead confirms before any Jira status change, item removal, or merge action.

## Approved Jira Statuses: Stage 1D

Use this current workflow label for Development Route Stage 1D work:

- Stage 1D In Progress

## Approved Route Labels

Use these exact labels when classifying initiative route:

- Development Route
- Implementation Route
- Support Route
- TBC

Do not use "Implementation / Support Route" as a combined label in new artefacts.

## Approved Initiation Artefact Terms

Use these exact terms for the formal DRB approval artefact and related outputs:

- Completed Initiation Form (formal DRB approval artefact for all governed routes)
- Development Scope / Deliverables Brief (Development Route scoping artefact)
- Jira Initiation Summary / Delivery Context (Jira description field output for all routes)

Do not use "DRB Brief" as the name of the final approval pack or formal DRB approval artefact.

## Retained DRB Terms

These DRB-related terms remain valid and must not be deprecated:

- DRB (Digital Review Board)
- DRB meeting
- DRB approval
- DRB decision
- DRB priority decision
- Priority Discussion Note
- DRB approval status

## Deprecated Terms

The following terms are deprecated and must not be used in new artefacts:

- DRB Brief (as a final pack deliverable or formal approval document — replaced by Completed Initiation Form)
- Pack 1 (replaced by Development Route Final Outputs or Stage 1 outputs as applicable)
- Implementation / Support Route (replaced by Implementation Route and Support Route as separate labels)
