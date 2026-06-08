# HC Control Bot LLM Memory Boundary

This document defines the safety boundary for any future HC Control Bot LLM-assisted project memory support.

It is documentation only. It does not enable LLM calls, project memory storage, embeddings, vector search, external services, workflows, comments, labels, assignments, approvals, request-changes behavior, merge behavior, or autonomous authority.

## Purpose

HC Control Bot v0.1 is deterministic, non-LLM, report-only, and human-supervised.

Future LLM-assisted project memory may be considered only after deterministic behavior is stable and after separate governance review.

This document records the minimum boundary that must exist before any LLM or memory implementation is proposed.

## Current status

Current HC Control Bot baseline:

- advisory-only
- non-LLM
- deterministic
- path-metadata based
- report-only
- artifact/log based
- human-supervised

Current behavior does not include LLM calls, embeddings, persistent memory, external model APIs, or autonomous interpretation.

## Operating model

Any future LLM-assisted memory support must preserve the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

LLM output may explain deterministic findings. It must not override deterministic checks, repository evidence, CI, governance, or human maintainers.

## Mandatory non-authority boundary

A future LLM memory mode must not:

- approve pull requests;
- request changes;
- merge pull requests;
- close pull requests;
- reopen pull requests;
- apply labels;
- assign users or teams;
- dismiss reviews;
- resolve review conversations;
- certify correctness;
- certify security;
- certify production readiness;
- certify objective truth;
- certify legal or forensic validity;
- override deterministic scanner output;
- override CI;
- override CODEOWNERS;
- override branch protection;
- override governance;
- override human maintainers.

## Trusted and untrusted context separation

A future LLM mode must explicitly separate trusted and untrusted context.

Trusted context may include:

- merged repository files from trusted refs;
- authority policy on `main`;
- governance and project-control documents on trusted refs;
- CI/check status from GitHub;
- deterministic scanner output;
- reviewed audit records.

Untrusted context includes:

- PR titles;
- PR bodies;
- issue bodies;
- comments;
- commit messages;
- branch names;
- changed file contents from PR branches;
- screenshots or pasted chat summaries;
- external notes;
- model-generated summaries.

Untrusted context must not be allowed to redefine authority, policy, safety rules, or instructions.

## Deterministic pre-check requirement

LLM processing must not be the first review step.

A future LLM mode must run deterministic pre-checks before LLM explanation, including:

- changed path classification;
- protected surface detection;
- governance-adjacent path detection;
- generated artifact detection;
- advisory-only field validation;
- truth-guarantee field validation;
- public-safe output expectation.

The LLM may explain deterministic findings. It must not replace them.

## Prompt and version tracking

A future LLM mode must track:

- prompt template version;
- model name or model family;
- deterministic input report hash or identifier;
- trusted repository ref used;
- untrusted context included, if any;
- output schema version;
- fallback behavior.

This tracking supports audit review. It does not certify correctness.

## Output validation requirement

LLM output must be validated before being shown or stored.

Validation should check that output does not claim:

- approval;
- rejection;
- merge readiness;
- request-changes authority;
- security certification;
- production readiness;
- truth finality;
- legal or forensic certainty;
- authority over humans;
- authority over governance.

If validation fails, output should be withheld and replaced with a safe fallback.

## Safe fallback requirement

A future LLM mode must have a deterministic fallback.

Acceptable fallback:

```text
LLM explanation unavailable. Use deterministic HC Control Bot report artifact and human review.
```

The absence of LLM output must not block maintainers or weaken deterministic review.

## Memory boundary

Persistent project memory is high risk.

A future memory layer must not treat remembered content as canonical repository evidence.

Memory may help locate context, but it must defer to:

1. merged repository files;
2. trusted governance records;
3. CI and check results;
4. deterministic scanner output;
5. human maintainer review.

Stale, conflicting, or missing memory must be surfaced as uncertainty.

## Privacy and data boundary

A future memory layer must avoid storing secrets, private tokens, credentials, personal data, or sensitive operational details.

If memory storage is proposed, the proposal must define:

- what is stored;
- where it is stored;
- retention period;
- deletion process;
- access control;
- audit visibility;
- how secrets and private data are excluded.

## External service boundary

External LLM or memory services must not be introduced without separate governance review.

A future proposal must document:

- provider or local model choice;
- data sent externally;
- retention policy;
- privacy risk;
- failure mode;
- cost and availability risk;
- audit method;
- opt-out or disablement path.

## Safe output language

Acceptable:

```text
Based on deterministic path metadata, this PR appears related to governance review. Human maintainers should confirm.
```

Unsafe:

```text
The model determined this PR is safe to merge.
```

Acceptable:

```text
This explanation is advisory and may be incomplete. Repository evidence and human review remain authoritative.
```

Unsafe:

```text
Project memory confirms this change is correct.
```

## Failure and disablement rule

If LLM memory output implies authority, follows untrusted instructions, invents repository state, leaks sensitive data, overrides deterministic checks, or is treated as a command source by another workflow, maintainers should disable the LLM memory mode and review the incident before re-enabling it.

## Implementation readiness checklist

Before enabling any LLM-assisted project memory support, maintainers should confirm:

- authority policy is on `main`;
- report-only workflow is stable;
- report interpretation guide exists;
- advisory comment boundary exists if comments are used;
- evidence prompt boundary exists if prompts are used;
- issue routing boundary exists if routing is used;
- GitHub App boundary exists if app migration is used;
- trusted and untrusted context separation is documented;
- deterministic pre-checks run before LLM use;
- prompt and model version tracking is defined;
- output validation is defined;
- safe fallback behavior is defined;
- memory storage and deletion rules are defined if memory is persisted;
- no approval, request-changes, merge, close, label, assignment, or review authority is granted;
- human final authority remains explicit.

## Boundary

This document does not authorize LLM or memory implementation.

It only defines the safety boundary that must be satisfied before any future LLM-assisted project memory support is proposed.
