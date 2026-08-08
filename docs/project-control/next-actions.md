# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Independent external audit hardening is the active bounded phase. P0-1 was completed by #1229 and P0-2 by #1230. P0-3 is implemented in the current change and remains subject to current-head checks, review evidence, and human merge authority. P0-4 has not started.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, `remote-branch-inventory-2026-07-22.md` for the complete branch snapshot and cleanup execution record, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. The completed 76-branch operation does not authorize deletion of the 36 hold branches, later branches, files, issues, workflows, records, or any repository authority.

Repository structure cleanup now has a completed purpose-index chain. Use `repository-index-chain-2026-06-16.md` before proposing structure work, use `first-safe-repo-plan-2026-06-16.md` for the first safe follow-up path, and use `repository-cleanup-phase1-checkpoint-2026-06-16.md` as the phase 1 completion checkpoint.

Use [`independent-external-audit-p0-status.md`](independent-external-audit-p0-status.md) for the current P0 closeout evidence and remaining gate. It is separate from the historical #905-#923 outside-review notes.

Workflow noise-reduction status after #1005 through #1009:

A. `docs-drift.yml` main-push scope reduced by #1005 while preserving evidence-path coverage.
B. `terminology.yml` main-push scope reduced by #1006 while preserving terminology boundary coverage.
C. `verification-package-schema.yml` main-push scope reduced by #1007 while preserving schema/example coverage.
D. `archive.yml` branch-push noise reduced by #1008 by limiting archive automation to `main` plus existing path filters.
E. `workflow-map-index-2026-06-16.md` synchronized through #1008 by #1009.

Current immediate operator path:

1. Treat P0-1/#1229 and P0-2/#1230 as completed, evidence-backed findings. Do not recreate their slices.
2. Keep P0-3 limited to one Draft 2020-12 record schema, the shared validator, version/profile declarations, and their direct runtime, record, packaging, test, and documentation consumers. Require protected-path and exact-record review.
3. Do not open P0-4 implementation while P0-3 remains open. After P0-3 closes, inventory cryptographic-strength names and contain, rename, or relabel only the unsupported claims in one bounded slice.
4. Keep the three intentional issue surfaces distinct and open unless explicitly superseded: #812 HC Assistant Console v2, #1082 HC Signal Watch Console, and #1109 HC Mission Control / Active Task Queue.
5. Treat #1210/#1211 branch cleanup, #1216-#1225 Public Validator/review-timing work, #1005-#1009 workflow noise reduction, #1161-#1166 public surface work, #1197-#1203 HC Council work, #1205 CodeQL boundary, and #1209 QR compatibility repair as completed lines.
6. Use `repository-index-chain-2026-06-16.md` and `repository-cleanup-phase1-checkpoint-2026-06-16.md` before proposing repository-structure work. Preserve the 36 hold branches.
7. HC Control Bot, HC Trust Engineer Agent, and HC Council local runner remain GitHub-native or local advisory aids. Authority expansion remains parked.
8. Do not widen workflow permissions, enable auto-merge, delete workflows, remove checks, add uncontrolled issue-comment automation, or add label/assignment/reviewer/approval/merge/close authority without a new governance review.
9. Continue to use `pr-review-timing-audit-2026-07-25.md` for the current-head review-evidence contract. A timer or Automation Gate PASS is not proof of Codex review completion.
10. Before proposing or merging work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, changed files, checks, and current-head review evidence.

## Parked work

The following remain parked unless explicitly authorized, scoped, reviewed, and validated:

- workflow permission expansion, schema, validator, record, policy, federation, signing, canonical, trust-kernel index, generated-artifact, or protected governance changes;
- signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims;
- issue-comment based autonomous PR creation, fully autonomous issue-to-PR bridges, VPS runners, GitHub App runners, auto-merge, label/assignment/reviewer-request automation, approval/rejection/close authority, or other authority-changing automation.
- deletion of any held or later branch without a fresh exact-target gate and explicit human approval.

The current P0-3 work is an explicitly scoped exception for schema, validator,
record metadata, and direct consumers; it does not authorize broader protected-
path work.

## Immediate do-not-repeat summary

Completed public-validator and public-explorer planning, HC Control Bot, assistant-console, HC Council local report-only runner/command bridge, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, evidence artifact inspection, workflow noise reduction, repository purpose-index, repository index-chain, inventory passes, first safe repository plan, cleanup phase 1 checkpoint, CodeQL default-setup boundary, #1209 QR compatibility repair, #1210/#1211 branch inventory/cleanup, #1216-#1225 Public Validator/review-timing work, P0-1/#1229, and P0-2/#1230 should not be repeated unless new repository evidence or human reviewer direction identifies a concrete gap.

Use GitHub PR history for detailed completed-work history and `task-ledger.md` for milestone references. Do not list completed work as active next work in this file.

## Merge / review rule

Before merge, verify changed files, check results, review/Codex comments, risk scope, and review evidence tied to the current head SHA. Automation Gate PASS or an elapsed timer is not Codex-review evidence. Require matching current-head Codex evidence or an explicit exact-head human exception before merge guidance. If comments exist, fix them first. Human final authority remains the governance boundary.
