# Release Evidence Related Records Handling Plan

## Purpose

This plan defines how `records/pending/HC-RELEASE-2026-0001.json` `related_records` references should be reviewed before any historical HC:// records move from `records/verified/` to `records/archived/`.

It is documentation-only governance guidance for archive migration planning. It does not modify release evidence records, move records, modify records, modify hash files, modify QR artifacts, regenerate generated artifacts, change schemas, change validators, change workflows, change runtime behavior, or alter signing, federation, policy, or trust-kernel logic.

Migration is still not ready to execute.

## Scope

This plan applies to the current pending v0.1.0 release evidence record:

- `records/pending/HC-RELEASE-2026-0001.json`

It focuses only on the `related_records` entries that currently bind the pending release evidence context to historical records under `records/verified/`:

- `records/verified/HC-TEST-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0002.md`

This plan complements the historical record classification, archive migration readiness, blocker review, archive target path decision, hash handling plan, and QR handling plan. Hash handling, QR handling, generated artifact regeneration, and record movement remain separate review areas.

## Current related_records bindings

Current `related_records` status in `records/pending/HC-RELEASE-2026-0001.json` is `pending`.

| Related record ID | Current path binding | Current handling note |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `records/verified/HC-TEST-2026-0001.md` | Pending release evidence context that points to a historical test record. |
| `HC-CHATGPT-2026-0001` | `records/verified/HC-CHATGPT-2026-0001.md` | Pending release evidence context that points to a historical workflow test record. |
| `HC-CHATGPT-2026-0002` | `records/verified/HC-CHATGPT-2026-0002.md` | Pending release evidence context that points to a historical demo or protocol-context record. |

These path bindings are review-relevant evidence context. They should not be silently normalized from `records/verified/` to `records/archived/` during archive migration planning.

## Path-sensitive release evidence risk

`related_records` entries are path-sensitive because they record where release reviewers expected supporting context to live when the pending release evidence record was drafted. Moving the historical records without reviewing those references can create ambiguity about whether the release evidence record still points to the original context, an archived successor path, or a silently rewritten interpretation.

The risk is not limited to record identity. Even if the record IDs remain unchanged, changing the path text may affect:

- reviewer expectations for pending release evidence;
- audit trail continuity for the original release evidence context;
- coordination with hash manifests that still bind digests to `records/verified/` paths;
- coordination with QR artifacts that may still reference `records/verified/` paths;
- generated audit snapshot interpretation; and
- later decisions about whether `HC-RELEASE-2026-0001` remains `pending`, becomes `reviewed`, or becomes `verified`.

A future migration must therefore treat `related_records` path changes as release evidence review decisions, not as automatic path cleanup.

## Relationship to historical record classification

The three referenced records are classified as historical records and are not current v0.1.0 release evidence:

| Record ID | Historical classification | Active release evidence handling |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `historical_test_record` | Historical context only; not active release evidence. |
| `HC-CHATGPT-2026-0001` | `historical_workflow_test_record` | Historical context only; not active release evidence. |
| `HC-CHATGPT-2026-0002` | `historical_demo_or_protocol_context_record` | Historical context only; not active release evidence. |

The current pending release evidence record may cite these records as related context, but that citation does not convert the historical records into current release evidence. Archive migration planning should preserve that distinction.

## Preservation options

Maintainers may choose one of the following approaches in a later migration-specific PR:

1. **Preserve current `related_records` paths while the release evidence record remains pending.** Keep the `records/verified/` paths unchanged and document that they are legacy pending-context references until release evidence review decides otherwise.
2. **Preserve current paths and add separate migration documentation.** Keep `HC-RELEASE-2026-0001` unchanged, then document old path, proposed new path, reviewer, rationale, and release evidence status in a migration note.
3. **Update `related_records` paths after review.** Change paths to `records/archived/` only after maintainers approve the release evidence impact and record the old path, new path, reviewer, rationale, and whether the release evidence record remains `pending`, becomes `reviewed`, or becomes `verified`.
4. **Link both legacy and archived context through reviewed evidence.** If future schema or documentation conventions allow it, preserve the original path binding while adding explicit archived-path context in a reviewable way.
5. **Do not replace paths silently.** Blanket normalization from `records/verified/` to `records/archived/` is not an acceptable preservation strategy because it can erase review context.

