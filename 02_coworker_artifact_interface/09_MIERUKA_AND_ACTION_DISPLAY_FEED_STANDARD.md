# Mieruka and Action Display Feed Standard

## Status

Reusable, client-agnostic **specification** for the machine-readable projection that a read-only display layer (for example a Base44-class personal cockpit, a static dashboard, or any Mieruka board) consumes to render live initiative status, the action log, and pointers to the latest artefacts (PEP, Initiation Form, process pack, reports).

This file is a specification only. It defines the shape of the feed, not any client's data. No populated feed is ever committed to this public method repository.

The feed is a **derived display projection**, not a record of authority. It is regenerated from the single AI-readable per-initiative continuity record — the **Initiative Evidence and Decision File** (`02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`, implementing schema `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`). It adds no facts, holds no authority, and is never itself an AI-readable continuity record. Where this standard and any authority file conflict, the authority file governs and the conflict is surfaced to the Digital Lead.

## Purpose

Give the Digital Lead a single visual cockpit — portfolio Mieruka, action management, and latest-artefact access — driven entirely by the governed files, without introducing a second source of truth.

- **Display reads** the feed to render status. It does not compute or invent status.
- **The display owns nothing.** The feed is generated from confirmed governed records; the governed records remain the source.
- **The only write path** is the governed action write-back defined in Sections 7 and 7a, which routes back through the update-once rule and Digital Lead confirmation.

## First-principle boundaries (read before use)

1. **No second source of truth.** The feed never becomes a parallel initiative record, action register, or programme-memory ledger. It is a projection of the Initiative Evidence and Decision File and the governed action position. Schema `13` permits exactly one AI-readable per-initiative record; this standard does not create another.
2. **The feed lives in the bound private client repository**, alongside the live records it projects — never in this public method repository, and never in a location that mixes clients.
3. **One client per feed.** Under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` there is no stored file that aggregates more than one client. A consultant's multi-client "desktop" view is composed **at display time** by the app reading each separately-bound client repository's own feed; it is never a combined file written into any repository. A display-layer cache is permitted only if partitioned per client, rebuildable from the repository, and never treated as authority. A cache may hold display fields only: artefact and PEP **bodies never enter it**. `artefacts[].ref` and `linked_pep` are pointers resolved against the repository when opened, so artefact content does not transit or rest in the display layer.
4. **Confirmation-first is carried into the feed, not bypassed by it.** Every projected position carries its source, source date, Digital Lead confirmation status and freshness status. Positions that are `Pending confirmation`, `Stale`, `Revalidation due` or `Superseded` must be rendered as visibly flagged on the board itself, never as confirmed-current.
5. **The feed invents nothing.** Every value is either copied from a confirmed governed field or is a mechanical roll-up (for example an open-action count or a stage-cell state) of governed fields. No invented costs, benefits, risks, owners, dates, health ratings, or scores. Delivery health and priority are copied confirmed field values, not AI calculations.
6. **The feed is a controlled write-back, not an auto-update.** It is (re)generated at governed-session closeout under `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, proposed as a controlled update recommendation, and only written after Digital Lead approval. It is never silently mutated from ingested inputs.
7. **The display never authors a governed change.** Separation of duties is absolute: the **display requests**, the **AI Coworker authors** the change as a structured patch, the **Digital Lead confirms**, and the **executing layer applies the confirmed patch verbatim**. An executing layer that infers, interprets or composes a repository edit of its own has become an author and breaches this standard. See Section 7a.

## Ingestion note (uploaded / updated artefacts)

When the Digital Lead uploads or updates an artefact (for example revised meeting minutes), the governed flow is unchanged: the coworker proposes controlled updates to the Initiative Evidence and Decision File, PEP/control record and action position; the Digital Lead confirms; and only then is the feed regenerated so the display reflects the confirmed position. The display layer never ingests source artefacts or updates itself directly.

## Feed artefacts

Four artefacts make up the feed, all held in the bound private client repository:

