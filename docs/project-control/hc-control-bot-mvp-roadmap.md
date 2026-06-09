# HC Control Bot MVP Roadmap

> Status: implementation in progress
>
> Depends on: `docs/governance/hc-control-bot-authority-policy.md`
>
> Mode: roadmap and implementation status tracking

## Purpose

This roadmap defines the safe implementation path for the HC Control Bot / HC Trust Engineer.

This document tracks implementation state only. It does not itself implement code, scripts, workflows, runtime behavior, validators, schemas, records, QR behavior, signing, federation, generated artifacts, LLM integration, labels, checks, or dashboard features.

## Current Implementation Snapshot

As of the current roadmap update, the MVP has moved from planning into early implementation.

Implemented or partially implemented:

- deterministic path scanner in `scripts/hc_control_bot.py`;
- scanner tests in `tests/test_hc_control_bot.py`;
- machine-readable advisory JSON output;
- newline-delimited changed-path file input for safer workflow integration;
- single advisory comment workflow in `.github/workflows/hc-control-bot-advisory-comment.yml`;
- advisory-only wording and human final authority boundary.

Still not implemented:

- autonomous approval, rejection, closing, or merge behavior;
- automatic label application;
- LLM calls;
- trust scoring;
- production-readiness claims;
- external federation or hosted API behavior.

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

Steps 1 through 6 are now represented in repository artifacts. Later steps still require separate PRs and human maintainer review.

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

Status: represented in repository governance docs.

## Phase 1: Non-LLM Deterministic Scanner

Goal: create a small path and metadata scanner.

Implemented file:

```text
scripts/hc_control_bot.py
```

Allowed behavior:

- accept a list of changed file paths;
- accept a newline-delimited changed-paths file;
- match paths against protected or governance-adjacent surfaces;
- produce a structured advisory result;
- avoid reading PR body, comments, commit messages, or file contents for risk decisions;
- avoid LLM calls;
- avoid semantic review.

Initial protected surfaces include:

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

Expected result fields include:

```text
advisory_only
public_safe
truth_guarantee
human_review_required
review_priority
protected_paths_touched
governance_adjacent_paths_touched
generated_artifacts_observed
warnings
evidence_prompts
review_routes
suggested_labels
evidence_source
```

Status: implemented as deterministic scanner behavior.

## Phase 2: Scanner Tests

Goal: lock deterministic behavior before workflow integration.

Implemented tests:

```text
tests/test_hc_control_bot.py
```

Test coverage includes:

- non-protected docs path returns low advisory risk;
- governance path requires human review;
- workflow path raises protected-surface warning;
- runtime path raises protected-surface warning;
- generated artifact path is not treated as canonical record by default;
- instruction-like path text has no authority effect on scanner result;
- output always includes advisory and public-safety fields;
- CLI output remains machine-readable JSON;
- newline-delimited changed-path file input is supported.

Status: implemented as scanner regression coverage.

## Phase 3: Report-Only Integration

Goal: surface scanner output without creating authority confusion.

The first integration should be report-only if maintainers want the smallest workflow step.

Safety requirements:

- do not execute PR-branch code;
- do not read governance or bot policy files from the PR branch;
- read policy and configuration from trusted `main@SHA`;
- use changed-file metadata instead of untrusted PR content;
- never approve, reject, merge, close, reopen, or certify.

Status: represented by the advisory comment workflow, which checks out the trusted base revision and runs the deterministic scanner.

## Phase 4: Single Advisory Comment

Goal: make the bot useful without creating noise.

Comment rules:

- one bot comment per PR;
- update existing bot comment instead of posting repeated comments;
- aggregate all findings into one concise report;
- avoid decision-like wording;
- include advisory-only and human final authority language.

Current comment shape includes:

```text
HC Control Bot advisory observation

This is advisory and uses changed file path metadata only.
It is not approval, rejection, merge authority, or a final validation result.
Human maintainers retain final authority.
```

Status: implemented as single advisory comment workflow behavior.

## Phase 5: Evidence Prompt Support

Goal: ask for evidence when protected surfaces are touched.

Allowed prompts may request:

- test output for runtime or validator changes;
- example records for schema or record-boundary changes;
- documentation links for governance changes;
- before-and-after behavior notes for public verifier changes.

The bot may ask for evidence, but must not decide whether the evidence is sufficient.

Status: partially implemented as deterministic `evidence_prompts` in scanner output.

## Phase 6: Optional Issue Routing

Goal: help maintainers classify work.

This phase should not be added until the deterministic scanner is stable.

Allowed behavior:

- suggest likely area labels in plain text;
- surface related docs;
- leave final routing to humans.

Status: partially represented as suggested labels in advisory output only. No automatic label application is implemented.

## Phase 7: Optional GitHub App Migration

A GitHub App may be considered after the workflow version proves stable.

Possible reasons:

- cleaner permission isolation;
- multi-repo support;
- richer audit logs;
- project memory outside runner context;
- better webhook handling.

Migration must preserve the authority policy.

Status: deferred.

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

Status: deferred.

## Explicit Non-Goals for MVP

The MVP must not include:

- autonomous code review;
- approval or rejection behavior;
- merge behavior;
- issue closing or reopening;
- automatic label application unless separately approved;
- trust scoring;
- production-readiness claims;
- truth claims;
- LLM calls;
- embeddings;
- vector databases.
