# Client Project Workspace Guide

## Purpose

This is the practical setup guide for each client Claude Project. Detailed lifecycle and governance rules remain controlled by the authority files. The client workspace and reporting rules are governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`.

## Two client-project coworkers

Each initiative is owned by two client-project lifecycle coworkers in turn, inside the same continuous thread: the **Hopper Lifecycle Coworker** (origin and intake through approval to commence delivery) and the **Live Delivery Coworker** (approval through delivery, adoption, benefits, source-of-truth impact, and closeout). The only principal handover is Hopper Lifecycle Coworker → Live Delivery Coworker, at approval. DRB, source-of-truth artefact control, adoption, benefits, capitalisation, maturity review, and reporting are governed stages, controls, or modes inside the thread — not separate coworkers or threads. Digital Governance & Strategy is a programme governance and control function, not a client-project coworker.

## Project structure

Create one Claude Project per client.

Use only these thread types:

```text
HOP | [ID] | [Initiative]
LIVE | [ID] | [Initiative]
CLOSED | [ID] | [Initiative]
90 | Bi-Weekly Programme Reporting
91 | Monthly Leadership Reporting
```

There is no Portfolio Control thread and no separate DRB thread.

Each initiative remains in one continuous thread. Rename the thread as the initiative moves from Hopper to Live Delivery and then Closed.

## What belongs in the initiative thread

The initiative thread handles the full governed lifecycle for that initiative, including:

- origin and intake;
- clarification and route;
- initiation forms and DRB preparation;
- approval and handover;
- delivery control;
- decisions, risks, blockers, milestones, and evidence;
- acceptance, adoption, benefits, source-of-truth impact, and closeout where applicable.

The thread is not the controlled record. It works from the initiative evidence and decision files available in the project knowledge or supplied to the session.

## What belongs in the bi-weekly reporting thread

Use `90 | Bi-Weekly Programme Reporting` for:

- confirming the latest status of each initiative in scope;
- recording progress since the previous cycle;
- confirming next-fortnight work;
- identifying decisions, risks, blockers, milestone movement, and client actions;
- preparing the bi-weekly programme report.

Do not leave new facts only in this thread. Any confirmed change must first be routed to the affected initiative evidence and decision files.

## What belongs in the monthly leadership thread

Use `91 | Monthly Leadership Reporting` for:

- overall programme position;
- outcomes and material progress;
- assurance, risk, and control;
- leadership decisions or escalation;
- CAPEX or funding position;
- evidenced benefits, adoption, and source-of-truth impact;
- next leadership actions.

The monthly report must use the confirmed initiative positions. It must not become a separate source of truth.

## No live client-system connection

Claude cannot access live Jira, SharePoint, or Omega 365.

At the start of every material initiative or reporting session, Claude presents the latest position it holds and asks:

> **Is this still accurate? Please confirm or provide any changes since the last recorded update.**

The Digital Lead confirms or corrects the position.

Claude then:

1. identifies the affected initiative evidence and decision files;
2. updates or prepares those files for controlled update;
3. prepares Jira, SharePoint, and Omega 365 write-back instructions;
4. records whether the physical updates are complete, deferred, or pending;
5. produces the initiative output or report from the confirmed position.

## Update-once rule

Update the initiative evidence first, then produce the report.

This prevents the bi-weekly or monthly reporting thread from becoming newer than the initiative thread and prevents stale initiative responses later.

## Client-facing tool split

- **Jira:** initiative and delivery status.
- **SharePoint:** approved forms, decisions, evidence, reports, and controlled artefacts.
- **Omega 365:** actions.
- **Claude:** internal coordination, challenge, drafting, evidence-file maintenance, and write-back preparation.

Claude must never state that a client-system update has occurred unless the Digital Lead confirms the physical update.
