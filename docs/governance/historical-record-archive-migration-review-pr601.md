# Historical Record Archive Migration Blocker Review

## Purpose

This report reviews historical archive migration readiness after PR #600 before any record, hash, QR, generated artifact, or release evidence path is changed.

This is report-only governance documentation. It does not move records, modify hashes, modify QR artifacts, regenerate artifacts, change schemas, change validators, change workflows, change runtime behavior, or alter trust-kernel logic.

## Reviewed Scope

- `docs/governance/historical-record-archive-migration.md`
- `docs/governance/historical-record-classification.md`
- `docs/governance/release-evidence-lifecycle.md`
- `records/pending/HC-RELEASE-2026-0001.json`
- `hash/`
- `qr/`
- `generated/audit_snapshot.json`
- Documentation references to `records/verified/`

## Confirmed Blockers

- Historical records remain in `records/verified/` and are still path-sensitive review artifacts.
- Hash manifests for `HC-TEST-2026-0001`, `HC-CHATGPT-2026-0001`, and `HC-CHATGPT-2026-0002` still bind hashes to `records/verified/*.md` paths.
- `qr/HC-CHATGPT-2026-0001.txt` still points to `records/verified/HC-CHATGPT-2026-0001.md`.
- QR text artifacts for `HC-TEST-2026-0001` and `HC-CHATGPT-2026-0002` are not present in `qr/`, so the migration cannot assume all historical QR targets have matching text artifacts.
- `records/pending/HC-RELEASE-2026-0001.json` still lists the three historical records in `related_records` using `records/verified/*.md` paths.
- `generated/audit_snapshot.json` includes the historical record IDs and lists `records/verified/` and `records/archived/` as source directories.
- Documentation still contains intentional and example `records/verified/` references that must be reviewed before migration.
- The repository contains `records/archive/`, while several governance and generated references prefer or mention `records/archived/`; this path ambiguity remains unresolved.

## Missing Blockers To Add Before Migration

- Decide whether `records/archive/` remains a legacy/current path or whether `records/archived/` is the approved migration target.
- Confirm whether tooling expects `records/archive/`, `records/archived/`, or both before moving any files.
- Define whether historical hash manifests should be reissued with archived paths, retained as legacy path evidence, or replaced by a migration-specific manifest.
- Define whether old QR targets should be deprecated, redirected, regenerated, or retained as historical evidence.
- Decide whether `HC-RELEASE-2026-0001` should continue referencing historical records while pending, and whether path updates require reviewer evidence.
- Identify documentation examples that are canonical guidance versus illustrative examples before normalizing paths.
- Define the expected generated artifact regeneration command and review boundary for `generated/audit_snapshot.json`.

## Path Ambiguity: `records/archive` vs `records/archived`

`records/archive/` exists in the repository. `generated/audit_snapshot.json` lists `records/archived/` as a source directory, and governance documentation currently prefers `records/archived/` unless maintainers intentionally update tooling for `records/archive/`.

Do not silently normalize this difference. Maintainers should approve one target path and then align documentation, generators, validators, and audit expectations before any record migration.

## Impact Review

### Hash Impact

Moving historical records changes the path component recorded in existing `.sha256` manifests even if record content bytes remain unchanged. Migration must not fabricate replacement hashes. Maintainers should decide whether to reissue manifests, preserve old manifests as legacy evidence, or add a migration manifest that explains the path transition.

### QR Impact

At least one QR text artifact points directly to a `records/verified/` GitHub URL. A record move could create a stale QR target unless maintainers deprecate, redirect, or regenerate the QR target. Missing QR text artifacts for the other two historical records should be treated as an inventory finding, not as proof that no QR impact exists.

### Release Evidence `related_records` Impact

`HC-RELEASE-2026-0001` is pending release evidence and still references the three historical records by `records/verified/*.md` path. Updating those references should be handled with release evidence review because it changes recorded evidence context even if the record IDs stay the same.

### Generated Artifact Impact

`generated/audit_snapshot.json` includes historical record IDs and source directory paths. It should not be edited by hand for this review. After any approved migration, it should be regenerated with the repository-approved generator and manually reviewed for unexpected scope changes.

### Documentation Impact

Documentation references to `records/verified/` include boundary guidance, examples, Explorer material, verification package material, automation notes, and governance notes. These references should be reviewed by intent. Active path guidance should be updated only after the archive target path is approved; examples may need narrower wording instead of blanket replacement.

## Safe Migration Order

1. Approve the archive target path and document the decision.
2. Inventory all path-sensitive references for the three historical records.
3. Decide hash handling for legacy and migrated paths.
4. Decide QR deprecation, redirect, or regeneration handling.
5. Decide whether pending release evidence `related_records` should be updated before or after record movement.
6. Update documentation references that would otherwise mislead reviewers.
7. Move records only after reference handling is approved.
8. Reissue or preserve hash material according to the approved plan.
9. Update or deprecate QR artifacts according to the approved plan.
10. Regenerate generated artifacts using approved tooling.
11. Run terminology, docs drift, canonical artifact, validator, and migration-specific checks.
12. Record human-supervised validation and remaining uncertainty.

## Items That Must Be Updated Before Archive Migration

- Archive target path decision and rationale.
- Hash migration or preservation plan.
- QR migration, deprecation, or preservation plan.
- Release evidence `related_records` update plan for `HC-RELEASE-2026-0001`.
- Documentation reference review list for `records/verified/` examples and guidance.
- Generated artifact regeneration command and expected review boundary.
- Validation checklist for the migration PR.

## Items That Must Not Be Touched Yet

- Historical records in `records/verified/`.
- Hash manifests in `hash/`.
- QR artifacts in `qr/`.
- `generated/audit_snapshot.json`.
- `records/pending/HC-RELEASE-2026-0001.json`.
- Schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, and trust-kernel logic.

## Review Conclusion

Archive migration is not ready to execute. The blockers are mostly confirmed, and the most important unresolved decision is the archive target path. The next safe step is a maintainer-approved migration plan that resolves path naming, hash handling, QR handling, release evidence references, generated artifact regeneration, and documentation updates before any provenance-bearing artifact is moved or rewritten.
