# Post-Migration Release Evidence Related Records Review

## Purpose

This report reviews the `related_records` state in `records/pending/HC-RELEASE-2026-0001.json` after PR #610 moved three historical HC:// records from `records/verified/` to `records/archived/`.

This is a documentation-only governance review. It does not modify release evidence records, records, hash files, QR artifacts, generated artifacts, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Scope

Inspected inputs:

- `records/pending/HC-RELEASE-2026-0001.json`
- `docs/governance/release-evidence-related-records-handling-plan.md`
- `records/archived/HC-TEST-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0002.md`

The review focuses only on post-migration release evidence `related_records` references. It does not assert maintainer approval, forensic certainty, production readiness, release verification, or autonomous governance finality.

## 1. Current related_records inventory

Current `related_records` status in `records/pending/HC-RELEASE-2026-0001.json` is `pending`.

| Related record ID | Current release evidence path binding | Current repository location | Inventory note |
| --- | --- | --- | --- |
| `HC-TEST-2026-0001` | `records/verified/HC-TEST-2026-0001.md` | `records/archived/HC-TEST-2026-0001.md` | Historical test record now lives under `records/archived/`; release evidence still binds to the legacy `records/verified/` path. |
| `HC-CHATGPT-2026-0001` | `records/verified/HC-CHATGPT-2026-0001.md` | `records/archived/HC-CHATGPT-2026-0001.md` | Historical workflow test record now lives under `records/archived/`; release evidence still binds to the legacy `records/verified/` path. |
| `HC-CHATGPT-2026-0002` | `records/verified/HC-CHATGPT-2026-0002.md` | `records/archived/HC-CHATGPT-2026-0002.md` | Historical demo or protocol-context record now lives under `records/archived/`; release evidence still binds to the legacy `records/verified/` path. |

The pre-migration `records/verified/` target files for these three records are not present in the current tree. The archived files are present at the expected post-migration locations.

## 2. Legacy records/verified/ references

The release evidence record still contains three legacy `records/verified/` references:

- `records/verified/HC-TEST-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0002.md`

The pre-migration handling plan explicitly identified these bindings as path-sensitive pending release evidence context and warned against silently normalizing them from `records/verified/` to `records/archived/` during archive migration.

Additional legacy context remains inside the archived historical records:

- `records/archived/HC-CHATGPT-2026-0001.md` still lists `records/verified/HC-CHATGPT-2026-0001.md` as its `Archive Path` value.
- `records/archived/HC-TEST-2026-0001.md` contains hash and QR references, but does not contain an internal `records/verified/` path.
- `records/archived/HC-CHATGPT-2026-0002.md` contains hash, QR, and timeline references, but does not contain an internal `records/verified/` path.

## 3. Migration impact

PR #610 changed the repository locations of the scoped historical records, but no release evidence records were modified. The practical result is a split between:

- **record ID continuity**, where the same three historical record IDs remain identifiable under `records/archived/`; and
- **path-binding continuity**, where `HC-RELEASE-2026-0001` still records the original `records/verified/` paths as pending release evidence context.

This state is not automatically a release evidence failure. It is a post-migration path reconciliation finding. The release evidence record remains pending, and its `related_records` paths now point to legacy locations rather than the current archived file locations.

The migration impact should be interpreted as evidence preservation plus unresolved release evidence disposition, not as proof that the historical records became current release evidence and not as proof that `HC-RELEASE-2026-0001` has been validated.

## 4. Risks of leaving related_records unchanged

Leaving `related_records` unchanged preserves review context, but it has risks:

- Reviewers or tools may attempt to resolve the `records/verified/` paths and find that the files are no longer present there.
- The release evidence record may appear stale unless the legacy path-binding rationale is documented and discoverable.
- Future release review may conflate unresolved path references with current archived-path evidence.
- Automated inventory reports may flag the release evidence record as pointing to missing files.
- New contributors may not know that the unchanged paths were intentionally preserved as pending-context references after migration.
- Coordination with hash, QR, generated artifact, and documentation reference handling may remain incomplete if the release evidence decision is deferred indefinitely.

