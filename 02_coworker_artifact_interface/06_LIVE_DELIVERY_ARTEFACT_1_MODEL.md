# Live Delivery Programme Status — Artefact 1 Model

## Purpose

This file is the governing model for the Live Delivery Coworker's programme status artefact (Artefact 1). It defines the scope, mobilisation boundary, source precedence, template structure, generation protocol, and quality controls that govern every Artefact 1 output.

Artefact 1 is the primary active-portfolio delivery control document. It covers `In Delivery` and `Operational / Live` initiatives under ongoing delivery control, and may include `Mobilising` initiatives for portfolio and agenda visibility purposes only.

This model is an internal coworker authority file. Section 4 provides the Digital Lead-visible template guidance. All other content is internal to the coworker and governs how the artefact is produced.

---

## Artefact Reference

| # | Name | Scope | Governed by |
|---|---|---|---|
| Artefact 0 | Mobilisation Control Record | `Mobilising` initiatives | Artefact 0 model |
| **Artefact 1** | Live Delivery Programme Status | `In Delivery`, `Operational / Live`; `Mobilising` for agenda / portfolio visibility only | This file |
| Artefact 2 | [Future scope — not yet modelled] | — | Future model |

---

## Jurisdiction

Artefact 1 is owned by the **Live Delivery Coworker**.

It is governed by:

