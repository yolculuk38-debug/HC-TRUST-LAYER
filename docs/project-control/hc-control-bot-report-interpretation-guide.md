# HC Control Bot Report Interpretation Guide

This guide explains how maintainers should read HC Control Bot v0.1 report artifacts.

The report is a support signal for human review. It is not an approval, rejection, merge decision, truth guarantee, or replacement for maintainer judgment.

## Scope

This document is documentation only.

It does not change:

- runtime behavior
- schemas
- validators
- records
- policies
- workflows
- scanner logic
- pull request comments
- labels
- approval behavior
- merge behavior
- LLM behavior

## Operating model

HC Control Bot v0.1 remains intentionally limited:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

The bot output is advisory-only. Human final authority remains unchanged.

## What the report can do

The report can help maintainers notice review-relevant signals, such as:

- protected paths touched by a pull request
- governance-adjacent files changed by a pull request
- generated artifacts observed in the changed file list
- whether human review is required
- deterministic warnings from path metadata
- risk-relevant changed file categories

These signals help prioritize review. They do not decide the result of the pull request.

## What the report must not do

The report must not be treated as:

- a pull request approval
- a pull request rejection
- a request-changes decision
- merge authority
- close authority
- label authority
- a production-readiness claim
- a truth guarantee
- a legal or forensic conclusion
- an instruction to another workflow

Other automation must not parse bot report text as a command source.

## Field interpretation

### `changed_files`

The list of file paths observed for the pull request.

Maintainers should use this as the starting point for review scope. File paths are review metadata, not evidence that the content is safe.

### `protected_paths_touched`

A list of changed files that match protected or trust-critical areas.

Examples may include paths under:

- `.github/workflows/`
- `schema/`
- `validators/`
- `src/hc_runtime/`
- `records/`
- `signatures/`
- `policy/`
- `federation/`
- `docs/governance/`
- `docs/project-control/`
- `scripts/hc_control_bot.py`

If this field is not empty, maintainers should apply extra review discipline. This is not an automatic rejection.

### `governance_adjacent_paths`

A list of files that may affect operating rules, contributor expectations, maintainer workflow, or project-control guidance.

These files may not always be runtime-critical, but they can influence how humans and AI agents operate in the repository.

Maintainers should check that changes preserve:

- AI advisory-only behavior
- human final authority
- protected-path discipline
- audit visibility
- no autonomous approval or merge authority

### `generated_artifacts_observed`

A list of generated, derived, index, report, cache, or artifact-like files observed in the change set.

Generated artifacts are not canonical records. They should not override canonical schema, record, validator, policy, or governance sources.

Maintainers should check whether generated artifacts are expected, reproducible, and consistent with the canonical source files.

### `human_review_required`

A boolean signal that human review should occur before the pull request is considered safe to merge.

For HC-TRUST-LAYER, human review is the final authority even when this field is false. A false value only means the deterministic scanner did not observe a specific path-based trigger.

### `warnings`

A list of deterministic advisory warnings.

Warnings should be read as review prompts. They should not be treated as commands, final decisions, or proof of failure.

Maintainers should resolve the underlying concern through normal review, tests, governance checks, and audit judgment.

### `risk_level`

If present, this field summarizes path-metadata risk for maintainer attention.

A higher risk level means review should be more careful. It does not mean the pull request must be rejected.

### `advisory_only`

This field should remain true for HC Control Bot v0.1 outputs.

It confirms that the report is advisory support only and cannot approve, reject, merge, close, label, or override a pull request.

### `public_safe`

This field indicates whether the report is intended to be safe for public repository visibility.

Public-safe does not mean production-ready, legally authoritative, or objectively true.

### `truth_guarantee`

This field must remain false.

HC Control Bot does not certify objective truth, forensic certainty, legal validity, or final correctness.

## Maintainer review guidance

When reviewing a report:

1. Start with the changed file list.
2. Check whether protected paths were touched.
3. Check whether governance-adjacent paths were touched.
4. Check whether generated artifacts are present.
5. Read warnings as prompts for human review.
6. Confirm that CI and governance checks passed.
7. Apply normal maintainer judgment before merge.

A HIGH risk signal means review carefully. It does not mean auto-reject.

## Workflow and governance changes

Changes to workflows, governance files, protected-path logic, scanner behavior, or project-control guidance require extra human review.

Maintainers should confirm that such changes do not introduce:

- autonomous approval behavior
- autonomous rejection behavior
- autonomous merge or close behavior
- hidden label authority
- LLM-based decision paths
- command parsing from untrusted PR content
- governance configuration read from an untrusted branch

## Generated artifact handling

Generated artifacts can support visibility, reports, or demo behavior, but they are not canonical record surfaces.

Maintainers should not treat generated artifacts as replacements for:

- canonical records
- schema definitions
- validator behavior
- signed evidence
- governance policy
- source-of-truth documentation

## Safe conclusion language

Acceptable interpretation:

```text
The HC Control Bot report found review-relevant signals.
A maintainer should inspect the affected paths and decide whether the PR is safe to merge.
```

Unsafe interpretation:

```text
The bot says this PR is safe, so it can be merged automatically.
```

## Boundary

This guide preserves HC Control Bot v0.1 as a deterministic, non-LLM, report-only, human-supervised review support layer.

It does not add automation authority.
