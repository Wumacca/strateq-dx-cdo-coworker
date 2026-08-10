# Client Context Manifest Schema

## Status

Reusable schema. Authority for the structure, field meanings, allowed values, and validation rules of a client context manifest.

> The schema is reusable. The manifest instance is client-specific and must live in the client workspace, not in the DX Build repo.

This schema is governed by, and read together with, `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`.

## Purpose

The client context manifest is the addressing and control record for one client workspace. It tells the coworker, and any future application, where the client's programme truth lives, which files are required, who confirms status, and what the coworker is permitted to write.

Without a loaded, schema-valid manifest, the Active Client Workspace Resolution Gate fails closed and no client programme status may be asserted.

## Instance Location

| Item | Position |
|---|---|
| Schema (this file) | DX Build repository, `00_system_control/CLIENT_CONTEXT_MANIFEST_SCHEMA.md` |
| Manifest instance | Client workspace, `<client_repo_root>/00_system_control/CLIENT_CONTEXT_MANIFEST.md` or `.json` |
| Registry of manifests | Local environment configuration or future-app tenancy configuration. An anonymised example only is held at `00_system_control/CLIENT_CONTEXT_REGISTRY.example.json` |

A populated manifest for a real client must never be committed to the DX Build repository.

## Required Fields

All fields listed below are required. A manifest missing any required field is invalid and the resolution gate fails closed.

| # | Field | Type | Meaning |
|---:|---|---|---|
| 1 | `client_id` | string | Stable machine identifier for the client workspace. Used for addressing, registry keys, and folder naming |
| 2 | `client_name` | string | Human-readable client name used in session declarations and output headers |
| 3 | `workspace_type` | enum | The kind of workspace this manifest addresses |
| 4 | `client_repo_root` | path | Absolute root of the client workspace. All other paths in the manifest resolve relative to this root unless absolute |
| 5 | `programme_status_path` | path | Path to the client's live controlled status surface, `PROGRAMME_STATUS.md` |
| 6 | `artefact_register_path` | path | Path to the controlled artefact register |
| 7 | `decision_register_path` | path | Path to the decision register |
| 8 | `evidence_register_path` | path | Path to the evidence register of accepted delivered artefacts |
| 9 | `handover_register_path` | path | Path to the handover register |
| 10 | `jira_project_keys` | array of string | The client-facing Jira project keys in scope. Reference only — Claude has no live Jira connection |
| 11 | `sharepoint_root` | string (URL or path) | The controlled artefact and evidence store root. Reference only — Claude has no live SharePoint connection |
| 12 | `confirmation_authority` | string | The named role that confirms programme status for this client. Normally `Digital Lead` |
| 13 | `write_mode` | enum | What the coworker or app is permitted to write into this workspace |
| 14 | `status` | enum | Whether this manifest may be used to resolve a session |
| 15 | `last_validated` | date (`YYYY-MM-DD`) | Date the manifest was last validated against the actual workspace |
| 16 | `validation_owner` | string | The named role accountable for revalidating this manifest |

## Field Definitions, Allowed Values and Validation Rules

### 1. `client_id`

- **Meaning.** Stable machine identifier. Does not change when the client's trading name changes.
- **Allowed values.** Lowercase alphanumeric and underscore only, `^[a-z0-9_]+$`, 3–64 characters.
- **Validation.** Must be unique across the registry. Must match the final path segment of `client_repo_root` unless a deliberate alias is recorded in the workspace.

### 2. `client_name`

- **Meaning.** Human-readable name used in session declarations, gate output, and document headers.
- **Allowed values.** Free text, 1–120 characters.
- **Validation.** Must be present and non-empty. Must not be used as an addressing key — addressing uses `client_id`.

### 3. `workspace_type`

- **Meaning.** The kind of workspace being addressed, so the coworker applies the right expectations.
- **Allowed values.** `client_programme` | `client_pilot` | `internal_demo` | `example`.
- **Validation.** `example` is the only value permitted for a manifest or registry entry held in the DX Build repository. A DX Build file carrying any other value is a defect.

### 4. `client_repo_root`

- **Meaning.** Absolute root of the client workspace.
- **Allowed values.** Absolute filesystem path or repository URI.
- **Validation.** Must exist and be readable at resolution time. If unreadable, the gate result is **Access gap** and the session stops. Must not point inside the DX Build repository.

### 5. `programme_status_path`

- **Meaning.** Path to the client's `PROGRAMME_STATUS.md`, the live controlled status surface.
- **Allowed values.** Path, absolute or relative to `client_repo_root`. Conventionally `00_system_control/PROGRAMME_STATUS.md`.
- **Validation.** Mandatory for every client programme session. The file must exist and be loadable before any client programme status is asserted. It must be derived from `00_system_control/PROGRAMME_STATUS_TEMPLATE.md` and governed by `00_system_control/PROGRAMME_STATUS_RULES.md`.

### 6. `artefact_register_path`

- **Meaning.** Controlled artefacts, their revisions, and their active / superseded state.
- **Allowed values.** Path, absolute or relative to `client_repo_root`.
- **Validation.** Must resolve for source-of-truth, closeout, and artefact-impact sessions. A missing register for those session types is an access gap, not a silent omission.

### 7. `decision_register_path`

