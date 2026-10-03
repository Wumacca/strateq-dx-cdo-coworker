# BUILD | Coworker Architecture | Skills and Context Review

## Review position

Status: Review complete; implementation proposals pending Digital Lead decision.
This is an advisory method review, not a governance standard or a runtime instruction.
Accepting or merging this review records the assessment; it does not approve implementation,
alter the method baseline, install skills, enable connections or change client records.

- Repository: `Wumacca/strateq-dx-cdo-coworker`.
- Review branch: `build/skills-and-context-review`.
- Baseline: `cf72802f889eded3b5bd9b0251c13d9f5f556327` on `main`.
- Commission: Digital Lead requested this controlled review in the named build thread.
- Task type: Client-agnostic architecture and method QA.
- Lifecycle area: Governance / strategy / assessment; cross-cutting Coworker architecture.
- Jurisdiction: Method-Build Coworker; no client lifecycle session is being executed.
- Authority: `AGENTS.md`, `CLAUDE.md`, `00_system_control/OPERATING_RULES.md`,
  the fixed authority set, `00_system_control/11_COWORKER_ROUTER.md`,
  `00_system_control/18_CONTEXT_AND_CONTROL_LAYER_STANDARD.md` and
  `05_source_of_truth/01_DIGITAL_ARTEFACT_GOVERNANCE_MODEL.md`.
- Sources: Public method files at the pinned baseline and public repository PR/release metadata.
- Client boundary: No private client repository, live record, client attachment or client evidence was inspected or used.

## Recommendation

Keep the two-Coworker architecture and controlled source hierarchy. Prioritise entry-point
alignment, then make existing workflows easier to discover and execute. Treat context-loading
changes as a measured design proposal requiring approval before mandatory rules are reduced.

The current architecture already provides durable Markdown authority, routing, continuity,
evidence reconciliation, human approval, controlled changes and isolation. The main weakness
found is drift between entry points and the central rules. Skill packaging is incomplete,
and the mandatory context set is large enough to justify measurement.

## Scope and evidence limits

Reviewed the fixed authority set, method navigation, the existing Live Delivery skill and UI
metadata, Hopper readiness/route/intake models, all five B2-mapped process-mapping files,
central Live Status standard/interface, artefact registry and cockpit feed specification.
Source inventory and measurements were taken from exact baseline file content.

The repository has one `SKILL.md` under `.codex/skills/`:
`.codex/skills/strateq-dx-live-delivery/SKILL.md`.
This establishes repository packaging only. It does not establish which skills are installed
or discoverable in every AI platform.

Open PRs #15 and #20 were identified before changes. Their branches remain untouched.
They are not approved baseline authority for this review.

No model execution benchmark, installed-skill discovery test, connector permission test,
live client audit, workbook round-trip or document render was performed. Those are separate
implementation validations. No end-to-end runtime correctness or latency claim is made.

The originating video prompted the review; it is not method authority. Earlier comparison
used the publisher's overview and chapter list, not a full transcript. The seven image paths
supplied in chat were reported unavailable and their contents were not used. No finding here
depends on those images or on unverified video detail.

## Five proposals for decision

| ID | Proposal | Evidence and implication | Priority | Decision requested |
|---|---|---|---|---|
| SCR-01 | Align the Live Delivery entry point with current central authority | Its explicit section 2 load list omits the artefact registry and Context and Control standard required by the fixed set; inherited authority still applies | High | Approve a bounded entry-point alignment change |
| SCR-02 | Design and benchmark leaner context loading | The fixed authority set has 16 files, 273,131 Unicode characters and 36,097 whitespace-separated words before stage-specific additions | Medium | Approve design and measurement first; reserve rule changes for separate approval |
| SCR-03 | Package existing workflows as focused skills | Only Live Delivery has a repository skill; Hopper and process mapping have established governing models | Medium | Approve staged skill packaging without new Coworkers |
| SCR-04 | Specify a connector capability register | Existing controls define connection boundaries, but the baseline tree has no dedicated generic capability-register specification | Medium | Approve a blank method specification, without connecting services |
| SCR-05 | Reconcile Context and Control status wording with release evidence | Standard 18 still says Proposed, although PR #28 was merged and later registry releases record approved Context and Control artefact content | Medium | Approve evidence reconciliation and a separately reviewable wording correction |

