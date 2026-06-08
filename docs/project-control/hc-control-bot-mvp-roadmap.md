# HC Control Bot MVP Roadmap

> Status: planning roadmap
>
> Depends on: `docs/governance/hc-control-bot-authority-policy.md`
>
> Mode: documentation only

## Purpose

This roadmap defines the safe implementation path for the planned HC Control Bot / HC Trust Engineer.

This document does not implement code, scripts, workflows, runtime behavior, validators, schemas, records, QR behavior, signing, federation, generated artifacts, LLM integration, labels, checks, or dashboard features.

## Operating Principle

The first working version must be boring, deterministic, auditable, and non-authoritative.

The bot begins as an advisory path scanner, not as an autonomous reviewer.

## Required Order

Implementation must proceed in this order:

1. Authority policy on `main`.
2. MVP roadmap on `main`.
3. Deterministic scanner script.
4. Scanner tests.
5. Report-only integration.
6. Single advisory comment mode.
7. Evidence prompt support.
8. Optional issue routing.
9. Optional GitHub App migration.
10. Optional LLM-assisted project memory.

Steps 3 and later require separate PRs.

## Phase 0: Authority Policy

Phase 0 is complete when the authority policy exists on `main`.

The policy defines:

- advisory-only scope;
- human final authority;
- trusted `main@SHA` evidence model;
- untrusted PR and issue input model;
- deterministic non-LLM v0.1 requirement;
- future LLM conditions;
- comment safety rules;
- downstream automation boundary;
- protected surface escalation;
- audit expectations;
- future expansion review.

## Phase 1: Non-LLM Deterministic Scanner

Goal: create a small path and metadata scanner.

Recommended file:

```text
scripts/hc_control_bot.py
```

Allowed behavior:

- accept a list of changed file paths;
- match paths against protected or governance-adjacent surfaces;
- produce a structured advisory result;
- avoid reading PR body, comments, commit messages, or file contents for risk decisions;
- avoid LLM calls;
- avoid semantic review.

Initial protected surfaces may include:

```text
.github/workflows/**
schema/**
validators/**
src/hc_runtime/**
records/**
signatures/**
policy/**
federation/**
docs/governance/**
docs/project-control/**
scripts/hc_control_bot.py
```

Expected result fields:

```text
advisory_only
public_safe
truth_guarantee
human_review_required
protected_paths_touched
warnings
evidence_source
```

## Phase 2: Scanner Tests

Goal: lock deterministic behavior before workflow integration.

Recommended tests:

```text
tests/test_hc_control_bot.py
```

Test cases:

- non-protected docs path returns low advisory risk;
- governance path requires human review;
- workflow path raises protected-surface warning;
- runtime path raises protected-surface warning;
- generated artifact path is not treated as canonical record by default;
- instruction-like PR text has no effect on scanner result;
- output always includes advisory and public-safety fields.

## Phase 3: Report-Only Integration

Goal: surface scanner output without creating authority confusion.

The first integration should be report-only if maintainers want the smallest workflow step.

Safety requirements:

- do not execute PR-branch code;
- do not read governance or bot policy files from the PR branch;
- read policy and configuration from trusted `main@SHA`;
- use changed-file metadata instead of untrusted PR content;
- never approve, reject, merge, close, reopen, or certify.

## Phase 4: Single Advisory Comment

Goal: make the bot useful without creating noise.

Comment rules:

- one bot comment per PR;
- update existing bot comment instead of posting repeated comments;
- skip or minimize output for draft PRs;
- aggregate all findings into one concise report;
- avoid decision-like wording;
- include the advisory notice from the authority policy.

Suggested comment shape:

```text
HC Control Bot Advisory Note

Changed surfaces observed:
- docs/governance/example.md

Advisory observations:
- Protected or governance-adjacent path matched.
- Human-supervised review remains required.

Evidence source:
- Changed file metadata only.
- Policy baseline: main@SHA.

This observation is non-authoritative.
Human maintainers retain final authority.
Trust the record, not the narrative.
```

## Phase 5: Evidence Prompt Support

Goal: ask for evidence when protected surfaces are touched.

Allowed prompts may request:

- test output for runtime or validator changes;
- example records for schema or record-boundary changes;
- documentation links for governance changes;
- before-and-after behavior notes for public verifier changes.

The bot may ask for evidence, but must not decide whether the evidence is sufficient.

## Phase 6: Optional Issue Routing

Goal: help maintainers classify work.

This phase should not be added until the deterministic scanner is stable.

Allowed behavior:

- suggest likely area labels in plain text;
- surface related docs;
- leave final routing to humans.

## Phase 7: Optional GitHub App Migration

A GitHub App may be considered after the workflow version proves stable.

Possible reasons:

- cleaner permission isolation;
- multi-repo support;
- richer audit logs;
- project memory outside runner context;
- better webhook handling.

Migration must preserve the authority policy.

## Phase 8: Future LLM-Assisted Project Memory

LLM usage is not allowed in v0.1.

Future LLM use requires separate governance review and must include:

- trusted and untrusted context separation;
- deterministic pre-checks before LLM processing;
- output validation;
- prompt and version tracking;
- fallback output;
- no authority actions;
- audit logging.

The LLM may explain deterministic findings, but must not override them.

## Explicit Non-Goals for MVP

The MVP must not include:

- autonomous code review;
- approval or rejection behavior;
- merge behavior;
- issue closing or reopening;
- label automation unless separately approved;
- trust scoring;
- production-readiness claims;
- truth claims;
- LLM calls;
- embeddings;
- vector databases;
- dashboard or chat UI;
- multi-repo memory;
- CI release or deployment decisions.

## Review Gates

Each implementation phase should answer:

1. What trusted evidence did it read?
2. What untrusted input did it observe?
3. What actions can it take?
4. What actions are impossible by design?
5. What audit trace is produced?
6. How can a human maintainer ignore the advisory output?
7. Does it preserve AI advisory only and human final authority?

## Recommended PR Sequence

```text
#691 docs(project-control): add HC Control Bot MVP roadmap
#692 scripts: add HC Control Bot deterministic scanner
#693 tests: cover HC Control Bot scanner behavior
#694 workflows: add HC Control Bot report-only workflow
#695 workflows: add single advisory PR comment mode
```

The sequence may change if governance review requires a smaller step.

## MVP Completion Criteria

The MVP is complete when:

- authority policy exists on `main`;
- roadmap exists on `main`;
- deterministic scanner has tests;
- report integration avoids PR-branch governance as trusted input;
- output is advisory-only;
- one-comment behavior prevents noise;
- audit fields are available;
- humans remain the only final authority.
