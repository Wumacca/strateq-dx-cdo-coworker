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
docs/
```

## Folder Purposes

### 00_system_control
Controls how the repository is organised and how AI coworker support must behave. Includes the two-coworker client workspace and reporting protocol (`14`), the interactive session protocol (`12`), the initiative control record schema (`13`), the coworker router (`11`), and the coworker handover, lifecycle, operating, knowledge-capture, and vocabulary authority files. There are exactly two client-project lifecycle coworkers — the Hopper Lifecycle Coworker and the Live Delivery Coworker; Claude has no live connection to Jira, SharePoint, or Omega 365.

### 01_governance_lifecycle
Defines the governed Digital Governance / Digital Delivery lifecycle, starting with Hopper consolidation and Hopper priority screening, through route determination, Stage 1D / two-stage initiation, Completed Initiation Forms, and the Capex Request Session.

### 02_coworker_artifact_interface
Defines the working interface between the AI coworker and the Digital Lead, including the single AI-readable Initiative Evidence and Decision File template (`04`) and the bi-weekly programme update input template (`05`).

### 03_process_mapping
Defines how existing process matrices are converted into process mapping packs, Blueworks build briefs, bottleneck registers, and developer/vendor scope outputs.

### 04_intake_dispatch
Automatic Hopper clarification handling and Jira field-length rules for intake.

### 05_source_of_truth
The digital artefact governance model — how organisational artefacts are governed, classified, and updated; source-of-truth artefact control is a governed mode, not a separate coworker.

### 06_operating_manual
Human-facing, non-authoritative navigation: the governance and management manual (`01`) and the client project workspace guide (`02`).

### BOARD_INTERFACE
Board-facing, read-only repository index and briefing material.

### docs
Presentation and communication standards (for example the Communication & Framing Standard).

## Current Active Build Area

The active build area is:

```text
01_governance_lifecycle/
```

The immediate lifecycle focus is:

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
Initiation Form stage
```
