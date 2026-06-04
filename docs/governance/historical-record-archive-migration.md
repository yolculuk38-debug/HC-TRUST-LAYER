# Historical Record Archive Migration Readiness

## Purpose

This document defines what must be reviewed and updated before moving historical verified records from `records/verified/` to `records/archived/`.

This document does not move records, delete records, rewrite provenance, or change hashes, QR targets, generated artifacts, schemas, validators, workflows, or runtime behavior. It is a readiness note for a later maintainer-approved archive migration plan.

## Scope

This readiness note applies to the following historical verified records:

- `HC-TEST-2026-0001`
- `HC-CHATGPT-2026-0001`
- `HC-CHATGPT-2026-0002`

## Current Classification

| Record | Classification |
| --- | --- |
| `HC-TEST-2026-0001` | `historical_test_record` |
| `HC-CHATGPT-2026-0001` | `historical_workflow_test_record` |
| `HC-CHATGPT-2026-0002` | `historical_demo_or_protocol_context_record` |

These records are preserved historical artifacts. They are not current release evidence, are not active v0.1.0 public QR targets, and must not be deleted.

## Migration Blockers

The post-PR #599 reference audit identified path-sensitive references that block immediate archive migration:

- Hash manifests still point to `records/verified/`.
- QR target material still points to `records/verified/`.
- `records/pending/HC-RELEASE-2026-0001.json` `related_records` entries still point to `records/verified/`.
- `generated/audit_snapshot.json` references the records.
- Documentation examples still use `records/verified/` paths.
- `qr/HC-CHATGPT-2026-0002.txt` appears missing.
- `records/archive` versus `records/archived` path ambiguity must be resolved before migration.

## Required Migration Order

A later archive migration PR should use the following safe order:

1. Confirm the archive target path.
2. Preserve current record content.
3. Update or reissue hash manifests.
4. Update or deprecate QR target files.
5. Update release evidence `related_records` paths if maintainers approve.
6. Update stale documentation examples.
7. Move records only after references are planned.
8. Regenerate `generated/audit_snapshot.json`.
9. Run validation and manually review generated diffs.

## Archive Path Decision

Use `records/archived/` as the preferred target unless maintainers intentionally update tooling to support `records/archive/`.

The archive path choice must match generator and audit tooling before records are moved. Maintainers should resolve the path decision before any migration PR changes record locations or path-sensitive references.

## Non-Goals

This document does not:

- Create a public verifier.
- Claim production readiness.
- Claim security certification.
- Claim truth finality.
- Claim forensic certainty.
- Change release evidence status.
- Change historical record status by itself.

## Rules

- Do not delete historical records.
- Do not fabricate hashes.
- Do not fabricate QR evidence.
- Do not rewrite provenance.
- Do not move records without a maintainer-approved migration plan.
- Do not treat these records as current release evidence.
- Do not use these records as active v0.1.0 public QR targets.

## Future Archive Migration Checklist

Use this checklist for the later archive migration PR:

- [ ] Archive target path approved.
- [ ] Hash manifests updated or reissued.
- [ ] QR targets updated or deprecated.
- [ ] `HC-RELEASE-2026-0001` `related_records` reviewed.
- [ ] Documentation examples reviewed.
- [ ] `generated/audit_snapshot.json` regenerated.
- [ ] Stale `records/verified/` references checked.
- [ ] Validation checks passed.
- [ ] Human-supervised validation recorded.
