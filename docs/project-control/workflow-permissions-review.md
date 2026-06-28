# Workflow Permissions Review

## 1. Purpose

This document is an advisory, documentation-only review of GitHub Actions workflow permissions and least-privilege posture for HC-TRUST-LAYER.

It supports backlog item 3-3, “workflow permissions / least-privilege review.” It records observed workflow triggers, declared token scopes, write-capable permissions, secret exposure, and behavior from the current `.github/workflows/**` files. It does not change workflow permissions, workflow names, branch protection, rulesets, auto-merge behavior, checks, scripts, runtime code, schemas, validators, records, generated artifacts, canonical files, policy, federation, signing, signatures, labels, comments, reviewer requests, approvals, or merge authority.

## 2. HC boundary

The following HC boundary applies to this review:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- CI/checks are evidence, not trust authority.
- Permission review does not approve, reject, merge, certify, or establish truth.
- Human maintainer remains final authority.

Workflow permissions, comments, labels, artifacts, summaries, checks, status metadata, and attestations can support review. They do not establish legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness.

## 3. Review method

For each workflow under `.github/workflows/**`, inspect:

- workflow name;
- workflow file path;
- triggers;
- top-level `permissions`;
- job-level `permissions`;
- use of `GITHUB_TOKEN`;
- use of secrets;
- use of `pull_request_target`;
- use of `workflow_run`;
- use of `id-token: write`;
- use of `attestations: write`;
- use of `contents: write`;
- use of `issues: write`;
- use of `pull-requests: write`;
- use of `checks: write`;
- use of `statuses: write`;
- whether the workflow comments, labels, requests reviewers, approves, merges, updates files, uploads artifacts, or only reports/checks.

Assessment labels are conservative:

- `minimal / aligned`
- `probably acceptable`
- `needs clarification`
- `high sensitivity`
- `reduce permissions later`
- `needs maintainer confirmation`

## 4. Permission review table

