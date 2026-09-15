# Client Project Workspace Guide

## Purpose

Practical setup guide for each client AI Project/workspace. Authority remains with `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` and `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md`.

## Setup

1. Create one private repository and one AI Project/workspace for the client.
2. Add the client-boundary, context, source-of-truth, method-baseline and publication-control files.
3. Bind the workspace to the public method repository read-only and the selected client repository read/write.
4. Create one initiative folder and one continuous thread per initiative.
5. Create the two reporting threads.
6. Record the exact naming convention in `CLIENT_CONTEXT.md`; do not impose Jira IDs where the client does not use Jira.

## Default thread types

```text
HOP | [Group] | [Initiative]
LIVE | [Group] | [Initiative]
CLOSED | [Group] | [Initiative]
LIVE | Programme Reporting (Bi-Weekly)
LIVE | Leadership Reporting (Monthly)
```

## What belongs where

| Location | Purpose |
|---|---|
| Chat/thread | Working dialogue and continuity aid |
| Public method repo | Client-agnostic rules, schemas and Coworker skill |
| Private client repo | Live client working authority and initiative records |
| Initiative folder | Handover/source index, Initiative Delivery Setup, evidence/decision file and initiative artefacts |
| PEP workbook | Client-control plan, portfolio control and reporting inputs |
| External client store | Manually published approved copies where configured |

## Session start

The Coworker verifies the client boundary, reads the method baseline, inspects the initiative sources and presents the latest held position for confirmation. It asks only for gaps the evidence cannot answer.

For an initiative without an Initiation Form, the Coworker identifies the alternative authority to proceed. It may draft setup with no evidenced authority but cannot move the initiative to `In Delivery`.

## Session close

Update the initiative record and PEP first, then create reporting or publication outputs. Record every manual publication only after the Digital Lead confirms it.

## Zero crossover

Never search or reuse another client's repository, files, project knowledge or thread. Stop on a client mismatch. Only anonymised, Digital Lead-approved learning may be proposed back to the public method repository.
