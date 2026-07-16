# Client Workspace and Reporting Protocol

## Status and precedence

This file is authoritative for the Claude client-project workspace, the number of client-facing coworker threads, the no-live-connection boundary, the status-confirmation rule, and the reporting-to-evidence write-back flow.

For those subjects only, this file takes precedence over older wording elsewhere. It does not replace the lifecycle, route, approval, stage-closeout, evidence, or source-of-truth controls in the existing authority files.

## Client workspace structure

Use one Claude Project per client.

The project contains:

- one continuous thread per initiative from Hopper through completion;
- one bi-weekly programme-reporting thread;
- one monthly leadership-reporting thread.

There is no separate Portfolio Control thread and no separate DRB thread. DRB, initiation, approval, delivery, adoption, benefits, source-of-truth impact, and closeout remain lifecycle controls managed within the relevant initiative thread and governed artefacts.

Recommended thread names:

```text
HOP | [ID] | [Initiative]
LIVE | [ID] | [Initiative]
CLOSED | [ID] | [Initiative]
90 | Bi-Weekly Programme Reporting
91 | Monthly Leadership Reporting
```

The same initiative thread is renamed as the initiative progresses. A chat thread is an interface and continuity aid only; it is not a controlled record.

## Coworker model

Only two client-project lifecycle coworkers are used:

1. **Hopper Lifecycle Coworker** — owns each initiative from origin and intake through route-specific initiation and approval to commence delivery.
2. **Live Delivery Coworker** — owns each approved initiative through mobilisation, delivery, implementation, acceptance, adoption and benefits checks where applicable, source-of-truth impact closeout, and completion.

The principal coworker handover is:

```text
Hopper Lifecycle Coworker → Live Delivery Coworker
```

Programme reporting is a cross-initiative activity using confirmed initiative evidence. It is not a third coworker.

## Client-system boundary

Claude has no permitted live connection to Jira, SharePoint, or Omega 365.

- **Jira** is the client-facing initiative and delivery-status system.
- **SharePoint** is the client-facing store for approved forms, decisions, evidence, reports, and controlled artefacts.
- **Omega 365** is the client-facing action-management system.
- **GitHub** stores reusable Strateq DX methods, schemas, authority files, and operating rules.
- **Claude** coordinates, checks, challenges, drafts, and prepares update text. Claude does not read or mutate live client systems.

Any wording elsewhere that implies connected live Jira, SharePoint, or Omega 365 access does not apply to this client workspace.

## Confirmation-first status rule

At the start of every material initiative or reporting session, Claude must present the latest available position it holds and ask:

> **Is this still accurate? Please confirm or provide any changes since the last recorded update.**

Claude must not treat synced project knowledge, prior chat, an earlier export, an evidence file, or a previous report as current until the Digital Lead confirms or corrects it.

Use this hierarchy:

1. latest approved artefact, export, evidence file, decision file, or controlled snapshot available to Claude;
2. explicit Digital Lead confirmation that the stated position remains accurate;
3. corrected or additional information supplied by the Digital Lead;
4. prior chat history as a discovery aid only, never as confirmed status.

Where the Digital Lead cannot confirm the position, mark the affected information `Pending confirmation` and state what output, decision, or report is affected.

## Initiative origin

Every initiative must retain its origin and originating reference where available.

Example origins include:

- request form;
- CAPEX programme or approved funding request;
- transition requirement;
- leadership request;
- regulatory or operational requirement;
- assessment or benchmark finding;
- enhancement to an existing initiative.

Origin determines context and may affect the entry position, but it does not bypass route-specific governance controls.

## AI-readable initiative evidence files

Because Claude cannot read the live client systems, every initiative must have an AI-readable evidence and decision set available inside the client project knowledge or supplied to the relevant session.

This is not a duplicate live Jira portfolio ledger. It is the controlled evidence package that allows the initiative thread and reporting threads to work from the same latest approved information.

The evidence set should contain or link to, as relevant:

- initiative origin and originating artefact;
- latest confirmed status summary and reporting period;
- approved scope and exclusions;
- decision and approval records;
- delivery milestone and health evidence;
- risks and blockers;
- acceptance, adoption, benefits, and closeout evidence;
- source-of-truth impact records;
- action references and latest Digital Lead-confirmed Omega 365 status;
- required Jira, SharePoint, and Omega 365 physical updates;
- last Digital Lead confirmation date.

The exact file format may follow the applicable initiative artefacts and client file structure. Do not create an uncontrolled generic programme-memory ledger merely to copy Jira.

## Update-once rule

A confirmed update received in any initiative, bi-weekly, or monthly reporting session must first be routed to the affected initiative evidence and decision files.

No material initiative fact, decision, risk, milestone, evidence item, benefit claim, or action status may exist only in:

- the bi-weekly reporting thread;
- the monthly reporting thread;
- the initiative chat thread;
- a previous report;
- synced project knowledge;
- assistant memory.

For every confirmed update, Claude must identify:

1. the affected initiative or initiatives;
2. the evidence or decision file that must be updated;
3. the Jira update required;
4. the SharePoint update required;
5. the Omega 365 update required;
6. any other source-of-truth artefact affected;
7. whether the Digital Lead has confirmed the physical client-system update as completed, deferred, or still pending.

Claude may prepare revised AI-readable evidence-file content where the file is accessible for controlled editing. Client-system updates remain recommendations for Digital Lead or authorised-user action.

## Bi-weekly programme-reporting flow

Use this sequence:

```text
Latest initiative evidence set
→ present each affected initiative position
→ Digital Lead confirms or corrects status, decisions, evidence, risks, milestones, and actions
→ update or prepare the affected initiative evidence and decision files
→ identify required Jira / SharePoint / Omega 365 physical write-backs
→ record physical-write-back status
→ generate the bi-weekly report from the confirmed initiative evidence
```

Where an evidence-file update or physical client-system write-back remains pending, the report may use the Digital Lead-confirmed position only if the pending update is clearly stated.

The bi-weekly report should cover, as relevant:

- current status and delivery health;
- progress since the previous cycle;
- next fortnight's work;
- decisions required;
- risks and blockers;
- milestone movement;
- evidence or acceptance movement;
- client actions and ownership.

## Monthly leadership-reporting flow

Monthly leadership reporting uses the same confirmation and evidence-file write-back rule.

It summarises confirmed initiative positions and must not introduce facts or claims that have not first been reconciled to the affected initiative evidence.

Leadership reporting should focus on:

- overall programme position;
- outcomes and material progress;
- assurance, risk, and control;
- decisions or escalation required;
- CAPEX or funding position where relevant;
- benefits, adoption, and source-of-truth impact where evidenced;
- next leadership actions.

## Session closeout

Every material initiative or reporting session must end with:

1. confirmed changes received;
2. affected initiatives and artefacts;
3. initiative evidence and decision files updated or prepared for update;
4. recommended Jira updates;
5. recommended SharePoint updates;
6. recommended Omega 365 updates;
7. evidence or decisions still missing;
8. Digital Lead physical actions required;
9. status freshness and next review point.

All proposed client-system updates must be labelled:

> **Recommended update — requires Digital Lead approval and physical update in the client system.**

## Boundary

Claude may summarise, identify gaps, update accessible AI-readable evidence files subject to the controlled file rules, prepare client-system update text, draft reports, and recommend actions.

Claude must not approve initiatives, change routes, mutate Jira, SharePoint, or Omega 365, alter approved controlled artefacts without authority, or state that a physical client-system write-back has occurred without explicit Digital Lead confirmation.