| Workflow name | Workflow file | Trigger risk | Declared permissions | Write scopes observed | Token/secrets exposure | Actual behavior | Least-privilege assessment | Recommendation |
|---|---|---|---|---|---|---|---|---|
| HC-TRUST-LAYER Archive Automation | `.github/workflows/archive.yml` | Main push with scoped paths. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs archive normalization, hash verification, index generation, and QR generation. | minimal / aligned | Keep as-is unless maintainers identify duplicate main-push evidence later. |
| Auto Generate Hash Files | `.github/workflows/auto-hash.yml` | Push to `records/verified/**.md`; not branch-limited. | Top-level `contents: write`. | `contents: write`; commits and pushes `hash/*.sha256`. | Checkout uses `secrets.GITHUB_TOKEN`. | Generates SHA-256 files and pushes generated hash updates when changed. | high sensitivity; reduce permissions later; needs maintainer confirmation | Review in a separate workflow-specific PR before changing behavior or scopes. |
| Automation Gate | `.github/workflows/automation-gate.yml` | Pull request. | Top-level `contents: read`, `pull-requests: read`. | None observed. | Default checkout token; no explicit secrets observed. | Checks PR title/body, blocked binary file extensions, and Python syntax. | minimal / aligned | Keep; no permission reduction identified in this docs-only review. |
| Canonical Artifact Boundary Guard | `.github/workflows/canonical-artifacts.yml` | Pull request and scoped main push over canonical/generated/record-adjacent paths. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs canonical artifact guard. | minimal / aligned, with protected-boundary sensitivity | Keep; human review remains required for canonical-adjacent findings. |
| Docs Review Policy | `.github/workflows/docs-auto-merge.yml` | Pull request. | Top-level `contents: read`, `pull-requests: read`. | None observed. | `github-script` uses read token through action context. | Classifies PR scope and reports review requirements in logs. | probably acceptable | Keep; preserve report-only boundary. |
| Docs Drift Check | `.github/workflows/docs-drift.yml` | Pull request and scoped main push. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs documentation drift checker. | minimal / aligned | Keep. |
| Enable PR Auto-merge | `.github/workflows/enable-auto-merge.yml` | Pull request, including label changes. | Top-level `contents: read`, `pull-requests: read`. | None observed. | No explicit secrets observed. | Reports that automatic merge enablement is disabled. | probably acceptable | Keep; name/behavior concerns remain separate from permissions. |
| Governance Preflight | `.github/workflows/governance-preflight.yml` | Pull request. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs GitHub Actions version check and governance preflight. | minimal / aligned, with governance sensitivity | Keep; findings remain evidence only. |
| HC Assistant Command Listener | `.github/workflows/hc-assistant-command.yml` | `issue_comment` command surface. | Top-level `contents: read`, `issues: write`, `pull-requests: read`. | `issues: write`; posts or updates issue comments. | Uses `${{ github.token }}` and command artifacts; no broad secret beyond token observed. | Parses `/hc` commands, uploads command result, and writes advisory response comments. | high sensitivity; needs maintainer confirmation | Keep for now; review comment-writing scope and command input handling in a separate PR if maintainers choose. |
| HC Check Digest | `.github/workflows/hc-check-digest.yml` | Pull request, review/comment/check/status events, `workflow_run`, and manual dispatch. | Top-level `contents: read`, `actions: read`, `checks: read`, `pull-requests: read`. | None observed. | Uses `secrets.GITHUB_TOKEN` for read-only metadata fetches. | Builds advisory PR health digest artifacts and summaries from live metadata. | high sensitivity due to event surface; probably acceptable permissions | Keep; maintain read-only token posture and review event scope later if noisy. |
| HC Control Bot Advisory Comment | `.github/workflows/hc-control-bot-advisory-comment.yml` | `pull_request_target`, privileged PR context. | Top-level `contents: read`, `pull-requests: read`, `issues: write`. | `issues: write`; posts or updates one advisory PR comment. | Uses `${{ github.token }}` with privileged event context; checks out trusted base revision. | Collects changed path metadata, runs deterministic scanner, uploads report artifact, and writes one advisory comment. | high sensitivity; needs maintainer confirmation | Keep as-is in this PR; any permission or trigger change must be separate and carefully reviewed. |
| HC Control Bot Report | `.github/workflows/hc-control-bot-report.yml` | Pull request; checks out trusted base and PR docs as data. | Top-level `contents: read`, `pull-requests: read`. | None observed. | Uses `${{ github.token }}` for changed-file API; no write token observed. | Produces report-only scan output, taxonomy drift advisory, and artifacts. | probably acceptable | Keep; preserve report-only behavior and do not add comment/label mutation without review. |
| HC Repository Inventory | `.github/workflows/hc-repo-inventory.yml` | Pull request, manual, and main push. | Top-level `contents: read`, `id-token: write`, `attestations: write`. | `id-token: write`, `attestations: write` on non-PR trusted contexts. | Default token plus OIDC/attestation capability in trusted contexts. | Builds inventory reports, attests artifacts outside PR runs, and uploads artifacts. | high sensitivity; needs maintainer confirmation | Keep pending maintainer confirmation; review attestation necessity in a separate permission-reduction PR if desired. |
| HC Review Window Marker | `.github/workflows/hc-review-window-marker.yml` | Manual dispatch only. | Top-level `contents: read`, `pull-requests: read`, `issues: write`. | `issues: write`; may create or update advisory PR marker comment. | Uses write-capable issue token in manual context. | Manual advisory marker comment or summary fallback; no automatic PR trigger. | high sensitivity; probably acceptable due to manual trigger | Keep manual-only; do not expand automatic triggers without separate review. |
| HC Signal Watch Live RSS Dry Run | `.github/workflows/hc-signal-watch-live-rss-dry-run.yml` | Manual dispatch with external RSS URL input. | Top-level `contents: read`. | None observed. | No write token or repository secrets observed. | Fetches live RSS input, writes summaries, and uploads dry-run artifacts. | probably acceptable | Keep read-only; external data remains advisory and human-reviewed. |
| HC Signal Watch Report | `.github/workflows/hc-signal-watch-report.yml` | Schedule/manual/main-context live signal collection; PR local fixture mode. | Top-level `contents: read`, `actions: read`; report job `contents: read`, `actions: read`; console-comment job `contents: read`, `actions: read`, `issues: write`. | Job-level `issues: write` only for gated main-context console comment. | Console-comment job uses `secrets.GITHUB_TOKEN`; live RSS/network use occurs outside PR runs. | Produces signal reports and, on non-PR main contexts, may update one fixed issue comment. | high sensitivity; needs maintainer confirmation | Keep; review whether console comment needs separate workflow or narrower documentation in later PR. |
| Advisory Policy Evaluation | `.github/workflows/policy-evaluation.yml` | Pull request. | Top-level `contents: read`, `pull-requests: read`. | None observed. | Default checkout token; no explicit secrets observed. | Evaluates changed paths and prints advisory merge-risk summary. | minimal / aligned, with governance sensitivity | Keep. |
| PR Risk Labeler | `.github/workflows/pr-risk-labeler.yml` | Pull request. | Top-level `contents: read`, `pull-requests: write`, `issues: write`. | `pull-requests: write`, `issues: write`; creates labels and edits PR labels. | Uses `${{ github.token }}` as `GH_TOKEN`. | Applies/removes `manual-review` and removes `auto-merge`; does not approve or merge. | high sensitivity; reduce permissions later; needs maintainer confirmation | Review in a separate labeler-specific PR; do not change labels or scopes here. |
| PR Scope Guard | `.github/workflows/pr-scope-guard.yml` | Pull request. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs advisory scope checker with `continue-on-error` and reminder. | minimal / aligned | Keep. |
| HC Release Audit | `.github/workflows/release-audit.yml` | Pull request and manual dispatch. | Top-level `contents: read`. | None observed. | Checkout disables persisted credentials; no explicit secrets observed. | Produces release audit JSON/Markdown artifacts and summaries. | minimal / aligned | Keep; artifacts are evidence only. |
| Safe Auto Merge | `.github/workflows/safe-auto-merge.yml` | Pull request plus `workflow_run`; job runs only on pull request. | Top-level `contents: read`, `pull-requests: read`. | None observed. | No explicit secrets observed. | Reports disabled auto-merge boundary without mutating PR state. | needs clarification due to `workflow_run`; probably acceptable permissions | Keep; review duplicate/obsolete overlap under 3-4. |
| OpenSSF Scorecard Advisory | `.github/workflows/scorecard.yml` | Schedule and manual dispatch. | Top-level `contents: read`. | None observed. | Checkout disables persisted credentials; no publishing token observed. | Runs Scorecard with result publishing disabled and uploads artifact. | minimal / aligned | Keep. |
| Terminology Autofix Suggest (Advisory) | `.github/workflows/terminology-autofix-suggest.yml` | Pull request. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Generates and uploads advisory autofix report only when terminology guard fails. | minimal / aligned | Keep; no automatic commit/push authority. |
| Terminology Guard | `.github/workflows/terminology.yml` | Pull request and scoped main push. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs terminology guard. | minimal / aligned | Keep. |
| HC-TRUST-LAYER Validation | `.github/workflows/validate.yml` | Pull request and scoped main push for runtime/schema/records/tests. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Runs validation/test evidence and uploads generated artifacts. | minimal / aligned, with trust-kernel-adjacent sensitivity | Keep; artifacts/checks remain evidence only. |
| verification-package-schema | `.github/workflows/verification-package-schema.yml` | Pull request and scoped main push over schema/example checker paths. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Validates verification package schema/example. | minimal / aligned, with schema sensitivity | Keep. |
| Verify HC-TRUST-LAYER Archive | `.github/workflows/verify-archive.yml` | Scoped main push. | Top-level `contents: read`. | None observed. | Default checkout token; no explicit secrets observed. | Checks archive structure and required repository files. | minimal / aligned | Keep. |

