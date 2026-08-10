# Programme Status Template

## Status

Reusable template. This file is the generic structure from which each client workspace builds its own `PROGRAMME_STATUS.md`.

> This template holds **no client values**. Copy it into the client workspace at `<client_repo_root>/00_system_control/PROGRAMME_STATUS.md` and populate it there. A populated `PROGRAMME_STATUS.md` must never be committed to the DX Build repository.

Governed by `00_system_control/PROGRAMME_STATUS_RULES.md` and `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`.

All bracketed values below are placeholders. All tables ship empty.

---

## 0. Control Rules

> The Digital Lead is the sole confirmation authority for programme status. The accepted delivered artefact remains the evidence basis. `PROGRAMME_STATUS.md` is the live controlled status surface.

### Template control rules

1. Every coworker-created record defaults to `AWAITING DL`.
2. Only the Digital Lead may set `DL CONFIRMED`, `DL REJECTED`, `SUPERSEDED`, or `WITHDRAWN`.
3. Records are never deleted.
4. Corrections supersede rather than overwrite.
5. A handover becomes **stale**, not wrong, when downstream truth changes.
6. A downstream coworker must not continue on a stale handover.
7. Every substantive record must carry evidence pointer fields.

### Record status values

| Status | Meaning | Who may set it |
|---|---|---|
| `AWAITING DL` | Coworker-created or coworker-amended. Not yet confirmed. Default for every new record | Coworker |
| `DL CONFIRMED` | Confirmed by the Digital Lead against the accepted artefact | Digital Lead only |
| `DL REJECTED` | Reviewed and rejected by the Digital Lead. Retained, not deleted | Digital Lead only |
| `SUPERSEDED` | Replaced by a later record. Retained, with a pointer to the superseding record | Digital Lead only |
| `WITHDRAWN` | Withdrawn before confirmation. Retained, with the withdrawal reason | Digital Lead only |

### Required record metadata

Every substantive record in every section below must carry:

| Field | Meaning |
|---|---|
| Source Basis | Where the position came from — accepted artefact / register / export or snapshot / Digital Lead confirmation / inference |
| Evidence Path | The addressable location of the evidence |
| Evidence Artefact | The named artefact that is the evidence basis |
| Revision / Date | The revision and date of that artefact |
| Accepted By | Who accepted the artefact, and in what capacity |
| Confidence | Stated in words against the controlled source read. No numeric or percentage confidence scores |
| Status | One of the record status values above |

Where the evidence pointer fields cannot be completed, the record is still created, with the gap explicit and the confidence stated as unevidenced. The record must not be presented as confirmed truth.

### Correction rule

To correct a record: create a new record carrying the corrected position, set the original to `SUPERSEDED`, and record the pointer in both directions. Never edit a confirmed record in place. Section 15 logs the change.

### Header block

| Item | Value |
|---|---|
| Client | *[client_name]* |
| Client ID | *[client_id]* |
| Client repo root | *[client_repo_root]* |
| Manifest | *[path to CLIENT_CONTEXT_MANIFEST]* |
| Programme status revision | *[revision]* |
| Programme status date | *[YYYY-MM-DD]* |
| Confirmation authority | *[role, normally Digital Lead]* |
| Last Digital Lead confirmation | *[YYYY-MM-DD]* |

---

## 1. Programme Position

The current controlled position of the programme as a whole.

| Item | Position | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| Programme phase | | | | | | | | |
| Funding position | | | | | | | | |
| Approved envelope | | | | | | | | |
| Initiatives in flight | | | | | | | | |
| Initiatives live | | | | | | | | |
| Initiatives closed | | | | | | | | |
| Open Board / leadership asks | | | | | | | | |
| Principal risks to the programme position | | | | | | | | |

---

## 1A. Capital Efficiency / Cost Avoidance Evidence

Captures every cost-avoidance or capital-efficiency case that may be used in a Board-facing claim.

> One-off and recurring avoided costs must not be merged into a single total unless separately labelled.

Percentage reductions are calculated as `(baseline cost − revised cost) / baseline cost × 100`, and the calculation is shown, not just the result.

| Case | Baseline cost | Revised cost | Avoided cost (one-off) | Recurring avoided cost (per period, period stated) | Arithmetic check | Evidence basis | Claim status | Finance validation status | Board-safe wording | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | |

### Totals

| Total type | Value | Basis | Status |
|---|---|---|---|
| Total one-off avoided cost | | | |
| Total recurring avoided cost (per period, period stated) | | | |
| Combined total | Not permitted as a single unlabelled figure. State one-off and recurring separately | | |

### Section rules

- Do not invent savings.
- Do not merge one-off and recurring avoided costs into a single total unless each component is separately labelled.
- Mark finance-dependent claims as pending until validated by finance.
- Claim status values: `Confirmed` / `Supported-Pending` / `Not Claimable`.
- Where evidence is incomplete, use Board-safe wording rather than the unsupported figure.

---

## 1B. Plan Attainment Evidence

Captures delivery against what was committed.

> Live initiatives are complete for delivery closeout unless the governing route explicitly requires a post-adoption gate.

Delivery closeout and adoption / benefits remain separate lifecycle controls and must not be collapsed into one another.

