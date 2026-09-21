# Cockpit Feed Contract

## Status and scope

**Contract version:** `1.0.0`. **Status:** Approved method specification for implementation; integration not activated.

This is an interface specification, not an implemented exporter, JSON Schema,
connector or approval to change live client records. The controlled merge
releases this method specification; it does not activate a cockpit integration.
Client adoption requires a controlled update to the pinned method baseline,
an approved client export profile and a tested consumer. Existing client work
continues under its approved baseline until that adoption is completed.

The contract describes a generated, machine-readable projection of the bound
client's controlled records for the consultant's personal cockpit. It creates
neither a third lifecycle coworker nor another independently maintained status
record. It does not redesign the PEP or the approved meeting-minutes layout.

Working-file uploads and updates enter the bound AI initiative chat, not the
cockpit. The app has no artefact upload/import workflow, raw-document extraction,
document-generation chat or AI ingestion of working files. Its status reader
consumes the controlled metadata projection; its Artefacts page locates and
downloads already-produced files. That background read is not a user-facing
file-import feature.

## Authority and responsibilities

The authority files remain `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`,
`00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`,
`00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`,
`00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md` and the applicable
lifecycle files selected through `CLAUDE.md` B2.

| Responsibility | Owner |
|---|---|
| Interpret evidence, identify gaps, propose health, blockers, actions and the next control move | Bound Hopper or Live Delivery Coworker |
| Confirm the business position and approve controlled updates and transitions | Digital Lead; required governance-body decisions must also be evidenced |
| Hold initiative continuity, delivery controls and actions | The respective authorities named in the client profile |
| Produce and validate the approved projection | Deterministic exporter operating within the client allowlist |
| Compute counts and overdue indicators; render the last accepted projection | Cockpit read model |

An AI model may draft a proposed change, but cannot approve it or bypass source
controls. GPT and Claude must use the same approved contract and method baseline.
Model selection must not change progression rules or field meanings.

## Client export profile

Before activation, the bound client's `SOURCE_OF_TRUTH.md` must name:

- the initiative, PEP, action and approval authorities and their allowed paths;
- the approved method commit and contract version;
- the destination, permitted summary fields and named viewer of the cockpit;
- the board-spine configuration, route exceptions and mapping-policy version;
- the action-system edit route, date timezone and freshness/review policy;
- the exporter, read-only source permissions and generated-output location;
- the feed acknowledgment location and failure/reconciliation owner.

Client facts and feeds must never be committed to the public method repository
or bundled into the app's shared source repository. Reusable rules remain here;
app code remains in its own repository; client records stay in their designated
private authority. No global directory of client repositories is added here.

Each export and AI job binds exactly one client. An all-client cockpit view needs
explicit authorization for the selected summaries from each client profile and
an approved consultant-view policy before real client data is enabled. This
contract does not grant that exception to the isolation standard. Such a view
does not permit an AI job to load several clients' evidence or prompts together.
Personal actions are held separately and are never inserted into a client feed.

## Publication sequence

1. Read the allowlisted sources and establish the confirmation-first position.
2. Propose changes, evidence gaps, actions and any stage-transition decision.
3. Obtain approval for the controlled file updates; confirmation alone is not
   permission to write. Observe any separate stage gate and next-stage spin-up.
4. Apply the authorized source updates through the client's controlled route.
   Capture evidence of the released source revision and required write-backs.
5. Generate and validate the feed from that released revision. Proposed changes
   remain in review; do not insert their new values into confirmed feed fields.
6. Refresh the read-only app projection and record the accepted feed identity.
   Show success only after the destination acknowledges that exact identity.

If source updates or export are deferred, retain the last accepted projection
with its age and pending-update warning. Do not claim the dashboard has synced.
Pending external publication is tracked independently; it must not conceal a
Digital Lead-confirmed position in the controlled working authority.

## Feed envelope

The JSON envelope must contain these required fields. Null and empty
collections have explicit meanings; neither means an inferred fact or deletion.

