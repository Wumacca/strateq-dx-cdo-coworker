# Mieruka and Action Display Feed Standard

## Status

Reusable, client-agnostic **specification** for the machine-readable projection that a read-only display layer (for example a Base44-class personal cockpit, a static dashboard, or any Mieruka board) consumes to render live initiative status, the action log, and pointers to the latest artefacts (PEP, Initiation Form, process pack, reports).

This file is a specification only. It defines the shape of the feed, not any client's data. No populated feed is ever committed to this public method repository.

The feed is a **derived display projection**, not a record of authority. It is regenerated from the single AI-readable per-initiative continuity record — the **Initiative Evidence and Decision File** (`02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`, implementing schema `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`). It adds no facts, holds no authority, and is never itself an AI-readable continuity record. Where this standard and any authority file conflict, the authority file governs and the conflict is surfaced to the Digital Lead.

## Purpose

Give the Digital Lead a single visual cockpit — portfolio Mieruka, action management, and latest-artefact access — driven entirely by the governed files, without introducing a second source of truth.

- **Display reads** the feed to render status. It does not compute or invent status.
- **The display owns nothing.** The feed is generated from confirmed governed records; the governed records remain the source.
- **The only write path** is the governed action write-back defined in Section 7, which routes back through the update-once rule and Digital Lead confirmation.

## First-principle boundaries (read before use)

1. **No second source of truth.** The feed never becomes a parallel initiative record, action register, or programme-memory ledger. It is a projection of the Initiative Evidence and Decision File and the governed action position. Schema `13` permits exactly one AI-readable per-initiative record; this standard does not create another.
2. **The feed lives in the bound private client repository**, alongside the live records it projects — never in this public method repository, and never in a location that mixes clients.
3. **One client per feed.** Under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` there is no stored file that aggregates more than one client. A consultant's multi-client "desktop" view is composed **at display time** by the app reading each separately-bound client repository's own feed; it is never a combined file written into any repository.
4. **Confirmation-first is carried into the feed, not bypassed by it.** Every projected position carries its source, source date, Digital Lead confirmation status and freshness status. Positions that are `Pending confirmation`, `Stale`, `Revalidation due` or `Superseded` must be rendered as visibly flagged, never as confirmed-current.
5. **The feed invents nothing.** Every value is either copied from a confirmed governed field or is a mechanical roll-up (for example an open-action count) of governed fields. No invented costs, benefits, risks, owners, dates, health ratings, or scores. Delivery health and priority are copied confirmed field values, not AI calculations.
6. **The feed is a controlled write-back, not an auto-update.** It is (re)generated at governed-session closeout under `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, proposed as a controlled update recommendation, and only written after Digital Lead approval. It is never silently mutated from ingested inputs.

## Ingestion note (uploaded / updated artefacts)

When the Digital Lead uploads or updates an artefact (for example revised meeting minutes), the governed flow is unchanged: the coworker proposes controlled updates to the Initiative Evidence and Decision File, PEP/control record and action position; the Digital Lead confirms; and only then is the feed regenerated so the display reflects the confirmed position. The display layer never ingests source artefacts or updates itself directly.

## Feed artefacts

Three artefacts make up the feed, all held in the bound private client repository:

| Artefact | Location (private client repo) | Nature | Renders |
|---|---|---|---|
| Initiative display front-matter | header block carried on each Initiative Evidence and Decision File | authored-with-record, confirmed values only | one Mieruka tile |
| `portfolio.json` | client-repo root (or the path named in the client profile) | **generated** roll-up of all initiative front-matter for that client | the Mieruka board |
| `actions.yaml` | client-repo root (or the path named in the client profile) | governed action projection / working action log | the action log |

`portfolio.json` is a generated projection (treat it like a build artefact): regenerated from the initiative records, never hand-authored as truth. Front-matter on each record is the per-initiative source of the display fields, so no separate per-initiative feed file is created and nothing is duplicated.

## Section 5 — Initiative display front-matter

Carried as a YAML front-matter block on the initiative's Initiative Evidence and Decision File. Every field maps to schema `13`. Values use the controlled labels in `00_system_control/CONTROLLED_VOCABULARY.md`; where the bound client profile provides actual controlled-system status names, those names are used instead (same rule as Approved Hopper Statuses).