Priorities reflect method assurance and implementation order; they are not lifecycle statuses
or permission to implement. The five proposals can be approved independently.

### SCR-01 — Entry-point alignment

Evidence:
- `CLAUDE.md`, B1: every governed session loads the fixed authority set.
- `AGENTS.md`, Mandatory authority sequence: registry resolution and Context and Control.
- `.codex/skills/strateq-dx-live-delivery/SKILL.md`, section 2: neither
  `00_system_control/16_METHOD_ARTEFACT_REGISTRY.md` nor
  `00_system_control/18_CONTEXT_AND_CONTROL_LAYER_STANDARD.md` appears in its explicit list.
- The skill references registry 16 later for workbook work and invokes central routing
  at the end. These later references do not make its section 2 list complete.
- `AGENTS.md` is read in section 1, so its absence from section 2 is not a missing-load finding.

Risk: An agent treating the skill list as sufficient could omit current-state/control checks
or apply reusable artefact resolution only to workbooks. Central authority already prevents
that behaviour; the defect is entry-point clarity, not an authorised exemption.

Proposed change:
- Explicitly require the complete fixed set and applicable B2 rows, with the exact missing
  registry and control-layer pointers made visible.
- State that all reusable artefacts require the revision handshake.
- Clarify when central intake applies and its multi-item routing scope while retaining
  one-client binding and separate initiative records.
- Validate skill description and UI metadata against the resulting supported scope.

Likely files: the existing skill and `agents/openai.yaml`; navigation only where scope changes.
No new lifecycle owner, status vocabulary, client write permission or platform dependency.

Acceptance: direct skill use loads 16 and 18; an unpinned artefact blocks generation;
missing current-state confirmation blocks a current claim; mixed central updates bind and
split correctly; UI description does not imply unsupported scope.

### SCR-02 — Context-loading design and measurement

Evidence:
- `CLAUDE.md`, B1 defines 16 fixed files; B2 adds stage files and overlapping modes.
- The measured unique fixed-file content totals 273,131 characters and 36,097 words.
- Measurements include complete files exactly once, with UTF-8 decoded as Unicode.
  They are not token counts or proof that all files remain resident simultaneously.
- Router 11 includes workflow detail in addition to routing, while its boundary says it
  points to governing files and must not duplicate operating or route rules.
- Session gate, authority and approval reminders recur in multiple entry points.

Proposed first step:
1. Produce a dependency and duplication inventory tied to the current B1/B2 map.
2. Measure current loading on synthetic Hopper, Live Delivery and process-mapping requests.
3. Distinguish retrieved bytes, resident context, retrieval count, route accuracy, gate
   coverage and response effort; use the same model/tool configuration for comparisons.
4. Draft a design separating irreducible authority/boundary checks from workflow detail.
5. Present exact rule changes and retained dependencies for Digital Lead approval.

No skill may omit today's mandatory set while this proposal is pending. Deduplicate actual
retrieval of identical files within a verified session only where every required file
remains loaded and available; revalidate when the baseline or source changes.

A future loading design must preserve deterministic selection, B3 additions, B5 fail-closed
handling, confirmation-first state, multiple-choice clarification where required, approval
and isolation. A generated manifest, if approved, should derive from the authority map
and record baseline and source identity; it must not become a competing hand-maintained map.

Likely future files: `CLAUDE.md`, router 11 and affected entry points, plus navigation
and deterministic validation. No file split is approved by this review.

Acceptance: no mandatory check lost in synthetic comparisons; no stale baseline reused;
all route/mode unions resolved; missing files fail closed; any proposed load reduction is
supported by measured benefit and an explicit governance diff.

### SCR-03 — Skills as entry points to existing workflows

