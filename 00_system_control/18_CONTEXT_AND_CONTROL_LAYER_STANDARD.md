# Context and Control Layer Standard

## Status

Proposed controlled method standard. Merge and release require Digital Lead approval.

## Purpose

The Context and Control Layer is the reusable, client-agnostic operating layer that keeps a governed work unit understandable, current, evidence-led and recoverable across Coworker sessions.

It turns the existing route, current-state, evidence, handover, source-of-truth and assurance controls into one explicit control surface. It does not create a third Coworker, a programme-memory ledger, a parallel initiative record or an automatic approval path.

## Authority and boundaries

This standard is subordinate to:

- `CLAUDE.md`
- `AGENTS.md`
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`
- `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

The public method repository contains the reusable standard only. A populated Context and Control Layer belongs in the one bound private client repository or the client system named in `SOURCE_OF_TRUTH.md`. Client data, evidence, status and populated records must never be written to this method repository.

## 1. Context and Control Pack

Every controlled initiative or work unit must have one Context and Control Pack. It is a structured view over the existing controlled records, not a new source of truth.

The pack must point to, or contain the minimum fields from:

1. **Route map** — lifecycle stage, route, Coworker jurisdiction, authority files and permitted next control moves.
2. **Verified Current State** — the mandatory current-state block in section 2.
3. **Evidence index** — required, available, missing, stale and superseded evidence with location and last verification.
4. **Decision and approval pointers** — decision body, decision status, conditions, evidence reference and approval limitations.
5. **Scope and relationship pointers** — approved scope, exclusions, dependencies, constraints and linked initiatives.
6. **Risk, action and obligation pointers** — owner, due/review point, consequence and status for each unresolved item.
7. **Source-of-truth impact** — affected artefacts, required update, working path, publication status and approval state.
8. **Session and handover state** — bound context, session state, handover position, next trigger and Digital Lead action.
9. **Control and recovery metadata** — last control-check run, drift-audit result, open failures, branch/reference position and change history.

The Initiative Evidence and Decision File remains the single AI-readable per-initiative continuity record. The PEP, action system, evidence repository and source-of-truth registers remain authoritative for the record types assigned to them.

## 2. Verified Current State — mandatory

A Verified Current State block is mandatory in every client-copy Initiative Evidence and Decision File and every governed status/reporting projection that represents an initiative as current.

The block must contain:

| Field | Required content |
|---|---|
| As-of position | The status position being asserted and the date/time it was valid or last confirmed |
| Lifecycle position | Four-stage macro-stage, detailed lifecycle stage and current gate |
| Route and jurisdiction | Controlled route label and responsible Coworker/stage owner |
| Delivery / governance status | Controlled status and health, or an explicit pending status |
| Latest source | Exact controlled source/path or supplied evidence used |
| Source date | Date of the latest source |
| Last verified | Date/time the position was checked against the source |
| Verification owner | Digital Lead or authorised verifier |
| Confirmation status | Confirmed current / Corrected by Digital Lead / Pending confirmation / Superseded / Not applicable |
| Freshness status | Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable |
| State limitations | Missing, conflicting, unverified or accepted-gap information |
| Open blocker or decision | The item preventing or conditioning the next move |
| Next control move | One route-correct, evidence-led next control action |

“Last edited”, file modified time or chat recency is not a verification. A historical approval confirms a past decision; it does not by itself confirm current status.

If the block is missing, incomplete, stale, conflicting or not confirmed, the Coworker must not use the position as current. Mark the affected position `Pending confirmation`, `Stale` or `Accepted gap` as applicable, identify the consequence and route the required Digital Lead action.

## 3. Deterministic control-check catalogue

Control checks are deterministic tests against the existing controlled records. They identify a failure or recommendation; they do not approve, merge, publish, change scope or alter a client record.

Each check records:

| Field | Required content |
|---|---|
| Check ID | Stable catalogue identifier |
| Trigger | Session, event, stage gate, closeout or scheduled audit that invoked it |
| Condition | The rule tested |
| Evidence | Source/path and verification date |
| Outcome | Pass / Fail / Warning / Accepted gap / Not applicable |
| Severity | Critical / High / Medium / Low |
| Owner | Person or role responsible for resolution |
| Remediation | Required action and due/review point |
| Disposition | Open / Resolved / Deferred / Accepted |
| Approval need | Whether Digital Lead approval is required |

The baseline catalogue is:

