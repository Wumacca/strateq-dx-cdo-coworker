# Method Artefact Registry and Revision-Handshake Protocol

## Status

Mandatory global authority for **which reusable Strateq DX artefact revision a Coworker must use**, how a bound client resolves it, and the read/write boundary that keeps client data out of the method repository. This file applies to every model, tool, skill and governed session that generates, refreshes or populates a reusable artefact for a client.

It works with, and does not replace:

- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` — one-client binding and zero client crossover;
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` — client workspace, working authority and reporting;
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` — knowledge routing and controlled updates;
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` — artefact status, release and publication;
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` — the initiative schema several artefacts implement.

Where this file and a higher authority conflict, the higher authority governs and the conflict is surfaced to the Digital Lead (`CLAUDE.md` B4).

## Core principle

Strateq DX is the **single source of truth for reusable artefacts, templates, schemas and interface specifications**. A client Coworker may read both the Strateq DX method repository and its one bound client repository. It must:

1. retrieve the **latest approved** Strateq DX artefact revision (not an unpinned branch or an arbitrary uploaded file);
2. populate that artefact only with the **bound client's** information;
3. save the populated output **only in the bound client repository**.

No client data, client status, populated workbook or client-specific evidence is ever written into Strateq DX. The Strateq DX artefact is **read-only** during client work.

## 1. Reusable method artefact registry

This registry is the authoritative list of reusable artefacts clients adopt and populate. Each artefact has a stable `Artefact ID`. A revision label is `r<N>`, incremented whenever an approved change is made to the artefact **or** its interface/specification. The `Approving method commit` is the commit on the method repository default branch (`main`) at which that revision was approved.

| Artefact ID | Artefact name | Canonical repository path | Interface / specification path | Current approved revision | Approving method commit | Status | Superseded revisions | Compatibility notes | Client adoption requires explicit baseline update |
|---|---|---|---|---|---|---|---|---|---|
| `ART-PROGRAMME-WORKBOOK` | Strateq DX Digital Programme Workbook | `02_coworker_artifact_interface/blank_templates/Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx` | `02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md` | `r1` | `f8ffa9b` | Approved | none | Sheets: Programme Overview, Delivery Overview, Actions, Lists (hidden). Step-state + action-status dropdowns and date validation are structural; interface `r1` matches template `r1`. | Yes |
| `ART-PEP-WORKBOOK` | Strateq DX Live Delivery PEP Workbook | `02_coworker_artifact_interface/blank_templates/Strateq_DX_Live_Delivery_PEP_TEMPLATE.xlsx` | `02_coworker_artifact_interface/06_LIVE_DELIVERY_ARTEFACT_1_MODEL.md` (with `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md` and `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`) | `r1` | `b36e999` | Approved | none | PEP/client-control hierarchy; no dedicated single workbook interface file — governed by the three models cited. | Yes |
| `ART-MEETING-MINUTES` | Digital Team Meeting Minutes | `02_coworker_artifact_interface/blank_templates/Digital_Team_Meeting_Minutes_TEMPLATE.docx` | `06_operating_manual/02_CLIENT_PROJECT_WORKSPACE_GUIDE.md` | `r1` | `b36e999` | Approved | none | Human-facing minutes template; no machine interface. Formatting-only changes still increment the revision but need not force a baseline update. | No |
| `ART-INITIATIVE-EVIDENCE-FILE` | Initiative Evidence and Decision File | `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md` | `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` | `r1` | `bc1923c` | Approved | none | Client-copy implementation of the `13` schema; a schema change increments both and requires a baseline update. | Yes |
| `ART-INITIATIVE-DELIVERY-SETUP` | Initiative Delivery Setup Template | `02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md` | `02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md` | `r1` | `bc1923c` | Approved | none | Artefact 0 (exact title). Section changes increment the revision and require a baseline update. | Yes |

**Registry maintenance.** This registry is an open set. Any pull request that adds, renames, retires or changes an approved revision of a reusable artefact **or** its interface must update this registry in the same commit, set the new `Approving method commit`, move the prior revision into `Superseded revisions`, and (where `CLAUDE.md` B2 maps the artefact's interface) update B2, `00_system_control/FOLDER_MAP.md` and `README.md`. A `Superseded` artefact must not be resolved for new client work.

## 2. Deterministic artefact-resolution protocol (revision handshake)

Before **every** Coworker-generated refresh, workbook update, or population of any registered artefact, the Coworker must, in order:

1. **Bind exactly one client** under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`. If the binding is absent or ambiguous, stop (step 9).
2. **Read that client's `METHOD_BASELINE.md`** (or the equivalent method-reference control named in the client profile): the approved method commit and the per-artefact pinned revisions the client has adopted.
3. **Read this central registry** at the approved method commit. **If this registry file does not exist at that commit** — i.e. the client's approved method commit predates the introduction of `16_METHOD_ARTEFACT_REGISTRY.md`, or the required `Artefact ID` is not yet registered at that commit — treat the baseline as **stale/incompatible** and stop (step 9); do **not** fall back to reading the template at the stale commit, and do **not** assume the registry exists there. A baseline update to a method commit that contains this registry (and the required artefact row) is required first.
4. **Resolve the canonical artefact** — the row for the required `Artefact ID` — reading the file at its `Canonical repository path` as of the approved method commit.
5. **Compare** the client's pinned artefact revision with the registry's `Current approved revision`.
6. **Confirm the interface/specification version matches** the resolved artefact revision (the `Interface / specification path` at the same revision).
7. **Confirm the artefact is `Approved` and not `Superseded`.**
8. **Record in the working session** the resolved `Artefact ID`, revision and `Approving method commit` used (surfaced in the `12` Runtime Access Confirmation Gate / Live Session Status Board).
9. **Stop and ask the Digital Lead** (fail-closed, `CLAUDE.md` B5) if the client baseline is **stale** (pinned revision behind current approved, **or the approved method commit predates this registry / the artefact's registration**), **missing**, **ambiguous**, **incompatible** (interface/spec version mismatch), or the artefact is **superseded/withdrawn**. In every one of these cases the required next step is a Digital-Lead-approved baseline update to a method commit that contains this registry and the required approved artefact revision. Do not proceed on inference, do not read the artefact at a commit lacking the registry, do not silently upgrade the client's pinned revision, and do not ask-and-continue in the same turn.

A pinned revision is only changed by an explicit, Digital-Lead-approved baseline update in the client repository — never automatically by the Coworker.

## 3. "Latest" means latest **approved** revision

"Latest" is the `Current approved revision` recorded in this registry at the approved method commit. It is **not** the tip of an unpinned `main`, a work-in-progress branch, a draft, or an arbitrary file a user uploads into a session. An uploaded workbook is a supplied snapshot for reconciliation (`02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md`), never the reusable artefact source.

## 4. Permitted sources — and the no-crossover rule

When generating or populating an artefact for the bound client, the Coworker may use:

- the **central Strateq DX reusable artefact** resolved under section 2; and
- the **bound client's** current records, evidence, PEP/control record and actions in the one allowlisted client repository (and permitted client sources named in that client's `SOURCE_OF_TRUTH.md`).

