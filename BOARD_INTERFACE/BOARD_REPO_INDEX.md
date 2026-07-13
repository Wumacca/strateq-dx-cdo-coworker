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
| `00_system_control/` | System control files: lifecycle map, operating rules, controlled vocabulary, folder map, coworker handover model, knowledge capture rules, governed workflow looping standard, coworker router, interactive governed session protocol, initiative control record schema. |
| `00_system_control/CONTROLLED_VOCABULARY.md` | Controlled terminology for the programme. |
| `00_system_control/FOLDER_MAP.md` | Authoritative folder structure reference. |
| `00_system_control/OPERATING_RULES.md` | Binding operating rules for all coworker sessions. |
| `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` | **Machine / authority file.** Global authority for how material coworker sessions run interactively: runtime access gate, Client Context Gate, Initiative Reconciliation Gate, Required Inputs Gate, Live Session Status Board, controlled session states, and closeout write-back. |
| `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` | **Machine / authority file.** Reusable schema for initiative control fields. Jira is the target-state live record; GitHub holds the schema only. Not a live per-initiative ledger. |
| `05_source_of_truth/` | Source-of-truth governance model. |
| `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` | Defines how digital artefacts are governed, classified, and updated. |
| `06_operating_manual/01_DIGITAL_TRANSFORMATION_GOVERNANCE_AND_MANAGEMENT_MANUAL.md` | **Human-facing navigation manual — non-authoritative.** Explains how the Digital Lead uses the governed coworker system across the four-stage macro model and each lifecycle stage. Where it and an authority file differ, the authority file prevails. |

> **Machine / authority files vs human-facing navigation.** All files above except the operating manual are machine / authority files: they control coworker behaviour and prevail in any conflict. `06_operating_manual/01_DIGITAL_TRANSFORMATION_GOVERNANCE_AND_MANAGEMENT_MANUAL.md` is human-facing navigation only and is subordinate to the authority files it references.

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
| `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md` | Optional DRB meeting-support text output model. Meeting-support / decision-support text only, produced on explicit Digital Lead request; not the formal approval artefact (see `10`). |
| `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md` | Two-stage initiation model definition. |
| `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md` | Development route Stage 1D model and exception triggers. |
| `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md` | Governing model for the Hopper Portfolio Readiness Review: prepares the Jira Initiative View / Hopper priority view for leadership / DRB discussion (pre-initiation, pre-Pack 1; no separate DRB Priority Screen artefact by default). |
| `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md` | Single authority for the formal DRB-facing approval artefact: the Completed Initiation Form. Defines the session-opening source-document checklist, uploaded-form-as-primary-source rule, required form structure, Word / `.docx` export, and the pack-deliverable rule (do not collapse the pack into the form). |
| `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md` | Governing model for the Capex Request Session: a portfolio-level Hopper Portfolio Readiness mode for previous capex closeout, next capex portfolio request, evidence-safe Board narrative, client-review Board-draft deck, and controlled Hopper-to-Delivery handover. Formal output is the Portfolio Capex Request Pack. Allows a client-review Board-draft deck; prohibits a Board-final deck while blockers remain open. |
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

Not currently present as a dedicated folder. Active decisions are tracked in Jira (external to this repo) and referenced through lifecycle and governance files above. The Completed Initiation Form output model (`01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`) governs the formal approval artefact; the DRB meeting-support text model (`01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`) governs optional meeting-support text only.

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
| Initiation form / DRB Brief rename workstream | Resolved — formal approval artefact is now the Completed Initiation Form (`01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`); `06` reframed as optional DRB meeting-support text only |
| Active decision register | Not currently present as a repo file; tracked in Jira |
| Client template folder | Artefacts held in `02_coworker_artifact_interface/`; no dedicated `client_template/` folder present |
| Board interface folder | Newly created in this PR — not previously present |

---

*This index reflects the repository as inspected on 2026-06-22. No files were moved, renamed, or altered to produce this index.*
