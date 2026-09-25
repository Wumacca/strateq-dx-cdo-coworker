# Folder Map

## Purpose

This file defines the initial source-reference structure for the Strateq DX CDO Coworker repository.

## Folder Structure

```text
AGENTS.md
CLAUDE.md
CHATGPT_PROJECT_INSTRUCTIONS.md
00_system_control/
01_governance_lifecycle/
02_coworker_artifact_interface/
02_coworker_artifact_interface/blank_templates/
03_process_mapping/
04_intake_dispatch/
05_source_of_truth/
06_operating_manual/
BOARD_INTERFACE/
.codex/skills/
docs/
```

### Repository root

Contains the cross-model entry instructions (`AGENTS.md`), deterministic authority and lifecycle map (`CLAUDE.md`), and the non-authoritative build-only ChatGPT Project description (`CHATGPT_PROJECT_INSTRUCTIONS.md`). The Project description routes users to repository authority and never replaces it.

## Folder Purposes

### 00_system_control
Controls how the repository is organised and how AI Coworker support must behave. Includes the two-coworker client workspace and reporting protocol (`14`), client context isolation standard (`15`), method artefact registry and revision-handshake protocol (`16`), interactive session protocol (`12`), initiative control record schema (`13`), router (`11`), and the handover, lifecycle, operating, knowledge-capture and vocabulary authority files. Client work must bind one private client repository before any client source is read or written, and must resolve the latest approved reusable artefact revision through `16` before generating, refreshing or populating any artefact.

### 01_governance_lifecycle
Defines the governed Digital Governance / Digital Delivery lifecycle, starting with Hopper consolidation and priority screening, through route determination and initiation, into authorised mobilisation, live delivery, adoption / handover and closure. Stage 3 is governed by `01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`.

### 02_coworker_artifact_interface
Defines the working interface between the AI Coworker and the Digital Lead, including the single AI-readable Initiative Evidence and Decision File template (`04`), programme reporting input (`05`), Live Delivery Artefact 1 model (`06`), Initiative Delivery Setup model and template (`07` and `08`), and the programme/portfolio workbook interface (`10`).

`09_COCKPIT_FEED_CONTRACT.md` is the approved versioned cockpit projection
specification. Its client-adoption and activation gates preserve client isolation,
source-of-truth ownership and human-approved stage progression. It does not
introduce a live feed, a second initiative record or an additional coworker.

`10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md` is the method specification for
the Strateq DX Digital Programme Workbook — the governed human-facing
programme/portfolio interface and working snapshot (contract and initiative
management, lifecycle/current-step visibility, delivery milestones, open/overdue
actions, owners, due dates, notes and delivery-system references). It defines the
upload/reconciliation and Coworker-generated-refresh workflows, versioning,
status safeguards and source-of-truth boundaries. The workbook is an interface
and snapshot only; it never replaces the Initiative Evidence and Decision File,
PEP/control record, approved action system, formal approval records, evidence
registers or source-of-truth artefact governance.

`blank_templates/` holds the client-agnostic binary delivery templates that the models above describe: the Strateq DX Live Delivery PEP workbook (`Strateq_DX_Live_Delivery_PEP_TEMPLATE.xlsx`), the Strateq DX Digital Programme Workbook (`Strateq_DX_Digital_Programme_Workbook_TEMPLATE.xlsx`, described by `10`) and the Digital Team Meeting Minutes document (`Digital_Team_Meeting_Minutes_TEMPLATE.docx`). These are the single canonical blank sources. The Coworker resolves a canonical template from the approved Strateq DX method commit (revision-handshake in `16`) and uses it to generate the populated client-side output; the reusable blank templates are not stored or maintained in client repositories, and are never filled with client data in this public method repository.

### 03_process_mapping
Defines how existing process matrices are converted into process mapping packs, Blueworks build briefs, bottleneck registers, and developer/vendor scope outputs.

### 04_intake_dispatch
Automatic Hopper clarification handling and optional Jira field-length rules for clients whose controlled-system profile selects Jira.

### 05_source_of_truth
The digital artefact governance model — how organisational artefacts are governed, classified, and updated; source-of-truth artefact control is a governed mode, not a separate coworker.

### 06_operating_manual
Human-facing, non-authoritative navigation: the governance and management manual (`01`) and the client project workspace guide (`02`).

### BOARD_INTERFACE
Board-facing, read-only repository index and briefing material.

### .codex/skills

Reusable model-agnostic Coworker entry points. Skills route to the authority files; they do not duplicate client data or replace the governed method.

### docs
Presentation and communication standards (for example the Communication & Framing Standard).

## Current Active Build Area

The current governed build spans:

```text
00_system_control/
01_governance_lifecycle/
02_coworker_artifact_interface/
.codex/skills/
```

The lifecycle now continues from intake through delivery:

```text
Existing Hopper items
↓
Hopper consolidation
↓
Light-touch scoping with departments
↓
Hopper Priority Screen
↓
DRB priority discussion
↓
Approved / clarify / defer / reject / BAU / merge
↓
Approved route trigger or alternative mobilisation authority
↓
Authorised
↓
Mobilising — Initiative Delivery Setup
↓
In Delivery — PEP / client-control plan and Artefact 1
↓
Adoption / Handover
↓
Closed / Retired
```
