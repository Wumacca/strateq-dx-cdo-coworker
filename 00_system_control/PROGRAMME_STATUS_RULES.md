# Programme Status Rules

## Status

Authority file for how client-specific `PROGRAMME_STATUS.md` files are governed.

Read together with `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md` (resolution and interface) and `00_system_control/PROGRAMME_STATUS_TEMPLATE.md` (structure).

## Purpose

`PROGRAMME_STATUS.md` is the live controlled status surface for one client programme. These rules define what it is, what it is not, where it lives, who may change it, and how conflicts are resolved.

## Core Rules

### 1. DX Build contains the template and rules only

The DX Build repository holds `00_system_control/PROGRAMME_STATUS_TEMPLATE.md` and this rules file. It must never hold a populated `PROGRAMME_STATUS.md`, and must never hold client programme values, figures, initiative names, maturity scores, approval names, or evidence records.

### 2. Each client workspace contains its own `PROGRAMME_STATUS.md`

One client, one workspace, one `PROGRAMME_STATUS.md`, addressed by the client manifest field `programme_status_path` and conventionally located at:

```text
[ACTIVE_CLIENT_WORKSPACE]/00_system_control/PROGRAMME_STATUS.md
```

It is built from the template and is not restructured per client beyond adding client-required rows and sections. Section numbering and the required record metadata are fixed.

### 3. `PROGRAMME_STATUS.md` is a current controlled index, not the evidence itself

It records the current controlled position and points to where the evidence lives. It does not contain the evidence, and it does not replace the artefact, the register, or the client system of record.

- **Jira** remains the client-facing initiative and delivery-status system.
- **SharePoint / the controlled client store** remains the approved artefact and evidence store.
- **Omega 365** remains the action-management system.
- **`PROGRAMME_STATUS.md`** is the controlled index the coworker reads to know the current position and where its evidence sits.

Claude has no live connection to Jira, SharePoint, or Omega 365 and must never claim it has read or updated a live client system.

### 4. Every material status record must point to evidence

Every substantive record carries the required metadata: Source Basis, Evidence Path, Evidence Artefact, Revision / Date, Accepted By, Confidence, Status.

A record with no evidence pointer is permitted only when the gap is explicit: the pointer fields are left visibly open, the confidence states that the position is unevidenced, and the record is not used to support a Board-facing, assurance-facing, or approval-facing claim.

### 5. Accepted artefact overrides presented draft where figures conflict

> The accepted delivered artefact remains the evidence basis.

Where a figure in a deck, a summary, a report, a chat message, or a draft conflicts with the accepted delivered artefact, the accepted artefact governs. The conflict is surfaced to the Digital Lead before either figure is used in an output. The `PROGRAMME_STATUS.md` record is then corrected by supersession, not by overwriting.

### 6. Digital Lead confirms against accepted artefact

> The Digital Lead is the sole confirmation authority for programme status.

Confirmation is a control act performed **against the accepted artefact**. It is not an evidence source in itself. Recollection, chat memory, synced project knowledge, and unevidenced verbal positions are never recorded as the evidence basis.

Only the Digital Lead may set `DL CONFIRMED`, `DL REJECTED`, `SUPERSEDED`, or `WITHDRAWN`. Every coworker-created record defaults to `AWAITING DL`.

### 7. Coworker proposes updates only

The coworker reads `PROGRAMME_STATUS.md`, reconciles it against the available controlled sources, and proposes updates. It does not confirm status, and it writes only where the manifest `write_mode` is `approved_write` **and** the Digital Lead has approved that specific update.

Proposed updates are labelled:

> `Recommended update — requires Digital Lead approval.`

Proposed client-system updates are labelled:

> `Recommended update — requires Digital Lead approval and physical update in the client system.`

## Record Lifecycle

```text
Coworker creates or amends a record
→ record defaults to AWAITING DL
→ evidence pointer fields completed, or gap made explicit
→ Digital Lead reviews against the accepted artefact
→ DL CONFIRMED / DL REJECTED / correction raised
→ correction creates a new record and sets the original to SUPERSEDED
→ change logged in Section 15 File Change History
```

## Correction and Retention

1. Records are never deleted.
2. Corrections supersede rather than overwrite.
3. A superseded record retains a pointer to the record that superseded it, and the superseding record points back.
4. A withdrawn record retains its withdrawal reason.
5. Section 15 logs every change, appended and never edited.

## Handover Staleness

> A handover becomes stale, not wrong, when downstream truth changes. A downstream coworker must not continue on a stale handover.

Where a confirmed programme status position changes, every downstream handover that depended on the previous position is marked stale in Section 13 and reissued from the current confirmed position before the downstream stage continues. This restates, and does not replace, the handover authority in `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and the closeout rules in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

## Conflict Resolution Order

1. Accepted delivered artefact.
2. Active client `PROGRAMME_STATUS.md` record carrying a valid evidence pointer.
3. Client registers — artefact, decision, evidence, handover.
4. Initiative Evidence and Decision Files.
5. Supplied exports, snapshots, and in-session evidence.
6. Inference — never a source; labelled as inference, carries no evidence pointer.

Chat memory, synced project knowledge, prior session recollection, and last-used client context are not sources at any tier.

## Capital Efficiency and Plan Attainment Rules

These apply wherever Sections 1A and 1B are used, including in Capex Request Sessions governed by `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`.

- Do not invent savings, costs, benefits, dates, or approvals.
- One-off and recurring avoided costs must not be merged into a single total unless separately labelled.
- Percentage reductions are calculated as `(baseline cost − revised cost) / baseline cost × 100`, with the calculation shown.
- Finance-dependent claims are marked pending until validated by finance.
- Live initiatives are complete for delivery closeout unless the governing route explicitly requires a post-adoption gate.
- Adoption and benefits remain separate lifecycle controls and must not be collapsed into delivery closeout.
- Where an indicative capital value has not been confirmed, state `TBC` rather than estimating.

## Validation Checklist

| # | Check | Pass condition |
|---:|---|---|
| 1 | File location | In the client workspace, addressed by the manifest; not in DX Build |
| 2 | Derived from the template | Section numbering and required metadata intact |
| 3 | Every substantive record carries evidence pointer fields | Yes, or the gap is explicit and the record is not used for a controlled claim |
| 4 | Default status applied to coworker-created records | `AWAITING DL` |
| 5 | Confirmed statuses set only by the Digital Lead | Yes |
| 6 | No record deleted | Yes; corrections superseded |
| 7 | Conflicts resolved to the accepted artefact | Yes, and surfaced to the Digital Lead |
| 8 | One-off and recurring avoided costs separately labelled | Yes |
| 9 | Handover staleness reviewed after any status movement | Yes; stale handovers reissued before downstream continuation |
| 10 | Section 15 updated for every change | Yes |
| 11 | No claim of a live client-system read or update | Yes |

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`, `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
