# External Audit Triage

Status: advisory review intake.

This note records outside review findings and keeps them separated from repository-confirmed facts. It does not approve, reject, merge, release, certify, or change governance authority.

## Confirmed repository evidence

| Finding | Status | Evidence basis | Next action |
| --- | --- | --- | --- |
| Local verification package core exists. | Confirmed | `src/hc_trust/verification_package.py` implements local manifest and SHA-256 package checks. | Treat it as the current working core. |
| Package core boundary is advisory. | Confirmed | The implementation returns `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`. | Preserve this boundary. |
| CLI has `verify-package`. | Confirmed | `src/hc_trust/cli.py` calls `verify_verification_package()` and supports `--summary`. | Keep docs aligned. |
| Fixture package has tests. | Confirmed | `tests/test_verification_package_sample.py` keeps fixture signing and witness authority flags false. | Do not treat fixtures as real authority. |
| Source inventory support exists. | Confirmed | `scripts/hc_source_inventory.py` and `tests/test_hc_source_inventory.py` provide non-mutating source inventory reporting. | Use inventory before source cleanup. |
| Record normalizer safe controls exist. | Confirmed | `src/normalize_records.py` defaults to no write, requires `--write`, supports `--dry-run`, and skips protected record areas. | Keep tests locked. |
| Root integration script exists. | Confirmed | `test_integration.py` exists at repository root and has a separate status note. | Review coverage against current files. |

## Findings still requiring care

| Finding | Status | Evidence basis | Next action |
| --- | --- | --- | --- |
| Record normalizer risk. | Resolved for current main behavior | Current script uses explicit safe-write controls. | Do not remove those controls. |
| Integration coverage may be narrow. | Partially corrected / needs broader review | Root script exists, but full coverage still requires inventory. | Inventory `tests/` and root-level integration scripts before changing tests. |
| Genesis or historical hashes are shortened. | Historical context confirmed | `PROJECT_ORIGIN_RECORD.md` labels short values as historical display prefixes and not canonical verification anchors. | Do not rewrite without original canonical source text. |
| Source tree may include parked or experimental files. | Needs inventory | File count and implementation status require source inventory. | Use source inventory output first. |
| Branch count may be high. | Needs manual confirmation | Current branch search tooling did not return reliable inventory. | Verify in GitHub UI or reliable branch listing. |

## Operating decision

Start with inventory and small scoped PRs. Do not begin with broad cleanup or protected-path changes.

## Boundaries

This triage is advisory-only. Human maintainers retain final authority. No protected paths are changed by this note.
