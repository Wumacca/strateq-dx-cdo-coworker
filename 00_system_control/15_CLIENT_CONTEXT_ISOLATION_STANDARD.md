# Client Context Isolation Standard

## Status

Mandatory global authority for client separation, repository boundaries and fail-closed handling. This file applies to every model, tool, skill, project and governed session.

## Core rule

One client equals one private client repository and one bound working context. Client branches, folders or chat threads inside a shared repository are not acceptable isolation boundaries.

The public Strateq DX method repository contains reusable method only. It must contain zero client data.

## Session binding gate

Before reading or creating client content, the coworker must resolve and state:

| Binding field | Required value |
|---|---|
| Client ID | Exact ID from the client repository |
| Client name | Exact controlled name |
| Method repository | Approved read-only method repository |
| Client repository | Exactly one approved private repository |
| Write target | The bound client repository and active controlled branch |
| Initiative path | One initiative folder, or an approved portfolio/reporting path |
| Prohibited sources | Every other client repository, workspace, attachment set and thread |

No substantive work begins until the binding is complete.

## Repository permissions

During client work:

- **Read:** the public Strateq DX method repository and the bound private client repository.
- **Write:** the bound private client repository only, through a controlled branch or approved direct update.
- **Never read or write:** any other client's repository, files, project knowledge, chat exports or evidence.
- **Never write client data:** to the method repository, reusable Coworker skill, shared prompt, benchmark pack or another client repository.

## Zero-crossover controls

The coworker must:

1. verify the client marker in `CLIENT_BOUNDARY.md` before every material session;
2. check each supplied source against the bound client and initiative;
3. keep provenance for every fact used;
4. search only inside the two allowed repositories and the sources supplied for the active client session;
5. refuse cross-client comparisons unless the Digital Lead supplies an expressly anonymised, approved dataset in a non-client method workstream;
6. abstract lessons before proposing a method update, removing names, identifiers, commercial terms, dates, locations and traceable client facts;
7. require Digital Lead approval before an abstracted lesson is written to the method repository;
8. reset the client binding before moving to another client.

## Contamination test

Stop immediately if any of the following occurs:

- a source names a different client;
- a repository or path is outside the allowlist;
- the client identity is missing or ambiguous;
- content appears copied from another client;
- a requested output would expose another client's facts;
- a method change contains identifiable client data;
- the coworker cannot establish provenance.

Use this response:

> `STOPPED — client-boundary mismatch. No affected content has been reused or written. Digital Lead confirmation is required.`

Record the source, mismatch and affected proposed output without reproducing the conflicting client content.

## Client repository minimum controls

Each private client repository must contain:

- `CLIENT_BOUNDARY.md`
- `CLIENT_CONTEXT.md`
- `SOURCE_OF_TRUTH.md`
- `METHOD_BASELINE.md`
- `PUBLICATION_REGISTER.md`
- root `AGENTS.md`
- one controlled initiative folder per initiative

`CLIENT_BOUNDARY.md` must state the exact client ID, repository, classification, allowed method repository, prohibited crossover rule and publication boundary.

## Publication boundary

An external client store such as SharePoint may be a manual publication destination without being a connected working source. The client repository remains the working authority until the client profile explicitly changes it. A publication is recorded only after the Digital Lead confirms the upload.

## Audit evidence

Every material closeout records:

- bound client and repository;
- source files used;
- files changed;
- method baseline commit;
- any boundary exception or stop;
- release/publication status.

No exception to client separation may be inferred by the coworker.