## 5. High-risk permission patterns

| Pattern | Why sensitive | Current repo appears to use it? | Recommended handling |
|---|---|---|---|
| `pull_request_target` | Runs in a privileged base-repository context and can expose write-capable token behavior if untrusted PR code or data is executed unsafely. | Yes: `hc-control-bot-advisory-comment.yml`. | Remain as-is in this docs-only PR; review later before any expansion. |
| `workflow_run` | Runs based on another workflow result and can be confusing when combined with PR metadata, status, or privileged follow-up behavior. | Yes: `hc-check-digest.yml` and `safe-auto-merge.yml`. | Keep read-only; review event necessity separately if maintainers want reductions. |
| `id-token: write` | Allows OIDC token issuance for trusted identity exchange and should be scoped to workflows that need provenance or external trust integration. | Yes: `hc-repo-inventory.yml`. | Needs maintainer confirmation; reduce only in a separate attestation-focused PR if not needed. |
| `attestations: write` | Can create artifact provenance attestations that readers may over-interpret as trust authority. | Yes: `hc-repo-inventory.yml`. | Keep current boundary language; review later if attestation scope should narrow. |
| `contents: write` | Allows repository content mutation, commits, tags, or pushes depending on usage. | Yes: `auto-hash.yml`. | High sensitivity; review in a separate permission-reduction or workflow redesign PR. |
| `issues: write` | Allows issue or PR comments and labels through the issues API. | Yes: `hc-assistant-command.yml`, `hc-control-bot-advisory-comment.yml`, `hc-review-window-marker.yml`, `hc-signal-watch-report.yml` console-comment job, and `pr-risk-labeler.yml`. | Keep only where intentional comments/labels are documented; review each write workflow separately. |
| `pull-requests: write` | Allows PR mutation such as edits, labels through PR APIs, and related state changes. | Yes: `pr-risk-labeler.yml`. | High sensitivity; review later and preserve non-approval/non-merge boundary. |
| `checks: write` | Allows creating or updating check runs, which can affect reviewer interpretation and branch protection if configured. | No current explicit `checks: write` observed. | Do not add without a documented reason, boundary, and maintainer review. |
| `statuses: write` | Allows commit status mutation, which can affect branch protection if configured. | No current explicit `statuses: write` observed. | Do not add without a documented reason, boundary, and maintainer review. |
| Secrets available in workflow context | Secrets can expand impact if exposed to untrusted code, logs, or external calls. | Yes where `secrets.GITHUB_TOKEN` is referenced; no additional named external secrets were observed in this review. | Keep secrets out of untrusted PR code paths; document any new secret use before adding it. |
| PR-created code or data used with privileged token | Untrusted PR content can influence privileged API calls, comments, labels, generated reports, or files. | Yes as data in advisory/comment/report workflows; `pull_request_target` is the most sensitive instance. | Treat PR data as untrusted; privileged workflows must check out trusted base code and avoid executing PR code. |

