# Cockpit Feed Contract

## Status and scope

**Proposed version:** `1.0.0`. **Release status:** Draft for Digital Lead review.

This is an interface specification, not an implemented exporter, JSON Schema,
connector or approval to change live client records. It
does not activate a cockpit integration. Adoption requires an approved method
release, a pinned client method baseline, a client export profile and a tested
consumer. Existing client work continues under its approved baseline.

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
proposal does not grant that exception to the isolation standard. Such a view
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

The proposed JSON envelope contains these required fields. Null and empty
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
| `spines` | Versioned ordered stage definitions per board and approved route/PEP applicability rules |
| `initiatives` | Initiative projections described below |
| `actions` | Client-scoped projections from the designated action authority |
| `artifact_references` | Pointer-only evidence records and available download versions, with initiative links, reporting periods, immutable revisions and status |

The executable JSON Schema and consumer adapter are subsequent implementation
work after this proposal is approved. They must encode this specification and
pass the acceptance cases below before a feed is enabled.

## Initiative and stage projection

Each initiative carries stable identity, title, route, board, macro-stage,
lifecycle position, gate position, delivery owner, milestone, target finish,
PEP reference, blockers and next control move where evidenced. Unknown optional
values remain null with a gap reason; do not invent owners, dates or statuses.

Every material status carries its source reference/revision, source date,
confirmation status, confirming actor/date where applicable, freshness and
rationale. Fields with different evidence or confirmation dates must not inherit
a blanket initiative-level confirmation. Stage movements carry the approved
decision reference. Blockers carry an ID, impact, owner or explicit owner gap,
next action/reference and review point where known.

`stage_vector` contains each configured stage once, in spine order, with:

- `stage` and `state`: `complete`, `current`, `not_started` or `not_required`;
- evidence references and a decision reference where a governed gate applies;
- an explicit approved exemption basis for `not_required`;
- action links resolved from the canonical actions by initiative and stage.

There can be several actions for one stage. A UI `action_ref` may select a primary
next action but must not discard the others. Compute `needs_action` from the
approved action/status policy, rather than allowing an independently edited flag.

Board placement and stage cells are display projections, not new governance
stages. Macro-stages, route-specific gates and delivery milestones remain
distinct. No date, RAG colour, action count, file upload or vendor percentage
alone advances a stage. Completion requires the applicable evidence; governed
transitions and exemptions additionally require recorded approval. Corrections
or regressions require an explicit controlled decision, not a newer upload alone.

## Delivery health, blockers and confirmation

Retain the source's original `source_health` label and evidence. Project a
separate `delivery_health`: `Green`, `Amber`, `Red`, `Not applicable` or null.
Null means unassessed/unconfirmed, not Green and not Not applicable.

The following mapping is proposed for approval, not an existing automatic rule:

| Source position | Proposed treatment |
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

This proposal is not a drop-in replacement for the current fixture feed. The
app must retain its working fixture path until the adapter is built and tested.

| Current limitation | Required consumer work before activation |
|---|---|
| Bundled synthetic feeds | Add the authenticated, client-scoped reader; never bundle real client data |
| Two confirmation values and four freshness values | Preserve the complete controlled vocabularies and their display meanings |
| Delivery health requires a non-null colour or Not applicable | Support an explicitly unassessed position and a dated last-confirmed value |
| Actions without an initiative are treated as personal | Distinguish client-scoped administrative actions from truly personal actions |
| Single primary stage action reference | Retain all linked actions while selecting one primary action for display |
| Existing records lack the complete export provenance | Add source/approval references, version checks and accepted-snapshot identity |

No app entity migration, source-profile change or live feed activation is authorized by
opening this proposal. Implement and review those changes in the app workstream
after method approval; report schema, contract and browser tests separately.

## Coworker closeout addition

For a client with an approved cockpit export profile, add these items to the
existing controlled-update closeout; do not introduce another session protocol:

| Closeout item | Required evidence |
|---|---|
| Changed position | Affected initiative/action fields and the source evidence |
| Decision boundary | What is confirmed, proposed, approved, deferred or still missing |
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

Approval of this method proposal is separate from implementation sign-off.
JSON Schema, contract tests, adapters, authorization and authenticated UI tests
must supply runtime evidence before any real feed or download integration is enabled.
