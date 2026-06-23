# Controlled Vocabulary

## Purpose

This file defines the canonical vocabulary for the current Hopper-to-Initiation workflow.

Claude must use these exact labels when drafting Hopper consolidation outputs, Priority Screens, Jira-ready text, and optional DRB meeting-support text where explicitly requested by the Digital Lead. DRB Brief is not a default or final Hopper review artefact.

## Canonical DRB Priority Decisions

Use these exact labels:

- Progress to Approved Route Trigger
- Clarify Before Progression
- Merge / Duplicate
- Defer
- Reject
- Move to BAU Support
- Hold for Future Review

**Progress to Approved Route Trigger** — approved by leadership / DRB to move to the next route-correct stage: Pack 1 / Stage 1D for Development Epics, Initiation Form / Implementation Route for Implementation items, selection/support route for Support items, or existing delivery control for in-flight items.

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

Claude must not invent numeric scores, weightings, or a 1–5 scale. Where a Digital Lead-approved scoring model, team-returned charter score, or Jira-entered score exists, Claude may organise, display, summarise, and challenge the score, but must not create or alter scores without Digital Lead approval.

Scored fields in future request-intake models do not authorise Claude to create scores. Current Hopper review scoring may use Digital Lead-approved, team-returned, or Jira-entered scores only.

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

## Hopper Portfolio Readiness Review Terminology

The full Hopper Portfolio Readiness Review workflow is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. Use these defined terms:

- **Hopper Portfolio Readiness Review** — the pre-initiation, pre-Pack 1 review that organises minimum meeting information and scores so the Hopper is ready for a leadership / DRB priority discussion.
- **Jira Initiative View / Hopper priority view** — the organised Hopper / Initiative View screens in Jira / Jira Product Discovery. This is the **default meeting surface** for the leadership / DRB priority discussion. The term "Priority Screen" means this view unless the Digital Lead explicitly requests a separate artefact. A separate DRB Priority Screen document is **not** produced by default.
- **Development Epic** — a Chronos Dev, Omega Dev, CRM Dev, or equivalent build on an existing THREE60-owned platform. May use a department charter for detail / scoring. After approval, routes to Pack 1 / Stage 1D.
- **Grouped Initiative** — an implementation or support item grouped for leadership review. Not called an epic unless it is a development route. No charter by default.
- **Initiative Charter** — a pre-initiation input tool only. Gathers business reason, sub-task detail, deliverables / expected benefit, current method, and department priority score input. A charter is **not** an Initiation Form and does not approve or commit anything.
- **Implementation Route** (Hopper-review treatment term) — the tool / system exists or the route is sufficiently known; after approval, routes to Initiation Form / Implementation Route.
- **Support Route** (Hopper-review treatment term) — the tool does not yet exist or the solution route is not selected; the team needs Digital support to select then implement.
- **In-flight item** — an item already under initiation, delivery, adoption, or support control. Visible in the Hopper review but not regrouped as new backlog work unless the Digital Lead confirms.
- **Controlled update recommendation** — a proposed change to a controlled record (Jira, SharePoint, GitHub, Hopper, source-of-truth) that requires Digital Lead approval before it is applied.
- **Report-only recommendation** — an advisory output (CDO QA / self-improvement, knowledge capture, Jira / Hopper update, source-of-truth update) that must not automatically change any controlled record.

> **Hopper-review treatment vs active route classification.** "Implementation Route" and "Support Route" above are Hopper-review treatment / route-indication terms. They do **not** split or replace the active controlled route classification label `Implementation / Support Route` in the Approved Route Labels section. The formal split of that label is owned by the initiation-form-route-hardening workstream and is not performed here.

## Stage Closeout Naming

Stage closeout lines and stage naming must be route-correct and derived from this vocabulary and `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`. Do not invent generic "Stage 1 / Stage 2" wording. The canonical closeout paths and lines are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. For a Development Route initiative with no Stage 2 exception, the closeout line is: `Stage 1D is closed. Ready for Live Delivery spin-up.`
