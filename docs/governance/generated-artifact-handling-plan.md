# Generated Artifact Handling Plan

## Purpose

This plan defines how generated audit artifacts should be handled before any future historical record archive migration from `records/verified/` to `records/archived/`.

It is documentation-only governance guidance. It does not modify generated artifacts, move records, modify records, modify hashes, modify QR artifacts, modify release evidence, modify schemas, modify validators, modify workflows, modify runtime code, or alter signing, federation, policy, or trust-kernel logic.

## Scope

This plan covers the generated audit snapshot currently identified as path-sensitive migration evidence:

- `generated/audit_snapshot.json`

It is informed by the archive readiness, blocker review, archive target path decision, hash handling plan, QR handling plan, and release evidence `related_records` handling plan.

This plan applies only to generated audit artifact handling for future migration planning. It does not decide hash handling, QR handling, release evidence handling, documentation example cleanup, or record movement by itself.

## Current generated artifact bindings

The current `generated/audit_snapshot.json` includes generated audit context for the repository's record directories. Its current bindings include:

| Field | Current value or binding |
| --- | --- |
| `file_count` | `9` |
| `record_ids` | `.gitkeep`, `HC-2026-0002`, `HC-CHATGPT-2026-0001`, `HC-CHATGPT-2026-0002`, `HC-EXAMPLE-2026-0001`, `HC-TEST-2026-0001`, `README` |
| `sha256_manifest_hash` | `7882c93453c3ed3f1b165b495621f3a17e51e035ee0e9d988e8f3b5914b0a5a4` |
| `snapshot_timestamp` | `2026-05-26T16:05:54Z` |
| `source_directories` | `records/pending/`, `records/verified/`, `records/archived/` |

The snapshot includes the historical record IDs currently planned for archive migration review and lists both the current `records/verified/` source directory and the approved future `records/archived/` target path family.

The current snapshot should be treated as historical generated evidence for the repository state at the time it was generated. It should not be hand-edited, silently normalized, or used as proof that migration is ready to execute.

## Path-sensitive generated artifact risk

Generated audit artifacts can be path-sensitive even when individual record IDs remain unchanged. Moving records from `records/verified/` to `records/archived/` may change generated counts, source directory coverage, manifest hashes, record inventories, or review expectations.

That creates several migration risks:

- editing `generated/audit_snapshot.json` by hand could erase the generated evidence trail;
- regenerating the snapshot before record movement could create a misleading pre-migration artifact;
- regenerating the snapshot after record movement without recording source inputs and tooling could obscure why the generated values changed;
- treating generated output as canonical record evidence could blur the boundary between records and non-canonical artifacts; and
- replacing the existing snapshot without reviewer context could make it difficult to distinguish historical generated evidence from post-migration generated evidence.

Generated artifact handling must therefore preserve audit traceability and separate historical generated evidence from any future regenerated artifact.

## Preservation options

Maintainers may choose one of the following approaches in a future migration-specific PR:

1. **Preserve the current generated artifact until migration execution.** Leave `generated/audit_snapshot.json` unchanged during planning and treat it as historical generated evidence for the current repository state.
2. **Regenerate only after approved migration steps.** Move records and update reviewed path-sensitive references first, then regenerate the audit snapshot through approved tooling and review the generated diff.
3. **Preserve the legacy artifact and add migration evidence.** Keep enough legacy context to explain the pre-migration generated state, then document the source inputs, tool used, reviewer, rationale, and validation results for any later regeneration.
4. **Replace the generated artifact only with explicit review.** If maintainers choose to replace the current snapshot, the migration PR should state why replacement is appropriate and record the validation boundary for the regenerated output.

No option should fabricate generated values, hashes, reviewer approvals, migration timestamps, validation results, signatures, QR evidence, release evidence status, or production-readiness claims.

## Recommended approach

The recommended approach is to leave `generated/audit_snapshot.json` unchanged during pre-migration planning and treat the current file as historical generated evidence.

A future migration PR should:

- not edit `generated/audit_snapshot.json` before historical records move;
- never hand-edit generated artifacts;
- regenerate generated artifacts only through approved repository tooling;
- treat the current generated snapshot as evidence of the pre-migration generated state;
- document source inputs, tool used, reviewer, rationale, and validation results if artifact regeneration occurs later;
- review generated diffs manually for unexpected scope changes;
- coordinate regeneration with hash handling, QR handling, release evidence `related_records` handling, and documentation reference updates; and
- preserve audit traceability from pre-migration generated evidence to any post-migration regenerated artifact.

This approach keeps migration reviewable while avoiding claims of autonomous governance finality, forensic certainty, truth finality, live federation guarantees, or production readiness.

## Non-goals

This plan does not:

- modify `generated/audit_snapshot.json`;
- regenerate generated artifacts;
- move historical records;
- modify historical records;
- modify hash files or generate new hash files;
- modify QR artifacts or generate QR artifacts;
- modify release evidence records;
- modify canonical records, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or trust-kernel logic;
- decide final hash handling, QR handling, release evidence handling, documentation example cleanup, or migration execution readiness by itself; or
- claim that migration is ready to execute.

## Pre-migration requirements

Before any historical record moves from `records/verified/` to `records/archived/`, maintainers should complete the following generated-artifact-specific requirements:

1. Confirm that `records/archived/` remains the approved target path for historical record archival.
2. Confirm the affected historical record IDs and current generated snapshot bindings.
3. Identify the approved repository command or tooling path for regenerating `generated/audit_snapshot.json`.
4. Confirm that generated artifacts will not be hand-edited.
5. Decide whether the current generated artifact will remain as legacy generated evidence or be replaced after migration with documented review context.
6. Define the source inputs that the generator should use after migration.
7. Coordinate generated artifact handling with hash handling, QR handling, release evidence `related_records` handling, and documentation reference updates.
8. Record the reviewer, rationale, command used, and validation results for any future regeneration.
9. Run terminology, docs drift, canonical artifact, validator, and migration-specific checks required by the migration PR.
10. Record human-supervised validation before treating generated artifact handling as accepted.

## Future migration checklist

A future migration PR should include a generated artifact handling checklist similar to this:

- [ ] Current `generated/audit_snapshot.json` values are recorded before migration.
- [ ] Historical generated evidence is not hand-edited.
- [ ] Approved generator command or tooling path is identified.
- [ ] Generator source inputs are documented.
- [ ] Record movement, hash handling, QR handling, release evidence handling, and documentation reference handling are coordinated before regeneration.
- [ ] Any regenerated artifact records the tool used, reviewer, rationale, and validation results.
- [ ] Generated diffs are manually reviewed for unexpected file count, record ID, source directory, or manifest hash changes.
- [ ] Generated artifacts remain non-canonical artifacts and are not presented as canonical verification records.
- [ ] Human-supervised validation notes are included before migration is treated as accepted.

## Human-supervised validation notes

Generated artifact handling for archive migration must remain human-supervised. Agents and automation may inventory generated bindings, identify path-sensitive risks, suggest checklists, and prepare reviewable documentation, but they must not hand-edit generated artifacts, fabricate generated values, fabricate approvals, or treat migration as accepted without maintainer review.

Validation should explicitly distinguish:

- generated audit artifacts from canonical records;
- historical generated evidence from post-migration regenerated output;
- record ID continuity from path-binding continuity;
- current `records/verified/` source coverage from any future `records/archived/` source coverage;
- advisory agent output from maintainer approval; and
- documentation readiness from migration execution readiness.

Until a future maintainer-approved migration PR completes these steps, `generated/audit_snapshot.json` and the historical records planned for archival should remain unchanged.
