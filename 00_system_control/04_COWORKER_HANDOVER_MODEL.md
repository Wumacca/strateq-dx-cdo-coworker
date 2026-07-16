# Coworker Handover Model

## Purpose

This file defines how Strateq DX CDO Coworkers hand work between lifecycle stages without losing governance context, source-of-truth control, or delivery continuity.

## Core Model

Strateq DX uses exactly two client-project lifecycle coworkers across the digital governance lifecycle: the **Hopper Lifecycle Coworker** and the **Live Delivery Coworker**. Each owns a defined part of the initiative lifecycle. The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker.

DRB, source-of-truth artefact control, adoption, benefits review, capitalisation, maturity review, and programme / leadership reporting are governed lifecycle stages, controls, or operating modes handled within the initiative and reporting threads. They are not separate client-project coworkers and do not require their own threads or their own coworker handovers.

Jira remains the client-facing initiative and delivery-status system. SharePoint remains the organisational source-of-record artefact store. Omega 365 remains the action-management system. GitHub remains the source of reusable coworker operating rules. Claude has no live connection to Jira, SharePoint, or Omega 365 and must never claim it has read or updated a live client system.

## Two-Coworker Path

The client-project coworker path is:

1. Hopper Lifecycle Coworker
2. Live Delivery Coworker

The same continuous initiative thread is renamed as the initiative progresses (`HOP | [ID] | [Initiative]` → `LIVE | [ID] | [Initiative]` → `CLOSED | [ID] | [Initiative]`). Client workspace, thread, reporting, and no-live-connection rules are governed by `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`.

## Digital Governance & Strategy (control function)

Digital Governance & Strategy is a programme governance and control function, not a client-project coworker, client-project thread, additional lifecycle owner, or mandatory coworker handover.

It concerns the programme-level governance and strategy artefacts, including digital strategy, digital governance model, DRB governance, capitalisation request / approval artefacts, benchmark assessments, digital maturity assessments and registers, programme reporting, SharePoint file structure and artefact control, organisational interface model, programme-level source-of-truth registers, and lessons learned / knowledge base.

These functions are handled through the Hopper Lifecycle Coworker where initiative governance is concerned, through the bi-weekly and monthly reporting modes where cross-initiative governance is concerned, and through the Digital Lead's governance authority. A governance, assessment, strategy, or organisational signal that creates a candidate initiative enters the Hopper Lifecycle Coworker directly; no separate governance-to-Hopper coworker handover is required.

## Hopper Lifecycle Coworker

This coworker owns the route from Hopper to approved live job.

It is responsible for:

- Hopper clarification
- route classification (Development Route or Implementation / Support Route)
- Stage 1D Development Route DRB preparation and Scope Brief
- Stage 1D process mapping capture sheet issue
- Stage 1D pack gate and Stage 2 exception gate
- Stage 1D closeout and handover to Live Delivery (Development Route, no Stage 2 exception)
- Stage 1 DRB preparation (Implementation / Support Route)
- Stage 1 process mapping capture sheet issue
- Stage 2 initiation preparation
- requirements list preparation
- vendor / developer scope review support
- initiation approval pack preparation
- Jira update text (Stage 2 and where explicitly requested)
- Stage 2 closeout and handover to Live Delivery

## Live Delivery Coworker

This coworker owns the same initiative after it has been approved to commence.

It receives the principal controlled handover from the Hopper Lifecycle Coworker.

It is responsible for delivery mobilisation, delivery tracking, Jira execution structure, developer/vendor coordination artefacts, delivery risks, weekly delivery-control touchpoints, implementation evidence, acceptance, handover, adoption, benefits checks where applicable, source-of-truth impact, and delivery closeout — all inside the same continuous initiative thread.

## Adoption and benefits (internal Live Delivery stage)

Post-go-live adoption, benefits, competence, usage, support, and closeout evidence are internal stages of the Live Delivery Coworker's ownership, handled inside the same continuous initiative thread. They do not require a separate coworker or a coworker handover. The transition from delivery into adoption/benefits is an internal stage transition, recorded in the Initiative Evidence and Decision File, not an inter-coworker handover.

## Source-of-truth artefact control (governed mode)