```yaml
# --- display front-matter: projection of the Initiative Evidence and Decision File ---
initiative_id:        DEMO-001              # 13 §1 Identity
client_id:            DEMO-CLIENT           # 13 §1 Identity (integrity check; feed is single-client)
title:                Sample initiative     # 13 §1 Identity
route:                Development Route      # 13 §1 / controlled Route Labels
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
artefacts:                                  # 13 §7 evidence location (pointers only)
  - name:    Latest PEP
    type:    PEP
    ref:     path/or/link
    version: Rev3
    released: true
  - name:    Completed Initiation Form
    type:    Initiation Form
    ref:     path/or/link
    version: Rev1
    released: true
latest_source:        Digital Team Meeting Minutes 2026-09-12   # 13 §10a
source_date:          2026-09-12            # 13 §10a
confirmation_status:  Confirmed current     # 13 §10a (Confirmed current / Corrected by Digital Lead / Pending confirmation / Superseded / Not applicable)
last_confirmed_date:  2026-09-13            # 13 §10a
freshness:            Current               # 07 / 13 §10a (Current / Revalidation due / Stale / Superseded / Pending confirmation / Not applicable)
feed_generated_at:    2026-09-16T00:00:00Z  # projection timestamp
```

**Rendering rule.** `delivery_health` and `priority` carry the confirmed field value verbatim; the display maps them to colour (for example Green/Amber/Red, High/Medium/Low). The mapping is a display concern only — the coworker never derives the underlying rating. Any tile whose `confirmation_status` or `freshness` is not `Confirmed current` / `Current` must be shown with a visible flag.

## Section 6 — `portfolio.json` (the Mieruka board feed)

A generated roll-up for one client. Structure:

```json
{
  "client_id": "DEMO-CLIENT",
  "feed_generated_at": "2026-09-16T00:00:00Z",
  "feed_source": "Initiative Evidence and Decision Files (schema 13); generated projection — not a source of truth",
  "initiatives": [
    { "...": "one object per initiative, exactly the front-matter fields in Section 5" }
  ]
}
```

The display groups tiles by `macro_stage` or `lifecycle_position` for the Mieruka Kanban, colours by `delivery_health`, and surfaces `current_blockers`, `open_actions_count`, and flagged `confirmation_status` / `freshness`. `portfolio.json` contains exactly one client's initiatives; cross-client composition is display-time only.

## Section 7 — `actions.yaml` (action log and write-back)

The action log projects the governed action position: `Open actions` and `Action-system references` (schema `13` §8 and §10a).

