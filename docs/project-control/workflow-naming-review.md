# Workflow Naming Review

## 1. Purpose

This document is a documentation-only, advisory review of GitHub Actions workflow names compared with their observed behavior and authority level in HC-TRUST-LAYER.

It supports backlog item 3-2, “workflow names vs behavior review.” It does not rename workflows, edit workflow files, change permissions, add checkers, change branch protection, or change auto-merge behavior.

## 2. HC boundary

The following HC boundary applies to this naming review:

- `advisory_only=true` where applicable.
- `public_safe=true` where applicable.
- `truth_guarantee=false`.
- `human_review_required=true`.
- CI/checks are evidence, not trust authority.
- Workflow names must not imply legal truth, certification, autonomous governance, automatic approval, or merge authority unless the workflow actually has that behavior and maintainer governance explicitly allows it.

Workflow names, job summaries, labels, comments, artifacts, and check results can support human review. They do not establish legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness.

## 3. Review method

For each workflow under `.github/workflows/**`, this review compares:

- workflow `name:`;
- workflow filename;
- triggers;
- permissions;
- whether the workflow comments, labels, requests reviewers, approves, merges, uploads artifacts, produces reports, or only validates;
- the existing category in `docs/project-control/workflow-taxonomy.md`.

The labels below are conservative:

- `aligned`;
- `mostly aligned`;
- `needs clarification`;
- `misleading / should rename later`;
- `needs maintainer confirmation`.

## 4. Naming review table

| Workflow name | Workflow file | Taxonomy category | Observed behavior | Name/behavior alignment | Risk if misunderstood | Recommendation |
|---|---|---|---|---|---|---|
| HC-TRUST-LAYER Archive Automation | `.github/workflows/archive.yml` | validation/check | Runs archive normalization, hash verification, index, and QR checks on scoped main pushes with read-only contents permission. | mostly aligned | “Automation” could be read as repository mutation, but observed behavior is check evidence only. | Keep; taxonomy should continue to clarify evidence-only behavior. |
| Auto Generate Hash Files | `.github/workflows/auto-hash.yml` | artifact/canonical boundary guard | Uses `contents: write` to commit and push generated hash files for scoped records. | aligned | Name correctly signals generation, but write authority and evidence-bearing output could be underestimated. | Keep pending least-privilege review; document write behavior clearly. |
| Automation Gate | `.github/workflows/automation-gate.yml` | governance/preflight | Read-only PR checks for title/body, blocked binaries, and Python syntax. | mostly aligned | “Gate” may imply final approval or merge authority rather than check evidence. | Keep for now; clarify that this is a check gate, not trust authority. |
| Canonical Artifact Boundary Guard | `.github/workflows/canonical-artifacts.yml` | artifact/canonical boundary guard | Read-only boundary check for canonical/generated/record expectations. | aligned | “Canonical” and “Guard” may be interpreted as definitive canonical truth. | Keep; preserve human-review boundary in related docs. |
| Docs Review Policy | `.github/workflows/docs-auto-merge.yml` | auto-merge support / non-authoritative automation | Read-only PR report in logs; does not enable, approve, or merge. | needs clarification | Filename still says `docs-auto-merge`, which can imply automatic merge behavior. | Consider later filename/name cleanup only if maintainers find the history materially misleading. |
| Docs Drift Check | `.github/workflows/docs-drift.yml` | validation/check | Read-only documentation drift check on PRs and scoped main pushes. | aligned | “Check” is appropriate, but failures remain evidence rather than trust authority. | Keep. |
| Enable PR Auto-merge | `.github/workflows/enable-auto-merge.yml` | auto-merge support / non-authoritative automation | Read-only report-only workflow; automatic merge enablement is disabled. | misleading / should rename later | Name implies enabling auto-merge even though the workflow does not do so. | Follow-up 3-2b candidate; rename separately if maintainers agree. |
| Governance Preflight | `.github/workflows/governance-preflight.yml` | governance/preflight | Read-only governance preflight check for risk, protected paths, review requirement, and auto-merge eligibility signals. | aligned | “Governance” could be mistaken for final governance authority. | Keep; continue to state human final authority. |
| HC Assistant Command Listener | `.github/workflows/hc-assistant-command.yml` | report-only/advisory | Handles `/hc` issue comments and may post or update advisory issue comments with `issues: write`. | mostly aligned | “Assistant” could be mistaken for authoritative governance response; write-comment permission may be hidden. | Keep; document write-comment behavior in least-privilege review. |
| HC Check Digest | `.github/workflows/hc-check-digest.yml` | inventory/audit/digest | Produces advisory digest evidence from PR/check/review metadata and workflow events. | aligned | “Digest” appropriately signals summary, but live metadata may be over-read as final status. | Keep. |
| HC Control Bot Advisory Comment | `.github/workflows/hc-control-bot-advisory-comment.yml` | report-only/advisory | Uses `pull_request_target` and `issues: write` to post or update an advisory PR comment. | aligned | “Control Bot” could imply governance authority despite “Advisory Comment.” | Keep only with taxonomy and HC boundary clarification. |
| HC Control Bot Report | `.github/workflows/hc-control-bot-report.yml` | report-only/advisory | Produces report-only scan output and artifacts, including taxonomy drift warning. | mostly aligned | “Control Bot” could imply enforcement or autonomous control. | Keep; maintain report-only wording in summaries and taxonomy. |
| HC Repository Inventory | `.github/workflows/hc-repo-inventory.yml` | inventory/audit/digest | Produces inventory evidence and artifacts; trusted contexts can use `id-token: write` and `attestations: write`. | needs maintainer confirmation | “Inventory” is mild, but attestation permissions can imply provenance authority. | Keep; cover permissions in follow-up 3-3. |
| HC Review Window Marker | `.github/workflows/hc-review-window-marker.yml` | manual/debug | Manual advisory marker that may create or update a PR comment with `issues: write`. | mostly aligned | “Marker” is acceptable, but comment mutation and review-window wording may be over-read. | Keep; do not expand automatic behavior without review. |
| HC Signal Watch Live RSS Dry Run | `.github/workflows/hc-signal-watch-live-rss-dry-run.yml` | manual/debug | Manual read-only live RSS observation dry run with artifact and summary output. | aligned | External signal observation could be misunderstood as verified evidence. | Keep; preserve dry-run and advisory wording. |
| HC Signal Watch Report | `.github/workflows/hc-signal-watch-report.yml` | inventory/audit/digest | Produces advisory signal reports; a gated console-comment job may update an issue comment outside PR runs. | mostly aligned | “Signal Watch” may be mistaken for monitoring authority or verified external truth. | Keep; document comment-writing behavior in 3-3. |
| Advisory Policy Evaluation | `.github/workflows/policy-evaluation.yml` | governance/preflight | Read-only PR policy evaluation evidence. | aligned | “Policy Evaluation” could imply enforcement if “Advisory” is ignored. | Keep; retain “Advisory” in workflow name. |
| PR Risk Labeler | `.github/workflows/pr-risk-labeler.yml` | scope/risk guard | Mutates PR labels and can create labels, including manual-review and auto-merge label changes. | aligned | Label mutation can be mistaken for approval, rejection, or merge authority. | Keep pending least-privilege review; document non-merge authority clearly. |
| PR Scope Guard | `.github/workflows/pr-scope-guard.yml` | scope/risk guard | Read-only advisory scope guard with non-blocking behavior. | mostly aligned | “Guard” may imply blocking enforcement. | Keep; clarify advisory/non-blocking behavior. |
| HC Release Audit | `.github/workflows/release-audit.yml` | inventory/audit/digest | Produces release audit JSON/Markdown artifacts and summaries; does not publish releases. | mostly aligned | “Audit” can imply certification or completeness. | Keep only with evidence-only boundary. |
| Safe Auto Merge | `.github/workflows/safe-auto-merge.yml` | auto-merge support / non-authoritative automation | Read-only report-only workflow; does not enable, disable, approve, or perform merge. | misleading / should rename later | Name implies safe automatic merge behavior that the workflow does not perform. | Follow-up 3-2b candidate; rename separately if maintainers agree. |
| OpenSSF Scorecard Advisory | `.github/workflows/scorecard.yml` | inventory/audit/digest | Scheduled/manual read-only Scorecard scan with artifacts. | aligned | Scorecard findings may be over-read as certification. | Keep; advisory wording is appropriate. |
| Terminology Autofix Suggest (Advisory) | `.github/workflows/terminology-autofix-suggest.yml` | report-only/advisory | Runs terminology guard and uploads suggested autofix report; does not commit changes. | aligned | “Autofix” could be mistaken for automatic edits, but “Suggest (Advisory)” reduces risk. | Keep. |
| Terminology Guard | `.github/workflows/terminology.yml` | validation/check | Read-only terminology check on PRs and scoped main pushes. | mostly aligned | “Guard” may imply final terminology authority. | Keep; clarify check evidence only. |
| HC-TRUST-LAYER Validation | `.github/workflows/validate.yml` | validation/check | Runs validation/test evidence for records, schema, hashes, generated audit snapshot, explorer index, and runtime/API tests; uploads generated artifacts. | mostly aligned | “Validation” can be over-read as final correctness or trust guarantee. | Keep with HC boundary language. |
| verification-package-schema | `.github/workflows/verification-package-schema.yml` | validation/check | Read-only schema/example validation evidence. | aligned | Schema validation may be mistaken for complete package truth. | Keep. |
| Verify HC-TRUST-LAYER Archive | `.github/workflows/verify-archive.yml` | validation/check | Read-only archive structure check on scoped main pushes. | mostly aligned | “Verify” can imply final archive truth. | Keep with evidence-only boundary. |

