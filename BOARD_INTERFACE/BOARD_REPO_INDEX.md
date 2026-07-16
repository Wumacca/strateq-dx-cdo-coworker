# BOARD REPO INDEX — Strateq DX CDO Coworker

**Classification:** Board-Facing Advisory — Read Only  
**Date:** 2026-07-16  
**Purpose:** Provide the Board with a navigable index of current repository structure.

---

## 1. Main Source-of-Truth Files and Folders

| File / Folder | Description |
|---|---|
| `CLAUDE.md` | Role definition, operating authority, required behaviour, prohibited behaviour, and model guidance. Primary coworker instruction file. |
| `README.md` | Repository overview and entry-point index. |
| `00_system_control/` | System control files: lifecycle map, operating rules, controlled vocabulary, coworker handover model, knowledge capture rules, governed workflow looping standard, coworker router, interactive governed session protocol, initiative control record schema, and client workspace/reporting protocol. |
| `00_system_control/CONTROLLED_VOCABULARY.md` | Controlled terminology for the programme. |
| `00_system_control/FOLDER_MAP.md` | Folder structure reference. |
| `00_system_control/OPERATING_RULES.md` | Binding operating rules for all coworker sessions. |
| `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` | **Machine / authority file.** Global authority for how material coworker sessions run interactively. |
| `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` | **Machine / authority file.** Reusable schema for initiative control fields. Jira remains the target-state live record. |
| `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` | **Machine / authority file.** Governs the client Claude Project structure, no-live-client-system boundary, confirmation-first rule, initiative evidence continuity, and reporting-to-evidence write-back. |
| `05_source_of_truth/` | Source-of-truth governance model. |
| `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` | Defines how digital artefacts are governed, classified, and updated. |
| `06_operating_manual/01_DIGITAL_TRANSFORMATION_GOVERNANCE_AND_MANAGEMENT_MANUAL.md` | **Human-facing navigation manual — non-authoritative.** Explains the governed lifecycle. |
| `06_operating_manual/02_CLIENT_PROJECT_WORKSPACE_GUIDE.md` | **Human-facing navigation guide — non-authoritative.** Explains the practical one-client-project, one-thread-per-initiative, bi-weekly and monthly reporting setup. |

> **Machine / authority files vs human-facing navigation.** Authority files control coworker behaviour. Operating manuals and workspace guides are human navigation only and remain subordinate to the authority files they reference.

---

## 2. Workflow Files

| File | Description |
|---|---|
| `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` | Full programme lifecycle: stages, coworker paths, handover points, Hopper Lifecycle reference. |
| `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` | Governed workflow loop rules: proportionality, stage segregation, route-aware closeout, knowledge capture, CDO QA advisory. |
| `01_governance_lifecycle/00_REQUEST_INTAKE_MODEL_FUTURE.md` | Future-state public request intake model. |
| `01_governance_lifecycle/01_HOPPER_CONSOLIDATION_MODEL.md` | Rules for consolidating initiatives into the Hopper. |
| `01_governance_lifecycle/02_HOPPER_PRIORITY_SCREEN_MODEL.md` | Priority screening model for Hopper initiatives. |
| `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md` | Stage gate rules for moving from Hopper to Initiation. |
| `01_governance_lifecycle/04_INITIATION_FORM_INTAKE_MODEL.md` | Initiation form intake and processing model. |
| `01_governance_lifecycle/05_ROUTE_RULES.md` | Route determination rules. |
| `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md` | Optional DRB meeting-support text output model. |
| `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` | Two-stage initiation model definition. |
| `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md` | Development route Stage 1D model and exception triggers. |
| `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md` | Governing model for Hopper Portfolio Readiness Review. |
| `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md` | Authority for the formal DRB-facing Completed Initiation Form. |
| `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md` | Governing model for the Capex Request Session. |
| `03_process_mapping/01_PROCESS_MAPPING_MATRIX_INPUT_RULES.md` | Input rules for process mapping sessions. |
| `03_process_mapping/02_CREATE_PROCESS_MAPPING_PACK.md` | Process for creating a process mapping pack. |
| `03_process_mapping/03_BLUEWORKS_BUILD_BRIEF_RULES.md` | Rules for Blueworks build briefs. |
| `03_process_mapping/04_PROCESS_ARTIFACT_OUTPUT_MODEL.md` | Output model for process artefacts. |
| `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` | Swimlane process flow standard. |
| `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md` | Live session facilitator guide for process mapping. |
| `04_intake_dispatch/01_AUTOMATIC_HOPPER_CLARIFICATION_HANDLER.md` | Automatic handler for Hopper clarification inputs. |
| `04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md` | Jira field length rules for intake. |

---

## 3. Coworker and Client-Interface Files

| File | Description |
|---|---|
| `00_system_control/04_COWORKER_HANDOVER_MODEL.md` | Rules for handover between lifecycle coworkers. |
| `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` | Knowledge capture and source-of-truth update rules. |
| `00_system_control/11_COWORKER_ROUTER.md` | Routes each coworker session to the correct jurisdiction and authority files. |
| `02_coworker_artifact_interface/01_HOPPER_COWORKER_INTERFACE.md` | Interface model between Hopper lifecycle and coworker outputs. |
| `02_coworker_artifact_interface/02_HUMAN_FEEDBACK_INPUT_TEMPLATES.md` | Templates for human feedback input. |
| `02_coworker_artifact_interface/03_DECISION_FEEDBACK_TEMPLATES.md` | Templates for decision feedback capture. |
| `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md` | Reusable client-copy template for the AI-readable initiative evidence and decision continuity file. It is not a live GitHub initiative record. |
| `02_coworker_artifact_interface/05_BIWEEKLY_PROGRAMME_UPDATE_INPUT_TEMPLATE.md` | Structured Digital Lead input for confirming or correcting initiative positions before bi-weekly reporting. |

---

## 4. Operating Boundaries

- Jira remains the client-facing initiative and delivery-status system.
- SharePoint remains the organisational source-of-record artefact store.
- Omega 365 remains the action-management system.
- Claude has no permitted live connection to those client systems.
- Claude works from available initiative evidence and requires Digital Lead confirmation before treating status as current.
- Confirmed reporting updates must be written back to the affected initiative evidence and decision files before programme reporting is finalised.
- GitHub holds reusable methods and templates only; it must not become a parallel live Jira portfolio or Omega 365 action register.
