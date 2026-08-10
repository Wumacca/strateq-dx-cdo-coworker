# Archive Note

## Purpose

This note is the archive index for the DX Build repository. It records what has been held in `_archive/`, and what has been removed and why.

DX Build is a reusable method repository. It holds standards, schemas, templates, routing rules, interface contracts, generic anonymised examples, and coworker method files. Client programme evidence is not archived here — it belongs in the relevant client workspace, governed by `00_system_control/15_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`.

## Current Archive Contents

None. `_archive/` holds no source packs.

## Removal Record

Client-specific source archive removed from DX Build. Client programme evidence belongs in the relevant client workspace. Removed archive: `_archive/source_zips/THREE60_capitalisation_markdown_pack.zip`. Intended client workspace: `Clients/three60_energy`. Hash recorded in commit context.

| Item | Value |
|---|---|
| Removed path | `_archive/source_zips/THREE60_capitalisation_markdown_pack.zip` |
| Intended client workspace | `Clients/three60_energy` |
| Reason | Client-specific programme evidence must not be stored in the reusable DX Build repository |
| Contents inspected | No. The archive was not extracted, opened, or copied into any DX Build file |
| Hash | Recorded in the commit context for the removal commit |

The archive remains recoverable from git history at the removal commit's parent. Recovering it into DX Build is not permitted; recover it into the client workspace instead.

## Rule

Do not add client-specific source packs, evidence exports, Board packs, capitalisation packs, delivery evidence, or programme records to this repository, in `_archive/` or anywhere else. Route them to the active client workspace.

This restates the storage boundary in `00_system_control/OPERATING_RULES.md` and `00_system_control/15_CLIENT_WORKSPACE_INTERFACE_STANDARD.md`. It does not create a new rule.