## 5. High-risk naming patterns

The following patterns may imply authority if read without the workflow taxonomy and HC boundary:

- “Auto Merge”: acceptable only where the taxonomy and workflow behavior clarify that the workflow is non-authoritative unless it actually performs a merge.
- “Enable PR Auto-merge”: currently risky because the observed workflow is report-only and disabled for auto-merge enablement.
- “Safe Auto Merge”: currently risky because “safe” and “merge” can imply approved automated merge behavior that is not present.
- “Gate”: acceptable only when readers understand that checks are evidence and do not establish final trust authority.
- “Validation”: acceptable only when validation is understood as check evidence, not guaranteed correctness.
- “Policy Evaluation”: acceptable when paired with advisory wording and human-review boundaries.
- “Release Audit”: acceptable only as release evidence, not certification or complete audit assurance.
- “Control Bot”: acceptable only because taxonomy and HC boundary text clarify report-only or advisory authority.
- “Advisory Comment”: acceptable because it clearly limits comment authority, but write-comment behavior still requires least-privilege review.

## 6. Recommendations

Do not rename workflows in this PR. Recommended follow-up rules:

- Rename only if the current name is materially misleading.
- Prefer names that include “Advisory”, “Report”, “Check”, “Guard”, or “Digest” when behavior is report-only.
- Avoid names that imply final trust, certification, legal truth, identity finality, autonomous approval, or autonomous governance.
- If a workflow has write permissions, document that clearly in the taxonomy and naming review.
- Keep workflow naming changes small, separate, and reviewable by workflow family.

## 7. Follow-up items

- 3-2b optional: rename materially misleading workflows in separate PRs, one workflow family at a time.
- 3-3: least-privilege permissions review.
- 3-4: duplicate or obsolete workflow review.
