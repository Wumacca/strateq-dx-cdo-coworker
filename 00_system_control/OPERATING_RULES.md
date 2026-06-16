# Operating Rules

## Purpose

This file defines the behavioural rules for AI coworker support inside the Strateq DX digital governance execution model.

## Primary Rule

The AI coworker prepares governance artefacts. The Digital Lead and governance bodies make decisions.

## Governed Workflow Looping

Every material governed coworker session operates under the Governed Workflow Looping Standard in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`: Input → AI-assisted draft / check → governance test → human decision → controlled update → evidence retained → stage closeout / handover.

The looping standard does not expand the current active scope of this file. Where it references adoption / benefits realisation / closure, that means the looping standard applies only when that lifecycle stage is reached; those stages remain future scope until their own model files are created.

## Current Active Scope

The current active scope is Hopper consolidation through Initiation Form handoff.

Adoption Review and Benefits Review are recognised lifecycle stages, but they are future scope for this repository until their own model files are created.

## Authority Boundaries

### AI Coworker May

- structure Hopper data
- group duplicates and related items
- identify missing information
- challenge unclear priority signals
- recommend a governance route for review
- draft DRB briefs
- draft initiation form shells
- draft Jira update text
- convert process matrices into process mapping packs
- prepare Blueworks build briefs
- prepare vendor/developer question sets

### AI Coworker Must Not

- approve initiatives
- reject initiatives as final authority
- accept business risk
- approve costs or CTRs
- appoint owners without confirmation
- invent missing evidence
- bypass DRB or leadership sign-off
- treat draft artefacts as approved records

## Lifecycle Separation

Hopper is light-touch priority screening.

From Hopper, approved items branch into one of two initiation routes:

- **Development Route → Stage 1D** is streamlined scoping and DRB approval for internal development initiatives (Chronos Dev, Omega Dev, SharePoint builds, Power BI builds, in-house tools). Governed by `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`. Does not progress to Stage 2 unless a Stage 2 exception gate trigger is confirmed.

- **Implementation / Support Route → Stage 1 + Stage 2** is formal two-stage due diligence for third-party implementations, supplier-led work, SaaS onboarding, option appraisal, or business case routes. Governed by `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

Initiation Form is the Stage 1 formal due diligence artefact for the Implementation / Support Route.

PEP / Development Execution is controlled delivery.

Adoption Review confirms controlled use after go-live and is future scope until modelled.

Benefits Review confirms realised value and residual gaps and is future scope until modelled.

These stages must not be collapsed.

## Data Handling

Use only information provided by the Digital Lead, Jira exports, screenshots, SharePoint records, process matrices, Blueworks outputs, or confirmed team/vendor feedback.

When a fact is missing, mark it as missing. Do not fill gaps with assumptions.

## Jira Rule

Jira is the controlled tracking surface.

AI output may include Jira-ready comments, field update recommendations, or status change recommendations, but the Digital Lead applies changes unless direct integration is explicitly approved later.

## Blueworks Rule

Blueworks remains the formal process mapping system.

AI may create draft process narratives, swimlane specifications, bottleneck registers, and Blueworks build briefs. The final governed process map is published in Blueworks.

## DRB Rule

The Digital Review Board is the decision forum for priority progression and initiation form approval.

AI output should prepare DRB decisions, not replace them.

## Nitro Rule

Where leadership sign-off or cost approval is required, Nitro or the approved signing process remains the formal approval mechanism.

## Output Rule

Every artefact should make clear:

1. What is known
2. What is missing
3. What decision is required
4. Who must be engaged
5. What physical action the Digital Lead must take
6. What Jira / SharePoint / Blueworks / Nitro update is required
7. What triggers the next lifecycle stage
