# BOARD ACCESS NOTES — Strateq DX CDO Coworker

**Classification:** Board-Facing Advisory — Read Only  
**Date:** 2026-06-22  
**Purpose:** Define how the Board interacts with this repository and how Board recommendations are processed into governed changes.

---

## 1. What the Board May Read

The Board may read any file in the `BOARD_INTERFACE/` folder without restriction.

The Board may also read the following files from the main repository, which are non-confidential product governance files:

| File / Folder | Permitted |
|---|---|
| `README.md` | Yes |
| `CLAUDE.md` | Yes |
| `00_system_control/FOLDER_MAP.md` | Yes |
| `00_system_control/CONTROLLED_VOCABULARY.md` | Yes |
| `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` | Yes |
| `01_governance_lifecycle/` (all files) | Yes |
| `03_process_mapping/` (all files) | Yes |
| `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md` | Yes |
| `BOARD_INTERFACE/` (all files) | Yes |

---

## 2. What the Board May Request

The Board may request:

- Briefings on product scope, purpose, or positioning
- Updates to `BOARD_INTERFACE/` files (via Digital Lead)
- Review of any file listed under Section 1
- Advisory input sessions on strategy, AI governance philosophy, or product direction
- Explanations of lifecycle stages, route rules, or coworker boundaries
- Information about what is and is not in scope for the product

All requests should be directed to the Digital Lead. The Digital Lead determines how to action requests and whether they require a repo change.

---

## 3. What the Board Must Not Mutate

The Board must not directly edit, overwrite, delete, rename, or reclassify any file in this repository.

| Restricted Area | Reason |
|---|---|
| `CLAUDE.md` | Governs AI coworker behaviour; changes require Digital Lead review and formal commit |
| `00_system_control/` (all files) | Core operating authority; changes require Digital Lead approval |
| `01_governance_lifecycle/` (all files) | Programme lifecycle rules; changes require Digital Lead approval |
| `02_coworker_artifact_interface/` (all files) | Coworker interface models; changes require Digital Lead approval |
| `03_process_mapping/` (all files) | Process mapping standards; changes require Digital Lead approval |
| `04_intake_dispatch/` (all files) | Intake and dispatch rules; changes require Digital Lead approval |
| `05_source_of_truth/` (all files) | Source-of-truth governance; changes require Digital Lead approval |
| Any file outside `BOARD_INTERFACE/` | All changes outside this folder require Digital Lead ownership |

---

## 4. How Board Recommendations Should Become Repo Changes

Board recommendations that require a change to a governed file must follow this process:

1. **Board raises recommendation** with the Digital Lead (verbally, in writing, or via a Board session).
2. **Digital Lead assesses** whether the recommendation touches a governed file, a source-of-truth file, or an AI boundary rule.
3. **Digital Lead decides** whether to accept, modify, or decline the recommendation.
4. If accepted, **Digital Lead creates or commissions a branch** using the naming convention below.
5. **Changes are drafted** on the branch (by Digital Lead or AI-assisted coworker under Digital Lead direction).
6. **Digital Lead reviews** the draft and confirms it accurately reflects the Board recommendation.
7. **PR is raised** to main and reviewed before merge.
8. **No recommendation is treated as adopted** until the PR is merged to main by the Digital Lead.

Board recommendations are advisory only. They do not take effect until formally processed by the Digital Lead through the branch/PR process.

---

## 5. Branch / PR Rule for Product Changes

All product changes must follow this process:

| Step | Rule |
|---|---|
| Branch naming | Use descriptive prefix: `chore/`, `feat/`, `fix/`, `docs/` followed by a short description (e.g. `chore/board-brief-index`) |
| Never push directly to main | All changes must go via a branch and PR |
| PR review | Digital Lead must review the PR diff before merging |
| Merge authority | Digital Lead only |
| Commit messages | Clear and descriptive; reference the change type and scope |
| No force-push to main | Prohibited |
| Board-originated changes | Must be explicitly attributed in the PR description |

---

## 6. Private SOS Separation Rule

This repository (`strateq-dx-cdo-coworker`) is a **product governance repository**. It contains Strateq DX product files only.

The following rules govern SOS document separation:

| Rule | Detail |
|---|---|
| No SOS Class A–D documents in this repo | Private client, financial, legal, or confidential SOS documents must not be committed here |
| No client-specific data | Client initiative data, client organisation details, and client-specific process outputs are not held here |
| No cross-repo references to private SOS repos | This repo must not link to, embed, or reference content from private SOS repositories |
| Client-specific learning | May only be promoted to this repo as generalised product doctrine after explicit Digital Lead review and approval |
| Board members accessing this repo | Are accessing product governance files only; they are not accessing any private SOS records |
| If in doubt | Treat the file as private SOS and do not commit it here; raise with the Digital Lead |

Strateq's private SOS records are held in separate, access-controlled repositories and SharePoint stores. This product repo and those private records must remain separated at all times.

---

*These access notes are advisory only. They describe the current access and change governance framework as defined by the Digital Lead. They do not constitute a formal information security policy or a legal access agreement.*
