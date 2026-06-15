# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Working verification core / post-runtime stabilization.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates remain advisory only and are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority.

Cleanup sequence status after #993 through #996:

A. docs navigation cleanup — completed by #994.
B. report-only test duplicate inventory — completed by #995.
C. report-only workflow cleanup recommendation — completed by #996.
D. issue cleanup — checked; only #812 HC Assistant Console v2 remains open and it must stay `ACTIVE_KEEP`. Closed issues are audit/history records and must not be deletion targets.
E. branch cleanup remains open for complete branch-list triage. A previous connector check only confirmed no current `codex/cleanup` prefix candidates; it was prefix-specific only and was not a full remote branch cleanup review. Branch deletion remains parked unless a future complete branch-list review proves a branch is merged, stale, unused by open PRs, and human-approved.

1. Treat #994, #995, and #996 as completed cleanup audit follow-up steps, not active work.
2. Keep issue closure and branch deletion parked; do not delete files, close issues, delete branches, or change workflows from cleanup candidates.
3. Before proposing new work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, and repository evidence.

## Parked work

The following remain parked unless explicitly authorized, scoped, reviewed, and validated:

- workflow, schema, validator, record, policy, federation, signing, canonical, trust-kernel index, generated-artifact, or protected governance changes;
- signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims;
- issue-comment based autonomous PR creation, fully autonomous issue-to-PR bridges, VPS runners, GitHub App runners, auto-merge, label/assignment/reviewer-request automation, approval/rejection/close authority, or other authority-changing automation.

## Immediate do-not-repeat summary

Completed public-validator, public-explorer, HC Control Bot, assistant-console, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, and evidence artifact inspection work should not be repeated unless new repository evidence or human reviewer direction identifies a concrete gap.

Use GitHub PR history for detailed completed-work history and `task-ledger.md` for milestone references. Do not list completed work as active next work in this file.

## Merge / review rule

Before merge, verify changed files, check results, review/Codex comments, and risk scope. If comments exist, fix them first. Human final authority remains the governance boundary.
