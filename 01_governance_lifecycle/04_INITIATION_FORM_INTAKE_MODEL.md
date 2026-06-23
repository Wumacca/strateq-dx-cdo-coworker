# Initiation Form Intake Model

## Purpose

The Initiation Form stage is the formal due diligence stage after Hopper priority approval **for the Implementation / Support Route**.

It is used to prove that the correct delivery route has been selected before the initiative becomes live.

> **Development Route note:** If the approved initiative is an internal development item (Chronos Dev, Omega Dev, SharePoint build, Power BI build, in-house tool), this model does not apply unless a Stage 2 exception is triggered. Development Route items follow `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`. Only apply this file when Stage 2 exception triggers move a Development Route item to the full Stage 1 + Stage 2 process.

## Core Rule

Hopper asks:

> Is this worth formal assessment?

Initiation Form asks:

> Have we done enough due diligence to approve this for controlled delivery?

> **Sequencing boundary.** The Initiation Form is produced **after** leadership / DRB priority approval, on an explicit per-initiative route trigger. The Hopper Portfolio Readiness Review (`01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`) and any initiative charter are pre-initiation inputs only and are **not** Initiation Forms. Do not produce an Initiation Form during the Hopper review or from a charter.

## Stage Position

This flow applies to **Implementation / Support Route** items only.

```text
DRB priority approval
↓
Route confirmed: Implementation / Support Route
↓
Initiation Form In Progress
↓
Implementation or Development route selected
↓
Digital Team works with initiator / department / digital champion
↓
Process mapping pack if required
↓
Vendor / developer clarification if required
↓
DRB form approval
↓
Nitro / leadership sign-off if required
↓
Job Live
```

For Development Route items, see `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

## Required Inputs

Use confirmed information from:

- approved Hopper item
- DRB priority comments
- initiator / department answers
- digital champion input
- process matrix / Blueworks outputs where applicable
- vendor / developer answers where applicable
- cost / CTR assumptions where applicable

## Required Content Areas

The initiation form should capture:

- initiative title
- background and context
- problem statement
- options considered
- selected solution or proposed route
- solution overview
- process impact
- system impact
- maturity alignment
- scope boundaries
- out-of-scope items
- milestones
- benefits
- risks if not addressed
- risk assessment
- stakeholders
- communications plan
- competent people required for go-live
- training / adoption requirements
- costs / CTR position
- approvals

## AI Output: Initiation Form Build Pack

The AI coworker should produce:

1. Draft form content
2. Missing information
3. Questions for initiator
4. Questions for department / digital champion
5. Questions for vendor / developer
6. Process mapping requirement check
7. DRB review risks
8. Jira update text

## Physical Actions for Digital Lead

The Digital Lead should:

- work with the initiator and department to confirm facts
- confirm the route with the Digital Team
- run or arrange process mapping if work physically changes
- engage vendor/developer where feasibility, cost, or scope requires it
- confirm competent users and go-live ownership
- prepare the initiation form for DRB review

## Feedback Required from Digital Lead

Return to AI:

- completed answers
- route confirmed
- sponsor / owner / champion confirmation
- cost assumptions
- scope amendments
- process mapping output
- vendor/developer answers
- DRB concerns

## What Must Not Happen

Do not:

- approve the initiative only from Hopper data
- start controlled delivery before form approval
- ignore process change impacts
- leave competent people undefined for go-live
- leave development scope boundaries unclear
- leave system-of-record impacts unclear
- apply this model to a Development Route item unless a Stage 2 exception has been confirmed

## Stage Closeout

When this stage closes, produce the stage closeout using the Stage Closeout Handover output model in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. Hand over only what this stage agreed, delivered, approved, evidenced, and left open. Do not produce next-stage plans or checklists. Use the route-correct readiness line from the looping standard.

## Next Lifecycle Trigger

The next stage begins when the completed initiation form is ready for DRB form approval.