**Authority of actions.**
- Where the bound client profile names a client action-management system, that system is authority; `actions.yaml` mirrors it and any change is a `Recommended update — requires Digital Lead approval and physical update in the client system.`
- Where no external action system is named (for example the consultant's own action list), the Digital Lead's actions may be maintained as this controlled `actions.yaml` in the bound working authority, governed as a controlled record under the update-once rule.

Either way the feed invents no actions, owners, or due dates, and an action is marked complete only on Digital Lead confirmation.

```yaml
actions:
  - action_id:    DEMO-001-A1
    initiative_id: DEMO-001          # link/attach to an initiative; null for a standalone personal action
    description:   Confirm PEP Rev3 scope with sponsor
    owner:         <name>
    due_date:      2026-09-20
    status:        Open              # Open / In progress / Blocked / Done / Cancelled
                                     # (display-layer set; overridden by the client action-system's own statuses where one is named)
    source:        Digital Team Meeting Minutes 2026-09-12
    confirmation_status: Confirmed current
    created_at:    2026-09-12
    updated_at:    2026-09-13
```

**Write-back path.** The display may propose action changes (tick complete, add, re-attach to an initiative). A proposed change is committed back to `actions.yaml` in the bound private client repository as a **controlled write-back** (an authenticated commit), then reconciled per the update-once rule into the affected Initiative Evidence and Decision File. It does not alter any other governed field, and where an external action system is authority it remains a recommendation until the physical update is evidenced.

## Section 8 — Read and write integration (non-authoritative)

Implementation guidance for the display layer. It sets no governance and may be adapted to the chosen tool.

- **Read:** the display reads `portfolio.json` and `actions.yaml` from the bound private client repository (for example via the repository's API at page load, or a build step), and follows `artefacts[].ref` / `linked_pep` pointers to open the latest PEP and other outputs. It reads; it does not hold authority.
- **Refresh:** a repository push may notify the display to refresh; otherwise the display re-reads on load. "Visually driven by file updates" means the display re-projects whatever the confirmed records now say.
- **Write:** limited to the Section 7 action write-back, performed as an authenticated commit back to the client repository. Credentials stay server-side; no other write path exists.
- **Multi-client desktop:** the app is configured with each separately-bound client repository and composes the cross-client view in the browser. No combined multi-client file is ever written.

## Field mapping summary

| Feed field | Schema `13` source |
|---|---|
| `initiative_id`, `client_id`, `title`, `route`, `priority` | §1 Identity |
| `macro_stage`, `lifecycle_position`, `current_gate`, `gate_status` | §2 Lifecycle |
| `sponsor`, `delivery_owner` | §4 Ownership |
| `delivery_health`, `current_milestone`, `target_finish`, `current_blockers`, `linked_pep` | §6 Delivery |
| `artefacts[]` | §7 Evidence (evidence location, pointers only) |
| `actions[]`, `open_actions_count` | §8 Decisions and obligations; §10a action-system references |
| `latest_source`, `source_date`, `confirmation_status`, `last_confirmed_date`, `freshness` | §10a Confirmation, freshness and physical write-back |

## Worked example — synthetic, illustrative only

The block below is **not a client record**. IDs are deliberately fictitious (`DEMO-CLIENT`, `DEMO-001`). It exists only to show the shape of a rendered feed and must never be populated with client data in this public method repository.

```json
{
  "client_id": "DEMO-CLIENT",
  "feed_generated_at": "2026-09-16T00:00:00Z",
  "feed_source": "Initiative Evidence and Decision Files (schema 13); generated projection — not a source of truth",
  "initiatives": [
    {
      "initiative_id": "DEMO-001",
      "client_id": "DEMO-CLIENT",
      "title": "Sample delivery initiative",
      "route": "Development Route",
      "macro_stage": "Delivery",
      "lifecycle_position": "In Delivery",
      "current_gate": "Stage 1D",
      "gate_status": "Closed",
      "delivery_health": "Amber",
      "priority": "High",
      "sponsor": "<name>",
      "delivery_owner": "<name>",
      "current_milestone": "Build increment 2",
      "target_finish": "2026-11-30",
      "current_blockers": "Awaiting sponsor sign-off on scope Rev3",
      "open_actions_count": 2,
      "linked_pep": "initiatives/DEMO-001/PEP_Rev3",
      "artefacts": [
        { "name": "Latest PEP", "type": "PEP", "ref": "initiatives/DEMO-001/PEP_Rev3", "version": "Rev3", "released": true }
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
      "title": "Sample implementation initiative",
      "route": "Implementation Route",
      "macro_stage": "Initiation",
      "lifecycle_position": "Initiation Form In Progress",
      "current_gate": "Stage 1",
      "gate_status": "In progress",
      "delivery_health": "Green",
      "priority": "Medium",
      "sponsor": "<name>",
      "delivery_owner": "<name>",
      "current_milestone": "Initiation Form drafting",
      "target_finish": "2026-10-15",
      "current_blockers": "none",
      "open_actions_count": 1,
      "linked_pep": null,
      "artefacts": [],
      "latest_source": "Initiation Form draft v0.3",
      "source_date": "2026-09-10",
      "confirmation_status": "Pending confirmation",
      "last_confirmed_date": null,
      "freshness": "Pending confirmation"
    }
  ]
}
```

In this example the display would render `DEMO-001` as an Amber, high-priority tile in the Delivery column with a blocker and two open actions, and `DEMO-002` as a Green tile in the Initiation column **visibly flagged as `Pending confirmation`** — because an unconfirmed position must never be shown as current.

## Boundary

This standard adds no AI approval authority, no numeric confidence or maturity scoring, and no new source of truth. The feed is a read projection plus a single governed action write-back. Controlled record changes require Digital Lead approval; external system and publication write-backs remain recommendations until completion is evidenced. Client isolation under `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` is absolute: one client per feed, composition across clients at display time only.
