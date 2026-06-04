# Archive Target Path Decision

## Purpose

This note resolves the `records/archive/` versus `records/archived/` path ambiguity for historical HC:// records before any historical record migration, hash update, QR update, generated artifact regeneration, or release evidence path change.

This is documentation-only governance guidance. It does not move records, create archive directories, modify hashes, modify QR artifacts, regenerate generated artifacts, modify records, modify schemas, modify validators, modify workflows, modify runtime code, or alter signing, federation, policy, or trust-kernel logic.

## Decision

`records/archived/` is the approved migration target for future historical record archival.

`records/archive/` is a legacy/current repository path that exists today, but it is not the approved target for future historical record migration unless maintainers intentionally approve a later compatibility or tooling change.

Historical records currently located outside `records/archived/` must remain in place until a separate maintainer-approved migration PR updates path-sensitive references in the required order.

## Rationale

Choosing `records/archived/` is safer for future tooling and audit consistency because current repository references already treat `archived` as the lifecycle state and path family for archived canonical records.

Known alignment points include:

- `generated/audit_snapshot.json` lists `records/archived/` as a source directory.
- Canonical artifact checks and verification package export logic reference `records/archived/` as an expected canonical record directory.
- Policy and verification package documentation already use `records/archived/` patterns.
- Release evidence lifecycle language uses `archived` as the record lifecycle state.

Using the lifecycle-aligned plural path avoids introducing a second active archive spelling into future generators, validators, audit snapshots, policy references, and review checklists. It also reduces the risk that maintainers or agents silently normalize `archive` and `archived` differently during migration.

## Existing Path Ambiguity

The repository currently contains `records/archive/`. The `records/archived/` directory is not present in the current tree, but multiple generated, policy, documentation, and tooling references already name `records/archived/`.

The ambiguity is therefore not evidence that both paths are equally approved migration targets. It is a pre-migration blocker that must be resolved before records move or path-sensitive evidence changes.

For PR #602, the resolution is:

- `records/archived/` is the approved target path for future historical record migration.
- `records/archive/` is legacy/current repository material and should not receive new historical record migrations by default.
- Existing `records/archive/` references should be reviewed by intent before any update, not replaced blindly.

## Compatibility Notes

Existing references to `records/archive/` remain compatibility references until a later maintainer-approved cleanup or migration plan addresses them. They may describe historical repository structure, legacy examples, or current compatibility behavior.

Existing references to `records/archived/` remain valid as target-path guidance where they describe approved archival state, source directory expectations, or future migration planning.

Future tooling should not silently treat `records/archive/` and `records/archived/` as interchangeable. If compatibility support for both paths is required, it should be documented explicitly, tested, and reviewed as a separate change before any record movement.

## Non-Goals

This decision does not:

- Move records.
- Create `records/archived/`.
- Delete or modify `records/archive/`.
- Reissue hashes or modify hash manifests.
- Update, regenerate, redirect, or deprecate QR artifacts.
- Regenerate `generated/audit_snapshot.json`.
- Modify canonical records, schemas, validators, runtime code, workflows, signing logic, federation logic, policy files, or trust-kernel logic.
- Claim production readiness, forensic certainty, truth finality, live federation guarantees, or autonomous governance finality.

## Pre-Migration Implications

Before any historical record migration, maintainers should use `records/archived/` as the planned destination and complete a path-sensitive impact review for:

- hash manifests that currently bind evidence to existing paths;
- QR artifacts and public-facing references that may point to existing paths;
- release evidence `related_records` entries;
- generated audit snapshots and source directory lists;
- documentation examples that mention `records/verified/`, `records/archive/`, or `records/archived/`; and
- tooling assumptions in generators, validators, package export logic, and policy evaluation.

No historical record should be moved until the migration PR defines how each path-sensitive artifact will be preserved, updated, regenerated, deprecated, or retained as legacy evidence.

## Future Migration Requirement

A future historical record migration PR must:

1. Use `records/archived/` as the target path unless maintainers approve a superseding documented decision.
2. Preserve record content and provenance.
3. Explain how existing `records/archive/` compatibility references are handled.
4. Update or reissue path-sensitive hash material only through reviewable maintainer-approved steps.
5. Update, deprecate, or retain QR artifacts with explicit rationale.
6. Review release evidence links before changing `related_records` paths.
7. Regenerate generated artifacts with repository-approved commands instead of editing them by hand.
8. Run terminology, docs drift, canonical artifact, and relevant validation checks.
9. Record human-supervised validation before treating the migration as accepted.
