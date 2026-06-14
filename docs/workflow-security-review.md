# Workflow Security Review

## Purpose

This documentation-only review summarizes current GitHub Actions workflow security categories for HC-TRUST-LAYER. It uses the repository security audit checklist as source material and supports human-supervised validation for workflow changes.

The current audit posture flags GitHub Actions permissions for periodic re-validation, marks workflow triggers as aligned to expected events and paths, and treats generated artifact handling, PR routing, advisory comments, and any merge-related workflow as review-sensitive areas.

## 1. Workflows with write permissions

Workflows with write permissions can change repository state, PR state, labels, comments, or generated artifacts. They require closer review than read-only CI.

Current workflows with explicit write scopes:

- `auto-hash.yml`: uses `contents: write` to commit generated SHA-256 hash files after verified record changes.
- `pr-risk-labeler.yml`: uses `pull-requests: write` and `issues: write` to classify PR risk, apply `manual-review`, and remove stale `auto-merge` labels when present. It must never add an `auto-merge` label or enable merge automation.
- `hc-control-bot-advisory-comment.yml`: uses `issues: write` to post or update a single advisory HC Control Bot PR comment. It checks out the trusted base revision and remains advisory-only.
- `hc-assistant-command.yml`: uses `issues: write` to post or update advisory `/hc` command responses on issues. It checks out the trusted default branch and remains advisory-only.

## 2. Workflows using pull_request_target

`pull_request_target` workflows run with base-repository context and must be reviewed carefully, especially when they can write comments, labels, PR metadata, or merge settings.

Current workflows using `pull_request_target`:

- `hc-control-bot-advisory-comment.yml`

Manual review should confirm this workflow does not check out, import, execute, source, or evaluate untrusted pull request branch code with elevated token permissions. Its current design checks out the trusted base revision and reads changed file paths through the GitHub API.

## 3. Workflows that can affect labels, comments, merge posture, or artifacts

The following workflow categories affect review routing, advisory visibility, merge expectations, or generated artifacts:

- Label and PR routing: `pr-risk-labeler.yml`.
- Advisory comment output: `hc-control-bot-advisory-comment.yml`, `hc-assistant-command.yml`.
- Merge posture reporting: `docs-auto-merge.yml`, `enable-auto-merge.yml`, `safe-auto-merge.yml`, `policy-evaluation.yml`, `governance-preflight.yml`.
- Generated hash commits: `auto-hash.yml`.
- Uploaded artifacts: `validate.yml`, `terminology-autofix-suggest.yml`.

These areas are review-sensitive because they can affect the audit trail, reviewer expectations, generated artifact handling, or contributor interpretation of merge readiness.

## 4. Read-only / report-only workflow examples

Read-only workflows use explicit `contents: read` and, where needed, `pull-requests: read`. They run checks, validation, or advisory reporting without writing repository or PR state.

Current read-only/report-only workflow examples include:

- `archive.yml`
- `automation-gate.yml`
- `canonical-artifacts.yml`
- `docs-auto-merge.yml`
- `docs-drift.yml`
- `enable-auto-merge.yml`
- `governance-preflight.yml`
- `policy-evaluation.yml`
- `pr-scope-guard.yml`
- `safe-auto-merge.yml`
- `terminology-autofix-suggest.yml`
- `terminology.yml`
- `validate.yml`
- `verification-package-schema.yml`
- `verify-archive.yml`

Read-only status does not remove the need to review changed workflow logic, especially when the workflow handles canonical record boundaries, generated artifacts, or trust-kernel-adjacent checks.

## 5. Auto-merge boundary

Native or workflow-enabled auto-merge is not part of the current HC-TRUST-LAYER operating boundary.

- `docs-auto-merge.yml` is report-only and read-only.
- `enable-auto-merge.yml` is report-only and read-only.
- `safe-auto-merge.yml` is report-only and read-only.
- Human review and human merge remain required.

## 6. Manual review expectations for `.github/workflows` changes

Any `.github/workflows` change should receive human-supervised review before merge. Reviewers should check:

- whether permissions remain least-privilege and explicitly scoped;
- whether `pull_request_target` usage is necessary and bounded;
- whether workflow changes affect labels, PR metadata, comments, merge posture, artifacts, or generated files;
- whether untrusted pull request content could run with elevated permissions;
- whether terminology, docs drift, canonical artifact, and relevant test checks still run as expected;
- whether audit trail continuity and reviewer visibility are preserved.

## 7. Recommended rule: workflow changes require human-supervised review

Recommended rule: any change under `.github/workflows` requires human-supervised review and is not eligible for unsupervised auto-merge.

This rule aligns with HC-TRUST-LAYER governance boundaries, the repository security audit checklist, and the expectation that automation affecting review routing, artifacts, comments, or merge behavior remains bounded and reviewable.

## Source material

- `docs/repo-security-audit.md`
- Current workflow definitions under `.github/workflows/`
