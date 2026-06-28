# GitHub Actions Workflow Taxonomy

## 1. Purpose

This document is an advisory, documentation-only taxonomy for GitHub Actions workflow role and authority classification in HC-TRUST-LAYER. It helps maintainers, contributors, CI checks, and AI-assisted reviewers understand current workflow roles without changing workflow behavior.

This taxonomy documents observed workflow intent from the current `.github/workflows/**` files. It does not make any workflow more authoritative than its configured triggers, permissions, branch protection status, repository settings, or human maintainer review allow.

## 2. HC boundary

The following HC boundary markers apply to this taxonomy and to workflow interpretation unless a more specific, human-reviewed governance document says otherwise:

- `advisory_only=true` where applicable.
- `public_safe=true` where applicable.
- `truth_guarantee=false`.
- `human_review_required=true`.
- CI/checks are evidence, not trust authority.
- Report-only/advisory workflows do not approve, reject, merge, or establish truth.
- Humans remain final review and merge authority.

Workflow outputs, summaries, labels, comments, artifacts, and status checks can support review. They do not create legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness claims.

## 3. Classification buckets

| Bucket | Definition |
|---|---|
| report-only/advisory | Produces summaries, warnings, artifacts, or advisory evidence without approving, rejecting, merging, or establishing truth. |
| validation/check | Runs deterministic checks or tests that may fail a workflow run; still evidence for human review, not final trust authority. |
| governance/preflight | Evaluates review, governance, or automation eligibility boundaries before maintainers act. |
| scope/risk guard | Classifies changed paths, risk indicators, or review sensitivity; may be advisory or may mutate labels if configured. |
| artifact/canonical boundary guard | Checks canonical, generated, record, schema, or artifact boundaries and preserves review sensitivity around evidence-bearing paths. |
| inventory/audit/digest | Produces inventory, audit, digest, or release evidence for reviewers. |
| auto-merge support / non-authoritative automation | Mentions or supports auto-merge-related review flow, but remains non-authoritative unless the workflow actually performs a merge. |
| manual/debug | Runs only by manual dispatch or for bounded operator/debug use. |
| uncertain / needs maintainer confirmation | Behavior, authority, risk, or intended role is unclear from the workflow file and should be confirmed by maintainers before expansion. |

## 4. Workflow table

Authority levels are conservative. “High sensitivity” means the workflow uses a privileged/high-risk event, write-capable permissions, repository or PR state mutation, secrets, status/check metadata, comments, labels, artifacts tied to provenance, or protected/canonical path interpretation.

