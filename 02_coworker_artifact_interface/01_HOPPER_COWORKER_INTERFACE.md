# Hopper Coworker Interface

## Purpose

This file defines the working interface between the AI coworker and the Digital Lead during Hopper consolidation and priority screening.

## Controlled Vocabulary

Use `00_system_control/CONTROLLED_VOCABULARY.md` for consolidation outcomes, DRB priority decisions, priority signal labels, and current Jira status labels.

## Governed Workflow Looping

Material governed sessions follow `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. The Hopper Portfolio Readiness Review (the leadership-readiness form of Stage 2 below) is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`; its default meeting surface is the Jira Initiative View / Hopper priority view (not a separate DRB Priority Screen document), it is pre-initiation and pre-Pack 1, and every such session must close with the full looping closeout. The Stage 1D Session Start Checklist and the Initiation Form stage starter checklist in Stage 3 below are receiving-stage spin-up artefacts, produced only after the Digital Lead confirms the route and triggers the stage. A closing stage states readiness only and does not produce next-stage plans or checklists.

## Standard Loop

```text
Digital Lead provides Hopper data
↓
AI produces structured artefact
↓
Digital Lead validates and engages people
↓
Digital Lead feeds back decisions / answers
↓
AI prepares Jira-ready updates and next-stage artefacts
```

## Stage 1: Hopper Consolidation

### Input from Digital Lead

- Jira export or pasted Hopper list
- known comments
- available qualitative priority information
- screenshots or attached notes where relevant

### AI Output

Hopper Consolidation Table:

| Item | Apparent Type | Duplicate / Related Items | Business Area | System / Process Link | Issue Clarity | Missing Basic Info | Recommended Route | Suggested Consolidation Outcome | Department Questions | Jira Update |
|---|---|---|---|---|---|---|---|---|---|---|

Recommended Route values: `Development Route → Stage 1D`, `Implementation / Support Route → Stage 1 + Stage 2`, or `TBC`.

### Digital Lead Physical Action

- confirm or reject merge suggestions
- confirm or correct the Recommended Route for each item
- ask departments light clarification questions
- route BAU/support noise after confirmation
- confirm which items are ready for Priority Screen

### Feedback Required

- confirmed route per item
- clarified facts
- owner/champion confirmation
- duplicates merged
- items ready for priority screen

## Stage 2: Hopper Priority Screen

### Input from Digital Lead

- cleaned candidate list
- qualitative priority information
- known business exposure
- known system/process impact

### AI Output

Hopper Priority Screen:

| Item | Request Type | Business Priority Signal | Maturity / System Link | Missing Basic Info | Recommended DRB Decision | Questions Before DRB | Jira Update |
|---|---|---|---|---|---|---|---|

### Digital Lead Physical Action

- validate output
- speak to relevant stakeholders where needed
- take ready items to DRB

### Feedback Required

- DRB decision
- decision date
- conditions
- owner/sponsor/champion updates
- next status

## Stage 3: Handoff by Route

After DRB priority approval, route each item to the correct initiation stage.

### Development Route → Stage 1D

For items confirmed as internal development (Chronos Dev, Omega Dev, SharePoint build, Power BI build, in-house tool).

Governed by: `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`

**AI Output**

- Jira update text (route confirmed, Stage 1D In Progress)
- Stage 1D Session Start Checklist
- route confirmation note
- Stage 2 exception gate pre-check (flag any known triggers)

**Digital Lead Physical Action**

- update Jira status to Stage 1D In Progress
- confirm route
- supply required inputs listed in Stage 1D Session Start Checklist
- flag any known exception gate triggers before session begins

### Implementation / Support Route → Stage 1 + Stage 2

For items confirmed as third-party implementation, supplier-led, SaaS onboarding, option appraisal, or business case routes.

Governed by: `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`

**AI Output**

- Jira update text (route confirmed, Initiation Form In Progress)
- Initiation Form stage starter checklist
- route recommendation
- supporting artefact checklist

**Digital Lead Physical Action**

- update Jira
- start the correct initiation form
- arrange process mapping if required
- engage vendor/developer if required
