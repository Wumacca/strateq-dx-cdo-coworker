# Hopper Priority Screen Model

> **Meeting surface — read first.** "Priority Screen" means the **Jira Initiative View / Hopper priority view** (the organised Hopper / Initiative View screens in Jira / Jira Product Discovery). It is **not** a separate DRB Priority Screen document. The Hopper Portfolio Readiness Review prepares this view for leadership / DRB discussion and does not produce a separate artefact (DRB Priority Screen, DRB pack, or leadership paper) unless the Digital Lead explicitly requests one. The full review workflow is governed by `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`. Any written table or meeting-support text below is produced only where a written output is explicitly requested by the Digital Lead.

## Purpose

The Hopper Priority Screen prepares candidate Hopper items for leadership / Digital Review Board priority discussion by organising the Jira Initiative View / Hopper priority view.

It does not approve initiatives.

It does not replace the Initiation Form.

It answers one question:

> Is this item important enough for leadership / DRB to approve the correct next route trigger?

## Stage Position

```text
Hopper consolidation complete
↓
Candidate item ready for light priority screening
↓
Hopper Priority Screen
↓
DRB priority discussion
↓
Canonical DRB Priority Decision recorded
```

## Controlled Vocabulary

Use `00_system_control/CONTROLLED_VOCABULARY.md` for:

- Canonical DRB Priority Decisions
- Business Priority Signal labels
- current Jira status labels

Do not invent variants.

## Input Required

For each item, use available information:

- Jira ID
- Title
- Department / business area
- Request type
- Short description
- Why raised
- Known system affected
- Known process affected
- Urgency
- Safety & Duty Holder relevance
- Regulatory / Reputational relevance
- Financial / Commercial exposure
- Linked maturity track, if known
- Attachments / evidence, if provided
- Current comments

## Scoring Role

Priority screening supports DRB discussion.

It must not automatically approve or reject an item.

Business Priority Signal is qualitative only and must follow `CONTROLLED_VOCABULARY.md`.

Claude must not invent numeric scores, weightings, or a 1–5 scale. Where a Digital Lead-approved scoring model, team-returned charter score, or Jira-entered score exists, Claude may organise, display, summarise, and challenge the score, but must not create or alter scores without Digital Lead approval.

Recommended priority dimensions:

- Safety & Duty Holder relevance
- Regulatory / Reputational relevance
- Financial / Commercial exposure

Optional contextual factors:

- Operational efficiency
- Client confidence
- Maturity improvement
- Delivery dependency
- Existing programme alignment

## Valid Recommended DRB Decisions

Use the canonical DRB priority decision set from `00_system_control/CONTROLLED_VOCABULARY.md`.

| Decision | Meaning |
|---|---|
| Progress to Approved Route Trigger | Item approved by leadership / DRB to move to the next route-correct stage (Pack 1 / Stage 1D, Initiation Form / Implementation Route, selection/support route, or existing delivery control as applicable) |
| Clarify Before Progression | Targeted clarification is required before progression |
| Merge / Duplicate | Item should be joined to another Hopper item or initiative |
| Defer | Relevant but not for current programme window |
| Reject | No sufficient business case to progress |
| Move to BAU Support | Not a governed initiative |
| Hold for Future Review | Keep visible but do not progress now |

## Optional Written Output: Hopper Priority Screen

Use this format only where the Digital Lead explicitly requests a written Hopper Priority Screen output. The default meeting surface remains the Jira Initiative View / Hopper priority view.

Use this format:

| Item | Request Type | Business Priority Signal | Maturity / System Link | Missing Basic Info | Recommended DRB Decision | Questions Before DRB | Jira Update |
|---|---|---|---|---|---|---|

## Business Priority Signal

Use the labels from `CONTROLLED_VOCABULARY.md`:

- High
- Medium
- Low
- Unclear

Add a short reason.

Example:

```text
Medium — clear operational workflow issue, but financial / regulatory exposure not yet evidenced.
```

## Missing Basic Info

List only information needed for DRB priority decision.

Do not request full initiation-form detail at this stage.

## Questions Before DRB

Questions should be short and directed to the right party:

- initiator
- department lead
- digital champion
- system owner
- vendor
- developer
- commercial / finance

## Optional DRB Meeting-Support Text

This is not the formal approval artefact and is produced only when the Digital Lead explicitly asks for written meeting-support text. It does not replace Jira as the default meeting surface, and it does not replace the Completed Initiation Form where an approval document is required.

For items where the Digital Lead has asked for written meeting-support text, produce:

```markdown
### [Initiative / Hopper Item]

**Decision required:** [canonical DRB priority decision]

**Why this matters:** [short business reason]

**Known exposure:** [safety / regulatory / reputational / financial / operational]

**Current uncertainty:** [missing basic facts]

**Recommended position:** [recommendation for DRB discussion]

**Questions for DRB:**
- [question]
- [question]
```

## Physical Actions for Digital Lead

The Digital Lead should:

- validate the priority screen
- correct any misunderstood item
- obtain missing basic answers where possible
- take the item to DRB if ready
- record DRB decision
- update Jira status/comments

## Feedback Required from Digital Lead

Return to AI:

- DRB decision
- decision date
- conditions
- amendments requested
- route agreed
- owner/sponsor/champion confirmation
- next required stage

## Next Lifecycle Trigger

If DRB approves progression, the item moves to Initiation Form stage.

If not approved, it is clarified, deferred, rejected, merged, moved to BAU support, or held for future review.
