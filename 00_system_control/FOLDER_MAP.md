# Folder Map

## Purpose

This file defines the initial source-reference structure for the Strateq DX CDO Coworker repository.

## Folder Structure

```text
00_system_control/
01_governance_lifecycle/
02_coworker_artifact_interface/
03_process_mapping/
04_intake_dispatch/
05_source_of_truth/
06_operating_manual/
BOARD_INTERFACE/
.codex/skills/
docs/
```

## Folder Purposes

### 00_system_control
Controls how the repository is organised and how AI Coworker support must behave. Includes the two-coworker client workspace and reporting protocol (`14`), client context isolation standard (`15`), interactive session protocol (`12`), initiative control record schema (`13`), router (`11`), and the handover, lifecycle, operating, knowledge-capture and vocabulary authority files. Client work must bind one private client repository before any client source is read or written.

### 01_governance_lifecycle
Defines the governed Digital Governance / Digital Delivery lifecycle, starting with Hopper consolidation and priority screening, through route determination and initiation, into authorised mobilisation, live delivery, adoption / handover and closure. Stage 3 is governed by `12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md`.

### 02_coworker_artifact_interface
Defines the working interface between the AI Coworker and the Digital Lead, including the single AI-readable Initiative Evidence and Decision File template (`04`), programme reporting input (`05`), Live Delivery Artefact 1 model (`06`), and Initiative Delivery Setup model and template (`07` and `08`).

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
