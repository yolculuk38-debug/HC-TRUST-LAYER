# Historical Record Hash Handling Plan

## Purpose

This plan defines how existing hash manifests for historical HC:// records should be preserved, reissued, or linked before any future archive migration from `records/verified/` to `records/archived/`.

It is documentation-only governance guidance. It does not move records, modify records, modify hash manifests, generate new hash files, modify QR artifacts, regenerate generated artifacts, modify release evidence records, modify schemas, modify validators, modify workflows, modify runtime code, or alter signing, federation, policy, or trust-kernel logic.

## Scope

This plan covers the three historical records currently identified for future archive migration planning:

- `records/verified/HC-TEST-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0001.md`
- `records/verified/HC-CHATGPT-2026-0002.md`

It also covers their existing hash manifests:

- `hash/HC-TEST-2026-0001.sha256`
- `hash/HC-CHATGPT-2026-0001.sha256`
- `hash/HC-CHATGPT-2026-0002.sha256`

This plan relies on the approved future archive target path decision that selected `records/archived/` for historical record archival. Migration remains not ready to execute until all path-sensitive evidence handling is reviewed and approved.

## Current hash bindings

The current hash manifests bind each digest to the record path that existed when the manifest was created:

| Record ID | Existing manifest | Current path binding |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `hash/HC-TEST-2026-0001.sha256` | `records/verified/HC-TEST-2026-0001.md` |
| `HC-CHATGPT-2026-0001` | `hash/HC-CHATGPT-2026-0001.sha256` | `records/verified/HC-CHATGPT-2026-0001.md` |
| `HC-CHATGPT-2026-0002` | `hash/HC-CHATGPT-2026-0002.sha256` | `records/verified/HC-CHATGPT-2026-0002.md` |

These manifests are historical evidence. They should not be silently overwritten, renamed, or normalized during migration planning.

## Path-sensitive hash risk

Standard SHA-256 manifest lines include both a digest and a filename. Even if record content bytes remain unchanged, moving a record from `records/verified/` to `records/archived/` changes the path text recorded in the manifest line.

That creates a path-sensitive evidence risk:

- preserving only the old manifest may leave a valid digest associated with a legacy path;
- overwriting the old manifest may erase evidence of the original path binding;
- issuing a new manifest without linking it to the old manifest may obscure migration context; and
- changing path text without reviewer evidence may look like a hash update even when content is unchanged.

Migration must therefore separate content integrity from path-binding history and keep both reviewable.

## Preservation options

Maintainers may choose one of the following approaches in a future migration-specific PR:

1. **Preserve legacy manifests only.** Keep existing hash files unchanged as legacy path-bound evidence and document that they refer to the pre-migration `records/verified/` paths.
2. **Preserve legacy manifests and add migration-specific hash evidence.** Keep existing hash files unchanged, then add a reviewed migration note or manifest that records the old path, new path, content hash, command used, reviewer, and rationale.
3. **Preserve legacy manifests and reissue new archived-path manifests.** Keep existing hash files unchanged or explicitly mark them as legacy evidence, then add new reviewed manifests for `records/archived/` paths with clear linkage to the old manifests.
4. **Replace legacy manifests only with explicit maintainer approval.** This is the highest-risk option and should be used only if maintainers approve replacement in writing, explain why legacy evidence is no longer retained in-place, and preserve enough migration evidence for audit review.

No option should fabricate hashes, signatures, reviewer approvals, migration timestamps, or command output.

## Recommended approach

The recommended approach is to preserve existing hash files as legacy path-bound evidence and add a reviewable migration-specific hash handling step if records move.

A future migration PR should:

- avoid silently overwriting existing `.sha256` files;
- treat existing manifests as evidence for the current `records/verified/` path bindings;
- document whether new `records/archived/` path-bound hashes are issued, deferred, or intentionally not issued;
- if new hashes are issued, record the old path, new path, content hash, exact command used, reviewer, and rationale;
- link new hash evidence back to the legacy manifest instead of erasing the earlier binding; and
- preserve old hash evidence unless maintainers explicitly approve replacement.

This approach keeps the migration reviewable while avoiding claims of autonomous governance finality, forensic certainty, or production readiness.

## Non-goals

This plan does not:

- move historical records;
- modify historical records;
- modify existing hash manifests;
- generate new hash files;
- update, regenerate, redirect, or deprecate QR artifacts;
- modify generated artifacts;
- modify release evidence records;
- modify canonical records, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or trust-kernel logic;
- decide QR handling, release evidence handling, or generated artifact regeneration by itself; or
- claim that migration is ready to execute.

## Pre-migration requirements

Before any historical record moves from `records/verified/` to `records/archived/`, maintainers should complete the following requirements:

1. Confirm the migration PR scope and affected records.
2. Confirm that `records/archived/` remains the approved target path.
3. Inventory existing hash manifests and verify their current path bindings.
4. Decide whether legacy hash manifests will be retained only, linked to migration-specific evidence, or accompanied by new archived-path manifests.
5. Define the exact command that will be used if new content hashes or path-bound manifests are issued.
6. Define where migration-specific hash handling evidence will live.
7. Identify the reviewer responsible for validating the hash handling decision.
8. Decide how QR, release evidence, generated artifacts, and documentation references will be handled in separate reviewable steps.
9. Run terminology, docs drift, canonical artifact, validator, and migration-specific checks required by the migration PR.
10. Record remaining uncertainty before merge.

## Future migration checklist

A future migration PR should include a hash handling checklist similar to this:

- [ ] Existing legacy hash manifests are preserved or any replacement has explicit maintainer approval.
- [ ] Each moved record lists its old path and new path.
- [ ] Each hash decision explains whether the digest is content-only evidence, path-bound manifest evidence, or both.
- [ ] Any new hash command is recorded exactly as run.
- [ ] Any new hash output is reviewable and not fabricated.
- [ ] New hash evidence links back to the legacy manifest.
- [ ] QR artifact handling is reviewed separately.
- [ ] Release evidence `related_records` impact is reviewed separately.
- [ ] Generated artifact regeneration is performed by approved tooling, not hand editing.
- [ ] Human-supervised validation notes are included before the migration is treated as accepted.

## Human-supervised validation notes

Hash handling for archive migration must remain human-supervised. Agents and automation may inventory files, suggest commands, and prepare reviewable documentation, but they must not fabricate hash evidence, fabricate approvals, or treat a migration as accepted without maintainer review.

Validation should explicitly distinguish:

- legacy path-bound evidence from new archived-path evidence;
- content byte integrity from manifest path text;
- advisory agent output from maintainer approval; and
- documentation readiness from migration execution readiness.

Until a future maintainer-approved migration PR completes these steps, the historical records and their existing hash manifests should remain unchanged.
