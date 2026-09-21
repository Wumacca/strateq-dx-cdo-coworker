# Initiative Control Record Schema

## Status

Reusable schema for the initiative control fields used across the governed lifecycle. This file is a schema, not a live initiative record. The public method repository holds the schema only; a private client repository may hold one live client copy per initiative where the client profile selects GitHub as its working authority.

There is exactly one AI-readable per-initiative continuity record: the **Initiative Evidence and Decision File** (`02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`), which is the client-copy implementation of this schema, held in the controlled client workspace and governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. Do not maintain a second AI-readable initiative record alongside it.

This schema is applied by the Interactive Governed Session Protocol at reconciliation and closeout. Client binding is mandatory under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## Storage Rule

- **Reusable method/schema:** this public repository.
- **Live initiative record:** one Initiative Evidence and Decision File in the bound private client repository or approved client system.
- **Client-control plan:** the PEP or other source named in the client profile.
- **Detailed execution:** the named developer/vendor system or plan; referenced, not duplicated.
- **Actions, evidence and publication:** the systems/paths named in the client's `SOURCE_OF_TRUTH.md`.

No client record is permitted in this public repository. No uncontrolled ledger may duplicate the governed private client records.

## Field Set

### 1. Identity

- Initiative ID
- Client ID
- Initiative title
- Delivery group
- Summary
- Initiative origin
- Originating artefact / reference
- Requesting area
- Department
- Initiative type
- Approved route
- Priority

Route labels must use the controlled labels in `00_system_control/CONTROLLED_VOCABULARY.md` (Development Route / Implementation Route / Support Route / TBC). This schema does not create or split route labels.

### 2. Lifecycle

- Four-stage macro-stage
- Detailed repository lifecycle position
- Current gate
- Gate status
- Current delivery-record status
- Next control move
- Next stage trigger

### 3. Approval

- Approval basis
- Entry basis
- Authority to proceed and evidence status
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
- Detailed-plan owner
- Client-control-plan owner
- Budget/cost owner
- Digital financial-reporting basis
- Variation/expenditure authority
- Acceptance authority
- Go-live authority

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
- Delivery model
- Linked PEP
- Detailed-plan reference
- Current milestone
- Target finish
- Current blockers
- Candidate change controls
- Next fortnightly work package
- Evidence status
- Handover readiness
- Reporting audiences, cadence, cut-off and validator

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

- Assigned lifecycle coworker
- Coworker commencement status
- Coworker commencement date
- Bound AI Project/workspace
- Bound thread name
- Client-boundary gate result
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
- Action-system references (referenced, not duplicated)
- Required private-client-repository update and status (Pending / Completed / Deferred / Not applicable)
- Required external publication/evidence write-back and status
- Required action-system write-back and status

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

Each initiative's continuity record is the **Initiative Evidence and Decision File** — the client-copy implementation of this schema. There is one such record per initiative, not a parallel set of memory ledgers.

The Initiative Evidence and Decision File must:

- exist in the bound private client repository or approved client working system (never in this public method repository);
- use this Initiative Control Record schema;
- identify the configured client working authority and delivery-control records;
- record the latest information source and source date;
- record the Digital Lead confirmation status and last confirmation date;
- record the scope/filter of any supplied export and whether it covered the requested initiative or wider portfolio;
- identify fields that differ from the latest controlled source;
- identify an owner;
- record required repository updates, action-system updates and external publications with status.

Every governed-session closeout must propose, as recommendations for Digital Lead approval:

1. Initiative Evidence and Decision File update;
2. client working-authority update and status;
3. external publication/evidence write-back and status;
4. action-system write-back and status.

The Coworker must not treat the Initiative Evidence and Decision File as current where the confirmation-first status rule has not been satisfied or its freshness requires revalidation. Its authority is defined by the bound client's `SOURCE_OF_TRUTH.md`.

## Cockpit projection

The proposed `02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md` defines
how this record may feed a personal cockpit after its release and client-profile
activation gates are satisfied. The projection preserves field-level evidence,
confirmation and freshness; it does not replace this schema or the single
Initiative Evidence and Decision File. Export metadata is generated, not a new
manually maintained initiative register. A display RAG must not collapse stage
approval, closure, blockers or pending confirmation into one status.

For an activated feed profile, carry the reference and revision of the approved
initiative-specific control-applicability profile. It resolves initiative type,
route, entry authority, delivery model, scope and client requirements into
required, not-required or unresolved controls, retaining rule/evidence references
and exception decisions. Required evidence, stage completion and stage RAG are
assessed only after applicability. N/A is neither completion nor an accepted gap.
This is a reference to governed configuration, not a second initiative record.

## Boundary

This schema adds no AI approval authority or numeric AI confidence scoring. Controlled repository changes require Digital Lead approval before merge/release; external publications require confirmation.
