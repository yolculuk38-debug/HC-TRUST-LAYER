# HC-TRUST-LAYER Policy Workflow Integration (Advisory)

## Purpose

This document explains how HC-TRUST-LAYER CI now runs advisory policy evaluation on pull requests to produce merge risk guidance for human-supervised validation in the trust kernel.

The policy workflow is advisory-only and part of verification infrastructure hardening, not runtime merge enforcement.

## CI Integration Model

The GitHub Actions workflow `.github/workflows/policy-evaluation.yml` runs on pull request events and performs these steps:

1. collects changed file paths from the pull request diff,
2. executes `scripts/evaluate_policy.py` with those paths,
3. parses evaluator output into a compact advisory summary,
4. prints detected merge risk and recommended merge outcome.

This preserves existing workflow optimization by only evaluating paths changed in the PR.

## Merge Risk Classification

The advisory policy workflow reports:

- detected risk level (`low`, `medium`, `high`, `blocked`),
- affected policy categories (`low`, `medium`, `high`, `blocked`, `unknown`),
- recommended merge outcome:
  - `auto_merge_allowed`
  - `conditional_merge`
  - `human_review_required`
  - `blocked`

Unknown-path routing is conservative and escalates to `human_review_required`.

## Safe Fallback Behavior

The policy workflow includes conservative fallbacks:

- evaluator parsing failure => warning + `human_review_required`
- unknown path category => warning + `human_review_required`

These fallbacks keep advisory policy evaluation deterministic and compatible with trust kernel safety expectations.

## Current Limitations

Current HC-TRUST-LAYER policy workflow scope is intentionally limited:

- no runtime merge decision enforcement,
- no branch protection modification,
- no auto-close behavior,
- no auto-merge behavior,
- no validator changes,
- no schema changes.

## Future Enforcement Roadmap

Future phases may introduce explicit policy enforcement gates after governance approval, including:

- policy trace artifacts for audit review,
- opt-in enforcement switches for protected branches,
- explicit human-supervised validation checkpoints before any enforcement activation.

Any enforcement migration should remain transparent, auditable, and bounded by trust kernel controls.

## Workflow Examples

### Example 1: Docs-only PR

Changed paths: `docs/policy-evaluator.md`, `README.md`

Expected advisory output:

- risk level: `low`
- affected categories: `low`
- recommended merge outcome: `auto_merge_allowed`

### Example 2: Workflow Modification PR

Changed paths: `.github/workflows/docs-drift.yml`

Expected advisory output:

- risk level: `medium`
- affected categories: `medium`
- recommended merge outcome: `conditional_merge`

### Example 3: Schema Modification PR

Changed paths: `schema/record-v1.schema.json`

Expected advisory output:

- risk level: `high`
- affected categories: `high`
- recommended merge outcome: `human_review_required`

### Example 4: Blocked Generated Artifact Path

Changed paths: `generated/demo-output.json`

Expected advisory output:

- risk level: `blocked`
- affected categories: `blocked`
- recommended merge outcome: `blocked`

This route still remains advisory at this phase and supports human-supervised validation.
