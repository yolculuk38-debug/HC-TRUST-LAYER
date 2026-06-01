# Workflow Security Review

## Purpose

This documentation-only review summarizes current GitHub Actions workflow security categories for HC-TRUST-LAYER. It uses the repository security audit checklist as source material and supports human-supervised validation for workflow changes.

The current audit posture flags GitHub Actions permissions for periodic re-validation, marks workflow triggers as aligned to expected events and paths, and treats auto-merge safety and generated artifact handling as review-sensitive areas.

## 1. Workflows with write permissions

Workflows with write permissions can change repository state, PR state, labels, or merge settings. They require closer review than read-only CI.

Current workflows with explicit write scopes:

- `auto-hash.yml`: uses `contents: write` to commit generated SHA-256 hash files after verified record changes.
- `docs-auto-merge.yml`: uses `pull-requests: write` from `pull_request_target` to classify documentation PRs, manage labels, and set auto-merge policy.
- `enable-auto-merge.yml`: uses `contents: write` and `pull-requests: write` from `pull_request_target` to enable PR auto-merge when configured labels are present.
- `pr-risk-labeler.yml`: uses `pull-requests: write` and `issues: write` to classify PR risk and update labels.
- `safe-auto-merge.yml`: uses `contents: write` and `pull-requests: write` to enable low-risk auto-merge when policy labels allow it.

## 2. Workflows using pull_request_target

`pull_request_target` workflows run with base-repository context and must be reviewed carefully, especially when they can write labels, PR metadata, or merge settings.

Current workflows using `pull_request_target`:

- `docs-auto-merge.yml`
- `enable-auto-merge.yml`

Manual review should confirm these workflows do not check out or execute untrusted pull request code with elevated token permissions.

## 3. Workflows that can affect labels, PRs, auto-merge, or artifacts

The following workflow categories affect review routing, PR state, auto-merge behavior, or generated artifacts:

- Label and PR routing: `docs-auto-merge.yml`, `pr-risk-labeler.yml`.
- Auto-merge controls: `docs-auto-merge.yml`, `enable-auto-merge.yml`, `safe-auto-merge.yml`.
- Advisory merge-risk reporting: `policy-evaluation.yml`, `governance-preflight.yml`.
- Generated hash commits: `auto-hash.yml`.
- Uploaded artifacts: `validate.yml`, `terminology-autofix-suggest.yml`.

These areas are review-sensitive because they can affect the audit trail, reviewer expectations, or generated artifact handling.

## 4. Read-only workflows

Read-only workflows use explicit `contents: read` and, where needed, `pull-requests: read`. They run checks, validation, or advisory reporting without writing repository or PR state.

Current read-only workflow examples include:

- `archive.yml`
- `automation-gate.yml`
- `canonical-artifacts.yml`
- `docs-drift.yml`
- `governance-preflight.yml`
- `policy-evaluation.yml`
- `pr-scope-guard.yml`
- `terminology-autofix-suggest.yml`
- `terminology.yml`
- `validate.yml`
- `verification-package-schema.yml`
- `verify-archive.yml`

Read-only status does not remove the need to review changed workflow logic, especially when the workflow handles canonical record boundaries, generated artifacts, or trust-kernel-adjacent checks.

## 5. Manual review expectations for `.github/workflows` changes

Any `.github/workflows` change should receive human-supervised review before merge. Reviewers should check:

- whether permissions remain least-privilege and explicitly scoped;
- whether `pull_request_target` usage is necessary and bounded;
- whether workflow changes affect labels, PR metadata, auto-merge, artifacts, or generated files;
- whether untrusted pull request content could run with elevated permissions;
- whether terminology, docs drift, canonical artifact, and relevant test checks still run as expected;
- whether audit trail continuity and reviewer visibility are preserved.

## 6. Recommended rule: workflow changes require human-supervised review

Recommended rule: any change under `.github/workflows` requires human-supervised review and is not eligible for unsupervised auto-merge.

This rule aligns with HC-TRUST-LAYER governance boundaries, the repository security audit checklist, and the expectation that automation affecting review routing, artifacts, or merge behavior remains bounded and reviewable.

## Source material

- `docs/repo-security-audit.md`
- Current workflow definitions under `.github/workflows/`
