# Strateq DX Coworker Method

This public repository is the client-agnostic authority for Strateq DX governance and delivery methods. It contains reusable rules, lifecycle models, schemas, interfaces and Coworker instructions only.

## Data boundary

Client facts, evidence, live records and branded artefacts belong in a separate private repository for each client. They must never be committed here. Client branches or folders inside this repository are not permitted isolation boundaries.

Client repositories point one way to an approved method commit through their `METHOD_BASELINE.md`. This public repository must not maintain a client directory or links back to private client repositories.

Mandatory standard: `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## Core runtime

There are two lifecycle coworkers used inside one continuous initiative thread:

- Hopper Lifecycle Coworker — origin/intake through authority to commence.
- Live Delivery Coworker — mobilisation through delivery, adoption/handover and closeout.

The principal handover is Hopper → Live Delivery. Programme and leadership reporting are governed modes, not additional coworkers.

Stage 3 is governed by:

- `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`
- `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md`
- `02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md`
- `02_coworker_artifact_interface/06_LIVE_DELIVERY_ARTEFACT_1_MODEL.md`

The reusable runtime entry point is `.codex/skills/strateq-dx-live-delivery/`.

## Source architecture

| Layer | Role |
|---|---|
| This repository | Reusable method; read-only during client work |
| Private client repository | Client context, live working records and artefacts |
| Initiative folder | Initiative-specific evidence, setup and control records |
| ChatGPT/AI thread | Working interface only |
| External client store | Manual publication destination where configured |

The client profile names the actual delivery-control systems. Jira, SharePoint or any other platform is not assumed globally.

## Governing entry points

- `AGENTS.md` — model/tool instructions and client-binding rule
- `CLAUDE.md` — existing deterministic authority and stage map; applies to all models
- `CHATGPT_PROJECT_INSTRUCTIONS.md` — non-authoritative, build-only Project description for the Strateq DX method workspace
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/11_COWORKER_ROUTER.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`

## Cockpit feed contract

`02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md` defines the versioned
interface between approved client records and the personal cockpit. It separates
stage approval, delivery health, blockers, action status and freshness. It is a
released method specification, not a live integration: client baseline/profile approval, executable
schema, adapters and isolated tests are required before activation. Generated
feeds are projections, never another manually maintained source of truth.
Working-file uploads remain in the AI initiative chat. The specified Artefacts
feature selects initiative, artefact/report and reporting week for downloads of
saved versions, including historical PEPs and initiative-level executive and
leadership reports; it does not import or regenerate files.

The Initiative Delivery Setup model and template (`07` and `08`) require the
Coworker to establish each initiative's actual outcome, owned scope, exclusions,
deliverables, acceptance criteria and external dependencies before choosing
gates. Mieruka applicability and RAG follow that delivery definition. Existing
client workspaces adopt these rules through a controlled `METHOD_BASELINE.md`
update; this release does not rewrite their current records or enable a feed.

## Method artefact registry and revision handshake

`00_system_control/16_METHOD_ARTEFACT_REGISTRY.md` is the authoritative registry
of reusable artefacts (templates, schemas, interfaces, workbooks) and the
deterministic revision-handshake protocol. Strateq DX is the single source of
truth for these artefacts. Before any Coworker-generated refresh or populated
artefact, the Coworker binds one client, reads that client's `METHOD_BASELINE.md`,
reads the registry, resolves the latest **approved** artefact revision at the
approved method commit, confirms the interface/specification version matches and
the artefact is approved and not superseded, records the resolved
ID/revision/commit, and fails closed on a stale, missing, ambiguous or
incompatible baseline. "Latest" means the latest approved revision — never an
unpinned branch or an uploaded file. A client repository references the central
artefact revision through its `METHOD_BASELINE.md`; it does not duplicate the
reusable blank. Populated outputs stay client-side, and no client data is ever
written back into Strateq DX, which is read-only during client work. The file
includes a client-agnostic client-adoption reference pattern.

## Programme / portfolio workbook interface

`02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md`
specifies the Strateq DX Digital Programme Workbook — the governed human-facing
programme/portfolio interface and working snapshot for contract and initiative
management, lifecycle/current-step visibility, delivery milestones and
open/overdue actions. It defines the upload/reconciliation and
Coworker-generated-refresh workflows, versioning, status safeguards and
source-of-truth boundaries. An uploaded workbook is a supplied snapshot, not
automatically current: the Confirmation-First Status Gate applies, values are
reconciled against the controlled records, and the workbook never replaces the
Initiative Evidence and Decision File, PEP/control record, approved action
system, formal approval records, evidence registers or source-of-truth artefact
governance. The single canonical blank, client-agnostic template is
`02_coworker_artifact_interface/blank_templates/Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx`;
it is copied into a private client repository and populated there, never in this
public method repository.

## File-map maintenance

Any pull request that adds, renames, splits or retires a governance file must update `CLAUDE.md` B2, `00_system_control/FOLDER_MAP.md` and this README in the same commit.

## Executive communication

Executive and Board-facing outputs follow `docs/presentation-standards/communication-and-framing-standard.md`.
