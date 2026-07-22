# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Repository cleanup phase 1 mapping and the 2026-07-22 complete remote branch-list triage are evidence-complete. Destructive cleanup remains parked; phase 2 must stay small, reversible, evidence-backed, and human-reviewed.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, `remote-branch-inventory-2026-07-22.md` for the complete branch snapshot, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates remain advisory only and are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority.

Repository structure cleanup now has a completed purpose-index chain. Use `repository-index-chain-2026-06-16.md` before proposing structure work, use `first-safe-repo-plan-2026-06-16.md` for the first safe follow-up path, and use `repository-cleanup-phase1-checkpoint-2026-06-16.md` as the phase 1 completion checkpoint.

Workflow noise-reduction status after #1005 through #1009:

A. `docs-drift.yml` main-push scope reduced by #1005 while preserving evidence-path coverage.
B. `terminology.yml` main-push scope reduced by #1006 while preserving terminology boundary coverage.
C. `verification-package-schema.yml` main-push scope reduced by #1007 while preserving schema/example coverage.
D. `archive.yml` branch-push noise reduced by #1008 by limiting archive automation to `main` plus existing path filters.
E. `workflow-map-index-2026-06-16.md` synchronized through #1008 by #1009.

Current immediate operator path:

1. Review and merge the documentation-only remote branch inventory and project-control synchronization after all comments, threads, and checks are clear.
2. Treat the inventory's 76 branches as candidates only. Preserve the 36 hold branches. Any later deletion requires a fresh snapshot, exact target list, explicit human approval, a small batch, and post-action audit.
3. Keep the three intentional issue surfaces distinct and open unless explicitly superseded: #812 HC Assistant Console v2, #1082 HC Signal Watch Console, and #1109 HC Mission Control / Active Task Queue.
4. Treat #1005-#1009 workflow noise reduction, #1161-#1166 public surface work, #1197-#1203 HC Council local report-only/command bridge work, #1205 CodeQL default-setup boundary, and #1209 QR compatibility repair as completed lines, not active TODOs.
5. Use `repository-index-chain-2026-06-16.md` to locate the root, docs, src, scripts, generated/reference, historical/evidence, and public/demo indexes.
6. Use `repository-cleanup-phase1-checkpoint-2026-06-16.md` to confirm phase 1 completion and `first-safe-repo-plan-2026-06-16.md` before proposing a structure change.
7. After the current documentation synchronization, the next safe technical direction is the public validator / QR UX real-use path, demo runner/static viewer contract, `record_id` to advisory result flow, then runtime/protocol hardening. Keep each step small, evidence-backed, and human-reviewed.
8. HC Control Bot, HC Trust Engineer Agent, and HC Council local runner remain GitHub-native or local advisory aids. Authority expansion remains parked.
9. Do not widen workflow permissions, enable auto-merge, delete workflows, remove checks, add uncontrolled issue-comment automation, or add label/assignment/reviewer/approval/merge/close authority without a new governance review.
10. Before proposing new work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, and repository evidence.

## Parked work

The following remain parked unless explicitly authorized, scoped, reviewed, and validated:

- workflow permission expansion, schema, validator, record, policy, federation, signing, canonical, trust-kernel index, generated-artifact, or protected governance changes;
- signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims;
- issue-comment based autonomous PR creation, fully autonomous issue-to-PR bridges, VPS runners, GitHub App runners, auto-merge, label/assignment/reviewer-request automation, approval/rejection/close authority, or other authority-changing automation.
- branch deletion from the 2026-07-22 inventory without a fresh exact-target gate and explicit human approval.

## Immediate do-not-repeat summary

Completed public-validator and public-explorer planning, HC Control Bot, assistant-console, HC Council local report-only runner/command bridge, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, evidence artifact inspection, workflow noise reduction, repository purpose-index, repository index-chain, inventory passes, first safe repository plan, cleanup phase 1 checkpoint, CodeQL default-setup boundary, and #1209 QR compatibility repair should not be repeated unless new repository evidence or human reviewer direction identifies a concrete gap.

Use GitHub PR history for detailed completed-work history and `task-ledger.md` for milestone references. Do not list completed work as active next work in this file.

## Merge / review rule

Before merge, verify changed files, check results, review/Codex comments, and risk scope. If comments exist, fix them first. Human final authority remains the governance boundary.