| Workflow name | Workflow file path | Category | Authority level | Human review sensitivity | Notes |
|---|---|---|---|---|---|
| HC-TRUST-LAYER Archive Automation | `.github/workflows/archive.yml` | validation/check | Evidence only; main-push archive automation with read-only token. | Medium | Runs normalization, hash verification, archive index, and QR generation on main pushes for scoped paths. Does not write repository state. |
| Auto Generate Hash Files | `.github/workflows/auto-hash.yml` | artifact/canonical boundary guard | Repository-mutating automation; needs maintainer confirmation for authority boundaries. | High | Uses `contents: write`, commits, and pushes generated `hash/*.sha256`. Note for 3-3: write permission. Note for 3-4: overlaps with archive/hash evidence surfaces. |
| Automation Gate | `.github/workflows/automation-gate.yml` | governance/preflight | Check evidence; can fail on missing PR title/body, blocked binary files, or Python syntax. | Medium | Read-only PR gate. Does not approve, reject, or merge. |
| Canonical Artifact Boundary Guard | `.github/workflows/canonical-artifacts.yml` | artifact/canonical boundary guard | Check evidence for canonical/generated/record boundary expectations. | High | Read-only token, but evaluates protected and canonical-adjacent paths. Human review remains required. |
| Docs Review Policy | `.github/workflows/docs-auto-merge.yml` | auto-merge support / non-authoritative automation | Advisory report-only classification. | Medium | Name/file history may sound stronger than behavior; workflow states it is read-only and report-only. Note for 3-2: review name vs behavior. |
| Docs Drift Check | `.github/workflows/docs-drift.yml` | validation/check | Check evidence for documentation drift. | Medium | Read-only check across docs, implementation references, schema, examples, and workflow files. Does not establish truth. |
| Enable PR Auto-merge | `.github/workflows/enable-auto-merge.yml` | auto-merge support / non-authoritative automation | Report-only; automatic merge enablement is disabled in the workflow. | Medium | Name sounds stronger than behavior. Note for 3-2: review name vs actual disabled/report-only behavior. |
| Governance Preflight | `.github/workflows/governance-preflight.yml` | governance/preflight | Governance check evidence; may fail based on preflight script status. | High | Read-only token, but evaluates risk, protected paths, human review requirement, and auto-merge eligibility signals. |
| HC Assistant Command Listener | `.github/workflows/hc-assistant-command.yml` | report-only/advisory | Advisory command response; may write issue comments. | High | Uses `issues: write` and posts/updates public advisory comments for `/hc` commands. Note for 3-3: write permission and command surface need least-privilege review. |
| HC Check Digest | `.github/workflows/hc-check-digest.yml` | inventory/audit/digest | Advisory digest evidence from live PR/check/review metadata. | High | Uses `workflow_run`, `check_run`, status, review events, secrets token, and read permissions for actions/checks/PRs. Does not label, comment, approve, or merge. Note for 3-3: review event and token exposure risk. |
| HC Control Bot Advisory Comment | `.github/workflows/hc-control-bot-advisory-comment.yml` | report-only/advisory | Advisory comment automation; not trust authority. | High | Uses `pull_request_target` and `issues: write`. Treat as privileged/high-risk when combined with untrusted PR context. Note for 3-3: event and write permission require careful review. |
| HC Control Bot Report | `.github/workflows/hc-control-bot-report.yml` | report-only/advisory | Report-only scan and artifacts. | Medium | Checks out trusted base and PR docs as data, uploads artifacts, includes HC Review Window status, and emits the HC Workflow Taxonomy Drift advisory step/artifact when workflow changes lack a taxonomy update. Does not comment, label, approve, merge, or delay checks. |
| HC PR Lifecycle Compliance Report | `.github/workflows/hc-pr-lifecycle-compliance-report.yml` | report-only/advisory | Artifact-only, read-only PR lifecycle compliance report with no write authority. | Medium | Runs on `pull_request`, uploads JSON and Markdown artifacts, and reports advisory lifecycle signals for human review. Does not comment, label, request reviewers, assign, approve, merge, update PR or issue bodies, or resolve threads. |
| HC Repository Inventory | `.github/workflows/hc-repo-inventory.yml` | inventory/audit/digest | Inventory/attestation evidence; needs maintainer confirmation for attestation authority boundaries. | High | Uses `id-token: write` and `attestations: write`. Note for 3-3: write permissions and provenance implications require least-privilege review. |
| HC Review Window Marker | `.github/workflows/hc-review-window-marker.yml` | manual/debug | Manual advisory marker only. | High | `workflow_dispatch` only and uses `issues: write`; automatic PR triggers are disabled. Does not delay checks, approve, merge, label, assign, close, or request reviewers. |
| HC Signal Watch Live RSS Dry Run | `.github/workflows/hc-signal-watch-live-rss-dry-run.yml` | manual/debug | Manual read-only dry-run evidence. | Medium | Manual live RSS observation only; artifact and step summary output. Network fetch results remain advisory and require human review. |
| HC Signal Watch Report | `.github/workflows/hc-signal-watch-report.yml` | inventory/audit/digest | Advisory signal report; gated console-comment job may update one issue comment on main/schedule/manual contexts. | High | Report job is read-only. Console-comment job uses `issues: write` outside PR runs to update issue `#1082`. Note for 3-3: write permission and external signal ingestion need review. |
| Advisory Policy Evaluation | `.github/workflows/policy-evaluation.yml` | governance/preflight | Advisory policy evidence. | Medium | Read-only PR policy evaluation. Does not approve, reject, merge, or establish truth. |
| PR Risk Labeler | `.github/workflows/pr-risk-labeler.yml` | scope/risk guard | PR label mutation; non-merge authority. | High | Uses `pull-requests: write` and `issues: write`; creates/applies/removes labels including `manual-review` and removes `auto-merge`. Note for 3-3: write permissions. |
| PR Scope Guard | `.github/workflows/pr-scope-guard.yml` | scope/risk guard | Advisory scope evidence; currently non-blocking due to `continue-on-error`. | Medium | Read-only token and explicit advisory reminder. Human-supervised validation remains required. |
| HC Release Audit | `.github/workflows/release-audit.yml` | inventory/audit/digest | Report-only release audit evidence. | Medium | Produces JSON/Markdown artifacts and step summary. Does not publish releases, create tags, mutate changelogs, or grant merge authority. |
| Safe Auto Merge | `.github/workflows/safe-auto-merge.yml` | auto-merge support / non-authoritative automation | Report-only; does not enable, disable, or perform merge. | High | Uses `workflow_run`, so treat as higher-risk even though permissions are read-only and the job only runs on `pull_request`. Note for 3-2: review name vs disabled/report-only behavior. Note for 3-4: overlaps with Enable PR Auto-merge and Docs Review Policy naming. |
| OpenSSF Scorecard Advisory | `.github/workflows/scorecard.yml` | inventory/audit/digest | Advisory security evidence. | Medium | Scheduled/manual read-only Scorecard scan with artifacts. Plain-language risk areas include Dangerous-Workflow and Token-Permissions; findings are evidence, not authority. |
| Terminology Autofix Suggest (Advisory) | `.github/workflows/terminology-autofix-suggest.yml` | report-only/advisory | Advisory artifact only. | Low | Runs terminology guard and uploads suggested autofix report if needed. It does not modify, commit, push, approve, or merge. |
| Terminology Guard | `.github/workflows/terminology.yml` | validation/check | Check evidence for terminology boundaries. | Medium | Read-only terminology check for PRs and scoped main pushes. Does not replace human review. |
| HC-TRUST-LAYER Validation | `.github/workflows/validate.yml` | validation/check | Validation/test evidence for records, schema, hashes, generated audit snapshot, explorer index, and runtime/API tests. | High | Read-only token, but validates trust-kernel-adjacent records/schema/runtime behavior and uploads generated artifacts. |
| verification-package-schema | `.github/workflows/verification-package-schema.yml` | validation/check | Schema/example validation evidence. | High | Read-only token, but checks schema/example verification package boundaries. Human review remains required. |
| Verify HC-TRUST-LAYER Archive | `.github/workflows/verify-archive.yml` | validation/check | Main-push archive structure evidence. | Medium | Read-only structural check on main pushes for scoped archive paths. Does not mutate repository state. |

