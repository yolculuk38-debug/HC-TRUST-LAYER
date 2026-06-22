# HC Signal Watch Admin Notification Boundary

> Status: preferred next-direction boundary
> Scope: documentation only; no workflow, issue-comment, schedule, or notification automation implemented in this PR
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This document defines the preferred next direction for HC Signal Watch visibility: admin/operator-facing notification, not routine publication into public repository issues.

Signal Watch should help maintainers notice GitHub operational signals without making internal operational summaries the default public issue content. The GitHub Actions run summary and artifacts remain the evidence source. Human final authority remains required before any repository action.

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

`public_safe=true` describes this document itself. It does not mean routine Signal Watch operational summaries should be published to public issues by default.

## Preferred direction

The preferred direction is:

- Signal Watch should not publish routine status into public issues by default.
- Signal Watch summaries should be admin/operator-facing.
- GitHub Actions run summaries and artifacts remain the evidence source.
- Public issues must not be used as the default notification channel for internal operational signals.
- Human final authority remains required for interpretation and follow-up.

This direction preserves operator visibility while avoiding unnecessary public exposure of routine internal operational triage.

## Google Play style analogy

The intended operator experience is similar to a store-console background check pattern:

1. A background check runs.
2. An operator receives a concise notification only when attention is needed.
3. The operator should not need to hunt artifacts manually for every routine run.
4. Normal no-action runs can stay quiet.
5. Evidence remains available in the Actions run summary and artifacts for review.

This analogy is only a UX reference. It does not claim production readiness, external platform equivalence, legal status, security certainty, or correctness guarantees.

## Allowed future notification channels

Future notification design may consider these channels, subject to separate review where needed:

- GitHub Actions job summary;
- GitHub Actions artifacts;
- GitHub notification from workflow failure or manual run;
- private/admin-only operations repository issue, if created later;
- future GitHub App or external notification service, only after separate governance review.

The first two channels are already aligned with the current evidence-first model. Any private issue, GitHub App, or external service path requires separate design and governance review before implementation.

## Discouraged default channel

Public repository issue comments for routine Signal Watch status are discouraged and default-forbidden for admin-only operational updates.

A public `HC Signal Watch Console` issue may remain documented as a transparency option, but it is not the preferred default implementation for admin-only Signal Watch updates. Public issue publication must not become the default notification path for internal operational signals.

## Future implementation stages

### Stage 1: Current evidence view

- Actions summary only.
- Artifacts only.
- Manual `workflow_dispatch`.

### Stage 2: Admin-only notification design

- Define private/admin-only notification behavior.
- Keep routine status out of public issue comments.
- Preserve Actions summaries and artifacts as evidence.

### Stage 3: Optional private notification implementation

- Optional private operations issue or GitHub App notification.
- Separate PR required.
- Separate governance review required.

### Stage 4: Schedule review

- Schedule may be considered only after notification visibility and permissions are reviewed.
- Scheduled execution must preserve human-supervised validation and evidence review.

## Security boundaries

This boundary forbids implementation in this PR and sets limits for future designs:

- no public issue-comment automation by default;
- no automatic issue creation;
- no automatic PR creation;
- no labels;
- no reviewer requests;
- no approvals;
- no merges;
- no branch updates;
- no repository file writes;
- no LLM decision;
- no truth, security, legal, identity, correctness, production-readiness, or forensic certainty guarantee;
- no external notification provider unless separately reviewed;
- no secrets exposed to public logs or public issues.

## Relationship to the public console issue model

The fixed public `HC Signal Watch Console` issue model remains a possible transparency option. It should be treated as a separately reviewed public visibility model, not as the preferred default for admin-only operational updates.

For current operations, use the Actions summary and artifacts as the review surface. Future private/admin-only notification work should be scoped separately and remain advisory, public-safe in documentation, and human-supervised.
