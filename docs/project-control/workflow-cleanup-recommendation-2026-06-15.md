# Workflow Cleanup Recommendation — 2026-06-15

## 1. Executive summary

This document is a report-only workflow cleanup recommendation for cleanup sequence item C after the repository cleanup audit sequence.

No workflows are deleted, disabled, edited, renamed, or moved by this report. No source, tests, generated artifacts, records, schemas, validators, policy, federation, signatures, canonical files, or trust-kernel files are changed. The only change proposed in this PR is this documentation report.

Human review is required before any future workflow cleanup. This report is advisory-only evidence for maintainers and does not create merge authority, approval authority, governance authority, or a truth guarantee.

Boundary values preserved by this recommendation:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human final authority remains required
- CI/checks are evidence, not trust authority
- generated artifacts are advisory evidence, not canonical records

## 2. Workflow inventory method

The workflow inventory inspected every file under `.github/workflows/**` without modifying any workflow. Each workflow was reviewed by:

- filename and declared workflow name;
- trigger type, including `push`, `pull_request`, `pull_request_target`, `issue_comment`, `workflow_dispatch`, `workflow_run`, and `schedule`;
- declared GitHub token permissions;
- whether the workflow mutates repository or pull request state;
- whether the workflow comments, labels, enables auto-merge, writes contents, or uses `pull_request_target`;
- whether the workflow is security, governance, release, provenance, validation, or verification related.

The method is intentionally conservative. Workflows with write permissions, comment behavior, label behavior, auto-merge-adjacent behavior, `pull_request_target`, `issue_comment`, or governance/security/release/provenance responsibility are not recommended for deletion or disablement in this report.

## 3. Workflow classification table

