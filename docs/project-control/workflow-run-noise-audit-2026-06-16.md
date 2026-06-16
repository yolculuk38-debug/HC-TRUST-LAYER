# Workflow Run Noise Audit — 2026-06-16

## 1. Executive summary

This document is a report-only workflow run noise audit for HC-TRUST-LAYER after the repository cleanup sequence and branch cleanup triage.

No workflow runs are deleted by this report. No workflow files are changed. No workflows are disabled, renamed, moved, or removed. No source, tests, generated artifacts, records, schemas, validators, policy, federation, signatures, canonical files, trust-kernel files, issues, branches, or pull requests are changed.

The operator UI showed a large completed GitHub Actions history. Completed workflow runs are CI/audit history, not repository source files. Deleting old run history can reduce visible UI clutter, but it also removes diagnostic logs and review evidence. The safe cleanup direction is therefore to reduce future unnecessary workflow run volume before deleting past evidence.

Boundary values preserved by this audit:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human final authority remains required
- CI/checks are evidence, not trust authority
- generated artifacts are advisory evidence, not canonical records

## 2. Evidence reviewed

This audit builds on the existing report-only workflow cleanup recommendation:

- `docs/project-control/workflow-cleanup-recommendation-2026-06-15.md`

That earlier report classified workflows under `.github/workflows/**` and recommended no immediate workflow deletion, disablement, rename, move, or edit. It also identified auto-merge-related report-only workflows as overlap candidates and marked write-capable/comment-capable workflows as human-review-required.

Current live repository operating context at the time of this audit:

- No open PR cleanup action is required before this report.
- Issue #812 remains the active HC Assistant Console v2 reference and must stay ACTIVE_KEEP unless explicitly superseded by human review.
- The branch cleanup triage concluded no branch deletion now because complete remote branch evidence was not available.

## 3. What must not be cleaned by deletion first

Completed Actions runs should not be treated like stale repo files.

Do not use this audit to bulk-delete completed workflow runs unless a maintainer explicitly decides that losing old logs is acceptable. Historical runs can still be useful for:

- proving which checks ran for a PR or merge;
- diagnosing cancelled versus successful concurrency behavior;
- validating that governance, terminology, documentation drift, canonical artifact, and release audit checks existed at the time of a change;
- reconstructing project-control evidence during future audits.

This project prioritizes record integrity over visual tidiness. The safer goal is to reduce future noise, not erase past evidence.

## 4. Noise sources to review next

The likely future run-noise sources should be reviewed in this order.

| Area | Likely source of noise | Risk | Safe next action |
| --- | --- | --- | --- |
| Auto-merge boundary workflows | `enable-auto-merge.yml`, `safe-auto-merge.yml`, and `docs-auto-merge.yml` all report around merge policy boundaries. | Medium, because names are auto-merge-adjacent even when behavior is report-only. | Create a targeted docs/report PR comparing overlap and proposing a human-reviewed consolidation plan before any workflow edit. |
| Push-to-main plus PR duplication | Several guards run on both `pull_request` and `push` to `main`. | Medium, because some duplication is intentional post-merge evidence. | Review which push-to-main runs are required audit evidence and which are redundant after a successful PR check. |
| Pull request target/comment workflows | `hc-control-bot-advisory-comment.yml` and issue-comment assistant workflows can write comments. | High. | Park for dedicated security review; do not change triggers or permissions in a cleanup PR. |
| Label/write workflows | PR risk labeler and any write-capable workflow can mutate labels or repository-facing metadata. | High. | Keep human-reviewed; do not reduce or disable without replacement governance evidence. |
| Scheduled security scans | Weekly or manual security posture workflows may add visible history over time. | Low to medium. | Keep security evidence unless maintainers approve a cadence change. |
| Generated evidence workflows | Release audit, repository inventory, canonical artifact, validation, and archive/provenance checks can upload artifacts or summarize evidence. | Medium. | Keep until an evidence-retention policy exists. |

## 5. Safe reduction rules

A future implementation PR may reduce workflow noise only if all of the following are true:

- the workflow's purpose is still covered by another check or documented replacement;
- the change does not remove governance, security, provenance, release, validation, terminology, canonical artifact, or policy evidence;
- the workflow does not use `pull_request_target`, `issue_comment`, write permissions, label mutation, comment mutation, or auto-merge-adjacent behavior unless explicitly reviewed;
- the change is scoped to one workflow family at a time;
- before/after behavior is documented;
- all normal checks pass;
- a human maintainer approves the change.

## 6. Stop conditions

Stop and do not change workflows if any of the following are true:

- current open PR state is unclear;
- the workflow has write permissions;
- the workflow uses `pull_request_target`;
- the workflow responds to `issue_comment`;
- the workflow changes labels, comments, generated evidence, or repository content;
- the workflow protects governance, security, release, provenance, canonical, policy, terminology, validation, or archive boundaries;
- the proposed change is based only on UI clutter and not on documented duplicate behavior;
- the maintainer has not explicitly approved workflow behavior changes.

## 7. Recommended next PRs

Recommended future work should proceed in small, reviewable PRs:

1. Auto-merge policy overlap review: compare `enable-auto-merge.yml`, `safe-auto-merge.yml`, and `docs-auto-merge.yml`; recommend naming/documentation consolidation first, not behavior change.
2. Push-to-main duplication review: list workflows that run on both PR and `main` push; classify which post-merge runs are audit evidence and which may be redundant.
3. Workflow map/index: maintain a single operator-facing map of workflow purpose, trigger, permissions, mutation behavior, and risk.
4. Retention policy note: document whether completed workflow run deletion is ever allowed, and if so, what audit window must be retained.

## 8. Current safe action

Do not delete completed workflow run history now.

Do not edit workflow files in this PR.

The next safe action is a targeted report-only review of auto-merge-related workflow overlap, followed by a separate human-approved implementation PR only if the overlap review identifies a low-risk consolidation path.
