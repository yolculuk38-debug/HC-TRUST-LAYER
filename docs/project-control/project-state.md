# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Core file role

This file is the factory general status report / shift handoff summary. It summarizes the current phase, active focus, protected boundaries, source-of-truth priority, and major completed blocks only. It must not become a detailed per-PR history.

Shared factory model:

- `project-state.md` = factory general status report
- `next-actions.md` = short shift board
- `task-ledger.md` = phase/milestone ledger
- GitHub PR history = detailed work record
- Issues = work orders when needed

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Active operator views now point to current safe follow-up only. Completed verification, planner, inventory, governance, and evidence-inspection blocks are historical references, not active work. Candidate current work is limited to small human-reviewed documentation follow-up when new repository evidence or reviewer direction identifies a concrete gap. |
| Next up | Keep the next action scoped, documentation-first, and reviewable. Cross-check GitHub PR history and `task-ledger.md` before reopening any completed topic. |
| Blocked / parked work | Workflow, schema, validator, record, policy, federation, signing, trust-kernel index, generated artifact, QR/hash evidence format, governance-enforcement, authority-changing automation, source deletion/archival, and production-readiness claims remain parked unless explicitly authorized and validated. |
| Do-not-repeat summary | Completed public-validator/explorer, HC Control Bot, assistant-console, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, and evidence artifact inspection work should not be repeated without new evidence or reviewer direction. |
| Review / merge rule | Before merge: verify changed files, checks, review comments, and risk scope. Human final authority remains the governance boundary. |
| Source-of-truth priority | Markdown project-control docs and repository evidence outrank `hc_context`, chat memory, and advisory summaries. |


## Cleanup navigation status

The #993 repository cleanup audit is the cleanup source-of-truth: [`repository-cleanup-audit-2026-06-15.md`](repository-cleanup-audit-2026-06-15.md). Use [`next-actions.md`](next-actions.md) for active shift work, this file for current project state, [`task-ledger.md`](task-ledger.md) for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates are advisory only; they are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority. Issue #812 HC Assistant Console v2 remains `ACTIVE_KEEP` unless explicitly superseded by human review.

Cleanup sequence status: A. docs navigation cleanup completed by #994; B. report-only test duplicate inventory completed by #995; C. report-only workflow cleanup recommendation completed by #996. Live operator review found only #812 HC Assistant Console v2 remains open and it stays `ACTIVE_KEEP`; no other open issue cleanup action is currently available. Closed issues are not deletion targets because they preserve audit/history context. Branch cleanup remains open for complete branch-list triage: the previous connector check only confirmed no current `codex/cleanup` prefix candidates and must not be treated as a full remote branch cleanup review. Branch deletion remains parked unless a future complete branch-list review proves a branch is merged, stale, unused by open PRs, and human-approved. Next safe action is no destructive cleanup work; only future evidence-triggered report-only work; if maintainers want more cleanup, create a targeted docs/report-only issue or PR first.

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
- #898 signature/witness fixture package: added a non-canonical example package and test that demonstrate local fixture evidence while keeping `signatures_verified=false`, `witnesses_verified=false`, and `truth_guarantee=false`.
- #900 verification package quickstart update: linked the signature/witness fixture package from the CLI quickstart and recorded the local command to inspect it.
- #905-#919 outside-review and inventory-follow-up: triaged outside-review claims against repository evidence, added source inventory support, locked normalizer safety behavior, corrected integration-test status, recorded source-tree/security-policy/branch-count finding status, added source inventory review checklist, and synchronized project-control state.
- #974 HC Large-Repo Operating Model: completed documentation for large-repo operating boundaries.
- #975 large-repo governance automation baseline: completed baseline evidence path for ruleset readiness, Scorecard advisory signals, release audit review, and inventory artifacts without authority-changing automation.
- #976 governance automation review findings follow-up: completed follow-up for governance automation review findings while preserving advisory-only, public-safe, truth_guarantee=false, and human final authority boundaries.
- #977 CODEOWNERS protected governance ownership metadata classification: recorded `.github/CODEOWNERS` as protected governance ownership metadata without adding bot authority, reviewer-request automation, labels, assignments, or production-readiness claims.
- #978 AI Agent Supply-Chain Threat Model: added `docs/security/ai-agent-supply-chain-threat-model.md` as an advisory security review aid for AI-agent and repository supply-chain risks.
- #979 late-review follow-up for #978: addressed AI Agent Supply-Chain Threat Model review findings after #978 without claiming complete security or changing runtime/security feature readiness.
- #980 project-control security hardening sync: completed project-control security hardening synchronization as a do-not-repeat reference.
- #981 Governance Evidence Review Checklist: added `docs/project-control/governance-evidence-review-checklist.md` for human-reviewed generated evidence before cleanup, ruleset, workflow, release, or authority-changing action.
- #982 Governance Evidence Checklist State note: recorded the checklist state and preserved `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and human final authority boundaries.

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
- #898 added `examples/verification-package/signature-witness-fixture/` plus test coverage for the non-canonical local fixture package.
- #900 linked the signature/witness fixture package from `docs/verification-package-cli-quickstart.md`.
- The diagnostic outcome is that assistant-generated success claims must be checked against GitHub source-of-truth: branch visibility, PR visibility, changed files, checks, and merge state.
- Do not treat issue/comment based new-PR creation as reliable without repository evidence. Use PR-context review/fix assistance only after a real GitHub PR exists.
- Do not treat the signature fixture proposal, example package, or quickstart navigation as signing implementation, witness authority, identity finality, C2PA/OpenTimestamps/W3C VC verification, federation, or production readiness.

