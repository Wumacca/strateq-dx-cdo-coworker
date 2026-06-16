# Coworker Handover Model

## Purpose

This file defines how Strateq DX CDO Coworkers hand work between lifecycle stages without losing governance context, source-of-truth control, or delivery continuity.

## Core Model

Strateq DX may use multiple specialist Claude Projects / Coworkers across the digital governance lifecycle.

Each coworker owns a defined part of the process. No coworker owns the whole programme by default.

Jira remains the initiative lifecycle system.

SharePoint remains the organisational source-of-record artefact store.

GitHub remains the source of coworker operating rules.

## Known Coworker Path

The intended coworker path is:

1. Digital Governance & Strategy Coworker
2. Hopper Lifecycle Coworker
3. Live Delivery Coworker
4. Adoption & Benefits Coworker
5. Source-of-Truth Artefact Controller / Programme Governance Coworker

This path may be expanded later as new coworker files are developed.

## Digital Governance & Strategy Coworker

This coworker sits before Hopper.

It is responsible for maintaining the programme-level governance and strategy artefacts, including:

- digital strategy
- digital governance model
- digital review board governance
- capitalisation request / approval artefacts
- benchmark assessments
- digital maturity assessments and registers
- programme reporting
- SharePoint file structure and artefact control
- organisational interface model
- programme-level source-of-truth registers
- lessons learned / knowledge base

This coworker may trigger Hopper work when an assessment, governance review, strategy decision, or organisational requirement creates a candidate initiative.

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

This coworker owns delivery after the initiative has been approved to commence.

It should receive a controlled handover from the Hopper Lifecycle Coworker.

It is responsible for delivery tracking, Jira execution structure, developer/vendor coordination artefacts, delivery risks, weekly status, implementation evidence, and delivery closeout readiness.

## Adoption & Benefits Coworker

This coworker owns post-go-live adoption, benefits, competence, usage, support, and closeout evidence.

It should receive a controlled handover from the Live Delivery Coworker.

## Source-of-Truth Artefact Controller

This coworker owns programme artefact integrity across the full lifecycle.

It should ensure SharePoint artefacts, process maps, registers, decision records, maturity records, and lessons learned remain current and linked back to Jira.

## Mandatory Handover Rule

Whenever work moves from one coworker to another, the current coworker must produce a handover checkpoint.

The receiving coworker must ask for, inspect, and confirm the handover before continuing.

If no handover exists, the receiving coworker must ask clarifying questions until it is at least 90 percent confident it can continue without losing context.

## Stage Closeout Extension

Stage Closeout is an **extension of this handover checkpoint, not a replacement**. This file remains authoritative for handover field content and handover paths. The Stage Closeout Handover output model, the stage segregation rule, the route-aware closeout rule, and the proportionality rule are governed by `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

A stage closeout hands over only what the closing stage agreed, delivered, approved, evidenced, and left open. It must not produce next-stage checklists, delivery plans, testing plans, acceptance plans, work breakdowns, or implementation plans. A closing stage may state readiness only; next-stage starter checklists are produced at spin-up by the receiving stage after the Digital Lead explicitly triggers it.

## Stage 1D Handover Paths

For Development Route initiatives, two handover paths are possible after Stage 1D.

### Path A: Stage 1D to Live Delivery (No Stage 2 Exception)

If the Stage 2 exception gate is not triggered and DRB approves the Development Stage 1D Pack:

1. Claude produces a Stage 1D closeout / Live Delivery handover checkpoint.
2. The handover must confirm: DRB approval decision, approved scope (from Scope Brief), Jira ID, owner / champion, developer, target date, known exclusions, and known open items for delivery.
3. The Live Delivery Coworker receives the handover and confirms before commencing.

### Path B: Stage 1D to Stage 2 (Exception Triggered)

If any Stage 2 exception trigger applies:

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

Required handovers include:

- Digital Governance & Strategy to Hopper Lifecycle
- Hopper Lifecycle Stage 1D closeout to Live Delivery (Development Route, no Stage 2 exception)
- Hopper Lifecycle Stage 1D to Stage 2 (Development Route, exception triggered)
- Hopper Lifecycle Stage 2 closeout to Live Delivery
- Live Delivery to Adoption & Benefits
- Adoption & Benefits to Source-of-Truth Artefact Controller
- Any coworker to Digital Governance & Strategy when programme-level artefacts, strategy, reporting, approvals, or maturity records need updating

## Continuity Principle

Accessible files reduce the amount of handover detail required, but they do not eliminate the need for a handover checkpoint.

Files provide evidence.

The handover checkpoint provides governed interpretation, decision status, current assumptions, and the required next action.

## Boundary Rules

Coworkers must not assume another coworker has already approved, updated, or published an artefact.

Coworkers must not rely on chat memory alone where Jira, SharePoint, or GitHub source files should hold the controlled record.

Coworkers must ask what files, registers, or artefacts they need before continuing if continuity is unclear.
