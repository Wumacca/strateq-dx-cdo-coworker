# Client Workspace and Reporting Protocol

## Status and precedence

This file is authoritative for client workspaces, working-authority selection, initiative/reporting threads, confirmation-first reporting and write-back. Client separation is governed by `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` and takes precedence over convenience or prior chat context.

## One workspace and repository per client

Use one AI Project/workspace and one private repository per client. Do not place multiple clients in a shared repository, shared client project or client branch structure.

The client repository must contain the controls listed in the isolation standard, including `CLIENT_BOUNDARY.md`, `00_PROJECT_HOME.md`, `CLIENT_CONTEXT.md`, `SOURCE_OF_TRUTH.md`, `METHOD_BASELINE.md`, `PUBLICATION_REGISTER.md` and root `AGENTS.md`.

The AI Project/workspace must be dedicated to one client. Its shared files and connected sources must contain only the public method repository and the bound client's permitted sources. Use project-only memory or disable memory wherever persistent memory could import another project's or client's context. Project instructions cannot compensate for a shared multi-client source or cross-project memory boundary.

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
| Reusable artefact adoption | Per-artefact pinned revision in the client `METHOD_BASELINE.md`, resolved through `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md` |
| Live client working record | Exact private client repository/path or approved client system |
| Initiative evidence and decisions | Exact initiative file/path |
| PEP/client-control plan | Exact workbook/path |
| Detailed supplier/developer plan | Named owner and external reference; do not duplicate |
| Actions | Named approved system or controlled log |
| Approved artefacts/evidence | Exact controlled working location |
| External publication | Destination and manual/connected method |

For a GitHub-authority client, the private client repository is the live working authority. An external SharePoint library may be a manual publication destination only. The Coworker does not claim a publication until the Digital Lead confirms it and the Publication Register is updated.

## Reusable artefact resolution and write boundary

Reusable artefacts (templates, schemas, interfaces and workbooks) are the single source of truth in the Strateq DX method repository. Before generating, refreshing or populating any reusable artefact for the bound client, the Coworker runs the revision-handshake in `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md`: it reads the client `METHOD_BASELINE.md`, resolves the latest **approved** artefact revision from the central registry at the approved method commit, confirms the interface/specification version matches and the artefact is approved and not superseded, records the resolved artefact ID/revision/commit, and fails closed on a stale, missing, ambiguous or incompatible baseline. "Latest" is the current approved revision, never an unpinned branch or an uploaded file.

The client repository references the central artefact revision through its `METHOD_BASELINE.md`; it does not keep an independent duplicate of the reusable blank. Only the **populated, client-specific output** is stored client-side. No client data, status or populated artefact is written back to the method repository, which is read-only during client work. A pinned artefact revision changes only through a Digital-Lead-approved `METHOD_BASELINE.md` update.

## Runtime client gate

At the start of every material client session, the Coworker must:

1. bind the client and allowed repositories under the isolation standard;
2. verify the active AI Project/workspace, memory boundary, thread and initiative path;
3. identify the lifecycle stage and mapped method files;
4. where the session will generate, refresh or populate a reusable artefact, run the revision-handshake in `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md` (resolve the latest approved artefact revision against the client `METHOD_BASELINE.md`; fail closed on a stale, missing, ambiguous or incompatible baseline);
5. inspect the initiative handover/source index and available evidence;
6. record or refresh Coworker commencement in the Initiative Evidence and Decision File;
7. state what is present, missing, stale, conflicting or pending confirmation;
8. present the latest held position with its source and date;
9. ask: **Is this still accurate? Please confirm or provide any changes since the last recorded update.**

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

## Optional cockpit export profile

`02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md` governs
the interface specification for a generated personal-cockpit projection. It does not
enable exports by default. After controlled adoption of the method baseline, the client profile must approve
the destination, permitted summary fields, source authorities, action edit route,
mapping version and freshness policy before implementation is activated.

The cockpit must not become a second independently maintained initiative or
client-action authority. A source-backed edit follows the existing controlled
update route and is displayed as synchronized only after verified acknowledgment.
Personal actions remain separate from client feeds. Any combined client-summary
view requires explicit export permissions and an approved consultant-view policy;
this section does not relax single-client AI sessions or the isolation standard.

Working artefact updates are supplied in the bound AI initiative chat, not
uploaded into the cockpit. The cockpit's Artefacts feature is a read-only
initiative/period/version catalogue for already-produced files, including PEPs
and initiative-level executive and leadership reports. Historical downloads
preserve the selected released file; they do not regenerate it from current data.

## Programme / portfolio workbook interface

`02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md`
governs the Strateq DX Digital Programme Workbook — a governed human-facing
programme/portfolio interface and working snapshot for contract and initiative
management, lifecycle/current-step visibility, delivery milestones and
open/overdue actions. The blank client-agnostic template is held in the method
repository (`02_coworker_artifact_interface/blank_templates/Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx`)
and is copied into the bound private client repository and populated there.

An uploaded workbook is a supplied snapshot, not automatically current. Before
any workbook value is used, apply the confirmation-first status rule, then
reconcile the workbook against the controlled records (Initiative Evidence and
Decision File, PEP/control record, minutes, the approved action system and other
approved evidence) and classify each difference (unchanged, proposed update, new
record, missing record, conflict, stale value, unresolved identity). Confirmed
changes are reconciled into the controlled records under the update-once rule
before any report or refreshed workbook is generated. The Coworker does not
silently overwrite controlled records; lifecycle labels and milestone cells are
projections, not proof of approval or completion; blank cells do not mean "not
required"; and manually entered action counts do not override reconciled action
records. A Coworker-generated refreshed workbook is a dated snapshot produced from
the confirmed controlled records and never becomes a parallel source of truth.
Client adoption of the workbook as a working surface requires a client-specific
source-of-truth decision in the client profile.

## Session closeout

Every material session ends with:

- bound client and repository;
- bound AI Project/workspace, memory-boundary status and thread/path;
- confirmed changes and sources;
- files changed or prepared;
- decisions/evidence still missing;
- external publication/write-back status;
- Digital Lead actions and next review point.

Label unperformed external actions:

> **Recommended update — requires Digital Lead approval and physical update in the destination system.**

## Boundary

The Coworker may inspect, reconcile, draft, validate and update accessible working files within the approved branch. It cannot approve governance decisions, stage transitions, scope, cost, acceptance or go-live, and it cannot state that an external publication occurred without confirmation.
