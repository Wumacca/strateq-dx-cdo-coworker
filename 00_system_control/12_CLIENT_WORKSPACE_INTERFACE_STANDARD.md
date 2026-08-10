# Client Workspace Interface Standard

## Status

Authority file. This is the single source for how the reusable Strateq DX Build method, the coworker system, and any future application resolve and interface with a client-specific workspace.

> **File numbering note.** The numeric shorthand `12` used elsewhere in this repository refers to `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`. This standard must always be cited by its full path, `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`, never as bare `12`. The two files are complementary and neither overrides the other: the Interactive Governed Session Protocol governs the interactive session sequence; this file governs client workspace resolution and the method / programme-truth boundary. Where a renumbering PR is raised, it must update every reference under the PR maintenance rule in `CLAUDE.md`.

## 1. Purpose and Boundary

### Purpose

This standard defines how a governed coworker session, and any future application built on this method, resolves the **active client workspace** and interfaces with it, without storing client-specific programme truth in the DX Build repository.

It exists to keep two things permanently separate:

- the **reusable method** — how governed digital transformation work is run;
- the **client programme truth** — what is actually true, approved, delivered, spent, evidenced, and outstanding for one named client.

### Core architecture decision

> The DX Build repository defines the method. The active client workspace holds programme truth. No coworker or future app workflow may assert client programme status until the active client workspace has been resolved and the client `PROGRAMME_STATUS.md` has been loaded.

### Confirmation authority

> The Digital Lead is the sole confirmation authority for programme status. The accepted delivered artefact remains the evidence basis. `PROGRAMME_STATUS.md` is the live controlled status surface.

Digital Lead confirmation is a **control act against the accepted artefact**, not an evidence source in itself. Recollection, chat memory, or an unevidenced verbal position must never be recorded as the evidence basis. Where the Digital Lead confirms a position for which no accepted artefact is yet available, the record is confirmed with the evidence pointer left explicitly open and the confidence marked accordingly.

### Boundary

This standard does not:

