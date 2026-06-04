# Archive Migration Readiness Review

## Executive Summary

This report reviews readiness for a future historical archive migration of the following HC:// records from `records/verified/` to the approved archive target path:

- `HC-TEST-2026-0001`
- `HC-CHATGPT-2026-0001`
- `HC-CHATGPT-2026-0002`

This is a report-only governance review. It does not move files, modify records, modify hashes, modify QR artifacts, modify generated artifacts, modify release evidence, modify schemas, modify validators, modify workflows, or modify runtime behavior.

Readiness decision: **Conditionally Ready**.

The archive target path decision has been resolved in favor of `records/archived/`, and separate handling plans now exist for hash manifests, QR artifacts, release evidence `related_records`, and generated audit artifacts. However, the repository still contains path-sensitive bindings to `records/verified/`, and those bindings must be handled in a later maintainer-approved migration PR before any record movement is executed.

Migration should not be executed today without an implementation PR that coordinates record movement, path-sensitive evidence handling, generated artifact regeneration, validation, and human-supervised review.

## Reviewed Materials

Governance review inputs:

- `docs/governance/historical-record-archive-migration.md`
- `docs/governance/historical-record-archive-migration-review-pr601.md`
- `docs/governance/archive-target-path-decision.md`
- `docs/governance/historical-record-hash-handling-plan.md`
- `docs/governance/historical-record-qr-handling-plan.md`
- `docs/governance/release-evidence-related-records-handling-plan.md`
- `docs/governance/generated-artifact-handling-plan.md`

Inspected repository artifacts:

- `records/verified/HC-TEST-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0002.md`
- `hash/`
- `qr/`
- `generated/audit_snapshot.json`
- `records/pending/HC-RELEASE-2026-0001.json`

## Findings

### 1. Confirmed Blockers

The following blockers remain confirmed at review time:

1. **Historical records remain in `records/verified/`.** The three scoped historical records are still present at their current verified paths and have not been moved.
2. **Hash manifests remain path-bound to `records/verified/`.** Existing hash files bind each scoped record ID to its current `records/verified/*.md` path:
   - `hash/HC-TEST-2026-0001.sha256`
   - `hash/HC-CHATGPT-2026-0001.sha256`
   - `hash/HC-CHATGPT-2026-0002.sha256`
3. **At least one QR text artifact remains path-bound to `records/verified/`.** `qr/HC-CHATGPT-2026-0001.txt` points to a GitHub URL under `records/verified/`.
4. **QR artifact inventory is incomplete for the scoped records.** `qr/HC-CHATGPT-2026-0002.txt` is referenced by `records/verified/HC-CHATGPT-2026-0002.md` but is not present in `qr/`. No scoped QR text artifact was found for `HC-TEST-2026-0001`.
5. **Pending release evidence still references `records/verified/`.** `records/pending/HC-RELEASE-2026-0001.json` lists all three scoped historical records in `related_records` using `records/verified/*.md` paths.
6. **Generated audit evidence still reflects the current repository state.** `generated/audit_snapshot.json` includes the scoped historical record IDs and lists `records/verified/` and `records/archived/` as source directories.
7. **Documentation still contains intentional and example `records/verified/` references.** These references require intent-based review during migration and should not be blindly replaced.
8. **No migration implementation has been executed.** This review did not move records or update dependent artifacts, so migration remains blocked until a separate implementation PR handles the path-sensitive evidence chain.

### 2. Resolved Blockers

The following planning blockers appear resolved or materially narrowed by the reviewed governance documentation:

1. **Archive target path ambiguity is resolved.** Future historical record archival should use `records/archived/`; `records/archive/` remains legacy/current repository material unless maintainers approve a later compatibility change.
2. **Hash handling has a dedicated plan.** The repository now distinguishes legacy path-bound hash evidence from any future reissued or migration-specific hash evidence and prohibits fabricated hash updates.
3. **QR handling has a dedicated plan.** The repository now distinguishes existing QR target artifacts, missing QR text artifacts, possible deprecation, possible regeneration, and historical QR evidence preservation.
4. **Release evidence `related_records` handling has a dedicated plan.** The repository now treats pending release evidence path changes as review decisions rather than automatic cleanup.
5. **Generated artifact handling has a dedicated plan.** The repository now requires generated artifacts to remain unedited during planning and to be regenerated only through approved tooling after migration steps are defined.
6. **Record classification is stable for migration planning.** The scoped records are treated as preserved historical artifacts, not current release evidence and not active v0.1.0 public QR targets.

### 3. Remaining Blockers

Before migration can be executed, maintainers must still resolve the following implementation blockers:

1. Decide the exact hash preservation strategy: retain legacy manifests, reissue manifests for archived paths, add a migration manifest, or use an explicitly documented combination.
2. Decide the exact QR strategy: retain as historical evidence, deprecate stale targets, redirect if supported, regenerate if approved, or document missing artifacts without fabrication.
3. Decide whether and when `records/pending/HC-RELEASE-2026-0001.json` `related_records` paths should change, and record the reviewer/rationale if changed.
4. Identify the approved command or tooling path for regenerating `generated/audit_snapshot.json` after migration.
5. Define which documentation references to `records/verified/` are stale migration references versus intentional examples or current-state references.
6. Confirm whether `records/archived/` exists or must be created by the migration PR without disrupting current `records/archive/` material.
7. Define the validation checklist for the migration PR, including terminology, docs drift, canonical artifact checks, validators, and migration-specific path checks.
8. Record human-supervised validation after migration diffs are generated and before treating the migration as accepted.