| Artefact | Location (private client repo) | Nature | Renders |
|---|---|---|---|
| `spines.json` | client-repo root (or the path named in the client profile) | **configuration** — the client's board spines and `pep_type` templates (Section 5a.2) | the board columns |
| Initiative display front-matter | header block carried on each Initiative Evidence and Decision File | authored-with-record, confirmed values only | one Mieruka row |
| `portfolio.json` | client-repo root (or the path named in the client profile) | **generated** roll-up of all initiative front-matter for that client | the Mieruka boards |
| `actions.yaml` | client-repo root (or the path named in the client profile) | governed action projection / working action log | the action log |

`portfolio.json` is a generated projection (treat it like a build artefact): regenerated from the initiative records, never hand-authored as truth. Front-matter on each record is the per-initiative source of the display fields, so no separate per-initiative feed file is created and nothing is duplicated.

## Section 5 — Initiative display front-matter

Carried as a YAML front-matter block on the initiative's Initiative Evidence and Decision File. Every field maps to schema `13`. Values use the controlled labels in `00_system_control/CONTROLLED_VOCABULARY.md`; where the bound client profile provides actual controlled-system status names, those names are used instead (same rule as Approved Hopper Statuses).

```yaml
# --- display front-matter: projection of the Initiative Evidence and Decision File ---
initiative_id:        DEMO-001              # 13 §1 Identity
client_id:            DEMO-CLIENT           # 13 §1 Identity (integrity check; feed is single-client)
title:                Sample initiative     # 13 §1 Identity
route:                Development Route     # 13 §1 / controlled Route Labels
board:                live                  # Section 5a board registry (hopper / programme / live)
pep_type:             Fresh implementation  # Section 5b template registry (live board only)
macro_stage:          Delivery              # 13 §2 four-stage macro-stage
lifecycle_position:   In Delivery           # 13 §2 / Stage 3 Live Delivery Labels
current_gate:         Stage 1D              # 13 §2 current gate
gate_status:          Closed                # 13 §2 gate status
delivery_health:      Amber                 # 13 §6 confirmed field, copied not computed
priority:             High                  # 13 §1 / Business Priority Signal (High/Medium/Low/Unclear)
sponsor:              <name>                # 13 §4 Ownership
delivery_owner:       <name>                # 13 §4 Ownership
current_milestone:    <milestone>           # 13 §6 Delivery
target_finish:        2026-11-30            # 13 §6 Delivery
current_blockers:     <short text or none>  # 13 §6 Delivery
open_actions_count:   3                     # roll-up of actions.yaml for this initiative
linked_pep:           path/or/reference     # 13 §6 Linked PEP (pointer, not a copy)
stage_vector:                               # Section 5c — one entry per stage on the row's board
  - { stage: commercial,  state: complete,     needs_action: false }
  - { stage: discovery,   state: complete,     needs_action: false }
  - { stage: plan,        state: complete,     needs_action: false }
  - { stage: integrations,state: current,      needs_action: true, action_ref: DEMO-001-A1 }
  - { stage: uat_env,     state: not_started,  needs_action: false }
  - { stage: managed_svc, state: not_required, needs_action: false }
artefacts:                                  # 13 §7 evidence location (pointers only)
  - name:    Latest PEP
    type:    PEP
    ref:     path/or/link
    version: Rev3
    released: true
latest_source:        Digital Team Meeting Minutes 2026-09-12   # 13 §10a
source_date:          2026-09-12            # 13 §10a
confirmation_status:  Confirmed current     # 13 §10a (Confirmed current / Corrected by Digital Lead / Pending confirmation / Superseded / Not applicable)
last_confirmed_date:  2026-09-13            # 13 §10a
freshness:            Current               # 07 / 13 §10a (Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable)
feed_generated_at:    2026-09-16T00:00:00Z  # projection timestamp
```

