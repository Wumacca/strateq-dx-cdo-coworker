# Hopper Coworker Interface

## Purpose

This file defines the working interface between the AI coworker and the Digital Lead during Hopper consolidation and priority screening.

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
- available scores
- screenshots or attached notes where relevant

### AI Output

Hopper Consolidation Table:

| Item | Apparent Type | Duplicate / Related Items | Business Area | System / Process Link | Issue Clarity | Missing Basic Info | Suggested Outcome | Department Questions | Jira Update |
|---|---|---|---|---|---|---|---|---|---|

### Digital Lead Physical Action

- confirm or reject merge suggestions
- ask departments light clarification questions
- remove BAU/support noise
- confirm which items are ready for Priority Screen

### Feedback Required

- confirmed route
- clarified facts
- owner/champion confirmation
- duplicates merged
- items ready for priority screen

## Stage 2: Hopper Priority Screen

### Input from Digital Lead

- cleaned candidate list
- light priority scores
- known business exposure
- known system/process impact

### AI Output

Hopper Priority Screen:

| Item | Request Type | Business Priority Signal | Maturity / System Link | Missing Basic Info | Recommended DRB Decision | Questions Before DRB | Jira Update |
|---|---|---|---|---|---|---|

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

## Stage 3: Handoff to Initiation Form

### AI Output

- Jira update text
- initiation form starter checklist
- route recommendation
- supporting artefact checklist

### Digital Lead Physical Action

- update Jira
- start the correct initiation form
- arrange process mapping if required
- engage vendor/developer if required
