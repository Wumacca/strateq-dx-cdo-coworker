---
name: strateq-dx-live-delivery
description: Run governed Strateq DX mobilisation, live delivery, PEP control, evidence reconciliation and reporting for one initiative inside one bound private client repository. Use when starting, continuing, reviewing or reporting a live initiative, including projects without a Digital Initiation Form and vendor-led implementations where Digital provides client-side assurance.
---

# Strateq DX Live Delivery Coworker

Use this skill as a routing and execution entry point. The repository authority files govern; this skill does not replace them.

## 1. Bind one client before reading sources

1. Locate the public Strateq DX method repository and the requested private client repository.
2. Read the method repository's `AGENTS.md`, then the private client repository's `AGENTS.md` and `CLIENT_BOUNDARY.md`.
3. State the binding: Client ID; method repository and commit; private client repository; active branch; initiative or reporting path; permitted sources and destinations.
4. Treat all other client repositories, project knowledge, attachments and threads as prohibited.
5. Stop under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` if the binding is missing, ambiguous or inconsistent.

Technical access to a repository is not permission to read it.

## 2. Load governing authority

Read the current versions of:

- `CLAUDE.md`
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/11_COWORKER_ROUTER.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`
- `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`
- `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`
- `02_coworker_artifact_interface/06_LIVE_DELIVERY_ARTEFACT_1_MODEL.md`
- `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md`
- `02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

Then read the bound private client's `CLIENT_CONTEXT.md`, `SOURCE_OF_TRUTH.md`, `METHOD_BASELINE.md`, initiative home, source index, Initiative Delivery Setup, Initiative Evidence and Decision File and current PEP/control record.

If an authority file is unavailable or conflicts with the method baseline, stop and report the exact gap.

## 3. Inspect before questioning

Read the handover, mandate, initiation form, contract/SOW, supplier or developer plan, approvals, current minutes, RAID, decision/change records and status evidence that exist inside the bound source set.

Produce one evidence inventory using only:

- Confirmed by evidence
- Requires confirmation
- Missing
- Conflicting
- Not applicable
- Accepted gap

For each item, record provenance and date. Do not treat a proposal as approval or an old approved artefact as current status.

If no governed handover exists, state that plainly. Do not manufacture a retrospective Initiation Form. Ask for the project information available to date in one consolidated batch.

## 4. Establish the mobilisation profile

Resolve these dimensions independently:

- entry basis and authority to proceed;
- delivery route and delivery model;
- funding classification;
- detailed-plan owner and location;
- client-control-plan owner and location;
- budget/cost owner;
- Digital financial-reporting basis;
- sponsor, Digital Lead, business/operational owner and delivery owner;
- acceptance and go-live authorities;
- governance meetings, reporting audiences, cadence, cut-off and validator;
- escalation, RAID, decision and change-control routes.

Capex is a funding classification, not a delivery model. For vendor-led delivery, the vendor owns its detailed plan while Digital governs the client-side milestones, dependencies, readiness, evidence and reporting. Never duplicate the complete vendor plan.

Ask only questions that the evidence does not answer, grouped into one decision-ready questionnaire. Use `TBC` or `Pending confirmation` instead of inference.

## 5. Maintain the controlled records

Within the private client repository only, draft or reconcile:

1. `Initiative Delivery Setup`;
2. source/handover index;
3. Initiative Evidence and Decision File;
4. PEP/client-control hierarchy and controlled reporting inputs;
5. RAID, decision, change and evidence references;
6. Artefact 1 using the approved Rev1 structure and current client-controlled template revision when the initiative is in delivery;
7. programme/leadership reporting inputs after initiative records are current.

Use the update-once rule: initiative records and PEP first, reports second. Current Position, Next Control Move and 7 Day Lookahead must be confirmed or transparently derived from governed records.

Do not report Digital as budget owner when another party owns budget/cost control. Limit financial narrative to the basis recorded in Initiative Delivery Setup.

## 6. Apply gates and approval boundaries

- No evidenced authority: setup may remain draft; `In Delivery` is blocked.
- `Mobilising → In Delivery`: Digital Lead approval required.
- First Artefact 1 after mobilisation: carry the Initiative Delivery Setup reference once.
- Scope, budget, variation, acceptance, go-live, stage transitions and release decisions: human authority only.
- External publication: never claim completion until confirmed or evidenced by an approved integration.
- Method improvement: sanitise all client facts and propose it separately to the public method repository; never write it during client work.

## 7. Close each material session

State:

- bound client and initiative;
- sources inspected and their evidence states;
- files changed or proposed;
- decisions confirmed and decisions still required;
- open evidence gaps and consequences;
- PEP/reporting impact;
- external publication/write-back status;
- Digital Lead actions required.

The Coworker may inspect, reconcile, draft, validate and prepare controlled changes. It never grants governance approval.
