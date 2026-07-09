# Capex Request Session Model

## Status

Governing model for the Capex Request Session. This file is the single source of the full workflow. Other files (router, lifecycle map, controlled vocabulary, operating rules, Board repo index) hold short routing pointers only and must not duplicate the workflow logic in this file.

## Purpose

The Capex Request Session is a governed Hopper Portfolio Readiness mode used to prepare a programme-level capitalisation request.

It converts the process recently used for the THREE60 capitalisation closeout and next six-month request into a reusable Strateq DX method. It is used whenever the Digital Lead needs to close out a previous capex position and/or present the next portfolio-level capex ask to the Board, with an evidence-safe narrative and a client-review draft deck.

The Capex Request Session supports:

1. Previous capex closeout
2. Next capex portfolio request
3. Evidence-safe Board narrative
4. Client-review Board-draft deck
5. Controlled Hopper-to-Delivery handover

## Positioning

The Capex Request Session operates as portfolio-level bulk initiation review: it consolidates a set of candidate and in-flight initiatives into one funding request in a single session, rather than processing each initiative as a separate Pack 1 / Initiation Form session.

The formal output of this process is the **Portfolio Capex Request Pack**. Do not use "Bulk Initiation Pack" as the name of the formal artefact. "Bulk initiation" may be used only to describe how the process operates, never as an artefact name.

## Authority and Subordination

This model operates under, and does not override:

- `CLAUDE.md`
- `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`
- `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`
- `00_system_control/04_COWORKER_HANDOVER_MODEL.md`
- `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`
- `00_system_control/OPERATING_RULES.md`
- `00_system_control/CONTROLLED_VOCABULARY.md`
- `01_governance_lifecycle/05_ROUTE_RULES.md`
- `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`
- `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`
- `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`
- `docs/presentation-standards/communication-and-framing-standard.md`, where present

`00_system_control/11_COWORKER_ROUTER.md` resolves jurisdiction and points to this file. Where the router and this file appear to differ on the process, this file governs and the conflict must be surfaced to the Digital Lead before final output.

## Governance Sequence

The Capex Request Session sits across Digital Governance & Strategy, Hopper Portfolio Readiness, and DRB / leadership approval, with a controlled handover to Live Delivery for each approved initiative:

```text
Previous capex closeout evidence + next-candidate Hopper set
↓
Capex Request Session (Hopper Lifecycle Coworker)
↓
Capex Readiness Tracker populated / gap loop run to Digital-Lead-confirmed readiness
↓
Portfolio Capex Request Pack + client-review Board-draft deck produced
↓
DRB / leadership review and decision on the funding envelope
↓
Hopper → Live Delivery Handover Checklist issued per approved initiative
↓
Route-specific controls (Completed Initiation Form, Stage 1D, Stage 1 / Stage 2, PEP) proceed per initiative
```

The Capex Request Session is **not** a replacement for single-initiative route controls. It is a portfolio-level readiness and Board-narrative mode that sits alongside, and feeds into, the existing Hopper-to-Initiation route.

## Core Jurisdiction

The Hopper Lifecycle Coworker owns the Capex Request Session as a portfolio-level Hopper readiness / capex request process.

### The Hopper Coworker May

- read controlled delivery evidence
- identify closeout gaps
- facilitate clarification
- consolidate the next-capex initiative set
- route-classify each initiative
- assemble the combined business case
- produce the Capex Readiness Tracker
- produce Capital Efficiency Evidence
- produce Plan Attainment Evidence
- produce a Claim Safety Table
- produce a Board slide brief / storyboard
- produce a client-review Board-draft deck
- issue the Hopper → Live Delivery Handover Checklist

### The Hopper Coworker Must Not

- approve final spend
- approve variance
- approve maturity movement
- approve benefits realisation
- approve budget
- approve initiatives
- commit scope
- create a Board-final issue
- mobilise delivery
- update Jira
- update SharePoint
- update GitHub
- update source-of-truth artefacts
- invent delivery truth, cost, savings, benefits, maturity, or Board claims

## Output Boundary

The Capex Request Session may produce:

> A Board slide brief / storyboard and a client-review Board-draft deck, with all open dependencies visible as placeholders.

The Capex Request Session must not produce:

> A Board-final deck or final approval wording while finance, maturity, or other Board-final blockers remain open.

A Board-final deck may only be produced once every Board-final blocker on the Claim Safety Table is cleared, and only when the Digital Lead confirms it is ready to be issued as final.

## Mandatory Board Ask

