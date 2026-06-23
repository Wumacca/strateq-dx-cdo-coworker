# DRB Meeting-Support Text Output Model

## Purpose

This file defines the standard format for **optional DRB meeting-support text** — short executive, decision-ready summary text for Jira initiative descriptions and DRB approval meetings.

> **Formal approval artefact pointer.** The formal DRB-facing approval artefact is the **Completed Initiation Form**, governed by `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`. The output defined in this file is **optional DRB meeting-support text only**. It is not a final pack deliverable and not a formal approval artefact, and it must not replace the Completed Initiation Form or the Jira Initiative View / Hopper priority view as the default Hopper meeting surface. It is produced only when the Digital Lead explicitly requests written meeting-support text.

## Core Rule

DRB meeting-support text is optional decision-support text, not a working-session document and not the formal approval document.

It must be executive, decision-ready, and suitable for pasting into the Jira initiative description field.

It must not look like raw markdown notes, internal AI analysis, or a technical dump.

Open questions must not appear in the final meeting-support text.

If scope, ownership, system, process, delivery, risk, cost, timing, or approval questions remain unresolved, Claude must withhold the final text and return a questions-only output to the Digital Lead.

The final meeting-support text may only be produced when all questions are answered, excluded, or explicitly deferred outside the approval decision.

## Meeting-Support Text Formats

Claude must produce the meeting-support text in one of two formats:

1. Jira description version — clean paste-ready format for Jira description fields.
2. Word-friendly version — inline formatted version with headings, tables, and bullets suitable for copy/paste into Word.

Claude must ask which format is required unless the target is already clear from context.

## Meeting-Support Text Variants

Two variants are defined based on the initiative route. Each is optional meeting-support text that accompanies — and never replaces — the Completed Initiation Form.

### Development Approval meeting-support text

Used for Development Route Stage 1D initiatives where Pack 1 is sufficient for DRB to approve commencement of the live development job without requiring Stage 2.

The Development Approval meeting-support text must:

- state the decision as approval to commence the live development job
- summarise the Scope Brief as a supporting section
- confirm the Stage 2 exception gate decision in the Decision readiness section (confirming no exception triggers apply, or listing any the Digital Lead has explicitly accepted and why)
- not commit to external suppliers, quotes, or vendor selection unless already confirmed

### Implementation / Support Initiation meeting-support text

Used for Implementation / Support Route Stage 1 initiatives.

This meeting-support text:

- supports the Stage 1 decision: whether formal initiation should commence
- does not commit to a solution, cost, or delivery timeline (those belong in Stage 2)
- supports the fuller Stage 1 + Stage 2 route

If the route is unclear, Claude must ask before selecting the variant.

## Output Modes

Claude should produce two versions when preparing DRB meeting-support text:

1. Jira Description Version
2. Word-Friendly Version

The Jira Description Version is the primary output.

## Jira Description Version Standard

Use clean headings, short paragraphs, and compact tables only where useful.

Avoid excessive markdown symbols, code blocks, nested bullets, and long raw tables.

The meeting-support text must include:

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

The meeting-support text must not include an open questions section. If unresolved material questions exist, Claude must withhold the final text and return a questions-only output instead.

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

The swimlane should be separate from the Jira meeting-support text unless the user asks for it to be embedded.

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

DRB meeting-support text supports the decision discussion. It does not approve the initiative and it is not the formal approval artefact. The formal approval artefact is the Completed Initiation Form (`01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`).
