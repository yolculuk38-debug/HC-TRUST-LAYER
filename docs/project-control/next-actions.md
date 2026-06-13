# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is report-only unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator and public explorer planning/navigation are synchronized through #821/#822. HC Control Bot, assistant-console, repository assistant baseline, and operator-entry-map state are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core and local CLI sequence is complete through #843. HC Trust Engineer report generator, import fix, status checkpoint, and quickstart examples are complete through #872/#873/#874/#875. HC Engineer task planner, skipped-check/manual-review hardening, and operator quickstart are complete through #888/#889/#890. |
| Next up | A documentation-only synchronization after #890, then a narrow next trust-layer proposal or fixture/example improvement if new repository evidence justifies it. Do not repeat completed task-planner, report-generator, verification package, bot, public-validator, or public-explorer planning work. |
| Blocked / parked work | Larger trust layers and authority-changing automation remain parked unless explicitly authorized and reviewed. |
| Do-not-repeat references | #628, #629, #630, #631, #820/#821/#822, #823/#824, #826, #828, #831, #834, #838, #839, #841, #843, #872, #873, #874, #875, #888, #889, and #890 are completed references. #812 remains active console and #763 remains historical only. |
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
13. `docs/project-control/hc-trust-engineer-report-generator-status.md`

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
- #843 added a sample package and quickstart for the local verification package flow.
- This core verifies local package integrity only: manifest presence, listed file existence, SHA-256 digest matches, missing evidence, conflicting evidence, advisory-only output, public-safe output, and `truth_guarantee=false`.
- It does not verify legal truth, identity, witness authority, media provenance, timestamp attestations, network state, or production readiness.
- Do not repeat #838/#839/#841/#843 unless new repository evidence appears.

## Completed HC Trust Engineer report generator slice

- #872 added a local deterministic report-only generator that converts local JSON fixtures into advisory reports.
- #873 fixed direct script execution import behavior.
- #874 recorded the generator status and locked report-only boundaries.
- #875 added clean-docs and protected-path example fixtures plus a quickstart.
- The generator remains local, deterministic, report-only, public-safe, and advisory-only.
- It does not create approval, rejection, merge, close, label, assignment, reviewer-request, external network, or truth-finality authority.
- Do not repeat #872/#873/#874/#875 unless new repository evidence appears.

## Completed HC Engineer task planner slice

- #888 added a local deterministic advisory task planner for one-open-PR discipline, review order, merge gates, and post-merge cleanup.
- #889 hardened the planner after Codex review so skipped checks and scanner human-review signals require human review and block merge guidance.
- #890 added the operator quickstart for planner usage, output fields, and required blocker examples.
- The planner remains local, deterministic, public-safe, advisory-only, and `truth_guarantee=false`.
- It does not create approval, rejection, merge, close, label, assignment, reviewer-request, external network, LLM, or truth-finality authority.
- Do not repeat #888/#889/#890 unless new repository evidence appears.

## 1. Candidate next working-core PR

- Priority order: 1
- Mode: docs/test/sample only unless separately authorized.
- Candidate: after #890 state synchronization, prepare a narrow next trust-layer proposal or add a small fixture/example improvement only if it demonstrates existing behavior without changing protected areas.
- Safe output: a small example, test, or proposal that preserves advisory-only, public-safe, and `truth_guarantee=false` boundaries.
- Why it is next: report generator and task planner helper surfaces now exist; any next step should keep the same small scoped discipline and avoid authority expansion.

## 2. Parked larger implementation work

- Priority order: 2
- Mode: blocked unless explicitly authorized.
- Parked examples: issue comment integration, GitHub Actions integration for this generator, VPS runner, GitHub App runner, label application, assignment, reviewer requests, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. Advisory context may lag behind merged repository evidence.
