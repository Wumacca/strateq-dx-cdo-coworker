# Initiative Evidence and Decision File Template

## Status

Reusable client-copy template. This file defines the minimum AI-readable initiative evidence and decision record required by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. It is the client-copy implementation of the reusable Initiative Control Record schema (`00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`) and is the single AI-readable per-initiative continuity record — it does not sit alongside a separate interim register.

Do not use this public repository file as a live initiative record. Create the client-specific copy in the bound private client repository or approved client working system. `CLIENT_BOUNDARY.md` and `SOURCE_OF_TRUTH.md` determine the permitted sources and authority.

## Purpose

Provide one current, AI-readable initiative file that every initiative and reporting thread can use without relying on stale chat history.

The file is an evidence and decision continuity record. It must not duplicate the detailed delivery plan, action system or PEP.

## Confirmation statuses

Use only:

- `Confirmed current`
- `Corrected by Digital Lead`
- `Pending confirmation`
- `Superseded`
- `Not applicable`

## 1. Control header

| Field | Value |
|---|---|
| Initiative ID | |
| Client ID | |
| Initiative title | |
| Delivery group | |
| Assigned lifecycle coworker | Live Delivery Coworker |
| Coworker commencement status | Not started / Active / Suspended — awaiting evidence / Pending Digital Lead decision / Pending external approval / Ready for closeout / Closed and handed over |
| Coworker commencement date | |
| Bound AI Project / workspace | |
| Coworker thread name | `HOP / LIVE / CLOSED \| [Group] \| [Initiative]` |
| Client-boundary gate result | |
| Initiative origin | |
| Originating artefact / reference | |
| Requesting area | |
| Sponsor | |
| Digital Lead | |
| Business / delivery owner | |
| Approved route | |
| Entry basis | |
| Authority to proceed | |
| Delivery model | |
| Current lifecycle stage | |
| Current delivery-record status | |
| Detailed-plan owner / reference | |
| PEP/client-control-plan owner / reference | |
| Budget/cost owner | |
| Digital financial-reporting basis | |
| Acceptance / go-live authority | |
| Reporting period | |
| Latest information source | |
| Digital Lead confirmation status | |
| Last confirmed by Digital Lead | |
| Last confirmation date | |
| File version / date | |
| Context and Control Pack status / reference | |
| Verified Current State status | Current / Pending confirmation / Stale / Accepted gap |
| State as-of date/time | |
| Last verified date/time / verifier | |
| Freshness status | Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable |
| Last control-check run / outcome | |
| Drift-audit ID / status / next review | |

## 2. Current confirmed position

State the current position in no more than five short points:

- Current status:
- What changed since the previous update:
- Current delivery / governance health:
- Main issue requiring attention:
- Next control move:

## 2a. Verified Current State (mandatory)

Complete this block before using any initiative position as current. It is the client-side implementation of `00_system_control/18_CONTEXT_AND_CONTROL_LAYER_STANDARD.md`.

| Field | Value |
|---|---|
| As-of position and date/time | |
| Lifecycle position / current gate | |
| Route / responsible Coworker | |
| Delivery / governance status and health | |
| Latest source/path and source date | |
| Last verified date/time and verification owner | |
| Digital Lead confirmation status / last confirmation | |
| Freshness status | |
| State limitations / accepted gaps | |
| Open blocker or decision | |
| Next control move | |

If any required field is missing, stale, conflicting or unverified, mark the affected position `Pending confirmation`, `Stale` or `Accepted gap` and state the consequence. Do not infer current status from file dates, prior chat or historical approval.

## 3. Approval and decision position

| Decision / approval | Required from | Status | Date | Conditions / notes | Evidence reference |
|---|---|---|---|---|---|

Record only confirmed decisions. Mark anything not evidenced as `Pending confirmation`.

## 4. Scope and delivery basis

### Approved scope

- 

### Exclusions

- 

### Dependencies and constraints

- 

### Funding / CAPEX basis

- 

### Responsibility and reporting basis

- Detailed-plan owner:
- Client-control-plan owner:
- Budget/cost owner:
- Digital financial-reporting basis:
- Reporting audiences/cadence/cut-off/validator:
- Acceptance and go-live authority:

## 5. Delivery position

| Field | Confirmed position |
|---|---|
| Delivery health | On Track / At Risk / Blocked / Closed / Pending confirmation |
| Current milestone | |
| Progress position | |
| Target finish | |
| Work completed this period | |
| Next fortnight work | |
| Acceptance / handover readiness | |

## 6. Risks and blockers

| Risk / blocker | Impact | Owner | Mitigation / next action | Due / review point | Status |
|---|---|---|---|---|---|

## 7. Actions and controlled-system references

| Action | Owner | Due date | System/reference | Latest status supplied | Confirmation status |
|---|---|---|---|---|---|

This table records references and the latest Digital Lead-confirmed position only; it must not become a duplicate action register.

## 8. Evidence and artefacts

