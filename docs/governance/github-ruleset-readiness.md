# GitHub Ruleset Readiness

Status: advisory readiness document.

This document records the HC-TRUST-LAYER baseline for GitHub settings readiness. It is public-safe, report-only, and bounded by `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.

## Boundary

The repository can provide local evidence for candidate checks and protected surfaces. It cannot enforce repository settings through a pull request alone.

`python scripts/check_ruleset_readiness.py --format md` reports:

- required-check candidates;
- not required-ready checks;
- protected surfaces;
- whether key workflow files exist locally;
- `human_review_required=true`;
- `advisory_only=true`;
- `truth_guarantee=false`.

The checker does not call the GitHub API, does not mutate repository settings, does not approve changes, and does not create merge authority.

## Required-check candidates

The current readiness checker lists these candidates:

- `terminology` via `.github/workflows/terminology.yml`;
- `docs-drift` via `.github/workflows/docs-drift.yml`;
- `canonical-artifacts` via `.github/workflows/canonical-artifacts.yml`;
- `governance-preflight` via `.github/workflows/governance-preflight.yml`.

A repository administrator must decide which checks become enforced in GitHub settings.

## Not required-ready checks

The readiness checker intentionally keeps these out of the candidate list:

- `validate` via `.github/workflows/validate.yml`;
- `pr-scope-guard` via `.github/workflows/pr-scope-guard.yml`.

These checks can still provide evidence, but they should not be copied directly into enforced configuration until they are made safe for that use.

## Protected surfaces

The readiness baseline includes:

- `.github/CODEOWNERS`;
- `CODEOWNERS`;
- `protocol-graph.json`;
- `verification-map.json`;
- `trust-kernel-index.json`;
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
