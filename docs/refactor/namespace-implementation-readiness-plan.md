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

## 9. Do-not-touch without explicit approval

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

## 10. Safe PR shape for future refactor implementation

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

## 11. Real-world analogy

Treat namespace/refactor implementation like reorganizing bank branch departments or public-sector archive rooms: first map every control, record, and approval route; then move one shelf at a time only when audit evidence and rollback path are preserved.