These risks are manageable if the repository treats the current state as documented legacy pending-context evidence and keeps future reconciliation explicit and reviewable.

## 5. Risks of updating related_records

Updating `related_records` from `records/verified/` to `records/archived/` also has risks:

- A direct edit would modify a release evidence record and could appear to change the reviewed evidence context rather than only the file path.
- Silent normalization would erase the original path bindings that reviewers expected when the pending release evidence record was drafted.
- Updating the paths could imply maintainer approval, release evidence review completion, or validation status changes that have not been recorded.
- A path-only edit could diverge from hash manifests, QR artifacts, generated artifacts, and historical record-internal references that still preserve legacy context.
- Editing release evidence without old path, new path, reviewer, rationale, and status-impact notes would weaken auditability.
- Updating the record before deciding whether it remains `pending`, becomes `reviewed`, or becomes `verified` could blur release lifecycle boundaries.

Any future update should therefore be a small, explicit, human-reviewed release evidence decision rather than automatic archive-path cleanup.

## 6. Legacy evidence considerations

The legacy `records/verified/` bindings are reviewable evidence context. They show where the release evidence record pointed before historical record archival and help preserve the audit trail of the migration.

Legacy evidence handling should distinguish:

- historical records from current v0.1.0 release evidence;
- record ID continuity from path-binding continuity;
- pending release evidence context from validated release evidence;
- old `records/verified/` paths from current `records/archived/` locations;
- documentation-only review findings from maintainer approval; and
- preserved path evidence from any future archived-path correction.

The archived historical records should not be presented as current release evidence only because `HC-RELEASE-2026-0001` cites their record IDs. Likewise, unchanged legacy paths should not be treated as active current locations without explicit explanatory context.

## 7. Recommended approach

Recommended approach:

1. Preserve `records/pending/HC-RELEASE-2026-0001.json` unchanged in this PR.
2. Treat the existing `records/verified/` entries as legacy pending-context bindings after PR #610.
3. Treat the current `records/archived/` files as the current repository locations of the same historical records.
4. Keep the three referenced records classified as historical context, not active v0.1.0 release evidence.
5. Do not silently normalize `related_records` paths to `records/archived/`.
6. If maintainers later choose to update release evidence paths, do so in a separate small PR with old path, new path, reviewer, rationale, and release evidence status impact recorded.
7. Coordinate any future release evidence path update with hash handling, QR handling, generated artifact handling, and documentation reference handling.

This approach preserves evidence, keeps the review bounded, and maintains human-supervised validation boundaries.

## 8. Required future actions

Required future actions before treating release evidence `related_records` reconciliation as complete:

1. Maintainers should decide whether `HC-RELEASE-2026-0001` should preserve legacy `records/verified/` paths, add reviewed migration context elsewhere, or update `related_records` to `records/archived/` paths.
2. If paths are updated, document old path, new path, reviewer, rationale, and whether `HC-RELEASE-2026-0001` remains `pending`, becomes `reviewed`, or becomes `verified`.
3. Confirm that the three archived records remain historical records and are not promoted to current release evidence without a separate review.
4. Coordinate the release evidence decision with post-migration hash review, QR review, and generated artifact handling.
5. Keep any release evidence record edit in a separate, explicitly scoped PR because it would modify an evidence-bearing record.
6. Run terminology, docs drift, canonical artifact, and any applicable record validation checks after future release evidence documentation or record changes.
7. Preserve a clear human-supervised validation note for any final related-records disposition.

## 9. Go / No-Go recommendation

Recommendation: **Go for documentation-only merge of this review; No-Go for modifying release evidence `related_records` in this PR.**

Rationale:

- The current report documents the post-migration `related_records` state without modifying release evidence or other protected/evidence-bearing artifacts.
- The unchanged `records/verified/` paths preserve legacy pending-context bindings that should not be silently rewritten.
- The archived records are present at the post-migration locations, but the release evidence record has not been reviewed for a path update.
- Any future release evidence path update should be small, explicit, human-reviewed, and coordinated with hash, QR, generated artifact, and documentation handling.
