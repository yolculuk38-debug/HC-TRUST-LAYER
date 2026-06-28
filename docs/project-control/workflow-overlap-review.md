# Workflow Overlap Review

## 1. Purpose

This document is an advisory, documentation-only review of duplicate, overlapping, or possibly obsolete GitHub Actions workflows in HC-TRUST-LAYER.

It supports backlog item 3-4, “duplicate or obsolete workflow overlap review.” It documents observed workflow relationships and follow-up recommendations only. This review does not delete, disable, rename, merge, rewrite, or change any workflow.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true`.
- CI/checks are evidence, not trust authority.
- Overlap findings do not approve, reject, merge, certify, delete, disable, or establish truth.
- Human maintainer review remains the final authority.

Workflow status, artifacts, reports, labels, comments, summaries, digests, and advisory findings can support review. They do not establish legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, guaranteed correctness, or production readiness.

## 3. Review method

For each workflow under `.github/workflows/**`, this review inspected:

- workflow name;
- workflow file path;
- triggers;
- permissions summary;
- primary purpose;
- produced artifacts or reports;
- whether it validates, guards, reports, comments, labels, digests, audits, or supports auto-merge;
- relationship to `docs/project-control/workflow-taxonomy.md`, `docs/project-control/workflow-naming-review.md`, and `docs/project-control/workflow-permissions-review.md`.

The overlap labels below are conservative:

- `no obvious overlap`;
- `complementary`;
- `partial overlap`;
- `possible duplicate`;
- `possible obsolete`;
- `needs maintainer confirmation`.

## 4. Overlap review table

| Workflow name | Workflow file | Primary purpose | Similar / related workflows | Overlap type | Risk if duplicated or stale | Recommendation |
|---|---|---|---|---|---|---|
| HC-TRUST-LAYER Archive Automation | `.github/workflows/archive.yml` | Archive normalization, hash verification, index, and QR evidence on scoped main pushes. | `verify-archive.yml`, `auto-hash.yml`, `validate.yml` | partial overlap | Duplicate archive/hash evidence could create noisy main-push checks or unclear archive authority. | Keep for now; compare artifacts and required check status before any consolidation. |
| Auto Generate Hash Files | `.github/workflows/auto-hash.yml` | Generates and commits hash files for verified records. | `archive.yml`, `verify-archive.yml`, `canonical-artifacts.yml` | complementary / needs maintainer confirmation | Write-capable generated evidence could be mistaken for validation authority or duplicate hash evidence. | Do not merge with read-only checks; review separately because it uses repository write behavior. |
| Automation Gate | `.github/workflows/automation-gate.yml` | PR gate for title/body, blocked binary files, and Python syntax. | `governance-preflight.yml`, `policy-evaluation.yml`, `pr-scope-guard.yml`, `safe-auto-merge.yml` | complementary | If stale, auto-merge support or governance checks may reference outdated gate assumptions. | Keep; confirm whether downstream auto-merge support still needs this exact check name. |
| Canonical Artifact Boundary Guard | `.github/workflows/canonical-artifacts.yml` | Boundary guard for canonical, generated, record, and artifact expectations. | `validate.yml`, `verification-package-schema.yml`, `docs-drift.yml`, `auto-hash.yml` | complementary | Consolidation could blur canonical/generated/record authority boundaries. | Keep separate from general validation. |
| Docs Review Policy | `.github/workflows/docs-auto-merge.yml` | Read-only docs PR policy report with auto-merge boundary language. | `enable-auto-merge.yml`, `safe-auto-merge.yml`, `governance-preflight.yml` | partial overlap / possible obsolete | Filename suggests auto-merge history; duplicate disabled-auto-merge messaging may confuse reviewers. | Needs maintainer confirmation before any rename or removal; do not change behavior in this PR. |
| Docs Drift Check | `.github/workflows/docs-drift.yml` | Documentation drift validation. | `terminology.yml`, `terminology-autofix-suggest.yml`, `hc-control-bot-report.yml` | complementary | Duplicate docs warnings could hide which check is authoritative evidence. | Keep; preserve as validation separate from terminology and advisory report artifacts. |
| Enable PR Auto-merge | `.github/workflows/enable-auto-merge.yml` | Report-only disabled auto-merge boundary. | `safe-auto-merge.yml`, `docs-auto-merge.yml`, `governance-preflight.yml` | partial overlap / possible obsolete | Name implies enabling auto-merge despite disabled/report-only behavior. | Candidate for later maintainer-confirmed cleanup or rename; no deletion here. |
| Governance Preflight | `.github/workflows/governance-preflight.yml` | Governance preflight evidence for protected paths, review requirements, and auto-merge eligibility signals. | `policy-evaluation.yml`, `pr-scope-guard.yml`, `automation-gate.yml`, `pr-risk-labeler.yml` | complementary | Consolidation could mix advisory governance evidence with label mutation or scope checks. | Keep separate; do not merge with mutation workflows. |
| HC Assistant Command Listener | `.github/workflows/hc-assistant-command.yml` | Responds to `/hc` issue comments with advisory assistant output. | `hc-control-bot-advisory-comment.yml`, `hc-control-bot-report.yml`, `hc-review-window-marker.yml` | partial overlap / needs maintainer confirmation | Multiple comment surfaces may confuse advisory source and authority boundaries. | Keep only if command surface remains intended; review comment ownership before expansion. |
| HC Check Digest | `.github/workflows/hc-check-digest.yml` | Digest of PR, review, check, status, and workflow metadata. | `hc-repo-inventory.yml`, `release-audit.yml`, `hc-control-bot-report.yml`, `scorecard.yml` | complementary | Duplicate summaries may be read as final status or branch-protection truth. | Keep separate from inventory and release audit; verify consumers before changes. |
| HC Control Bot Advisory Comment | `.github/workflows/hc-control-bot-advisory-comment.yml` | Posts or updates one advisory PR comment from privileged PR context. | `hc-control-bot-report.yml`, `hc-assistant-command.yml`, `hc-review-window-marker.yml` | partial overlap / needs maintainer confirmation | Comment authority may overlap with report artifacts; `pull_request_target` and `issues: write` are high-sensitivity. | Do not consolidate with report-only workflow unless maintainers explicitly approve boundaries. |
| HC Control Bot Report | `.github/workflows/hc-control-bot-report.yml` | Report-only PR scan, artifacts, and taxonomy drift warning. | `hc-control-bot-advisory-comment.yml`, `hc-check-digest.yml`, `docs-drift.yml` | complementary | Report artifacts could duplicate advisory comments or digest evidence. | Keep report-only separation; maintain no-comment/no-label boundary. |
| HC Repository Inventory | `.github/workflows/hc-repo-inventory.yml` | Repository inventory and attestation evidence. | `hc-check-digest.yml`, `release-audit.yml`, `scorecard.yml` | complementary / needs maintainer confirmation | Inventory and attestation outputs may be over-read if duplicated with release audit. | Keep; review attestation-specific permissions separately before any consolidation. |
| HC Review Window Marker | `.github/workflows/hc-review-window-marker.yml` | Manual advisory marker/debug fallback for review-window status. | `hc-control-bot-report.yml`, `hc-control-bot-advisory-comment.yml` | possible obsolete / needs maintainer confirmation | Manual/debug workflow with comment permission may remain after active reporting moved elsewhere. | Mark as manual/debug; consider later removal only after checking recent runs and docs references. |
| HC Signal Watch Live RSS Dry Run | `.github/workflows/hc-signal-watch-live-rss-dry-run.yml` | Manual live RSS observation dry run. | `hc-signal-watch-report.yml` | partial overlap / possible obsolete | Manual live fetch may duplicate report workflow dry-run capabilities. | Confirm whether operators still need it before removal; preserve as manual/debug until then. |
| HC Signal Watch Report | `.github/workflows/hc-signal-watch-report.yml` | Scheduled/manual/PR signal watch report and bounded console-comment update. | `hc-signal-watch-live-rss-dry-run.yml`, `scorecard.yml`, `release-audit.yml` | complementary | External signal and comment outputs may be confused with repository validation. | Keep separated from validation; review live/manual dry-run overlap later. |
| Advisory Policy Evaluation | `.github/workflows/policy-evaluation.yml` | Advisory policy evaluation for PRs. | `governance-preflight.yml`, `pr-scope-guard.yml`, `automation-gate.yml` | complementary | Duplicate governance language could confuse policy evidence with final approval. | Keep separate; document policy scope if future consolidation is proposed. |
| PR Risk Labeler | `.github/workflows/pr-risk-labeler.yml` | Applies/removes PR risk labels and removes auto-merge label when needed. | `pr-scope-guard.yml`, `governance-preflight.yml`, `policy-evaluation.yml` | complementary / needs maintainer confirmation | Label mutation could be mixed with read-only advisory checks if consolidated. | Do not merge with read-only checks; treat mutation boundary as separate authority. |
| PR Scope Guard | `.github/workflows/pr-scope-guard.yml` | Advisory scope/risk guard for PR paths. | `pr-risk-labeler.yml`, `governance-preflight.yml`, `policy-evaluation.yml` | complementary | Duplicated scope logic could drift from labeler or governance preflight. | Keep read-only guard separate; compare rules before any future cleanup. |
| HC Release Audit | `.github/workflows/release-audit.yml` | Release audit artifacts and summaries. | `hc-repo-inventory.yml`, `hc-check-digest.yml`, `scorecard.yml` | complementary | Audit artifacts could be mistaken for inventory attestations or check digests. | Keep separate; verify release-specific consumers before changes. |
| Safe Auto Merge | `.github/workflows/safe-auto-merge.yml` | Report-only disabled auto-merge support, including `workflow_run` after Automation Gate. | `enable-auto-merge.yml`, `docs-auto-merge.yml`, `automation-gate.yml`, `governance-preflight.yml` | partial overlap / possible obsolete | Duplicate disabled auto-merge workflows may confuse reviewers; `workflow_run` adds sensitivity. | Candidate for maintainer-confirmed cleanup or rename in a separate PR. |
| OpenSSF Scorecard Advisory | `.github/workflows/scorecard.yml` | Scheduled/manual OpenSSF Scorecard advisory evidence. | `release-audit.yml`, `hc-repo-inventory.yml`, `hc-check-digest.yml` | no obvious overlap | If stale, security posture evidence may be ignored or misread. | Keep; not a consolidation candidate from this review. |
| Terminology Autofix Suggest (Advisory) | `.github/workflows/terminology-autofix-suggest.yml` | Uploads advisory terminology autofix suggestions when terminology guard fails. | `terminology.yml`, `docs-drift.yml` | complementary | Suggestion artifacts could be mistaken for automatic edits. | Keep separate from the blocking guard; do not add mutation behavior. |
| Terminology Guard | `.github/workflows/terminology.yml` | Terminology boundary validation. | `terminology-autofix-suggest.yml`, `docs-drift.yml` | complementary | Duplicate docs checks may obscure terminology-specific failures. | Keep as the primary terminology check. |
| HC-TRUST-LAYER Validation | `.github/workflows/validate.yml` | Broad validation and runtime/schema/record test evidence. | `verification-package-schema.yml`, `canonical-artifacts.yml`, `archive.yml`, `verify-archive.yml` | complementary | Over-consolidation could make trust-kernel checks less reviewable. | Keep broad validation separate from specialized boundary checks. |
| verification-package-schema | `.github/workflows/verification-package-schema.yml` | Verification package schema/example validation. | `validate.yml`, `canonical-artifacts.yml` | complementary | Schema-specific evidence could be hidden inside broad validation if merged. | Keep specialized schema check separate unless maintainers intentionally consolidate. |
| Verify HC-TRUST-LAYER Archive | `.github/workflows/verify-archive.yml` | Main-push archive structure verification. | `archive.yml`, `validate.yml`, `auto-hash.yml` | partial overlap | Duplicate archive checks may add noise if they validate the same paths differently. | Compare exact scripts/artifacts and branch protection before any later cleanup. |

## 5. High-risk overlap areas

### Auto-merge / safe auto-merge / enable auto-merge

`docs-auto-merge.yml`, `enable-auto-merge.yml`, and `safe-auto-merge.yml` appear partially overlapping because each references docs review or disabled/report-only auto-merge support. They do not appear to perform auto-merge in this review, but their names can imply stronger behavior than observed.

- Current assessment: partial overlap; possible obsolete candidates require maintainer confirmation.
- Stale or obsolete signal: `enable-auto-merge.yml` and `safe-auto-merge.yml` may preserve historical disabled-auto-merge surfaces.
- Later deletion/disable consideration: only after checking recent runs, required check status, branch protection/rulesets, workflow references, and maintainer intent.
- Evidence to check before removal: run history, check names required by branch protection, PR docs that mention auto-merge, downstream references to `Automation Gate`, and whether maintainers still want a report-only auto-merge boundary.

### HC Control Bot Report / advisory comment / assistant command listener

`hc-control-bot-report.yml`, `hc-control-bot-advisory-comment.yml`, and `hc-assistant-command.yml` all provide advisory HC bot surfaces, but they have different authority boundaries: report-only artifacts, advisory PR comment mutation, and command-triggered issue comment responses.

- Current assessment: complementary with partial overlap in reviewer-facing advisory output.
- Stale or obsolete signal: none confirmed; comment surfaces need maintainer confirmation because multiple public advisory comments may confuse source and authority.
- Later deletion/disable consideration: only after deciding which advisory surface is intended for routine PR review and which is command/manual support.
- Evidence to check before removal: recent comment usage, artifact usage, issue comment command usage, public docs references, and any required review-window process dependency.

### HC Check Digest / repository inventory / release audit

`hc-check-digest.yml`, `hc-repo-inventory.yml`, and `release-audit.yml` all produce evidence summaries, but they target different review moments: PR/check metadata digest, repository inventory/attestation evidence, and release audit artifacts.

- Current assessment: complementary.
- Stale or obsolete signal: none confirmed.
- Later deletion/disable consideration: not recommended without a dedicated audit/evidence lifecycle review.
- Evidence to check before removal: artifact consumers, attestation requirements, release process docs, run history, and whether branch protection or release procedures expect the specific check names.

### Docs drift / terminology guard / terminology autofix suggest

`docs-drift.yml`, `terminology.yml`, and `terminology-autofix-suggest.yml` overlap around documentation quality, but they separate drift validation, terminology validation, and advisory suggestions.

- Current assessment: complementary.
- Stale or obsolete signal: none confirmed.
- Later deletion/disable consideration: not recommended unless maintainers intentionally redesign docs validation.
- Evidence to check before removal: failure patterns, artifact usage, docs drift checker scope, terminology allowlist changes, and whether autofix suggestion artifacts remain useful.

### Governance preflight / advisory policy evaluation / PR scope guard

`governance-preflight.yml`, `policy-evaluation.yml`, and `pr-scope-guard.yml` all evaluate PR governance or scope signals. `pr-risk-labeler.yml` is related but mutates labels, so it should not be merged into read-only checks without explicit review.

- Current assessment: complementary with possible rule overlap.
- Stale or obsolete signal: none confirmed; duplicated path/risk rules may drift over time.
- Later deletion/disable consideration: only after comparing rule sets and confirming no branch-protection or reviewer process dependency.
- Evidence to check before removal: scripts invoked, changed-path rule sources, label behavior, check requirement status, and maintainer expectations for advisory versus mutating outputs.

### Signal watch workflows

`hc-signal-watch-report.yml` and `hc-signal-watch-live-rss-dry-run.yml` overlap around signal watch and RSS observation. The report workflow appears to be the routine scheduled/manual report surface, while live RSS dry run appears manual/debug.

- Current assessment: partial overlap; manual/debug surface may be a cleanup candidate.
- Stale or obsolete signal: live RSS dry run may be historical or operator-only.
- Later deletion/disable consideration: only if maintainers confirm the report workflow covers required dry-run use.
- Evidence to check before removal: operator docs, recent manual dispatches, issue binding docs, network/live-fetch expectations, and artifacts used during signal-watch review.

### Manual/debug workflows

`hc-review-window-marker.yml` and `hc-signal-watch-live-rss-dry-run.yml` appear manual/debug oriented. Manual workflows can still have high sensitivity when they use comment permissions or live external inputs.

- Current assessment: needs maintainer confirmation.
- Stale or obsolete signal: possible, especially if active behavior moved to report workflows.
- Later deletion/disable consideration: reasonable only as a separate PR after the workflow is clearly marked historical/manual/debug and no longer needed.
- Evidence to check before removal: recent dispatches, operator documentation, issue/PR comments produced, check requirements, and maintainer confirmation.

### Validation and schema workflows

`validate.yml`, `verification-package-schema.yml`, `canonical-artifacts.yml`, `archive.yml`, and `verify-archive.yml` overlap around validation evidence, schema evidence, canonical/generated boundaries, and archive structure.

- Current assessment: complementary with partial archive overlap between `archive.yml` and `verify-archive.yml`.
- Stale or obsolete signal: no schema or validation workflow is confirmed obsolete.
- Later deletion/disable consideration: not recommended without checking exact scripts, artifacts, and branch-protection dependencies.
- Evidence to check before removal: scripts invoked, path filters, artifact outputs, branch protection/rulesets, required checks, generated/canonical boundary docs, and release/archive procedures.

## 6. Recommended HC workflow consolidation rules

- Do not delete or disable a workflow without checking recent runs, required check status, branch protection, artifacts, and downstream docs.
- Do not merge two workflows if one has stronger permissions or privileged triggers.
- Prefer keeping validation, advisory reporting, digesting, and mutation/comment behavior separated.
- Prefer documentation-first review before enforcement or deletion.
- Treat workflows using `pull_request_target`, `workflow_run`, `issues: write`, `contents: write`, `id-token: write`, or `attestations: write` as high-sensitivity.
- If a workflow is only historical/manual/debug, mark it as such before removal.
- Any removal must be a separate PR with explicit human approval.

## 7. Findings

- Workflows that appear complementary include `canonical-artifacts.yml`, `docs-drift.yml`, `governance-preflight.yml`, `hc-check-digest.yml`, `hc-repo-inventory.yml`, `policy-evaluation.yml`, `pr-scope-guard.yml`, `release-audit.yml`, `scorecard.yml`, `terminology.yml`, `terminology-autofix-suggest.yml`, `validate.yml`, and `verification-package-schema.yml`.
- Workflows with partial overlap include `archive.yml` with `verify-archive.yml`, the three auto-merge-named workflows, HC Control Bot/advisory command surfaces, signal watch workflows, and validation/archive workflows.
- Workflows needing maintainer confirmation include `auto-hash.yml`, `docs-auto-merge.yml`, `enable-auto-merge.yml`, `hc-assistant-command.yml`, `hc-control-bot-advisory-comment.yml`, `hc-review-window-marker.yml`, `hc-signal-watch-live-rss-dry-run.yml`, `pr-risk-labeler.yml`, and `safe-auto-merge.yml`.
- Workflows that may be candidates for later cleanup include `enable-auto-merge.yml`, `safe-auto-merge.yml`, `hc-review-window-marker.yml`, and `hc-signal-watch-live-rss-dry-run.yml`, but no cleanup is approved by this document.
- Workflows that should not be consolidated without explicit human approval include mutation/comment/label workflows and read-only validation/report workflows because they separate authority boundaries.

## 8. Follow-up items

- 3-4b optional: clean up one confirmed obsolete workflow in a separate PR.
- 3-4c optional: add a report-only workflow overlap/drift note if useful later.
- 3-5 optional: update the project-control workflow index after any confirmed cleanup.
- 4-1 next phase: core package boundary review, if backlog order continues.
