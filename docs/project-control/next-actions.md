# Next Actions

This file is the short active shift board for HC-TRUST-LAYER. It should show only current operator work, parked work, immediate do-not-repeat reminders, and the merge/review rule.

Operating boundaries remain: `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`; human final authority remains required. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Current phase

Working verification core / post-runtime stabilization.

## Next safe actions

Cleanup navigation follows the repository cleanup audit from #993. Use `repository-cleanup-audit-2026-06-15.md` as the cleanup source-of-truth, this file for active shift work, `project-state.md` for current project state, `task-ledger.md` for milestone history, and GitHub PR history for detailed completed PR history. Cleanup candidates remain advisory only and are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority.

Cleanup sequence status:

A. docs navigation cleanup — completed by PR #994.
B. report-only test duplicate inventory — completed by PR #995.
C. report-only workflow cleanup recommendation — completed by PR #996.
D. issue cleanup status — live operator review found only #812 HC Assistant Console v2 remains open and it stays `ACTIVE_KEEP`; no other open issue cleanup action is currently available. Closed issues are not deletion targets because they preserve audit/history context.
E. branch cleanup status — live operator review found no current `codex/cleanup` branch candidates. Branch deletion remains parked unless a future branch is proven merged, stale, unused by open PRs, and human-approved.

1. Do not perform destructive cleanup work.
2. Only start future cleanup work when new repository evidence triggers a report-only review.
3. If maintainers want more cleanup, create a targeted docs/report-only issue or PR first.
4. Before proposing new work, cross-check `project-state.md`, `task-ledger.md`, current GitHub PR history, and repository evidence.

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
