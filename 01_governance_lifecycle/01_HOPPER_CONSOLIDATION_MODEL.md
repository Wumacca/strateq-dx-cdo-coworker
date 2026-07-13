# Hopper Consolidation Model

## Purpose

The Hopper Consolidation stage turns the current live Hopper into a clean, decision-ready governance canvas.

It is used when existing Hopper items have accumulated from benchmarking, maturity reviews, team-raised improvements, completed initiative follow-ons, process findings, integration needs, dashboard gaps, vendor ideas, or manual workflow problems.

## Core Principle

Hopper is light-touch priority screening.

Initiation Form is formal due diligence.

Do not overload Hopper with initiation-form detail.

> **Leadership-readiness review pointer.** When consolidation feeds a leadership / DRB priority discussion, the governing model is `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. The "Priority Screen" step prepares the Jira Initiative View / Hopper priority view as the default meeting surface — not a separate DRB Priority Screen document. The review is pre-initiation and pre-Pack 1.

## Stage Position

```text
Existing Hopper items
↓
Hopper consolidation
↓
Light-touch scoping with departments
↓
Hopper Priority Screen
↓
DRB priority discussion
↓
Approved / clarify / defer / reject / BAU / merge
↓
Initiation Form stage
```

## What Enters Consolidation

Inputs may include:

- Jira Hopper export
- Jira screenshots
- manually copied Hopper table
- maturity register gaps
- process workshop outputs
- completed initiative follow-ons
- digital review actions
- dashboard/reporting requests
- system enhancement requests
- integration needs

## Consolidation Objectives

For each Hopper item, determine:

1. What the item appears to be
2. Whether it duplicates or overlaps another item
3. Which department / function owns the problem
4. Which process or system is affected
5. Whether the item is BAU, support, improvement, implementation, development, dashboard, integration, or unclear
6. What light clarification is needed before DRB
7. Whether the item should be priority screened

## Consolidation Actions

AI coworker should:

- group duplicates
- identify related items that may need a parent initiative
- separate BAU/support noise from governed initiative candidates
- flag unclear ownership
- flag unclear system/process impact
- flag missing business problem
- flag items requiring department scoping
- prepare concise questions for each department/champion
- run the Cross-Initiative Impact Check for each new or materially changed item (see below)
- recommend whether each item proceeds to Priority Screen

## Valid Consolidation Outcomes

| Outcome | Meaning |
|---|---|
| Ready for Priority Screen | Basic information is sufficient for light priority scoring / DRB discussion |
| Clarify with Department | Basic problem, owner, system, process, or impact is unclear |
| Merge / Duplicate | Item overlaps another item and should be consolidated |
| Move to BAU Support | Item is support/admin/minor fix, not governed initiative material |
| Hold for Future Review | Potentially relevant but not ready for current programme planning |
| Reject Candidate | No clear business problem or governance relevance |

## Minimum Information Before Priority Screen

A Hopper item should normally have:

- Title
- Department / business area
- Short description
- Why raised
- Known system affected, if any
- Known process affected, if any
- Request type or apparent type
- Any obvious urgency or business exposure

If these are missing, the item should usually be clarified before priority screening.

## Department Scoping

Department scoping is light-touch.

The aim is not to complete the initiation form.

The aim is to confirm:

- what problem exists
- who owns it
- what process or system is affected
- what happens today
- what the department believes needs to change
- whether there is any obvious safety, regulatory, reputational, financial, operational, or client impact
- whether this is support, improvement, implementation, development, dashboard/reporting, or integration related

## Cross-Initiative Impact Check

Every new or materially changed initiative must be run through a Cross-Initiative Impact Check at Hopper intake (and again at any material change). This is a mandatory input requirement, session-checklist step, output, and closeout requirement of Hopper consolidation. Session mechanics run under `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`; the reconciliation source hierarchy governs how the existing portfolio is read.

The check compares the new or materially changed initiative against:

- systems affected;
- processes affected;
- departments;
- existing Hopper initiatives;
- approved initiatives;
- live delivery initiatives;
- proposed functionality;
- integrations;
- data flows;
- source-of-truth artefacts;
- shared vendors;
- shared delivery resources;
- delivery timing;
- feature or scope overlap;
- strategic objectives;
- maturity objectives;
- roadmap tracks.

### Approved outcomes

- Absorb into existing initiative
- Merge / duplicate
- Controlled change to live initiative
- Create dependency
- Sequence separately
- Retain as separate initiative
- No material impact
- Clarification required

### Rules

- Scope must not be silently absorbed into a live initiative.
- Any recommendation to modify a live initiative becomes a **candidate change control** — the affected initiative and its approval basis must be identified, and its current delivery position considered.
- The Digital Lead decides the final treatment. The coworker may recommend but cannot change scope or route.

### Output

Add one row per checked initiative:

| Initiative | Compared against | Overlap / dependency found | Approved outcome | Candidate change control? (Y/N) | Affected initiative & approval basis | Digital Lead decision |
|---|---|---|---|---|---|---|

The Digital Lead decision column must be left blank or set to "To confirm". Cross-Initiative Impact Check outcomes and any candidate change controls must appear in the session closeout write-back.

## AI Output: Hopper Consolidation Table

Recommended output columns:

| Item | Apparent Type | Duplicate / Related Items | Business Area | System / Process Link | Issue Clarity | Missing Basic Info | Suggested Consolidation Outcome | Department Questions | Jira Update |
|---|---|---|---|---|---|---|---|---|---|

## Physical Actions for Digital Lead

The Digital Lead should:

- review AI grouping and challenge wrong merges
- speak to department leads or digital champions for unclear items
- confirm which duplicates should merge
- remove BAU/support items from governed Hopper
- prepare clean candidate list for priority screening
- update Jira with comments, status, labels, or links

## Feedback Required from Digital Lead

Return to AI:

- confirmed duplicate/merge decisions
- department answers
- owner/champion confirmations
- corrected system/process links
- BAU/support routing decisions
- items confirmed for Priority Screen

## System Updates Required

Update Jira to reflect:

- merged items
- duplicate references
- clarification required
- BAU/support routing
- ready for Priority Screen
- hold/reject decisions

## Next Lifecycle Trigger

The next stage begins when a clean set of candidate items is confirmed as ready for Hopper Priority Screen.
