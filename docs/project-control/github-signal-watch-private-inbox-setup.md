# HC Signal Watch Private Inbox Setup Contract

> Status: future setup contract; documentation only
> Scope: private/admin-only Signal Watch operator inbox setup requirements
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This document defines the human setup requirements for a future private/admin-only Signal Watch operator inbox.

This document does not:

- implement notification automation;
- create a private repository;
- create issues;
- add schedules;
- add workflow changes.

Boundary values for this documentation-only setup contract:

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

`public_safe=true` describes this documentation. It does not mean future private inbox contents are public-safe by default.

## Recommended private channel

A private/admin-only operations repository is the preferred future notification target for private Signal Watch operator notifications.

Suggested repository name examples:

- `HC-TRUST-OPS`
- `HC-OPERATOR-INBOX`
- `HC-SIGNAL-INBOX`

The exact repository name must be chosen by the maintainer. The private repository must not be assumed to exist.

## Required human-created issue

The maintainer may create one fixed private issue for future inbox updates, such as:

- `HC Operator Notification Queue`
- `HC Signal Watch Inbox`

The issue must be created by a human before any future automation can update it.

Future automation must not create unlimited issues. Future automation should update one marked latest-status comment or one controlled thread only after separate implementation review.

## Future required configuration

Any future implementation must require explicit maintainer-provided configuration before publishing private operator notifications:

- private inbox repository full name;
- private inbox issue number;
- maintainer GitHub username for optional mention;
- optional notification mode:
  - `no-notify`;
  - `mention-maintainer`;
  - `comment-only`;
- optional priority threshold:
  - `P0 only`;
  - `P0/P1`;
  - `P0/P1/P2`;
- optional duplicate handling mode:
  - `update-existing`;
  - `append-latest`;
  - `manual-only`.

The private inbox repository and issue number must be treated as configuration, not as repository facts.

## Security and permissions

Future implementation must use least privilege.

Future implementation must not use:

- `contents: write` on HC-TRUST-LAYER;
- `pull-requests: write`;
- labels;
- reviewers;
- approvals;
- merges;
- branch writes.

If cross-repo commenting is used later, the token and permission model must be separately reviewed before implementation.

Secrets must not be printed to logs. Issue content must never be parsed as commands. Queue items must not control workflow behavior.

## Evidence lock

Every future private inbox notification must include:

- workflow run link;
- artifact name or link when available;
- artifact digest or hash when available;
- `generated_at` or run timestamp;
- signal title/source;
- `recommended_action`;
- priority;
- `human_review_required=true`;
- `truth_guarantee=false`;
- `advisory_only=true`.

A private inbox notification must point to evidence; it must not replace the evidence.

## Notification behavior

A notification is an early-warning review prompt, not mandatory work.

P0, P1, and P2 signals may create notification candidates. P3 and no-action signals should normally stay quiet unless manually requested.

An operator may dismiss, archive, ignore, watch, escalate, create an issue, or create a pull request after reviewing the evidence and repository context.

AI assistants must not treat queue notifications as mandatory work. Trust the record, not the assistant.

## Cleanup and retention

Notification cleanup may delete or archive queue comments or queue items only after separate review.

Cleanup must not delete:

- GitHub Actions artifacts;
- canonical records;
- evidence logs;
- HC:// records.

Auto-delete behavior must be separately reviewed before implementation.

## Explicit non-goals

This PR does not implement or authorize:

- workflow implementation;
- schedule implementation;
- private repository creation;
- issue creation;
- issue-comment automation;
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

Any future implementation must be reviewed separately before it creates, updates, archives, deletes, comments on, schedules, labels, requests review for, approves, merges, writes branches, writes repository files, or otherwise mutates any repository, issue, pull request, queue item, branch, workflow, or external notification service.

Human final authority remains required. The private inbox is an advisory notification surface only and not a governance authority, correctness guarantee, identity guarantee, legal guarantee, security guarantee, production-readiness claim, or forensic certainty claim.
