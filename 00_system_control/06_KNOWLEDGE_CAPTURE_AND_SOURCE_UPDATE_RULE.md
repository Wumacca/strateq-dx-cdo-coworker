# Knowledge Capture and Source Update Rule

## Purpose

This file defines how durable facts, decisions, and technical constraints discovered during governed sessions are identified, routed, and stored in controlled source-of-truth locations.

Claude must not leave durable knowledge only in chat. Chat is ephemeral. Controlled files, Jira, and SharePoint are the governed record.

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
| Operating rule or governance process change | GitHub repository file (most specific governing file) |
| Initiative-specific field, scope, decision, or assumption | Initiative Evidence and Decision File first, then the Jira initiative field or Jira comment write-back |
| Action / task status | Initiative Evidence and Decision File reference, then the Omega 365 write-back (Omega 365 is the action-management system) |
| Process flow, RACI, bottleneck, or future-state requirement | Process mapping artefact (SharePoint or agreed file location) |
| System, integration, or technical constraint | System specification or technical artefact (SharePoint or agreed file location) |
| Source-of-truth artefact impact | Source-of-truth impact register or artefact update record |
| Programme-level decision, risk, or governance outcome | SharePoint programme governance record or decision register |
| Lessons learned or governance improvement | SharePoint lessons learned register (Digital Governance & Strategy control function) |

## Knowledge Capture Review

At the end of each governed session or thread, Claude must run a Knowledge Capture Review.

The review must:

1. Identify any durable facts, decisions, technical constraints, system behaviours, role permissions, integration details, file-size rules, assumptions, or governance decisions that emerged during the session.
2. For each item identified, propose the target controlled location using the routing table above.
3. Present the proposed captures to the Digital Lead for approval before updating any file.
4. Not silently update repository files, Jira, or SharePoint without Digital Lead approval.

Claude must propose; the Digital Lead decides.

## Knowledge Capture Review Format

At the end of a session, Claude must state:

**Knowledge Capture Review**

| # | Knowledge item | Proposed target location | Action required |
|---|---|---|---|

If no durable knowledge items are identified, Claude must state: "No durable knowledge items identified for capture in this session."

## Example

Knowledge item discovered during a session:

> "Chronos Goods Received attachments use Amazon S3 storage; no artificial application file-size limit is currently specified beyond Amazon S3 limits."

This is a confirmed technical constraint.

Proposed routing:

- Target: Chronos / Goods Receipting system specification or technical artefact stored in SharePoint (or agreed controlled file location).
- Do not leave only in chat.
- Do not add to a generic operating rule file unless it has programme-wide applicability.

## Relationship to Governed Workflow Looping

This file remains authoritative for knowledge capture and source-of-truth update routing.

In a material governed session, the Knowledge Capture Review runs as a component of the stage closeout / handover under `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, alongside the CDO QA / Self-Improvement Check and Source-of-Truth Update Recommendations. All three are advisory only. None of them update workflow files, source-of-truth artefacts, Jira, SharePoint, or repository files without Digital Lead approval of a controlled update.

## Update-Once and Reporting

A confirmed update received in any initiative, bi-weekly, or monthly session must first be reconciled into the affected Initiative Evidence and Decision File before any report is generated, per `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`. Knowledge captured during a bi-weekly or monthly reporting session must be routed to the affected initiative evidence files first; it must not remain only in the reporting thread or a report.

No material fact may remain only in a chat, a reporting thread, a previous report, an input template, Claude Project knowledge, or assistant memory. Reports are controlled outputs and snapshots, not parallel sources of truth, and must not become the newest unrecorded source of initiative status.

Required Jira, SharePoint, and Omega 365 physical write-backs are prepared as recommendations labelled `Recommended update — requires Digital Lead approval and physical update in the client system.` Claude has no live connection to those systems and must never claim a client-system update has occurred; a write-back is complete only when the Digital Lead explicitly confirms the physical update.

## Boundary Rule

Claude must not update controlled source-of-truth files without Digital Lead approval.

Claude must not treat chat confirmation alone as sufficient authority to update a repository file, Initiative Evidence and Decision File, Jira field, SharePoint artefact, or Omega 365 action.

Knowledge capture proposals are outputs for Digital Lead action, not self-authorised updates.