**Rendering rule.** `delivery_health` and `priority` carry the confirmed field value verbatim; the display maps them to colour (for example Green/Amber/Red, High/Medium/Low). The mapping is a display concern only — the coworker never derives the underlying rating. Any row whose `confirmation_status` or `freshness` is not `Confirmed current` / `Current` must be shown with a visible flag.

## Section 5a — Board registry and stage spines

The Mieruka form is a **matrix**: initiatives down the left, stages across the top, one status cell per intersection. A board's **stage spine is fixed** so that every row on it is directly comparable — this is what makes the board scannable, and it is not varied per initiative.

Each initiative declares exactly one `board`. An initiative may move between boards as it progresses (Hopper → Programme → Live); it is never on two boards at once on the same feed generation.

| `board` | Rows | Stage spine (`stage` keys, in order) |
|---|---|---|
| `hopper` | pre-approval items | `intake`, `clarify`, `consolidated`, `priority_screen`, `drb`, `route_trigger` |
| `programme` | approved initiation forms (macro lifecycle) | `authorised`, `mobilising`, `in_delivery`, `go_live`, `adoption`, `operational` |
| `live` | initiatives in delivery (default reference spine, Section 5a.1) | `commercial`, `discovery`, `plan`, `integrations`, `uat_env`, `uat_signoff`, `production`, `go_live`, `hypercare`, `managed_svc` |

The `hopper` and `programme` spines are derived from `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` and the controlled Stage 3 labels, and are method-fixed.

The spine a display renders is always read from the client's `spines.json` (Section 5a.2), never hard-coded into the display. The table above is the method default that a client's configuration reproduces or, for `live`, may override.

### Section 5a.1 — The live delivery spine is a default, not a mandate

The `live` spine above is the **default reference delivery spine**. Where the bound client profile names a different delivery phase/milestone structure, that structure governs for that client. The client's own spine is declared in its `SOURCE_OF_TRUTH.md` as the governed statement of record, and expressed machine-readably in that client's `spines.json` (Section 5a.2) for the display to read. Where the two disagree, `SOURCE_OF_TRUTH.md` governs and the conflict is surfaced to the Digital Lead.

This standard does not impose a delivery methodology; it requires only that whatever spine a client uses is **fixed for the board**, declared, and machine-readable, so the matrix stays comparable.

Display labels and the milestone each stage represents (default spine):

| `stage` key | Column label | Milestone |
|---|---|---|
| `commercial` | Commercial | Contract signed and commercials agreed |
| `discovery` | Discovery | Requirements and scope signed off |
| `plan` | Plan | Project plan approved |
| `integrations` | Integrations | Key dependency — development |
| `uat_env` | UAT Env | UAT environment ready for testing |
| `uat_signoff` | UAT Sign-off | UAT sign-off |
| `production` | Production | Production ready |
| `go_live` | Go-Live | Go-Live |
| `hypercare` | Hypercare | Hypercare exit / transition to BAU |
| `managed_svc` | Managed Services | Managed services operating model agreed |

### Section 5a.2 — `spines.json` (the client's spine and template configuration)

`spines.json` is the canonical machine-readable configuration for one client's board columns and `pep_type` templates. It is **configuration, not a projection**: it is authored alongside the client's declared method position, changes rarely, and is not regenerated at closeout like `portfolio.json`.

```json
{
  "client_id": "DEMO-CLIENT",
  "boards": {
    "live": {
      "label": "Live Delivery",
      "stages": [
        { "stage": "commercial", "label": "Commercial", "milestone": "Contract signed and commercials agreed" }
      ]
    }
  },
  "pep_types": {
    "Fresh implementation": { "not_required": [] },
    "Support selection and due diligence": { "not_required": ["integrations", "uat_env"] }
  }
}
```

**Rules.**

