# GitHub Ruleset Readiness

Status: advisory readiness document.

This document records the HC-TRUST-LAYER baseline for GitHub branch protection and ruleset readiness. It is public-safe, report-only, and bounded by `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.

## Boundary

The repository can provide local evidence for expected checks and protected surfaces. It cannot enforce GitHub rulesets, code-owner approvals, branch protection, or required checks through a pull request alone.

`python scripts/check_ruleset_readiness.py --format md` reports:

- expected required checks;
- protected surfaces;
- whether key workflow files exist locally;
- `human_review_required=true`;
- `advisory_only=true`;
- `truth_guarantee=false`.

The checker does not call the GitHub API, does not mutate repository settings, does not approve changes, and does not create merge authority.

## Expected required-check candidates

The current readiness checker treats these as candidate checks for human-configured GitHub rulesets:

- `validate` via `.github/workflows/validate.yml`;
- `terminology` via `.github/workflows/terminology.yml`;
- `docs-drift` via `.github/workflows/docs-drift.yml`;
- `canonical-artifacts` via `.github/workflows/canonical-artifacts.yml`;
- `governance-preflight` via `.github/workflows/governance-preflight.yml`;
- `pr-scope-guard` via `.github/workflows/pr-scope-guard.yml`.

A repository administrator must decide which checks become required in GitHub settings.

## Protected surfaces

The readiness baseline includes:

- `.github/workflows/`;
- `docs/project-control/`;
- `docs/governance/`;
- `scripts/`;
- `src/`;
- `tests/`;
- `records/`;
- `schema/`;
- `validators/`;
- `policy/`;
- `signatures/`;
- `federation/`.

These surfaces require human-supervised review. Local readiness evidence does not change governance authority.