### 4. Migration Readiness Status

Status: **Conditionally Ready**.

The repository is conditionally ready to prepare a narrowly scoped migration implementation PR because the major governance decisions and handling plans now exist. It is **not ready for immediate execution today** because path-sensitive records, hashes, QR artifacts, release evidence references, generated artifacts, and documentation references remain unchanged.

### 5. Ready / Not Ready / Conditionally Ready

Decision: **Conditionally Ready**.

Conditions:

- The migration must occur in a separate maintainer-approved implementation PR.
- The migration PR must preserve record content and provenance.
- The migration PR must not fabricate hashes, QR evidence, reviewer approvals, validation results, signatures, release status, or production-readiness claims.
- The migration PR must coordinate hash, QR, release evidence, generated artifact, and documentation updates in the documented order.
- The migration PR must include validation output and human-supervised review notes before merge.

### 6. Required Actions Before Migration

Before any historical record is moved, maintainers should complete these actions:

1. Confirm `records/archived/` as the implementation target in the migration PR.
2. Preserve the exact current content of the three historical records before movement.
3. Inventory and record current hash manifest bindings.
4. Choose and document the hash handling approach.
5. Inventory current QR artifacts and missing QR text artifacts.
6. Choose and document the QR handling approach.
7. Decide whether pending release evidence `related_records` should remain as legacy pending-context references or be updated after record movement.
8. Identify the approved generator command for `generated/audit_snapshot.json`.
9. Review documentation references to `records/verified/` by intent.
10. Move records only after dependent reference handling is planned.
11. Regenerate generated artifacts only through approved tooling, not by hand.
12. Run required checks and record results.
13. Perform human-supervised validation of the full migration diff.

### 7. Risks If Migration Is Executed Today

If migration is executed today without completing the remaining actions, the repository risks:

- breaking hash path bindings while preserving content hashes but changing manifest path semantics;
- leaving QR targets stale or unverifiable from the repository path shown to users;
- silently changing pending release evidence context without reviewer rationale;
- producing generated artifact drift or erasing historical generated evidence;
- mixing `records/archive/` and `records/archived/` semantics in future tooling or documentation;
- making documentation examples inconsistent with record locations;
- creating the appearance of completed validation without human-supervised review; and
- weakening provenance continuity by treating path cleanup as a mechanical move rather than an evidence-preserving migration.

### 8. Recommended Migration Order

Use this order for the future implementation PR:

1. Confirm `records/archived/` as the migration target and document that `records/archive/` remains legacy/current material.
2. Record pre-migration inventory for the three scoped records, hash manifests, QR artifacts, release evidence references, generated audit snapshot, and documentation references.
3. Preserve record content and provenance before movement.
4. Decide and document hash handling.
5. Decide and document QR handling.
6. Decide and document release evidence `related_records` handling.
7. Review documentation references by intent and prepare only necessary updates.
8. Move the three historical records to `records/archived/` in the approved migration PR.
9. Apply approved hash, QR, release evidence, and documentation updates.
10. Regenerate `generated/audit_snapshot.json` through approved tooling.
11. Run validators and required checks.
12. Manually review the complete diff for unintended record, hash, QR, generated, schema, validator, workflow, or runtime changes.
13. Record human-supervised validation before merge.

### 9. Rollback Requirements

The future migration PR should remain small enough to revert safely. Rollback should require:

1. Restoring the three historical records to their pre-migration `records/verified/` paths if the migration is reverted.
2. Restoring any changed hash manifests or migration hash evidence to the pre-migration state.
3. Restoring any changed QR artifacts or QR deprecation notes to the pre-migration state.
4. Restoring `records/pending/HC-RELEASE-2026-0001.json` if `related_records` paths were changed.
5. Restoring the pre-migration generated audit snapshot or regenerating it from the restored tree using approved tooling.
6. Reverting documentation updates that depended on the migration.
7. Re-running required checks after rollback.
8. Recording rollback rationale and human-supervised validation.

### 10. Final Recommendation

Proceed with a future migration implementation PR only after maintainers approve the remaining path-sensitive handling decisions. The current state is suitable for planning and scoped implementation preparation, but not for immediate migration execution.

Final recommendation: **Conditionally Ready for a separate maintainer-approved migration PR; not ready for migration execution today.**

## Risk Assessment

Overall risk level: **Medium until migration execution; High if executed without the required actions.**

The highest-risk areas are path-sensitive provenance bindings and evidence continuity:

- Hash manifests currently include `records/verified/` paths.
- QR text artifacts are incomplete and at least one target points to `records/verified/`.
- Pending release evidence includes `records/verified/` `related_records` paths.
- Generated audit evidence reflects the current pre-migration repository state.
- Documentation includes mixed current-state, example, and migration-planning references.

These risks are manageable if the migration is kept small, reviewed by humans, validated through repository checks, and executed only after hash, QR, release evidence, generated artifact, and documentation handling decisions are explicit.

## Readiness Decision

**Conditionally Ready.**

This review supports preparing a future migration PR. It does not approve immediate migration execution. The future migration PR must be evidence-preserving, human-supervised, and limited to the documented scope.

## Next Actions

1. Maintainers should approve the exact migration scope and confirm the three historical records included.
2. Maintainers should choose hash, QR, release evidence, generated artifact, and documentation handling options.
3. The migration PR should implement only the approved path-sensitive changes.
4. The migration PR should run terminology, docs drift, canonical artifact, validator, and migration-specific checks.
5. Reviewers should manually inspect all provenance-bearing and generated diffs before merge.
