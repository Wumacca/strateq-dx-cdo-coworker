# Completed Initiation Form Output Model

## Purpose

This file is the single authority for the formal DRB-facing approval artefact.

The formal approval document produced for leadership / DRB approval is the **Completed Initiation Form**. This applies to both the Development Route (Stage 1D / Pack 1, Development Approval) and the Implementation / Support Route (full two-stage initiation).

Other files must hold short routing pointers to this file. They must not duplicate the full rules below.

## Naming Rule

The formal approval document must be called **Completed Initiation Form**.

Do not use "DRB Brief" as the name of a final pack deliverable or formal approval artefact.

The term **DRB** may still be used for:

- DRB meeting
- DRB approval
- DRB decision required
- DRB approval status
- DRB-ready pack
- DRB decision text
- optional DRB meeting-support text where explicitly requested by the Digital Lead

But the approval document itself is the **Completed Initiation Form**.

## Optional DRB Meeting-Support Text Rule

Short DRB summaries may exist only as optional meeting-support text, Jira-ready text, or decision-support text, and only when the Digital Lead explicitly requests them.

Optional DRB meeting-support text:

- must not replace the Completed Initiation Form
- must not be treated as a formal approval artefact
- does not replace the Jira Initiative View / Hopper priority view as the default Hopper meeting surface

The format for optional DRB meeting-support text is governed by `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md`, which is meeting-support text only and is not the formal approval artefact.

## Pack Deliverable Rule

Do not collapse the whole pack into the Initiation Form. The Completed Initiation Form is the formal approval document within the pack; it does not replace the other required pack outputs.

### Development Route Stage 1D / Pack 1

The corrected Pack 1 / Stage 1D outputs are:

1. Jira field-ready values (250-character limit per `04_intake_dispatch/02_JIRA_FIELD_LENGTH_RULES.md`)
2. Completed Initiation Form — Development Approval
3. Scope Brief — including epic, task / milestone, and subtask level where provided
4. Process flow swimlane specification — produced from the completed Process Flow Capture Sheet where process mapping is required
5. Source-of-truth artefact impact check and handover note — required where controlled artefacts are impacted, using `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`

The detailed Stage 1D rules remain governed by `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`.

### Implementation / Support Route or full two-stage initiation

The equivalent formal approval output must also be called the **Completed Initiation Form**. The detailed rules remain governed by `01_governance_lifecycle/04_INITIATION_FORM_INTAKE_MODEL.md` and `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`.

## Session-Opening Source-Document Checklist

At the start of any Pack 1, Pack 2, Initiation Form, Implementation Route, Support Route, or Stage 1D session, Claude must request available source documents before producing outputs.

The source-document checklist must include:

- Current / draft Initiation Form, if available
- Hopper / Jira idea record or Jira work item export
- Leadership / DRB approval decision or Approved Route Trigger decision
- Process Flow Capture Sheet, where process mapping is required or likely required
- Vendor quote(s), T&Cs, or options comparison documents, where third-party solution selection is involved
- Existing process maps or parent process artefacts
- Existing system / register / interface documents, where impacted
- Known approval records, DRB notes, or decision history
- Any supporting evidence or attachments referenced by the initiator

## Uploaded Initiation Form Handling Rule

If a draft or partially completed Initiation Form is uploaded, Claude must treat it as the **primary approval-document source**.

Claude must:

- read the uploaded Initiation Form
- identify missing or weak sections
- ask only the questions needed to fully populate the form
- use the answers and supporting documents to produce the Completed Initiation Form
- preserve the organisation's intended form structure where possible
- avoid creating a separate DRB Brief unless the Digital Lead explicitly requests it as optional meeting-support text only

## Required Initiation Form Structure

Where the organisation's template is available, Claude must align the Completed Initiation Form to that structure, including where applicable:

### Initiative Initiation

- Initiative Title
- Raised By
- Date
- Initiative Description
- Background & Context
- Problem Statement
- Options Considered
- Solution Overview
- Benefits To The Business
- Perceived Urgency / Risk If Not Addressed
- Supporting Documents

### Digital Assessment & Project Charter

- Confirmation of problem statement
- Refinements / scope clarifications
- Selected solution
- Selection appraisal
- Digital maturity alignment
- Roadmap track
- Maturity goal support
- System impact
- New system(s)
- Existing system(s) enhanced
- Systems made redundant
- Integrations required
- Specialist IT / security steps required
- Scope definition
- In Scope
- Out of Scope
- Success Measures

### Risk Assessment

- Key risks
- Risk score
- Mitigations
- Mitigated risk score

### Stakeholders and Communications

- Key stakeholders
- Communications plan

### Approvals Register

- Raised By
- Reviewed By
- Authorised By
- Approval comments

Claude must not invent costs, benefits, risks, owners, sponsors, dates, scores, or technical facts to fill the form.

## Export Format

The Completed Initiation Form export must be Word-compatible / `.docx` where possible, preserving headings, tables, and section structure for copy/paste into the organisation's Word template. A clean Jira-paste version may also be provided where useful.

## Boundary

The Completed Initiation Form prepares the decision and supports DRB approval. It does not approve the initiative. Leadership / DRB approval creates the Approved Route Trigger; after approval each initiative follows its correct route under `01_governance_lifecycle/05_ROUTE_RULES.md` and `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md`.