The Coworker must **never combine client sources across clients**. Another client's repository, workspace, export, attachment or memory is a prohibited source even if technically accessible; its appearance is a contamination stop under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## 5. Write boundary

- Reusable artefacts, templates, schemas, interface specifications and this registry are maintained **in the Strateq DX method repository** only.
- **Populated** client workbooks and client status remain in the **relevant bound client repository** (or the client system named in its `SOURCE_OF_TRUTH.md`).
- **No** client status, client data, populated artefact or client-specific evidence is ever written back to Strateq DX. A reusable lesson may enter the method repository only after it is abstracted to remove all client-identifying data and the Digital Lead approves the method change (`00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`).
- During client work the Strateq DX method repository is **read-only**; the single write target is the bound client repository through its controlled branch or approved direct update.

There is no client write-back path into Strateq DX. The registry resolution is a **read** of the method repository followed by a **write** only into the client repository.

## 6. Client repository does not duplicate the reusable template

A client repository does **not** maintain an independent copy of the blank reusable Strateq DX template as if it were a second source of truth. It **references the central artefact revision through its `METHOD_BASELINE.md`** (Artefact ID + pinned revision + approving method commit). What the client repository holds is the **populated, client-specific output** produced from the resolved artefact — for example a populated programme workbook — which is client data and must stay client-side. When the central artefact advances, the client adopts the new revision through a controlled `METHOD_BASELINE.md` update; it does not fork or hand-maintain the reusable blank.

## 7. Standard client-adoption reference pattern

Future client repositories implement adoption through `METHOD_BASELINE.md` (a client-repository control listed in `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`). The pattern below is client-agnostic and contains **no client data**; a client repository fills the placeholders in its own repository, never here:

```text
# METHOD_BASELINE.md  (client repository)

Method repository:      <approved Strateq DX method repository>
Approved method commit: <full SHA on main>

## Adopted reusable artefacts (revision handshake)
| Artefact ID                   | Pinned revision | Approving method commit | Adopted on | Notes |
|-------------------------------|-----------------|-------------------------|------------|-------|
| ART-PROGRAMME-WORKBOOK        | r<N>            | <sha>                   | <date>     |       |
| ART-PEP-WORKBOOK              | r<N>            | <sha>                   | <date>     |       |
| ART-INITIATIVE-EVIDENCE-FILE  | r<N>            | <sha>                   | <date>     |       |
| ...                           | ...             | ...                     | ...        |       |

## Adoption rule
- Populated outputs are stored only in this client repository.
- No client data is written back to the method repository.
- A pinned revision changes only by a Digital-Lead-approved update to this file.
```

At resolution time the Coworker performs the section 2 handshake between each client-pinned revision here and the `Current approved revision` in the central registry, and fails closed on any stale, missing, ambiguous or incompatible baseline.

## Boundary

This registry adds no AI approval authority. The Coworker resolves, compares, records and fails closed; it does not approve a revision, upgrade a client baseline, merge/release a method change, or write client data into the method repository. Digital Lead approval governs every method-repository change and every client baseline update.
