# PR Governance Preflight (Advisory)

## Purpose

The HC-TRUST-LAYER PR governance preflight adds a lightweight, deterministic advisory layer for pull request risk signaling before merge eligibility decisions.

This control-layer script helps reviewers quickly triage scope while preserving human-supervised validation and reviewer authority.

## Script

- Path: `scripts/check_pr_governance.py`
- Invocation: `python scripts/check_pr_governance.py`

## Governance Signals

The script classifies changed paths into `LOW`, `MEDIUM`, or `HIGH` risk and prints:

- `RISK: LOW|MEDIUM|HIGH`
- `AUTO_MERGE_ELIGIBLE: yes|no`
- `HUMAN_REVIEW_REQUIRED: yes|no`
- `PROTECTED_PATHS_TOUCHED: yes|no`

Additional advisory flags are reported for docs-only, dependency-only, and tests-only scope.
When label conflicts are present, an explicit `OVERRIDE_REASON` field is emitted.

## Protected Paths

The preflight treats the following path families as protected:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- `src/hc_runtime/**`

Touching any protected path is classified as `HIGH` risk.

## Eligibility Logic

### HIGH risk

- Always requires human review.
- Never auto-merge eligible.

### LOW risk

LOW risk eligibility is limited to:

- docs-only changes, or
- dependency-only patch changes, or
- tests-only hardening,

and only when protected paths are not touched.

### MEDIUM risk

All remaining non-protected mixed scopes are treated as `MEDIUM` and require human review.

## Label Conflict Handling (Governance Override)

The preflight accepts optional labels using:

- `python scripts/check_pr_governance.py --labels <label1> <label2> ...`

When conflicting labels are present, manual governance boundaries override auto-merge eligibility:

- `manual-review` + `auto-merge`
- `risk-high` + `auto-merge`
- `blocked-human-review` + `auto-merge`

Expected behavior for each conflict:

- auto-merge must not proceed,
- human-supervised validation is required,
- workflow may cancel auto-merge safely,
- preflight prints `OVERRIDE_REASON` with the governing explanation.

Manual-review semantics always override auto-merge eligibility in this advisory governance layer.

## Authority and Safety Boundary

This preflight is advisory-only governance guidance.

- It does **not** change runtime semantics.
- It does **not** modify canonical schema behavior.
- It does **not** weaken validators.
- It does **not** alter signing or security workflows.
- It does **not** enable unrestricted autonomous merge behavior.

Final merge authority remains human-supervised in HC:// and HC-TRUST-LAYER governance workflows.
