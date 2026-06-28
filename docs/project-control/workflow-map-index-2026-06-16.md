# Workflow Map Index — 2026-06-16

This document is a docs-only workflow map for HC-TRUST-LAYER. It records current GitHub Actions workflow behavior after the initial workflow noise-reduction PRs merged on 2026-06-16.

Synchronized through: current post-#1120 state; the relevant HC Review Window workflow behavior change came from #1117.

## Project boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index does not change workflow permissions, triggers, labels, comments, auto-merge behavior, source code, tests, generated artifacts, records, schemas, validators, policy, federation, signatures, canonical files, or trust-kernel files.

## Recommendation legend

- `KEEP`: keep as-is unless a later human-reviewed change request identifies a specific issue.
- `REVIEW_DUPLICATION_CANDIDATE`: review later for possible overlap, duplicate evidence, or redundant main-push runs.
- `PARK_HIGH_RISK`: do not expand without explicit human review because the workflow can mutate repository or PR state.
- `HUMAN_REVIEW_REQUIRED`: preserve or strengthen human-supervised review boundaries before any change.
- `POSSIBLE_LOW_RISK_REDUCTION`: possible later simplification candidate if the evidence role is redundant and reviewers agree.

## Related taxonomy

See `docs/project-control/workflow-taxonomy.md` for the advisory role and authority classification of current GitHub Actions workflows. See `docs/project-control/workflow-naming-review.md` for the advisory review of workflow names against observed behavior.

## Workflow inventory

| Workflow file path | Workflow name | Trigger/event type | Permissions summary | Writes repository state | Comments | Labels | Enables auto-merge | Commits files | Uploads artifacts | Runs on `pull_request` | Runs on push to `main` | Main-push run classification | Risk level | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `.github/workflows/archive.yml` | HC-TRUST-LAYER Archive Automation | `push` to `main` with paths: `records/**`, `src/**`, `docs/**`, `qr/**` | `contents: read` | No | No | No | No | No | No | No | Yes, when path filters match | Main-only archive evidence; branch-push noise reduced after #1008 | Medium | `KEEP` |
| `.github/workflows/auto-hash.yml` | Auto Generate Hash Files | `push` with path `records/verified/**.md` | `contents: write` | Yes | No | No | No | Yes; commits and pushes generated `hash/*.sha256` when changed | No | No | Possible, because push is not branch-limited | Intended generated hash evidence, but repository-state mutation is high review sensitivity | High | `PARK_HIGH_RISK` |
| `.github/workflows/automation-gate.yml` | Automation Gate | `pull_request` types: opened, synchronize, reopened, edited | `contents: read`, `pull-requests: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/canonical-artifacts.yml` | Canonical Artifact Boundary Guard | `pull_request`; `push` to `main` with scoped canonical boundary paths | `contents: read` | No | No | No | No | No | No | Yes | Yes, when scoped path filters match | Main-push scope reduced after #1013 while preserving broad PR coverage and canonical-boundary evidence | Medium | `KEEP` |
| `.github/workflows/docs-auto-merge.yml` | Docs Review Policy | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read` | No | No; reports in logs only | No | No | No | No | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/docs-drift.yml` | Docs Drift Check | `pull_request`; `push` to `main` with scoped paths for inspected docs, checker script, and evidence path groups | `contents: read` | No | No | No | No | No | No | Yes | Yes, when scoped path filters match | Main-push scope reduced after #1005 while preserving evidence-path coverage | Low | `KEEP` |
| `.github/workflows/enable-auto-merge.yml` | Enable PR Auto-merge | `pull_request` types: opened, reopened, synchronize, ready_for_review, labeled, unlabeled | `contents: read`, `pull-requests: read` | No | No; reports disabled auto-merge boundary in logs | No | No | No | No | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/governance-preflight.yml` | Governance Preflight | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/hc-assistant-command.yml` | HC Assistant Command Listener | `issue_comment` type: created; job only runs for comments starting with `/hc` | `contents: read`, `issues: write`, `pull-requests: read` | No repository file writes; may write issue comments | Yes; posts or updates an HC Assistant response comment | No | No | No | Yes | No | No | Not applicable | High | `PARK_HIGH_RISK` |
| `.github/workflows/hc-control-bot-advisory-comment.yml` | HC Control Bot Advisory Comment | `pull_request_target` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read`, `issues: write` | No repository file writes; may write PR comments | Yes; posts or updates one advisory PR comment | No | No | No | Yes | No; uses `pull_request_target`, not `pull_request` | No | Not applicable | High | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/hc-control-bot-report.yml` | HC Control Bot Report | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read` | No | No; report-only job summary and artifact include HC Review Window status; does not comment, label, approve, merge, or delay checks | No | No | No | Yes | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/hc-review-window-marker.yml` | HC Review Window Marker | `workflow_dispatch` only; automatic PR triggers disabled | `contents: read`, `pull-requests: read`, `issues: write` | No | May create or update advisory PR marker comment only when manually dispatched; falls back to job summary on permission denial | No | No | No | No | No | No | Not applicable | High, because it has issue comment write permission even though it is manual-only | `HUMAN_REVIEW_REQUIRED` / `PARK_HIGH_RISK`; do not expand without explicit review |
| `.github/workflows/hc-repo-inventory.yml` | HC Repository Inventory | `pull_request`; `workflow_dispatch`; `push` to `main` | `contents: read`, `id-token: write`, `attestations: write` | No | No | No | No | No | Yes | Yes | Yes | Intended audit evidence for repository inventory attestations on trusted contexts | Medium | `KEEP` |
| `.github/workflows/policy-evaluation.yml` | Advisory Policy Evaluation | `pull_request` | `contents: read`, `pull-requests: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/pr-risk-labeler.yml` | PR Risk Labeler | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: write`, `issues: write` | Yes; mutates PR labels and can create labels | No | Yes; applies/removes `manual-review` and removes `auto-merge` | No | No | No | Yes | No | Not applicable | High | `PARK_HIGH_RISK` |
| `.github/workflows/pr-scope-guard.yml` | PR Scope Guard | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/release-audit.yml` | HC Release Audit | `pull_request`; `workflow_dispatch` | `contents: read` | No | No | No | No | No | Yes | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/safe-auto-merge.yml` | Safe Auto Merge | `pull_request` types: opened, synchronize, reopened, labeled, unlabeled, ready_for_review; `workflow_run` for completed Automation Gate | `contents: read`, `pull-requests: read` | No | No; reports disabled auto-merge boundary in logs | No | No | No | No | Yes | No | Not applicable | Low | `REVIEW_DUPLICATION_CANDIDATE` |
| `.github/workflows/scorecard.yml` | OpenSSF Scorecard Advisory | `workflow_dispatch`; scheduled weekly cron | `contents: read` | No | No | No | No | No | Yes | No | No | Not applicable | Low | `KEEP` |
| `.github/workflows/terminology-autofix-suggest.yml` | Terminology Autofix Suggest (Advisory) | `pull_request` | `contents: read` | No | No | No | No | No | Yes, only when terminology guard fails | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/terminology.yml` | Terminology Guard | `pull_request`; `push` to `main` with scoped terminology paths | `contents: read` | No | No | No | No | No | No | Yes | Yes, when scoped path filters match | Main-push scope reduced after #1006 while preserving terminology boundary coverage | Low | `KEEP` |
| `.github/workflows/validate.yml` | HC-TRUST-LAYER Validation | `pull_request`; `push` to `main` with validation path filters | `contents: read` | No | No | No | No | No | Yes | Yes | Yes, when validation path filters match | Main-push scope reduced after #1011 while preserving broad PR validation coverage | Medium | `KEEP` |
| `.github/workflows/verification-package-schema.yml` | verification-package-schema | `pull_request`; `push` to `main` with scoped schema/example checker paths | `contents: read` | No | No | No | No | No | No | Yes | Yes, when scoped path filters match | Main-push scope reduced after #1007 while preserving verification package schema/example coverage | Medium | `KEEP` |
| `.github/workflows/verify-archive.yml` | Verify HC-TRUST-LAYER Archive | `push` to `main` with scoped archive-structure paths | `contents: read` | No | No | No | No | No | No | No | Yes, when scoped archive path filters match | Main-push scope reduced after #1012 while preserving archive-structure evidence coverage | Medium | `KEEP` |