| Path | Purpose | Trigger | Permissions summary | Mutates repo state | Authority-changing risk | Recommendation | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `.github/workflows/archive.yml` | Runs archive-related normalization, hash verification, index, and QR generation commands on scoped pushes. | `push` paths for records, source, docs, and QR. | `contents: read`. | No. | Low. | KEEP | Read-only archive/provenance-adjacent workflow; no immediate cleanup action without human review of generated-output expectations. |
| `.github/workflows/auto-hash.yml` | Generates SHA-256 files for verified records and commits them. | `push` paths for `records/verified/**.md`. | `contents: write`. | Yes. | High. | HUMAN_REVIEW_REQUIRED | Write-capable generated hash workflow affects provenance evidence; no deletion or disablement should occur without explicit human review. |
| `.github/workflows/automation-gate.yml` | Checks PR title/body, generated binary file scope, and Python syntax. | `pull_request`. | `contents: read`, `pull-requests: read`. | No. | Low. | KEEP_SECURITY_OR_GOVERNANCE | PR control-layer guard; keep active unless maintainers approve a later targeted review. |
| `.github/workflows/canonical-artifacts.yml` | Runs canonical artifact boundary guard. | `pull_request`, `push` to `main`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Protects canonical artifact boundaries; generally should remain active. |
| `.github/workflows/docs-auto-merge.yml` | Classifies docs-only versus manual-review scope and reports requirements. | `pull_request`. | `contents: read`, `pull-requests: read`. | No. | Medium. | REVIEW_DUPLICATION_CANDIDATE | Auto-merge-adjacent by name but read-only/report-only; document overlap with other governance classifiers before any change. |
| `.github/workflows/docs-drift.yml` | Runs documentation drift check. | `pull_request`, `push` to `main`. | `contents: read`. | No. | Low. | KEEP_SECURITY_OR_GOVERNANCE | Documentation consistency guard; generally should remain active. |
| `.github/workflows/enable-auto-merge.yml` | Reports that automatic merge enablement is disabled. | `pull_request` lifecycle and label events. | `contents: read`, `pull-requests: read`. | No. | Medium. | REVIEW_DUPLICATION_CANDIDATE | Auto-merge-adjacent by name but report-only; any disable/delete decision is human-review-required. |
| `.github/workflows/governance-preflight.yml` | Runs governance preflight and reports risk signals. | `pull_request`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Governance boundary workflow; should generally remain active. |
| `.github/workflows/hc-assistant-command.yml` | Responds to `/hc` issue comments with advisory assistant output. | `issue_comment`. | `contents: read`, `issues: write`, `pull-requests: read`. | Yes, comments. | High. | PARK_HIGH_RISK | Comment-capable command listener uses issue comments and write permission; requires security review before changes. |
| `.github/workflows/hc-control-bot-advisory-comment.yml` | Posts or updates one advisory PR comment from trusted base context. | `pull_request_target`. | `contents: read`, `pull-requests: read`, `issues: write`. | Yes, comments. | High. | PARK_HIGH_RISK | Uses `pull_request_target` and issue write permission; any change is high-risk and human-review-required. |
| `.github/workflows/hc-control-bot-report.yml` | Produces advisory HC Control Bot report artifacts/summaries. | `pull_request`. | `contents: read`, `pull-requests: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Advisory control-plane evidence; keep while reviewing bot family as a group. |
| `.github/workflows/hc-repo-inventory.yml` | Generates repository inventory evidence. | `pull_request`, `workflow_dispatch`, `push` to `main`. | `contents: read`. | No. | Low. | KEEP | Read-only repository inventory evidence; no immediate cleanup recommended. |
| `.github/workflows/policy-evaluation.yml` | Produces advisory policy evaluation output. | `pull_request`. | `contents: read`, `pull-requests: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Policy evaluation is governance-related and should generally remain active. |
| `.github/workflows/pr-risk-labeler.yml` | Applies/removes manual-review and auto-merge labels based on changed paths. | `pull_request`. | `contents: read`, `pull-requests: write`, `issues: write`. | Yes, labels. | High. | PARK_HIGH_RISK | Label-changing workflow with write permissions; no cleanup action without explicit human review. |
| `.github/workflows/pr-scope-guard.yml` | Runs advisory PR scope boundary checker. | `pull_request`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Protected-scope guard; generally should remain active. |
| `.github/workflows/release-audit.yml` | Builds local report-only release audit evidence and uploads artifacts. | `pull_request`, `workflow_dispatch`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Release evidence workflow; generally should remain active. |
| `.github/workflows/safe-auto-merge.yml` | Reports auto-merge boundary and human merge requirement. | `pull_request`, `workflow_run` for Automation Gate. | `contents: read`, `pull-requests: read`. | No. | Medium. | REVIEW_DUPLICATION_CANDIDATE | Auto-merge-adjacent but report-only; review overlap with other auto-merge policy workflows. |
| `.github/workflows/scorecard.yml` | Runs OpenSSF Scorecard advisory scan. | `workflow_dispatch`, weekly `schedule`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Security posture evidence; generally should remain active. |
| `.github/workflows/terminology-autofix-suggest.yml` | Generates advisory terminology autofix report artifact when terminology guard fails. | `pull_request`. | `contents: read`. | No. | Low. | KEEP | Advisory-only report; no automatic code modification or write permission. |
| `.github/workflows/terminology.yml` | Runs terminology guard. | `pull_request`, `push` to `main`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Protects HC:// and HC-TRUST-LAYER terminology boundaries; generally should remain active. |
| `.github/workflows/validate.yml` | Runs validation, hash checks, generated evidence builds, and runtime/API tests. | Scoped `push` and `pull_request`. | `contents: read`. | No repository mutation; uploads artifacts. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Core validation and verification evidence; generally should remain active. |
| `.github/workflows/verification-package-schema.yml` | Validates verification package example/schema. | `pull_request`, `push` to `main`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Verification package schema validation; generally should remain active. |
| `.github/workflows/verify-archive.yml` | Verifies required repository archive structure on main pushes. | `push` to `main`. | `contents: read`. | No. | Medium. | KEEP_SECURITY_OR_GOVERNANCE | Archive/provenance continuity check; generally should remain active. |

## 4. Special review groups

### A. Auto-merge related

Reviewed workflows:

- `.github/workflows/enable-auto-merge.yml`
- `.github/workflows/safe-auto-merge.yml`
- `.github/workflows/docs-auto-merge.yml`

Findings:

- `enable-auto-merge.yml` is advisory/evaluation only in the inspected state. It reports that automatic merge enablement is disabled and does not enable, disable, or perform a merge.
- `safe-auto-merge.yml` is advisory/evaluation only in the inspected state. It reports the auto-merge boundary for pull request events and declares that it must never enable, disable, or perform a PR merge.
- `docs-auto-merge.yml` is advisory/evaluation only in the inspected state. It classifies PR scope and reports human review and human merge requirements.
- Cancelled concurrency runs should be ignored when a later successful run exists for the same workflow/ref or PR context, provided the later run covers the relevant head SHA and the latest run evidence is clear.
- Disablement or deletion of any auto-merge-related workflow is human-review-required because these workflows document and enforce the current boundary that automatic merge behavior is disabled or advisory only.

Recommendation: keep these workflows active for now, document overlap, and open a later targeted auto-merge policy review issue or docs/report PR if maintainers want to reduce naming overlap.

### B. Assistant / control bot related

Reviewed workflows:

- `.github/workflows/hc-assistant-command.yml`
- `.github/workflows/hc-control-bot-advisory-comment.yml`
- `.github/workflows/hc-control-bot-report.yml`

Findings:

