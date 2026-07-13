# Digital Transformation Governance & Management Manual

> This manual explains how the Digital Lead uses the governed coworker system. Lifecycle and workflow rules remain controlled by the referenced authority files. Where this manual and an authority file differ, the authority file prevails.

**Classification:** Human-facing navigation manual — non-authoritative.

## How to read this manual

This manual is the human operating view. It tells the Digital Lead what each stage is for, how to open it, what the coworker will do, what the Digital Lead must do, and what "done" looks like. It does not contain the detailed workflow logic — that stays in the controlled authority files named in each section.

Every material governed session runs under the Interactive Governed Session Protocol (`00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`), which wraps the stage work in a fixed set of gates. Whatever stage you spin up, the coworker begins with:

1. **Runtime Access Confirmation Gate** — what live files and client records it can see, and what is missing.
2. **Client Context Gate** (proportionate) — which controlled client-context source it is working from.
3. **Initiative Reconciliation Gate** — the current initiative position from Jira / a Jira export / an interim register, plus any unresolved obligations.
4. **Required Inputs Gate** — one consolidated table of what is present, missing, stale, or an accepted gap.

It then maintains a **Live Session Status Board**, ends every substantive response with **Digital Lead actions required**, and cannot treat a session as closed until it has proposed a **controlled write-back** and the Digital Lead has approved, deferred, or accepted the gap.

---

## A-to-Z Overview — the four-stage macro model

The human operating view of the whole programme is four stages:

1. **Request to Hopper** — a need becomes a visible candidate item.
2. **Hopper to Go / No-Go Decision** — the item is readied, prioritised, and taken to leadership / DRB for a route decision.
3. **Initiative Delivery / Live Implementation Control** — the approved initiative is delivered under control.
4. **Completion and Handover** — the initiative is completed, adopted, and its evidence and source-of-truth records are updated.

This four-stage model is the **human operating view**. It does **not** replace the detailed controlled lifecycle in `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`. The same initiative moves across both views at once: the macro-stage is the plain-language position, the detailed lifecycle stage is the controlled process position.

| Four-stage macro model (human view) | Detailed repository lifecycle (controlled view) |
|---|---|
| 1. Request to Hopper | Steps 1–4: Digital Governance & Strategy → Assessment / Benchmark → Candidate Initiative Creation → Hopper / Intake Consolidation |
| 2. Hopper to Go / No-Go Decision | Steps 5–13: Light-touch scoping → Hopper Portfolio Readiness → DRB Priority Discussion → Route Classification → Stage 1D / Stage 1 → Stage 2 → Initiation Form / DRB form approval → Nitro / leadership sign-off |
| 3. Initiative Delivery / Live Implementation Control | Steps 14–15, 19: Job Live → Live Delivery → PEP / Development Execution |
| 4. Completion and Handover | Steps 16–18: Go-Live / Deployment → Adoption & Benefits → Source-of-Truth Artefact Control / Programme Governance Update |

Client context and maturity links are a **future governed layer** referenced by this manual but not yet operationally governed (see the placeholder note at the end).

---

## Standard manual-section anatomy

Every stage section below uses the same 17-point anatomy:

1. Purpose
2. What this stage owns
3. What this stage does not own
4. Entry criteria
5. Exact spin-up command
6. Authority files
7. Overview workflow
8. Required inputs
9. Coworker responsibilities
10. Digital Lead responsibilities
11. Live session checklist
12. Required artefacts and records
13. Approval points
14. Freshness obligations
15. Exit criteria
16. Closeout / handover
17. What the coworker will ask for next

### Checklist rule

The checklists in this manual are **expected checklists for human planning**. The live checklist used in a governed session is generated at session spin-up from the current authority file, the current initiative record, current artefacts / evidence, and the current approval and freshness position. Where they differ, the session-generated checklist prevails.

---

## Section 1 — Client Governance Foundation

`Placeholder — lifecycle-recognised, not operationally governed yet.`

