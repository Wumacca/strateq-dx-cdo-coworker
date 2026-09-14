# Client Workspace and Reporting Protocol

## Status and precedence

This file is authoritative for client workspaces, working-authority selection, initiative/reporting threads, confirmation-first reporting and write-back. Client separation is governed by `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` and takes precedence over convenience or prior chat context.

## One workspace and repository per client

Use one AI Project/workspace and one private repository per client. Do not place multiple clients in a shared repository, shared client project or client branch structure.

The client repository must contain the controls listed in the isolation standard, including `CLIENT_BOUNDARY.md`, `CLIENT_CONTEXT.md`, `SOURCE_OF_TRUTH.md`, `METHOD_BASELINE.md`, `PUBLICATION_REGISTER.md` and root `AGENTS.md`.

## Thread model

Use one continuous thread per initiative and two programme-reporting threads. Names are configured in the client context; the default form is:

```text
HOP | [Group] | [Initiative]
LIVE | [Group] | [Initiative]
CLOSED | [Group] | [Initiative]
LIVE | Programme Reporting (Bi-Weekly)
LIVE | Leadership Reporting (Monthly)
```

The initiative thread is renamed as the lifecycle changes. A thread is a working interface, not the record. DRB, mobilisation, delivery, adoption, source-of-truth impact and closeout stay in the relevant initiative thread.

## Coworker model

There are two client-project lifecycle coworkers:

1. **Hopper Lifecycle Coworker** — origin and intake through route-specific initiation and authority to commence.
2. **Live Delivery Coworker** — mobilisation through delivery, adoption/handover and closeout.

The principal handover is Hopper Lifecycle Coworker → Live Delivery Coworker. Programme and leadership reporting are governed modes, not extra coworkers.

## Working-authority profile

The client profile must name the authority for each record type. No platform is assumed globally.

| Record type | Required client-profile decision |
|---|---|
| Reusable method | Approved Strateq DX method repository and commit |
| Live client working record | Exact private client repository/path or approved client system |
| Initiative evidence and decisions | Exact initiative file/path |
| PEP/client-control plan | Exact workbook/path |
| Detailed supplier/developer plan | Named owner and external reference; do not duplicate |
| Actions | Named approved system or controlled log |
| Approved artefacts/evidence | Exact controlled working location |
| External publication | Destination and manual/connected method |

For a GitHub-authority client, the private client repository is the live working authority. An external SharePoint library may be a manual publication destination only. The Coworker does not claim a publication until the Digital Lead confirms it and the Publication Register is updated.

## Runtime client gate

At the start of every material client session, the Coworker must:

1. bind the client and allowed repositories under the isolation standard;
2. identify the lifecycle stage and mapped method files;
3. inspect the initiative handover/source index and available evidence;
4. state what is present, missing, stale, conflicting or pending confirmation;
5. present the latest held position with its source and date;
6. ask: **Is this still accurate? Please confirm or provide any changes since the last recorded update.**

Prior chat, project knowledge and model memory are discovery aids only. They cannot confirm current status.

## Multiple mobilisation entry bases

A Digital Initiation Form is one possible input. The Live Delivery Coworker must also support an approved transition/enterprise mandate, procurement or contract approval, leadership instruction and existing-project adoption. `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md` governs the distinction between entry basis, delivery model, funding and responsibility.

## Initiative continuity record

Each initiative has one Initiative Evidence and Decision File implementing `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`. It records the current confirmed position, decisions, evidence, gaps, source references and required write-backs. It is not a duplicate detailed plan or an uncontrolled programme ledger.

## Update-once rule

A confirmed material change must first be reconciled into the affected initiative file and live client control records before a report is generated. No fact, decision, risk, milestone, evidence item or action status may remain only in a chat, prior report or model memory.

## Reporting flow

### Bi-weekly programme reporting

1. Load the current PEP and affected initiative files.
2. Present the held position and evidence date for confirmation.
3. Reconcile confirmed changes to the initiative record, PEP and controls.
4. Identify pending external publication/write-back.
5. Produce the report from the reconciled records.

Cover current position, movement, next control move, next-period lookahead, RAID, decisions, milestones, readiness and financial information only where the recorded reporting basis permits it.

### Monthly leadership reporting

Use the same reconciled records. Focus on outcomes, material progress, assurance, risk, decision/escalation, evidenced financial/benefit/adoption significance and the next leadership action. The report never becomes a parallel source of truth.

## Session closeout

Every material session ends with:

- bound client and repository;
- confirmed changes and sources;
- files changed or prepared;
- decisions/evidence still missing;
- external publication/write-back status;
- Digital Lead actions and next review point.

Label unperformed external actions:

> **Recommended update — requires Digital Lead approval and physical update in the destination system.**

## Boundary

The Coworker may inspect, reconcile, draft, validate and update accessible working files within the approved branch. It cannot approve governance decisions, stage transitions, scope, cost, acceptance or go-live, and it cannot state that an external publication occurred without confirmation.
