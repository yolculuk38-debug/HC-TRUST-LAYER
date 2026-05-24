# HC-TRUST-LAYER Policy Evaluator (Advisory Skeleton)

## Purpose

The `policy evaluator` is an advisory-only CLI skeleton that starts turning HC:// machine-readable `policy rules` into executable merge risk classification.

In this phase, it does **not** enforce merge outcomes. It supports trust kernel visibility and human-supervised validation by producing deterministic guidance from changed repository paths.

## Script

- Path: `scripts/evaluate_policy.py`
- Policy input: `policy/hc-policy-v1.yml`
- Runtime mode: advisory-only

## Inputs

The evaluator accepts changed file paths as CLI arguments:

```bash
python3 scripts/evaluate_policy.py <path1> <path2> ...
```

It loads path risk patterns from `policy/hc-policy-v1.yml` and classifies each path into:

- `low`
- `medium`
- `high`
- `blocked`
- `unknown` (fallback category for unmatched paths)

## Output Summary

The evaluator prints:

1. category counts
2. per-category path listing
3. recommended merge outcome

Recommended outcomes:

- `auto_merge_allowed`
- `conditional_merge`
- `human_review_required`
- `blocked`

## Current Merge Risk Logic

Initial HC-TRUST-LAYER policy evaluator behavior:

- blocked path match => `blocked`
- high risk path match => `human_review_required`
- medium risk path match => `conditional_merge`
- only low risk paths => `auto_merge_allowed`
- unknown paths => `human_review_required`

This logic is intentionally conservative for trust kernel safety and human-supervised validation.

## Safe Fallback Behavior

If policy parsing fails (missing file or invalid structure), the evaluator fails closed:

- returns non-zero exit status
- emits advisory parse-failure summary
- recommends `human_review_required`

This keeps merge risk routing conservative even when policy rules cannot be read.

## Dependency Model

The skeleton avoids external dependencies.

It uses a minimal in-repo parser for the specific `path_risk_rules` structure in `policy/hc-policy-v1.yml`, so current CI does not require adding a YAML package.

## Examples

### 1) Docs-only change

```bash
python3 scripts/evaluate_policy.py README.md
```

Expected merge risk guidance: `auto_merge_allowed`.

### 2) Workflow change

```bash
python3 scripts/evaluate_policy.py .github/workflows/terminology.yml
```

Expected merge risk guidance: `conditional_merge`.

### 3) Record schema change

```bash
python3 scripts/evaluate_policy.py schema/record-v1.schema.json
```

Expected merge risk guidance: `human_review_required`.

### 4) Generated artifact path

```bash
python3 scripts/evaluate_policy.py generated/test.json
```

Expected merge risk guidance: `blocked`.

## Future Workflow Integration

Planned next steps (not implemented in this skeleton):

- wire evaluator output into CI reporting artifacts
- feed merge risk summary into policy engine decision traces
- keep enforcement disabled until explicit governance activation

The current implementation remains advisory-only and does not alter branch protection, validators, or schemas.
- Policy workflow integration: `docs/policy-workflow-integration.md`

