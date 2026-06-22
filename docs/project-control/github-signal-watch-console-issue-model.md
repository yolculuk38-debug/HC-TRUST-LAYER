# HC Signal Watch Console Issue Model

> Status: practical same-repo public-safe issue visibility model
> Scope: documentation only; no automation implemented in this PR
> Authority: advisory only
> Production readiness: not claimed

> Direction note: the practical default for now is the same-repo public-safe console issue mode described in [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md). HC-TRUST-LAYER remains the single operational repository; no second private operations repository is required for the current model.

## Purpose

The **HC Signal Watch Console** is a fixed, human-created GitHub issue intended to provide mobile-friendly, operator-facing advisory visibility for HC Signal Watch reports in the same HC-TRUST-LAYER repository.

It exists so operators do not need to remember specific GitHub Actions pages or manually hunt for artifact downloads before reviewing recent Signal Watch status. The console issue is a surfaced summary view only. It keeps the audit trail visible while separating evidence artifacts from convenience summaries.

Boundary values for this documentation-only PR:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_file_branch_mutation=false
issue_comment_automation=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

`issue_comment_automation=false` applies to this PR because this document defines the future model only. It does not implement workflow, script, issue comment, or repository automation.

A future workflow that posts or updates a comment in the fixed console issue would have `issue_comment_automation=true` and would mutate GitHub issue state. That future issue-comment update must not be described as `repository_mutation=false`. The narrower boundary is that future comment automation may update only the human-created fixed console issue, while repository files and branches remain unchanged: `repository_file_branch_mutation=false`.

## Same-repo practical default

The same-repo public-safe console issue mode is the practical default for now. Signal Watch evidence remains in Actions summaries and artifacts. The fixed issue is only an advisory notification surface and does not replace evidence review.

No `HC-TRUST-OPS` repository or second private repository is required for the current model. The private inbox path remains optional, future, and parked unless public-safe same-repo issue mode becomes insufficient.

## Fixed issue

The suggested console issue name is fixed:

```text
HC Signal Watch Console
```

The alternative fixed issue title is `HC Operator Notification Queue`.

The fixed console issue must be created by a human before any future workflow may update it. Future automation, if separately proposed and reviewed, may only update that human-created fixed issue, either through one latest-status comment or one controlled thread. This model does not authorize automatic creation of additional issues.

## Source of truth

The source of truth remains:

1. the GitHub Actions run;
2. the JSON artifact;
3. the Markdown artifact;
4. the Actions job summary.

A future issue comment is only a surfaced summary. It is not the canonical artifact, does not replace artifact review, and does not create truth, security, legal, identity, correctness, production-readiness, or forensic certainty guarantees.

Human final authority remains required before any repository action.

## Intended future flow

The intended future visibility flow is:

```text
GitHub Changelog RSS / manual signal
→ Signal Watch dry-run workflow
→ JSON + Markdown artifacts
→ Actions job summary
→ HC Signal Watch Console issue advisory comment
→ human final decision
```

The issue comment is a convenience view for operators. It should point back to the evidence-bearing workflow run and artifacts so review remains audit-friendly.

## Future comment behavior

If future issue-comment automation is proposed and reviewed separately, the expected behavior is:

- post or update one latest-status comment in the fixed console issue;
- avoid spammy per-run comments by default;
- include a link to the GitHub Actions run;
- include an artifact reference or digest when available;
- include `fetch_status`;
- include `safe_failure`;
- include `signal_count`;
- include `recommended_action`;
- include `human_review_required=true`;
- include `truth_guarantee=false`;
- include `issue_comment_automation=true` for that future workflow;
- include that the issue comment update is a GitHub issue state mutation;
- include `repository_file_branch_mutation=false`.

The latest-status comment may summarize recent advisory status, but reviewers must use the workflow run and artifacts when validating details.

## Allowed suggested actions

A future issue comment may suggest only bounded, human-reviewed next steps:

- `no-action`;
- `manual review`;
- `prepare issue suggestion`;
- `prepare PR suggestion`;
- `watch future GitHub changes`.

These suggestions are advisory triage language. They do not authorize repository file or branch mutation, approval, merge, release, or governance decisions.

## Forbidden behavior

This model forbids:

- automatic issue creation except updating the one human-created fixed console issue in a future separately reviewed implementation;
- automatic PR creation;
- labels;
- reviewer requests;
- approvals;
- merges;
- branch updates;
- repository file writes;
- LLM decisions;
- truth, security, legal, identity, correctness, production-readiness, or forensic certainty guarantees.

The console issue must not be used to create autonomous governance authority for bots, agents, or LLMs.

## Why this exists

The console issue model exists to:

- provide a mobile-friendly operator view;
- avoid manual artifact hunting;
- keep the audit trail visible;
- separate evidence artifacts from surfaced summaries.

This design keeps Signal Watch advisory, public-safe, and human-supervised while improving operator visibility for future HC:// Control Panel direction.
