# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Working verification core / post-runtime stabilization.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates remain advisory only and are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority.

Workflow noise-reduction status after #1005 through #1009:

A. `docs-drift.yml` main-push scope reduced by #1005 while preserving evidence-path coverage.
B. `terminology.yml` main-push scope reduced by #1006 while preserving terminology boundary coverage.
C. `verification-package-schema.yml` main-push scope reduced by #1007 while preserving schema/example coverage.
D. `archive.yml` branch-push noise reduced by #1008 by limiting archive automation to `main` plus existing path filters.
E. `workflow-map-index-2026-06-16.md` synchronized through #1008 by #1009.

Current immediate operator path:

1. Treat #1005, #1006, #1007, #1008, and #1009 as completed workflow noise-reduction follow-up, not active work.
2. Do not widen workflow permissions, enable auto-merge, delete workflows, remove checks, or change authority boundaries from cleanup candidates.
3. Keep write-capable or authority-adjacent workflows parked unless a future human-reviewed PR has a concrete reason, narrow diff, green checks, and no unresolved review comments.
4. Before proposing new work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, and repository evidence.

## Parked work

The following remain parked unless explicitly authorized, scoped, reviewed, and validated:

- workflow permission expansion, schema, validator, record, policy, federation, signing, canonical, trust-kernel index, generated-artifact, or protected governance changes;
- signing implementation, witness authority, QR/canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, and production-readiness claims;
- issue-comment based autonomous PR creation, fully autonomous issue-to-PR bridges, VPS runners, GitHub App runners, auto-merge, label/assignment/reviewer-request automation, approval/rejection/close authority, or other authority-changing automation.

## Immediate do-not-repeat summary

Completed public-validator, public-explorer, HC Control Bot, assistant-console, validator pipeline, verification package, HC Trust Engineer, HC Engineer planner, signature/witness planning, PR-flow diagnostic, repository inventory, governance automation, governance evidence review, evidence artifact inspection, and workflow noise-reduction work should not be repeated unless new repository evidence or human reviewer direction identifies a concrete gap.

Use GitHub PR history for detailed completed-work history and `task-ledger.md` for milestone references. Do not list completed work as active next work in this file.

## Merge / review rule

Before merge, verify changed files, check results, review/Codex comments, and risk scope. If comments exist, fix them first. Human final authority remains the governance boundary.
