# HC Signal Watch Admin Notification Boundary

> Status: notification boundary
> Scope: documentation only; no workflow, issue-comment, schedule, or notification automation implemented in this PR
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This document defines the HC Signal Watch notification boundary for admin/operator-facing review prompts and public-safe same-repo issue visibility.

Signal Watch should help maintainers notice GitHub operational signals without exposing secrets, private data, or internal security-sensitive details. In this public repository, GitHub Actions job summaries and artifacts are public-safe evidence surfaces. A fixed same-repo public-safe console issue may be used when evidence-anchored and limited to public-safe content. Human final authority remains required before any repository action.

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

## Practical direction

The practical direction is:

- Signal Watch evidence remains in Actions summaries and artifacts.
- Same-repo public-safe console issue mode is the practical default when a surfaced issue notification is needed.
- The same-repo model is documented in [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md).
- No second private repository is required for the current model.
- Signal Watch notifications should avoid secrets, private data, and internal security-sensitive details.
- Human final authority remains required for interpretation and follow-up.

This direction preserves operator visibility while avoiding unnecessary public exposure of internal operational details.

## Google Play style analogy

The intended operator experience is similar to a store-console background check pattern:

1. A background check runs.
2. An operator receives a concise notification only when attention is needed.
3. The operator should not need to hunt artifacts manually for every routine run.
4. Normal no-action runs can stay quiet.
5. Evidence remains available in the public-safe Actions run summary and artifacts for review.

This analogy is only a UX reference. It does not claim production readiness, external platform equivalence, legal status, security certainty, or correctness guarantees.

## Evidence surfaces and allowed future notification channels

The current evidence surfaces are:

- GitHub Actions job summary;
- GitHub Actions artifacts.

In this public repository, those evidence surfaces are public-safe review surfaces. They are not private/admin-only notification channels and must not be described as private admin notification. They may reduce artifact hunting for operators, but they do not provide private maintainer notification.

Future notification design may consider these channels, subject to separate review:

- GitHub notification from workflow failure or manual run, when visibility is limited to maintainers by GitHub permissions;
- same-repo public-safe console issue, when evidence-anchored and limited to public-safe content;
- optional private/admin-only operations repository issue, if created later;
- future GitHub App or external notification service, only after separate governance review.

Any private issue, GitHub App, or external service path requires separate design and governance review before implementation.

Private inbox implementation remains optional, future, and parked. If reconsidered later, it requires the [HC Signal Watch Private Inbox Setup Contract](github-signal-watch-private-inbox-setup.md) to be completed first.

## Public-safe same-repo issue boundary

Public repository issue comments are allowed only when they are evidence-anchored, public-safe, advisory, and limited to the fixed same-repo console issue model. They must not contain secrets, tokens, credentials, private account data, personal data, raw private logs, or internal security-sensitive details.

The fixed public `HC Signal Watch Console` issue is the practical default for same-repo surfaced notifications when needed. It must not become a command surface, source of truth, or mandatory work list.

## Future implementation stages

### Stage 1: Current evidence view

- Actions summary only as a public-safe evidence surface.
- Artifacts only as public-safe evidence surfaces.
- Manual `workflow_dispatch`.
- No private/admin-only notification channel yet.

### Stage 2: Same-repo public-safe console design

- Use [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md) as the practical default.
- Do not classify Actions summaries or artifacts as private/admin-only notification channels.
- Keep issue content public-safe, evidence-anchored, and advisory.
- Preserve Actions summaries and artifacts as public-safe evidence surfaces.

### Stage 3: Optional private notification implementation

- Optional private operations issue or GitHub App notification.
- Separate PR required.
- Separate governance review required.

### Stage 4: Schedule review

- Schedule may be considered only after notification visibility and permissions are reviewed.
- Scheduled execution must preserve human-supervised validation and evidence review.

## AI assistant interpretation boundary

Trust the record, not the assistant. AI assistant summaries are advisory only and must not become the source of truth for Signal Watch interpretation.

The source of truth remains:

- the GitHub Actions run;
- the generated Signal Watch artifacts;
- the artifact digest or hash when available;
- the original Signal Watch record.

Any future admin-only notification must be evidence-anchored and include these references when available:

- workflow run link;
- artifact name or link;
- artifact digest or hash;
- `generated_at` value or workflow run timestamp;
- `recommended_action`;
- `human_review_required=true`;
- `truth_guarantee=false`.

An AI assistant must not present a notification as mandatory work without citing the underlying Signal Watch evidence. A Signal-derived issue or pull request must include the Signal evidence reference and explain why the action is needed. Merge and review decisions must not rely on an AI narrative alone.

Operators may dismiss, archive, ignore, watch, or escalate notifications. A notification is not an obligation. Public issue comments are allowed only under the same-repo public-safe console boundary and must remain evidence-anchored and advisory.

This PR remains documentation-only and does not add workflows, scripts, issue-comment automation, schedules, labels, reviewer requests, approvals, merges, repository writes, external services, or LLM decisions.

## Security boundaries

This boundary forbids implementation in this PR and sets limits for future designs:

- no issue-comment automation in this PR;
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
- no secrets exposed to public logs, public artifacts, public summaries, or public issues.

## Relationship to the public console issue model

The fixed public `HC Signal Watch Console` issue model is the practical same-repo default for surfaced public-safe notifications when needed. See [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md).

For current operations, use the Actions summary and artifacts as public-safe evidence review surfaces. Future private/admin-only notification work is optional, parked, and should be reconsidered only if the same-repo public-safe issue mode becomes insufficient.
