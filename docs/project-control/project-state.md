# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator / explorer planning is synchronized through #821/#822. HC Control Bot, assistant-console, repository assistant baseline, and operator-entry-map state are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core, hardening, CLI, sample, and quickstart are complete through #838/#839/#841/#843. HC Trust Engineer report generator, direct CLI fix, status checkpoint, examples, and quickstart are complete through #872/#873/#874/#875. HC Engineer task planner, skipped-check/manual-review hardening, operator quickstart, and state sync are complete through #888/#889/#890/#891. Signature/witness verification planning, GitHub issue/comment PR-flow diagnostic note, and signature/witness fixture-format proposal are complete through #892/#894/#896, with #893 closed as a completed diagnostic issue. |
| Next up | Continue the working core in small scoped PRs only. Candidate next work: a non-canonical verification-package fixture/example that demonstrates the documented signature/witness fixture shape without touching protected paths or adding uncontrolled automation. |
| Blocked / parked work | Workflow, schema, validator, record, policy, federation, signing, trust-kernel index, generated artifact, QR/hash evidence format, governance-enforcement, authority-changing automation, and production-readiness claims remain parked unless explicitly authorized and validated. |
| Do-not-repeat references | Treat #628, #629, #630, #631, #682, #683, #685, #686, #688, #701, #794, #795, #796, #811, #813, #814, #820, #821, #822, #823, #824, #826, #828, #831, #834, #838, #839, #841, #843, #872, #873, #874, #875, #888, #889, #890, #891, #892, #893, #894, and #896 as completed references. #812 remains the active HC Assistant Console v2 reference; #763 remains historical only. |
| Review / merge rule | Before merge: verify changed files, checks, Codex/review comments, and risk scope. If comments exist, fix first. Human final authority remains the governance boundary. |
| Protected-path reminder | Do not modify `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, `records/**`, generated artifacts, QR/hash evidence, or trust-kernel indexes unless explicitly requested and approved. |
| Source-of-truth priority | Repository markdown docs, merged files, checks, PR evidence, and human review decisions outrank chat memory and advisory machine-readable context. |

## Current phase

Working verification core / post-runtime stabilization.

## Repository status

HC-TRUST-LAYER is advisory-only, early-stage trust infrastructure. Repository evidence, merged files, checks, and human review decisions are the source of truth for current state. AI agents and automation are advisory only; human reviewers retain final authority, especially for trust-kernel-adjacent or protected-path work.

The `v0.1.0` tag remains the initial protected protocol infrastructure and release-candidate documentation baseline. `main` has continued beyond that tag and is the active development line.

## Last known completed stabilization sequence

- #628 telemetry contract review: TELEMETRY CONTRACT SUFFICIENT
- #629 replay / continuity edge-case coverage: merged
- #630 runtime stabilization review: RUNTIME CONDITIONALLY STABILIZED
- #631 HC Operating Layer review: OPERATING LAYER CONDITIONALLY SUFFICIENT
- #834 validator pipeline nested response contract coverage: merged test-only hardening for `ValidatorPipeline` nested response shapes.
- #838 verification package hash core: added a local advisory verifier for manifest-listed file existence and SHA-256 digest matching.
- #839 verification package hash core hardening: handled malformed manifest files without raising and enforced resolved package-path containment before hashing.
- #841 verification package CLI entry point: added `hc-trust verify-package <package_path>` around the local hash core.
- #843 verification package sample / quickstart: added a minimal valid package, quickstart, and regression test for the CLI/core path.
- #872 HC Trust Engineer report generator: added local deterministic report-only advisory JSON generation from local fixtures.
- #873 report generator CLI import fix: preserved direct script execution.
- #874 report generator status checkpoint: recorded report-only boundaries and direct CLI behavior.
- #875 report generator quickstart/examples: added clean-docs and protected-path fixtures plus quickstart instructions.
- #888 HC Engineer task planner: added deterministic advisory task planning, review order, merge gates, and post-merge cleanup.
- #889 task planner hardening: treated skipped checks and scanner human-review signals as manual-review merge blockers.
- #890 task planner quickstart: documented operator usage, output fields, and required blocker examples.
- #891 project-control synchronization: recorded the task-planner quickstart sequence after #888/#889/#890.
- #892 signature/witness verification proposal: added a documentation-only planning layer for future signature and witness verification without touching protected implementation paths.
- #893/#894 GitHub issue/comment PR-flow diagnostic: tested the issue/comment assisted PR path, recorded that GitHub source-of-truth must still verify actual branches and PRs, and merged a docs-only operations note through #894.
- #896 signature/witness fixture-format proposal: recorded a docs-only fixture shape for future `signature_proof` and existing local `witness_proof` evidence without implementing signing or changing protected paths.

## Completed verification package hash core sequence

- #838 added `src/hc_trust/verification_package.py` and `tests/test_verification_package_hash_core.py`.
- #839 followed up on automated review findings and hardened manifest handling and path containment before treating a file as package evidence.
- #841 exposed the core through the existing `hc-trust` CLI as `hc-trust verify-package <package_path>`.
- #843 added `examples/verification-package/valid/`, `docs/verification-package-cli-quickstart.md`, and `tests/test_verification_package_sample.py`.
- This is the first usable local verification-package integrity slice: manifest, listed file existence, SHA-256 match, missing/conflicting evidence, CLI entry point, and sample package.
- It does not verify legal truth, QR authenticity, signatures, witnesses, C2PA assertions, OpenTimestamps attestations, federation state, or production readiness.
- Do not repeat #838/#839/#841/#843 unless new repository evidence appears.

## Completed HC Trust Engineer report generator and task planner sequence

- #872 added `scripts/hc_trust_engineer_report.py` and tests for local deterministic report-only advisory JSON generation from local fixtures.
- #873 fixed direct script execution import behavior for the report generator.
- #874 recorded the report generator status checkpoint and locked report-only, local-only, public-safe, and advisory-only boundaries.
- #875 added clean-docs and protected-path report fixtures plus quickstart instructions for the report generator.
- #888 added `scripts/hc_engineer_task_plan.py`, a task-plan fixture, and tests for deterministic advisory PR planning, one-open-PR discipline, review order, merge gates, and post-merge cleanup.
- #889 hardened the task planner so scanner human-review signals and skipped checks block merge guidance and set `merge_gate.requires_human_review=true`.
- #890 added `docs/hc-engineer/task-planner-quickstart.md` documenting planner usage, output fields, clean docs-only, open PR, unresolved review/Codex, skipped-check, and scanner-marked human-review examples.
- #891 synchronized project-control state after the task planner quickstart.
- The report generator and task planner remain local, deterministic, report-only/operator-aid surfaces. They do not create approval, rejection, merge, close, label, assignment, reviewer-request, external network, LLM, truth-finality, or production-readiness authority.
- Do not repeat #872/#873/#874/#875/#888/#889/#890/#891 unless new repository evidence appears.

## Completed signature/witness and operations-flow diagnostic sequence

- #892 added `docs/verification/signature-witness-verification-proposal.md` as a documentation-only planning layer for future signature and witness verification.
- #893 tested whether a GitHub issue/comment request could drive a branch, commit, and PR flow. It is closed as completed diagnostic evidence, not as implementation authority.
- #894 added `docs/operations/github-pr-flow-note.md`, recording the controlled assistant GitHub PR-flow note and preserving human final authority.
- #896 added `docs/verification/signature-witness-fixture-format-proposal.md`, recording a fixture-format proposal for future `signature_proof` and existing local `witness_proof` evidence.
- The diagnostic outcome is that assistant-generated success claims must be checked against GitHub source-of-truth: branch visibility, PR visibility, changed files, checks, and merge state.
- Do not treat issue/comment based new-PR creation as reliable without repository evidence. Use PR-context review/fix assistance only after a real GitHub PR exists.
- Do not treat the signature fixture proposal as signing implementation, witness authority, identity finality, C2PA/OpenTimestamps/W3C VC verification, federation, or production readiness.

## Completed public validator / public explorer planning sequence

- #682 linked public validator planning navigation.
- #820 added the official documentation-only Public Validator MVP Specification.
- #821 synchronized navigation and project-control references so the #820 specification is the primary planner entry and duplicate Public Validator MVP specification work is avoided.
- #822 synchronized project-state and task-ledger references after #820/#821 public validator navigation.
- #683 added the public explorer navigation map.
- #685 completed the public explorer planning gap review.
- #686 added the public explorer maturity checklist.
- #688 completed public explorer checklist navigation alignment.
- Public validator and public explorer planning should not be repeated unless new repository evidence appears.

## Completed HC Control Bot advisory comment governance sequence

- #701 documented the HC Control Bot advisory comment boundary.
- #794 documented the advisory comment lifecycle.
- #795 documented the advisory comment template.
- #796 linked the HC Control Bot reference chain in the Operator Entry Map.
- #823 added advisory human reviewer-role suggestions to HC Control Bot output and advisory comments while preserving advisory-only boundaries.
- #824 synchronized the HC Control Bot MVP roadmap after #823 so reviewer-role suggestions are recorded as advisory-only implementation state.
- HC Control Bot scanner, advisory comment, reviewer-role suggestions, and `/hc` command surfaces remain advisory-only and do not create approval, rejection, merge, close, label, assignment, reviewer request, LLM review, production-readiness, certification, or truth-finality authority.

## Recent completed assistant-console maintenance

- #811 recorded the assistant console rotation plan as completed operating-layer planning evidence.
- #812 is the active HC Assistant Console v2 reference for current assistant-console work.
- #763 is closed and retained only as the historical first smoke-test trail.
- #813 synchronized `/hc status`, command tests, and active-console documentation references with #812 as active.
- #814 synchronized the assistant listener smoke-test checklist with the current rotation state.
- #826 recorded the HC Engineer / HC Assistant command-surface status checkpoint.
- #828 recorded the repository assistant baseline status.
- #831 synchronized the Operator Entry Map after #826/#828 so command-surface and repository-assistant baseline references are current.
- #811, #813, #814, #826, #828, and #831 are do-not-repeat references for assistant-console, command-surface, repository-assistant baseline, or operator-entry-map synchronization unless new repository evidence appears.

## Current focus

- Keep onboarding, navigation, and project-control documents synchronized with current repository state.
- Continue the working verification core in small, reviewable slices.
- First practical layer is local package integrity: manifest + SHA-256 + missing/conflicting evidence + local CLI entry point + sample package.
- HC Trust Engineer report and task-planning helpers now provide local operator evidence and planning discipline for small PR flow.
- Signature/witness planning and signature/witness fixture-format planning now exist as documentation-only next-layer boundaries; implementation remains parked unless explicitly authorized.
- GitHub issue/comment assisted PR creation was tested as diagnostic evidence; do not rely on reported success until GitHub source-of-truth confirms branch, PR, changed files, and checks.
- Later layers are non-canonical signature/witness fixture examples, QR/canonical-domain binding, C2PA/OpenTimestamps references, federation, dispute/governance, and public UX.
- Avoid repeating completed public validator/public explorer planning, HC Control Bot comment governance, HC Control Bot reviewer-role roadmap synchronization, HC Engineer command-surface status checkpointing, repository assistant baseline work, operator-entry-map synchronization, assistant-console rotation, telemetry contract, replay / continuity, runtime stabilization review, validator pipeline nested response contract work, verification package hash-core/CLI/sample work, report-generator work, task-planner work, signature/witness proposal work, signature/witness fixture-format proposal work, or GitHub PR-flow diagnostic work unless new repository evidence appears.

## Next safe task

The next safe task is either:

1. A non-canonical verification-package fixture/example that demonstrates the documented `signature_proof` and `witness_proof` fixture shapes without touching protected implementation paths; or
2. A small verification-package fixture/example improvement that demonstrates existing behavior without changing validators, schemas, records, signing, federation, policy, runtime code, or workflows.

Recommended decision language after this synchronization is complete: **SIGNATURE-WITNESS FIXTURE STATE SYNCHRONIZED**.

## Shift-change checklist

Use `docs/project-control/shift-change-checklist.md` for the full operator handoff checklist. Minimum handoff steps are:

1. Read the project-control files in the documented order before proposing work.
2. Reconcile current state against repository evidence, changed files, recent commits or PRs, checks, and task-ledger notes.
3. Check in with role, scope, intended files, protected-path assessment, expected checks, and any evidence gaps.
4. Use `docs/project-control/active-work-registry.md` only as an advisory shift-level coordination snapshot when active, blocked, parked, or checkout status needs to be recorded.
5. Check out with changed files, commit or PR references when available, checks run, unresolved gaps, and next safe action.
6. Attach an evidence bundle that includes task reference, changed files, checks, review notes when available, and stale-context observations.

## Stale-context guidance

Markdown project-control docs are authoritative for shift handoff, current focus, safe next work, and do-not-repeat boundaries. The `hc_context` directory is advisory agent context and may lag behind markdown docs, merged files, checks, PR records, protected indexes, or human review decisions. If `hc_context` or chat memory conflicts with markdown project-control docs or other repository evidence, report the mismatch in the handoff notes instead of resolving or rewriting state automatically.

## Operating rule

Every agent must read this file before proposing work. Do not rely on chat memory alone, and do not repeat merged, superseded, abandoned, or closed work.
