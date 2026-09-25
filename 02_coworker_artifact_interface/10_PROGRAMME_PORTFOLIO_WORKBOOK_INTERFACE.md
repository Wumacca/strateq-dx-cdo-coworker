# Programme / Portfolio Workbook Interface

## Status

Reusable method specification for the **Strateq DX Digital Programme Workbook** — a governed human-facing programme/portfolio interface and working snapshot. This file is method authority. The blank binary template it describes is:

`02_coworker_artifact_interface/blank_templates/Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx`

The public method repository holds only the blank, client-agnostic template and these reusable rules. It must contain zero client data (`00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`). Each client copies the template into its own bound private client repository and populates it there.

## Purpose

The workbook gives the Digital Lead a single, manually maintained surface to see and manage a delivery portfolio across contracts and initiatives, and to hand that snapshot to the AI Coworker for status/action extraction and for Coworker-generated refreshed versions.

It supports:

- programme-level management;
- contract-level management;
- contained initiative management;
- lifecycle / current-step visibility;
- delivery milestones;
- open and overdue actions;
- owners and due dates;
- notes and delivery-system references;
- regular manual updates by the Digital Lead;
- upload into the AI Coworker for status/action extraction;
- Coworker-generated refreshed versions when requested.

## What the workbook is — and is not

The workbook is a **governed interface and working snapshot**. It is a projection and working aid, not a control record.

It is **not**, and must never be treated as, a replacement for:

- the Initiative Evidence and Decision File (`02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`, schema `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`);
- the PEP / client-control record;
- the approved action-management system named in the client profile;
- formal approval records (Completed Initiation Form and DRB decisions);
- evidence registers;
- source-of-truth artefact governance (`05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`).

Where the workbook and any controlled record disagree, the controlled record governs and the difference is surfaced to the Digital Lead, never silently applied.

## Sheet structure

The template contains four sheets. `Lists` is hidden and drives the dropdowns; the other three are working surfaces. Sheet names, structure, formulas and dropdowns are fixed method scaffolding — do not rename or restructure them when adopting the template; enter client content into the cells only.

### 1. `Programme Overview`

Programme-level roll-up. One row per initiative, grouped under its contract, showing the initiative and its current lifecycle step across the six macro steps (`1. Commercial Approval`, `2. Mobilising`, `3. In Delivery`, `4. UAT`, `5. Live`, `6. Adopted`). Values are pulled by formula from `Delivery Overview`; this sheet is read-mostly and is not the place to type status.

> **Initiative currency rule (client copy).** In a populated client copy, the
> initiative rows must be labelled with the **latest approved initiative names for
> each contract** and must always reflect the **latest list of initiatives
> currently being worked, grouped by contract**. Generic labels such as
> `Initiative 1` must **not** appear in a populated workbook. Each initiative must
> carry a **stable, unique identifier or approved delivery-system reference** (the
> `Delivery-system ref` column, using the system named in the client's
> `SOURCE_OF_TRUTH.md`) so it can be matched to its controlled record across
> refreshes. The client working copy must be updated whenever the approved
> contract initiative list changes: every Coworker-generated refresh brings the
> rows current against the confirmed controlled records — adding newly approved
> initiatives under their contract, and moving completed, closed or retired ones
> to their correct lifecycle status rather than leaving stale entries. This
> currency rule applies to the client copy only; the **blank template may retain
> placeholder slots** (`Contract 1–3`, `Initiative 1–3`) and the public method
> repository keeps only those client-agnostic placeholders.

### 2. `Delivery Overview`

The primary working sheet. Structure:

| Area | Meaning |
|---|---|
| Contract group header | A contract / programme grouping (`Contract 1`, `Contract 2`, `Contract 3` in the blank template). Rename to the client's contract or programme grouping. |
| Contract / initiative (col A) | The initiative name within the contract. Blank rows are spare slots. |
| Delivery-system ref (col B) | Free-text reference to the record in the client's delivery system (the system named in the client's `SOURCE_OF_TRUTH.md`; no platform is assumed). |
| Current Step (col C) | Computed from the milestone cells; a projection, not an approval. |
| PEP milestone columns (cols D–M) | The ten PEP milestones grouped under the six macro steps: `Leadership Approval`, `Vendor Onboarded`, `Project kick-off`, `PEP Build`, `Work Delivered`, `Functional Testing`, `UAT approval`, `Go-live`, `Hypercare`, `Adoption (30-day)`. Each cell takes a **Step state** dropdown value. |
| Actions (Open) / (Overdue) (cols N–O) | Counted by formula from the matching initiative block on `Actions`. |
| Notes (col P) | Free text. |
| Contract key / helper (cols Q–R) | Helper columns that build the initiative keys used by the dropdowns; keep, do not repurpose. |

### 3. `Actions`

The action tracker, blocked into the same contract → initiative groups as `Delivery Overview`. Columns: `Action ID`, `Action`, `Owner`, `Due`, `Status`, `Notes`, `Overdue`. `Status` uses the **Action status** dropdown; `Due` takes a date; `Overdue` is computed (an action is overdue when it is dated, still open/in-progress/blocked, and past today). Group and sub-group header rows show live open/overdue counts by formula.

### 4. `Lists` (hidden)

The controlled dropdown vocabulary and helper lists that drive validation:

