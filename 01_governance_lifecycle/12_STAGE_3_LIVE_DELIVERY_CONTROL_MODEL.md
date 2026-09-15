# Stage 3 Live Delivery Control Model

## Status

Authoritative model for mobilisation and live delivery after an initiative is authorised. It applies to Development, Implementation and Support routes and to initiatives entering through an approved non-initiation mandate.

## Lifecycle

Stage 3 uses this controlled path:

`Authorised → Mobilising → In Delivery → Adoption / Handover → Closed`

`Paused (On Hold)` may be applied with an owner, reason and review point. `Operational / Live` may describe the operating state after go-live but does not replace the Adoption / Handover control.

Only the Digital Lead may approve a stage transition.

## Independent mobilisation dimensions

The Coworker must not infer responsibility from a single bucket. It records these dimensions independently:

| Dimension | Controlled position |
|---|---|
| Entry basis | Initiation Form; transition/enterprise mandate; contract/procurement approval; leadership instruction; existing project adoption; exception with authority not evidenced |
| Delivery route | Development Route; Implementation Route; Support Route; TBC |
| Delivery model | Development-led; Digital-led implementation/support; vendor-led implementation with Digital client-side assurance; TBC |
| Funding classification | Capex; Opex; programme/transition funding; other; TBC |
| Detailed-plan owner | Named developer, Digital owner, vendor or other |
| Client-control-plan owner | Named Digital Lead or approved owner |
| Budget/cost owner | Digital; client project/programme manager; business owner; shared; other; TBC |
| Digital financial-reporting basis | Full; owner-supplied summary; approved variations only; emerging impacts/exceptions only; none; TBC |
| Acceptance/go-live authority | Named client authority |
| Reporting route | Audiences, cadence, cut-off, validator and escalation path |

Capex is a funding classification, not a delivery model.

## Valid entry to mobilisation

An approved Digital Initiation Form is one entry basis, not the only one. Valid alternatives include an approved programme or transition mandate, contract or procurement approval, leadership decision, project charter, approved business case or formal workstream instruction.

No Initiation Form does not mean no authority. Where no authority to proceed is evidenced:

> `No approved mobilisation authority has been evidenced. Setup may proceed in draft, but the initiative cannot transition to In Delivery.`

Do not manufacture a retrospective Initiation Form solely to satisfy the workflow.

## Mobilisation sequence

1. Bind the client under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.
2. Inspect the handover and all supplied governing sources.
3. Produce an evidence inventory: confirmed, confirmation required, missing and conflicting.
4. Identify the entry basis and authority to proceed.
5. Resolve the independent dimensions above.
6. Ask one consolidated set of questions for gaps only.
7. Draft `Initiative Delivery Setup`.
8. Configure the client-control plan, RAID/decision/change/evidence controls and reporting chain.
9. Reconcile the Initiative Evidence and Decision File and PEP.
10. Stop for Digital Lead approval of `Mobilising → In Delivery`.

## Delivery-model controls

### Development-led delivery

The development owner controls detailed execution. The client-control plan retains approved scope, delivery milestones, dependencies, acceptance gates, evidence and changes.

### Digital-led implementation or support

Digital coordinates the agreed delivery activities and maintains the applicable client-control plan and governance records.

### Vendor-led implementation with Digital client-side assurance

The vendor owns its detailed implementation plan and technical execution. Digital controls the client side of scope, milestones, dependencies, decisions, RAID, data, integration, testing, training, readiness, acceptance, evidence and reporting.

Do not duplicate the vendor's complete plan. The PEP contains the milestones, client obligations, interface dependencies, acceptance gates, required evidence and approved variations that the client must govern.

## Delivery source-of-truth map

Each initiative's `Initiative Delivery Setup` must name exactly one authority for each record type:

- supplier/developer detailed plan;
- client-side PEP/control plan;
- RAID, decisions and changes;
- approved artefacts and evidence;
- current reporting narrative;
- budget/cost position;
- manual publication destination.

For a client using GitHub as its working authority, the private client repository holds the live controlled records and approved working artefacts. External SharePoint publication is manual and is not current until confirmed in the Publication Register.

## Reporting chain

Reporting must be derived from governed records:

`Detailed-owner update → delivery-control meeting → PEP/control records → Artefact 1 → programme/leadership reporting`

Supplier-reported overall percentage must not pass directly into leadership reporting. Progress rolls up from agreed milestones or leaf activities with completion evidence. Narrative fields such as Current Position, Next Control Move and 7 Day Lookahead must be confirmed or derived transparently; they must not be invented.

Where Digital does not own budget, reporting must not imply that it does. Financial reporting is limited to the basis recorded in `Initiative Delivery Setup`.

## Stage gates

### Mobilising → In Delivery

Requires Digital Lead approval and, as applicable:

- authority to proceed evidenced;
- delivery and governance ownership confirmed;
- scope and exclusions recorded;
- source-of-truth map confirmed;
- PEP/control structure established;
- budget and financial-reporting responsibility confirmed;
- acceptance and go-live authority named;
- reporting cadence and escalation route confirmed;
- material gaps accepted with owner and review point.

### In Delivery → Adoption / Handover

Requires delivery/acceptance evidence, operational ownership, support and readiness position, open obligations and approved transition decision.

### Adoption / Handover → Closed

Requires closeout evidence, residual ownership, source-of-truth impact, lessons and publication/write-back status.

## Artefact interface

- Artefact 0: `Initiative Delivery Setup` — governed by `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md`.
- Artefact 1: live delivery meeting/reporting record using the approved Rev1 structure and the current client-controlled file revision — governed by `02_coworker_artifact_interface/06_LIVE_DELIVERY_ARTEFACT_1_MODEL.md`.
- PEP: client-control plan and portfolio reporting source, not a second supplier plan.
- Initiative Evidence and Decision File: current evidence and decision continuity record.

The first Artefact 1 record after mobilisation carries the approved `Initiative Delivery Setup` reference once. Later records do not repeat the mobilisation handover unless it changes through control.

## Boundary

The Coworker drafts, reconciles, validates and recommends. It does not approve a stage, scope, budget, variation, acceptance or go-live decision.
