# Workflow Map Index — 2026-06-16

This document is a docs-only workflow map for HC-TRUST-LAYER. It records current GitHub Actions workflow behavior before any workflow behavior changes are proposed or implemented.

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

## Workflow inventory

| Workflow file path | Workflow name | Trigger/event type | Permissions summary | Writes repository state | Comments | Labels | Enables auto-merge | Commits files | Uploads artifacts | Runs on `pull_request` | Runs on push to `main` | Main-push run classification | Risk level | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `.github/workflows/archive.yml` | HC-TRUST-LAYER Archive Automation | `push` with paths: `records/**`, `src/**`, `docs/**`, `qr/**` | `contents: read` | No | No | No | No | No | No | No | Possible, because push is not branch-limited | Possible duplicate noise; archive checks may overlap PR validation when docs/source/record paths are pushed to `main` | Medium | `REVIEW_DUPLICATION_CANDIDATE` |
| `.github/workflows/auto-hash.yml` | Auto Generate Hash Files | `push` with path `records/verified/**.md` | `contents: write` | Yes | No | No | No | Yes; commits and pushes generated `hash/*.sha256` when changed | No | No | Possible, because push is not branch-limited | Intended generated hash evidence, but repository-state mutation is high review sensitivity | High | `PARK_HIGH_RISK` |
| `.github/workflows/automation-gate.yml` | Automation Gate | `pull_request` types: opened, synchronize, reopened, edited | `contents: read`, `pull-requests: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/canonical-artifacts.yml` | Canonical Artifact Boundary Guard | `pull_request`; `push` to `main` | `contents: read` | No | No | No | No | No | No | Yes | Yes | Intended audit evidence for canonical artifact boundary checks | Medium | `KEEP` |
| `.github/workflows/docs-auto-merge.yml` | Docs Review Policy | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read` | No | No; reports in logs only | No | No | No | No | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/docs-drift.yml` | Docs Drift Check | `pull_request`; `push` to `main` | `contents: read` | No | No | No | No | No | No | Yes | Yes | Intended audit evidence for documentation drift checks; possible overlap with PR runs after merge | Low | `POSSIBLE_LOW_RISK_REDUCTION` |
| `.github/workflows/enable-auto-merge.yml` | Enable PR Auto-merge | `pull_request` types: opened, reopened, synchronize, ready_for_review, labeled, unlabeled | `contents: read`, `pull-requests: read` | No | No; reports disabled auto-merge boundary in logs | No | No | No | No | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/governance-preflight.yml` | Governance Preflight | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/hc-assistant-command.yml` | HC Assistant Command Listener | `issue_comment` type: created; job only runs for comments starting with `/hc` | `contents: read`, `issues: write`, `pull-requests: read` | No repository file writes; may write issue comments | Yes; posts or updates an HC Assistant response comment | No | No | No | Yes | No | No | Not applicable | High | `PARK_HIGH_RISK` |
| `.github/workflows/hc-control-bot-advisory-comment.yml` | HC Control Bot Advisory Comment | `pull_request_target` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read`, `issues: write` | No repository file writes; may write PR comments | Yes; posts or updates one advisory PR comment | No | No | No | Yes | No; uses `pull_request_target`, not `pull_request` | No | Not applicable | High | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/hc-control-bot-report.yml` | HC Control Bot Report | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: read` | No | No | No | No | No | Yes | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/hc-repo-inventory.yml` | HC Repository Inventory | `pull_request`; `workflow_dispatch`; `push` to `main` | `contents: read` | No | No | No | No | No | Yes | Yes | Yes | Intended audit evidence for repository inventory attestations on trusted contexts | Low | `KEEP` |
| `.github/workflows/policy-evaluation.yml` | Advisory Policy Evaluation | `pull_request` | `contents: read`, `pull-requests: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `HUMAN_REVIEW_REQUIRED` |
| `.github/workflows/pr-risk-labeler.yml` | PR Risk Labeler | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read`, `pull-requests: write`, `issues: write` | Yes; mutates PR labels and can create labels | No | Yes; applies/removes `manual-review` and removes `auto-merge` | No | No | No | Yes | No | Not applicable | High | `PARK_HIGH_RISK` |
| `.github/workflows/pr-scope-guard.yml` | PR Scope Guard | `pull_request` types: opened, synchronize, reopened, ready_for_review | `contents: read` | No | No | No | No | No | No | Yes | No | Not applicable | Medium | `KEEP` |
| `.github/workflows/release-audit.yml` | HC Release Audit | `pull_request`; `workflow_dispatch` | `contents: read` | No | No | No | No | No | Yes | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/safe-auto-merge.yml` | Safe Auto Merge | `pull_request` types: opened, synchronize, reopened, labeled, unlabeled, ready_for_review; `workflow_run` for completed Automation Gate | `contents: read`, `pull-requests: read` | No | No; reports disabled auto-merge boundary in logs | No | No | No | No | Yes | No | Not applicable | Low | `REVIEW_DUPLICATION_CANDIDATE` |
| `.github/workflows/scorecard.yml` | OpenSSF Scorecard Advisory | `workflow_dispatch`; scheduled weekly cron | `contents: read` | No | No | No | No | No | Yes | No | No | Not applicable | Low | `KEEP` |
| `.github/workflows/terminology-autofix-suggest.yml` | Terminology Autofix Suggest (Advisory) | `pull_request` | `contents: read` | No | No | No | No | No | Yes, only when terminology guard fails | Yes | No | Not applicable | Low | `KEEP` |
| `.github/workflows/terminology.yml` | Terminology Guard | `pull_request`; `push` to `main` | `contents: read` | No | No | No | No | No | No | Yes | Yes | Intended audit evidence for terminology boundaries; possible overlap with PR runs after merge | Low | `KEEP` |
| `.github/workflows/validate.yml` | HC-TRUST-LAYER Validation | `push` and `pull_request` with paths: `records/**`, `schema/**`, `src/**`, `tests/**`, `pyproject.toml`, `requirements.txt`, `.github/workflows/validate.yml` | `contents: read` | No | No | No | No | No | Yes | Yes, when path filters match | Possible, because push is not branch-limited and path-filtered | Intended validation evidence for record/schema/source/test changes; possible duplicate noise after PR merge | Medium | `KEEP` |
| `.github/workflows/verification-package-schema.yml` | verification-package-schema | `pull_request`; `push` to `main` | `contents: read` | No | No | No | No | No | No | Yes | Yes | Intended audit evidence for verification package example schema checks | Medium | `KEEP` |
| `.github/workflows/verify-archive.yml` | Verify HC-TRUST-LAYER Archive | `push` to `main` | `contents: read` | No | No | No | No | No | No | No | Yes | Intended audit evidence for repository structure/archive verification | Medium | `KEEP` |

## Initial observations

- Workflows with write-capable permissions or state mutation are the highest-risk review targets: `auto-hash.yml`, `hc-assistant-command.yml`, `hc-control-bot-advisory-comment.yml`, and `pr-risk-labeler.yml`.
- Workflows with main-push evidence runs should be preserved unless reviewers decide a specific run is duplicate noise and the audit evidence value is low.
- Workflows that mention auto-merge currently describe disabled or report-only behavior in the inspected workflow files; this index does not assert that as a trust guarantee.
- Any later workflow behavior change should be proposed separately, remain human-reviewable, and avoid weakening HC:// evidence preservation or HC-TRUST-LAYER governance boundaries.