| List | Values |
|---|---|
| Step state (milestone cells) | `● Complete`, `● In Progress`, `● Not started`, `● Not required`, `● Blocked` |
| Status (initiative lifecycle) | `● Hopper Backlog`, `● Initiation Form in Progress`, `● Mobilising`, `● In Delivery`, `● Operational / Live`, `● Closed / Retired`, `● Paused (On Hold)` |
| RAG | `Green`, `Amber`, `Red` |
| Action status | `Open`, `In progress`, `Blocked`, `Done`, `Cancelled` |
| Action step | the ten PEP milestones plus `General` |
| Initiative keys / Contracts | helper keys built from the working sheets |

These lists align with the Stage 3 Live Delivery labels in `00_system_control/CONTROLLED_VOCABULARY.md`. Adjust list membership only through a controlled change, and keep it reconciled with the controlled vocabulary.

## Upload and reconciliation workflow

An uploaded workbook is a **supplied snapshot; it is not automatically current.** When the Digital Lead uploads a populated workbook for status/action extraction, the Coworker must:

1. Apply the **Confirmation-First Status Gate** (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`, `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`): present the held position with its source and date and ask the Digital Lead to confirm or correct before any workbook value is treated as current.
2. Confirm the single-client binding (`00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`) before reading the workbook as client content; stop closed on any client-boundary mismatch.
3. Reconcile the workbook against the controlled records: the Initiative Evidence and Decision File, the PEP / client-control record, meeting minutes, the approved action-management system and other approved evidence named in the client's `SOURCE_OF_TRUTH.md`.
4. Classify every reconciled difference and present them for decision — never apply them silently:

   | Classification | Meaning |
   |---|---|
   | Unchanged | Workbook matches the controlled record. |
   | Proposed update | Workbook carries a change to reconcile into the controlled record, subject to Digital Lead approval. |
   | New record | Workbook contains an initiative or action not yet in the controlled records. |
   | Missing record | A controlled record is absent from the workbook (a blank cell does not by itself mean "not required"). |
   | Conflict | Workbook and a controlled record disagree; the controlled record governs pending Digital Lead decision. |
   | Stale value | Workbook value is older than a confirmed controlled position. |
   | Unresolved identity | An initiative/action cannot be matched to a controlled record with confidence. |

5. Under the update-once rule, reconcile confirmed changes into the affected Initiative Evidence and Decision File and PEP / control record **before** any report or refreshed workbook is generated.

## Status safeguards

- An uploaded workbook is a supplied snapshot, not automatically current; the Confirmation-First Status Gate applies before any value is used.
- The Coworker must not silently overwrite controlled records; differences are surfaced and classified for Digital Lead decision.
- Lifecycle labels and milestone cells are **projections / signals, not proof** of approval or completion. `Released`/`Published`, approval and go-live are evidenced only in the controlled records and formal approval artefacts.
- Blank cells do **not** automatically mean "not required"; an unpopulated cell is unknown until reconciled.
- Manually entered action counts and typed statuses must **not** override reconciled action records from the approved action-management system.
- A populated client copy must use the latest approved initiative names per contract with a stable, unique identifier or approved delivery-system reference for each initiative; generic placeholder labels (e.g. `Initiative 1`) must not remain in a populated workbook (see the Initiative currency rule).
- Client adoption of this workbook as a working surface requires a client-specific source-of-truth decision recorded in that client's profile; it does not change any controlled record on its own.
- The public method repository must contain only the blank template and these reusable method rules.

## Generated-output workflow

When the Digital Lead requests a refreshed version, the Coworker generates it **from the reconciled, Digital-Lead-confirmed controlled records**, not from the raw uploaded snapshot. The refreshed initiative rows must satisfy the Initiative currency rule above — reflecting the latest live list of initiatives per contract, with new initiatives added under their contract and completed/closed/retired initiatives shown at their correct lifecycle status rather than left stale. A generated workbook is a projection / snapshot for the requested cut-off; it carries its source and date, does not become a second source of truth, and does not perform any external write-back. External publication and any client-system write-back remain `Recommended update — requires Digital Lead approval and physical update in the destination system.` until completion is evidenced.

## Versioning

- The blank template in this repository is the single canonical client-agnostic source; it is never populated here.
- Each client copies the template into its bound private client repository and versions its populated copy there under that client's controls.
- A Coworker-generated refreshed workbook is a dated snapshot for a stated cut-off; it does not supersede the controlled records and is retained per the client's working-authority and artefact-governance rules.

## Source-of-truth boundary

The workbook sits alongside, and never above, the controlled architecture in `00_system_control/OPERATING_RULES.md` and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. It is an interface and working snapshot. The Initiative Evidence and Decision File, the PEP / client-control record, the approved action-management system, the formal approval records and the source-of-truth artefacts remain the authorities. Reconciliation flows into those records under the update-once rule; the workbook never becomes a parallel ledger.

## Governing-file dependencies

- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` — Confirmation-First Status Gate and gate sequence.
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` — the initiative fields the workbook projects.
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` — confirmation-first reporting, update-once and reporting flow.
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` — single-client binding and zero client data in this repository.
- `00_system_control/CONTROLLED_VOCABULARY.md` — the Stage 3 lifecycle, step-state and status labels used by the dropdowns.
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` — artefact status, release/publication boundary.
- `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md` — the delivery stage the workbook surfaces.

## Boundary

The Coworker may inspect, reconcile, classify, draft and prepare a refreshed workbook within the bound client's approved branch. It cannot approve governance decisions, stage transitions, acceptance or go-live, cannot treat the workbook as a controlled record, and cannot state that an external publication or write-back occurred without Digital Lead confirmation.
