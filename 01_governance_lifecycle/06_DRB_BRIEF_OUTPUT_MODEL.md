# DRB Brief Output Model

## Purpose

This file defines the standard DRB Brief format for Jira initiative descriptions and DRB approval meetings.

## Core Rule

The DRB Brief is a Leadership Team approval document, not a working-session document.

The DRB Brief must be executive, decision-ready, and suitable for pasting into the Jira initiative description field.

It must not look like raw markdown notes, internal AI analysis, or a technical dump.

Open questions must not appear in the final DRB Brief.

If scope, ownership, system, process, delivery, risk, cost, timing, or approval questions remain unresolved, Claude must withhold the final DRB Brief and return a questions-only output to the Digital Lead.

The final DRB Brief may only be produced when all questions are answered, excluded, or explicitly deferred outside the approval decision.

## DRB Brief Formats

Claude must produce the DRB Brief in one of two formats:

1. Jira description version — clean paste-ready format for Jira description fields.
2. Word-friendly version — inline formatted version with headings, tables, and bullets suitable for copy/paste into Word.

Claude must ask which format is required unless the target is already clear from context.

## Output Modes

Claude should produce two versions when preparing a DRB brief:

1. Jira Description Version
2. Word-Friendly Version

The Jira Description Version is the primary output.

## Jira Description Version Standard

Use clean headings, short paragraphs, and compact tables only where useful.

Avoid excessive markdown symbols, code blocks, nested bullets, and long raw tables.

The brief must include:

- Initiative title
- Decision required
- Executive summary
- Current problem
- Current process
- Proposed future requirement
- Expected benefit
- Risk / impact view
- Process flow status
- Decision readiness
- Recommended DRB decision
- Next steps if approved

The brief must not include an open questions section. If unresolved material questions exist, Claude must withhold the final brief and return a questions-only output instead.

## Required DRB Decision Labels

Use the canonical decision labels in:

`00_system_control/CONTROLLED_VOCABULARY.md`

## Process Flow Requirement

If the initiative changes how work is done, Claude must include a Process Flow Status section.

This section must state one of:

- Process flow drafted and attached
- Process flow required before Initiation Form
- Process flow not required
- Insufficient process detail to draft flow

## Swimlane Requirement

If process information is available, Claude must also produce a Draft Swimlane Process Flow using:

`03_process_mapping/05_SWIMLANE_PROCESS_FLOW_STANDARD.md`

The swimlane should be separate from the Jira DRB Brief unless the user asks for it to be embedded.

## Jira Description Template

Use this structure:

Title: [Initiative name]

Decision required: [canonical DRB decision]

Executive summary:
[2 to 4 sentences explaining what this is, why it matters, and what DRB is being asked to decide.]

Current problem:
[Short plain-language problem statement.]

Current process:
[Short summary of what happens today.]

Future requirement:
[Short summary of the required change or capability.]

Expected benefit:
[Short summary of business value / risk reduction / control improvement.]

Risk and impact view:
Safety / Duty Holder: [Low / Medium / High / Critical / TBC]
Regulatory / Reputational: [Low / Medium / High / Critical / TBC]
Commercial: [Low / Medium / High / Critical / TBC]
Operational: [Low / Medium / High / Critical / TBC]

Process flow status:
[Status statement]

Decision readiness:
[State that all material questions have been resolved, excluded, or explicitly deferred outside this approval decision.]

Recommended DRB decision:
[Canonical decision + short reason.]

Next steps if approved:
[Short action list.]

## Boundary

The DRB Brief prepares the decision. It does not approve the initiative.
