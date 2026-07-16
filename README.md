## Strateq DX Repository Purpose

Strateq DX is the controlled evidence and delivery repository for Strateq-led digital transformation, governance, capitalisation, and Board reporting work. It is separate from Quantuum AI product build material.

## Repository Structure

- `THREE60/` holds THREE60 delivery and governance evidence.
- `_archive/source_zips/` holds original source packs and imported zip files.
- Board-facing content must be generated from controlled markdown source files, not from standalone slide edits.

## Client Workspace and Reporting Controls

There are exactly two client-project lifecycle coworkers — the **Hopper Lifecycle Coworker** (origin and intake through approval to commence delivery) and the **Live Delivery Coworker** (approval through delivery, adoption, benefits, source-of-truth impact, and closeout). The only principal coworker handover is Hopper Lifecycle Coworker → Live Delivery Coworker. DRB, source-of-truth artefact control, adoption, benefits, capitalisation, maturity review, and reporting are governed stages, controls, or modes — not separate coworkers or threads. Digital Governance & Strategy is a programme governance and control function, not a client-project coworker. Each initiative runs in one continuous thread (`HOP` → `LIVE` → `CLOSED`), with only two non-initiative threads: `90 | Bi-Weekly Programme Reporting` and `91 | Monthly Leadership Reporting`.

The Claude client-project workspace, no-live-connection boundary, confirmation-first status rule, single AI-readable Initiative Evidence and Decision File, and reporting-to-initiative-evidence write-back are governed by:

- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`
- `00_system_control/13_INITIATIVE_CONTROL_RECORD_SCHEMA.md` (reusable schema; the evidence file is its client-copy implementation)
- `02_coworker_artifact_interface/04_INITIATIVE_EVIDENCE_AND_DECISION_FILE_TEMPLATE.md`
- `02_coworker_artifact_interface/05_BIWEEKLY_PROGRAMME_UPDATE_INPUT_TEMPLATE.md`
- `06_operating_manual/02_CLIENT_PROJECT_WORKSPACE_GUIDE.md`

These files do not replace the existing lifecycle, route, approval, evidence, stage-closeout, or source-of-truth controls. Jira (initiative and delivery status), SharePoint (approved artefacts and evidence), and Omega 365 (action management) remain the client-facing operational tools. Claude has no permitted live connection to them and never claims it has read or updated a live client system.

## Executive Communication & Framing Standard

All executive presentations, board packs, CDO communications, Strateq DX materials, Quantuum materials, and tool-generated presentation outputs must follow the Communication & Framing Standard:

- Start with the executive decision or opportunity, not background.
- Frame around business outcomes, assurance, risk, value, and next decisions.
- Use a narrative arc: position → evidence → implication → recommendation → next step.
- Present recommendations clearly with action, rationale, benefit, and decision required.
- Avoid data dumps, preambles, technical-first explanations, and task-reporting.
- Preserve CDO positioning as translator, integrator, disruptor, and business-impact leader.

Canonical file:
`docs/presentation-standards/communication-and-framing-standard.md`