| Committed initiative | Status (delivered / live / controlled / next-phase) | Date movement reason | Budget position | Unsupported claims flagged | Board-safe closeout wording | Post-adoption gate required (Y/N, route basis) | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

### Attainment summary

| Item | Value | Basis | Status |
|---|---|---|---|
| Committed initiative count | | | |
| Delivered / live / controlled | | | |
| Moved to next phase | | | |
| Not delivered | | | |
| Attainment position as stated to the Board | | | |

---

## 2. Assessment / Benchmark / Maturity

| Item | Position | Assessment / review date | Reviewer | Movement proposed | Movement status | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

Maturity-impact statuses use the controlled vocabulary in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`: `No maturity impact identified` / `Expected maturity impact` / `Provisional maturity impact` / `Pending adoption evidence` / `Confirmed maturity impact` / `Rejected — insufficient evidence`.

A live maturity position is never moved solely because delivery is complete, where adoption or embedded-use evidence is required.

---

## 3. Hopper: Intake, Consolidation & Scoping

| Initiative / item | Origin | Department / function | Business reason | Consolidation outcome | Scoping state | Next control move | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

---

## 4. Hopper: Priority, DRB Decision & Route Classification

| Initiative | Proposed priority | Priority basis | DRB decision | Decision date | Route classification | Route basis | Grouping / epic | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

Route classification uses the controlled route labels in `00_system_control/CONTROLLED_VOCABULARY.md`.

---

## 5. Initiation: Stage 1D / Stage 1 / Process Mapping / Stage 2

| Initiative | Route | Stage | Stage state | Pack / form reference | Process mapping required (Y/N) | Process mapping state | Stage 2 exception tested (Y/N) | Open items | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | |

---

## 6. Approval: DRB Form & Leadership Sign-Off

| Initiative | Approval artefact | Approval type | Approval body | Approval date | Approval conditions | Approved scope summary | Approved cost position | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

The formal approval artefact is the Completed Initiation Form, governed by `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`.

---

## 6A. Capital Decision Register

Portfolio-level capital decisions: what was requested, what was approved, and what remains open.

| Capital decision | Request type (closeout / next capex / variation) | Requested value or TBC | Approved value or TBC | Decision body | Decision date | Decision conditions | Open dependencies / Board-final blockers | Funding envelope vs initiative approval boundary noted (Y/N) | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | |

> Approval of a capex request approves the funding envelope / programme intent only. It does not automatically approve each initiative to begin delivery unless the approval explicitly confirms that route and the required initiative-level controls are complete.

---

## 7. Job Live

| Initiative | Live job reference | Mobilisation date | Delivery owner | Delivery structure in place (Y/N) | Reporting cadence | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

---

## 8. Live Delivery

| Initiative | Delivery state | Milestone position | Schedule movement and reason | Scope changes | Risks / issues / blockers | Delivery evidence produced | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |

---

## 9. Go-Live / Deployment

| Initiative | Go-live date | Users identified (Y/N) | Support route in place | Training / competence evidence | Operational readiness confirmed | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

---

## 10. Adoption & Benefits

| Initiative | Adoption gate state | 30-day review outcome | Usage evidence | Ownership confirmed | Benefits claimed | Benefits evidence | Benefits status | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

Adoption and benefits are separate lifecycle controls from delivery closeout and must not be collapsed into it.

---

## 11. Source-of-Truth Artefact Control

| Artefact | Artefact type | Controlled location | Active revision | Superseded revision | Update required | Update state (recommended / approved / physically updated) | Owner | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

A physical client-system update is marked complete only when the Digital Lead explicitly confirms the physical update occurred.

---

## 12. Errors, Corrections & Duplications

Records are never deleted. Corrections supersede.

| Record corrected | Section | Original position | Corrected position | Correction reason | Superseding record reference | Duplicate of | Correction date | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

---

## 13. Handover Register

| Handover | From | To | Handover date | Handover artefact reference | Basis position at handover | Downstream position now | Staleness state (current / stale) | Staleness reason | Reissued (Y/N, date) | Downstream continued? (must be N while stale) | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | |

### Staleness rule

> A handover becomes stale, not wrong, when downstream truth changes. A downstream coworker must not continue on a stale handover. The handover is reissued from the current confirmed position before the downstream stage continues.

---

## 14. Gaps, Opportunities & Open Clarifications

| Item | Type (gap / opportunity / clarification) | Description | Impact if unresolved | Blocks which output or decision | Owner | Required input | Target date | Source Basis | Evidence Path | Evidence Artefact | Revision / Date | Accepted By | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

Accepted gaps are recorded explicitly as accepted by the Digital Lead, with the residual risk stated. An unrecorded gap is not an accepted gap.

---

## 15. File Change History

Every change to this file is logged. Entries are appended, never edited or removed.

| Date | Revision | Section(s) changed | Change summary | Records superseded | Made by | Confirmed by | Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## Boundary

This template defines structure only. It does not extend AI authority, does not create a live connection to Jira, SharePoint, or Omega 365, and does not override `00_system_control/PROGRAMME_STATUS_RULES.md`, `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`, `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`, or `00_system_control/OPERATING_RULES.md`.