| Check ID | Control test | Fail-closed condition |
|---|---|---|
| CCL-001 | Route and lifecycle stage resolve to the deterministic map | Stage, route or jurisdiction cannot be identified |
| CCL-002 | Verified Current State block is complete | Current position is missing, incomplete or unsupported |
| CCL-003 | Current state has a valid source, source date and verification owner | Source is missing, stale, conflicting or unverified |
| CCL-004 | Status, gate, route and next control move are compatible | A record claims a move that its stage or approval does not permit |
| CCL-005 | Required evidence is present or explicitly recorded as missing/accepted gap | A controlled decision or progression lacks required evidence |
| CCL-006 | Decision and approval references are traceable | Approval, condition or decision outcome cannot be evidenced |
| CCL-007 | Open risks, blockers, actions and obligations have ownership and review points | Material unresolved item has no accountable owner or review point |
| CCL-008 | Source-of-truth impact is identified and routed | A material artefact/process/register impact has no controlled update path |
| CCL-009 | Client path and canonical branch are bound and rechecked | Branch/path is missing, stale, divergent, undocumented or ambiguous |
| CCL-010 | Client isolation and provenance are intact | Source, memory, repository or output boundary is uncertain |
| CCL-011 | Handover/closeout contains the required evidence and write-back recommendation | Stage or Coworker transition lacks a governed checkpoint |
| CCL-012 | Change and recovery history is traceable | Material change has no controlled branch, commit/version or recovery reference |

CCL-009 and CCL-010 are always fail-closed. CCL-001 through CCL-006 are fail-closed when the affected output, decision or stage progression depends on the unresolved condition. No check overrides the Digital Lead approval gate.

## 4. Trigger points

Run the relevant checks:

- at material session start, after the Runtime Access and Client Context Gates;
- at the Confirmation-First Status Gate before current position is used;
- when a source, evidence file, export or status update is supplied;
- before a route, gate, stage, scope or approval transition;
- before reporting or workbook refresh;
- after a material change or branch-resolution pass;
- at stage closeout, handover or source-of-truth impact review;
- during the scheduled drift audit.

The Coworker may run additional proportionate checks, but must not remove the mandatory checks for the affected control surface.

## 5. Drift-audit scorecard

Drift is any divergence between the route map, Verified Current State, controlled records, evidence, branch/path, approvals or source-of-truth position.

Drift review is both event-driven and cadence-based:

- material changes and stage gates trigger relevant checks immediately;
- each active controlled workspace receives a periodic audit at the cadence set by its client profile;
- where no client cadence is defined, use a weekly method-maintenance review for the working authority;
- an urgent audit may be requested whenever the Digital Lead identifies suspected drift.

There is no universal stale-after-N-days rule. Apply the event/cadence freshness model in `07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

The audit scorecard must record:

| Field | Required content |
|---|---|
| Audit ID and period | Unique review reference and as-of period |
| Scope | Records, initiatives, branches and artefacts checked |
| Baseline | Method commit, client baseline and relevant artefact revisions |
| Checks run | Catalogue IDs and trigger |
| Results | Pass, fail, warning, accepted gap and not-applicable counts |
| Critical findings | Fail-closed blockers and affected outputs |
| State drift | Missing, stale, conflicting or unverified current-state blocks |
| Evidence drift | Missing, orphaned, superseded or unlinked evidence |
| Governance drift | Route/status mismatch, missing approval or unauthorised progression |
| Source drift | Source-of-truth impact not routed or publication status unclear |
| Branch/path drift | Divergent, duplicate, stale or reporting-invisible branch position |
| Remediation | Action, owner, due/review point and status |
| Trend | Comparison with the previous audit |
| Digital Lead disposition | Approved, deferred, accepted gap or further evidence required |
| Recovery reference | Branch, commit, version or backup reference where applicable |

Audit outcomes are:

- **Clear** — no unresolved material finding;
- **Watch** — warnings or low-impact findings with owners and review points;
- **Blocked** — a fail-closed condition prevents the affected write, report, decision or transition;
- **Accepted gap** — the Digital Lead has explicitly accepted the bounded gap and its consequence.

A drift audit is an assurance output, not an automatic repair command. Remediation is proposed through the normal controlled update route.

## 6. Handover and session integration

The Context and Control Pack is created or refreshed at session spin-up and carried through the Live Session Status Board. The receiving Coworker inspects it at handover but still performs its own access, confirmation and reconciliation gates.

Every material closeout records:

- the Verified Current State position;
- control checks run and unresolved findings;
- drift-audit status and next review point;
- source-of-truth and knowledge-capture recommendations;
- controlled repository, external publication and action-system write-back recommendations;
- the Digital Lead action required.

## 7. Method adoption

A client adopting this standard must create or update its client-side initiative records and workspace controls through an approved method-baseline change. The client copy must not be written back to the public method repository.

A reusable method improvement must be abstracted, client-free, approved by the Digital Lead and released through the method repository's branch and pull-request controls.

## Boundary

This standard adds no approval authority, no automatic mutation authority and no client repository access. It is a control and assurance layer over the existing Strateq DX lifecycle, Coworker, source-of-truth and client-isolation model.
