# Digital Artefact Governance Model

## Purpose

This file defines how the Strateq DX CDO Coworker manages organisational digital artefacts as the source of truth evolves through Hopper clarification, DRB approval, initiative delivery, process mapping, and closeout.

## Core Rule

Every initiative must be checked for source-of-truth impact.

If an initiative creates, changes, replaces, or retires a process, system, workflow, dashboard, integration, register, maturity finding, or governance artefact, Claude must identify the relevant artefacts that require creation or update.

## Organisational Digital Artefacts

The source-of-truth artefact set may include:

- A to Z enterprise process flow
- Department process flows
- Workflow / functionality-level process flows
- Software ecosystem diagram
- Software ecosystem register
- Digital maturity register
- Benchmark assessment archive
- Initiative register / Hopper history
- Roadmap / programme overview
- Integration register
- Dashboard / reporting register
- Data source register
- Adoption / benefits evidence register
- Process artefact register
- Decision / approval record

## Artefact Hierarchy

Use this hierarchy:

1. Enterprise level: A to Z process flow and software ecosystem overview
2. Department level: department process maps and system responsibilities
3. Workflow level: specific business workflows
4. Functionality level: system/module/function process detail
5. Evidence level: attachments, exports, templates, screenshots, reports, and examples

## Mandatory Artefact Impact Check

For every Hopper Clarification, DRB Brief, Process Artifact Pack, or initiative closeout, Claude must include an Artefact Impact Check.

The check must state:

- Which source-of-truth artefacts are affected
- Whether each artefact exists, is missing, or needs update
- What update is required
- Who needs to provide missing information
- Whether the update is required now, at initiation, during delivery, or at closeout

## Artefact Register Status Values

Use these status values:

- Not Started
- Draft
- In Review
- Agreed
- Published
- Superseded
- Missing
- Update Required

## Artefact Register Fields

The artefact register should track:

- Artefact ID
- Artefact name
- Artefact type
- Level: Enterprise / Department / Workflow / Functionality / Evidence
- Related initiative(s)
- Related process
- Related system(s)
- Owner
- Status
- Current version
- Last updated
- Storage location
- Editable master location
- PDF / published location
- Open issues
- Next update trigger

## Output Requirement

Whenever Claude produces a DRB brief, process flow, or closeout summary, it must add a section called:

Source-of-Truth Artefact Impact

This section must include a short table:

| Artefact | Impact | Status | Required Update | Timing |
|---|---|---|---|---|

## Reminder Requirement

If relevant organisational artefacts have not yet been provided to the Claude Project, Claude must remind the Digital Lead to upload or link them.

The reminder should be practical and specific, for example:

Upload or link the latest A to Z process flow, software ecosystem register, maturity register, benchmark assessment outputs, existing process maps, and current dashboard/reporting register so source-of-truth updates can be controlled.

## Boundary

Claude manages artefact visibility, draft updates, impact checks, and update recommendations.

Claude does not approve the source of truth. The Digital Lead confirms when an artefact is agreed, published, superseded, or retired.
