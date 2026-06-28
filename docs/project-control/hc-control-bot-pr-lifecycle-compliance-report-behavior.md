# HC Control Bot PR Lifecycle Compliance Report Behavior

## 1. Purpose

This document defines the expected report-only behavior for an HC Control Bot PR Lifecycle Compliance Report.

The report helps the human final reviewer evaluate whether a PR appears aligned with the HC PR lifecycle.

The report is:

- documentation-defined behavior
- advisory-only
- report-only
- public-safe
- evidence-producing
- not enforcement
- not automation authority
- not an approval mechanism
- not a merge mechanism
- not a label mechanism
- not a reviewer-request mechanism
- not an assignment mechanism
- not a new comment authority

The report can inform human review, but it cannot approve, reject, merge, label, assign, request reviewers, resolve threads, close issues, open issues, or mutate governance state.

## 2. HC boundary flags

Boundary flags:

- advisory_only=true
- report_only=true
- public_safe=true
- truth_guarantee=false
- human_review_required=true
- approval_authority=false
- merge_authority=false
- label_authority=false
- reviewer_request_authority=false
- assignment_authority=false
- issue_mutation_authority=false
- thread_resolution_authority=false
- governance_mutation_authority=false

AI accelerates work.
CI produces evidence.
Governance sets boundaries.
Audit records what happened.
Human maintainer makes the final decision.

A clean compliance report does not mean the PR is legally true, identity-final, forensically certain, certified, production-ready, safe to merge automatically, or guaranteed correct.

It only means the report did not detect a defined lifecycle concern within its report scope.

## 3. Relationship to existing HC review documents

This document adds report behavior guidance for HC Control Bot lifecycle compliance evidence. It should be read with:

- `docs/project-control/hc-agent-task-and-pr-lifecycle-standard.md`, which defines the HC PR lifecycle and the report-only role of HC Control Bot.
- `docs/project-control/human-final-reviewer-pr-checklist-boundary-review.md`, which defines the human final reviewer checklist and merge-readiness review boundary.
- `.github/pull_request_template.md`, which structures PR body evidence supplied by contributors.
- Existing HC Control Bot advisory/report-only behavior, which preserves non-authoritative reporting and human supervision.
- Existing HC Check Digest behavior, which summarizes check evidence for human evaluation.

The report should summarize lifecycle evidence for the human reviewer.
It should not replace the PR template.
It should not replace the human final reviewer checklist.
It should not replace direct diff review.
It should not replace current-head checks review.
It should not replace review thread inspection.
It should not replace post-merge audit.

## 4. Report scope

The PR lifecycle compliance report may inspect or summarize:

- PR number
- PR title
- PR state
- draft state
- base branch
- head branch
- current head SHA
- commit count
- changed file count
- additions/deletions
- PR body section presence
- changed file categories
- protected path signals
- generated/canonical artifact signals
- records/evidence signals
- workflow/CI/bot surface signals
- package/dependency surface signals
- runtime/API/CLI/public-output surface signals
- schema/validator/signing/federation/policy surface signals
- HC boundary language signals
- review-window marker/report presence
- Observed at
- Eligible after
- marker/report head SHA
- current head SHA match/mismatch
- check summary by current head SHA
- advisory/report-only check summary
- failed/missing/stale check signals
- cancelled duplicate run interpretation signal
- review comment presence
- active unresolved non-outdated thread signal
- outdated unresolved thread signal
- resolved thread signal
- fix-task evidence signal
- authority expansion signal
- follow-up classification signal
- post-merge audit evidence signal if the report is used after merge

The report must prefer current head SHA evidence over stale cached summaries.

## 5. Report non-scope

The report must not:

- decide truth
- decide legal validity
- decide identity finality
- decide forensic certainty
- decide certification
- decide production readiness
- approve a PR
- reject a PR
- merge a PR
- enable auto-merge
- label a PR
- remove a label
- assign a user
- remove an assignee
- request reviewers
- remove reviewers
- resolve review threads
- dismiss reviews
- close issues
- open issues
- update issue bodies
- update PR bodies
- create new comments beyond any already-governed existing advisory single-comment path
- expand comment authority
- alter workflows
- alter code
- alter checks
- alter branch protection
- alter repository settings
- make network calls beyond already-governed repository evidence access
- store private data
- expose secrets
- summarize private context into public output

## 6. Evidence model

The report evidence model should include these fields:

