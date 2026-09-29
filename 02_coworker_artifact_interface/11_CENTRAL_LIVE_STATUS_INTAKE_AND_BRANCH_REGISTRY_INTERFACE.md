# Central Live Status Intake and Branch Registry Interface

**Interface ID:** ART-CENTRAL-LIVE-STATUS-BRANCH-REGISTRY  
**Revision:** r1  
**Status:** reusable client-copy interface; populate only in a private client repository  
**Method authority:** `00_system_control/17_CENTRAL_LIVE_STATUS_INTAKE_AND_BRANCH_ROUTING_STANDARD.md`

## Central Live Status thread starter

Copy this starter into the client-approved central thread and replace bracketed values with client-controlled values.

```text
# Client Live Status

Client: [client identifier]
Approved private repository: [repository/path]
Approved reporting source: [normally main, or client-approved equivalent]
Branch registry path/ref: [client-controlled path and revision]
Last registry verification: [UTC date/time and verifier]

Update sender:
Update date/time:
Update type: status | decision | action | RAID | initiative/workstream context | artefact | mixed
Initiative/workstream reference(s):
Source/evidence links:
Requested decision or safe next action:

Routing control:
- Read the branch registry before processing.
- Bind each reference to one canonical path and branch.
- Stop and record a blocker if any binding is missing, stale, divergent, undocumented or ambiguous.
- Split mixed updates into separate initiative/workstream change sets.
- Commit each change set only to its controlled branch.
- The central thread is an intake/router and does not replace initiative records.
- Report only after the approved reporting source or client-approved exposure is current.
```

## Client-level branch registry

Maintain one current registry in the client repository. Each row is a binding decision, not a suggestion.

| Field | Required content |
|---|---|
| Client | Client identifier |
| Initiative/workstream name | Stable name and identifier |
| Classification/contract/programme grouping | Approved grouping |
| Controlled path | Canonical folder/path |
| Canonical branch | One approved working branch |
| Branch status versus main | In sync / ahead / behind / diverged / unknown, with checked commit/date |
| Duplicate/stale/non-canonical branches | Names, refs and disposition; use “none recorded” when empty |
| Reporting visibility | Not visible / branch-only / exposed by approved process / merged to reporting source |
| Last verified date | UTC date and verifier |
| Blocker/decision required | Binding decision, owner and due date, or “none” |
| Safe next action | Exact non-destructive next step |

Recommended supporting fields are EIDF path, PEP/control-record path, programme action tracker reference, thread reference, registry row status and last reconciled commit. Do not add a second status ledger.

## Initiative/workstream creation checklist

Before accepting status updates for a newly created item, record:

- [ ] controlled path created or confirmed;
- [ ] canonical branch created or confirmed;
- [ ] registry row added and approved;
- [ ] branch status versus reporting source checked;
- [ ] duplicate/stale/non-canonical branches checked;
- [ ] EIDF/controlled initiative record linked;
- [ ] programme action tracker and thread tracker updated;
- [ ] central Live Status routing instruction posted;
- [ ] first update held until the binding gate passes.

## Controlled values

**Branch status:** in sync, ahead, behind, diverged, missing, stale, undocumented, ambiguous.  
**Reporting visibility:** branch-only, pending reconciliation, exposed by approved process, merged to reporting source, blocked.  
**Safe actions:** verify, reconcile, record decision, create approved branch, merge through approved review, or escalate. Deletion, force-push and destructive history changes are never a safe default.

## Central thread closeout

Every update records the registry revision read, affected initiative/workstream rows, target branches, separate change sets, approval/merge state, tracker actions and unresolved decisions. The client Live Status thread may summarize linked outcomes but never stores a replacement EIDF or programme ledger.