Evidence:
- `README.md` identifies the existing Live Delivery runtime entry point.
- `00_system_control/FOLDER_MAP.md` says skills route to authority files.
- Hopper readiness: `01_governance_lifecycle/09_HOPPER_PORTFOLIO_READINESS_REVIEW_MODEL.md`,
  `01_governance_lifecycle/02_HOPPER_PRIORITY_SCREEN_MODEL.md`,
  `04_intake_dispatch/01_AUTOMATIC_HOPPER_CLARIFICATION_HANDLER.md` and route rules.
- Process mapping: the five mapped files under `03_process_mapping/`.
- Method QA: `AGENTS.md`, `CLAUDE.md`, control-layer 18 and artefact governance.

Suggested sequence:
1. `strateq-dx-method-qa`: method-only baseline, authority/navigation checks and proposed fixes.
2. `strateq-dx-hopper`: established Hopper intake/readiness and route-correct stage routing.
3. `strateq-dx-process-mapping`: approved-stage process capture and exportable packs.

These are proposed package names, not new Coworkers. Hopper remains the pre-live owner;
process mapping remains a capability within the routed lifecycle; method QA is build-only.

Each package should contain a concise trigger description, authority pointers, source
requirements, permitted output boundaries and matching UI metadata. Keep detailed workflow
logic in the governing files. A trigger must not automatically spin up a later stage.
Use existing controlled vocabulary, and define exclusions such as client work for method QA.

Likely files: new repository skill directories, UI metadata and repository navigation.
Update B2/router mappings in the same change where governance routing is added or changed.
Repository packaging is distinct from personal-skill installation or platform deployment.

Acceptance: synthetic positive and negative triggers select the correct skill and stage;
Hopper cannot generate Pack 1 before spin-up; process output remains draft until approval;
method QA cannot open client sources; skill descriptions and UI metadata agree.
Evaluate at least one normal case and one missing-evidence/ambiguous-route case per package.

### SCR-04 — Connector capability register specification

Evidence:
- `00_system_control/14_CLIENT_WORKSPACE_AND_REPORTING_PROTOCOL.md` requires an explicit
  working-authority profile and confirmed publication.
- `00_system_control/15_CLIENT_CONTEXT_ISOLATION_STANDARD.md` separates technical access
  from authority and recommends repository-scoped access where supported.
- `02_coworker_artifact_interface/09_COCKPIT_FEED_CONTRACT.md` and README distinguish
  specification from activated integration.
- No dedicated generic connector capability-register file exists in the baseline tree.
  This does not establish that connectors are absent in every environment.

Proposed blank specification fields:
- capability ID, service/type and permitted operations;
- authority for each record type and approved read/write/publication boundary;
- account/tenant routing requirement and isolated scope, stored client-side when populated;
- available versus verified versus authorised versus executed state;
- required approval and evidence of successful execution;
- authentication method category, error handling and manual fallback;
- verification date, revalidation trigger and owner;
- recovery/reversal constraints where an operation writes.

The public method holds only field definitions and blank structure. Account details,
permissions, credentials, client paths and populated entries remain in the bound private
workspace. Never store secrets in either register. No universal MCP-first purchasing rule
or mandatory vendor/tool stack is proposed.

Likely files: a new numbered system-control standard or interface, selected during
implementation, with B2, router, folder-map and README updates in the same change.

Acceptance: synthetic cases distinguish available access from permitted writes; wrong
account/scope fails closed; read-only credentials cannot publish; a failed/absent write
cannot be reported complete; manual fallback is clearly recorded.

### SCR-05 — Approval and release wording reconciliation

Evidence:
- `00_system_control/18_CONTEXT_AND_CONTROL_LAYER_STANDARD.md`, Status:
  "Proposed controlled method standard. Merge and release require Digital Lead approval."
- PR #28 introduced the layer and was merged at
  `25d3a12a89adfe1928f880725af8fd54a758fac0`.
