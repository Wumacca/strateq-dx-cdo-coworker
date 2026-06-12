# Completed Initiation Form Output Model

## Purpose

This file defines the structure, content requirements, and output standard for the Completed Initiation Form — the formal DRB approval artefact for Development Route, Implementation Route, and governed Support Route initiatives.

The Completed Initiation Form is the document DRB reviews and approves before a digital initiative proceeds to live delivery.

"DRB Brief" is no longer used as a final approval artefact label. The following terms remain valid: DRB meeting, DRB approval, DRB decision, DRB Priority Discussion Note, DRB approval status.

For the three-route model rules, see `01_governance_lifecycle/05_ROUTE_RULES.md`.

## Core Rule

The Completed Initiation Form must be:

- executive and decision-ready
- route-specific in its content
- free of open questions before DRB submission
- reviewed and approved by the Digital Lead before DRB submission

Claude must withhold the Completed Initiation Form and return a questions-only output if unresolved material questions remain.

## Route-Specific Application

### Development Route

Section 1 is completed by the requesting department / initiator.

The Digital Team adds: confirmed development route, scope, deliverables, exclusions, duration, risk assessment, system / process impact, source-of-truth artefact impact, and project charter information.

DRB approval of the Completed Initiation Form authorises commencement of the live internal development job.

Stage 2 review is not required unless an exception trigger applies under `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

### Implementation Route

The requesting department must provide options / vendor / cost / CTR due diligence.

The Digital Team reviews, challenges, assesses, recommends, and completes the Digital Assessment / Project Charter.

Stage 2 review remains relevant where vendor, options, commercial, or implementation due diligence is required before DRB can approve.

Governed by `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

### Support Route

For governed Support Route items crossing risk, cost, control, or change thresholds, a proportionate Completed Initiation Form is required.

Minor BAU support must not be forced into full Initiation Form governance.

## Development Route: Required Sections

### Section 1 — Department / Initiator (department-owned)

- initiative title
- background and context
- problem statement
- current process / workflow
- future requirement
- expected benefit
- impacted systems
- operational impact
- risk flags

### Digital Team Additions

- confirmed development route
- confirmed scope
- agreed deliverables
- exclusions
- development owner / developer
- linked Jira task where known
- estimated duration
- target date where known
- system impact assessment
- process impact assessment
- security / data / integration considerations
- success measures
- risks and mitigations
- stakeholders and communications plan
- supporting documents list
- source-of-truth artefact impact summary

## DRB Approval Wording

Use this decision wording for Development Route approvals:

> "Approve [initiative name] to proceed as a live internal development job under the Development Route, based on the confirmed scope, exclusions, duration, risk controls, and supporting artefacts recorded in the Completed Initiation Form."

## Development Route Final Outputs

For Development Route, the final output set produced before DRB approval is:

1. **Completed Initiation Form** — the formal DRB approval artefact
2. **Development Scope / Deliverables Brief** — confirmed scope, deliverables, exclusions, duration, and project charter items
3. **Process flow document or swimlane specification** — where process mapping is required. Apply `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` and `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md`.
4. **Source-of-truth artefact impact check and handover note** — where controlled artefacts are impacted. Apply `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.
5. **Jira Initiation Summary / Delivery Context** — paste-ready Jira description field update

## Jira Initiation Summary / Delivery Context

The Jira Initiation Summary / Delivery Context replaces the previous "Jira description version" or "DRB Brief Jira description" output.

It is a paste-ready Jira description field update that records:

- initiative name and Jira key
- approved route
- decision required / DRB decision status
- confirmed scope summary
- key deliverables
- exclusions
- duration and target date
- key risks and controls
- process and source-of-truth impact summary
- next action

It is a Jira record of the initiation context for delivery tracking. It is not an approval document.

## Output Format

Claude must produce the Completed Initiation Form in one of two formats unless otherwise specified:

1. Word-friendly version — headings, sections, and tables suitable for copy/paste into Word or SharePoint
2. Paste-ready summary — condensed version for Jira description field

The Word-friendly version is the primary output.

Claude must ask which format is required unless the target is already clear from context.

## Required DRB Decision Labels

Use the canonical decision labels in `00_system_control/CONTROLLED_VOCABULARY.md`.

## Process Flow Requirement

If the initiative changes how work is done, the Completed Initiation Form must include a Process Flow Status statement:

- Process flow drafted and attached
- Process flow required before DRB approval
- Process flow not required
- Insufficient process detail to draft flow

## Swimlane Requirement

If process information is available, Claude must produce a draft swimlane process flow using:

`03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`

The swimlane is a supporting artefact. It should be separate from the Completed Initiation Form unless the Digital Lead asks for it embedded.

## Boundary

The Completed Initiation Form prepares the DRB decision. It does not approve the initiative.

DRB remains the decision-making body.
