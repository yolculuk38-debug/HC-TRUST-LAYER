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
| Source inventory support exists. | Confirmed | `scripts/hc_source_inventory.py` and `tests/test_hc_source_inventory.py` provide non-mutating Python source inventory reporting. | Use inventory output before deleting, moving, or archiving source files. |
| Record normalizer safe-write controls exist. | Confirmed | `src/normalize_records.py` defaults to no write, requires `--write`, supports `--dry-run`, and skips protected `records/archive/` and `records/verified/` paths. | Keep tests locked before changing record normalization behavior. |

## Findings requiring direct verification

| Finding | Status | Evidence gap | Next action |
| --- | --- | --- | --- |
| A record normalization script silently rewrites records. | Resolved as not matching current main behavior | The current script is `src/normalize_records.py`, not repository-root `normalize_records.py`. Current behavior uses explicit safe-write controls and protected record skipping. | Keep safety tests current. Do not remove safe-write controls. |
| Integration tests cover only a narrow example set. | Needs verification | `test_integration.py` was not found as a direct current test file during the current search. The exact current test matrix still needs inventory. | Use source/test inventory output before editing tests. |
| Genesis or historical hashes are shortened. | Partially resolved / historical context confirmed | `GENESIS_BLOCK.md` explicitly labels displayed short values as historical display prefixes, not canonical verification anchors, and preserves recovered English full-hash candidates as non-canonical candidates only. | Do not rewrite historical prefixes without original canonical source text. If full hashes are later recovered, add them only with provenance and non-canonical status unless re-hashed from source text. |
| The repository contains many stub or experimental Python files. | Needs inventory | File count and implementation status require direct source inventory. | Use the source inventory reporter, then classify results before moving or deleting files. |
| Branch count is excessive. | Needs manual confirmation | Current branch search tooling did not return a reliable branch inventory. | Verify in GitHub UI or a reliable API listing before deleting branches. |

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