Every Capex Request Session must put the Board Ask up front. The ask must not be hidden at the end of the deck or buried in evidence.

The Board Ask must include:

- closeout ask
- continuation / next-capex ask
- indicative capital value or explicit TBC
- purpose of continuation
- open dependencies / Board-final blockers

Do not invent an indicative capital value. Where finance has not confirmed a figure, state it as **TBC** rather than estimating.

## Capital Efficiency Evidence

Capital Efficiency Evidence is a mandatory information requirement and output section covering, for each cost-avoidance / value case:

- baseline cost
- revised cost
- avoided cost
- recurring avoided cost, if applicable
- arithmetic check
- evidence basis
- claim status
- finance validation status
- Board-safe wording

### Rules

- Do not invent savings.
- Do not mix one-off and recurring savings into one total without labelling which is which.
- Calculate percentage reductions correctly: `(baseline cost − revised cost) / baseline cost × 100`. Show the calculation, not just the result.
- Mark finance-dependent claims as pending until validated by finance.
- Use Board-safe wording (see `docs/presentation-standards/communication-and-framing-standard.md` Section 6) where evidence is incomplete.

### Capital Efficiency Evidence Table

| Case | Baseline cost | Revised cost | Avoided cost | Recurring avoided cost (if applicable) | Arithmetic check | Evidence basis | Claim status | Finance validation status | Board-safe wording |
|---|---|---|---|---|---|---|---|---|---|

## Plan Attainment Evidence

Plan Attainment Evidence is a mandatory information requirement and output section covering:

- committed initiatives
- delivered / live / controlled / next-phase status
- date movement reason
- budget position
- unsupported claims
- Board-safe closeout wording

### Delivery / Adoption Separation Rule

> Delivery may close once delivery acceptance, go-live, and delivery evidence are complete. Adoption and benefits remain separate lifecycle controls where required and must not be collapsed into delivery closeout.

### Plan Attainment Evidence Table

| Committed initiative | Status (delivered / live / controlled / next-phase) | Date movement reason | Budget position | Unsupported claims flagged | Board-safe closeout wording |
|---|---|---|---|---|---|

## Claim Safety Table

The Claim Safety Table is the claim-safety control table for all Board-facing outputs produced in a Capex Request Session.

Minimum fields:

- claim
- evidence source
- claim status
- Board-safe wording
- blocker / dependency
- owner
- confidence basis

### Claim Status Values

Use the claim classification in `docs/presentation-standards/communication-and-framing-standard.md` Section 6: Confirmed / Supported-Pending / Not Claimable.

### Confidence Basis Rule

Confidence is a source-read judgement, not a score. Do not use invented numeric confidence scores (no 1–5, no percentage confidence). State the confidence basis in words, referencing the controlled source it is read from (for example: "confirmed from finance reconciliation", "read from Digital Lead status confirmation, unvalidated by finance", "inferred, no controlled source").

### Claim Safety Table

| Claim | Evidence source | Claim status | Board-safe wording | Blocker / dependency | Owner | Confidence basis |
|---|---|---|---|---|---|---|

## Deck Output Standard

The client-review Board-draft deck must follow the Executive Communication & Framing Standard where `docs/presentation-standards/communication-and-framing-standard.md` exists.

Use the narrative arc: **position → evidence → implication → recommendation → next step**.

The deck must be:

- decision-led, not activity-led
- Board-safe
- claim-safe
- evidence-mapped
- explicit on blockers
- explicit on the ask

The deck must frame the capex request through the Board Pack Framing Hierarchy (`docs/presentation-standards/communication-and-framing-standard.md` Section 5):

1. enterprise risk and assurance
2. Duty Holder / regulatory expectation where applicable
3. operating model and governance
4. scalability and sustainability
5. efficiency, automation and tooling
6. cost avoidance / capital efficiency where evidenced

## Source-Read Contract

The deliverables / evidence file is the target-state primary source for live programme status, where it exists and is mature.

Where the deliverables file is not yet mature, the coworker must request interim evidence such as:

- current Jira plan snapshot
- Board delivery deck
- Digital Lead status confirmation
- finance reconciliation
- maturity reviewer / date / approval status
- adoption gate records

### Source-Read Order

Read status from controlled files in this order where available:

1. Deliverables / evidence file
2. Actual delivery and variance record
3. Benefits and evidence register
4. Emergent work register
5. Digital governance process map
6. Digital maturity register
7. Final finance reconciliation
8. Adoption gate records and assurance evidence
9. Original approved capitalisation request
10. Executive Communication & Framing Standard / protocol

