# Hopper Priority Screen Model

## Purpose

The Hopper Priority Screen prepares candidate Hopper items for Digital Review Board priority discussion.

It does not approve initiatives.

It does not replace the Initiation Form.

It answers one question:

> Is this item important enough to progress into formal initiation due diligence?

## Stage Position

```text
Hopper consolidation complete
↓
Candidate item ready for light priority scoring
↓
Hopper Priority Screen
↓
DRB priority discussion
↓
Progress / clarify / defer / reject / BAU / merge
```

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

Priority scoring supports DRB discussion.

It must not automatically approve or reject an item.

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

| Decision | Meaning |
|---|---|
| Progress to Initiation Form | Item deserves formal due diligence |
| Clarify Before DRB | Missing basic information prevents priority discussion |
| Clarify After DRB | DRB sees relevance but requires targeted answers before progression |
| Merge / Duplicate | Item should be joined to another Hopper item or initiative |
| Defer | Relevant but not for current programme window |
| Reject | No sufficient business case to progress |
| Move to BAU Support | Not a governed initiative |
| Hold for Future Review | Keep visible but do not progress now |

## AI Output: Hopper Priority Screen

Use this format:

| Item | Request Type | Business Priority Signal | Maturity / System Link | Missing Basic Info | Recommended DRB Decision | Questions Before DRB | Jira Update |
|---|---|---|---|---|---|---|

## Business Priority Signal

Use one of:

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

## DRB Brief Format

For items going to DRB, produce:

```markdown
### [Initiative / Hopper Item]

**Decision required:** Progress / clarify / defer / reject / BAU / merge

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
