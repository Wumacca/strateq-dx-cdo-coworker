# Controlled Vocabulary

## Purpose

This file defines the canonical vocabulary for the current Hopper-to-Initiation workflow.

Claude must use these exact labels when drafting Hopper consolidation outputs, Priority Screens, DRB briefs, and Jira-ready text.

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
- Implementation / Support Route
- TBC

"Hybrid route" is not an approved route label and must not be used as an active route classification.

> **Route-vocabulary split dependency.** Splitting the combined `Implementation / Support Route` label into separate `Implementation Route` and `Support Route` labels is owned by the initiation-form-route-hardening workstream and is not performed here. `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` describes provisional Implementation Route and Support Route closeout behaviour that must be reconciled with these controlled labels once that split lands.

## Stage Closeout Naming

Stage closeout lines and stage naming must be route-correct and derived from this vocabulary and `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`. Do not invent generic "Stage 1 / Stage 2" wording. The canonical closeout paths and lines are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. For a Development Route initiative with no Stage 2 exception, the closeout line is: `Stage 1D is closed. Ready for Live Delivery spin-up.`
