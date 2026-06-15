# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is report-only unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator and public explorer planning/navigation are synchronized through #821/#822. HC Control Bot, assistant-console, repository assistant baseline, and operator-entry-map state are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core and local CLI sequence is complete through #843. HC Trust Engineer report generator, import fix, status checkpoint, and quickstart examples are complete through #872/#873/#874/#875. HC Engineer task planner, skipped-check/manual-review hardening, operator quickstart, and state synchronization are complete through #888/#889/#890/#891. Signature/witness planning, GitHub issue/comment PR-flow diagnostic evidence, signature/witness fixture-format planning, non-canonical signature/witness fixture package evidence, quickstart navigation, and fixture output-mode clarification are recorded through #892/#893/#894/#896/#898/#900/#949. Repository inventory ledger, test-anchor detection, category-specific Markdown inventory views, actor/PR trace evidence, large-repo governance automation baseline, governance automation review findings follow-up, CODEOWNERS protected governance ownership metadata classification, AI Agent Supply-Chain Threat Model work, and #978 late-review follow-up are complete through #967/#968/#970/#973/#976/#977/#978/#979 and this phase. |
| Next up | Use generated repository inventory artifacts, ruleset readiness reports, Scorecard advisory signals, and release audit reports as human-reviewed evidence before proposing any cleanup or authority change. Do not repeat completed task-planner, report-generator, verification package, bot, public-validator, public-explorer, signature/witness proposal, fixture-format proposal, fixture-package, quickstart navigation, fixture output-mode clarification, PR-flow diagnostic work, or repository inventory ledger/category-view work. |
| Blocked / parked work | Larger trust layers, issue-comment based autonomous PR creation, fully autonomous issue -> Codex -> PR bridge, VPS runners, GitHub App runners, auto-merge authority, label/assignment/reviewer-request automation, approval/rejection/close authority, signing implementation, witness authority, real GitHub settings enforcement by administrators, and authority-changing automation remain parked unless explicitly authorized and reviewed. |
| Do-not-repeat references | #628, #629, #630, #631, #820/#821/#822, #823/#824, #826, #828, #831, #834, #838, #839, #841, #843, #872, #873, #874, #875, #888, #889, #890, #891, #892, #893, #894, #896, #898, #900, #949, #967, #968, #970, #973, #976, #977, #978, and #979 are completed references. #812 remains active console and #763 remains historical only. |
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
14. `docs/project-control/inventory-ledger-completion-status.md`

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
- Do not repeat #872/#873/#874/#875 unless new evidence appears.

## Completed HC Engineer task planner slice

- #888 added a local deterministic advisory task planner for one-open-PR discipline, review order, merge gates, and post-merge cleanup.
- #889 hardened the planner after Codex review so skipped checks and scanner human-review signals require human review and block merge guidance.
- #890 added the operator quickstart for planner usage, output fields, and required blocker examples.
- #891 synchronized project-control state after the task planner quickstart.
- The planner remains local, deterministic, public-safe, advisory-only, and `truth_guarantee=false`.
- It does not create approval, rejection, merge, close, label, assignment, reviewer-request, external network, LLM, or truth-finality authority.
- Do not repeat #888/#889/#890/#891 unless new repository evidence appears.

## Completed signature/witness and PR-flow diagnostic slice

- #892 added a docs-only signature/witness verification proposal.
- #893 tested GitHub issue/comment based new-PR creation as diagnostic evidence and is closed as completed.
- #894 added a docs-only GitHub PR-flow note.
- #896 added a docs-only signature/witness fixture-format proposal.
- #898 added a non-canonical signature/witness fixture package plus test coverage for local-only advisory behavior.
- The diagnostic outcome: assistant or Codex claims about branch/commit/PR creation must be verified against GitHub source-of-truth. If the branch or PR is not visible in GitHub, it is not complete.
- Use controlled assistant/GitHub connector PR creation for new PRs and Codex primarily for PR-context review/fix assistance.
- The signature/witness fixture-format proposal and example package are not signing implementation, witness authority, identity finality, C2PA/OpenTimestamps/W3C VC verification, federation, or production readiness.

## Completed signature/witness fixture quickstart navigation

- #900 linked the non-canonical signature/witness fixture package from the verification package CLI quickstart and recorded the local JSON verifier command for inspection.
- #949 clarified that fixture-specific `signatures_verified=false` and `witnesses_verified=false` keys are visible in full JSON verifier output, while `--summary` remains a shorter operator summary view.
- These updates are documentation-only navigation and output-mode clarification. They do not add signing implementation, witness authority, identity finality, federation, production readiness, certification, legal truth, or guaranteed correctness.
- Do not repeat #900 or #949 unless new repository evidence appears.

## Completed repository inventory ledger slice

- #967 added `scripts/hc_repo_inventory.py`, tests, documentation, and a read-only report workflow that uploads JSON/Markdown repository inventory artifacts.
- #968 improved test-anchor detection so inventory entries can link source and script files to exact, prefix-style, or reference-based tests.
- #970 added category-specific Markdown views for latest changes, tests, source, workflows, docs, records/schema/protected, and review-needed entries while keeping JSON output backward compatible.
- #973 added actor and PR trace evidence to inventory outputs.
- The inventory ledger remains advisory-only, public-safe, `truth_guarantee=false`, inventory-only, and non-mutating. Repository inventory artifacts now have a GitHub-native attestation path when workflow permissions and platform support are available.
- Do not repeat #967/#968/#970/#973 unless new repository evidence appears.

## Completed governance/security hardening follow-up

- #976 completed governance automation review findings follow-up.
- #977 completed `.github/CODEOWNERS` protected governance ownership metadata classification.
- #978 added the AI Agent Supply-Chain Threat Model at `docs/security/ai-agent-supply-chain-threat-model.md`.
- #979 completed the late-review follow-up for #978.
- Treat #976/#977/#978/#979 as do-not-repeat references unless new repository evidence appears.
- This state remains `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and subject to human final authority. It does not claim complete security, production readiness, objective truth, autonomous governance authority, or runtime/security feature readiness.


## Completed large-repo governance automation baseline

- This phase adds a CODEOWNERS baseline, local ruleset readiness reporting, GitHub-native inventory artifact attestation, OpenSSF Scorecard advisory evidence, and a deterministic release audit checker.
- The baseline remains `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and human-review-required.
- Codex issue-to-PR automation, auto-merge authority, approve/reject/close/label/assign/reviewer-request authority, and real GitHub settings enforcement remain parked.
- Scorecard runs as advisory JSON artifact evidence only; SARIF upload is intentionally not enabled in this baseline.
- Release audit automation does not publish releases, create tags, modify changelogs, or claim release readiness by itself.

## 1. Candidate next working-core PR

- Priority order: 1
- Mode: report/docs/test/sample only unless separately authorized.
- Candidate: review generated repository inventory artifacts for test inventory evidence and branch-count evidence before any cleanup or rewrite proposal.
- Safe output: a small report, documentation update, or test/sample-only improvement that preserves advisory-only, public-safe, and `truth_guarantee=false` boundaries.
- Why it is next: #967/#968/#970/#973 completed the repository inventory ledger, smarter test-anchor detection, category-specific Markdown views, and actor/PR trace evidence. Remaining safe work should use generated evidence before changing source, tests, branches, protected paths, or authority boundaries.

## 2. Parked larger implementation work

- Priority order: 2
- Mode: blocked unless explicitly authorized.
- Parked examples: issue-comment based autonomous PR creation, VPS runner, GitHub App runner, label application, assignment, reviewer requests, signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. Advisory context may lag behind merged repository evidence.