- **Meaning.** Decisions, decision basis, approver, and date.
- **Allowed values.** Path, absolute or relative to `client_repo_root`.
- **Validation.** Must resolve for approval, DRB, and capex sessions.

### 8. `evidence_register_path`

- **Meaning.** Accepted delivered artefacts and the evidence pointers that support programme status records.
- **Allowed values.** Path, absolute or relative to `client_repo_root`.
- **Validation.** Must resolve wherever an evidenced claim is produced. The accepted delivered artefact indexed here is the evidence basis; the programme status record points to it, and does not replace it.

### 9. `handover_register_path`

- **Meaning.** Issued handovers, their state, and whether they have become stale.
- **Allowed values.** Path, absolute or relative to `client_repo_root`.
- **Validation.** Must resolve for handover sessions and for any session that changes a programme status position on which a downstream handover depends.

### 10. `jira_project_keys`

- **Meaning.** Client-facing Jira project keys in scope for this workspace.
- **Allowed values.** Array of strings, each `^[A-Z][A-Z0-9]{1,9}$`. May be an empty array where no Jira project is in scope.
- **Validation.** Reference only. Presence of a key does not imply access. Claude has no live Jira connection and must never claim one.

### 11. `sharepoint_root`

- **Meaning.** Root of the controlled artefact and evidence store.
- **Allowed values.** URL or path string. May be an empty string where SharePoint is not the client's store.
- **Validation.** Reference only. Presence does not imply access. Claude has no live SharePoint connection and must never claim one.

### 12. `confirmation_authority`

- **Meaning.** The named role that confirms programme status for this client.
- **Allowed values.** Free text role name. Default and expected value: `Digital Lead`.
- **Validation.** Must name a role, not an individual's recollection. Confirmation by this authority is a control act against the accepted artefact; it is not itself the evidence basis.

### 13. `write_mode`

- **Meaning.** What the coworker or future app may write into this workspace.
- **Allowed values.**

| Value | Meaning |
|---|---|
| `proposal_only` | **Default.** The coworker reads and proposes controlled updates. It writes nothing. Every update is labelled `Recommended update — requires Digital Lead approval.` |
| `approved_write` | The coworker may write a specific update to a named client workspace file **after** the Digital Lead has approved that specific update. It confers no standing write authority and never extends to Jira, SharePoint, or Omega 365 |
| `read_only` | The coworker reads only. It must not propose controlled updates for this workspace |

- **Validation.** Default is `proposal_only`. A manifest that omits `write_mode` is treated as `proposal_only`. Raising `write_mode` to `approved_write` requires a recorded Digital Lead decision in the client decision register. `write_mode` never authorises a write to a live client system.

### 14. `status`

- **Meaning.** Whether this manifest may be used to resolve a session.
- **Allowed values.** `active` | `draft` | `suspended` | `archived`.
- **Validation.** Only `active` may resolve a session. `draft`, `suspended`, and `archived` fail the resolution gate closed; the coworker states the status and stops.

### 15. `last_validated`

- **Meaning.** The date the manifest was last checked against the actual workspace — paths resolve, required files exist, keys and roles still correct.
- **Allowed values.** `YYYY-MM-DD`.
- **Validation.** Must be present. Where the manifest has not been validated within the client's agreed revalidation cadence, the coworker flags it as `Revalidation due` at the resolution gate and asks the Digital Lead whether to proceed. A stale manifest is a flag, not an automatic stop, unless a required path fails to resolve.

### 16. `validation_owner`

- **Meaning.** The named role accountable for revalidating this manifest.
- **Allowed values.** Free text role name. Normally `Digital Lead`.
- **Validation.** Must be present and must name a role.

## Structural Rules

1. All required fields must be present. A missing required field invalidates the manifest.
2. Unknown fields are permitted but ignored by the resolution gate. They must not carry programme truth.
3. The manifest is an addressing and control record. It must not contain programme status, figures, costs, maturity scores, initiative lists, approval names, or evidence content. Those belong in `PROGRAMME_STATUS.md` and the registers.
4. One manifest addresses exactly one client workspace. Multi-client manifests are not permitted.
5. Path fields must not resolve into the DX Build repository.

## Validation Checklist

| # | Check | Pass condition |
|---:|---|---|
| 1 | All 16 required fields present | Yes |
| 2 | `client_id` pattern and uniqueness | `^[a-z0-9_]+$`, unique in registry |
| 3 | `workspace_type` valid, and `example` if held in DX Build | Yes |
| 4 | `client_repo_root` exists, readable, outside DX Build | Yes |
| 5 | `programme_status_path` resolves to a template-derived `PROGRAMME_STATUS.md` | Yes |
| 6 | Register paths required by the session type resolve | Yes, or gap named and accepted |
| 7 | `jira_project_keys` well-formed; no implied live access | Yes |
| 8 | `confirmation_authority` names a role | Yes |
| 9 | `write_mode` valid; defaults to `proposal_only` | Yes |
| 10 | `status` is `active` for a session to proceed | Yes |
| 11 | `last_validated` present and within cadence, or flagged | Yes |
| 12 | `validation_owner` present | Yes |
| 13 | Manifest carries no programme truth | Yes |

## Boundary

This schema defines structure only. It does not extend AI authority, does not create a live connection to any client system, and does not override `00_system_control/12_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`, `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md`, or `00_system_control/OPERATING_RULES.md`.