- One `spines.json` per client, in that client's repository. It carries no other client's configuration.
- It must declare all three boards (`hopper`, `programme`, `live`). The `hopper` and `programme` spines reproduce the method-fixed spines in Section 5a; only `live` may differ.
- `stage` keys are the join between configuration and feed: every `stage_vector` entry's `stage` must exist in that board's declared spine, in spine order. A `stage_vector` that does not match its board's spine is a feed defect, not a display problem to work around.
- `label` and `milestone` are display strings only. Changing a label never changes a `stage` key; keys are stable identifiers.
- `pep_types` carries the machine-readable form of the Section 5b templates, including any additional template the client profile declares.
- Changing a spine or template is a controlled update requiring Digital Lead confirmation, and any initiative whose `stage_vector` no longer matches must be regenerated in the same controlled change.

## Section 5b — `pep_type` template registry

Initiatives on the `live` board differ in delivery shape. The spine stays fixed; the **`pep_type` template** declares which stages that shape actually uses. Stages a template does not use are projected as `not_required` — the black cell — so heterogeneous delivery types render on one consistent grid without widening it.

Method-default templates (client-agnostic; a client profile may declare additional templates). The machine-readable form of these templates, for the display to read, is the `pep_types` block of that client's `spines.json` (Section 5a.2):

| `pep_type` | Typical shape | Stages not used (default) |
|---|---|---|
| `Full migration and implementation` | migration of an existing platform plus new implementation | none |
| `Fresh implementation` | new implementation, no incoming migration | none by default |
| `Data migration into an existing platform` | data moved into a platform already live | `production`, `managed_svc` where the live platform and its service model already exist |
| `Support selection and due diligence` | assisted selection / digital due diligence; no build or deployment | `integrations`, `uat_env`, `uat_signoff`, `production`, `go_live`, `hypercare`, `managed_svc` |

**Rules.**

- A template sets the **default** `not_required` set. The confirmed position on the initiative record governs where it differs, and any difference is a recorded, confirmed decision — not a display-time guess.
- `not_required` means *out of scope for this delivery shape*. It never means skipped, deferred, or unevidenced. A stage that is in scope but not yet reached is `not_started`.
- The coworker does not reclassify an initiative's `pep_type`. Changing it is a controlled update requiring Digital Lead confirmation.
- The detailed PEP task set sits **beneath** each stage in the PEP / client-control record. It is never promoted into board columns and is never duplicated into the feed.

## Section 5c — `stage_vector` (the row of cells)

`stage_vector` carries one entry per stage on the row's board, in spine order. It is a **mechanical roll-up** of the governed position and the PEP tasks beneath each stage — not a judgement.

```yaml
stage_vector:
  - stage:        integrations      # must match a stage key in the row's board spine
    state:        current           # complete | current | not_started | not_required
    needs_action: true              # true where an open/overdue action or recorded blocker sits at this stage
    action_ref:   DEMO-001-A1       # optional; the action_id driving needs_action
```

**Cell state derivation.**

| `state` | Set when |
|---|---|
| `complete` | every PEP task beneath the stage is recorded complete, or the stage's milestone is evidenced as achieved |
| `current` | the stage is the initiative's current confirmed position on that board |
| `not_started` | the stage is in scope for the `pep_type` but not yet reached |
| `not_required` | the stage is outside the `pep_type` scope (Section 5b) |

**Rules.**

- Exactly one entry may be `current`, except where the confirmed position is between stages, in which case none is and `current_milestone` carries the position.
- `needs_action` is set **mechanically** — an open, overdue or blocked action recorded against the stage, or a recorded blocker. It is never an AI assessment of risk.
- `needs_action` drives the display's "needs progressing" list. Display colour on a `current` cell comes from `delivery_health` and `needs_action`; the display never computes the underlying health.
- A stage-cell state is never used to infer approval, funding, acceptance or go-live authority. Those remain governed fields under schema `13`.

## Section 6 — `portfolio.json` (the board feed)

A generated roll-up for one client. Structure:

```json
{
  "client_id": "DEMO-CLIENT",
  "feed_generated_at": "2026-09-16T00:00:00Z",
  "feed_source": "Initiative Evidence and Decision Files (schema 13); generated projection — not a source of truth",
  "spines_ref": "spines.json",
  "initiatives": [
    { "...": "one object per initiative, exactly the front-matter fields in Section 5" }
  ]
}
```

