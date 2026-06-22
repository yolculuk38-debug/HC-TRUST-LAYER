# HC Signal Watch Operator Notification Queue

> Status: future queue model; documentation only
> Scope: same-repo practical notification model with optional future private inbox
> Authority: advisory only
> Production readiness: not claimed

## Purpose

The HC Operator Notification Queue is an advisory model for important HC Signal Watch notifications. The current practical path is the same-repo public-safe console issue mode documented in [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md).

Private inbox setup remains optional, future, and parked. Before any private inbox implementation, maintainers must satisfy the [HC Signal Watch Private Inbox Setup Contract](github-signal-watch-private-inbox-setup.md).

The queue is intended to help a maintainer/operator notice meaningful Signal Watch items without treating notifications as mandatory work. It is a notification model only; it is not implemented by this PR.

Boundary values for this documentation-only model:

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

`public_safe=true` describes this documentation. It does not make future queue contents public-safe by default.

The queue is not:

- a public issue feed;
- a mandatory work list;
- an automation command surface;
- the source of truth.

A notification is not an obligation. Human final authority remains required before any issue, pull request, branch, label, reviewer, approval, merge, or governance action.

## Core flow

The future queue model follows this advisory flow:

```text
Signal Watch detects a meaningful signal
→ evidence is produced in Actions run/artifacts
→ queue receives an advisory notification only if attention is needed
→ operator reviews evidence
→ operator may dismiss, archive, ignore, watch, escalate, create issue, or create PR
→ human final decision remains required
```

Actions runs, summaries, and artifacts remain evidence surfaces. The queue only points an operator toward evidence when attention may be needed.

## Queue item evidence requirements

Each future queue item should include the following fields when available:

- workflow run link;
- artifact name or link when available;
- artifact digest or hash when available;
- `generated_at` or workflow run timestamp;
- signal title/source;
- `recommended_action`;
- priority;
- `human_review_required=true`;
- `truth_guarantee=false`;
- `advisory_only=true`.

A queue item must not replace the underlying Actions run, generated artifact, artifact digest or hash, source signal, or HC:// review record.

## Priority levels

| Priority | Meaning |
| --- | --- |
| P0 | Urgent safety/governance/security check required. |
| P1 | Important repo/operator review required. |
| P2 | Useful opportunity or moderate operational signal. |
| P3 | Informational/watch only. |
| no-action | Recorded but no operator action required. |

Priority is an advisory triage hint. It is not a truth, security, legal, identity, correctness, production-readiness, or forensic guarantee.

## Operator outcomes

A human operator may mark or treat a queue item as:

- dismissed;
- archived;
- ignored;
- watching;
- issue-needed;
- PR-needed;
- follow-up-later;
- duplicate.

These outcomes are operator workflow states only. They do not approve, reject, merge, certify, or finalize any HC-TRUST-LAYER action.

## Duplicate and cleanup behavior

Repeated signals should update or reference the existing queue item rather than spamming new notifications.

No-action and informational items may be archived or deleted later, but retention and cleanup policy must be separately reviewed before implementation.

Automatic deletion must not remove evidence artifacts or canonical records. Cleanup of notification items must remain separate from evidence preservation, artifact retention, and canonical HC:// record boundaries.

## Same-repo practical path and optional private inbox

The current practical path is a same-repo, public-safe, evidence-anchored fixed issue in HC-TRUST-LAYER when a surfaced notification is needed. No `HC-TRUST-OPS` repository or second private repository is required for the current model.

GitHub Actions summaries and artifacts remain the current evidence surfaces. They are not replaced by the queue or by any issue comment.

Private/admin-only inbox setup remains optional and future. It may be reconsidered later only if public-safe same-repo issue mode becomes insufficient.

## AI assistant access boundary

Trust the record, not the assistant.

AI assistants may read queue items only through authorized access. AI summaries are advisory only and must cite the underlying evidence before recommending issue, pull request, or merge action.

AI assistants must not:

- treat notifications as mandatory work;
- treat the queue as the source of truth;
- recommend issue, PR, or merge action without citing the evidence;
- change queue status unless explicitly authorized in a future separate governance-reviewed implementation;
- claim approval, rejection, merge, certification, truth, legal, identity, correctness, production-readiness, or forensic authority.

The source of truth remains the evidence: the Actions run, generated Signal Watch artifacts, artifact digest or hash when available, source signal, and any relevant HC:// review record.

## Future weekly schedule relationship

Weekly Signal Watch scheduling may be considered only after notification behavior is separately reviewed.

Weekly checks should avoid noise. No-action weekly runs may stay quiet. Only meaningful P0, P1, or P2 items should create operator-facing notification candidates.

Any schedule remains a separate implementation decision and must preserve human-supervised validation, public-safe evidence surfaces, and advisory-only interpretation.

## Explicit non-goals

This PR does not implement or authorize:

- workflow implementation;
- schedule implementation;
- private repository creation;
- issue comment automation;
- issue creation;
- public issue comments;
- automatic issue creation;
- automatic PR creation;
- labels;
- reviewer requests;
- approvals;
- merges;
- branch updates;
- repository file writes outside docs;
- LLM decision authority;
- external notification provider;
- truth, security, legal, identity, correctness, production-readiness, or forensic guarantee.

## Implementation review requirement

Any future implementation must be reviewed separately before it creates, updates, archives, deletes, comments on, schedules, labels, requests review for, approves, merges, or otherwise mutates any repository, issue, pull request, queue item, branch, or external notification service.