## 5. Authority rules

- Advisory/report-only workflows may produce summaries, warnings, labels, comments, artifacts, or step summaries, but they do not establish truth.
- Validation/check workflows may detect failing conditions but do not replace human review.
- Auto-merge support workflows must be treated as support/non-authoritative unless they actually perform a merge; if uncertain, mark `needs maintainer confirmation`.
- Workflows touching labels, reviewers, comments, pull requests, statuses, or contents require higher review sensitivity.
- Workflows using `pull_request_target`, `workflow_run`, write permissions, or secrets must be marked high-risk or `needs maintainer confirmation`.
- Status checks are merge-gate evidence only when configured by repository branch protection or rulesets. They are not truth authority.
- GitHub Actions permissions should be understood and minimized using least-privilege review. OpenSSF Scorecard risk areas such as Dangerous-Workflow and Token-Permissions should be considered high-risk review topics in plain language.

## 6. What this taxonomy does not do

This PR and document do not:

- change workflow permissions;
- change branch protection;
- enable or disable auto-merge;
- make advisory checks authoritative;
- replace CODEOWNERS;
- replace maintainer review;
- certify workflow security.

## Related naming review

See `docs/project-control/workflow-naming-review.md` for the advisory backlog item 3-2 review of workflow names against observed behavior and authority boundaries. See `docs/project-control/workflow-permissions-review.md` for the advisory backlog item 3-3 least-privilege permissions review. See `docs/project-control/workflow-overlap-review.md` for the advisory backlog item 3-4 duplicate or obsolete workflow overlap review.

## 7. Follow-up items

- 3-1b: HC Control Bot Report now includes a report-only workflow taxonomy drift checker.
  - Rule: if `.github/workflows/**` changes but `docs/project-control/workflow-taxonomy.md` does not change, HC Control Bot Report warns.
  - The checker is stdlib-only, deterministic, report-only, and advisory.
  - It does not block merge.
  - It emits: “Workflow files changed without workflow taxonomy update. Human review required.”
- 3-2: review workflow names vs actual behavior.
- 3-3: review least-privilege permissions. See `docs/project-control/workflow-permissions-review.md`.
- 3-4: duplicate or obsolete workflow overlap review is documented in `docs/project-control/workflow-overlap-review.md`.