| Field | Contract |
|---|---|
| `contract_version` | Exact supported version, initially `1.0.0` |
| `client_id` | Exact bound client ID; also present on every domain record |
| `feed_id` | Immutable identity reused when the same export is retried |
| `generated_at` | UTC generation timestamp, distinct from business confirmation |
| `method_revision` | Approved method commit pinned by the client baseline |
| `mapping_version` | Approved status and lifecycle projection policy revision |
| `source_manifest` | Source IDs, allowed locations, immutable revisions/hashes, source dates and release/approval evidence references; no credentials or artefact bodies |
| `coverage` | Explicit `client` or `initiatives` scope and the exact included initiative IDs; omissions never mean removal |
| `spines` | Versioned ordered stage profiles per board, with approved route/PEP applicability rules; each initiative references its selected profile/revision |
| `initiatives` | Initiative projections described below |
| `actions` | Client-scoped projections from the designated action authority |
| `artifact_references` | Pointer-only evidence records and available download versions, with initiative links, reporting periods, immutable revisions and status |

The executable JSON Schema and consumer adapter remain subsequent implementation
work. They must encode this specification and
pass the acceptance cases below before a feed is enabled.

## Initiative and stage projection

Each initiative carries stable identity, title, initiative type, route, entry
basis, delivery model, applicability-profile reference/revision, selected
spine-profile ID/revision, board, macro-stage,
lifecycle position, gate position, delivery owner, milestone, target finish,
PEP reference, blockers and next control move where evidenced. Unknown optional
values remain null with a gap reason; do not invent owners, dates or statuses.

Every material status carries its source reference/revision, source date,
confirmation status, confirming actor/date where applicable, freshness and
rationale. Fields with different evidence or confirmation dates must not inherit
a blanket initiative-level confirmation. Stage movements carry the approved
decision reference. Blockers carry an ID, impact, owner or explicit owner gap,
next action/reference and review point where known.

`stage_vector` contains each stage of the selected approved profile once, in
that profile's spine order, with:

- `stage`, resolved `applicability`, its rule/evidence basis and `state`:
  `complete`, `current`, `not_started` or `not_required`; where applicability
  remains `pending_resolution`, state is null and the UI shows To confirm;
- separate `stage_health`, health basis, freshness and linked blocker/action IDs;
- deliverable and acceptance-criterion references supporting that cell;
- evidence references and a decision reference where a governed gate applies;
- an approved non-applicability rule or explicit exception basis for `not_required`;
- action links resolved from the canonical actions by initiative and stage.

There can be several actions for one stage. A UI `action_ref` may select a primary
next action but must not discard the others. Compute `needs_action` from the
approved action/status policy, rather than allowing an independently edited flag.

Board placement and stage cells are display projections, not new governance
stages. Macro-stages, route-specific gates and delivery milestones remain
distinct. No date, RAG colour, action count, file upload or vendor percentage
alone advances a stage. Completion requires the applicable evidence; governed
transitions and exceptions additionally require recorded approval. Corrections
or regressions require an explicit controlled decision, not a newer upload alone.

## Initiative-specific control applicability

### Delivery definition before applicability

The Coworker must first understand what the initiative is actually contracted or
mandated to deliver. Use the confirmed delivery definition in
`02_coworker_artifact_interface/07_INITIATIVE_DELIVERY_SETUP_MODEL.md` and
`02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md`, or the
equivalent controlled scope for the active lifecycle stage. Do not start with a
generic implementation checklist and treat it as the initiative's scope.

Resolve outcome, Digital's responsibilities, delivery approach, explicit
exclusions, deliverables, acceptance criteria, necessary external dependencies,
owners, acceptance authority and agreed targets/review triggers. Unknown criteria
remain visible gaps. The confirmed profile references this controlled definition
and the actual required gates, not just a broad initiative-type label.

For an illustrative export-only initiative, the confirmed gates might be:

| Possible gate | Evidence to agree for that initiative |
|---|---|
| Export requirements and authority agreed | Authorized scope, source, recipient, format and agreed data cut-off |
| Extraction ready / produced | The required export, against the agreed extraction specification |
| Export verified | Agreed completeness/integrity checks and disposition of exceptions |
| Handover accepted | Evidence the designated recipient accepted the agreed deliverable |