**Point-in-time, and where history lives.** `portfolio.json` is a point-in-time projection: it is regenerated and overwritten, and carries no time series. It must not be extended into one, and no history table or snapshot store may be created alongside it — that would be a second source. Where a trend view is needed (action burndown, time-in-stage, "what is stalled"), it is derived from the **version history of `portfolio.json` in the client repository itself**, which already preserves every prior generation. History is read from the repository, never accumulated in the feed or the display layer.

The display renders one matrix per `board`, rows filtered by `board`, columns from that board's spine, and one cell per `stage_vector` entry. It surfaces `current_blockers`, `open_actions_count`, `needs_action` cells, and flagged `confirmation_status` / `freshness`. `portfolio.json` contains exactly one client's initiatives; cross-client composition is display-time only.

## Section 7 — `actions.yaml` (the action log)

The action log projects the governed action position: `Open actions` and `Action-system references` (schema `13` §8 and §10a).

**Authority of actions.**
- Where the bound client profile names a client action-management system, that system is authority; `actions.yaml` mirrors it and any change is a `Recommended update — requires Digital Lead approval and physical update in the client system.`
- Where no external action system is named (for example the consultant's own action list), the Digital Lead's actions may be maintained as this controlled `actions.yaml` in the bound working authority, governed as a controlled record under the update-once rule.

Either way the feed invents no actions, owners, or due dates, and an action is marked complete only on Digital Lead confirmation.

```yaml
actions:
  - action_id:    DEMO-001-A1
    initiative_id: DEMO-001          # link/attach to an initiative; null for a standalone personal action
    stage:        integrations       # optional; the stage this action sits at (drives needs_action)
    description:  Confirm integration mapping with sponsor
    owner:        <name>
    due_date:     2026-09-20
    status:       Open               # Open / In progress / Blocked / Done / Cancelled
                                     # (display-layer set; overridden by the client action-system's own statuses where one is named)
    source:       Digital Team Meeting Minutes 2026-09-12
    outcome_note: null               # populated at closure (Section 7a)
    confirmation_status: Confirmed current
    created_at:   2026-09-12
    updated_at:   2026-09-13
```

## Section 7a — Action-closure write-back: the structured patch contract

This section defines the **only** write path from the display layer back into governed records, and the separation of duties that keeps it controlled (boundary 7).

**The four roles.**

| Role | Does | Must never |
|---|---|---|
| Display layer | emits a closure **request** | author, infer or compose a repository edit |
| AI Coworker | authors a **structured patch** against the governed records | apply the patch, or change a field outside the permitted target set |
| Digital Lead | **confirms** or rejects the patch | — |
| Executing layer | applies the confirmed patch **verbatim** | interpret prose, re-derive a change, or apply an unconfirmed patch |

### 7a.1 Closure request (display → AI Coworker)

```json
{
  "request_type": "action_closure",
  "client_id": "DEMO-CLIENT",
  "action_id": "DEMO-001-A1",
  "initiative_id": "DEMO-001",
  "closed_by": "<Digital Lead>",
  "closed_date": "2026-09-16",
  "outcome_note": "<what was actually done>",
  "feed_generated_at": "2026-09-16T00:00:00Z",
  "observed_revisions": {
    "actions.yaml": "<revision id observed by the display>",
    "initiatives/DEMO-001/EVIDENCE_AND_DECISION.md": "<revision id>"
  }
}
```

The request carries **no proposed edits** — only the fact of closure and what the display was looking at when it was raised.

### 7a.2 Authored patch (AI Coworker → Digital Lead, for confirmation)

```json
{
  "patch_version": "1.0",
  "request_type": "action_closure",
  "client_id": "DEMO-CLIENT",
  "authored_by": "<model identifier>",
  "authored_at": "2026-09-16T10:04:00Z",
  "summary": "Close DEMO-001-A1; mark integrations mapping task complete; log closure in the Evidence and Decision File.",
  "requires_confirmation": true,
  "atomic": true,
  "changes": [
    {
      "file": "actions.yaml",
      "expected_revision": "<revision id>",
      "op": "set_field",
      "target": "actions[action_id=DEMO-001-A1].status",
      "from": "Open",
      "to": "Done"
    },
    {
      "file": "actions.yaml",
      "expected_revision": "<revision id>",
      "op": "set_field",
      "target": "actions[action_id=DEMO-001-A1].outcome_note",
      "from": null,
      "to": "<what was actually done>"
    },
    {
      "file": "initiatives/DEMO-001/EVIDENCE_AND_DECISION.md",
      "expected_revision": "<revision id>",
      "op": "append_item",
      "target": "decision_log",
      "to": "2026-09-16 — DEMO-001-A1 closed by Digital Lead. <outcome note>."
    }
  ],
  "external_writebacks": [
    {
      "system": "<system named in the client profile>",
      "text": "<update text>",
      "status": "Recommended update — requires Digital Lead approval and physical update in the client system."
    }
  ]
}
```

### 7a.3 Rules

- **Allowlisted operations only:** `set_field`, `append_item`, `set_status`. Whole-file replacement is not a permitted operation — a patch can never rewrite a governed record wholesale.
- **Every change names** `file`, `expected_revision`, `target`, and (for `set_field`) both `from` and `to`. This makes the patch auditable and conflict-detectable.
- **Atomic:** all changes apply or none do.
- **Conflict handling:** if any `expected_revision` no longer matches, the whole patch is abandoned, the request is re-authored against the current records, and the Digital Lead is asked again. Never force, never overwrite a newer revision. This is the case where the Digital Lead has edited the records directly in a governed session while a patch was pending.
- **Confirm-first is the default.** A patch applies only on explicit Digital Lead confirmation. A client may be switched to auto-apply for `action_closure` only, by explicit Digital Lead instruction recorded in that client's profile; external write-backs remain recommendations regardless.
- **Confirmation fields move with the change.** Any field a patch alters has its `confirmation_status` and `last_confirmed_date` updated to reflect the confirmation event.
- **The feed is regenerated after apply**, so the display re-projects the new confirmed position. The display does not patch its own cache into agreement.
- **Only this contract is a permitted path to a governed change.** A display platform's own built-in model or in-app AI feature (an `InvokeLLM`-style convenience call) is not an AI Coworker under this standard: it does not author against the loaded authority files and does not return a validated patch. It may be used for non-governed convenience only — never to originate, approve or apply a change to a governed record.

### 7a.4 Permitted target sets

A request type may only touch its permitted targets. Anything else is a boundary breach and is rejected, not negotiated.

| `request_type` | Permitted targets | Always prohibited |
|---|---|---|
| `action_closure` | the action's `status`, `outcome_note`, `updated_at`; the initiative's `open_actions_count` and the affected `stage_vector` entry; the PEP task/phase status beneath that stage; the Evidence and Decision File decision/action log | `route`, `pep_type`, approval basis, entry basis, decision outcome, funding/capex position, scope, exclusions, `delivery_health`, `priority`, acceptance or go-live authority, any other initiative, any other client |
| `artefact_refresh` | `lifecycle_position`, `current_gate`/`gate_status`, `current_milestone`, `target_finish`, `current_blockers`, `stage_vector`, new/updated `actions[]`, `latest_source`, `source_date` | as above, plus: creating an approval, acceptance or go-live position that is not evidenced in the supplied artefact |

Closing an action never changes delivery health, priority, route or any approval position. Those are confirmed Digital Lead / decision-body fields under schema `13` and move only through their own governed control.

## Section 8 — Read and write integration (non-authoritative)

Implementation guidance for the display layer. It sets no governance and may be adapted to the chosen tool.

- **Read:** the display reads `portfolio.json` and `actions.yaml` from the bound private client repository (for example via the repository's API at page load, or a build step), and follows `artefacts[].ref` / `linked_pep` pointers to open the latest PEP and other outputs. It reads; it does not hold authority.
- **Cache:** optional, and only under boundary 3 — partitioned per client, showing a visible last-synced position, manually re-syncable, and fully rebuildable from the repository. A cache is disposable; a stale cache is a display defect, never a new position.
- **Refresh:** a repository push may notify the display to refresh; otherwise the display re-reads on load. "Visually driven by file updates" means the display re-projects whatever the confirmed records now say.
- **Write:** limited to emitting the Section 7a closure request. The display never commits. Credentials for the executing layer stay server-side and are scoped to the minimum needed for the bound client's repository.
- **Degradation:** the display must render fully in read-only mode when the AI Coworker layer is unavailable. Only the write-back is disabled; status remains visible.
- **Multi-client desktop:** the app is configured with each separately-bound client repository and composes the cross-client view in the browser. No combined multi-client file is ever written.

## Field mapping summary

| Feed field | Schema `13` source |
|---|---|
| `initiative_id`, `client_id`, `title`, `route`, `priority` | §1 Identity |
| `board`, `macro_stage`, `lifecycle_position`, `current_gate`, `gate_status` | §2 Lifecycle |
| `sponsor`, `delivery_owner` | §4 Ownership |
| `pep_type`, `delivery_health`, `current_milestone`, `target_finish`, `current_blockers`, `linked_pep` | §6 Delivery (delivery model / plan reference) |
| `stage_vector` | §6 Delivery (current milestone, blockers) + §7 Evidence, rolled up per stage |
| `artefacts[]` | §7 Evidence (evidence location, pointers only) |
| `actions[]`, `open_actions_count` | §8 Decisions and obligations; §10a action-system references |
| `latest_source`, `source_date`, `confirmation_status`, `last_confirmed_date`, `freshness` | §10a Confirmation, freshness and physical write-back |

## Worked example — synthetic, illustrative only

Not a client record. IDs are deliberately fictitious. This shows the shape only and must never be populated with client data in this public method repository. Stage vectors are abbreviated to the stages that carry meaning in each case.

```json
{
  "client_id": "DEMO-CLIENT",
  "feed_generated_at": "2026-09-16T00:00:00Z",
  "feed_source": "Initiative Evidence and Decision Files (schema 13); generated projection — not a source of truth",
  "initiatives": [
    {
      "initiative_id": "DEMO-001",
      "client_id": "DEMO-CLIENT",
      "title": "Sample fresh implementation",
      "route": "Implementation Route",
      "board": "live",
      "pep_type": "Fresh implementation",
      "macro_stage": "Delivery",
      "lifecycle_position": "In Delivery",
      "delivery_health": "Amber",
      "priority": "High",
      "current_milestone": "Integration build",
      "target_finish": "2026-11-30",
      "current_blockers": "Integration mapping unconfirmed",
      "open_actions_count": 1,
      "linked_pep": "initiatives/DEMO-001/PEP_Rev3",
      "stage_vector": [
        { "stage": "commercial",   "state": "complete",     "needs_action": false },
        { "stage": "discovery",    "state": "complete",     "needs_action": false },
        { "stage": "plan",         "state": "complete",     "needs_action": false },
        { "stage": "integrations", "state": "current",      "needs_action": true, "action_ref": "DEMO-001-A1" },
        { "stage": "uat_env",      "state": "not_started",  "needs_action": false },
        { "stage": "uat_signoff",  "state": "not_started",  "needs_action": false },
        { "stage": "production",   "state": "not_started",  "needs_action": false },
        { "stage": "go_live",      "state": "not_started",  "needs_action": false },
        { "stage": "hypercare",    "state": "not_started",  "needs_action": false },
        { "stage": "managed_svc",  "state": "not_started",  "needs_action": false }
      ],
      "latest_source": "Digital Team Meeting Minutes 2026-09-12",
      "source_date": "2026-09-12",
      "confirmation_status": "Confirmed current",
      "last_confirmed_date": "2026-09-13",
      "freshness": "Current"
    },
    {
      "initiative_id": "DEMO-002",
      "client_id": "DEMO-CLIENT",
      "title": "Sample selection and due diligence",
      "route": "Support Route",
      "board": "live",
      "pep_type": "Support selection and due diligence",
      "macro_stage": "Delivery",
      "lifecycle_position": "In Delivery",
      "delivery_health": "Green",
      "priority": "Medium",
      "current_milestone": "Requirements gathering",
      "target_finish": "2026-10-15",
      "current_blockers": "none",
      "open_actions_count": 0,
      "linked_pep": null,
      "stage_vector": [
        { "stage": "commercial",   "state": "complete",     "needs_action": false },
        { "stage": "discovery",    "state": "current",      "needs_action": false },
        { "stage": "plan",         "state": "not_started",  "needs_action": false },
        { "stage": "integrations", "state": "not_required", "needs_action": false },
        { "stage": "uat_env",      "state": "not_required", "needs_action": false },
        { "stage": "uat_signoff",  "state": "not_required", "needs_action": false },
        { "stage": "production",   "state": "not_required", "needs_action": false },
        { "stage": "go_live",      "state": "not_required", "needs_action": false },
        { "stage": "hypercare",    "state": "not_required", "needs_action": false },
        { "stage": "managed_svc",  "state": "not_required", "needs_action": false }
      ],
      "latest_source": "Due diligence working note 2026-09-11",
      "source_date": "2026-09-11",
      "confirmation_status": "Confirmed current",
      "last_confirmed_date": "2026-09-11",
      "freshness": "Current"
    },
    {
      "initiative_id": "DEMO-003",
      "client_id": "DEMO-CLIENT",
      "title": "Sample hopper item",
      "route": "TBC",
      "board": "hopper",
      "macro_stage": "Intake",
      "lifecycle_position": "Ready for Priority Screen",
      "delivery_health": "Not applicable",
      "priority": "Unclear",
      "current_milestone": "Awaiting DRB priority discussion",
      "target_finish": null,
      "current_blockers": "none",
      "open_actions_count": 1,
      "linked_pep": null,
      "stage_vector": [
        { "stage": "intake",         "state": "complete",    "needs_action": false },
        { "stage": "clarify",        "state": "complete",    "needs_action": false },
        { "stage": "consolidated",   "state": "complete",    "needs_action": false },
        { "stage": "priority_screen","state": "current",     "needs_action": true, "action_ref": "DEMO-003-A1" },
        { "stage": "drb",            "state": "not_started", "needs_action": false },
        { "stage": "route_trigger",  "state": "not_started", "needs_action": false }
      ],
      "latest_source": "Hopper consolidation 2026-09-08",
      "source_date": "2026-09-08",
      "confirmation_status": "Pending confirmation",
      "last_confirmed_date": null,
      "freshness": "Pending confirmation"
    }
  ]
}
```

Rendered: `DEMO-001` shows green through Plan, an amber **current** cell at Integrations badged for action, and not-started cells beyond. `DEMO-002` shows the `pep_type` mechanism — complete/current through Discovery, then **not required** (black) across every build and deployment stage, because selection and due diligence does not use them. `DEMO-003` sits on the Hopper board at Priority Screen and is **visibly flagged `Pending confirmation`**, because an unconfirmed position must never be shown as current.

## Boundary

This standard adds no AI approval authority, no numeric confidence or maturity scoring, and no new source of truth. The feed is a read projection plus a single governed action write-back under the Section 7a patch contract. The display requests, the AI Coworker authors, the Digital Lead confirms, and the executing layer applies verbatim; no other party authors a governed change. Controlled record changes require Digital Lead approval; external system and publication write-backs remain recommendations until completion is evidenced. Client isolation under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` is absolute: one client per feed, one client per cache partition, composition across clients at display time only.