| Evidence / artefact | Purpose / applicability | Status | Canonical location / reference | Latest version or update date | Last verified | Freshness / reconciliation | Owner / required action |
|---|---|---|---|---|---|---|---|

Include, where relevant:

- originating request, transition/enterprise mandate, contract, procurement approval or leadership instruction;
- Completed Initiation Form and approval evidence;
- scope / requirements / process artefacts;
- delivery and milestone evidence;
- testing, acceptance, training, adoption, benefits, and closeout evidence;
- source-of-truth impact record.
- For each applicable artifact, record the latest known update date/version, last verification, freshness and whether the latest copy was supplied, confirmed unchanged, missing, conflicting, superseded or not applicable. Preserve unknown dates as Unknown until verified.

## 9. Source-of-truth impact

| Artefact / register affected | Impact | Required update | Owner | Timing | Approval status |
|---|---|---|---|---|---|

## 10. Required controlled updates and publications

| Target | Required update | Status | Owner | Completion confirmation / date |
|---|---|---|---|---|
| Bound private client repository | | Pending / Completed / Deferred / Not applicable | | |
| External publication destination | | Pending / Completed / Deferred / Not applicable | | |
| Action/delivery system where configured | | Pending / Completed / Deferred / Not applicable | | |

The Coworker may prepare an approved repository branch. The Digital Lead approves merge/release and performs or confirms external publication.

For an activated cockpit export profile only, include generated-feed handoff and
verified receipt in the session closeout under
`02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md`. Reference the export
and acknowledgment rather than copying its data into a second status table.
Where the integration is absent, state `Not implemented`; do not claim a sync.

The closeout also identifies the confirmed control-applicability profile and
revision, any required/N/A/unresolved control changes, and the supporting rule
or decision. Link to the applicable setup/profile rather than duplicating it.
An enterprise mandate may replace the Initiation Form as the entry basis where
the approved profile permits; it does not remove authority-to-proceed checks.

## 11. Reporting extract

Use only confirmed information.

### Bi-weekly programme update

- Status / health:
- Progress this period:
- Next fortnight:
- Decisions required:
- Risks / blockers:
- Client actions:

### Monthly leadership significance

- Outcome / control movement:
- Material risk or assurance point:
- Decision / escalation required:
- Funding / benefit / adoption significance where evidenced:

## 12. Change log

| Date | Confirmed change | Source | Files / systems affected | Digital Lead confirmation | Updated by |
|---|---|---|---|---|---|

## 13. Context and Control audit

| Audit / check | Trigger or period | Result | Severity | Finding / evidence | Owner | Remediation / review point | Digital Lead disposition |
|---|---|---|---|---|---|---|---|

Record applicable control checks from `00_system_control/18_CONTEXT_AND_CONTROL_LAYER_STANDARD.md`, including route/stage, current-state completeness, source/freshness, evidence, approval traceability, open obligations, source-of-truth impact, branch binding, client isolation and recovery/change traceability. This is an assurance projection over the existing records, not a second status or action register.

## Update-once rule

When an update is confirmed in an initiative, bi-weekly, or monthly reporting session:

1. update this initiative evidence and decision file first;
2. update any separate controlled decision or evidence artefact affected;
3. identify private-repository, action-system and external-publication write-backs;
4. generate reporting wording from the updated confirmed position.

No material initiative fact may remain only in a chat or reporting thread.

## Portfolio coverage check

Complete when a new initiative affects other work or when preparing an all-initiative/programme output.

| Registry/reporting-source revision and ref | In-scope initiative/workstream IDs | Latest EIDF/PEP/control refs and source dates checked | Reporting visibility | Missing/stale/conflicting/inaccessible/excluded items | Verifier / date |
|---|---|---|---|---|---|

Record links and verification outcomes, not copied initiative status. Each initiative's EIDF remains its own status authority. Do not claim portfolio completeness when the scope source, a required initiative record or its latest status is unavailable; ask for clarification or record an accepted gap.

## Boundary

The Coworker may prepare or revise this file inside the bound client repository when authorised. It must not claim an external publication or system update without evidence or Digital Lead confirmation.

## Central Live Status and branch binding

Add these control-header fields to every client copy: central Live Status thread/equivalent; controlled initiative/workstream path; canonical working branch; client branch-registry row; last branch verification; branch status versus approved reporting source; duplicate/stale/non-canonical branch disposition; reporting visibility; blocker/decision required; safe next action; programme action tracker and thread tracker references. Updates arriving through the central thread are reconciled into this EIDF on the originating branch. Mixed updates stay separate. Reporting extracts remain pending until the approved reporting source is current.

## Branch resolution and source recheck fields

Add to the control header/change log: registry revision read; canonical branch versus `main`; controlled home; source index; setup file; RAID/action log; verification date; candidate branches; preserved branch-only commits; authorised consolidation decision; no-routing branches; branch-only position; reporting-visible position; and blocker/safe next action. Do not mark the record reportable until the approved reporting source is current.
