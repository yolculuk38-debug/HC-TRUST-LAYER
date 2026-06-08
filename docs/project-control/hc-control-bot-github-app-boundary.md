# HC Control Bot GitHub App Boundary

This document defines the safety boundary for any future HC Control Bot GitHub App migration.

It is documentation only. It does not create a GitHub App, change workflows, request new permissions, add webhooks, add comments, add labels, add assignments, approve pull requests, merge pull requests, introduce LLM behavior, or grant autonomous authority.

## Purpose

HC Control Bot currently runs as a repository workflow-based advisory layer.

A GitHub App may be considered later only if the workflow version proves stable and maintainers need cleaner permission isolation, richer audit logs, multi-repository support, or better webhook handling.

Any migration must preserve the authority policy.

## Current status

Current HC Control Bot baseline:

- advisory-only
- non-LLM
- deterministic
- path-metadata based
- report-only
- artifact/log based
- human-supervised

Current behavior does not include a GitHub App.

## Operating model

Any GitHub App migration must preserve the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

A GitHub App may improve operational isolation. It must not create decision authority.

## Allowed reasons to consider a GitHub App

A future GitHub App may be considered for:

- cleaner permission isolation;
- explicit app-level audit logs;
- separate installation and revocation control;
- multi-repository support;
- better webhook event handling;
- reduced reliance on broad workflow token behavior;
- clearer separation between advisory reporting and maintainer authority.

These are operational reasons only. They do not justify autonomous decision-making.

## Mandatory authority boundary

A future GitHub App must not:

- approve pull requests;
- request changes;
- merge pull requests;
- close pull requests;
- reopen pull requests;
- apply labels without separate governance approval;
- remove labels without separate governance approval;
- assign users or teams without separate governance approval;
- dismiss reviews;
- resolve review conversations;
- bypass CI;
- bypass CODEOWNERS;
- bypass branch protection;
- override governance;
- override human maintainers;
- certify correctness;
- certify security;
- certify production readiness;
- certify objective truth;
- certify legal or forensic validity.

## Permission principle

A future GitHub App must use least privilege.

The default permission posture should be read-only unless a separate reviewed governance decision grants a narrow write action.

Potential read-only capabilities may include:

- read pull request metadata;
- read changed file paths;
- read repository contents from trusted refs;
- read workflow/check status;
- read issues for advisory orientation;
- read review metadata for audit context.

Potential write capabilities must be treated as separate governance decisions.

## Write permission boundary

Write permissions are authority-sensitive.

A future GitHub App must not receive write permissions for comments, labels, assignments, checks, statuses, reviews, issues, or pull requests unless the exact behavior is separately documented, reviewed, tested, and approved by human maintainers.

Even if a write permission is later granted, the app output must remain advisory unless governance explicitly changes that boundary.

## Webhook input boundary

Webhook payloads are event inputs, not trusted truth sources.

A future GitHub App must treat PR titles, PR bodies, issue bodies, comments, commit messages, branch names, and changed file contents as untrusted input.

Trusted policy and configuration must come from reviewed repository state, preferably `main@SHA` or another explicitly trusted ref.

## Configuration boundary

The app must not read authority policy, routing rules, safety rules, or decision rules from an untrusted PR branch.

If configuration is needed, it should be versioned, auditable, and read from a trusted baseline.

## Audit requirements

A future GitHub App migration should provide audit visibility for:

- event received;
- trigger source;
- repository and ref used;
- changed path metadata used;
- advisory output generated;
- permission scope used;
- whether any write action was attempted;
- human-facing output produced;
- errors or fallback behavior.

Audit logs must support review. They must not imply final correctness.

## Failure and disablement rule

If a GitHub App performs authority-like behavior, uses excessive permissions, reads policy from an untrusted branch, treats user text as commands, or is interpreted as merge authority, maintainers should disable the app and review the incident before re-enabling it.

## Migration readiness checklist

Before creating or installing a GitHub App, maintainers should confirm:

- authority policy is on `main`;
- report-only workflow is stable;
- report interpretation guide exists;
- advisory comment boundary exists if comments are used;
- evidence prompt boundary exists if prompts are used;
- issue routing boundary exists if routing is used;
- required permissions are listed and justified;
- default permissions are read-only;
- no merge, approval, request-changes, close, label, assignment, or review authority is granted by default;
- webhook inputs are treated as untrusted;
- trusted configuration source is defined;
- audit log expectations are defined;
- human final authority remains explicit.

## Boundary

This document does not authorize GitHub App implementation.

It only defines the safety boundary that must be satisfied before any future GitHub App migration is proposed.