These are examples to tailor and confirm, not a newly mandated universal route.
Target-system migration, data cleansing, transformation/mapping, full system
UAT, cutover or hypercare may be N/A when excluded from the agreed scope. Export
verification is still required where it is part of the acceptance criteria;
marking migration N/A does not imply that the export can be unverified.

An externally owned activity remains a dependency if this initiative needs it
to deliver or obtain acceptance. Record that owner and dependency evidence
without importing the other party's full implementation plan. The initiative's
RAG describes its own agreed outcomes and dependencies, not the completion
percentage or status of the entire parent programme.

### Resolve applicable controls

Resolve what is required before assessing completion or RAG. The same board
column can be required for one initiative and not required for another. Its
absence must not create a false overdue action, blocker or Red assessment.

The applicability profile uses independent dimensions, not a single type label:

- initiative type and scope;
- approved route and route-specific exception triggers;
- entry basis and evidenced authority to proceed;
- delivery model and the split of Digital, vendor and client responsibilities;
- approved client requirements and the configured board/PEP controls.

Use the existing route and mobilisation authorities, particularly
`01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`,
`01_governance_lifecycle/12_STAGE_3_LIVE_DELIVERY_CONTROL_MODEL.md` and
`02_coworker_artifact_interface/08_INITIATIVE_DELIVERY_SETUP_TEMPLATE.md`.
Do not create new route labels. Descriptive enterprise-project support is not
automatically the controlled `Support Route`; confirm route independently.

Each stage/control has `applicability` = `required`, `not_required` or
`pending_resolution`, plus `rule_id`, `rule_version`, rationale, evidence
references and the confirmed applicability-profile revision. Where a rule is
conditional, record the condition and its evaluated inputs. Resolve it to
required/not required only when the inputs and authority support that result;
otherwise keep it pending. A required control can be not started or not yet due.

For an explicit exception, also retain the approving authority, decision date,
conditions and review trigger. Applying an already-approved method/profile rule
does not require a new exception approval for every cell. Changing that rule or
waiving an otherwise required control does require controlled approval.

| Evidenced initiative context | Applicability treatment |
|---|---|
| Enterprise/transition-project support entered under a confirmed enterprise mandate or leadership instruction, with no separate Initiation Form requirement | Initiation Form is N/A under the approved entry profile; retain the mandate/decision evidence. Authority to proceed and applicable mobilisation controls still apply. |
| Development Route through Stage 1D, with no Stage 2 exception and confirmed approval of that path | Stage 1D remains required; Stage 2 is N/A under the confirmed route rule. Existing DRB approval and Live Delivery handover controls remain. |
| Development Route with an evidenced Stage 2 exception trigger | Stage 2 is required; do not inherit the no-exception N/A treatment. |
| Implementation/Support Route entered through the formal initiation path | Apply the route's initiation requirements; an enterprise-support label does not remove them. |
| Vendor-led implementation | Vendor ownership does not make client acceptance, interfaces or assurance controls N/A; resolve responsibilities and evidence references. |
| Data/integration/testing control outside approved scope | N/A only where the approved profile establishes non-applicability; a missing document is insufficient. |
| Type, entry authority, condition or scope unresolved | To confirm, with the unresolved question and owner; do not assume N/A or Green. |

These examples apply existing method rules; they are not blanket waivers by
initiative name. The absence of an Initiation Form may be legitimate; an
unresolved authority-to-proceed gap still prevents entry to In Delivery.

The bound coworker proposes and reconciles the profile at intake/spin-up and
revisits it when route, scope, entry basis, responsibilities or method baseline
changes. Carry its confirmed reference in the single Initiative Evidence and
Decision File and, for mobilisation, the applicable Initiative Delivery Setup.
The app consumes that profile; it does not guess applicability from missing
files, a free-text title or the selected board. Changes create a new controlled
profile revision and preserve previously released historical snapshots.

