# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator / explorer planning and navigation are synchronized through #821/#822; HC Control Bot advisory comment governance/navigation, advisory reviewer-role suggestions, roadmap synchronization, assistant-console rotation state, HC Engineer command-surface status, repository assistant baseline status, and operator-entry-map navigation are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core was added in #838, hardened in #839, and exposed through the local CLI in #841. |
| Next up | Continue the working core in small scoped PRs only. Candidate next work: a minimal quickstart / sample package for `hc-trust verify-package`, followed later by signature/witness/QR/C2PA/OpenTimestamps layers. Do not reopen #838/#839/#841 hash-core and CLI work unless new repository evidence appears. |
| Blocked / parked work | Workflow, schema, validator, record, policy, federation, signing, trust-kernel index, generated artifact, QR/hash evidence format, governance-enforcement, and production-readiness claims remain parked unless explicitly authorized and validated. |
| Do-not-repeat references | Treat #628, #629, #630, #631, #682, #683, #685, #686, #688, #701, #794, #795, #796, #811, #813, #814, #820, #821, #822, #823, #824, #826, #828, #831, #834, #838, #839, and #841 as completed references. #812 remains the active HC Assistant Console v2 reference; #763 remains historical only. |
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

## Completed verification package hash core sequence

- #838 added `src/hc_trust/verification_package.py` and `tests/test_verification_package_hash_core.py`.
- The core verifies local `manifest.json`, listed file existence, SHA-256 digest matches, missing evidence, conflicting evidence, advisory-only status, public-safe status, and `truth_guarantee=false` output.
- #839 followed up on automated review findings and hardened manifest handling and path containment before treating a file as package evidence.
- #841 exposed the core through the existing `hc-trust` CLI as `hc-trust verify-package <package_path>`, printing the advisory JSON result and returning non-zero for non-verified packages.
- This is the first usable local verification-package integrity slice. It does not verify legal truth, QR authenticity, signatures, witnesses, C2PA assertions, OpenTimestamps attestations, federation state, or production readiness.
- Do not repeat #838/#839/#841 unless new repository evidence appears.

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
- #763 is closed and retained only as the historical first smoke-test trail; do not treat it as the active console or reopen it for rotation work.
- #813 synchronized `/hc status`, command tests, and active-console documentation references with #812 as active.
- #814 synchronized the assistant listener smoke-test checklist with the current rotation state.
- #826 recorded the HC Engineer / HC Assistant command-surface status checkpoint, including implemented `/hc` commands, current safe boundaries, and staged expansion guidance.
- #828 recorded the repository assistant baseline status, marking the current assistant foundation sufficient for advisory operating-layer use while parking future expansion behind separate scoped review.
- #831 synchronized the Operator Entry Map after #826/#828 so command-surface and repository-assistant baseline references are current.
- #811, #813, #814, #826, #828, and #831 are do-not-repeat references for assistant-console, command-surface, repository-assistant baseline, or operator-entry-map synchronization unless new repository evidence appears.

## Current focus

- Keep onboarding, navigation, and project-control documents synchronized with current repository state.
- Continue the working verification core in small, reviewable slices.
- First practical layer is local package integrity: manifest + SHA-256 + missing/conflicting evidence + local CLI entry point.
- Later layers are signature/witness verification, QR/canonical-domain binding, C2PA/OpenTimestamps references, federation, dispute/governance, and public UX.
- Avoid repeating completed public validator/public explorer planning, HC Control Bot comment governance, HC Control Bot reviewer-role roadmap synchronization, HC Engineer command-surface status checkpointing, repository assistant baseline work, operator-entry-map synchronization, assistant-console rotation, telemetry contract, replay / continuity, runtime stabilization review, validator pipeline nested response contract work, or verification package hash-core/CLI work unless new repository evidence appears.

## Next safe task

The next safe task is either:

1. A documentation-only synchronization after #841; or
2. A small docs/test-only quickstart or sample package that demonstrates `hc-trust verify-package <package_path>` without changing protected paths.

Recommended decision language after a navigation refresh is complete: **NAVIGATION REFRESH COMPLETE**.

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
