# Initiation Form Intake Model

## Purpose

This file defines the intake model for the Completed Initiation Form — the formal DRB approval artefact for all digital initiative routes.

For the full content standard, DRB approval wording, Jira Initiation Summary / Delivery Context output, and route-specific variants, see:

`01_governance_lifecycle/06_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`

> **Development Route:** Development Route items follow `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`. The Completed Initiation Form for Development Route is produced under Stage 1D without requiring Stage 2, unless an exception trigger applies. If process mapping is required, also load `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md` and `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`.

## Core Rule

Hopper asks:

> Is this worth formal assessment?

Completed Initiation Form asks:

> Have we done enough due diligence to approve this for controlled delivery?

## Stage Position

### Development Route

```text
DRB priority approval
↓
Route confirmed: Development Route
↓
Stage 1D session
↓
Completed Initiation Form produced (Section 1 + Digital Team additions)
↓
DRB approves → live internal development job
```

For Development Route, apply `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

### Implementation Route

```text
DRB priority approval
↓
Route confirmed: Implementation Route
↓
Stage 1 clarification
↓
Stage 2 formal initiation (options / vendor / cost / CTR due diligence)
↓
Completed Initiation Form produced (full due diligence)
↓
DRB approves → live delivery
```

For Implementation Route, apply `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

### Support Route

Minor BAU support must not be forced into Initiation Form governance.

Only governed support items crossing risk, cost, control, or change thresholds require a proportionate Completed Initiation Form.

## Required Inputs

Use confirmed information from:

- approved Hopper item
- DRB priority comments
- initiator / department answers (Section 1 confirmation for Development Route)
- digital champion input
- process matrix / Blueworks outputs where applicable
- vendor / developer answers where applicable (Implementation Route)
- cost / CTR assumptions where applicable (Implementation Route)

## Required Content Areas

For the full content standard by route, apply `01_governance_lifecycle/06_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`.

**Development Route — Section 1 (department-owned):**

- initiative title, background, problem statement, current process, future requirement, expected benefit, impacted systems, operational impact, risk flags

**Development Route — Digital Team additions:**

- confirmed development route, scope, deliverables, exclusions, developer, duration, system / process impact, security / data / integration, success measures, risks, stakeholders, source-of-truth artefact impact

**Implementation Route (full due diligence):**

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

## AI Output

**For Development Route, Claude must produce:**

1. Completed Initiation Form (Development Route content standard)
2. Development Scope / Deliverables Brief
3. Process flow swimlane specification (if process mapping required)
4. Source-of-truth artefact impact check and handover note (if artefacts impacted)
5. Jira Initiation Summary / Delivery Context

**For Implementation Route, Claude must produce:**

1. Draft Completed Initiation Form content
2. Missing information list
3. Questions for initiator
4. Questions for department / digital champion
5. Questions for vendor / developer
6. Process mapping requirement check
7. DRB review risks
8. Jira Initiation Summary / Delivery Context

## Physical Actions for Digital Lead

The Digital Lead should:

- confirm Section 1 is completed by the requesting department / initiator (Development Route)
- confirm Digital Team additions: scope, deliverables, duration, risk (Development Route)
- confirm the route with the Digital Team
- run or arrange process mapping if work physically changes
- engage vendor / developer where feasibility, cost, or scope requires it (Implementation Route)
- confirm competent users and go-live ownership
- prepare the Completed Initiation Form for DRB review

## Feedback Required from Digital Lead

Return to AI:

- Section 1 completion confirmed (Development Route)
- completed answers
- route confirmed
- sponsor / owner / champion confirmation
- cost assumptions (Implementation Route)
- scope amendments
- process mapping output
- vendor / developer answers (Implementation Route)
- DRB concerns

## What Must Not Happen

Do not:

- approve the initiative only from Hopper data
- start controlled delivery before Completed Initiation Form is approved by DRB
- ignore process change impacts
- leave competent people undefined for go-live
- leave development scope boundaries unclear
- leave system-of-record impacts unclear
- force Stage 2 on Development Route initiatives without a confirmed exception trigger
- apply this model to a Development Route item without first loading `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`
- force minor BAU support into Initiation Form governance

## Next Lifecycle Trigger

The next stage begins when the Completed Initiation Form is approved by DRB.
