# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Working verification core / post-runtime stabilization.

## Next safe actions

Cleanup navigation now follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates remain advisory only and are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority.

Active cleanup sequence:

A. docs navigation cleanup
B. test duplicate inventory
C. workflow cleanup recommendation
D. issue cleanup with human approval
E. branch cleanup with human approval

1. Complete the docs navigation cleanup from #993 item A without deleting, moving, renaming, archiving, or changing files outside the allowed project-control docs.
2. Park test duplicate inventory, workflow cleanup recommendations, issue cleanup, and branch cleanup until their separate scoped review steps.
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
