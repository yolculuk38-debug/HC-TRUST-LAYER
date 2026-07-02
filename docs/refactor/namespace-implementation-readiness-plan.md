# Namespace Implementation Readiness Plan

## 1. Purpose

This document is a conservative readiness plan for possible future namespace/refactor implementation in HC-TRUST-LAYER. It does not perform refactor work, authorize source moves, or change repository behavior. It exists to define prerequisites, risk boundaries, evidence requirements, and safe sequencing before any future namespace/refactor implementation is proposed.

This plan supports the HC Trust Engineer Agent, report-only runner, controlled assistant, GitHub-native advisory layer, project-control queue, and governance boundary by keeping namespace work scoped, reviewable, and human-supervised.

## 2. HC boundary statement

This document preserves the following HC:// and HC-TRUST-LAYER boundaries:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `label_reviewer_mutation=false`
- no new or unauthorized issue-comment automation
- no source/runtime move
- no import path change
- no CLI behavior change
- no package metadata change
- no workflow change
- no workflow permission change
- no new workflow
- no new check
- no runtime behavior change
- no public API behavior change
- no schema/validator/record/generated/canonical behavior change
- no bot authority expansion
- CI/checks are evidence, not trust authority
- human maintainers/reviewers make final decisions

## 3. Non-goals

This PR does not:

- move files
- rename files
- delete files
- split packages
- merge packages
- change imports
- change CLI entrypoints
- change runtime behavior
- change tests
- change workflows
- change package metadata
- change schema, validators, records, generated artifacts, canonical artifacts, policy, federation, signing, hash, or QR behavior
- change bot/AI/comment/label/reviewer/approval/merge/close authority

## 4. Namespace vocabulary

- **Core protocol/runtime-adjacent surface:** Files that influence protocol interpretation, verification semantics, or runtime-adjacent behavior even when not directly executable.
- **Runtime/API/CLI surface:** Source modules, package entrypoints, public API paths, and command behavior used by repository tooling or downstream consumers.
- **Governance/policy surface:** Documents and configuration that explain authority, review boundaries, policy interpretation, escalation, or maintainer control.
- **Advisory/report-only surface:** Reports, plans, controlled assistant outputs, and report-only runner material that provide evidence or recommendations without approval, merge, label, reviewer, close, or mutation authority.
- **Public/demo/docs surface:** Public-safe documentation, demos, and examples that explain repository behavior without claiming final truth, autonomous authority, or guaranteed correctness.
- **Test/validation surface:** Test suites, fixtures, validators, and checks that provide evidence about expected behavior without replacing human review.
- **Generated/canonical/evidence surface:** Generated outputs, canonical artifacts, records, signatures, hashes, QR artifacts, and provenance-bearing material that must preserve audit continuity.
- **Experimental surface:** Draft, future-facing, or research material that may guide later work but does not establish implemented behavior or authority.
- **Protected/high-risk surface:** Any path where movement or mutation may affect record identity, verification semantics, governance interpretation, package behavior, workflow behavior, evidence continuity, or authority boundaries.

## 5. Current-state classification table

