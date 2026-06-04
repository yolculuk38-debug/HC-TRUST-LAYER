# Archive Migration Implementation Plan

## Purpose

This plan converts the PR #607 readiness decision, **Conditionally Ready**, into a precise implementation checklist for a future historical archive migration PR.

The recommended decision for this PR is: **do not execute migration yet**. Prepare a future implementation PR only after this checklist is reviewed by maintainers.

This is report-only and documentation-only governance planning. It does not move records, modify records, modify hashes, modify QR artifacts, modify generated artifacts, modify release evidence, modify schemas, modify validators, modify workflows, modify runtime code, or alter signing, federation, policy, canonical, or trust-kernel logic.

## Scope

The future migration scope is limited to moving the three scoped historical HC:// record files from `records/verified/` to the approved archive target path, `records/archived/`, if maintainers later approve execution.

The future migration PR must preserve record content, provenance continuity, review boundaries, and auditability. It must treat all path-sensitive evidence changes as explicit human-reviewed decisions, not automatic cleanup.

## Preconditions

Before a future migration PR moves any record, maintainers should confirm that:

1. PR #607 remains the controlling readiness input and its readiness decision remains **Conditionally Ready**.
2. `records/archived/` remains the approved archive target path.
3. The scoped records are still historical records and are still intended for archival.
4. The current source paths exist and are unchanged immediately before migration.
5. Existing hash, QR, release evidence, generated artifact, and documentation reference handling plans have been reviewed together.
6. The future migration PR has an assigned human reviewer for each decision point listed below.
7. The migration PR will not fabricate hashes, QR evidence, reviewer approvals, signatures, timestamps, command output, release validation results, or production-readiness claims.
8. The migration PR will keep implementation, validation, and rollback small enough to review and revert safely.

## Exact Records in Scope

| Record ID | Current path | Future target path |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `records/verified/HC-TEST-2026-0001.md` | `records/archived/HC-TEST-2026-0001.md` |
| `HC-CHATGPT-2026-0001` | `records/verified/HC-CHATGPT-2026-0001.md` | `records/archived/HC-CHATGPT-2026-0001.md` |
| `HC-CHATGPT-2026-0002` | `records/verified/HC-CHATGPT-2026-0002.md` | `records/archived/HC-CHATGPT-2026-0002.md` |

No other record is approved by this plan for movement.

## Out-of-Scope Files

The following files and path families are out of scope for this planning PR and must remain unchanged here:

