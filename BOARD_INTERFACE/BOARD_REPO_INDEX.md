# BOARD REPO INDEX — Strateq DX CDO Coworker

**Classification:** Board-Facing Advisory — Read Only  
**Date:** 2026-06-22  
**Purpose:** Provide the Board with a navigable index of current repository structure. No files have been moved or altered to produce this index.

---

## 1. Main Source-of-Truth Files and Folders

| File / Folder | Description |
|---|---|
| `CLAUDE.md` | Role definition, operating authority, required behaviour, prohibited behaviour, and model guidance. Primary coworker instruction file. |
| `README.md` | Repository overview. |
| `00_system_control/` | System control files: lifecycle map, operating rules, controlled vocabulary, folder map, coworker handover model, knowledge capture rules, governed workflow looping standard, coworker router. |
| `00_system_control/CONTROLLED_VOCABULARY.md` | Controlled terminology for the programme. |
| `00_system_control/FOLDER_MAP.md` | Authoritative folder structure reference. |
| `00_system_control/OPERATING_RULES.md` | Binding operating rules for all coworker sessions. |
| `05_source_of_truth/` | Source-of-truth governance model. |
| `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` | Defines how digital artefacts are governed, classified, and updated. |

---

## 2. Workflow Files

| File | Description |
|---|---|
| `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` | Full programme lifecycle: stages, coworker paths, handover points, Hopper Lifecycle reference. |
| `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` | Governed workflow loop rules: proportionality, stage segregation, route-aware closeout, knowledge capture, CDO QA advisory. |
| `01_governance_lifecycle/00_REQUEST_INTAKE_MODEL_FUTURE.md` | Future-state public request intake model. |
| `01_governance_lifecycle/01_HOPPER_CONSOLIDATION_MODEL.md` | Rules for consolidating initiatives into the Hopper. |
| `01_governance_lifecycle/02_HOPPER_PRIORITY_SCREEN_MODEL.md` | Priority screening model for Hopper initiatives. "Priority Screen" = the Jira Initiative View / Hopper priority view, not a separate DRB document (see `09`). |
| `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md` | Stage gate rules for moving from Hopper to Initiation. |
| `01_governance_lifecycle/04_INITIATION_FORM_INTAKE_MODEL.md` | Initiation form intake and processing model. |
| `01_governance_lifecycle/05_ROUTE_RULES.md` | Route determination rules (standard vs development route). |
| `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md` | DRB brief output model for initiation and approval artefacts. |
| `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` | Two-stage initiation model definition. |
| `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md` | Development route Stage 1D model and exception triggers. |
| `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md` | Governing model for the Hopper Portfolio Readiness Review: prepares the Jira Initiative View / Hopper priority view for leadership / DRB discussion (pre-initiation, pre-Pack 1; no separate DRB Priority Screen artefact by default). |
| `03_process_mapping/01_PROCESS_MAPPING_MATRIX_INPUT_RULES.md` | Input rules for process mapping sessions. |
| `03_process_mapping/02_CREATE_PROCESS_MAPPING_PACK.md` | Process for creating a process mapping pack. |
| `03_process_mapping/03_BLUEWORKS_BUILD_BRIEF_RULES.md` | Rules for Blueworks build briefs (optional tooling). |
| `03_process_mapping/04_PROCESS_ARTIFACT_OUTPUT_MODEL.md` | Output model for process artefacts. |
| `03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md` | Swimlane process flow standard. |
| `03_process_mapping/06_LIVE_PROCESS_MAPPING_SESSION_FACILITATOR.md` | Live session facilitator guide for process mapping. |
| `04_intake_dispatch/01_AUTOMATIC_HOPPER_CLARIFICATION_HANDLER.md` | Automatic handler for Hopper clarification inputs. |
| `04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md` | Jira field length rules for intake. |

---

## 3. Coworker Files

| File | Description |
|---|---|
| `00_system_control/04_COWORKER_HANDOVER_MODEL.md` | Rules for handover between lifecycle coworkers. |
| `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` | Knowledge capture and source-of-truth update rules. |
| `00_system_control/11_COWORKER_ROUTER.md` | Routes each coworker session to the correct jurisdiction, lifecycle stage, authority files, permitted outputs, and approval gates. |

---

## 4. Client Template Files

| File / Folder | Description |
|---|---|
| `02_coworker_artifact_interface/` | Coworker–artefact interface files. |
| `02_coworker_artifact_interface/01_HOPPER_COWORKER_INTERFACE.md` | Interface model between Hopper lifecycle and coworker outputs. |
| `02_coworker_artifact_interface/02_HUMAN_FEEDBACK_INPUT_TEMPLATES.md` | Templates for human feedback input into coworker sessions. |
| `02_coworker_artifact_interface/03_DECISION_FEEDBACK_TEMPLATES.md` | Templates for decision feedback capture. |

---

## 5. Active Decision Files

Not currently present as a dedicated folder. Active decisions are tracked in Jira (external to this repo) and referenced through lifecycle and governance files above. The DRB brief output model (`01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`) governs the artefact format for approval decisions.

---

## 6. Review / Handover Files

| File | Description |
|---|---|
| `00_system_control/04_COWORKER_HANDOVER_MODEL.md` | Coworker handover checkpoint model. |
| `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` | Stage closeout, handover, and CDO QA advisory report rules. |

Dedicated review artefacts (closeout evidence, lessons learned) are stored in SharePoint per the artefact governance model, not in this repo.

---

## 7. Open Items / Constraints

| Item | Status |
|---|---|
| CDO control panel concept | In development — no dedicated file yet present in repo |
| Initiation form / DRB Brief rename workstream | Open — noted in CLAUDE.md as unresolved in current PR |
| Active decision register | Not currently present as a repo file; tracked in Jira |
| Client template folder | Artefacts held in `02_coworker_artifact_interface/`; no dedicated `client_template/` folder present |
| Board interface folder | Newly created in this PR — not previously present |

---

*This index reflects the repository as inspected on 2026-06-22. No files were moved, renamed, or altered to produce this index.*
