# Route Rules

## Purpose

This file defines the three-route model for digital initiatives, the criteria for classifying each route, and the key governance rules that govern each route.

This file is a routing reference. Detailed workflow rules are in the route-specific authority files.

## Three-Route Model

### Development Route

Internal development initiatives approved by DRB through a Completed Initiation Form.

**Examples:**

- Chronos Dev
- Omega Dev
- SharePoint internal build
- Power BI internal build
- any in-house development tool or internal platform enhancement

**Key rules:**

- The formal DRB approval artefact is the Completed Initiation Form
- Section 1 completed by the requesting department; Digital Team adds scope, deliverables, duration, risk assessment, and artefact impact
- Requesting department must confirm requirements before Completed Initiation Form is finalised
- Development team must confirm scope and duration before Completed Initiation Form is finalised
- DRB approval of the Completed Initiation Form authorises commencement of the live internal development job
- Stage 2 due diligence is not required unless an exception trigger applies
- Exception triggers must be tested before final output production

**Authority file:** `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`

### Implementation Route

Third-party implementations and externally-led delivery requiring full due diligence before DRB approval.

**Examples:**

- third-party software implementation
- supplier-led delivery
- external platform implementation
- option appraisal / quote comparison route
- business case / funding route

**Key rules:**

- The requesting department must provide options / vendor / cost / CTR due diligence
- Stage 1 clarifies the initiative; Stage 2 builds the formal initiation pack
- The Digital Team reviews, challenges, assesses, recommends, and completes the Digital Assessment / Project Charter
- DRB approves the Completed Initiation Form (Stage 2 pack) before live delivery starts
- Vendor / cost / CTR / implementation route must be confirmed before approval
- Nitro / leadership sign-off applies where cost or risk thresholds require it

**Authority file:** `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`

### Support Route

BAU operational support and minor improvements that do not require full initiation governance.

**Examples:**

- BAU support request
- minor operational fix
- small internal process workaround
- operational improvement below risk / cost / control thresholds

**Key rules:**

- Minor BAU support must not be forced into Initiation Form governance
- Only governed support items crossing risk, cost, control, or change thresholds require a proportionate Completed Initiation Form
- Support items below thresholds route to BAU Support in Jira
- Threshold crossing triggers Hopper entry and route classification
- Proportionality is governed by the Digital Lead, not AI default

**Note:** Support Route governance is proportionate. Escalation to Hopper and Completed Initiation Form only applies where risk, cost, control, or change significance warrants it.

## Route Classification

Route classification must be confirmed before any initiation session begins.

Use the Initiative Type field in Jira as the primary classification signal.

If the route is unclear, Claude must ask the Digital Lead before producing any outputs.

Route labels to use:

- `Development Route`
- `Implementation Route`
- `Support Route`
- `TBC`

## Exception: Development Route Requiring Stage 2

A Development Route initiative must be escalated to Stage 2 if any of the following exception triggers applies:

- Scope is not confirmed (requesting department has not confirmed requirements)
- Development team has not confirmed duration or feasibility
- Material architecture, security, or integration risk remains unresolved
- Material third-party cost or vendor decision is required
- Third-party supplier selection is required
- Business case or funding approval is required
- DRB requests further due diligence

If no exception trigger applies, Stage 2 must not be forced on Development Route initiatives.

## Cross-References

| Route | Session trigger | Authority file |
|---|---|---|
| Development Route | `spin up stage 1 session` + Development Route confirmed | `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md` |
| Implementation Route | Stage 1 / Stage 2 initiation | `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` |
| Support Route | BAU Support in Jira, or threshold-triggered Hopper entry | `00_system_control/CONTROLLED_VOCABULARY.md` |
| All routes — Completed Initiation Form | When producing the formal DRB approval artefact | `01_governance_lifecycle/06_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md` |
| All routes — process mapping | When Process Mapping Required = Yes | `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md` |
| All routes — swimlane | When swimlane required | `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` |
| All routes — handover | When responsibility transitions | `00_system_control/04_COWORKER_HANDOVER_MODEL.md` |
| All routes — artefact impact | When controlled artefacts affected | `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` |
