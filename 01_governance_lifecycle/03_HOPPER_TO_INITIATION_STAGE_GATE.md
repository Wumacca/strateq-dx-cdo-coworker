# Hopper to Initiation Stage Gate

## Purpose

This file defines the governed handoff from Hopper Priority Screen into Initiation Form stage.

The stage gate prevents lightly screened ideas from moving into delivery without formal due diligence.

## Core Rule

A Hopper item can only enter Initiation Form stage after a DRB priority decision confirms that formal due diligence is justified.

## Stage Gate Flow

```text
Hopper Priority Screen
↓
DRB priority discussion
↓
DRB decision recorded
↓
If approved: Initiation Form stage begins
↓
Route selected: Implementation or Development
```

## Valid DRB Priority Decisions

| Decision | Next Action |
|---|---|
| Progress to Initiation Form | Start Initiation Form stage |
| Clarify Before Progression | Gather targeted answers and return to DRB or delegated reviewer |
| Merge / Duplicate | Link or consolidate in Jira |
| Defer | Record reason and review window |
| Reject | Record reason and close / remove from active Hopper |
| Move to BAU Support | Route to support workflow |
| Hold for Future Review | Keep visible but out of current programme |

## Required Record Before Progression

Before moving to Initiation Form stage, Jira should show:

- DRB priority decision
- decision date
- route condition, if known
- sponsor / owner if known
- department / digital champion if known
- whether process mapping is likely required
- whether vendor/developer engagement is likely required

## What Must Not Happen

Do not:

- start PEP / Development Execution directly from Hopper
- treat Priority Screen as approved business case
- request full delivery mobilisation before initiation approval
- treat unclear ownership as acceptable for progression
- move BAU support into Initiation Form

## AI Coworker Role

AI may produce:

- DRB decision summary
- Jira update text
- Initiation Form stage starter checklist
- route recommendation: Implementation / Development / unclear
- missing information list
- department / vendor / developer question list

AI must not approve the stage gate.

## Jira Update Template

```markdown
DRB priority decision recorded.

Decision: [Progress / Clarify / Defer / Reject / BAU / Merge / Hold]
Date: [date]
Conditions: [conditions]
Next stage: [Initiation Form / Clarification / BAU / Deferred / Rejected / Merged]
Owner / sponsor: [confirmed / TBC]
Digital champion: [confirmed / TBC]
Notes: [short note]
```

## Next Lifecycle Trigger

The next stage begins when the item status is changed to Initiation Form In Progress or equivalent, and the correct route is selected or prepared.