## HC Review Window observation

- HC Review Window active reporting surface is now `HC Control Bot Report`.
- `HC Review Window Marker` is preserved only as manual debug/passive fallback.
- The marker workflow is not a required check.
- CI/checks remain evidence, not trust authority.
- Human final authority remains required.

## Initial observations

- Workflows with write-capable permissions, PR/comment mutation, labels, or state mutation remain the highest-risk review targets: `auto-hash.yml`, `hc-assistant-command.yml`, `hc-control-bot-advisory-comment.yml`, `hc-repo-inventory.yml`, and `pr-risk-labeler.yml`.
- Initial low-risk reductions merged for `docs-drift.yml`, `terminology.yml`, `verification-package-schema.yml`, `archive.yml`, `validate.yml`, `verify-archive.yml`, and `canonical-artifacts.yml`; these changes narrowed main-push or branch-push behavior without changing permissions, jobs, or scripts.
- `auto-hash.yml` remains parked because it has `contents: write` and commits/pushes generated hash files.
- `hc-repo-inventory.yml` remains preserved because its trusted-context inventory attestations use `id-token: write` and `attestations: write`.
- Workflows with main-push evidence runs should be preserved unless reviewers decide a specific run is duplicate noise and the audit evidence value is low.
- Workflows that mention auto-merge currently describe disabled or report-only behavior in the inspected workflow files; this index does not assert that as a trust guarantee.
- Any later workflow behavior change should be proposed separately, remain human-reviewable, and avoid weakening HC:// evidence preservation or HC-TRUST-LAYER governance boundaries.