| Surface | Current role | Future namespace/refactor posture | Why it matters | Implementation risk | Evidence required before any future move/change |
|---|---|---|---|---|---|
| `src/` | Runtime and library implementation surface. | Do not move or rename until imports, APIs, CLI behavior, package discovery, and tests are mapped. | Runtime movement can change verification behavior or public integration paths. | High. | Import map, API map, CLI map, package discovery notes, contract tests, old/new behavior comparison, rollback plan, explicit human-maintainer authorization. |
| `tests/` | Test suites and fixtures. | Refactor only after affected runtime and validation expectations are mapped. | Tests are evidence for behavior and guard against accidental contract drift. | Medium to high. | Test coverage inventory, fixture impact review, old/new test paths, rollback plan, explicit scope approval. |
| `scripts/` | Checks, report generators, validation helpers, and bounded maintenance utilities. | Keep stable unless script entrypoints, users, and outputs are mapped. | Scripts produce review evidence but are not trust authority. | Medium to high. | Script caller map, output comparison, docs references, check invocation list, rollback plan. |
| `.github/` | GitHub-native advisory layer, workflow configuration, and repository automation. | Do not move/change without dedicated workflow authorization. | Workflow changes can affect CI evidence, permissions, and review flow. | Very high. | Workflow reference map, permission impact statement, no authority expansion statement, human-maintainer authorization, rollback path. |
| `docs/` | Documentation, onboarding, architecture, planning, demos, and explanatory material. | Low-risk docs may be reorganized only with link checks and authority-boundary review. | Documentation shapes contributor interpretation and public-safe boundaries. | Medium. | Link check, audience impact, boundary-language review, affected docs list, rollback plan. |
| `docs/project-control/` | Project-control queue, state, next actions, and operating-layer coordination. | Do not move without maintainer confirmation. | It coordinates controlled assistant and report-only runner work without replacing human review. | High. | Project-control reference map, issue/PR link impact, governance boundary review, human-maintainer authorization. |
| `docs/governance/` | Governance interpretation and review-boundary material. | Do not move without governance-specific approval. | It affects authority interpretation and maintainer decision routes. | High. | Governance reference map, authority impact statement, explicit no-authority-expansion statement, human-maintainer authorization. |
| `docs/workflows/` | Workflow documentation and cleanup planning. | Keep separate from actual workflow implementation changes. | It explains automation posture without changing workflows. | Medium to high. | Workflow-doc link check, confirmation of no workflow/check/permission change, rollback plan. |
| `schema/` | Schema definitions and record contracts. | Do not move without explicit dedicated approval. | Schema paths can define canonical record boundaries. | Very high. | Schema reference map, validator impact, record compatibility evidence, canonical impact statement, human-maintainer authorization. |
| `validators/` | Validation and verification surfaces. | Do not move without explicit dedicated approval. | Validator changes can affect verification interpretation. | Very high. | Validator caller map, test coverage, behavior comparison, schema impact review, human-maintainer authorization. |
| `records/` | Evidence-bearing records and provenance artifacts. | Do not move except under dedicated evidence-preserving plan. | Records preserve audit continuity. | Very high. | Record inventory, provenance impact statement, hash/signature impact check, rollback plan, human-maintainer authorization. |
| `generated/` | Generated or derived artifacts. | Do not hand-move or hand-edit without generation plan. | Generated paths may mirror canonical sources or release evidence. | Very high. | Generator map, regeneration command, diff evidence, canonical impact check, human-maintainer authorization. |
| `canonical/` | Canonical artifacts where present. | Do not move without explicit canonical-boundary approval. | Canonical artifacts may define trusted navigation or reference boundaries. | Very high. | Canonical reference inventory, compatibility evidence, provenance review, rollback plan, human-maintainer authorization. |
| `policy/` | Policy and governance-control material. | Do not move without policy-specific authorization. | Policy movement can alter governance interpretation. | Very high. | Policy reference map, authority impact statement, no-expansion statement, human-maintainer authorization. |
| `federation/` | Federation-related references or implementation surfaces. | Do not move without dedicated federation review. | Federation posture affects future trust-boundary interpretation. | High. | Federation reference map, behavior impact statement, test/evidence plan, human-maintainer authorization. |
| `signatures/` | Signature-related evidence or signing references. | Do not move without signing/evidence approval. | Signature paths can affect evidence continuity and signing expectations. | Very high. | Signature inventory, verification reference map, hash/canonical impact statement, human-maintainer authorization. |
| `hash/` | Hash references and integrity artifacts. | Do not move without integrity evidence plan. | Hash paths may anchor evidence relationships. | Very high. | Hash inventory, reference map, old/new digest comparison where applicable, human-maintainer authorization. |
| `qr/` | QR verification artifacts and references. | Do not move without QR-boundary approval. | QR paths can affect verification interpretation and public guidance. | High. | QR reference map, behavior impact statement, docs link check, human-maintainer authorization. |
| `examples/` | Example packages, demos, and contributor-facing examples. | Move only after docs links and demo expectations are checked. | Examples can shape public understanding and onboarding. | Medium. | Example reference map, demo behavior check, public-safe language review, rollback plan. |
| `CODEOWNERS` | Ownership and review-routing control. | Do not move/change without explicit maintainer authorization. | Ownership paths can affect review expectations. | Very high. | Ownership impact statement, protected-path review, human-maintainer authorization. |
| `AGENTS.md` | Agent and contributor operating instructions. | Do not move/change without explicit maintainer authorization. | It defines controlled assistant behavior and repository-facing boundaries. | High. | Agent-instruction impact review, scope statement, human-maintainer authorization. |
| `HC_BOOTSTRAP.md` | Startup and handoff protocol. | Do not move/change without explicit maintainer authorization. | It guides repository operating-layer entry. | High. | Bootstrap reference map, handoff impact statement, human-maintainer authorization. |
| `CONTRIBUTING.md` | Contributor workflow guidance. | Do not move/change without contributor-path review. | It affects PR discipline and contributor onboarding. | High. | Contributor-path impact statement, link check, human-maintainer authorization. |
| `SECURITY.md` | Security reporting and escalation guidance. | Do not move/change without security-specific approval. | It affects vulnerability reporting expectations. | Very high. | Security-route impact statement, link check, human-maintainer authorization. |
| `GOVERNANCE.md` | Governance and merge authority guidance. | Do not move/change without governance-specific approval. | It affects authority interpretation. | Very high. | Governance impact statement, no-authority-expansion statement, human-maintainer authorization. |
| `pyproject.toml` | Package metadata, tooling configuration, and possible entrypoint configuration. | Do not change during namespace work unless package impact is the explicit scope. | Metadata can change package discovery, CLI exposure, or tooling behavior. | Very high. | Package discovery map, CLI impact review, tooling output comparison, human-maintainer authorization. |
| `requirements.txt` | Dependency surface. | Do not change for namespace-only work. | Dependency changes alter environment expectations and may mask refactor risk. | High. | Dependency impact statement, install/test comparison, human-maintainer authorization. |