Source-of-truth artefact integrity is a governed control mode applied within the initiative thread whenever an initiative creates, changes, replaces, or retires a controlled artefact, governed by `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. It ensures SharePoint artefacts, process maps, registers, decision records, and maturity records remain current and referenced against the client-facing Jira status. It is a mode, not a separate client-project coworker, and does not require its own thread or coworker handover.

## Mandatory Handover Rule

Whenever work moves from one coworker to another, the current coworker must produce a handover checkpoint.

The receiving coworker must ask for, inspect, and confirm the handover before continuing.

If no handover exists, the receiving coworker must ask clarifying questions until it is at least 90 percent confident it can continue without losing context.

## Stage Closeout Extension

Stage Closeout is an **extension of this handover checkpoint, not a replacement**. This file remains authoritative for handover field content and handover paths. The Stage Closeout Handover output model, the stage segregation rule, the route-aware closeout rule, and the proportionality rule are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

A stage closeout hands over only what the closing stage agreed, delivered, approved, evidenced, and left open. It must not produce next-stage checklists, delivery plans, testing plans, acceptance plans, work breakdowns, or implementation plans. A closing stage may state readiness only; next-stage starter checklists are produced at spin-up by the receiving stage after the Digital Lead explicitly triggers it.

## Stage 1D Handover Paths

For Development Route initiatives, two paths are possible after Stage 1D. Path A is the principal coworker handover to Live Delivery; Path B is an internal escalation within the Hopper Lifecycle Coworker's ownership, not a coworker handover.

### Path A: Stage 1D to Live Delivery (No Stage 2 Exception)

If the Stage 2 exception gate is not triggered and DRB approves the Development Stage 1D Pack:

1. Claude produces a Stage 1D closeout / Live Delivery handover checkpoint.
2. The handover must confirm: DRB approval decision, approved scope (from Scope Brief), Jira ID, owner / champion, developer, target date, known exclusions, and known open items for delivery.
3. The Live Delivery Coworker receives the handover and confirms before commencing.

### Path B: Stage 1D to Stage 2 (Exception Triggered — internal escalation)

If any Stage 2 exception trigger applies (this is an internal escalation within the Hopper Lifecycle Coworker, not a coworker handover):

1. Claude produces a Stage 1D to Stage 2 escalation checkpoint.
2. The checkpoint must confirm: which exception trigger applies, what evidence supports it, current scope and open questions, and what Stage 2 inputs are required.
3. Stage 2 is then run under `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

Detailed Stage 1D workflow is governed by `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

## Stage 2 Fresh Upload Check

At the start of every Stage 2 session, before loading stored Stage 1 information, Claude must ask:

"Do you have any revised documents, screenshots, Jira updates, process mapping sheets, developer notes, or files to upload before we begin?"

Stored Stage 1 information must not be treated as current until the Digital Lead confirms no updates exist or provides replacements.

Detailed Stage 2 workflow is governed by `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

## Handover Checkpoint Format

Every coworker handover must include:

- originating coworker / lifecycle stage
- receiving coworker / lifecycle stage
- Jira key(s)
- initiative / programme name
- current lifecycle status
- decision already made
- decision still required
- approved scope
- out of scope
- key assumptions
- open questions
- known risks / constraints
- source-of-truth artefacts affected
- SharePoint artefact locations
- Jira links / update status
- required next action
- files the receiving coworker must inspect
- confidence level and remaining information gaps

## Handover Timing

The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker, which occurs at approval to commence delivery. It takes one of these route-specific forms:

- Hopper Lifecycle Stage 1D closeout to Live Delivery (Development Route, no Stage 2 exception)
- Hopper Lifecycle Stage 2 closeout to Live Delivery (Implementation / Support Route, and Development Route where the Stage 2 exception is triggered)

Stage 1D to Stage 2 (Development Route, exception triggered) is an internal escalation within the Hopper Lifecycle Coworker's ownership, not a coworker handover. Delivery → adoption/benefits → source-of-truth impact → closeout are internal Live Delivery stage transitions inside the same continuous initiative thread, recorded in the Initiative Evidence and Decision File; they are not coworker handovers. Programme-level artefact, strategy, reporting, approval, or maturity updates are handled through the reporting modes and the Digital Lead's governance authority, not through a coworker handover.

## Continuity Principle

Accessible files reduce the amount of handover detail required, but they do not eliminate the need for a handover checkpoint.

Files provide evidence.

The handover checkpoint provides governed interpretation, decision status, current assumptions, and the required next action.

## Boundary Rules

Coworkers must not assume another coworker has already approved, updated, or published an artefact.

Coworkers must not rely on chat memory alone where Jira, SharePoint, or GitHub source files should hold the controlled record.

Coworkers must ask what files, registers, or artefacts they need before continuing if continuity is unclear.
