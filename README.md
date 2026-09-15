# Strateq DX Coworker Method

This public repository is the client-agnostic authority for Strateq DX governance and delivery methods. It contains reusable rules, lifecycle models, schemas, interfaces and Coworker instructions only.

## Data boundary

Client facts, evidence, live records and branded artefacts belong in a separate private repository for each client. They must never be committed here. Client branches or folders inside this repository are not permitted isolation boundaries.

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

## File-map maintenance

Any pull request that adds, renames, splits or retires a governance file must update `CLAUDE.md` B2, `00_system_control/FOLDER_MAP.md` and this README in the same commit.

## Executive communication

Executive and Board-facing outputs follow `docs/presentation-standards/communication-and-framing-standard.md`.