### Map actual delivery criteria to the board

Bind every required delivery/acceptance criterion to an appropriate gate/cell
and its evidence/actions in the selected stage profile. Several criteria may
contribute to one gate, but a gate is not complete because only one criterion
is satisfied. All mandatory criteria must be met, or any permitted conditional
progression must carry the exact approval, outstanding obligation and review
point. Every required criterion must remain discoverable from the matrix/drawer.

Reuse a stage profile when it genuinely fits. Where a generic implementation
spine misrepresents the work, configure an approved initiative-specific profile
with meaningful gate names; do not label export handover as a system go-live.
This changes the delivery display, not the governed macro-lifecycle or route.
Group compatible profiles on a matrix and retain shared portfolio fields across
profiles; do not force unrelated stage columns to have equivalent meanings.

At each confirmed source update, reassess criterion progress, evidence, remaining
work, blockers and dates, then produce the cell state/RAG and next action.
Criteria changes must be controlled and versioned. Do not manufacture percentage
complete by dividing generic stage counts, silently weaken criteria to obtain
Green, or recreate historical reports with the latest profile.

## Mieruka cell assessment and roll-up

Evaluate a cell in this order: applicability, completion/evidence/approval,
confirmation/freshness, then the approved stage-health policy.

| Cell position | Display and control behavior |
|---|---|
| Confirmed not required | Neutral N/A, `state: not_required`, `stage_health: Not applicable`; expose the reason and rule. Exclude from applicable-stage denominators. |
| Applicability unresolved | To confirm, null state/health; expose missing evidence or decision. Show an unresolved count and do not claim full readiness. |
| Required but not yet due | Not started/planned; assess risks only where evidenced. Not automatically Amber or Red. |
| Required and evidence/approval complete | Complete marker with its evidence; completion does not determine initiative delivery RAG. |
| Required with a current material risk or blocker | Show the evidenced stage RAG and separate blocker/action details under the approved severity policy. |
| Previously assessed but now stale/unconfirmed | Show the dated last-confirmed position with a warning; no fresh Green or silently renewed N/A assertion. |

An accepted gap is not N/A and not completion. Keep the required control, gap,
owner, conditions and review point visible; any conditional progression must
refer to the approving decision. A deferral is not non-applicability either.

Stage health is separate from the initiative's overall `delivery_health`. Do not
paint every stage with the initiative colour, average colours, or count N/A as
completed work. Required gate failures and unresolved applicability remain
visible even if an overall health assessment has been confirmed. Any roll-up
must use a documented client-approved policy with contributing reasons; absent
that policy, preserve the explicit confirmed overall assessment and exceptions.

`stage_health` uses Green, Amber, Red, Not applicable or null. Reserve Not
applicable for a confirmed non-applicable control. Null means no current health
assessment and must not be rendered as Green. A completion marker is a separate
visual indicator and is not itself a RAG assessment.

Do not close linked actions solely because a profile now marks their stage N/A.
Reconcile those actions through their authority and retain any remaining
obligations. N/A is not a mechanism for hiding blockers or making progress rise.

## Delivery health, blockers and confirmation

Retain the source's original `source_health` label and evidence. Project a
separate `delivery_health`: `Green`, `Amber`, `Red`, `Not applicable` or null.
Null means unassessed/unconfirmed, not Green and not Not applicable.

The following mapping defines the contract treatment. It must be implemented
and adopted in the client mapping profile before use; it is not an active rule
in the current app:

| Source position | Contract treatment |
|---|---|
| Confirmed `On Track` | Green, with source/rationale and current confirmation |
| Confirmed `At Risk` | Amber, with source/rationale and current confirmation |
| `Blocked` | Record the blocker; use an explicitly confirmed RAG assessment, not an automatic Red mapping |
| `Closed` | Record approved lifecycle closure; do not infer Green or Not applicable |
| `Pending confirmation` | Keep confirmation pending; no current RAG assertion |
| Explicitly confirmed Green, Amber or Red | Preserve the approved assessment and its evidence |
| Explicitly approved non-applicability | Not applicable, with its basis |
| Missing, conflicting or unmapped position | Null current assessment and a visible review reason |