## 6. Readiness checklist before any actual refactor

Before any implementation PR moves, renames, splits, merges, or edits namespace-sensitive files, confirm:

- current imports mapped
- current CLI entrypoints mapped
- package discovery behavior mapped
- tests that cover affected surface identified
- docs links checked
- workflow references checked
- generated/canonical references checked
- protected-path impact checked
- rollback plan written
- one namespace family per PR
- human maintainer explicitly authorizes scope
- no authority expansion
- old/new behavior comparison available

## 7. Safe future PR sequence

1. Docs-only current-state map.
2. Tests-only import/CLI contract coverage.
3. One low-risk docs/demo namespace cleanup, if needed.
4. One low-risk internal helper move, if tests prove stable.
5. Runtime/API/CLI changes only after contract coverage exists.
6. Protected/generated/canonical/schema/validator/policy/federation/signing/QR/hash changes only with explicit human approval and dedicated evidence.


## 8. Runtime namespace migration checkpoint after #1174, #1175, and #1176

This checkpoint records the current docs-only namespace/refactor migration status after the completed low-risk runtime helper moves in #1174, #1175, and #1176. It does not authorize additional source moves, change runtime behavior, expand bot authority, or replace human review. HC:// and HC-TRUST-LAYER authority boundaries remain advisory-only, public-safe, and subject to human final authority.

Completed low-risk runtime helper moves:

- #1174 moved `hc_runtime.redaction` to `hc_runtime.contracts.redaction`.
- #1175 moved `hc_runtime.abuse_signals` to `hc_runtime.contracts.abuse_signals`.
- #1176 moved `hc_runtime.decision_engine` to `hc_runtime.contracts.decision_engine`.

Old import compatibility wrappers remain required for these moved helpers. They preserve reviewable compatibility while callers, downstream references, and future coverage are evaluated. Removing those wrappers is not part of this checkpoint.

A follow-up candidate scan found no fourth clearly low-risk runtime helper move that is currently safe. Remaining runtime candidates appear to touch protected or higher-risk behavior, integration, evidence, or authority-adjacent surfaces, including:

