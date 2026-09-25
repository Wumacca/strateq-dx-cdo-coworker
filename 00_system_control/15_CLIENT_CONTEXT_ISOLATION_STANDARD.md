# Client Context Isolation Standard

## Status

Mandatory global authority for client separation, repository boundaries and fail-closed handling. This file applies to every model, tool, skill, project and governed session.

## Core rule

One client equals one private client repository and one bound working context. Client branches, folders or chat threads inside a shared repository are not acceptable isolation boundaries.

The public Strateq DX method repository contains reusable method only. It must contain zero client data.

The repository link is intentionally one-way: each private client's `METHOD_BASELINE.md` pins the approved public-method commit, while the public method repository never enumerates clients or links back to private client repositories. The client root instructions and `00_PROJECT_HOME.md` route the Coworker to that client's files and initiative paths.

## Session binding gate

Before reading or creating client content, the coworker must resolve and state:

| Binding field | Required value |
|---|---|
| Client ID | Exact ID from the client repository |
| Client name | Exact controlled name |
| AI Project / workspace | Exact controlled project or local workspace name |
| Memory boundary | Project-only, disabled or not applicable; never cross-project/client memory |
| Method repository | Approved read-only method repository and baseline commit |
| Client repository | Exactly one approved private repository |
| Write target | The bound client repository and active controlled branch |
| Thread and initiative path | Exact active thread plus one initiative folder, or an approved portfolio/reporting path |
| Prohibited sources | Every other client repository, workspace, attachment set and thread |

No substantive work begins until the binding is complete.

## Repository permissions

During client work:

- **Read:** the public Strateq DX method repository and the bound private client repository.
- **Write:** the bound private client repository only, through a controlled branch or approved direct update.
- **Never read or write:** any other client's repository, files, project knowledge, chat exports or evidence.
- **Never write client data:** to the method repository, reusable Coworker skill, shared prompt, benchmark pack or another client repository.

Reusable artefacts (templates, schemas, interfaces and workbooks) are resolved **read-only** from the method repository through the revision-handshake in `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md` (latest **approved** revision against the client `METHOD_BASELINE.md`, fail-closed on a stale, missing, ambiguous or incompatible baseline). The populated output is written **only** to the bound client repository. There is no client write-back path into the method repository: no populated artefact, client status or client-specific evidence is ever committed to Strateq DX. A reusable improvement enters the method repository only as an abstracted, client-free change under zero-crossover control 8 below and Digital Lead approval.

## Zero-crossover controls

The coworker must:

1. verify the client marker in `CLIENT_BOUNDARY.md` before every material session;
2. verify that the active AI Project/workspace and thread match the boundary marker;
3. use project-only memory or disable memory where persistent memory could import context from another project/client;
4. check each supplied source against the bound client and initiative;
5. keep provenance for every fact used;
6. search only inside the two allowed repositories and the sources supplied for the active client session;
7. refuse cross-client comparisons unless the Digital Lead supplies an expressly anonymised, approved dataset in a non-client method workstream;
8. abstract lessons before proposing a method update, removing names, identifiers, commercial terms, dates, locations and traceable client facts;
9. require Digital Lead approval before an abstracted lesson is written to the method repository;
10. reset the client binding before moving to another client.

Project instructions and repository allowlists are procedural safeguards, not substitutes for technical access control. Where a connector or execution environment can access multiple client repositories, use repository-scoped credentials or an environment restricted to the bound client wherever the platform supports it. If another client's content appears in injected memory or session context, treat that as a boundary mismatch and stop without using or reproducing it.

## Contamination test

Stop immediately if any of the following occurs:

- a source names a different client;
- a repository or path is outside the allowlist;
- the client identity is missing or ambiguous;
- the active AI Project/workspace, memory boundary or thread does not match `CLIENT_BOUNDARY.md`;
- content appears copied from another client;
- another client's content appears in injected memory or session context;
- a requested output would expose another client's facts;
- a method change contains identifiable client data;
- the coworker cannot establish provenance.

Use this response:

> `STOPPED — client-boundary mismatch. No affected content has been reused or written. Digital Lead confirmation is required.`

Record the source, mismatch and affected proposed output without reproducing the conflicting client content.

## Client repository minimum controls

Each private client repository must contain:

- `CLIENT_BOUNDARY.md`
- `00_PROJECT_HOME.md`
- `CLIENT_CONTEXT.md`
- `SOURCE_OF_TRUTH.md`
- `METHOD_BASELINE.md`
- `PUBLICATION_REGISTER.md`
- root `AGENTS.md`
- one controlled initiative folder per initiative

`CLIENT_BOUNDARY.md` must state the exact client ID, repository, classification, approved AI Project/workspace, memory boundary, allowed method repository and commit, prohibited crossover rule and publication boundary.

`00_PROJECT_HOME.md` must state the exact AI Project/workspace name, purpose and client boundary, permitted shared sources, thread naming convention, live working authority and output locations. It is navigation only and must not become a parallel source of initiative status.

`METHOD_BASELINE.md` must pin the approved method repository and commit and, per reusable artefact adopted, the pinned revision and approving method commit resolved through `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md`. A pinned revision changes only through a Digital-Lead-approved update to this file (see the client-adoption reference pattern in `16`).

## Publication boundary

An external client store such as SharePoint may be a manual publication destination without being a connected working source. The client repository remains the working authority until the client profile explicitly changes it. A publication is recorded only after the Digital Lead confirms the upload.

## Audit evidence

Every material closeout records:

- bound client and repository;
- bound AI Project/workspace, memory-boundary status and thread/path;
- source files used;
- files changed;
- method baseline commit;
- any boundary exception or stop;
- release/publication status.

No exception to client separation may be inferred by the coworker.
