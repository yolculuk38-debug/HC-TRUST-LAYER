# HC Control Bot Evidence Prompt Boundary

This document defines the safety boundary for any future HC Control Bot evidence prompt support.

It is documentation only. It does not enable comments, workflows, labels, approvals, request-changes behavior, merge behavior, LLM behavior, or autonomous authority.

## Purpose

HC Control Bot may later help maintainers ask for evidence when protected or governance-adjacent surfaces are touched.

This support must remain advisory. The bot may identify missing evidence categories and ask for supporting material, but it must not decide whether the evidence is sufficient.

## Current status

Current HC Control Bot baseline:

- advisory-only
- non-LLM
- deterministic
- path-metadata based
- report-only
- artifact/log based
- human-supervised

Current behavior does not include evidence prompt comments or automated evidence sufficiency decisions.

## Operating model

Evidence prompt support must preserve the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

The bot may ask for evidence. Humans decide whether that evidence is enough.

## Allowed evidence prompt categories

A future evidence prompt may ask maintainers or contributors to provide:

- test output for runtime changes;
- test output for validator changes;
- example records for schema or record-boundary changes;
- before-and-after behavior notes for public verifier changes;
- documentation links for governance changes;
- migration notes for policy or project-control changes;
- generated artifact reproduction steps when generated files are changed;
- screenshots or logs for demo-only UI changes;
- security rationale for workflow or automation changes.

These prompts are review aids, not enforcement decisions.

## Disallowed evidence prompt behavior

Evidence prompt support must not:

- approve evidence as sufficient;
- reject evidence as insufficient;
- decide merge readiness;
- request changes;
- apply labels;
- block merges;
- bypass human review;
- certify correctness;
- certify security;
- certify production readiness;
- certify objective truth;
- certify legal or forensic validity.

## Protected-surface evidence expectations

When protected paths are touched, the bot may suggest evidence categories.

Examples:

| Surface | Possible evidence prompt |
| --- | --- |
| `.github/workflows/**` | Provide workflow safety rationale and confirm no PR branch code execution. |
| `src/hc_runtime/**` | Provide runtime tests and public-safe response examples. |
| `validators/**` | Provide validator test output and malformed-input behavior notes. |
| `schema/**` | Provide example records and compatibility notes. |
| `records/**` | Provide canonical record rationale and hash/provenance notes. |
| `docs/governance/**` | Provide related decision or policy reference. |
| `docs/project-control/**` | Provide operating-layer relationship and non-authority boundary. |
| `scripts/hc_control_bot.py` | Provide deterministic scanner test output and authority-boundary rationale. |

The bot may recommend these categories. It must not judge final sufficiency.

## Generated artifact evidence

When generated artifacts are observed, the bot may ask for:

- the canonical source used to generate them;
- reproduction command or workflow name;
- expected output relationship;
- confirmation that generated artifacts are not treated as canonical records.

Generated artifacts remain non-canonical unless a separate reviewed governance decision says otherwise.

## Evidence source disclosure

Any future evidence prompt should disclose what triggered the prompt.

For v0.1-style behavior, valid trigger sources include:

```text
Changed file metadata only.
Protected path match.
Governance-adjacent path match.
Generated artifact path match.
```

The prompt must not imply semantic file-content review unless a later approved implementation explicitly supports that scope.

## Safe prompt language

Acceptable:

```text
This change touches a protected path. Please provide relevant test output or rationale for human review.
```

Unsafe:

```text
This change lacks sufficient evidence and must be rejected.
```

Acceptable:

```text
Generated artifacts were observed. Please identify the canonical source and reproduction method.
```

Unsafe:

```text
The generated artifact is invalid.
```

## Human final authority

Maintainers decide whether submitted evidence is sufficient.

The bot may support evidence collection, but final review must remain human-supervised and grounded in repository evidence, CI results, governance rules, and maintainer judgment.

## Downstream automation boundary

No workflow or automation should treat evidence prompt text as a command, approval signal, rejection signal, merge signal, label signal, or governance decision.

Evidence prompts are human-readable review support only.

## Failure and disablement rule

If an evidence prompt implies authority, decides sufficiency, repeatedly creates noisy requests, or is used as command input by another workflow, maintainers should disable the evidence prompt mode and review the incident before re-enabling it.

## Implementation readiness checklist

Before enabling evidence prompt support, maintainers should confirm:

- authority policy is on `main`;
- report-only workflow is stable;
- report interpretation guide exists;
- advisory comment boundary exists if comments are used;
- no approval, request-changes, merge, close, or label permission is required;
- no LLM behavior is introduced;
- no PR branch code is executed;
- prompts disclose trigger source;
- prompts avoid sufficiency decisions;
- downstream workflows do not parse prompts as commands.

## Boundary

This document does not authorize evidence prompt implementation.

It only defines the safety boundary that must be satisfied before any future evidence prompt support is proposed.