1. **Purpose.** Establish the controlled client context — profile, strategic objectives, maturity roadmap, software / process ecosystem, governance artefact register — that every later stage's Client Context Gate is grounded in.
2. **What this stage owns.** The controlled client-context sources (once modelled).
3. **What this stage does not own.** Initiative-level scope, delivery, or approval.
4. **Entry criteria.** New client, or a material change to strategy / maturity / ecosystem / governance.
5. **Exact spin-up command.** Not yet governed. Do not spin up.
6. **Authority files.** Client Digital Governance Profile model — `Placeholder — lifecycle-recognised, not operationally governed yet.`; Client Governance Artefact Register model — `Placeholder — lifecycle-recognised, not operationally governed yet.`
7–17. Not operationally governed yet. Do not invent workflow detail. Until modelled, the Client Context Gate is satisfied per `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` by a controlled client-context artefact or explicit Digital Lead confirmation.

---

## Section 2 — Digital Governance & Strategy

1. **Purpose.** Maintain the governance environment that creates, assesses, prioritises, funds, reports, and controls digital change.
2. **What this stage owns.** Digital strategy, governance model, DRB model, capitalisation artefacts, programme reporting, SharePoint artefact library structure, creation of candidate initiatives.
3. **What this stage does not own.** Hopper triage, initiation, delivery, or approval decisions.
4. **Entry criteria.** Standing responsibility; or a governance / strategy signal that may create a candidate initiative.
5. **Exact spin-up command.** `Spin up a Digital Governance & Strategy session for [topic].`
6. **Authority files.** `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.
7. **Overview workflow.** Access gate → client context → reconcile relevant governance records → structure the governance artefact or candidate signal → recommendations → closeout.
8. **Required inputs.** Strategy / governance documents, benchmark or maturity records where relevant, programme reports.
9. **Coworker responsibilities.** Structure, draft, challenge, identify gaps, prepare recommendations and handover to Hopper where a candidate initiative is created.
10. **Digital Lead responsibilities.** Confirm strategy direction, approve controlled updates, confirm candidate initiatives.
11. **Live session checklist.** Access confirmed · client context grounded · governance records reconciled · artefact / candidate drafted · recommendations labelled · write-back proposed.
12. **Required artefacts and records.** Governance artefacts, candidate initiative note, SharePoint references.
13. **Approval points.** Digital Lead approves any controlled update and confirms a candidate initiative before Hopper handover.
14. **Freshness obligations.** Client strategy / maturity context rechecked at the proportionate Client Context Gate.
15. **Exit criteria.** Candidate initiative confirmed, or governance artefact updated and approved.
16. **Closeout / handover.** Governance-to-Hopper handover when a candidate initiative enters the Hopper (`00_system_control/04_COWORKER_HANDOVER_MODEL.md`).
17. **What the coworker will ask for next.** Whether to hand the candidate to the Hopper / Intake stage.

---

## Section 3 — Assessment / Benchmark / Maturity Review

1. **Purpose.** Identify gaps, risks, improvement areas, or digital maturity needs that may create candidate initiatives.
2. **What this stage owns.** Assessment evidence and recommendation logs (as a lifecycle-recognised activity).
3. **What this stage does not own.** Maturity score calculation, maturity register mutation, or initiative approval. The full Maturity Improvement Loop and Formal Re-Benchmark / Maturity Snapshot models are not yet governed.
4. **Entry criteria.** Benchmark or maturity review requested by Digital Governance & Strategy.
5. **Exact spin-up command.** `Spin up an Assessment / Benchmark / Maturity Review for [scope].`
6. **Authority files.** `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` (Step 2); Maturity Improvement Loop model — `Placeholder — lifecycle-recognised, not operationally governed yet.`; Formal Re-Benchmark / Maturity Snapshot model — `Placeholder — lifecycle-recognised, not operationally governed yet.`
7. **Overview workflow.** Access gate → client context → reconcile assessment evidence → structure gaps / candidate initiatives → recommendations → closeout. Do not invent benchmark scoring.
8. **Required inputs.** Benchmark assessment, maturity register snapshot, assessment evidence.
9. **Coworker responsibilities.** Organise, display, summarise and challenge existing Digital Lead-approved scores; identify candidate initiatives; never create or alter scores.
10. **Digital Lead responsibilities.** Own the scoring methodology and any score, approve candidate initiatives.
11. **Live session checklist.** Access confirmed · assessment evidence reconciled · gaps identified · candidate initiatives proposed · no scores invented · write-back proposed.
12. **Required artefacts and records.** Assessment evidence, recommendation log, candidate initiative notes.
13. **Approval points.** Digital Lead confirms candidate initiatives and any score.
14. **Freshness obligations.** Maturity context rechecked at the proportionate Client Context Gate and at formal re-benchmarking.
15. **Exit criteria.** Candidate initiatives identified, or assessment closed.
16. **Closeout / handover.** Handover to Hopper if a candidate enters the Hopper.
17. **What the coworker will ask for next.** Whether to route identified gaps into the Hopper.

---

## Section 4 — Hopper / Intake

1. **Purpose.** Consolidate existing candidate initiatives into a clean, decision-ready governance canvas and remove duplicates, BAU, and unclear entries.
2. **What this stage owns.** Hopper intake and consolidation, light-touch department scoping, the Cross-Initiative Impact Check at intake.
3. **What this stage does not own.** Priority decisions, initiation, delivery, or approval.
4. **Entry criteria.** Existing Hopper items or a new candidate initiative to consolidate.
5. **Exact spin-up command.** `Spin up a Hopper / Intake consolidation session.`
6. **Authority files.** `01_governance_lifecycle/01_HOPPER_CONSOLIDATION_MODEL.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`; `00_system_control/CONTROLLED_VOCABULARY.md`.
7. **Overview workflow.** Access gate → client context → initiative reconciliation → required inputs → consolidation table → Cross-Initiative Impact Check → recommendations → closeout.
8. **Required inputs.** Jira Hopper export / screenshot / table, department notes, maturity or process findings.
9. **Coworker responsibilities.** Group duplicates, flag unclear ownership / system / process, run the Cross-Initiative Impact Check for new or materially changed items, recommend consolidation outcomes.
10. **Digital Lead responsibilities.** Confirm merges, obtain department answers, decide BAU / support routing, confirm items ready for Priority Screen.
11. **Live session checklist.** Access confirmed · reconciliation source stated · consolidation table produced · Cross-Initiative Impact Check run · outcomes recommended · write-back proposed.
12. **Required artefacts and records.** Hopper consolidation table, Cross-Initiative Impact Check output, Jira update recommendations.
13. **Approval points.** Digital Lead confirms consolidation outcomes; BAU / Reject / Merge are recommendations only.
14. **Freshness obligations.** Initiative relationships / dependencies rechecked at Hopper intake and material change.
15. **Exit criteria.** Clean candidate list confirmed ready for Hopper Priority Screen.
16. **Closeout / handover.** Internal Hopper continuity note; write-back recommendation.
17. **What the coworker will ask for next.** Whether to spin up the Hopper Portfolio Readiness Review.

---

## Section 5 — Hopper Portfolio Readiness

1. **Purpose.** Prepare the Hopper for a leadership / DRB priority discussion by organising the Jira Initiative View / Hopper priority view.
2. **What this stage owns.** Grouping review, minimum Hopper information, scoring / priority preparation, Cross-Initiative Impact Check across the portfolio.
3. **What this stage does not own.** Pack 1, Initiation Forms, delivery plans, costings, process maps, source-of-truth updates, or approval.
4. **Entry criteria.** A Hopper snapshot / export uploaded, or leadership asks for the next programme window.
5. **Exact spin-up command.** `Spin up a Hopper Portfolio Readiness Review.`
6. **Authority files.** `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`; `00_system_control/11_COWORKER_ROUTER.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`.
7. **Overview workflow.** Access gate → client context → reconciliation → required inputs → Part 1 grouping → Part 2 minimum information → Part 3 scoring → Cross-Initiative Impact Check → mandatory looping closeout.
8. **Required inputs.** Hopper export / Jira Initiative View, benchmark assessment, maturity register snapshot, prior handovers.
9. **Coworker responsibilities.** Pre-populate proposed tables from the source-read hierarchy, distinguish facts from inference, propose priority, never approve or update controlled records automatically.
10. **Digital Lead responsibilities.** Validate proposals, correct misread items, take the view to leadership / DRB, record decisions.
11. **Live session checklist.** Access confirmed · sources considered listed · grouping / minimum-information / scoring tables produced · Cross-Initiative Impact Check run · closeout produced.
12. **Required artefacts and records.** Grouped Initiative / Epic table, minimum information, priority view, Cross-Initiative Impact Check output, recommended Hopper updates.
13. **Approval points.** All updates are recommendations requiring Digital Lead approval; leadership / DRB makes the route decision.
14. **Freshness obligations.** Client strategy / maturity context rechecked at the full Client Context Gate; initiative relationships rechecked at material change.
15. **Exit criteria.** Portfolio view ready for leadership / DRB discussion.
16. **Closeout / handover.** Mandatory looping closeout; readiness statement only.
17. **What the coworker will ask for next.** Which approved initiatives to take to the DRB Priority Decision and route trigger.

---

## Section 6 — DRB Priority Decision

1. **Purpose.** Support the governed handoff from Hopper Priority Screen into the correct initiation route after a DRB priority decision.
2. **What this stage owns.** DRB decision summary, route classification recommendation, stage-gate record.
3. **What this stage does not own.** The decision itself (DRB / leadership owns it), initiation, or delivery.
4. **Entry criteria.** A DRB priority decision has been taken, or is being prepared, for a screened item.
5. **Exact spin-up command.** `Record the DRB priority decision for [initiative ID / title].`
6. **Authority files.** `01_governance_lifecycle/03_HOPPER_TO_INITIATION_STAGE_GATE.md`; `01_governance_lifecycle/02_HOPPER_PRIORITY_SCREEN_MODEL.md`; `00_system_control/CONTROLLED_VOCABULARY.md`.
7. **Overview workflow.** Access gate → reconciliation → confirm canonical DRB decision → classify route → Jira update text → closeout.
8. **Required inputs.** DRB decision, decision date, conditions, route indication, owner / sponsor / champion where known.
9. **Coworker responsibilities.** Draft the DRB decision summary and route classification recommendation; produce Jira update text; never approve the gate or assign route.
10. **Digital Lead responsibilities.** Confirm the canonical DRB decision and the route; confirm the record before progression.
11. **Live session checklist.** Access confirmed · canonical decision confirmed · route classified · required record present · Jira text drafted · write-back proposed.
12. **Required artefacts and records.** DRB decision summary, route classification, Jira update text.
13. **Approval points.** Digital Lead confirms decision and route; coworker does not approve.
14. **Freshness obligations.** DRB / approval decision valid once formally recorded unless superseded.
15. **Exit criteria.** Canonical DRB decision and route recorded; item ready for the correct route spin-up.
16. **Closeout / handover.** Readiness statement into the route-correct next stage; each approved initiative gets its own route trigger.
17. **What the coworker will ask for next.** Whether to spin up Stage 1D / Pack 1 or Implementation / Support initiation for the approved initiative.

---

## Section 7 — Development Route / Stage 1D / Pack 1

1. **Purpose.** Clarify an internal development initiative enough for DRB to approve commencement of the live development job.
2. **What this stage owns.** Stage 1D clarification, Scope Brief, Process Flow Capture Sheet, the Stage 2 exception gate test, Stage 1D closeout.
3. **What this stage does not own.** Stage 2 detail (unless the exception gate is triggered), delivery mobilisation, or approval.
4. **Entry criteria.** DRB approved a Development Epic and the Digital Lead spins up Pack 1 / Stage 1D.
5. **Exact spin-up command.** `Spin up Pack 1 for [initiative ID / title].`
6. **Authority files.** `01_governance_lifecycle/08_DEVELOPMENT_ROUTE_STAGE_1D_MODEL.md`; `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`.
7. **Overview workflow.** Access gate → full client context → reconciliation → required inputs → Stage 1D shaping → Stage 2 exception test → Completed Initiation Form (Development Approval) → closeout.
8. **Required inputs.** Approved route trigger, business reason, scope inputs, department charter where used, uploaded Initiation Form as primary source where supplied.
9. **Coworker responsibilities.** Shape scope, draft the Completed Initiation Form and supporting pack deliverables, test the Stage 2 exception gate, prepare DRB-facing text.
10. **Digital Lead responsibilities.** Confirm scope, confirm the Stage 2 exception position, take the pack to DRB, record approval.
11. **Live session checklist.** Access confirmed · client context grounded · reconciliation done · scope shaped · Stage 2 exception tested · form drafted · write-back proposed.
12. **Required artefacts and records.** Completed Initiation Form (Development Approval), Scope Brief, swimlane / process flow capture where applicable.
13. **Approval points.** DRB approves commencement; Digital Lead approves controlled updates.
14. **Freshness obligations.** Scope / exclusions valid until approved change control; owner / champion confirmed at spin-up.
15. **Exit criteria.** DRB approval to commence, with no Stage 2 exception, or Stage 2 triggered.
16. **Closeout / handover.** `Stage 1D is closed. Ready for Live Delivery spin-up.` (unless Stage 2 exception).
17. **What the coworker will ask for next.** Whether to hand over to Live Delivery or spin up Stage 2 under the exception.

---

## Section 8 — Implementation / Support Initiation

1. **Purpose.** Clarify a Hopper item enough for DRB to decide whether formal two-stage digital initiation should commence (Implementation / Support Route).
2. **What this stage owns.** Stage 1 clarification, process mapping decision, Stage 2 initiation pack preparation.
3. **What this stage does not own.** Development Route Stage 1D, delivery mobilisation, or approval.
4. **Entry criteria.** DRB approved an Implementation / Support item and the Digital Lead spins up the initiation session.
5. **Exact spin-up command.** `Spin up the Implementation / Support initiation session for [initiative].`
6. **Authority files.** `01_governance_lifecycle/07_TWO_STAGE_DIGITAL_INITIATION_MODEL.md`; `01_governance_lifecycle/04_INITIATION_FORM_INTAKE_MODEL.md`; `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`.
7. **Overview workflow.** Access gate → full client context → reconciliation → required inputs → Stage 1 clarification → process mapping decision → Stage 2 initiation pack → closeout. Stages 1 and 2 must not be collapsed.
8. **Required inputs.** Approved route trigger, business reason, system / process context, vendor / developer inputs where relevant.
9. **Coworker responsibilities.** Clarify Stage 1, decide whether process mapping is required, prepare requirements list, source-of-truth impact report and initiation pack.
10. **Digital Lead responsibilities.** Confirm scope and route, engage vendors / departments, take the pack to DRB.
11. **Live session checklist.** Access confirmed · client context grounded · reconciliation done · Stage 1 / Stage 2 kept separate · pack drafted · write-back proposed.
12. **Required artefacts and records.** Completed Initiation Form, process mapping capture sheet where required, requirements list, source-of-truth impact report.
13. **Approval points.** DRB approval at Stage 1 and Stage 2; Digital Lead approves controlled updates.
14. **Freshness obligations.** Cost / vendor quote valid until expiry or commercial change; scope valid until approved change control.
15. **Exit criteria.** Stage 1 closed / Stage 2 readiness, then Stage 2 closed / Live Delivery readiness.
16. **Closeout / handover.** `Stage 1 is closed. Ready for Stage 2 spin-up.` then `Stage 2 is closed. Ready for Live Delivery spin-up.`
17. **What the coworker will ask for next.** Whether to spin up Stage 2 or hand over to Live Delivery.

---

## Section 9 — Completed Initiation Form / Approval

1. **Purpose.** Produce the formal DRB-facing approval artefact — the Completed Initiation Form — for both routes.
2. **What this stage owns.** The Completed Initiation Form structure, the uploaded-form-as-primary-source rule, Word / `.docx` export, and the pack-deliverable rule.
3. **What this stage does not own.** The approval decision, delivery, or the optional DRB meeting-support text (which is not the formal artefact).
4. **Entry criteria.** A route stage (Stage 1D / Pack 1 or Stage 1 / Stage 2) requires the formal approval document.
5. **Exact spin-up command.** `Prepare the Completed Initiation Form for [initiative].`
6. **Authority files.** `01_governance_lifecycle/10_COMPLETED_INITIATION_FORM_OUTPUT_MODEL.md`; `01_governance_lifecycle/06_DRB_BRIEF_OUTPUT_MODEL.md` (optional meeting-support text only).
7. **Overview workflow.** Access gate → source-document checklist → build the form from controlled sources → pack deliverables → closeout.
8. **Required inputs.** Session-opening source documents; uploaded Initiation Form as primary source where supplied.
9. **Coworker responsibilities.** Build the form to the required structure, keep the pack deliverables distinct from the form, prepare the export.
10. **Digital Lead responsibilities.** Confirm content, take the form to DRB, record approval.
11. **Live session checklist.** Access confirmed · source-document checklist run · form structured · pack not collapsed into the form · write-back proposed.
12. **Required artefacts and records.** Completed Initiation Form (`.docx`), supporting pack deliverables.
13. **Approval points.** DRB approves; Digital Lead confirms the form.
14. **Freshness obligations.** DRB / approval decision valid once formally recorded unless superseded.
15. **Exit criteria.** Completed Initiation Form approved.
16. **Closeout / handover.** Route-correct readiness statement into the next stage.
17. **What the coworker will ask for next.** Whether the approved form triggers Live Delivery spin-up.

---

## Section 10 — Capex Request Session

1. **Purpose.** Prepare a programme-level capitalisation request: previous capex closeout, next capex portfolio request, evidence-safe Board narrative, client-review Board-draft deck, and controlled Hopper-to-Delivery handover.
2. **What this stage owns.** The Portfolio Capex Request Pack, Capex Readiness Tracker, Capital Efficiency Evidence, Plan Attainment Evidence, Claim Safety Table, client-review Board-draft deck.
3. **What this stage does not own.** Final spend / maturity / benefits approval, a Board-final deck while blockers remain open, or initiative-level route controls.
4. **Entry criteria.** The Digital Lead opens a capex request / capitalisation closeout-and-next-request session.
5. **Exact spin-up command.** `Spin up the Capex Request Session.`
6. **Authority files.** `01_governance_lifecycle/11_CAPEX_REQUEST_SESSION_MODEL.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`; `docs/presentation-standards/communication-and-framing-standard.md`.
7. **Overview workflow.** Access gate → full client context → reconciliation → readiness tracker → evidence sections → claim safety → Board-draft deck → handover checklist → closeout. (See the governing model for the full workflow.)
8. **Required inputs.** Prior capex position, initiative evidence, finance validation where available.
9. **Coworker responsibilities.** Consolidate the portfolio request, keep claims Board-safe, mark open dependencies as placeholders, never issue a Board-final deck while a blocker remains open.
10. **Digital Lead responsibilities.** Confirm evidence, own approval and Board issuance, clear Board-final blockers.
11. **Live session checklist.** Access confirmed · readiness tracker built · evidence sections completed · claim safety table produced · Board-draft (not final) deck · write-back proposed.
12. **Required artefacts and records.** Portfolio Capex Request Pack and its component evidence and Board-draft deck.
13. **Approval points.** Digital Lead / Board approves; no Board-final deck while blockers remain open.
14. **Freshness obligations.** Cost / vendor quote and plan attainment evidence revalidated at commercial change or review events.
15. **Exit criteria.** Portfolio Capex Request Pack ready for Board review (draft), or closeout of previous capex.
16. **Closeout / handover.** Hopper → Live Delivery Handover Checklist; each initiative still needs its own route trigger.
17. **What the coworker will ask for next.** Which approved initiatives to route individually, and whether to hand over to Live Delivery.

---

## Section 11 — Initiative Delivery / Live Implementation Control

`Placeholder — lifecycle-recognised, not operationally governed yet.` The full Stage 3 Live Delivery model is not built in this workstream.

1. **Purpose.** Move the approved initiative into controlled delivery execution and track scope, risks, blockers, and implementation evidence.
2. **What this stage owns.** Delivery mobilisation and tracking (once the model is built).
3. **What this stage does not own.** Adoption, benefits, or source-of-truth register updates.
4. **Entry criteria.** A route stage closed with a Live Delivery readiness statement and the Digital Lead spins up delivery.
5. **Exact spin-up command.** `Spin up Live Delivery for [initiative].`
6. **Authority files.** `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` (Steps 14–15, 19); `00_system_control/04_COWORKER_HANDOVER_MODEL.md`. Detailed Stage 3 Live Delivery model — `Placeholder — lifecycle-recognised, not operationally governed yet.`
7–17. Beyond mobilisation intake and the interactive gates, detailed delivery workflow is not yet governed. Do not invent workflow detail. The interactive gates, Live Session Status Board, freshness model, and closeout write-back in `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md` still apply. Live delivery status and RAID are revalidated each fortnightly delivery cycle or material event.

---

## Section 12 — Completion and Handover

1. **Purpose.** Close a stage or delivery cleanly, hand over only what the closing stage agreed, and propose the controlled write-back.
2. **What this stage owns.** The stage closeout / handover checkpoint and the closeout write-back.
3. **What this stage does not own.** Next-stage planning detail.
4. **Entry criteria.** A material stage or delivery is ready for closeout.
5. **Exact spin-up command.** `Close out and hand over the session for [initiative].`
6. **Authority files.** `00_system_control/04_COWORKER_HANDOVER_MODEL.md`; `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`; `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`.
7. **Overview workflow.** Confirm stage outcome → produce Stage Closeout Handover → propose controlled write-back → Knowledge Capture / CDO QA / Source-of-Truth recommendations → Digital Lead approval.
8. **Required inputs.** What was agreed, delivered, approved, evidenced, and left open in the closing stage.
9. **Coworker responsibilities.** Produce the closeout and the write-back covering all required fields; label all write-backs as recommendations.
10. **Digital Lead responsibilities.** Approve, defer, or accept-the-gap on the write-back; confirm handover.
11. **Live session checklist.** Closeout sections produced · write-back proposed · knowledge capture run · handover state set · Digital Lead approval recorded.
12. **Required artefacts and records.** Stage Closeout Handover, controlled write-back recommendation.
13. **Approval points.** Session is not closed until the Digital Lead approves / defers / accepts the write-back.
14. **Freshness obligations.** Source-of-truth impact rechecked at material change, go-live, and closeout.
15. **Exit criteria.** Write-back approved / deferred / gap accepted and handover state set to `Closed and handed over`.
16. **Closeout / handover.** Route-correct readiness statement into the next stage or lifecycle coworker.
17. **What the coworker will ask for next.** Whether to hand over to Adoption & Benefits or Source-of-Truth Control.

---

## Section 13 — Adoption and Benefits

`Placeholder — lifecycle-recognised, not operationally governed yet.` The Adoption and Benefits model is not built in this workstream.

1. **Purpose.** Confirm controlled use, competence, benefits evidence, ownership, and closeout readiness after go-live, and confirm / revise / reject any proposed maturity movement.
2. **What this stage owns.** Adoption and benefits confirmation (once modelled), including confirming maturity impact.
3. **What this stage does not own.** Delivery execution or approved maturity-register mutation (Source-of-Truth control owns the register).
4. **Entry criteria.** Go-live handover received and the Digital Lead spins up adoption.
5. **Exact spin-up command.** Not yet governed. Do not spin up.
6. **Authority files.** Adoption and Benefits model — `Placeholder — lifecycle-recognised, not operationally governed yet.`
7–17. Not operationally governed yet. Do not invent workflow detail. Note the maturity boundary: delivery closeout may propose only a **provisional** maturity impact; the Adoption and Benefits stage confirms, revises, or rejects the movement using operational-use, ownership, adoption, and benefit evidence, subject to Source-of-Truth and Digital Lead approval.

---

## Section 14 — Source-of-Truth Control

1. **Purpose.** Maintain source-of-truth artefact integrity when lifecycle changes occur — registers, process flows, decision records, superseded / active artefact control.
2. **What this stage owns.** Source-of-truth registers and artefact control, and approval routing for register changes (including any approved maturity-register update).
3. **What this stage does not own.** Initiative approval, delivery, or invented scores / maturity movement.
4. **Entry criteria.** A material change, go-live, or closeout impacts a source-of-truth artefact.
5. **Exact spin-up command.** `Spin up a Source-of-Truth impact review for [initiative / artefact].`
6. **Authority files.** `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`; `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`; `00_system_control/12_INTERACTIVE_GOVERNED_SESSION_PROTOCOL.md`.
7. **Overview workflow.** Access gate → full client context → reconciliation → artefact impact check → recommended register updates → Digital Lead / authorised reviewer approval.
8. **Required inputs.** Affected artefacts, change trigger, evidence.
9. **Coworker responsibilities.** Run the artefact impact check, recommend register updates, never mutate a controlled register.
10. **Digital Lead responsibilities.** Approve register changes; authorise the reviewer where required.
11. **Live session checklist.** Access confirmed · artefacts identified · impact check run · updates recommended · approval recorded.
12. **Required artefacts and records.** Artefact impact report, recommended register updates.
13. **Approval points.** Any live register change requires Source-of-Truth Artefact Controller and Digital Lead / authorised reviewer approval.
14. **Freshness obligations.** Source-of-truth impact rechecked at material change, go-live, and closeout.
15. **Exit criteria.** Impacted registers updated (on approval) or gap accepted.
16. **Closeout / handover.** Governance update checkpoint; may create new Hopper candidates.
17. **What the coworker will ask for next.** Whether any residual gap should return to Digital Governance & Strategy or the Hopper.

---

## Section 15 — Programme Closeout / Learning

1. **Purpose.** Update programme artefacts, registers, lessons learned, and reporting as the lifecycle closes or creates new candidates.
2. **What this stage owns.** Lessons learned and programme reporting updates (as a lifecycle-recognised activity under source-of-truth / governance control).
3. **What this stage does not own.** New initiative approval or delivery.
4. **Entry criteria.** Adoption / source-of-truth control complete, or a programme learning point is captured.
5. **Exact spin-up command.** `Spin up a Programme closeout / learning capture.`
6. **Authority files.** `00_system_control/06_KNOWLEDGE_CAPTURE_AND_SOURCE_UPDATE_RULE.md`; `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`; `00_system_control/05_DIGITAL_GOVERNANCE_PROGRAMME_LIFECYCLE.md` (Step 18).
7. **Overview workflow.** Access gate → reconciliation → knowledge capture review → recommended updates → Digital Lead approval.
8. **Required inputs.** Closeout records, lessons learned, programme report inputs.
9. **Coworker responsibilities.** Run the Knowledge Capture Review, recommend durable updates, never mutate controlled records.
10. **Digital Lead responsibilities.** Approve durable updates and reporting.
11. **Live session checklist.** Access confirmed · knowledge capture run · durable items identified · updates recommended · approval recorded.
12. **Required artefacts and records.** Knowledge capture table, lessons learned, programme report updates.
13. **Approval points.** Digital Lead approves any durable update.
14. **Freshness obligations.** Recheck source-of-truth and client context at the proportionate gates.
15. **Exit criteria.** Durable learning captured (on approval); new candidates routed to Hopper where relevant.
16. **Closeout / handover.** Governance update checkpoint closes the lifecycle or creates new Hopper candidates.
17. **What the coworker will ask for next.** Whether any learning creates a new candidate initiative for the Hopper.

---

## Example spin-up commands

- `Spin up a Hopper Portfolio Readiness Review.`
- `Spin up Pack 1 for [initiative ID / title].`
- `Spin up the Implementation / Support initiation session for [initiative].`
- `Spin up the Capex Request Session.`
- `Spin up Live Delivery for [initiative].`
- `Resume the suspended session for [initiative].`
- `Run initiative reconciliation before opening this session.`

Whatever you spin up, the coworker begins with the Runtime Access Confirmation Gate, the proportionate Client Context Gate, the Initiative Reconciliation Gate, and the Required Inputs Gate before substantive stage work.

## Future client-context and maturity layer

The following are referenced by this manual but are `Placeholder — lifecycle-recognised, not operationally governed yet.`:

- Client Digital Governance Profile model
- Client Governance Artefact Register model
- Maturity Improvement Loop model
- Formal Re-Benchmark / Maturity Snapshot model

Until these are governed, the Client Context Gate is satisfied by a controlled client-context artefact or explicit Digital Lead confirmation, and no maturity score is calculated or maturity position updated by the coworker.
