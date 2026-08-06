# Artefact Writing Conventions

## Purpose

This file defines the default writing and formatting conventions for all Strateq DX CDO Coworker artefacts: tables, registers, process flows, spreadsheet cells, and prose.

These conventions apply alongside the output rules in `00_system_control/OPERATING_RULES.md`. RACI participation rules for the Digital Team and the prohibition on inventing RACI accountability are governed by `00_system_control/OPERATING_RULES.md`, not this file. The Initiative and Work-Item Identifier Control Rule is governed by `00_system_control/OPERATING_RULES.md`; this file does not restate it.

## 1. Default Shortform Writing Standard

All artefact content — tables, registers, process flows, spreadsheet cells, and prose — must use terse, telegraphic wording by default.

Rules:

- Remove unnecessary connective and filler language.
- Preserve the full meaning, control requirement, and technical detail.
- Prefer the shortest wording that remains unambiguous.
- Shortform means concise, not incomplete. Material scope, dependencies, decisions, risks, controls, and technical requirements must not be omitted.

Example:

| Verbose | Preferred |
|---|---|
| `Load approved budget into Chronos Budget Register via Excel upload` | `Load approved budget to Budget Register (Excel upload)` |

This standard applies to tables, registers, and prose equally. It extends the Output Rule in `00_system_control/OPERATING_RULES.md` and does not conflict with it.

## 2. Process-Flow Artefact Conventions

### 2.1 Document Title

- Use a clean document title only.
- Do not embed `DRAFT`, review instructions, or ceremonial governance wording in the title.
- For process-flow artefacts, draft state is indicated through the Process Agreement Status field defined in `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`, not embedded in the document title. Other artefact types use their own controlled draft or status mechanism (filename convention, sign-off block, or status field as governed by the relevant authority file). This file does not introduce a new universal status field.

### 2.2 Layout

- No separate legend or instruction row unless genuinely required to understand the artefact.
- Table headers begin at the first appropriate table row.
- Do not use decorative or status shading to indicate unresolved items.

### 2.3 Material Pending Items

Where a material uncertainty must remain visible in a process-flow artefact, record it as terse text in the `Comments` column, for example:

- `PENDING PowerBI session`
- `PENDING scoping`

Leave `Comments` blank where there is nothing material to record.

### 2.4 Preferred Column Terminology

Where the following concepts are present in a process-flow artefact, prefer these column names:

| Concept | Preferred column name |
|---|---|
| The process step being performed | `Current Process Step` |
| The system or tool capability the development team must deliver to enable the step | `Development Scope` |
| Material open items or pending confirmation | `Comments` |

`Development Scope` applies where the concept being captured is the system or tool capability Digital or development must build or configure to support the process step — not where the column describes a general future-state operational change or requirement. It does NOT assign Digital as Responsible or Accountable for executing the operational process step. See the Digital Team Operational RACI Boundary in `00_system_control/OPERATING_RULES.md`.

Do not hard-code this exact column set into every process artefact. Apply the preferred names where the concepts are present. Other column structures remain valid where the concepts differ.

## 3. Existing Conventions to Preserve

The following conventions, established across existing authority files, must not be regressed:

- Plain language over ceremonial wording.
- No loud draft banners in titles or table headers.
- Each artefact type uses its own controlled draft or status mechanism as governed by the relevant authority file; no new universal status field is introduced by this file.
- Short table labels.
- Only confirmed content in controlled artefacts.
- No speculative roles or mitigations.
- Real-world context in parentheses where it materially aids understanding.
- Named accountable owners only when genuinely confirmed.
- Standard controlled sign-off convention.
- Current confirmed evidence takes precedence over stale working references.

## Boundary

This file governs writing and formatting conventions. It does not define lifecycle stages, route rules, approval authority, source-of-truth governance, or identifier control. RACI participation rules and the Initiative and Work-Item Identifier Control Rule are in `00_system_control/OPERATING_RULES.md`. Process-flow output formats are governed by `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`. Process-flow session facilitation is governed by `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md`.
