# Initiative Delivery Setup Model

## Controlled title

The exact Artefact 0 title is:

> **Initiative Delivery Setup**

Do not expand, suffix or replace this title with “mobilisation record”, “Jira setup record” or “delivery-control setup record”.

## Purpose

Establish the evidenced basis, responsibilities, controls and readiness required to move an authorised initiative from `Mobilising` to `In Delivery`.

## Required sections

### 1. Control header

- Client ID and initiative identity
- Assigned lifecycle Coworker, commencement status and date
- Bound AI Project/workspace and thread name
- Version, status, owner and review date
- Bound private client repository and initiative path
- Method baseline commit

### 2. Mobilisation basis

- Entry basis
- Authority to proceed
- Approval reference, decision owner and effective date
- Scope, exclusions, outcome and success criteria
- Unresolved authority gap, if any

### 3. Delivery profile

- Delivery route
- Delivery model
- Funding classification
- Detailed-plan owner and location
- Client-control-plan owner and location
- Digital Lead, sponsor, business/operational owner and delivery owner
- Acceptance and go-live authority

### 4. Financial responsibility

- Budget/cost owner
- Information accessible to Digital
- Digital financial-reporting basis
- Variation/expenditure approval authority
- Required financial reporting audience and cadence

### 5. Governance and reporting

- Meetings, chair, cadence and participants
- Reporting cut-off and validator
- Programme, leadership and other reporting audiences
- Escalation thresholds and route
- RAID, decision and change-control authority

### 6. Delivery-control structure

- PEP hierarchy and milestone completion criteria
- Client activities and interface dependencies
- Data, integration, test, training, readiness and cutover controls where applicable
- Evidence required for milestone completion, acceptance and go-live
- Vendor/developer plan interface without duplication

### 7. Evidence inventory

Classify every required source as `Confirmed by evidence`, `Requires confirmation`, `Missing`, `Conflicting`, `Not applicable` or `Accepted gap` and record its provenance.

### 8. Readiness decision

- Gate checks
- Accepted gaps with owner and review point
- Digital Lead decision: Approved / Approved with conditions / Not approved / Pending
- Effective transition date
- First Artefact 1 handover reference

## Dynamic discovery rule

The Coworker inspects the supplied handover first and asks only for information not answered by evidence. If no governed handover exists, it states that plainly and requests the available project record to date in one consolidated batch.

### Establish the actual delivery definition

Before assessing delivery readiness or presenting a Mieruka position, the
Coworker must establish the initiative's actual outcome, work boundary and
definition of done. A route or project-type label alone is insufficient.

Within the existing mobilisation basis and delivery-control structure:

1. Reconcile the mandate, agreed scope, handover and current delivery evidence.
2. State exactly what Digital is accountable for delivering, what others own,
   what is excluded and which external outcomes are necessary dependencies.
3. Identify each deliverable and its acceptance criteria, evidence, responsible
   owner, acceptance authority and agreed target or review trigger. Mark gaps
   explicitly; do not invent dates, thresholds or acceptance criteria.
4. Determine the actual delivery approach and applicable gates. Present one
   consolidated set of questions for unresolved scope or criteria, then obtain
   Digital Lead confirmation and approval of the controlled setup/profile.
5. Where a cockpit feed is enabled, map those criteria to the configured cells
   under `02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md`. Preserve
   the criteria and evidence references behind each cell.

For example, an export-only scope can require agreed extraction requirements,
the export itself, agreed completeness/integrity checks and accepted handover.
It does not automatically include target-system migration, cleansing,
transformation/mapping, cutover or a full implementation test programme. Confirm
that boundary from evidence; do not assume all export work has identical gates.

Work owned by someone else is not automatically N/A. If it is needed for this
initiative's deliverable or acceptance, retain it as an externally owned
dependency/assurance obligation. Conversely, do not assess a bounded support
deliverable against completion of the entire parent enterprise programme.

At each material delivery update, reconcile progress, blockers and actions
against these agreed criteria. New or changed obligations require a proposed
controlled update, not silent scope expansion or a more favourable assessment.
This definition stays in Initiative Delivery Setup and the named controls; it
does not create a separate plan or additional initiative record.

## No-authority rule

Drafting may continue where useful, but the record cannot approve `In Delivery` when authority to proceed is not evidenced or explicitly confirmed by the Digital Lead.

## Close rule

Artefact 0 closes only when the Digital Lead records the `Mobilising → In Delivery` decision. The first Artefact 1 record carries the setup reference once.