A client-approved RAG policy must define when material delivery impact requires
Red; AI cannot invent a threshold or downgrade a confirmed Red assessment. RAG
describes delivery health, a blocker describes an impediment, and overdue
describes an action date. None silently overwrites the others.

Preserve all confirmation values from the initiative template:
`Confirmed current`, `Corrected by Digital Lead`, `Pending confirmation`,
`Superseded`, `Not applicable`. A corrected position needs evidence of the
correction and its controlled source update; it is not an AI correction.

Preserve all freshness values from `07`: `Current`, `Revalidation due`, `Stale`,
`Superseded`, `Pending confirmation`, `Not applicable`. Apply the configured
event/cadence policy; never make up a universal stale-after-days threshold.

An old confirmed value can remain visible as **last confirmed**, with its date
and freshness warning. It must not count as a current confirmed assessment.
Refreshing or reopening the app does not reconfirm business status.

## Initiative artefact downloads and history

The Artefacts feature is a read-only catalogue and download surface. Its workflow
is: select the client/initiative, select an available artefact, choose its
reporting week or week-ending date and available version, then download it.
An all-client filter may aid navigation only under the summary permissions above;
the actual artefact selection and access checks remain client/initiative scoped.

Include PEPs, other released initiative artefacts, and **initiative-level
executive and leadership reports**. These reports must be selectable against
the initiative, not available solely as portfolio-wide outputs. If a programme
report is shared by several initiatives, label it as a shared report; do not
present the entire programme report as an initiative-specific report or expose
another client's material. A genuine initiative-level report must already exist
as a released output from the governed AI initiative work.

Each downloadable version carries:

| Field | Purpose |
|---|---|
| `artifact_id`, `artifact_version_id` | Stable artefact identity plus an immutable version identity |
| `client_id`, `initiative_id` | Ownership and initiative association, checked on every download |
| `artifact_type`, `title` | PEP, executive report, leadership report or another approved type |
| `reporting_period_start`, `reporting_period_end` | Business period covered, where applicable |
| `week_ending` | Configured reporting-week end date, not inferred from upload time |
| `revision`, `source_revision`, `content_hash` | Exact released file version and integrity evidence |
| `released_at`, `approval_ref`, `release_status` | Release evidence, distinct from the reporting period |
| `filename`, `media_type`, `size_bytes`, `storage_ref` | Download metadata and an allowlisted private location, never credentials or file bodies |

The client profile fixes the reporting-week convention and timezone. A week-date
selection resolves to that convention; the UI shows the actual selected period.
Monthly/other-period reports keep their true periods and are not relabelled as
weekly reports. A week filter must state whether it matches the report's covered
period or its release week. Do not invent weekly reports or new reporting cycles.

List only genuinely available versions as downloadable. Missing, unpublished,
revoked or inaccessible files show an explicit unavailable state. Do not silently
substitute a different week, the latest version or a different initiative. If
several revisions cover a period, let the user choose the revision and show dates.

Historical downloads return the exact saved file for that period and revision,
not a report regenerated using today's data. Released versions must not be
overwritten; corrections create a new version with its own release evidence.
Older superseded releases remain identifiable and downloadable only where the
client's retention/access policy permits. A release, retention or permission
change must not leave a misleading enabled download link.

File bytes remain in approved private source storage. The app authorizes and
streams the selected file or issues a short-lived authorized download link; it
does not place bodies in entity records, source-control bundles or public URLs.
Do not follow arbitrary user-supplied storage URLs with service credentials.

There are no Upload, Import, Replace file or Regenerate historical report
controls in this feature. Working revisions and newly requested reports go
through the AI initiative chat and the existing approval/release process.

## Actions and derived signals

Each action carries a stable `action_id`, `client_id`, description, owner or
explicit owner gap, due date or null, canonical status, source/revision and
confirmation metadata. `initiative_id` is optional; `stage` is optional and must
be null without an initiative. A stage link must resolve within that initiative's
configured spine. Client-scoped administrative actions need not invent an
initiative. Purely personal actions remain outside this per-client contract.

