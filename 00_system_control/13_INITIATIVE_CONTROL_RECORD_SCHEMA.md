# Initiative Control Record Schema

## Status

Reusable schema for the initiative control fields used across the governed lifecycle. This is a **schema**, not a live initiative record. Do not create one GitHub file per initiative. GitHub holds the reusable method / schema only; it does not hold live per-initiative data.

There is exactly one AI-readable per-initiative continuity record: the **Initiative Evidence and Decision File** (`02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`), which is the client-copy implementation of this schema, held in the controlled client workspace and governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. Do not maintain a second AI-readable initiative record alongside it.

This schema is applied by the Interactive Governed Session Protocol (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`) at the Initiative Reconciliation Gate and in the closeout write-back. Claude has no live connection to Jira, SharePoint, or Omega 365.

## Storage Rule

- **Client-facing initiative and delivery status:** Jira (target-state). Claude reads supplied exports / snapshots only; it has no live connection.
- **Approved artefacts and evidence:** SharePoint / controlled client workspace.
- **Action management:** Omega 365 (referenced, not duplicated).
- **Single AI-readable continuity record:** the Initiative Evidence and Decision File in the controlled client workspace, implementing this schema.
- **Reusable method / schema:** GitHub (this file).

No permanent live per-initiative ledger is permitted in the reusable GitHub repository. No permanent portfolio index or programme-memory ledger that duplicates Jira is permitted in GitHub.

## Field Set

### 1. Identity

- Initiative ID
- Initiative title
- Summary
- Initiative origin
- Originating artefact / reference
- Requesting area
- Department
- Initiative type
- Approved route
- Priority

Route labels must use the controlled labels in `00_system_control/CONTROLLED_VOCABULARY.md` (Development Route / Implementation / Support Route / TBC). This schema does not create or split route labels.

### 2. Lifecycle

- Four-stage macro-stage
- Detailed repository lifecycle position
- Current gate
- Gate status
- Current Jira status
- Next control move
- Next stage trigger

### 3. Approval

- Approval basis
- Decision body
- Decision date
- Decision outcome
- Decision conditions
- Approval evidence link
- Funding / capex position
- Approval limitations

### 4. Ownership

- Sponsor
- Digital Lead
- Business owner
- Digital Champion
- Delivery owner
- Vendor
- Developer
- Support owner

### 5. Scope

- Approved scope
- Exclusions
- Success measures
- Dependencies
- Constraints
- Assumptions
- Source-of-truth impact

### 6. Delivery

- Delivery status
- Delivery health
- Linked PEP
- Linked Epic
- Current milestone
- Target finish
- Current blockers
- Candidate change controls
- Next fortnightly work package
- Evidence status
- Handover readiness

### 7. Evidence

- Required artefacts
- Available evidence
- Missing evidence
- Evidence owner
- Evidence location
- Last verified date
- Evidence status
- Acceptance position
- Approval position

### 8. Decisions and obligations

- Decision log
- Open actions
- Digital Lead obligations
- External obligations
- Accepted gaps
- Due dates
- Review dates
- Consequences of non-completion

### 9. Initiative relationships

- Linked initiatives
- Dependencies
- Shared systems
- Shared processes
- Shared vendors
- Shared resources
- Feature overlap
- Delivery timing conflict
- Recommended relationship treatment

Recommended relationship treatment uses the Cross-Initiative Impact Check outcomes governed by the Hopper / intake authority files (Absorb into existing initiative / Merge / duplicate / Controlled change to live initiative / Create dependency / Sequence separately / Retain as separate initiative / No material impact / Clarification required). The coworker may recommend a treatment but cannot change scope or route.

### 10. Session control

- Last governed session
- Session type
- Session state
- Suspension reason
- Pending evidence
- Pending decision
- Next session trigger
- Closeout position
- Handover position

### 10a. Confirmation, freshness and physical write-back

- Latest information source
- Source date
- Digital Lead confirmation status (Confirmed current / Corrected by Digital Lead / Pending confirmation / Superseded / Not applicable)
- Last confirmed by Digital Lead
- Last confirmation date
- Freshness status (Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable)
- Omega 365 action references (referenced, not duplicated)
- Required Jira physical write-back and status (Pending / Completed / Deferred / Not applicable)
- Required SharePoint physical write-back and status
- Required Omega 365 physical write-back and status

Physical write-backs are prepared as recommendations; only the Digital Lead or an authorised user performs them, and a write-back is marked complete only on explicit Digital Lead confirmation.

Session state uses the controlled session states in `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` (Not started / Active / Suspended — awaiting evidence / Pending Digital Lead decision / Pending external approval / Ready for closeout / Closed and handed over).

### 11. Strategic and maturity alignment fields (future-state)

These fields are reserved now for future alignment with the Client Digital Governance Profile and Maturity Improvement Loop models. They are **schema fields only**. Do not calculate maturity scores and do not update maturity positions in this workstream.

- Linked client strategic objective(s)
- Linked maturity roadmap track(s)
- Linked benchmark assessment question(s)
- Baseline maturity position
- Intended capability improvement
- Maturity evidence required
- Maturity evidence collected
- Expected maturity impact
- Provisional maturity impact
- Confirmed maturity impact
- Maturity-impact approval status
- Remaining capability gap
- Client-context artefacts potentially affected

Maturity-impact values use the controlled maturity-impact vocabulary and boundary in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` (No maturity impact identified / Expected maturity impact / Provisional maturity impact / Pending adoption evidence / Confirmed maturity impact / Rejected — insufficient evidence).

## Single AI-readable record: the Initiative Evidence and Decision File

Because Claude has no live connection to Jira, SharePoint, or Omega 365, each initiative's AI-readable continuity record is the **Initiative Evidence and Decision File** — the client-copy implementation of this schema. It replaces any separate "interim client Initiative Control Register" concept; there is one AI-readable record per initiative, not two.

The Initiative Evidence and Decision File must:

- exist in the controlled client workspace (not in this GitHub repository);
- use this Initiative Control Record schema;
- identify Jira as the client-facing initiative and delivery-status system;
- record the latest information source and source date;
- record the Digital Lead confirmation status and last confirmation date;
- record the Jira scope / filter of any supplied export and whether it covered the requested initiative or the wider portfolio;
- identify fields known to differ from the latest supplied Jira export;
- identify an owner;
- record required Jira, SharePoint, and Omega 365 physical write-backs and their status.

Every governed-session closeout must propose, as recommendations for Digital Lead approval:

1. Initiative Evidence and Decision File update;
2. Jira physical write-back text and status;
3. SharePoint / evidence physical write-back and status;
4. Omega 365 physical write-back and status.

The coworker must not treat the Initiative Evidence and Decision File as current where the confirmation-first status rule has not been satisfied or where its freshness is overdue under the applicable freshness rule in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. The Initiative Evidence and Decision File is not automatically the organisational source of record; SharePoint holds the organisational source-of-record artefacts.

## Boundary

This schema adds no AI approval authority, no numeric AI confidence scoring, and no authority to mutate Jira, SharePoint, GitHub or source-of-truth records. All controlled updates require Digital Lead approval under `00_system_control/OPERATING_RULES.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.