- `issue_comment` workflows can be triggered by comments and should be treated as high-attention automation, especially when they have `issues: write` permission and can post or update comments.
- `pull_request_target` workflows execute in a sensitive context and require conservative handling even when they check out trusted base code and avoid running untrusted PR code.
- Repo-write/commenting risk exists for workflows that have `issues: write` because comments can affect reviewer perception and repository-facing audit trails.
- The current assistant/control bot boundary is advisory-only. These workflows must not approve, reject, close, merge, assign authority, request reviewers, or create autonomous governance authority.
- Changes need human review because these workflows are repository-facing control-plane automation and can affect public PR discussion even when they do not mutate source files.

Recommendation: park high-risk write/comment-capable workflows for a dedicated human-supervised security review, and keep read-only report workflows active until that review exists.

### C. Security / governance / release

The following workflow categories should generally remain active because they provide review evidence or boundary checks:

- governance preflight: `.github/workflows/governance-preflight.yml`;
- policy evaluation: `.github/workflows/policy-evaluation.yml`;
- scorecard: `.github/workflows/scorecard.yml`;
- release audit: `.github/workflows/release-audit.yml`;
- canonical artifact guard: `.github/workflows/canonical-artifacts.yml`;
- PR scope guard: `.github/workflows/pr-scope-guard.yml`;
- terminology guard: `.github/workflows/terminology.yml`;
- docs drift: `.github/workflows/docs-drift.yml`;
- validation and verification package schema: `.github/workflows/validate.yml` and `.github/workflows/verification-package-schema.yml`.

These workflows are part of the evidence-preserving operating layer. They provide CI/check evidence, not trust authority. They should generally remain active unless maintainers approve a targeted workflow review with clear replacement evidence and no loss of auditability.

### D. Mutating / write-capable workflows

Workflows with write-capable, comment-capable, label-capable, `pull_request_target`, `issue_comment`, auto-merge-adjacent, or similar control behavior:

| Workflow | Trigger or permission signal | Behavior | Flag |
| --- | --- | --- | --- |
| `.github/workflows/auto-hash.yml` | `contents: write` | Commits generated hash files. | HUMAN_REVIEW_REQUIRED |
| `.github/workflows/hc-assistant-command.yml` | `issue_comment`, `issues: write` | Posts or updates advisory command comments. | PARK_HIGH_RISK |
| `.github/workflows/hc-control-bot-advisory-comment.yml` | `pull_request_target`, `issues: write` | Posts or updates advisory PR comments. | PARK_HIGH_RISK |
| `.github/workflows/pr-risk-labeler.yml` | `pull-requests: write`, `issues: write` | Creates/applies/removes labels. | PARK_HIGH_RISK |
| `.github/workflows/enable-auto-merge.yml` | Auto-merge-adjacent name and label-triggered PR events. | Reports disabled auto-merge only. | HUMAN_REVIEW_REQUIRED |
| `.github/workflows/safe-auto-merge.yml` | Auto-merge-adjacent name and `workflow_run`. | Reports disabled auto-merge only. | HUMAN_REVIEW_REQUIRED |
| `.github/workflows/docs-auto-merge.yml` | Auto-merge-adjacent name. | Reports docs review policy only. | HUMAN_REVIEW_REQUIRED |

No immediate workflow deletion, disablement, rename, move, or edit is recommended for these workflows.

## 5. Safe cleanup recommendations

This report does not recommend immediate deletion.

Allowed next steps:

- keep security, governance, release, provenance, validation, and terminology workflows active;
- park write-capable or comment-capable workflows for human-supervised review;
- document overlap between auto-merge-related report-only workflows;
- require human review before any workflow disablement, deletion, rename, move, or permission change;
- create a later targeted workflow review issue for auto-merge policy naming and overlap;
- create a workflow map/index PR if maintainers want easier navigation.

## 6. Stop conditions

Stop and require human review if any future cleanup proposal reaches one of these conditions:

- workflow deletion is proposed;
- workflow disablement is proposed;
- a workflow has write permissions;
- a workflow uses `pull_request_target`;
- a workflow controls labels, comments, or auto-merge behavior;
- a workflow protects governance, security, release, or provenance boundaries;
- current open PR state is unknown;
- latest run evidence is unclear.

Under these conditions, the safe action is to stop, document the risk, and wait for maintainers. CI/checks are evidence, not trust authority, and human final authority remains required.

## 7. Suggested future PRs

Suggested future work should remain docs/report-only unless human review approves a targeted implementation:

1. Workflow map / index PR that documents each workflow, trigger, permissions, and boundary.
2. Auto-merge policy review PR that compares `enable-auto-merge.yml`, `safe-auto-merge.yml`, and `docs-auto-merge.yml` as report-only workflows and proposes human-approved naming or documentation changes.
3. Assistant/control bot workflow security review PR that documents `issue_comment`, `pull_request_target`, comment-write behavior, advisory-only boundaries, and required controls.

No immediate workflow deletion is proposed.