No option should fabricate reviewer approvals, release validation results, migration timestamps, signatures, hashes, QR evidence, or production-readiness claims.

## Recommended approach

The recommended approach is to leave `records/pending/HC-RELEASE-2026-0001.json` unchanged during pre-migration planning and treat its current `related_records` paths as pending release evidence context.

A future migration PR should:

- not edit `HC-RELEASE-2026-0001.json` until maintainers explicitly review release evidence impact;
- treat the existing `records/verified/` paths as historical pending-context bindings;
- keep the three referenced records classified as historical and not current release evidence;
- decide release evidence handling separately from hash handling, QR handling, generated artifact regeneration, and record movement;
- if `related_records` paths are updated later, document the old path, new path, reviewer, rationale, and whether `HC-RELEASE-2026-0001` remains `pending`, becomes `reviewed`, or becomes `verified`;
- avoid silently normalizing `related_records` from `records/verified/` to `records/archived/`; and
- avoid claims of autonomous governance finality, forensic certainty, truth finality, live federation guarantees, or production readiness.

## Non-goals

This plan does not:

- modify `records/pending/HC-RELEASE-2026-0001.json`;
- move historical records;
- modify historical records;
- modify hash files or generate new hash files;
- modify QR artifacts or generate QR artifacts;
- modify generated artifacts;
- modify canonical records, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or trust-kernel logic;
- decide final release evidence verification status;
- decide hash handling, QR handling, generated artifact regeneration, or documentation example cleanup by itself; or
- claim that migration is ready to execute.

## Pre-migration requirements

Before any historical record moves from `records/verified/` to `records/archived/`, maintainers should complete the following release-evidence-specific requirements:

1. Confirm that `records/archived/` remains the approved target path for historical record archival.
2. Confirm the affected historical record IDs and current `related_records` path bindings.
3. Confirm that `HC-RELEASE-2026-0001` remains a pending release evidence record unless maintainers separately approve a status change.
4. Decide whether current `related_records` paths should remain as legacy pending-context references or be updated after migration.
5. If any path update is proposed, document old path, new path, reviewer, rationale, and release evidence status impact before editing the release evidence record.
6. Confirm that historical records remain historical and are not presented as current release evidence.
7. Coordinate the release evidence decision with hash handling, QR handling, generated artifact regeneration, and documentation reference updates.
8. Define whether a release evidence correction note, migration note, or direct reviewed record edit will carry the path-change rationale.
9. Run terminology, docs drift, canonical artifact, validator, and migration-specific checks required by the migration PR.
10. Record human-supervised validation before treating release evidence related-record handling as accepted.

## Future migration checklist

A future migration PR should include a `related_records` handling checklist similar to this:

- [ ] `HC-RELEASE-2026-0001` current status and lifecycle status are recorded before migration.
- [ ] Each related record lists its old `records/verified/` path.
- [ ] Each moved related record lists its intended `records/archived/` path.
- [ ] Maintainers decide whether `related_records` paths remain legacy context or are updated.
- [ ] Any updated path records old path, new path, reviewer, rationale, and release evidence status impact.
- [ ] Historical records remain classified as historical and not current release evidence.
- [ ] Hash handling is reviewed separately.
- [ ] QR handling is reviewed separately.
- [ ] Generated artifact regeneration is performed by approved tooling, not hand editing.
- [ ] Documentation references are reviewed by intent, not blanket-normalized.
- [ ] Human-supervised validation notes are included before migration is treated as accepted.

## Human-supervised validation notes

Release evidence related-record handling for archive migration must remain human-supervised. Agents and automation may inventory references, report path-sensitive bindings, suggest migration checklists, and prepare reviewable documentation, but they must not fabricate approvals, silently rewrite release evidence context, or treat migration as accepted without maintainer review.

Validation should explicitly distinguish:

- pending release evidence context from verified release evidence;
- historical records from current release evidence;
- record ID continuity from path-binding continuity;
- legacy `records/verified/` context from any future `records/archived/` context;
- advisory agent output from maintainer approval; and
- documentation readiness from migration execution readiness.

Until a future maintainer-approved migration PR completes these steps, `HC-RELEASE-2026-0001` and the historical records it references should remain unchanged.
