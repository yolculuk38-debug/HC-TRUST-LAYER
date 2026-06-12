# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is report-only unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator and public explorer planning/navigation are synchronized through #821/#822. HC Control Bot, assistant-console, repository assistant baseline, and operator-entry-map state are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core was added in #838, hardened in #839, and exposed through `hc-trust verify-package` in #841. |
| Next up | Docs-only synchronization after #841, then a separate small sample or quickstart for `hc-trust verify-package`. |
| Blocked / parked work | Larger trust layers remain parked unless explicitly authorized and reviewed. |
| Do-not-repeat references | #628, #629, #630, #631, #820/#821/#822, #823/#824, #826, #828, #831, #834, #838, #839, and #841 are completed references. #812 remains active console and #763 remains historical only. |
| Review / merge rule | Before merge: verify changed files, checks, Codex/review comments, and risk scope. If comments exist, fix first. Human final authority remains the governance boundary. |
| Source-of-truth priority | Markdown project-control docs and repository evidence outrank `hc_context`, chat memory, and advisory summaries. |

## Shift-change read order

Before taking the next action, read:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/START_HERE.md`
4. `docs/project-control/project-state.md`
5. `docs/project-control/agent-operating-model.md`
6. `docs/project-control/task-ledger.md`
7. `docs/project-control/next-actions.md`
8. `docs/project-control/active-work-registry.md`
9. `docs/project-control/shift-change-checklist.md`
10. `docs/project-control/operator-entry-map.md`
11. `docs/project-control/hc-engineer-command-surface-status.md`
12. `docs/project-control/repository-assistant-baseline-status.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination.

## Completed public validator / public explorer planning sequence

- Public validator planning navigation was linked in #682.
- #820 added the official documentation-only Public Validator MVP Specification.
- #821 and #822 synchronized navigation and project-control state after #820.
- Public explorer navigation and planning work was completed through #683, #685, #686, and #688.
- Do not repeat this planning sequence unless new repository evidence appears.

## Completed HC Control Bot and assistant-console maintenance

- HC Control Bot advisory comment governance and roadmap state are completed through #701, #794, #795, #796, #823, and #824.
- Assistant-console, HC Engineer command-surface, repository assistant baseline, and operator-entry-map state are completed through #811, #812, #813, #814, #826, #828, and #831.
- These documents and features do not create independent authority, production readiness, certification, or truth-finality.

## Completed validator pipeline test hardening

- #834 locked nested `ValidatorPipeline` response contract coverage for `canonical_bridge`, `schema_result`, `hash_result`, `trust_assignment`, and `escalation`.
- Do not repeat validator pipeline nested response contract test work unless new repository evidence appears.

## Completed verification package hash core

- #838 added a local verification package hash core.
- #839 hardened that core after automated review by handling malformed manifest files without raising and checking resolved file location before hashing.
- #841 exposed the core as `hc-trust verify-package <package_path>`.
- This core verifies local package integrity only: manifest presence, listed file existence, SHA-256 digest matches, missing evidence, conflicting evidence, advisory-only output, public-safe output, and `truth_guarantee=false`.
- It does not verify legal truth, identity, witness authority, media provenance, timestamp attestations, network state, or production readiness.
- Do not repeat #838/#839/#841 unless new repository evidence appears.

## 1. Docs-only synchronization after #841

- Priority order: 1
- Mode: docs only.
- Safe output: project-control docs reflect #841 and do-not-repeat boundaries.
- Why it is next: project-control must match merged code/test state before the next working-core slice.

## 2. Candidate next working-core PR

- Priority order: 2
- Mode: docs/test sample only unless separately authorized.
- Candidate: add a minimal sample package or quickstart for `hc-trust verify-package <package_path>`.
- Safe output: a small example and/or quickstart that demonstrates the existing verifier response without changing protected areas.
- Why it is next: the package hash core and CLI exist; a sample package makes the core practically usable before larger trust layers.

## 3. Parked larger implementation work

- Priority order: 3
- Mode: blocked unless explicitly authorized.
- Parked examples: witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. Advisory context may lag behind merged repository evidence.