- Registry 16 records approved EIDF r3 and Delivery Setup r2 at
  `052a747c12deec2331c17a5de6b9a66bb1a5dca4` (PR #31), including Context and Control content.
- AGENTS, CLAUDE, router and README make the layer mandatory or describe adoption.

Interpretation: a stale status heading is likely. Merge metadata and approved downstream
artefact rows support reconciliation, but do not justify inventing a new approval date,
approver, release or client adoption. The review does not declare the standard unapproved.

Proposed change: reconcile the existing Digital Lead decision and release evidence;
then propose precise status wording and any necessary release reference corrections.
Keep existing client-baseline adoption gates. Do not create a new artefact revision merely
to make wording appear current; assess revision impact under registry 16.

Acceptance: standard status, authority references and release evidence agree; no approval
or client adoption is inferred; any substantive schema/template change receives its own
revision and approval.

## Validation plan for implementation

The following are acceptance scenarios, not tests reported as executed by this review.

| Case | Synthetic trigger or failure | Required result |
|---|---|---|
| V01 | Governed request through direct Live Delivery skill | Full fixed authority and correct B2 union available |
| V02 | One required authority file unavailable | B5 stop; no governed output |
| V03 | Old source presented as current | Pending confirmation; no current-status claim |
| V04 | Client marker or memory boundary mismatch | Isolation stop before affected content is reused |
| V05 | Unpinned or superseded reusable artefact | Revision handshake blocks generation |
| V06 | Material question unresolved | Required multiple-choice gate remains blocking or explicit bounded disposition recorded |
| V07 | Hopper request without later-stage spin-up | No initiation/delivery plan beyond permitted stage |
| V08 | Process capture with missing evidence | Gaps surfaced; draft status and correct output limits retained |
| V09 | Central intake contains multiple work units | Canonical branches bound; separate changes; no parallel ledger |
| V10 | Branch-only update absent from reporting source | No reportable merged-state claim |
| V11 | Connector write absent or failed | No completed publication/write-back claim |
| V12 | QA suggests a rule improvement | Proposal only; no self-authorised governance change |

Use client-free synthetic fixtures only in this build project. Record actual inputs,
loaded file set, observed output, pass/fail reason and model/tool configuration.
Static path/frontmatter checks alone cannot establish runtime behaviour.

## Review validation completed

- Current main SHA confirmed and pinned; baseline commit is PR #35's workbook-fidelity merge.
- Open PRs #15 and #20 identified and preserved.
- Public-method-only source boundary maintained.
- Repository skill count, fixed-file count, word/character totals and missing-load finding
  reproduced from baseline content.
- Existing skill reads AGENTS in section 1; it is excluded from the missing-load conclusion.
- PR #28 merge metadata and current registry release rows cross-checked for SCR-05.
- Review references checked against the baseline repository tree.
- Proposed package names distinguished from controlled Coworker/route/status vocabulary.
- Proposed scenarios distinguished from performed tests.
- Review does not change governance files, workbook/docx templates, artefact revisions,
  client baselines or active connections.

No binary templates were edited; formula/render tests are not applicable to this review.

## Controlled next actions and closeout

Files in the review PR:
- `docs/reviews/SKILLS_AND_CONTEXT_REVIEW.md` — this advisory assessment.
- `README.md` — navigation link marked advisory.

No governance file is added, renamed, split or retired; therefore B2 and FOLDER_MAP authority
mapping changes are not required for this review-only PR. Any implementation that changes
governance files must update all required maps and navigation in the same controlled change.

Knowledge capture: this review is the durable record of five method proposals and their
evidence. No client-derived lesson or live state is captured. QA findings remain advisory.

Digital Lead actions:
1. Approve, amend or defer SCR-01 through SCR-05 independently.
2. Separately decide whether to merge the review-only PR.
3. Authorise implementation scope before a follow-on branch changes operating rules or skills.

Approval of implementation scope does not authorise merge/release or client adoption.
Pending decisions remain explicit. No client follow-up, external publication or lifecycle
handover is required by this review.