- `report_name`: Stable report name, such as `HC Control Bot PR Lifecycle Compliance Report`.
- `report_version`: Version of the report shape and semantics.
- `advisory_only`: Boolean boundary flag. Expected value: `true`.
- `report_only`: Boolean boundary flag. Expected value: `true`.
- `public_safe`: Boolean boundary flag. Expected value: `true`.
- `truth_guarantee`: Boolean boundary flag. Expected value: `false`.
- `human_review_required`: Boolean boundary flag. Expected value: `true`.
- `repository`: HC-TRUST-LAYER repository identifier used for report context.
- `pr_number`: PR number observed by the report.
- `pr_title`: PR title observed by the report.
- `pr_state`: PR state observed by the report.
- `draft`: Draft state observed by the report.
- `base_branch`: Base branch observed by the report.
- `head_branch`: Head branch observed by the report.
- `head_sha`: Current PR head SHA observed by the report.
- `observed_at`: Time when evidence was observed.
- `evidence_sources`: Public-safe evidence inputs used by the report.
- `lifecycle_summary`: Concise summary of lifecycle alignment signals.
- `findings`: Structured findings with severity, evidence, and scope.
- `warnings`: Potential lifecycle concerns that need human evaluation.
- `blockers_for_human_review`: Report language for possible blockers the human reviewer should evaluate. Do not use bot-blocking language.
- `not_evaluated`: Items not evaluated, including unavailable evidence or private-context exclusions.
- `followups`: Follow-up items that may be considered outside the current PR scope.
- `generated_by`: Report generator identity, limited to HC Control Bot report context.
- `generated_at`: Time when the report output was generated.

The bot reports possible blockers for a human reviewer to evaluate. It does not block merge by itself.

## 7. Finding severity

Report finding levels:

- `info`: Useful lifecycle context.
- `advisory`: Non-blocking signal that may help review.
- `warning`: Potential lifecycle concern that should be evaluated before merge readiness.
- `hold_for_human_review`: A report-detected condition that should normally prevent merge-ready status until a human reviewer evaluates and resolves or explicitly accepts the risk.

No severity level grants bot approval or bot rejection authority.

## 8. Lifecycle checks to report

### PR identity group

Report:

- PR number present
- title present
- open/closed state
- draft state
- base branch
- head branch
- head SHA
- commit count
- changed file count

### PR body group

Report:

- motivation/summary presence
- description presence
- testing/checks presence
- scope presence
- out-of-scope presence
- HC boundary language presence
- authority expansion denial presence
- human final review language presence
- follow-up classification presence
- mismatch risk between PR body and changed files

### Changed file group

Report:

- docs-only
- code touched
- tests touched
- workflows touched
- scripts touched
- templates touched
- schema touched
- validators touched
- records/evidence touched
- generated artifacts touched
- canonical/trust-kernel artifacts touched
- policy touched
- federation touched
- signing/signatures touched
- demo fixtures touched
- package/dependency files touched

### Protected path group

Report:

- protected path touched
- protected path explicitly scoped
- protected path not mentioned in PR body
- authority-adjacent path touched
- root canonical/trust-kernel artifact touched
- package/dependency surface touched

Canonical/trust-kernel root artifacts include:

- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`

This list is not exhaustive if repository inventory or governance documents define additional canonical roots.

### Review-window group

Report:

- marker/report found
- Observed at
- Eligible after
- marker/report head SHA
- current PR head SHA
- head SHA match
- current time after Eligible after
- newer relevant commit/update detected
- missing/stale/mismatched marker signal
- review window status

PR created_at, updated_at, and latest commit time are supporting context only when marker/report exists.

### Current-head checks group

Report:

- checks collected for current head SHA
- success checks
- failed checks
- missing expected checks if detectable
- stale checks if detectable
- advisory/report-only checks
- validation checks
- enforcement checks when known
- cancelled duplicate runs
- later success run for same head if present

Cancelled duplicate runs are not success by themselves.
They may be acceptable only when a later run on the same head succeeded.

### Review comments and threads group

Report:

- review submissions present
- review comments present
- active unresolved non-outdated threads
- outdated unresolved threads
- resolved threads
- comments reviewed against current head if detectable
- fix-related new commit signal if detectable

Active unresolved non-outdated threads should normally be reported as `hold_for_human_review`.

Outdated unresolved threads should be reported as `warning` unless current diff evidence indicates the issue was addressed.

### Authority boundary group

Report possible signs of:

- new or expanded comment authority
- approval authority
- merge authority
- label authority
- reviewer-request authority
- assignment authority
- issue mutation authority
- thread resolution authority
- governance mutation authority
- auto-merge language
- truth guarantee language
- legal truth language
- identity finality language
- forensic certainty language
- certification language
- production readiness guarantee language

### Post-merge audit group

When the report is used after merge, report:

- PR closed
- merged=true
- merge commit SHA
- merged_at
- changed file count
- additions/deletions
- follow-up classification
- project-control update need
- no state-sync loop warning for small PRs

## 9. Suggested report output shape

The following generic shape is illustrative documentation, not implementation:

```text
{
  report_name: "HC Control Bot PR Lifecycle Compliance Report",
  report_version: "0.1",
  advisory_only: true,
  report_only: true,
  public_safe: true,
  truth_guarantee: false,
  human_review_required: true,
  pr: {
    number: "example-pr-number",
    title: "example-pr-title",
    state: "open",
    draft: false,
    base_branch: "example-base",
    head_branch: "example-head",
    head_sha: "example-current-head-sha"
  },
  evidence: {
    observed_at: "example-observed-time",
    evidence_sources: ["example-public-safe-source"],
    review_window: {
      marker_found: true,
      observed_at: "example-marker-observed-time",
      eligible_after: "example-eligible-time",
      marker_head_sha: "example-current-head-sha",
      current_head_sha: "example-current-head-sha",
      head_sha_match: true
    },
    current_head_checks: {
      head_sha: "example-current-head-sha",
      success: ["example-success-check"],
      failed: [],
      missing: [],
      stale: [],
      advisory_report_only: ["example-advisory-check"]
    }
  },
  lifecycle_summary: "example lifecycle summary for human review",
  findings: [
    {
      severity: "info",
      group: "PR identity",
      message: "example finding"
    }
  ],
  warnings: [],
  blockers_for_human_review: [],
  not_evaluated: [],
  followups: []
}
```

## 10. Human-readable summary behavior

A concise human-readable report summary should use these sections:

- HC Control Bot PR Lifecycle Compliance Report
- Boundary
- PR identity
- Scope signals
- Protected path signals
- Review-window signal
- Current-head checks signal
- Review comments/thread signal
- Authority boundary signal
- Human review note
- Follow-ups

The summary must be written as evidence, not command.
It must not tell the bot to merge.
It must not tell the bot to approve.
It must not tell the bot to resolve threads.
It must not tell the bot to label.
It must not pretend to be the human final reviewer.

## 11. Existing advisory single-comment path

This document preserves the existing HC Control Bot advisory single-comment path.

This document does not remove or forbid the existing governed advisory single-comment path.
This document does not create a new comment mode.
This document does not expand comment authority.
Any future change to comment behavior requires a separate governed PR.

## 12. Report timing

The report may be generated when separately governed report generation exists for:

- PR opened
- PR synchronized / new commit
- PR marked ready for review
- manual workflow run if already governed
- post-merge verification if separately governed

Every report must identify the head SHA it observed.
A report must be considered stale after a new PR head commit.
A report must not be reused as current evidence after the head SHA changes.

## 13. Staleness rules

A report is stale as current merge-readiness evidence when any of these conditions occur after report generation:

- PR head SHA changed
- PR state changed
- draft state changed
- changed files changed
- relevant checks changed
- review-window marker/report changed
- new review comment added
- thread state changed
- merge state changed

A stale report is still audit evidence, but not current merge-readiness evidence.

## 14. Public safety rules

The report must be public-safe.

It must not include:

- secrets
- tokens
- private keys
- private credentials
- private email contents
- private chat contents
- private prompt contents
- private personal data
- hidden chain-of-thought
- unredacted environment variables
- sensitive system configuration
- non-public repository data

If a signal requires private context, report:

```text
not_evaluated: private_context_required
```

## 15. Failure modes

When evidence is missing, the report should fail safe into human review:

- Missing PR metadata: `hold_for_human_review`.
- Missing changed-file data: `hold_for_human_review`.
- Missing current-head checks: `warning` or `hold_for_human_review` depending on expected check availability.
- Missing review-window marker/report where expected: `hold_for_human_review`.
- Missing review-thread data: `warning`.
- Missing PR body: `warning` or `hold_for_human_review` depending on change surface.
- Tool/API unavailable: `not_evaluated` entry plus human review required.

The report must fail safe into human review, not automatic approval.

## 16. Acceptance criteria for future implementation

Any future implementation PR must:

- remain report-only unless separately governed
- preserve advisory_only=true
- preserve report_only=true
- preserve public_safe=true
- preserve truth_guarantee=false
- preserve human_review_required=true
- emit current head SHA
- avoid stale evidence reuse
- preserve existing advisory single-comment path boundaries
- avoid new or expanded comment authority unless separately governed
- avoid label/reviewer/assignment/approval/merge/thread-resolution authority
- avoid private data exposure
- distinguish advisory/report-only/validation/enforcement checks where known
- report cancelled duplicate runs correctly
- report review-window marker/head SHA matching correctly
- report canonical/trust-kernel root artifacts correctly
- include tests for docs and report examples if implementation adds examples or fixtures
- include audit-friendly output shape

## 17. Follow-up plan

Follow-ups:

- 5-2e: Optionally implement report-only HC Bot PR lifecycle compliance check.
- 5-3: Protected path contributor guide review.
- PR Trust Receipt: Parked future product idea after lifecycle compliance report is documented and report-only implementation is stable.

These follow-ups are not part of this PR.
