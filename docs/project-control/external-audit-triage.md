# External Audit Triage

Status: advisory review intake.

This note records an external review input and separates repository-confirmed findings from items that still require direct GitHub evidence. It does not approve, reject, merge, release, certify, or change governance authority.

## Confirmed repository evidence

| Finding | Status | Evidence basis | Next action |
| --- | --- | --- | --- |
| A local verification package core exists. | Confirmed | `src/hc_trust/verification_package.py` implements local manifest and SHA-256 package checks. | Continue treating it as the current working core. |
| The package core is local-only and advisory-only. | Confirmed | The implementation returns `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`. | Preserve this boundary. |
| The CLI has a `verify-package` command. | Confirmed | `src/hc_trust/cli.py` calls `verify_verification_package()` and supports `--summary`. | Keep CLI docs aligned with examples. |
| The signature/witness fixture package is covered by tests. | Confirmed | `tests/test_verification_package_sample.py` covers the local fixture package and keeps `signatures_verified=false` and `witnesses_verified=false`. | Do not treat the fixture as real signing or witness authority. |

## Findings requiring direct verification

| Finding | Status | Evidence gap | Next action |
| --- | --- | --- | --- |
| A record normalization script silently rewrites records. | Not confirmed in this triage | `normalize_records.py` was not found at repository root during the current check. | Search repository paths and workflows before opening any fix PR. |
| Integration tests cover only a narrow example set. | Needs verification | The exact current test matrix was not fully audited in this triage. | Add a test-coverage inventory before changing tests. |
| Genesis or historical hashes are shortened. | Needs verification | The exact source file and expected full hash source were not verified in this triage. | Create a separate evidence note before editing historical records. |
| The repository contains many stub or experimental Python files. | Needs verification | File count and implementation status require direct source inventory. | Create an inventory-only PR before moving or deleting files. |
| Branch count is excessive. | Needs manual confirmation | Branch search tooling did not return branch inventory in this triage. | Use GitHub UI or a reliable API listing before deleting branches. |

## Operating decision

Do not start with deletion, archival, or protected-path changes. The next safe action is an inventory-only PR that classifies source files as one of:

- active implementation;
- test support;
- documentation support;
- experimental;
- parked;
- needs review.

## Boundaries

This triage is advisory-only. Human maintainers retain final authority. No protected paths are changed by this note.
