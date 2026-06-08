# HC Control Bot Advisory Comment Boundary

This document defines the safety boundary for any future HC Control Bot advisory PR comment mode.

It is documentation only. It does not enable comments, workflows, labels, approvals, request-changes behavior, merge behavior, LLM behavior, or autonomous authority.

## Purpose

HC Control Bot v0.1 currently produces report-only artifacts and logs. If the project later adds a single advisory PR comment mode, that mode must remain non-authoritative, deterministic, human-supervised, and bounded by the authority policy.

This document records the boundary before any implementation is considered.

## Current status

Current HC Control Bot baseline:

- advisory-only
- non-LLM
- deterministic
- path-metadata based
- report-only
- artifact/log based
- human-supervised

Current behavior does not include PR comments.

## Operating model

Any future advisory comment mode must preserve the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

The bot may help orient maintainers. It must not decide.

## Mandatory boundaries

A future advisory comment mode must not:

- approve pull requests
- request changes
- reject pull requests
- merge pull requests
- close pull requests
- reopen pull requests
- apply labels
- remove labels
- assign reviewers
- dismiss reviews
- resolve review conversations
- certify production readiness
- certify security
- certify objective truth
- certify forensic certainty
- override CI
- override governance
- override CODEOWNERS
- override branch protection
- override human maintainers

## Comment frequency rule

If advisory PR comments are ever enabled, the bot should post at most one visible advisory note per pull request.

Preferred behavior:

1. create one advisory note when needed;
2. update the existing bot note when possible;
3. avoid repeated noisy comments;
4. skip or minimize output for low-risk draft work;
5. keep all findings aggregated in one concise place.

Repeated comments can create authority confusion and review fatigue.

## Allowed comment content

A future advisory comment may summarize deterministic scanner output, such as:

- changed file surfaces observed
- protected paths touched
- governance-adjacent paths touched
- generated artifacts observed
- human review reminder
- warnings from path metadata
- evidence source used by the report

The comment should be short, factual, and traceable to the report artifact.

## Disallowed comment content

A future advisory comment must not include wording that implies:

- approval
- rejection
- merge readiness
- request-changes authority
- final correctness
- objective truth
- security certification
- production readiness
- legal validity
- forensic certainty
- maintainer replacement

Avoid phrases like:

```text
This PR is safe to merge.
This PR is approved.
This PR is rejected.
This change is verified as true.
This output certifies correctness.
```

## Required advisory footer

Any future advisory comment should include a clear boundary notice similar to:

```text
This is an advisory HC Control Bot observation.
It is not approval, rejection, merge authority, or a truth guarantee.
Human maintainers retain final authority.
```

## Evidence source rule

A future advisory comment must disclose its evidence source.

For v0.1-style behavior, the correct evidence source is:

```text
Changed file metadata only.
```

The comment must not imply that the bot reviewed file content, PR intent, security correctness, runtime behavior, or truthfulness unless a later reviewed implementation explicitly supports that scope.

## Trusted baseline rule

Governance, policy, and bot behavior configuration must be read from trusted repository state, not from untrusted PR branch content.

A future implementation must preserve the rule that PR title, PR body, comments, commit messages, and changed file content are untrusted input.

## Downstream automation rule

No workflow or automation should treat HC Control Bot comment text as an executable command, merge signal, approval signal, label signal, or governance decision.

Bot comments are human-readable advisory notes only.

## High-risk wording rule

If a future comment mentions high risk, it must describe high risk as a review-priority signal, not as an automatic failure.

Acceptable:

```text
High-risk surfaces were observed. Human review should inspect these paths carefully.
```

Unsafe:

```text
High risk detected. This PR must be rejected.
```

## Generated artifact rule

If generated artifacts are observed, the comment may mention them as non-canonical support artifacts.

It must not imply that generated artifacts replace canonical records, schemas, validators, governance policy, signatures, or source-of-truth documentation.

## Failure and disablement rule

If the bot comments with authority-like wording, posts repeated noisy comments, comments based on untrusted instruction text, or is interpreted as a command source by another workflow, maintainers should disable comment mode and review the incident before re-enabling it.

## Implementation readiness checklist

Before enabling advisory comments, maintainers should confirm:

- authority policy is on `main`
- report-only workflow is stable
- report interpretation guide exists
- single-comment behavior is implemented or otherwise guaranteed
- no approval, request-changes, merge, close, or label permission is required
- no LLM behavior is introduced
- no PR branch code is executed
- comments include an advisory footer
- comments disclose evidence source
- downstream workflows do not parse comments as commands

## Boundary

This document does not authorize comment mode.

It only defines the safety boundary that must be satisfied before any future advisory comment implementation is proposed.