## Completed outside-review and inventory-follow-up sequence

- #905 added the initial outside-review triage and separated confirmed evidence from unverified findings.
- #906 added source inventory triage after direct repository searches.
- #907 added the non-mutating source inventory reporter and tests.
- #908 updated finding status after early verification.
- #909 locked `src/normalize_records.py` safe-write behavior with tests.
- #910 added the initial test inventory note.
- #911 corrected the root-level integration test note after `test_integration.py` was found.
- #912 added integration-test finding status.
- #913 synchronized the main triage table.
- #914 added source-tree finding status.
- #915 added security-policy finding status.
- #916 added the external audit follow-up checkpoint and synchronized the task ledger.
- #918 added branch-count finding status after connector branch searches did not confirm the reported branch-count concern.
- #919 added a source inventory review checklist and cleanup gate.
- The completed decision is: do not treat outside-review claims as repository truth without GitHub evidence; do not delete, move, archive, or rewrite source/tests from name-based assumptions; use inventory evidence first.
- Remaining care items are source inventory output review, test inventory review, and branch-count confirmation through reliable branch listing or manual GitHub UI verification.

## Completed governance/security hardening sequence

- #974 completed the HC Large-Repo Operating Model.
- #975 completed the large-repo governance automation baseline.
- #976 completed governance automation review findings follow-up.
- #977 completed `.github/CODEOWNERS` protected governance ownership metadata classification.
- #978 added the AI Agent Supply-Chain Threat Model at `docs/security/ai-agent-supply-chain-threat-model.md`.
- #979 completed the late-review follow-up for the #978 threat model.
- #980 completed project-control security hardening synchronization.
- These entries, plus #981/#982/#985/#987, are do-not-repeat references for the same governance/security hardening, governance evidence checklist state sync, generated governance evidence review, and artifact-inspection guidance unless new repository evidence appears.
- The state remains `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and human final authority remains required. This sequence does not claim complete security, production readiness, objective truth, autonomous governance authority, or any runtime/security feature readiness.

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
- Signature/witness planning, signature/witness fixture-format planning, a non-canonical signature/witness fixture package, and quickstart navigation now exist as documentation/example next-layer boundaries; implementation remains parked unless explicitly authorized.
- Outside-review and inventory follow-up are synchronized through #919. Use repository evidence first; do not act on unverified outside-review claims.
- GitHub issue/comment assisted PR creation was tested as diagnostic evidence; do not rely on reported success until GitHub source-of-truth confirms branch, PR, changed files, and checks.
- Later layers are example navigation, demo index references, QR/canonical-domain binding, C2PA/OpenTimestamps references, federation, dispute/governance, and public UX.
- Avoid repeating completed public validator/public explorer planning, HC Control Bot comment governance, HC Control Bot reviewer-role roadmap synchronization, HC Engineer command-surface status checkpointing, repository assistant baseline work, operator-entry-map synchronization, assistant-console rotation, telemetry contract, replay / continuity, runtime stabilization review, validator pipeline nested response contract work, verification package hash-core/CLI/sample work, report-generator work, task-planner work, signature/witness proposal work, signature/witness fixture-format proposal work, signature/witness example-package work, GitHub PR-flow diagnostic work, outside-review follow-up triage, branch-count finding status, source-inventory review checklist work, governance automation review findings follow-up, CODEOWNERS protected governance ownership metadata classification, AI Agent Supply-Chain Threat Model work, #978 late-review follow-up, Governance Evidence Review Checklist work, Governance Evidence Checklist State note work, generated governance evidence review work, or evidence artifact inspection guidance unless new repository evidence appears.

## Next safe task

The next safe task is human-reviewed follow-up only: record a small documentation note or report if repository evidence or a human reviewer identifies a concrete gap after #985/#987. Do not rerun or present the generated governance evidence review / artifact inspection sequence as the active next task. Do not delete, move, archive, rewrite source files, change workflows, change rulesets, change releases, or change authority from generated output alone.

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