- `records/**`
- `hash/**`
- `qr/**`
- `generated/**`
- `schema/**`
- `validators/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- `policy/**`
- `.github/workflows/**`
- runtime and library implementation files under `src/**`
- release evidence records, including `records/pending/HC-RELEASE-2026-0001.json`

A future migration PR may touch some path-sensitive artifacts only after explicit maintainer approval, but this plan does not approve those changes by itself.

## Implementation Order

A future migration PR should use this order unless maintainers approve a documented alternative:

1. Reconfirm the exact migration scope and record inventory.
2. Reconfirm that `records/archived/` is the target path and that `records/archive/` is not the default migration target.
3. Record pre-migration status for the scoped records, hash manifests, QR artifacts, release evidence `related_records`, generated artifacts, and documentation references.
4. Decide hash handling before any hash file is created, updated, replaced, or deprecated.
5. Decide QR handling before any QR text or binary artifact is created, updated, replaced, redirected, or deprecated.
6. Decide release evidence `related_records` handling before changing `records/pending/HC-RELEASE-2026-0001.json`.
7. Decide generated artifact regeneration handling before regenerating `generated/audit_snapshot.json` or any generated output.
8. Decide documentation reference handling before updating references that mention `records/verified/`, `records/archive/`, or `records/archived/`.
9. Create `records/archived/` if it still does not exist and if the migration PR is approved to execute.
10. Move only the three scoped record files, preserving file contents.
11. Apply only the reviewed path-sensitive updates approved for that migration PR.
12. Regenerate generated artifacts only through approved repository tooling, if regeneration is approved.
13. Run validation commands and review all diffs manually.
14. Record human-supervised validation notes and unresolved risks before merge.

## Hash Handling Decision Point

Before migration execution, maintainers must choose and document one hash strategy:

- preserve existing legacy `.sha256` manifests only;
- preserve existing manifests and add migration-specific hash evidence;
- preserve existing manifests and reissue new archived-path manifests; or
- replace legacy manifests only with explicit maintainer approval and preserved audit context.

The recommended default is to preserve existing hash files as legacy path-bound evidence and add reviewable migration-specific hash handling only if maintainers approve it. Any new hash command must be recorded exactly as run, and new hash evidence must link back to the legacy manifest instead of erasing the earlier path binding.

## QR Handling Decision Point

Before migration execution, maintainers must choose and document one QR strategy:

- preserve existing QR artifacts as historical path-bound access evidence;
- preserve existing QR artifacts and add migration documentation;
- preserve legacy QR artifacts and add reviewed archived-path QR targets;
- deprecate legacy QR artifacts without deletion; or
- replace or overwrite legacy QR artifacts only with explicit maintainer approval and preserved audit context.

The recommended default is to treat existing QR files as legacy path-bound evidence and avoid silently overwriting them. Missing QR text artifacts for `HC-CHATGPT-2026-0002` and `HC-TEST-2026-0001` must be recorded as inventory findings, not filled by fabricated QR evidence.

## Release Evidence `related_records` Decision Point

Before migration execution, maintainers must choose and document how `records/pending/HC-RELEASE-2026-0001.json` should handle `related_records` entries that currently point to the scoped `records/verified/*.md` files.

Accepted options include preserving current paths while the release evidence remains pending, preserving current paths and adding migration documentation, updating paths after release evidence review, or linking legacy and archived context through reviewed evidence if repository conventions support that approach.

The recommended default is to leave `records/pending/HC-RELEASE-2026-0001.json` unchanged during pre-migration planning and treat any later path update as a release evidence review decision.

## Generated Artifact Regeneration Decision Point

Before migration execution, maintainers must decide whether generated artifacts remain legacy generated evidence or are regenerated after approved migration steps.

The recommended default is to leave `generated/audit_snapshot.json` unchanged during planning and regenerate generated artifacts only after record movement and reviewed path-sensitive updates are complete. Any regeneration must use approved repository tooling, never hand editing, and must record source inputs, command used, reviewer, rationale, validation results, and manual diff review.

## Documentation Reference Update Decision Point

Before migration execution, maintainers must decide how documentation references to `records/verified/`, `records/archive/`, and `records/archived/` should be handled.

Documentation references must be reviewed by intent. Examples, historical notes, current path descriptions, target-path guidance, and compatibility references should not be blindly replaced. Any future documentation update should identify whether each changed reference is:

- a current-state reference that must change after migration;
- a historical reference that should remain unchanged;
- a target-path reference that already points to `records/archived/`;
- a compatibility reference for `records/archive/`; or
- an example that should be updated only if the example is meant to describe post-migration state.

## Validation Commands and Checks

A future migration PR should run at least the following checks, adjusting only if maintainers document why a command is unavailable or superseded:

```sh
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
python scripts/check_pr_scope.py
```

The migration PR should also run any repository validators or migration-specific checks required by the changed files. If generated artifacts are regenerated, the exact generator command must be recorded and followed by manual review of generated diffs.

## Human-Supervised Review Requirements

Human-supervised review is required before migration execution and before merge of any implementation PR. Review must confirm:

- the migration moves only the three scoped historical records;
- the record contents are preserved;
- hash handling is approved and documented;
- QR handling is approved and documented;
- release evidence `related_records` handling is approved and documented;
- generated artifact handling is approved and documented;
- documentation reference updates are intent-reviewed;
- validation commands were run and results are recorded;
- unresolved findings are explicitly documented; and
- no production readiness, forensic certainty, truth finality, live federation guarantee, autonomous governance finality, fabricated evidence, or fabricated approval claim is introduced.

Agents and automation may prepare inventories, suggest commands, and draft reviewable documentation, but they must not treat the migration as accepted without maintainer review.

## Rollback Plan

A future migration PR must remain small enough to revert safely. If migration validation fails or reviewers reject any decision point, the rollback plan should be:

1. Revert moved scoped records from `records/archived/` back to their original `records/verified/` paths.
2. Revert any migration-specific hash, QR, release evidence, generated artifact, and documentation changes made in that PR.
3. Remove `records/archived/` only if it was created by the migration PR and is empty after rollback.
4. Re-run the same validation commands used for the migration PR.
5. Record the failed decision point, rollback commit, and remaining blocker in governance documentation before attempting a new migration PR.

Rollback must not delete legacy evidence, fabricate replacement evidence, or weaken guards to make checks pass.

## Go / No-Go Checklist for Future Migration PR

Use this checklist before opening or merging a future migration implementation PR:

- [ ] PR #607 **Conditionally Ready** decision has been reviewed.
- [ ] `records/archived/` is still the approved target path.
- [ ] The future PR moves only the three scoped records listed in this plan.
- [ ] No additional records are moved, edited, deleted, or normalized.
- [ ] Hash handling option is selected, reviewed, and documented.
- [ ] QR handling option is selected, reviewed, and documented.
- [ ] Missing QR artifact findings are documented without fabricated evidence.
- [ ] `records/pending/HC-RELEASE-2026-0001.json` `related_records` handling is selected, reviewed, and documented.
- [ ] Generated artifact regeneration approach is selected, reviewed, and documented.
- [ ] Documentation references are reviewed by intent before any update.
- [ ] Generated artifacts are regenerated only through approved tooling, if regeneration is approved.
- [ ] Validation commands and any migration-specific checks are run and recorded.
- [ ] Human-supervised reviewer approval is recorded.
- [ ] Rollback path is clear and limited to the migration PR.
- [ ] No-Go if any required decision point remains unresolved.
- [ ] No-Go if validation fails and maintainers have not documented the failure as an accepted blocker.
- [ ] No-Go if the PR would fabricate hashes, QR evidence, release validation results, signatures, approvals, timestamps, command output, or production-readiness claims.

Until every Go item is satisfied and every No-Go condition is resolved, migration should remain unexecuted.
