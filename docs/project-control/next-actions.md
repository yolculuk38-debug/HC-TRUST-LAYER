# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Repository cleanup phase 1 mapping, the 2026-07-22 branch cleanup, Public Validator QR/demo hardening, the deterministic combined local QR/Public Validator CLI, the installed-CLI checkout-root repair, and the report-only review-timing audit are complete through #1225. All 36 hold branches were preserved; phase 2 and later Public Validator slices must stay small, reversible, evidence-backed, and human-reviewed.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, `remote-branch-inventory-2026-07-22.md` for the complete branch snapshot and cleanup execution record, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. The completed 76-branch operation does not authorize deletion of the 36 hold branches, later branches, files, issues, workflows, records, or any repository authority.

Repository structure cleanup now has a completed purpose-index chain. Use `repository-index-chain-2026-06-16.md` before proposing structure work, use `first-safe-repo-plan-2026-06-16.md` for the first safe follow-up path, and use `repository-cleanup-phase1-checkpoint-2026-06-16.md` as the phase 1 completion checkpoint.

Workflow noise-reduction status after #1005 through #1009:

A. `docs-drift.yml` main-push scope reduced by #1005 while preserving evidence-path coverage.
B. `terminology.yml` main-push scope reduced by #1006 while preserving terminology boundary coverage.
C. `verification-package-schema.yml` main-push scope reduced by #1007 while preserving schema/example coverage.
D. `archive.yml` branch-push noise reduced by #1008 by limiting archive automation to `main` plus existing path filters.
E. `workflow-map-index-2026-06-16.md` synchronized through #1008 by #1009.

Current immediate operator path:

1. Treat #1210/#1211 branch inventory, state synchronization, and approved 76-branch cleanup as complete. Preserve the 36 hold branches.
2. Treat #1216 bundled `record_id` runner alignment, #1217 single scannable demo QR entry, #1219 live navigation/fail-closed hardening, #1220 task-handoff test repair, #1222 combined CLI, #1223 installed-CLI root repair, and #1225 report-only review-timing audit as complete. Do not recreate these slices.
3. Keep the three intentional issue surfaces distinct and open unless explicitly superseded: #812 HC Assistant Console v2, #1082 HC Signal Watch Console, and #1109 HC Mission Control / Active Task Queue.
4. Treat #1005-#1009 workflow noise reduction, #1161-#1166 public surface work, #1197-#1203 HC Council local report-only/command bridge work, #1205 CodeQL default-setup boundary, and #1209 QR compatibility repair as completed lines, not active TODOs.
5. Use `repository-index-chain-2026-06-16.md` to locate the root, docs, src, scripts, generated/reference, historical/evidence, and public/demo indexes.
6. Use `repository-cleanup-phase1-checkpoint-2026-06-16.md` to confirm phase 1 completion and `first-safe-repo-plan-2026-06-16.md` before proposing a structure change.
7. Use `pr-review-timing-audit-2026-07-25.md` as the evidence source for one documentation-only alignment of the review-window, mission-execution, lifecycle, final-reviewer, and PR-template wording. Preserve the 90-second minimum anti-rush window, but require matching current-head Codex evidence or an explicit exact-head human exception before merge guidance. Do not change workflows, permissions, required checks, auto-merge behavior, or authority.
8. HC Control Bot, HC Trust Engineer Agent, and HC Council local runner remain GitHub-native or local advisory aids. Authority expansion remains parked.
9. Do not widen workflow permissions, enable auto-merge, delete workflows, remove checks, add uncontrolled issue-comment automation, or add label/assignment/reviewer/approval/merge/close authority without a new governance review.
10. Do not treat Automation Gate PASS or a fixed 90-second delay as proof that Codex reviewed the current head. Require matching current-head review evidence or a GitHub-recorded human exception for the exact current head before merge guidance. Before proposing new work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, and repository evidence.

## Parked work

The following remain parked unless explicitly authorized, scoped, reviewed, and validated:

- workflow permission expansion, schema, validator, record, policy, federation, signing, canonical, trust-kernel index, generated-artifact, or protected governance changes;
- signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims;
- issue-comment based autonomous PR creation, fully autonomous issue-to-PR bridges, VPS runners, GitHub App runners, auto-merge, label/assignment/reviewer-request automation, approval/rejection/close authority, or other authority-changing automation.
- deletion of any held or later branch without a fresh exact-target gate and explicit human approval.

## Immediate do-not-repeat summary

Completed public-validator and public-explorer planning, HC Control Bot, assistant-console, HC Council local report-only runner/command bridge, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, evidence artifact inspection, workflow noise reduction, repository purpose-index, repository index-chain, inventory passes, first safe repository plan, cleanup phase 1 checkpoint, CodeQL default-setup boundary, #1209 QR compatibility repair, #1210/#1211 branch inventory/cleanup, #1216 bundled `record_id` runner alignment, #1217 single scannable demo QR entry, #1219 live navigation/fail-closed hardening, #1220 task-handoff test repair, #1222 combined CLI, #1223 installed-CLI root repair, and #1225 review-timing audit should not be repeated unless new repository evidence or human reviewer direction identifies a concrete gap.

Use GitHub PR history for detailed completed-work history and `task-ledger.md` for milestone references. Do not list completed work as active next work in this file.

## Merge / review rule

Before merge, verify changed files, check results, review/Codex comments, risk scope, and review evidence tied to the current head SHA. Automation Gate PASS or an elapsed timer is not Codex-review evidence. Require matching current-head Codex evidence or an explicit exact-head human exception before merge guidance. If comments exist, fix them first. Human final authority remains the governance boundary.
