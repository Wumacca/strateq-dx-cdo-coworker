# Strateq DX Coworker Instructions

These instructions apply to every AI model or coding agent operating in this repository. `CLAUDE.md` is retained as the existing authority filename; its rules apply to all coworkers, not only Claude.

## Repository role

This repository is the client-agnostic Strateq DX method authority. It may contain reusable governance rules, schemas, blank interfaces and skills only. It must never contain a client's facts, evidence, credentials, live artefacts or initiative records.

## Mandatory authority sequence

Before governed work, read and apply:

1. `CLAUDE.md`
2. `00_system_control/OPERATING_RULES.md`
3. `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`
4. the fixed authority set and stage-specific files mapped in `CLAUDE.md` B2

For Live Delivery, this always includes:

- `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`
- `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md`
- `02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md`
- `02_coworker_artifact_interface/06_LIVE_DELIVERY_ARTEFACT_1_MODEL.md`

## Client binding

Client work is permitted only after the coworker has read the selected private client repository's `CLIENT_BOUNDARY.md` and stated the bound client ID, AI Project/workspace, memory-boundary status, allowed repositories, thread/path and write target. During a client session:

- this method repository is read-only;
- exactly one private client repository is the write authority;
- no other client source may be searched, opened, copied, compared or referenced;
- cross-project/client memory must be disabled or project-only where the platform supports persistent memory;
- any client mismatch, ambiguous source or unapproved repository is a stop condition.

The coworker must fail closed under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## Decision boundary

The coworker may inspect, reconcile, draft, validate and prepare controlled changes. The Digital Lead approves governance decisions, source-of-truth changes, stage transitions and releases.

## File-map maintenance

Any pull request that adds, renames, splits or retires a governance file must update `CLAUDE.md` B2, `00_system_control/FOLDER_MAP.md` and the root `README.md` in the same change.