Canonical action statuses are `Open`, `In progress`, `Blocked`, `Done` and
`Cancelled`. Source-system labels need an explicit mapping. Unknown labels are
validation failures, not silently Open. Missing actions in a later extract are
not automatically Done, Cancelled or deleted.

The app derives:

- open counts from Open, In progress and Blocked actions in the selected scope;
- overdue from an open status and a due date before today's date in the approved
  timezone; date-only deadlines are not overdue on the due date itself;
- unconfirmed, blocked and revalidation indicators independently;
- primary next action using a documented, deterministic selection rule.

Pending-confirmation actions remain visible as unresolved and explicitly
unconfirmed. Separate confirmed and unconfirmed totals where a headline would
otherwise imply every item is current. Null dates are undated, not overdue.

Client action edits in a future cockpit must follow the designated authority's
controlled update route and then refresh the projection. The app must not claim
an edit has reached that authority before acknowledgment. Selecting the cockpit
as an action authority requires a separate explicit profile decision and tested
write path; it is not activated by this contract.

## Feed reading and reconciliation controls

- Validate client binding, supported versions, source/release provenance, dates,
  enums, spine order/applicability, ownership and referential integrity server-side.
  Never trust a browser-supplied confirmation or approval flag as authorization.
- Use client-qualified record keys. Reject duplicate keys within a feed; never
  resolve an initiative or action using another client's record.
- Replaying an accepted `feed_id` with the same content is a no-op. Reusing it
  with different content is rejected. Record feed identity and content hash.
- Verify source revision ordering using the configured authority. `generated_at`
  is not proof a source is newer. Stale, divergent or unverifiable revisions go
  to reconciliation and cannot overwrite the accepted projection.
- Do not publish a partially imported dataset to some views. Validate and stage
  a complete accepted snapshot before switching the read model. A failed refresh
  retains the previous snapshot and visibly reports the error.
- Preserve explicit source closure, cancellation and supersession. This v1
  interface never hard-deletes records merely because they are omitted.
- Render source text as data, not executable content or AI instructions. Reject
  out-of-allowlist references and unsafe links; never follow arbitrary pointers
  with service credentials. Store pointer metadata, not artefact/PEP bodies.

These are implementation requirements, not claims that the current seed function
or platform provides transactions, atomic locks or the completed integration.
Do not use `seedFromFixtures` as the production reader or retirement mechanism.
These internal snapshot controls do not authorize artefact imports or uploads.

## Compatibility with the existing cockpit

This contract is not a drop-in replacement for the current fixture feed. The
app must retain its working fixture path until the adapter is built and tested.

| Current limitation | Required consumer work before activation |
|---|---|
| Bundled synthetic feeds | Add the authenticated, client-scoped reader; never bundle real client data |
| Two confirmation values and four freshness values | Preserve the complete controlled vocabularies and their display meanings |
| Delivery health requires a non-null colour or Not applicable | Support an explicitly unassessed position and a dated last-confirmed value |
| Actions without an initiative are treated as personal | Distinguish client-scoped administrative actions from truly personal actions |
| Single primary stage action reference | Retain all linked actions while selecting one primary action for display |
| Existing records lack the complete export provenance | Add source/approval references, version checks and accepted-snapshot identity |
| Stage cells lack a complete applicability decision and separate stage-health basis | Add the versioned initiative profile, per-control rule/evidence, explicit unresolved applicability and independent cell health |
| Board spines are currently selected at client/board level | Resolve an initiative's approved stage-profile revision, map its deliverable/acceptance criteria and group compatible profiles without mislabelling stages |

Releasing this method specification does not itself authorize an app entity
migration, client source-profile change or live feed activation. Implement and
review the consumer changes in the app workstream, and adopt client profiles
through their controlled route. Report schema, contract and browser tests separately.

## Coworker closeout addition

For a client with an approved cockpit export profile, add these items to the
existing controlled-update closeout; do not introduce another session protocol:

