# PR Governance Preflight (Advisory)

## Purpose

The HC-TRUST-LAYER PR governance preflight adds a lightweight, deterministic advisory layer for pull request risk signaling before merge eligibility decisions.

This control-layer script helps reviewers quickly triage scope while preserving human-supervised validation and reviewer authority.

## Script

- Path: `scripts/check_pr_governance.py`
- Invocation: `python scripts/check_pr_governance.py`

## Governance Signals

The script classifies changed paths into `LOW`, `MEDIUM`, or `HIGH` risk and prints two report sections:

1. `HUMAN_READABLE_SUMMARY` for maintainers and reviewers.
2. `MACHINE_READABLE_SUMMARY` for automation and parser stability.

Human-readable fields include:

- risk level
- auto-merge eligibility
- human review requirement
- protected-path touch status and protected path list
- override reason (or `none`)

Machine-readable fields continue to include:

- `RISK: LOW|MEDIUM|HIGH`
- `AUTO_MERGE_ELIGIBLE: yes|no`
- `HUMAN_REVIEW_REQUIRED: yes|no`
- `PROTECTED_PATHS_TOUCHED: yes|no`
- `OVERRIDE_REASON: ...` when applicable

Additional advisory flags are reported for docs-only, dependency-only, and tests-only scope.

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

## Maintainer Read Order

To keep governance preflight review fast and mobile-readable:

1. Read `HUMAN_READABLE_SUMMARY` first for immediate triage.
2. If `Protected paths touched` is `yes`, route to human-supervised validation and appropriate reviewers.
3. If `Auto-merge eligible` is `no`, check `Override reason` for blocking governance context.
4. Use `MACHINE_READABLE_SUMMARY` only for automation checks, logs, and parser-backed workflows.

This preserves human-supervised validation while keeping HC:// governance status obvious at a glance.
