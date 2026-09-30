# Central Live Status Intake and Branch Routing Standard

**Status:** reusable client-agnostic method standard  
**Applies to:** every new client workspace and every new initiative or workstream  
**Authority:** subordinate to `CLAUDE.md`, `OPERATING_RULES.md`, the Client Context Isolation Standard, the Method Artefact Registry and the Interactive Governed Session Protocol.

## Purpose

Every client has one central **Live Status** thread, or an explicitly named equivalent, as the single user-facing intake point for status updates, decisions, actions, RAID, initiative/workstream context and uploaded artefacts. The thread is an intake and routing surface. It is not a programme ledger and it never replaces controlled initiative records.

Each initiative or workstream retains its own controlled folder/path, controlled working branch and Initiative Evidence and Decision File (EIDF). The central thread uses the client-level branch registry to route each update to those controlled records.

## Client-level controls

The private client repository must contain, or explicitly expose through an approved client process:

- one central Live Status thread;
- one client-level initiative/workstream branch registry;
- a programme action tracker and thread tracker;
- one controlled path and one canonical working branch for every initiative/workstream;
- a reporting source (normally `main`) and an approved source-of-truth/workbook position.

The public method repository contains only this reusable rule and blank interface. It never contains client rows, branches, records or populated status.

## Intake and binding gate

Before the central thread processes any update or writes any record, it must:

1. bind exactly one client and approved private repository;
2. read the current branch registry and verify its last-verified date;
3. identify every referenced initiative/workstream and its canonical path and branch;
4. compare the branch with the approved reporting source and identify divergence;
5. classify the update as one initiative/workstream or mixed;
6. stop before writing when a row is missing, stale, divergent, undocumented, non-canonical or ambiguous.

A stopped item records the blocker and asks for the required binding decision. No write, merge, report refresh or external publication occurs until the decision is recorded and the registry is reconciled.

## New initiative/workstream control

Creation or confirmation of an initiative/workstream is incomplete until the client controls show all of the following:

- controlled folder/path created or confirmed;
- canonical working branch created or confirmed;
- branch registered at client level;
- branch status versus the reporting source recorded;
- duplicate, stale or non-canonical branches recorded;
- programme action tracker and thread tracker updated;
- EIDF/controlled initiative record linked;
- central Live Status routing instruction posted.
- expected artifact set resolved from the client profile, stage and source index;
- latest recorded version/update date and last verification date listed for each applicable artifact;
- Digital Lead asked to provide the latest copies or confirm recorded versions remain current;
- artifact inventory and unresolved/missing/conflicting items recorded in the EIDF.

The creation record must state the safe next action and the person who can approve a binding decision. Future updates are submitted to the central Live Status thread and are written to the originating initiative/workstream branch. The thread requests and inventories the applicable latest artifacts with source/path, latest recorded update date, last verification and disposition. It does not accept the new item as status-ready until required artifact gaps are supplied, clarified or explicitly accepted.

## Routing and commit behaviour

The central thread reads the registry before every update. A mixed update is split into separate change sets by initiative/workstream. Each change set is reconciled against that initiative's EIDF, PEP/control record and current evidence, then committed separately to its canonical branch. The central thread may link the results and update the tracker after approval; it must not collapse the records into one branch.

Branch names are descriptive implementation details. The registry's canonical branch is authoritative. A branch that is stale, divergent, undocumented or competing with another candidate remains blocked until a binding decision is recorded. The safe next action must never silently select a branch.

## Reporting visibility

Programme, leadership and workbook outputs are generated only from latest reconciled controlled records and the approved live workbook/source-of-truth position. A change is visible to reporting only after it is merged to the approved reporting source, normally `main`, or explicitly exposed through a client-approved process. A change that exists only on an initiative branch is not a reportable current position.

The workbook is a governed interface/snapshot. It does not override the branch registry, EIDF, PEP/control record, action system or formal approvals.
For any programme-level output, the Coworker records the reporting-source and registry revision used, enumerates every in-scope initiative/workstream, verifies each latest confirmed status and artifact-source date, and reports missing, stale, inaccessible, conflicting or excluded items. The output points to canonical artifacts and states its coverage; it does not copy artifact contents into a parallel ledger.

## Prohibited operations

Branch deletion, force-push, history rewriting, destructive rebases, Jira or other external-system updates, and external publication remain prohibited unless the bound client's controls expressly authorise the action and the Digital Lead records that authorisation. Tool access is not permission.

## Closeout and handover

Every central-thread session closes with the registry rows checked, change sets and target branches listed, reporting visibility stated, tracker updates identified, unresolved decisions recorded and the Digital Lead action block. Handover and knowledge capture preserve the same branch binding; a handover never creates a second source of truth.

## Required references

- `02_coworker_artifact_interface/11_CENTRAL_LIVE_STATUS_INTAKE_AND_BRANCH_REGISTRY_INTERFACE.md`
- `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md`
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`
- `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md`
- `02_coworker_artifact_interface/10_PROGRAMME_PORTFOLIO_WORKBOOK_INTERFACE.md`

## Mandatory pre-processing recheck

After reading the branch registry and before accepting a live update, recheck the relevant:

1. canonical branch and its current head/state versus `main`;
2. initiative/workstream controlled home/path;
3. source index or artefact index;
4. Initiative Delivery Setup file;
5. Initiative Evidence and Decision File;
6. RAID and action log.

Record the refs and verification time in the intake closeout. If any required source is missing or inconsistent, hold the update and enter binding resolution before writing.

## Binding-resolution pass

A binding-resolution pass is required for a missing, stale, divergent, undocumented or competing branch. It must:

- inspect every candidate branch and identify branch-only commits;
- preserve all controlled branch-only commits;
- consolidate relevant data into one canonical branch only when the authorised client decision permits it;
- mark duplicate, old or non-canonical branches as **no-routing** in the registry;
- avoid branch deletion unless separately authorised and technically available;
- avoid force-push, destructive rebases or history rewriting unless expressly authorised;
- record what remains branch-only and what is reporting-visible after the pass.

Live Status routing may resume only when the registry records one current canonical branch per initiative/workstream and no branch-level blocker remains. Housekeeping deletion is never a routing prerequisite.

Workbook refreshes, programme reporting updates, Jira updates and SharePoint publication require explicit client-control authorisation even when the underlying branch is resolved.
