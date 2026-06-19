# Governance Preflight Workflow Integration (Advisory)

## Purpose

This workflow integrates the HC-TRUST-LAYER governance preflight into GitHub Actions so pull request governance classification is part of the repository control pipeline.

The workflow is advisory and preserves HC:// human-supervised validation authority.

## Workflow

- Path: `.github/workflows/governance-preflight.yml`
- Trigger: pull request events (`opened`, `synchronize`, `reopened`, `ready_for_review`)
- Commands:
  - `python scripts/check_github_actions_versions.py`
  - `python scripts/check_pr_governance.py --base-ref <base-sha> --head-ref <head-sha>`

## Deterministic and Lightweight Design

- Uses `actions/checkout@v6` with full history (`fetch-depth: 0`) for stable diff availability.
- Uses `actions/setup-python@v6` with `python-version: '3.x'`.
- Runs `scripts/check_github_actions_versions.py` as a deterministic, network-free stale action guard before governance classification.
- Uses deterministic PR SHA inputs from `github.event.pull_request.base.sha` and `github.event.pull_request.head.sha`.
- Uses workflow concurrency and bounded runtime (`timeout-minutes: 10`) to keep execution predictable and low-friction.

## Required Governance Summary in Logs

The workflow prints the governance summary fields from `scripts/check_pr_governance.py`:

- `RISK`
- `AUTO_MERGE_ELIGIBLE`
- `HUMAN_REVIEW_REQUIRED`
- `PROTECTED_PATHS_TOUCHED`

## Risk Reporting Behavior

### HIGH risk

When `RISK: HIGH`, the workflow explicitly reports:

- human review required
- auto-merge not eligible

### LOW risk

When `RISK: LOW`, the workflow reports:

- safe automation candidate (advisory only)

## Authority and Boundary

This integration is governance control-layer signaling only.

- It does **not** change runtime semantics.
- It does **not** change canonical schema.
- It does **not** weaken validators.
- It does **not** modify signing or security workflows.
- It does **not** auto-merge pull requests.

Final merge authority remains human-supervised in HC:// governance workflows.
