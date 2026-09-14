# Knowledge Capture and Source Update Rule

## Purpose

This file defines how durable facts, decisions, and technical constraints discovered during governed sessions are identified, routed, and stored in controlled source-of-truth locations.

The Coworker must not leave durable knowledge only in chat. Chat is ephemeral. The governed record spans distinct roles selected in the bound client profile:

- **Initiative Evidence and Decision File** — the AI-readable per-initiative continuity record;
- **PEP / client-control record** — the client-side delivery hierarchy and reporting inputs where selected;
- **private client working authority** — the governed live records, working evidence indexes and released artefacts;
- **external client systems** — publication, execution or action systems named in the client profile.

Technical availability is not authority. The Coworker may read or write only the sources allowlisted by the current client binding. External publication remains manual unless the client profile explicitly authorises a governed integration.

## What Counts as Durable Knowledge

Durable knowledge includes:

- confirmed technical constraints or system behaviours
- confirmed integration details or API behaviours
- confirmed file-size limits, storage rules, or platform constraints
- confirmed role permissions or access boundaries
- confirmed process decisions or agreed scope boundaries
- confirmed assumptions elevated to facts by a subject matter expert, developer, or vendor
- governance decisions made by DRB, Digital Lead, or leadership
- risk acceptances or risk deferrals
- agreed scope inclusions or exclusions
- confirmed supplier or developer commitments
- artefact version decisions (superseded / active)

## What Does Not Count as Durable Knowledge

The following do not require knowledge capture routing:

- general background information widely available from public sources
- working hypotheses not yet confirmed
- questions still open and unanswered
- formatting preferences or session-specific instructions
- intermediate drafts not yet agreed

## Knowledge Routing Rules

Each durable knowledge item must be routed to the most appropriate controlled location:

| Knowledge type | Controlled location |
|---|---|
| Reusable operating rule or governance-process change | Public method repository, in the most specific governing file, only after client facts are removed |
| Client-specific operating rule or context | Bound private client repository |
| Initiative-specific field, scope, decision or assumption | Initiative Evidence and Decision File first, then the PEP / client-control record and any required external write-back |
| Action / task status | Initiative Evidence and Decision File reference, then the action system named in the client profile where applicable |
| Process flow, RACI, bottleneck or future-state requirement | Process artefact in the bound client working authority; publish externally only where required |
| System, integration or technical constraint | Client technical artefact in the bound client working authority |
| Source-of-truth artefact impact | Source-of-truth impact register or artefact update record |
| Programme-level decision, risk or governance outcome | Bound client programme governance record or decision register |
| Client lesson learned | Bound private client repository; propose only a sanitised reusable method change to the public repository |

## Knowledge Capture Review

At the end of each governed session or thread, the Coworker must run a Knowledge Capture Review.

The review must:

1. Identify any durable facts, decisions, technical constraints, system behaviours, role permissions, integration details, file-size rules, assumptions, or governance decisions that emerged during the session.
2. For each item identified, propose the target controlled location using the routing table above.
3. Present the proposed captures to the Digital Lead for approval before updating any file.
4. Not silently update governed records or external client systems without Digital Lead approval.

The Coworker proposes; the Digital Lead decides.

## Knowledge Capture Review Format

At the end of a session, Claude must state:

**Knowledge Capture Review**

| # | Knowledge item | Proposed target location | Action required |
|---|---|---|---|

If no durable knowledge items are identified, Claude must state: "No durable knowledge items identified for capture in this session."

## Example

Knowledge item discovered during a session:

> "The approved solution specification confirms that attachments use the selected object-storage service and records the applicable file-size control."

This is a confirmed technical constraint.

Proposed routing:

- Target: the initiative's solution specification or technical artefact in the bound client working authority; publish externally where the client profile requires it.
- Do not leave only in chat.
- Do not add to a generic operating rule file unless it has programme-wide applicability.

## Relationship to Governed Workflow Looping

This file remains authoritative for knowledge capture and source-of-truth update routing.

In a material governed session, the Knowledge Capture Review runs as a component of the stage closeout / handover under `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, alongside the CDO QA / Self-Improvement Check and Source-of-Truth Update Recommendations. All three are advisory only. None of them authorises a controlled update without Digital Lead approval.

## Update-Once and Reporting

A confirmed update received in any initiative, bi-weekly, or monthly session must first be reconciled into the affected Initiative Evidence and Decision File before any report is generated, per `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. Knowledge captured during a bi-weekly or monthly reporting session must be routed to the affected initiative evidence files first; it must not remain only in the reporting thread or a report.

No material fact may remain only in a chat, a reporting thread, a previous report, an input template, AI-workspace knowledge or assistant memory. Reports are controlled outputs and snapshots, not parallel sources of truth, and must not become the newest unrecorded source of initiative status.

Required external physical write-backs are prepared as recommendations labelled `Recommended update — requires Digital Lead approval and physical update in the client system.` A write-back is complete only when the Digital Lead explicitly confirms it occurred or an approved integration provides verifiable evidence.

## Confirmation versus file-update approval

Digital Lead confirmation and controlled-file update approval are distinct:

- Digital Lead confirmation **establishes or corrects the current business position** (the confirmation-first status rule). It does not, by itself, apply any file update.
- A proposed controlled file update — including an update to the Initiative Evidence and Decision File or a reusable GitHub authority file — is applied **only when the Digital Lead explicitly approves that update or explicitly instructs Claude to make it**.
- Confirmation of a status position does **not** prove that an external client system was physically updated; the write-back is complete only when the Digital Lead, an authorised user or an approved integration provides evidence.
- The Coworker may maintain the Initiative Evidence and Decision File and PEP/control record only inside the allowlisted client working authority. External client-system mutation remains a Digital Lead or authorised-user action unless expressly governed otherwise.

## Boundary Rule

The Coworker must not update controlled source-of-truth files without Digital Lead approval.

The Coworker must not treat chat confirmation of a status position as sufficient authority to apply a controlled file update or claim an external client-system update occurred.

Knowledge capture proposals are outputs for Digital Lead action, not self-authorised updates.