Where a source in this order does not exist or is not accessible, flag it as an access gap under the Claude Opus Access Confirmation Gate in `CLAUDE.md` rather than substituting an assumption.

## Readiness Gate

The session reaches ready only when every required item is either:

- present from a controlled source, or
- explicitly logged as an accepted gap by the Digital Lead

The readiness state is confirmed by the Digital Lead. Do not describe readiness as an AI-generated numeric confidence score or percentage.

## Gap Loop

Use one consolidated gap request, not drip-feed questions.

The gap loop is:

1. read sources
2. populate Capex Readiness Tracker
3. present gaps / questions in one consolidated set
4. receive Digital Lead input
5. update tracker
6. repeat until Digital Lead confirms ready

## Capex Readiness Tracker

The Capex Readiness Tracker is the working control document for the session. It tracks, per initiative and per evidence requirement, what is known, what is missing, and what is an accepted gap.

### Capex Readiness Tracker Table

| Initiative / case | Evidence requirement | Source read | Status (present / missing / accepted gap) | Owner | Digital Lead decision |
|---|---|---|---|---|---|

## Hopper → Live Delivery Handover Checklist

### Handover Control Rule

> No approved initiative moves from Hopper to Live Delivery unless the handover checklist is complete or the Digital Lead explicitly accepts the missing items as mobilisation gaps.

This strengthens, and does not replace, the existing Hopper Lifecycle Stage 1D / Stage 2 closeout to Live Delivery handover paths governed by `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`.

### Handover Checklist Fields

The handover checklist must include, per initiative:

- initiative name / ID
- approved route: Development Route / Implementation / Support Route / TBC
- approval basis
- approval date and conditions
- business justification
- success measures
- indicative cost and capex / non-capex position
- owner / sponsor / champion
- dependencies and sequencing anchors
- open scoping actions
- PEP / delivery-structure setup required in Jira
- artefacts to update on mobilisation
- open evidence dependencies
- accepted mobilisation gaps
- handover point recorded
- receiving coworker / owner confirmed

## Capex Approval Boundary

> Approval of the capex request approves the funding envelope / programme intent only. It does not automatically approve each initiative to begin delivery unless the approval explicitly confirms that route and the required initiative-level controls are complete.

> The Portfolio Capex Request Pack does not replace route-specific controls, Completed Initiation Forms, Stage 1D, Stage 1 / Stage 2, PEP, Live Delivery handover, or source-of-truth approval.

Each approved initiative still requires its own route trigger under `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md` and `01_governance_lifecycle/05_ROUTE_RULES.md`, and its own Completed Initiation Form under `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md` where required, before delivery mobilisation.

## Session Outputs

A Capex Request Session may produce, once Digital Lead approval is given at each controlled step:

1. Access confirmation gate response
2. Source-read status reflection
3. Capex Readiness Tracker
4. Portfolio Capex Request Pack
5. Capital Efficiency Evidence
6. Plan Attainment Evidence
7. Claim Safety Table
8. Board slide brief / storyboard
9. Client-review Board-draft deck
10. Hopper → Live Delivery Handover Checklist

## Prohibited Outputs

A Capex Request Session must not produce:

- final spend approval
- maturity approval
- benefits approval
- a Board-final deck while blockers remain open
- initiative-level delivery mobilisation
- Pack 1 / Stage 1D / Stage 1 / Stage 2 detail before route-specific spin-up
- Jira delivery / epic build
- unsupported Board claims
- controlled updates without Digital Lead approval

## Looping Compliance — Mandatory Closeout

Every Capex Request Session is a material governed session under `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md` and must close with the full governed workflow-looping closeout, using the field authority in `00_system_control/04_COWORKER_HANDOVER_MODEL.md` and `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.

Closeout must include, where material: the handover (`04`), Knowledge Capture Review (`06`), the CDO QA / Self-Improvement Check (advisory only), and Source-of-Truth Update Recommendations (advisory only). All are report-only recommendations and do not update any controlled record without Digital Lead approval.

## Approval Gate

Digital Lead approval is required for:

- session spin-up
- readiness confirmation
- output use / issue of the deck or pack
- every controlled update

## Boundary

Nothing in this file extends AI authority beyond the boundaries set in `00_system_control/OPERATING_RULES.md`, `00_system_control/04_COWORKER_HANDOVER_MODEL.md`, `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`, `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`, and `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`. Where this file and an authority file appear to conflict, surface the conflict to the Digital Lead before producing final output.
