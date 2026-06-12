# Hopper Coworker Interface

## Purpose

This file defines the working interface between the AI coworker and the Digital Lead during Hopper consolidation and priority screening.

## Controlled Vocabulary

Use `00_system_control/CONTROLLED_VOCABULARY.md` for consolidation outcomes, DRB priority decisions, priority signal labels, approved route labels, and current Jira status labels.

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

Recommended Route values: `Development Route → Stage 1D`, `Implementation Route → Stage 1 + Stage 2`, `Support Route`, or `TBC`.

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

Governed by: `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`

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

### Implementation Route → Stage 1 + Stage 2

For items confirmed as third-party implementation, supplier-led, SaaS onboarding, option appraisal, or business case routes.

Governed by: `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`

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

### Support Route

For items confirmed as minor BAU support, system fixes, or operational assistance that does not justify Initiation Form governance.

Governed by: `01_governance_lifecycle/05_ROUTE_RULES.md`

**AI Output**

- Jira update text (route confirmed, BAU Support)
- proportionate support note
- confirmation that Stage 1D and Stage 1 governance do not apply

**Digital Lead Physical Action**

- update Jira status to BAU Support after Digital Lead confirmation
- route to the appropriate support team or BAU tracking mechanism