- public validator
- canonical lookup/loader
- QR parser/bridge/spoof protection
- runtime pipeline/state/app/router
- event store
- federation/policy/queue
- schema/validator/record/hash/signing
- generated/canonical artifacts

Future runtime namespace moves require at least one of the following before implementation:

- new targeted tests for the affected surface
- a separate risk plan with affected files, behavior impact, rollback path, and validation evidence
- human-approved higher-risk refactor scope

This checkpoint is advisory documentation only. It does not claim production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness. Human maintainers and reviewers retain final authority.

## 9. Final closeout: runtime helper namespace migration phase

This closeout records that the low-risk runtime helper namespace migration phase is complete. It is a docs-only checkpoint after #1173, #1174, #1175, #1176, and #1177. It does not reopen the helper migration phase, authorize new source moves, change runtime behavior, change CLI behavior, change package metadata, change workflows, or change schema, validator, record, hash, QR, signing, federation, policy, canonical, or generated artifacts.

Completed sequence:

- #1173 added import, CLI, and package-discovery contract coverage before namespace moves.
- #1174 moved `hc_runtime.redaction` to `hc_runtime.contracts.redaction` while preserving old import compatibility.
- #1175 moved `hc_runtime.abuse_signals` to `hc_runtime.contracts.abuse_signals` while preserving old import compatibility.
- #1176 moved `hc_runtime.decision_engine` to `hc_runtime.contracts.decision_engine` while preserving old import compatibility.
- #1177 recorded the checkpoint that no fourth clearly low-risk helper move is currently safe.

Compatibility wrappers remain required for the moved helpers. They must not be removed without a separate deprecation and removal plan that is explicitly approved, scoped, tested, and documented.

The following areas were intentionally not moved in this phase:

- public validator
- canonical lookup/loader
- QR parser/bridge/spoof protection
- runtime pipeline/state/app/router
- event store
- federation/policy/queue
- schema/validator/record/hash/signing
- generated/canonical artifacts

Future work in those areas is not a continuation of the low-risk helper phase. It is a new higher-risk workstream that requires separate planning and approval before implementation. At minimum, future higher-risk runtime namespace work must include:

- explicit human approval
- affected-file list
- behavior-impact analysis
- rollback path
- targeted tests
- CI evidence
- compatibility plan

HC:// and HC-TRUST-LAYER authority boundaries remain unchanged:

- advisory-only
- public-safe
- no truth guarantee
- human review required
- no bot approval authority
- no bot merge authority
- no autonomous governance authority

This closeout is advisory documentation only. It does not claim production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness. Human maintainers and reviewers retain final authority. Any further runtime namespace movement requires a new higher-risk plan.

## 10. Higher-risk runtime namespace workstream

This section defines a new higher-risk runtime namespace workstream. It is not a continuation of the completed low-risk runtime helper phase from #1173, #1174, #1175, #1176, #1177, and #1178. It does not authorize implementation, source moves, behavior changes, wrapper removals, CLI changes, package metadata changes, workflow changes, or protected-path changes.

### Higher-risk surfaces and required evidence

Each surface below requires the listed evidence before any implementation PR is opened:

| Surface | Required evidence before implementation |
|---|---|
| Public validator | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Canonical lookup/loader | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| QR parser/bridge/spoof protection | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Runtime pipeline/state/app/router | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Event store | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Federation/policy/queue | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Schema/validator/record/hash/signing | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |
| Generated/canonical artifacts | Affected-file list, behavior-impact analysis, compatibility/deprecation plan, rollback path, targeted tests, CI evidence, and explicit human approval. |

### Implementation rules

Future higher-risk runtime namespace implementation must follow these rules:

- one surface per PR
- no mixed refactor and behavior changes
- no wrapper removal without a separate deprecation and removal plan
- no CLI, package, or workflow change mixed into runtime namespace work
- no schema, validator, record, hash, QR, signing, federation, policy, canonical, or generated change without a dedicated PR and explicit human approval

### First recommended candidate for future coverage planning only