- override `CLAUDE.md`, the programme lifecycle map, the operating rules, the route rules, or source-of-truth governance;
- replace the Interactive Governed Session Protocol (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`) — client workspace resolution runs **before** and **feeds** the interactive gates;
- replace the client workspace and reporting protocol (`00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`), which governs the Claude Project workspace, thread model, and reporting cycles;
- create a live connection to any client system;
- extend AI authority beyond `00_system_control/OPERATING_RULES.md`.

## 2. Rule — DX Build Stores Method Only

The DX Build repository (`strateq-dx-cdo-coworker`) may contain only:

- reusable standards;
- schemas;
- templates;
- routing rules;
- interface contracts;
- generic, anonymised examples;
- coworker method files;
- human-facing operating manuals and presentation standards.

The DX Build repository must **not** contain:

- client programme status;
- client initiative names, figures, costs, savings, or capital values;
- client maturity scores or benchmark results;
- client approval names, approver identities, or decision records;
- client artefact records, registers, or evidence;
- client handover records;
- client-specific capex packs or Board decks;
- any real client registry or manifest instance.

Where an existing DX Build file names a real client, that is a defect to be raised for correction, not a precedent.

## 3. Rule — Client Repos Store Programme Truth

Each client has one client workspace, held in its own repository or controlled location, for example:

```text
C:/Documents/GitHub/Clients/<client_id>
```

The client workspace holds:

- `00_system_control/CLIENT_CONTEXT_MANIFEST.md` (or `.json`) — the client manifest instance;
- `00_system_control/PROGRAMME_STATUS.md` — the live controlled status surface;
- the artefact register;
- the decision register;
- the evidence register;
- the handover register;
- Initiative Evidence and Decision Files;
- client-specific packs, decks, and reports.

Programme truth is written to the client workspace, never to DX Build.

## 4. Active Client Workspace Resolution Gate

### Core sequence

Every session that concerns a client programme must run this sequence before any substantive client output:

1. Identify active client.
2. Load active client `CLIENT_CONTEXT_MANIFEST`.
3. Confirm client repo root and required files exist.
4. Load active client `PROGRAMME_STATUS.md`.
5. Load DX Build authority files.
6. Apply lifecycle routing.
7. Proceed only after required gates are satisfied.

### Gate output

The coworker must present a session start declaration before substantive work:

| Gate item | Position |
|---|---|
| Active client | *client_name (client_id)* |
| Client repo root | *path* |
| Manifest loaded | Yes / No — *path* |
| Manifest `last_validated` | *date* |
| `PROGRAMME_STATUS.md` loaded | Yes / No — *path* |
| Programme status revision / date | *value* |
| Required registers present | *list, with any missing named* |
| Write mode | proposal_only / approved_write / read_only |
| DX Build authority files loaded | *list* |
| Lifecycle stage identified | *stage* |
| Gate result | Resolved / Access gap / Stop and ask |

The session proceeds only when the Digital Lead confirms.

### Relationship to the other gates

Client workspace resolution precedes, and does not replace:

- the Claude Opus Access Confirmation Gate in `CLAUDE.md`;
- the Runtime Access Confirmation, Client Context, Confirmation-First Status, Initiative Reconciliation, and Required Inputs gates in `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`.

Resolution establishes **which** client and **which** files. The Confirmation-First Status Gate establishes whether the loaded business position is still current. Neither substitutes for the other.

## 5. Required Client Manifest

Every client workspace must hold one manifest instance conforming to `00_system_control/CLIENT_CONTEXT_MANIFEST_SCHEMA.md`.

The manifest is the addressing record for the client workspace. It declares the repo root, the paths to the required programme files, the client-facing system keys, the confirmation authority, and the write mode.

The schema lives in DX Build. The manifest instance lives in the client workspace. DX Build must never hold a populated manifest for a real client.

## 6. Required Client Programme Files

A client workspace is only resolvable when the following exist and are addressable from the manifest:

| # | File | Purpose | Required |
|---:|---|---|---|
| 1 | `CLIENT_CONTEXT_MANIFEST` | Addressing and control record for the workspace | Mandatory |
| 2 | `PROGRAMME_STATUS.md` | Live controlled status surface, built from `00_system_control/PROGRAMME_STATUS_TEMPLATE.md` and governed by `00_system_control/PROGRAMME_STATUS_RULES.md` | Mandatory |
| 3 | Artefact register | Controlled artefacts, revisions, active / superseded state | Mandatory for source-of-truth and closeout sessions |
| 4 | Decision register | Decisions, decision basis, approver, date | Mandatory for approval, capex, and DRB sessions |
| 5 | Evidence register | Accepted delivered artefacts and evidence pointers | Mandatory for any evidenced claim |
| 6 | Handover register | Issued handovers, their state, and staleness | Mandatory for handover sessions |

Where a required file for the session type is missing, the gate result is **Access gap**. The coworker states which file is missing and stops.

## 7. Read / Write Boundary

| Actor | May read | May write |
|---|---|---|
| Coworker (default) | DX Build method files; active client manifest; active client `PROGRAMME_STATUS.md`; active client registers; supplied exports, snapshots, and evidence | Nothing. Proposes controlled updates only |
| Coworker (where `write_mode: approved_write` and the Digital Lead has approved the specific update) | As above | The named client workspace file, for the approved update only |
| Coworker | — | Never Jira, SharePoint, or Omega 365. Claude has no live connection to any client system |
| Digital Lead | All | All, as confirmation authority |

Every proposed client-workspace update is labelled:

> `Recommended update — requires Digital Lead approval.`

Every proposed client-system update (Jira, SharePoint, Omega 365) is labelled:

> `Recommended update — requires Digital Lead approval and physical update in the client system.`

A client-system update is marked complete only when the Digital Lead explicitly confirms the physical update occurred. The coworker must never claim it has read or updated a live client system.

## 8. Source Precedence

Where sources disagree, apply this precedence:

1. **Accepted delivered artefact** — the evidence basis. A signed, issued, or formally accepted artefact overrides any presented draft, summary, or deck.
2. **Active client `PROGRAMME_STATUS.md`** — the live controlled status surface, where the record carries a valid evidence pointer.
3. **Client registers** — artefact, decision, evidence, and handover registers.
4. **Initiative Evidence and Decision Files** — per-initiative continuity records.
5. **Supplied exports, snapshots, and in-session evidence** — current Jira export, Board deck, finance reconciliation, adoption record.
6. **DX Build method files** — authoritative for *how*, never for *what is true about a client*.
7. **Inference** — never a source. Inferred positions are labelled as inference and carry no evidence pointer.

Chat memory, synced project knowledge, prior session recollection, and last-used client context are **not sources** at any tier.

Where the accepted artefact and `PROGRAMME_STATUS.md` conflict, the artefact governs the figure and `PROGRAMME_STATUS.md` is corrected by supersession under `00_system_control/PROGRAMME_STATUS_RULES.md`. The conflict is surfaced to the Digital Lead before any output uses either figure.

## 9. Fail-Closed Rule

> If the active client cannot be identified, the client manifest cannot be loaded, required client files are missing, or programme status conflicts cannot be resolved, the coworker must stop and ask the Digital Lead. It must not proceed on inference, last-used client context, chat memory, or partial file access.

The stop response must state:

1. what was resolved;
2. what could not be resolved;
3. the exact file, path, or decision required to proceed;
4. the question to the Digital Lead.

There is no partial-proceed. A session that cannot resolve the active client produces no client programme status, no capex output, no handover, and no controlled update.

## 10. Future App / Tenant Interface Model

The same resolution contract supports a future application or multi-tenant service. No client programme truth moves into DX Build to enable it.

```text
Client Registry
→ Client Context Manifest
→ Programme Status
→ Artefact / Decision / Evidence / Handover Registers
→ Coworker workflow execution
```

### Layer responsibilities

| Layer | Holds | Lives in |
|---|---|---|
| Client Registry | The set of known clients and the pointer to each client's manifest | Local environment configuration or future-app tenancy configuration |
| Client Context Manifest | Addressing, paths, keys, confirmation authority, write mode | The client workspace |
| Programme Status | The live controlled status surface | The client workspace |
| Registers | Artefacts, decisions, evidence, handovers | The client workspace |
| Coworker workflow execution | The method — standards, schemas, templates, routing, interface contracts | DX Build |

### Permitted app / coworker behaviour

The app or coworker may:

- read current client status;
- propose controlled updates;
- write only after Digital Lead approval, where write capability exists.

Write capability is governed by the manifest `write_mode` field, which defaults to `proposal_only`. A tenancy configuration must not raise `write_mode` without a recorded Digital Lead decision.

> The real active-client registry is local, environment-specific, or future-app tenancy configuration. It must not contain real client programme truth in the DX Build repo.

The only registry artefact permitted in DX Build is the anonymised example, `00_system_control/CLIENT_CONTEXT_REGISTRY.example.json`.

## 11. Prohibited Behaviour

The coworker and any future app must not:

- assert client programme status before the active client workspace is resolved and `PROGRAMME_STATUS.md` is loaded;
- default to the last-used client, the most recently discussed client, or the only client it has ever seen;
- infer the active client from a file name, a figure, a person's name, or a chat reference;
- write client-specific programme truth into DX Build;
- create a real client manifest, registry, or `PROGRAMME_STATUS.md` inside DX Build;
- treat Digital Lead recollection as the evidence basis;
- treat `PROGRAMME_STATUS.md` as the evidence itself rather than the controlled index pointing to evidence;
- proceed on partial file access;
- claim a live read or update of Jira, SharePoint, or Omega 365;
- apply a controlled update without explicit Digital Lead approval;
- silently continue on a stale handover after programme status has moved.

## 12. Validation Checklist

Run before closing any session that touched client workspace resolution, and before merging any PR that changes this interface.

| # | Check | Pass condition |
|---:|---|---|
| 1 | Active client identified explicitly | Client named by the Digital Lead or by an unambiguous session parameter, not inferred |
| 2 | Manifest loaded | Manifest path resolved, schema-valid, `status: active` |
| 3 | Repo root confirmed | `client_repo_root` exists and is readable |
| 4 | `PROGRAMME_STATUS.md` loaded | Loaded from the client workspace path, revision and date stated |
| 5 | Required registers present for the session type | Present, or the gap is named and accepted by the Digital Lead |
| 6 | Write mode respected | No write attempted beyond the declared `write_mode` |
| 7 | Source precedence applied | Accepted artefact governs where figures conflict |
| 8 | Confirmation-First Status Gate run | Held position presented with source and date; Digital Lead confirmed or corrected |
| 9 | Fail-closed honoured | No client output produced from an unresolved or partially resolved workspace |
| 10 | No client truth written to DX Build | Diff of the DX Build repository contains no client-specific values, names, figures, or records |
| 11 | Handover staleness checked | Downstream handovers reissued where programme status moved |
| 12 | Updates labelled | Every proposed update carries the correct approval label |

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
