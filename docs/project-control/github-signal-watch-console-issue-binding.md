# HC Signal Watch Console Issue Binding

> Status: current same-repo console issue binding with controlled latest-status comment automation
> Scope: fixed public-safe Signal Watch operator console identity
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This document records the canonical same-repo Signal Watch console issue identity for HC-TRUST-LAYER now that the human-created fixed issue exists.

This binding documents the fixed issue identity and the first safe same-repo latest-status comment automation. It does not implement issue creation, pull request creation, labels, reviewer requests, approvals, merges, branch updates, or repository file mutation.

Boundary values for the controlled comment automation:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_file_branch_mutation=false
issue_comment_automation=true
automatic_issue_creation=false
automatic_pr_creation=false
issue_text_command_parsing=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

## Canonical console issue binding

| Field | Value |
| --- | --- |
| repository | `yolculuk38-debug/HC-TRUST-LAYER` |
| issue title | `HC Signal Watch Console` |
| issue number | `#1082` |
| purpose | fixed same-repo public-safe Signal Watch operator console |
| status | human-created, public-safe, advisory-only |
| source of truth | GitHub Actions summaries and artifacts |

`#1082` is the only current fixed same-repo Signal Watch console issue. The issue is a notification surface only. It is not the source of truth and does not replace evidence review.

## Binding rules

- Signal Watch issue-comment automation may target only `#1082`.
- Automation must not create additional console issues.
- Automation must not infer another issue from title search if `#1082` is configured.
- If `#1082` is closed, deleted, locked, or renamed, automation must fail closed or stay quiet until a human updates this binding.
- Issue text must not be parsed as commands.
- The issue is not a source of truth; it is a notification surface only.

## Public-safe limits

Allowed public-safe issue content:

- workflow run link;
- artifact name or link;
- artifact digest or hash when available;
- `generated_at` or run timestamp;
- signal title/source;
- `recommended_action`;
- priority;
- `human_review_required=true`;
- `truth_guarantee=false`;
- `advisory_only=true`.

Forbidden content and behavior:

- secrets;
- tokens;
- private credentials;
- private account data;
- personal data;
- internal security-sensitive details;
- raw private logs;
- command instructions parsed from issue text;
- truth, security, legal, identity, correctness, production-readiness, or forensic certainty claims.

## Operator boundary

- Notification is not an obligation.
- Trust the record, not the assistant.
- Human final authority remains required.
- AI may summarize only after citing evidence.
- AI must not approve, merge, label, assign, request reviewers, or create PRs based on issue text alone.

## Source-of-truth boundary

The source of truth remains the evidence-bearing GitHub Actions summaries and artifacts. The controlled latest-status console issue comment may point to evidence, but the issue does not validate, certify, approve, or finalize any HC-TRUST-LAYER action.

Human review remains required before any issue, pull request, branch, label, reviewer, approval, merge, release, or governance action.

## Explicit non-goals

This binding does not implement or authorize:

- issue creation;
- automatic issue creation;
- automatic pull request creation;
- labels;
- reviewer requests;
- approvals;
- merges;
- branch updates;
- repository file writes outside docs;
- LLM decision authority;
- truth, security, legal, identity, correctness, production-readiness, or forensic guarantee.