The first recommended higher-risk candidate is the event store surface, for coverage planning only. It appears to be the least risky among the higher-risk group because it is narrower than public validator, canonical lookup/loader, QR parser/bridge/spoof protection, federation/policy/queue, schema/validator/record/hash/signing, and generated/canonical artifact surfaces. This plan does not implement event store namespace work and does not authorize source movement. A future planning PR should map affected files, current callers, behavior boundaries, compatibility expectations, rollback path, targeted tests, CI evidence, and required human approval before any implementation is proposed.

### Event store coverage map

This subsection maps the event store surface for future coverage planning only. It is documentation-only and does not authorize implementation, source movement, behavior changes, wrapper removal, CLI/package/workflow changes, protected-path changes, or bot authority expansion.

Event store files discovered:

- `src/hc_runtime/events/__init__.py` re-exports `RuntimeEventStore` from the event store module.
- `src/hc_runtime/events/store.py` defines the append-only advisory in-memory `RuntimeEventStore`.

Current direct callers/importers discovered:

- `src/hc_runtime/state.py` imports `RuntimeEventStore` through `hc_runtime.events` and creates the shared `EVENT_STORE`.
- `src/hc_runtime/runtime.py` imports `RuntimeEventStore` through `hc_runtime.events` for runtime flow support.
- `src/hc_runtime/routes/verify.py` uses the shared `EVENT_STORE` history and append behavior through runtime route flows.
- `src/hc_runtime/routes/health.py` reads `EVENT_STORE._events` for advisory degraded-runtime telemetry counts.
- `tests/test_hc_runtime_pipeline.py` imports `RuntimeEventStore` through `hc_runtime.events` and checks deterministic history and append-only behavior.
- `tests/runtime/test_replay_continuity_edge_cases.py` imports and instantiates `RuntimeEventStore` for replay warning and continuity history checks.
- `tests/runtime/test_secret_redaction_runtime_outputs.py` imports and instantiates `RuntimeEventStore` for public-safe runtime event redaction checks.
- `tests/runtime/test_degraded_recovery_edge_cases.py` imports and instantiates `RuntimeEventStore` for degraded recovery history and telemetry checks.
- Runtime app and telemetry tests use the shared `EVENT_STORE` and its `_events` list to reset state or verify public response and telemetry behavior.

Existing tests discovered:

- `tests/test_hc_runtime_pipeline.py` includes event store checks for deterministic history ordering, append-only preservation, replay warning, and continuity history behavior.
- `tests/test_hc_runtime_app.py` covers runtime history response shape, record-scoped missing history, event visibility, append-only history growth, advisory/public-safe event markers, and degraded runtime event telemetry.
- `tests/runtime/test_replay_continuity_edge_cases.py` covers isolated replay warning history, record scoping, event ordering, advisory/public-safe markers, and replay visibility.
- `tests/runtime/test_secret_redaction_runtime_outputs.py` covers event details and history redaction boundaries for public runtime outputs.
- `tests/runtime/test_degraded_recovery_edge_cases.py` covers degraded recovery events, event ordering, advisory/public-safe markers, degraded telemetry counts, malformed degraded details, and empty-history behavior.
- `tests/runtime/test_telemetry_payload_contract.py`, `tests/runtime/test_telemetry_payload_safety_contract.py`, `tests/test_hc_runtime_response_contracts.py`, and related runtime tests cover telemetry keys, event counts, public response contracts, and shared event-store reset behavior.
- `tests/test_refactor_contracts.py` includes the `hc_runtime.events` import namespace in refactor contract coverage.

Behavior boundaries that must not change:

- `RuntimeEventStore` remains append-only for recorded advisory runtime events.
- Event order remains deterministic in append order for history and telemetry consumers.
- `history(record_id)` remains record-scoped and returns no events for unrelated or missing records.
- Public event payloads remain redacted through existing redaction helpers before storage or exposure.
- Event dictionaries retain current public markers, including `advisory_only=True`, `public_safe=True`, and timestamped `occurred_at` values.
- Existing event types and details used by runtime flows remain compatible, including `trust_state_transition`, `continuity_checkpoint`, `replay_warning`, and `runtime_recovery_mode`.
- Runtime history and telemetry outputs remain advisory and do not imply truth guarantee, final identity determination, forensic certainty, production readiness, certification authority, or autonomous governance authority.
- Shared runtime state continues to expose the existing `EVENT_STORE` behavior expected by routes and tests.

