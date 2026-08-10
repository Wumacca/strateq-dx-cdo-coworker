## Strateq DX Repository Purpose

Strateq DX Build is the **reusable method repository** for Strateq-led digital transformation, governance, capitalisation, and Board reporting work. It holds the standards, schemas, templates, routing rules, and coworker method files. It does not hold any client's programme truth. It is separate from Quantuum AI product build material.

## DX Build, Client Workspace, and Future App

> The DX Build repository defines the method. The active client workspace holds programme truth. No coworker or future app workflow may assert client programme status until the active client workspace has been resolved and the client `PROGRAMME_STATUS.md` has been loaded.

### DX Build (this repository)

- reusable methods;
- schemas;
- authority files;
- coworker routing;
- templates.

Also: interface contracts, generic anonymised examples, and human-facing operating manuals. Nothing client-specific.

### Client workspace (one per client, held separately)

- active programme status;
- client artefacts;
- decision/evidence registers;
- client-specific capex packs;
- client-specific handovers.

Also: the client context manifest instance, the artefact and handover registers, and the Initiative Evidence and Decision Files.

### Future app

- resolves client context through the manifest;
- executes coworker workflows against the active client workspace.

```text
Client Registry
→ Client Context Manifest
→ Programme Status
→ Artefact / Decision / Evidence / Handover Registers
→ Coworker workflow execution
```

The app or coworker may read current client status, propose controlled updates, and write only after Digital Lead approval, where write capability exists. The manifest `write_mode` field defaults to `proposal_only`.

### Governing files

| File | Purpose |
|---|---|
| `00_system_control/15_CLIENT_WORKSPACE_INTERFACE_STANDARD.md` | The interface standard: resolution gate, read/write boundary, source precedence, fail-closed rule, future app / tenant model |
| `00_system_control/CLIENT_CONTEXT_MANIFEST_SCHEMA.md` | Reusable manifest schema. Instances live in the client workspace |
| `00_system_control/PROGRAMME_STATUS_TEMPLATE.md` | Reusable programme status structure |
| `00_system_control/PROGRAMME_STATUS_RULES.md` | How client `PROGRAMME_STATUS.md` files are governed |
| `00_system_control/CLIENT_CONTEXT_REGISTRY.example.json` | Anonymised example registry only |

> The Digital Lead is the sole confirmation authority for programme status. The accepted delivered artefact remains the evidence basis. `PROGRAMME_STATUS.md` is the live controlled status surface.

**Client-specific programme truth must not be stored in the DX Build repository.**

## Repository Structure

- `00_system_control/` holds the system control, routing, interface, schema, and template authority files.
- `01_governance_lifecycle/` holds the governed lifecycle, route, initiation, and Capex Request Session models.
- `02_coworker_artifact_interface/` holds the coworker / Digital Lead working interface templates.
- `03_process_mapping/`, `04_intake_dispatch/`, `05_source_of_truth/` hold the process, intake, and artefact governance models.
- `06_operating_manual/` holds human-facing, non-authoritative navigation.
- `BOARD_INTERFACE/` and `docs/` hold Board-facing index material and presentation standards.
- `_archive/` holds the archive note and index. Client-specific source packs and evidence exports are not archived here — see `_archive/ARCHIVE_NOTE.md`.
- Board-facing content must be generated from controlled markdown source files, not from standalone slide edits.

## PR Maintenance Rule

Any PR that adds, renames, splits, retires, or relocates a lifecycle, route, handover, source-of-truth, workflow, or coworker authority file must update the `CLAUDE.md` Tier 2 map, `00_system_control/11_COWORKER_ROUTER.md`, this README / the folder map, and the affected lifecycle index. The PR must fail review if these are not updated.

## Client Workspace and Reporting Controls

There are exactly two client-project lifecycle coworkers — the **Hopper Lifecycle Coworker** (origin and intake through approval to commence delivery) and the **Live Delivery Coworker** (approval through delivery, adoption, benefits, source-of-truth impact, and closeout). The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker. DRB, source-of-truth artefact control, adoption, benefits, capitalisation, maturity review, and reporting are governed stages, controls, or modes — not separate coworkers or threads. Digital Governance & Strategy is a programme governance and control function, not a client-project coworker. Each initiative runs in one continuous thread (`HOP` → `LIVE` → `CLOSED`), with only two non-initiative threads: `90 | Bi-Weekly Programme Reporting` and `91 | Monthly Leadership Reporting`.

The Claude client-project workspace, no-live-connection boundary, confirmation-first status rule, single AI-readable Initiative Evidence and Decision File, and reporting-to-initiative-evidence write-back are governed by:

- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` (reusable schema; the evidence file is its client-copy implementation)
- `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`
- `02_coworker_artifact_interface/05_BIWEEKLY_PROGRAMME_UPDATE_INPUT_TEMPLATE.md`
- `06_operating_manual/02_CLIENT_PROJECT_WORKSPACE_GUIDE.md`

These files do not replace the existing lifecycle, route, approval, evidence, stage-closeout, or source-of-truth controls. Jira (initiative and delivery status), SharePoint (approved artefacts and evidence), and Omega 365 (action management) remain the client-facing operational tools. Claude has no permitted live connection to them and never claims it has read or updated a live client system.

## Executive Communication & Framing Standard

All executive presentations, board packs, CDO communications, Strateq DX materials, Quantuum materials, and tool-generated presentation outputs must follow the Communication & Framing Standard:

- Start with the executive decision or opportunity, not background.
- Frame around business outcomes, assurance, risk, value, and next decisions.
- Use a narrative arc: position → evidence → implication → recommendation → next step.
- Present recommendations clearly with action, rationale, benefit, and decision required.
- Avoid data dumps, preambles, technical-first explanations, and task-reporting.
- Preserve CDO positioning as translator, integrator, disruptor, and business-impact leader.

Canonical file:
`docs/presentation-standards/communication-and-framing-standard.md`
