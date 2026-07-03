# HC Terminology Audit

> Status: active terminology audit note
> Scope: distinguish active HC:// / HC-TRUST-LAYER terminology from legacy historical/provenance references

## Current Active Terms

Use these terms for active public-facing and technical documentation:

- `HC://` for the active protocol language.
- `HC-TRUST-LAYER` for the current repository and technical implementation.
- `HC Trust Layer` for readable prose when not referring to the repository slug.

## Legacy / Historical Terms

These terms may appear in preserved historical context:

- legacy repository names from earlier public identity phases
- `Project Origin Record`

Historical references should not be silently deleted when they are evidence-bearing or provenance-bearing.

## Do Not Rewrite Automatically

Do not rewrite these areas without explicit review because they preserve audit history, migration context, or witness/provenance evidence:

- `witness-archive/**`
- `records/archived/**`
- `PROJECT_ORIGIN_RECORD.md`
- migration/governance evidence documents
- generated artifacts derived from canonical sources
- schema fixtures or tests that intentionally validate legacy safety behavior

## Active Documentation Cleanup Rule

If a legacy term appears in an active user-facing guide, quickstart, QR/security guide, or runtime-facing document and is not clearly historical, prefer active wording. Use `HC://`, `HC-TRUST-LAYER`, `Project Origin Record`, `witness archive`, `provenance record`, or `historical/provenance context` as appropriate. Preserve historical origin wording only when it is evidence-bearing and explicitly qualified as legacy origin, historical record, or archived provenance.

## Findings From This Pass

### Updated

- `qr/README.md`
  - Replaced active legacy QR archive wording with `HC:// archive records`.
  - Replaced active legacy public archive link wording with `official public HC:// archive links`.
  - Replaced active legacy security wording with `official HC:// archive location or approved GitHub Pages/GitHub repository address`.

### Preserved

- `witness-archive/**`
- `records/archived/**`
- `PROJECT_ORIGIN_RECORD.md`
- `docs/START_HERE.md` legacy-name explanation

These are intentionally preserved because the repository already documents them as provenance/evidence-bearing or historical context.

### Follow-Up Candidate

- `test_integration.py`
  - Header currently uses legacy project naming in a legacy test suite.
  - Suggested future change: `HC:// TRUST LAYER Legacy Integration Test Suite`.
  - This should be done in a separate small PR because it is a legacy script and should not be mixed with broad terminology cleanup.