| Closeout item | Required evidence |
|---|---|
| Changed position | Affected initiative/action fields and the source evidence |
| Decision boundary | What is confirmed, proposed, approved, deferred or still missing |
| Control applicability | Profile revision, required/N/A/unresolved controls, changed conditions and decision evidence |
| Delivery criteria | Actual deliverables, completion/acceptance evidence, owned scope, necessary external dependencies and cell mapping |
| Source write-back | Authority, exact revision and completed/pending status |
| Feed handoff | Contract version, covered IDs, generated location and feed identity, or reason not generated |
| Cockpit receipt | Accepted identity and timestamp, or pending/failed; never assumed |
| Next control move | Required action, responsible owner and decision/review trigger |

The exporter generates the data from the approved sources. The Digital Lead
does not maintain a second manual JSON register. If the exporter is not built,
report that limitation; a drafted extract is not a published or accepted feed.

## Acceptance gate before activation

Use synthetic fixtures and an isolated test destination, not real client writes:

1. One approved source change produces matching Portfolio, Boards, Needs
   Progressing, Actions and initiative-detail views from one accepted snapshot.
2. Re-reading the same feed creates no duplicates; altered identity reuse is rejected.
3. Stale and conflicting revisions do not replace the accepted position.
4. A stage move without required approval fails, even with no open actions.
5. An overdue action does not automatically turn the initiative Red or advance it.
6. Missing, corrected, superseded and unconfirmed statuses preserve their meaning.
7. A wrong-client reference fails without reading or mutating that other client.
8. Partial coverage never deletes omitted records or closes omitted actions.
9. Several actions on one stage, unlinked client actions and undated actions render correctly.
10. An interrupted refresh leaves the previous snapshot consistent across all pages.
11. Unauthorized source locations, invalid references, enums and dates are rejected.
12. Summary export permission is enforced without combining client AI contexts.
13. Selecting an initiative exposes its PEP and available initiative-level
    executive/leadership reports, with exact period and revision choices.
14. A historical download matches the saved version/hash; a missing period has
    no substitute download and creates no new report.
15. Cross-client, revoked and unauthorized downloads are denied server-side.
16. No artefact upload/import, replacement or regeneration route exists in the
    app; working-file updates remain in the AI initiative chat.
17. Enterprise-project support with a confirmed alternative authority and an
    approved no-form profile shows Initiation Form as N/A, while mobilisation
    and authority-to-proceed checks still operate.
18. Without evidenced authority, a missing Initiation Form does not authorize
    entry to In Delivery; applicable unresolved gates remain visible.
19. Development Route with and without a Stage 2 exception produces different
    applicability; no blanket type label overrides a route-specific condition.
20. Missing evidence, accepted gaps, deferred work and unknown applicability
    never become N/A or completed automatically.
21. N/A controls are excluded from applicable-stage totals; unresolved controls
    prevent a false full-readiness claim, and future required stages are not
    automatically Red merely because they have not started.
22. Different stage risks produce independent cell RAG, with evidence, without
    copying the overall initiative RAG across the row.
23. A scope/profile change records its authority and re-evaluates applicability
    without closing actions or rewriting saved historical reports.
24. An export-only synthetic initiative is assessed against its confirmed export
    deliverables, checks and handover; excluded implementation activities do not
    create false failures, missing artefacts or overdue actions.
25. An externally owned prerequisite remains visible where needed for the
    initiative's delivery; external ownership alone does not make it N/A.
26. Every required acceptance criterion resolves to a suitable gate/cell and
    source evidence; one completed criterion does not complete a multi-criterion
    gate or imply that the parent programme has finished.
27. Different approved delivery profiles render meaningful columns/groups;
    export acceptance is not presented as target-system migration or go-live.
28. Missing or changed delivery criteria require reconciliation and controlled
    approval; they do not produce invented requirements or a silent Green result.

Approval of this method specification is separate from implementation sign-off.
JSON Schema, contract tests, adapters, authorization and authenticated UI tests
must supply runtime evidence before any real feed or download integration is enabled.