- `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`
- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`

---

## Mobilisation Boundary and Artefact 0 Relation

A `Mobilising` initiative **may appear in Artefact 1 for portfolio and agenda visibility purposes only.**

- **Artefact 0** is the mobilisation control record for a `Mobilising` initiative.
- **Artefact 1 ongoing delivery control does not begin** for a `Mobilising` initiative until the effective `Mobilising → In Delivery` status handoff has occurred in Jira.
- A `Mobilising` initiative that appears in Artefact 1 is present for portfolio tracking and agenda awareness only; Artefact 0 remains the sole control record until the handoff is confirmed.

Do not use wording that states or implies Artefact 1 "starts the ongoing control cycle" for an initiative that remains at `Mobilising` status. The unambiguous qualifier above applies in all cases.

---

## Active-Portfolio Scope

The active-portfolio completeness check covers three Jira status values:

| Jira Status | Artefact 1 Role |
|---|---|
| `Mobilising` | Portfolio and agenda visibility only. Ongoing delivery control remains with Artefact 0 until the confirmed `Mobilising → In Delivery` handoff in Jira. |
| `In Delivery` | Primary ongoing delivery control scope. |
| `Operational / Live` | Ongoing delivery control: go-live confirmation, early-life issues, and next actions. Remains in Artefact 1 scope until the initiative passes into the adoption / closure control. |

`Operational / Live` is included because Artefact 1 retains control of go-live confirmation, early-life issues, and next actions for that status until the initiative passes into the adoption / closure control.

---

## Source Precedence

| Source | Role |
|---|---|
| **Jira** | Primary governed source for current Initiative Status. Consistent with the locked Stage 3 Jira boundary. |
| **Approved controlled artefacts** | Authority and evidence for lifecycle transitions. Used as assurance cross-checks. They are not parallel live Status registers. |
| **Conflict: Jira vs controlled artefact evidence** | Do not resolve autonomously. Stop and prompt the Digital Lead before finalising the record. |
| **Completeness control** | Reads governed sources and raises prompts only. Creates no new register. Performs no Jira, SharePoint, or controlled-record update. |

Claude has no live connection to Jira, SharePoint, or Omega 365. Governed sources are read only from supplied exports, snapshots, and Initiative Evidence and Decision Files confirmed by the Digital Lead.

---

## Section 1 — Programme Overview

| Field | Content |
|---|---|
| Artefact period | |
| Prepared by | |
| Review date | |
| Initiatives in scope | |
| Known omissions and reason | |
| Outstanding Digital Lead confirmations | |

---

## Section 2 — Active Portfolio Status

Use one row per initiative. Read Initiative Status from Jira (primary source). Use approved controlled artefacts as assurance cross-checks only — they are not parallel Status registers.

| Initiative ID | Initiative Title | Jira Status | Responsible Owner | Last Confirmed Position | Progress Since Last Artefact | Current Risks / Blockers | Milestone / Target | Next Actions | Evidence / Decision Reference | Digital Lead Confirmation |
|---|---|---|---|---|---|---|---|---|---|---|

Allowed values for `Jira Status` in this table:

- `Mobilising` — appears for portfolio / agenda visibility only; Artefact 0 remains control record.
- `In Delivery` — primary ongoing delivery control.
- `Operational / Live` — go-live and early-life control.

`Digital Lead Confirmation` must be left blank or marked `Pending` until the Digital Lead confirms the position at the Confirmation-First Status Gate.

---

## Section 3 — Risks, Issues, and Decisions

### Cross-Portfolio Risks and Issues

| Matter | Initiatives Affected | Impact | Owner | Required Control Action | Reporting Significance |
|---|---|---|---|---|---|

### Pending Decisions

| Initiative | Decision / Approval Required | Decision Body / Owner | Target Date | Consequence if Delayed |
|---|---|---|---|---|

### Confirmed Decisions Since Last Artefact

| Initiative | Decision | Decision Body / Owner | Date | Outcome | Evidence Reference |
|---|---|---|---|---|---|

---

## Section 4 — Template Guidance

This section contains Digital Lead-visible guidance for completing and using Artefact 1. The initiative-completeness control is governed by the Generation Protocol (internal coworker authority) and is not replicated here.

### When to Use This Artefact

Artefact 1 is the active-portfolio delivery control record for the Live Delivery Coworker. It is produced at each governed delivery review cycle.

### Confirmation-First Status Rule

Before any initiative position is used or reported, the Digital Lead must confirm or correct the latest available position at the Confirmation-First Status Gate. Positions not yet confirmed are marked `Pending confirmation`.

### Jira as Primary Status Source

Current Initiative Status is read from Jira (primary governed source). Approved controlled artefacts provide lifecycle transition authority and assurance cross-checks; they do not override a confirmed Jira status.

Where Jira status conflicts with an approved transition or control artefact, do not resolve the conflict autonomously. The coworker will prompt the Digital Lead before finalising the record.

### Mobilising Initiatives in This Artefact

A `Mobilising` initiative may appear in Artefact 1 for portfolio and agenda visibility only. Artefact 0 remains its mobilisation control record. Artefact 1 ongoing delivery control does not begin for that initiative until the effective `Mobilising → In Delivery` handoff is confirmed in Jira.

### Initiative Omissions

If an initiative is omitted from the current agenda, the coworker will prompt before finalising. The Digital Lead must confirm inclusion or explicitly confirm exclusion. No initiative is added or removed automatically.

### Physical Update Rule

Every confirmed update must be written back to the affected Initiative Evidence and Decision File and, where applicable, to Jira, SharePoint, and Omega 365. The coworker prepares recommended write-backs; the Digital Lead applies them. No update is marked complete until the Digital Lead confirms the physical update has occurred.

---

## Generation Protocol

The generation protocol is internal to the coworker. It governs how Artefact 1 is generated, what checks must pass before finalisation, and what the coworker must prompt before producing the final output. It is not part of the Digital Lead-visible template.

### Governing Sources

At session opening, the coworker reads the following governed sources in this order:

1. Latest Digital Lead-confirmed Initiative Evidence and Decision Files for all `Mobilising`, `In Delivery`, and `Operational / Live` initiatives.
2. Jira export, snapshot, or supplied status for current Initiative Status (primary governed source).
3. Approved controlled artefacts for lifecycle transition authority and assurance cross-checks.

Where a source is unavailable, the coworker declares the access gap and does not infer status.

### Completeness Check

Before producing Artefact 1, the coworker must check Jira for all current `Mobilising`, `In Delivery`, and `Operational / Live` initiatives.

If any initiative at one of these statuses is absent from the latest agenda, the coworker must raise the following prompt before proceeding:

> "The following current Mobilising / In Delivery / Operational / Live initiatives are not included in the latest agenda:
> [Initiative ID — Initiative title — current Status]
> Should these initiatives be included in the latest agenda?"

The coworker must not add any omitted initiative automatically. Digital Lead confirmation is required before an initiative is included. Digital Lead explicit confirmation is also required before an initiative is confirmed for exclusion.

The completeness control reads governed sources and raises prompts only. It creates no new register and performs no Jira, SharePoint, or controlled-record update.

### Generation Quality Check

A multi-initiative active-portfolio Artefact 1 must not be finalised until the following condition is met:

**Every `Mobilising`, `In Delivery`, and `Operational / Live` initiative that is absent from the agenda has either been included following Digital Lead confirmation, or explicitly confirmed for exclusion by the Digital Lead.**

This is a hard gate. The completeness check must be run and all missing-initiative prompts must be resolved before the final Artefact 1 output is produced. A partial resolution (some initiatives confirmed, others still pending) is not sufficient to pass the gate.

### Conflict Resolution

Where Jira status and an approved controlled artefact evidence appear to conflict, the coworker must stop and prompt the Digital Lead before finalising the record. It must not resolve the discrepancy autonomously.

### Knowledge Capture

At Artefact 1 closeout, the coworker must identify confirmed updates that require write-back to Initiative Evidence and Decision Files and to client systems (Jira, SharePoint, Omega 365). Write-backs are presented as recommendations only and are not applied without Digital Lead approval. Governed by `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.

---

## Output Boundary

Artefact 1 outputs are limited to:

- the programme status document covering the active-portfolio scope above
- recommended Initiative Evidence and Decision File updates for Digital Lead approval
- recommended Jira, SharePoint, and Omega 365 write-backs for Digital Lead approval

Artefact 1 does not:

- create a programme-memory or programme-status ledger
- update Jira, SharePoint, or Omega 365 directly
- finalise status without Digital Lead confirmation
- add or exclude initiatives from the agenda without Digital Lead confirmation
- resolve a Jira / controlled-artefact conflict without Digital Lead confirmation
- begin ongoing delivery control for a `Mobilising` initiative before the confirmed `Mobilising → In Delivery` handoff
