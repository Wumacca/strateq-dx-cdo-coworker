# Decision Feedback Templates

## Priority Gate Feedback

```text
Item:
Review date:
Decision:
Reason:
Conditions:
Clarification needed:
Owner:
Champion:
Next status:
Next action:
```

## Form Review Feedback

```text
Initiative:
Review date:
Decision:
Route:
Cost position:
Conditions:
Scope changes:
Risks:
Next status:
Execution workspace:
```

## Jira Update Request

```text
Item:
Current status:
Target status:
Comment needed:
Fields to update:
Links or attachments:
```

## Output Rule

After receiving decision feedback, the AI coworker should produce a short decision summary and Jira-ready text. A next-stage starter checklist is produced only when the Digital Lead explicitly spins up the next stage, by the receiving stage, per the stage segregation and starter-checklist timing rules in `00_system_control/07_GOVERNED_WORKFLOW_LOOPING_STANDARD.md`. When closing a stage, produce the stage closeout and readiness statement only.

## Central Live Status routing fields

Decision and feedback submissions must identify the canonical initiative/workstream path and branch registry row. The central thread reads the registry before routing, stops on an unbound or ambiguous branch, and records the binding decision before any controlled write or external-system update.
