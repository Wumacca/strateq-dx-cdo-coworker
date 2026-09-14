# Digital Artefact Governance Model

## Purpose

Define how Strateq DX identifies, changes, approves, releases, publishes and retires controlled digital artefacts across the initiative lifecycle.

## Source architecture

| Layer | Authority |
|---|---|
| Reusable Strateq DX method | Public method repository |
| Client working records and artefacts | Bound private client repository or system named in `SOURCE_OF_TRUTH.md` |
| Initiative continuity | Initiative Evidence and Decision File |
| Delivery control | PEP/client-control plan named in the client profile |
| Detailed execution | Named vendor/developer plan; referenced, not duplicated |
| External organisational publication | Destination named in the client profile; manual unless a verified connection is authorised |

Client data is prohibited from the public method repository. The zero-crossover standard is `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## Core rule

Every initiative must be checked for source-of-truth impact. If it creates, changes, replaces or retires a process, system, workflow, dashboard, integration, register, maturity finding or governance artefact, the Coworker identifies the affected controlled artefact and the required update.

The Coworker does not approve the source of truth. The Digital Lead confirms when an artefact is agreed, released, published, superseded or retired.

## Working and publication boundary

Where the client profile selects a private GitHub repository as the working authority:

- editable masters and control records live in that repository;
- changes are prepared through a controlled branch/PR;
- merge/release requires Digital Lead approval;
- a client SharePoint or other external store is a publication destination only;
- publication is recorded in `PUBLICATION_REGISTER.md` after the Digital Lead confirms it.

Do not treat a manually published copy as newer than the working master unless the source-of-truth profile is formally changed.

## Artefact classes

- Enterprise: end-to-end process and ecosystem views.
- Department: department processes and system responsibilities.
- Workflow: specific business workflows.
- Functionality: module/function detail.
- Evidence: exports, screenshots, test evidence, reports and examples.
- Governance: strategies, approvals, decisions, reporting, handover and lessons.

## Mandatory Artefact Impact Check

Apply at material Hopper decisions, completed initiation, Initiative Delivery Setup, process artefact creation, material delivery change and closeout.

State:

- affected artefact;
- whether it exists, is missing, needs update or is superseded;
- required update and owner;
- timing/trigger;
- working-authority path;
- external publication destination/status;
- related initiative/control reference.

Use:

| Artefact | Impact | Status | Required update | Working-authority path | Publication destination/status | Timing |
|---|---|---|---|---|---|---|

## Status values

- Not Started
- Draft
- In Review
- Agreed
- Released
- Published
- Superseded
- Missing
- Update Required

`Released` means approved in the working authority. `Published` means external publication has been confirmed. They are not interchangeable.

## Artefact register fields

- Artefact ID and name
- Type and level
- Related initiative/process/system
- Owner
- Status
- Current version
- Last updated
- Editable master path
- Released path/commit
- External destination and publication date
- Open issues
- Next update trigger

## Required output

Whenever the Coworker produces a Completed Initiation Form, Initiative Delivery Setup, process pack, Artefact 1 baseline change or closeout, include `Source-of-Truth Artefact Impact` using the table above.

## Learning back to method

A client lesson may enter the public method repository only after it has been abstracted to remove identifiable client data and the Digital Lead approves the method change. Raw client artefacts and examples must not be copied.

## Boundary

The Coworker may inspect, draft, compare, validate and prepare controlled repository changes when authorised. It may not approve, merge/release, publish externally or declare a publication complete without evidence or Digital Lead confirmation.
