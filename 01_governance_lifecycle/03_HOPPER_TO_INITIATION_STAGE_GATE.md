# Hopper to Initiation Stage Gate

## Purpose

This file defines the governed handoff from Hopper Priority Screen into the correct initiation route.

The stage gate prevents lightly screened ideas from moving into delivery without formal due diligence.

From this gate, approved items branch into one of three routes:

- **Development Route → Stage 1D** — for internal development initiatives (Chronos Dev, Omega Dev, SharePoint builds, Power BI builds, in-house tools). Governed by `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.
- **Implementation Route → Stage 1 + Stage 2** — for third-party implementations, supplier-led work, SaaS onboarding, option appraisal, or business case routes. Governed by `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.
- **Support Route** — for minor BAU support, system fixes, or operational assistance that does not justify Initiation Form governance. Governed by `01_governance_lifecycle/05_ROUTE_RULES.md`. Minor BAU support must not be forced into Stage 1D or Stage 1.

## Core Rule

A Hopper item can only proceed past this gate after a DRB priority decision confirms that formal due diligence is justified.

Route selection is made at this gate, not assumed from Hopper data.

## Controlled Vocabulary

Use `00_system_control/CONTROLLED_VOCABULARY.md` for the canonical DRB priority decision set, approved route labels, and current Jira status labels.

Do not invent decision labels or Jira status names.

## Stage Gate Flow

```text
Hopper Priority Screen
↓
DRB priority discussion
↓
Canonical DRB priority decision recorded
↓
If approved: Route Classification
↓
┌─────────────────────────────────────┬────────────────────────────────────────────────────┬─────────────────────────────────┐
│ Development Route                   │ Implementation Route                               │ Support Route                   │
│ (internal dev, Chronos, Omega,      │ (third-party, supplier, SaaS, option appraisal,    │ (minor BAU support, system fix, │
│  SharePoint build, Power BI build,  │  business case, uncertain architecture,            │  operational assistance,        │
│  in-house tool)                     │  material cost, supplier selection)                │  not justified for full init.)  │
└─────────────────────────────────────┴────────────────────────────────────────────────────┴─────────────────────────────────┘
↓                                     ↓                                                     ↓
Stage 1D                              Stage 1 → Stage 2                                     BAU Support route
(08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL) (07_TWO_STAGE_DIGITAL_INITIATION_MODEL)               (05_ROUTE_RULES.md)
```

If route is unclear, flag as TBC and ask the Digital Lead before loading any stage-specific rules.

## Valid DRB Priority Decisions

Use the canonical DRB priority decisions from `00_system_control/CONTROLLED_VOCABULARY.md`.

| Decision | Next Action |
|---|---|
| Progress to Initiation Form | Classify route then start Stage 1D, Stage 1, or Support Route |
| Clarify Before Progression | Gather targeted answers and return to DRB or delegated reviewer |
| Merge / Duplicate | Link or consolidate in Jira |
| Defer | Record reason and review window |
| Reject | Record reason and close / remove from active Hopper after Digital Lead confirmation |
| Move to BAU Support | Route to Support Route after Digital Lead confirmation |
| Hold for Future Review | Keep visible but out of current programme |

## Required Record Before Progression

Before moving past this gate, Jira should show:

- DRB priority decision
- decision date
- confirmed route: Development Route / Implementation Route / Support Route
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
- move BAU support into Stage 1D or Stage 1
- apply Stage 1 + Stage 2 rules to a confirmed Development Route item
- apply Stage 1D rules to a confirmed Implementation Route item
- force minor BAU support items into Initiation Form governance

## AI Coworker Role

AI may produce:

- DRB decision summary
- Route Classification recommendation (Development Route / Implementation Route / Support Route)
- Jira update text
- Stage 1D Session Start Checklist (Development Route only)
- Initiation Form stage starter checklist (Implementation Route only)
- missing information list
- department / vendor / developer question list

AI must not approve the stage gate or assign route without Digital Lead confirmation.

## Jira Update Template

```markdown
DRB priority decision recorded.

Decision: [canonical DRB priority decision]
Date: [date]
Route: [Development Route → Stage 1D / Implementation Route → Stage 1 + Stage 2 / Support Route / TBC]
Conditions: [conditions]
Next stage: [next lifecycle stage / status]
Owner / sponsor: [confirmed / TBC]
Digital champion: [confirmed / TBC]
Notes: [short note]
```

## Next Lifecycle Trigger

**Development Route:** The next stage begins when the item status is set to Stage 1D In Progress and the Digital Lead confirms the route. Load `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

**Implementation Route:** The next stage begins when the item status is changed to Initiation Form In Progress or equivalent, and the correct route is selected or prepared. Load `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

**Support Route:** The item is routed to BAU Support handling. Load `01_governance_lifecycle/05_ROUTE_RULES.md` for proportionate support rules. Do not open a Stage 1D or Stage 1 session.
