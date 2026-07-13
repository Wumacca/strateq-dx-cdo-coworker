# Initiative Control Record Schema

## Status

Reusable schema for the initiative control fields used across the governed lifecycle. This is a **schema**, not a live initiative record. Do not create one GitHub file per initiative. GitHub holds the reusable method / schema only; it does not hold live per-initiative data.

This schema is applied by the Interactive Governed Session Protocol (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`) at the Initiative Reconciliation Gate and in the closeout write-back.

## Storage Rule

- **Target-state live Initiative Control Record:** Jira.
- **Approved artefacts and evidence:** SharePoint / controlled client workspace.
- **Reusable method / schema:** GitHub (this file).
- **Interim client Initiative Control Register:** controlled client workspace only, transitional (see below).

No permanent live per-initiative ledger is permitted in the reusable GitHub repository. No permanent portfolio index that duplicates Jira is permitted in GitHub.

## Field Set

### 1. Identity

- Initiative ID
- Initiative title
- Summary
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

## Interim Client Initiative Control Register

An interim register may be used only where:

- Jira does not yet contain the required fields;
- Jira is not connected to the coworker environment;
- a current Jira export is not practical for every session.

The interim register must:

- exist in the controlled client workspace (not in this GitHub repository);
- use this Initiative Control Record schema;
- identify Jira as the target-state live source;
- include `Last reconciled with Jira`;
- include the Jira source / export date;
- include the Jira scope / filter used;
- identify whether the export covered the requested initiative or the wider portfolio;
- identify fields known to differ from Jira;
- identify an owner;
- be explicitly transitional.

Every governed-session closeout that uses the interim register must propose:

1. Jira update text;
2. interim-register update;
3. SharePoint / evidence update;
4. updated `Last reconciled with Jira` position.

The coworker must not claim that the interim register is current where reconciliation is overdue under the applicable freshness rule in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

## Boundary

This schema adds no AI approval authority, no numeric AI confidence scoring, and no authority to mutate Jira, SharePoint, GitHub or source-of-truth records. All controlled updates require Digital Lead approval under `00_system_control/OPERATING_RULES.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.