## 6. Recommended permission rules for HC

- Default to `contents: read`.
- Prefer job-level permissions over broad workflow-level permissions when only one job needs elevated access.
- PR workflows should avoid write tokens unless absolutely required.
- Privileged write workflows must not execute untrusted PR code.
- Advisory/report-only workflows should not need write permissions unless they intentionally post one controlled comment.
- Auto-merge support must remain non-authoritative and human-governed.
- Artifact/report workflows should not need repository write permission.
- Any write permission must be documented with reason and boundary.

## 7. Findings

- Least-privilege aligned workflows appear to be the read-only check/report workflows: `archive.yml`, `automation-gate.yml`, `canonical-artifacts.yml`, `docs-auto-merge.yml`, `docs-drift.yml`, `enable-auto-merge.yml`, `governance-preflight.yml`, `hc-control-bot-report.yml`, `policy-evaluation.yml`, `pr-scope-guard.yml`, `release-audit.yml`, `scorecard.yml`, `terminology-autofix-suggest.yml`, `terminology.yml`, `validate.yml`, `verification-package-schema.yml`, and `verify-archive.yml`.
- Workflows needing maintainer confirmation include `auto-hash.yml`, `hc-assistant-command.yml`, `hc-check-digest.yml`, `hc-control-bot-advisory-comment.yml`, `hc-repo-inventory.yml`, `hc-review-window-marker.yml`, `hc-signal-watch-report.yml`, `pr-risk-labeler.yml`, and `safe-auto-merge.yml`.
- Workflows that should be reviewed in a later permission-reduction PR include `auto-hash.yml`, `hc-assistant-command.yml`, `hc-control-bot-advisory-comment.yml`, `hc-repo-inventory.yml`, `hc-signal-watch-report.yml`, and `pr-risk-labeler.yml`.
- High-sensitivity workflows due to trigger or write scope include `auto-hash.yml` (`contents: write`), `hc-assistant-command.yml` (`issues: write` on issue comments), `hc-check-digest.yml` (`workflow_run` and broad metadata events), `hc-control-bot-advisory-comment.yml` (`pull_request_target` and `issues: write`), `hc-repo-inventory.yml` (`id-token: write` and `attestations: write`), `hc-review-window-marker.yml` (`issues: write`), `hc-signal-watch-report.yml` (job-level `issues: write` and live signal context), `pr-risk-labeler.yml` (`pull-requests: write` and `issues: write`), and `safe-auto-merge.yml` (`workflow_run`).
- No explicit `checks: write` or `statuses: write` scopes were observed in this review.

These findings are not fixes. They are advisory observations for human maintainers and future scoped PRs.

## 8. Follow-up items

- 3-3b optional: reduce permissions in separate workflow-specific PRs.
- 3-3c optional: add report-only permission drift warning if useful later.
- 3-4: duplicate or obsolete workflow overlap review.
