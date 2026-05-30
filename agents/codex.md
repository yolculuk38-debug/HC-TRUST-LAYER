# Codex Role in HC-TRUST-LAYER Agent Workspace

## Role

Codex supports HC:// delivery by executing scoped repository work:

- implement scoped repo tasks
- create PRs
- run checks
- fix CI failures
- preserve repository rules

## Boundaries

Codex must follow strict trust-kernel boundaries:

- do not change schemas unless requested
- do not change validators unless requested
- do not weaken security checks
- do not bypass human review

## Required Checks

Before proposing merge, run applicable checks:

- terminology guard
- docs drift guard
- canonical artifact guard
- JSON validity when JSON files change

Codex must preserve audit trail continuity, canonical record boundaries, and provenance expectations across all scoped edits.

## Dependency Installation Limits

Codex sandboxes may be unable to install Python test packages because upstream package access can return `403 Forbidden` or similar network policy errors. Treat those local installation failures as environment limitations, not as repository validation failures.

The repository source of truth for full runtime/API validation is GitHub Actions, where the test job installs the explicit test extra with `python -m pip install -e ".[test]"` and runs the complete runtime/API pytest scope, including `tests/runtime` and `tests/test_hc_runtime_response_contracts.py`.

When package installation is unavailable locally, Codex should still run lightweight checks that do not require network access where possible and clearly report any skipped or blocked full-test validation.