Compatibility expectations if a future namespace move is attempted:

- Preserve the public `hc_runtime.events` import path through a compatibility wrapper unless a separately approved deprecation/removal plan exists.
- Preserve `RuntimeEventStore` construction, method names, method signatures, return shapes, and event dictionary keys.
- Preserve `EVENT_STORE` behavior in `hc_runtime.state` and all route-level consumers.
- Preserve direct test and runtime access to `_events` unless a future PR explicitly maps, tests, and approves a replacement compatibility path.
- Keep CLI behavior, package discovery, package metadata, workflow behavior, schema/validator/record/hash/QR/signing/federation/policy/canonical/generated artifacts, and bot authority unchanged.

Rollback expectations:

- A future event store namespace implementation PR must be reversible by restoring the prior `src/hc_runtime/events/` module layout and `hc_runtime.events` import behavior.
- Compatibility wrappers must remain until rollback risk and downstream import usage are explicitly reviewed.
- Rollback must preserve existing event history semantics, public-safe redaction, telemetry counts, route response shapes, and advisory authority markers.
- Any failed future implementation must be reverted without modifying workflows, package metadata, CLI entrypoints, schema, validators, records, hash, QR, signing, federation, policy, canonical artifacts, generated artifacts, or bot authority.

Targeted tests required before any implementation PR:

- Run focused event store unit coverage in `tests/test_hc_runtime_pipeline.py`.
- Run runtime app/history coverage in `tests/test_hc_runtime_app.py`.
- Run replay continuity edge-case coverage in `tests/runtime/test_replay_continuity_edge_cases.py`.
- Run degraded recovery edge-case coverage in `tests/runtime/test_degraded_recovery_edge_cases.py`.
- Run secret-redaction runtime output coverage in `tests/runtime/test_secret_redaction_runtime_outputs.py`.
- Run telemetry payload contract and safety coverage in `tests/runtime/test_telemetry_payload_contract.py` and `tests/runtime/test_telemetry_payload_safety_contract.py`.
- Run refactor contract coverage in `tests/test_refactor_contracts.py` to confirm `hc_runtime.events` compatibility.
- Run repository documentation and canonical checks required for the implementation scope.

This PR does not authorize:

- event store source move
- event store behavior change
- wrapper removal
- CLI/package/workflow change
- schema/validator/record/hash/QR/signing/federation/policy/canonical/generated change
- bot authority expansion

HC:// and HC-TRUST-LAYER authority boundaries remain unchanged for this event store coverage map:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `autonomous_governance_authority=false`

### Not authorized by this plan

This plan does not authorize:

- source moves
- behavior changes
- wrapper removals
- bot authority expansion
- workflow or package changes

### Authority boundaries

HC:// and HC-TRUST-LAYER authority boundaries remain unchanged for this workstream:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`
- `autonomous_governance_authority=false`


## 11. Do-not-touch without explicit approval

Do not touch these surfaces for namespace/refactor implementation without explicit human-maintainer approval and dedicated evidence:

- generated/canonical/evidence surfaces
- schema and validators
- records
- signing/signature surfaces
- hash and QR verification surfaces
- policy/federation surfaces
- workflow files
- package metadata
- CLI entrypoints
- `CODEOWNERS`
- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- governance/security/contribution root docs
- auto-merge and bot authority surfaces

## 12. Safe PR shape for future refactor implementation

Future refactor PRs must state:

- exact files moved/renamed/edited
- old import path
- new import path
- compatibility behavior
- CLI/package impact
- workflow/check impact
- docs-link impact
- protected-path impact
- generated/canonical/evidence impact
- rollback path
- tests run
- human-maintainer authorization statement

## 13. Real-world analogy

Treat namespace/refactor implementation like reorganizing bank branch departments or public-sector archive rooms: first map every control, record, and approval route; then move one shelf at a time only when audit evidence and rollback path are preserved.
