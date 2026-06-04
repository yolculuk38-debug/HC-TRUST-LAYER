# Post-Migration Hash/Path Reconciliation Review

## Purpose

This report reviews the hash/path state after PR #610 moved three historical HC:// records from `records/verified/` to `records/archived/` without modifying hash artifacts.

This is a documentation-only governance review. It does not modify hash files, records, QR artifacts, release evidence, generated artifacts, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Scope

Inspected inputs:

- `hash/`
- `records/archived/HC-TEST-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0002.md`

The review focuses on path-bound hash references and migration impact. It does not assert maintainer approval, forensic certainty, production readiness, or autonomous governance finality.

## 1. Current hash inventory

Current files under `hash/`:

| File | Current contents / binding | Notes |
| --- | --- | --- |
| `hash/.gitkeep` | Empty placeholder | No hash evidence. |
| `hash/HC-CHATGPT-2026-0001.sha256` | `e76cd39fbd8dca4368a7f6ae84a69fe51850ded16e8aaebbbcaa2e34bd986e0f  records/verified/HC-CHATGPT-2026-0001.md` | Historical manifest remains bound to the pre-migration path. |
| `hash/HC-CHATGPT-2026-0002.sha256` | `8a849d5e7f3a4eac8138d6e71afdb5727fba6e18be7b8ad23625493dee78c56d  records/verified/HC-CHATGPT-2026-0002.md` | Historical manifest remains bound to the pre-migration path. |
| `hash/HC-CLAUDE-2026-0001.sha256` | `fc32bc9690c493515a5ca71dfc6a0b6dec8a5faa0d62ba1b7eb2c015a13d10a0  HC-CLAUDE-2026-0001` | Not part of the three migrated records; path format differs from the others. |
| `hash/HC-TEST-2026-0001.sha256` | `10a252de2f70d8890bc71007c21194a0023f1e3322ef1c127f599966ad3499c5  records/verified/HC-TEST-2026-0001.md` | Historical manifest remains bound to the pre-migration path. |
| `hash/README.md` | Empty file | No hash evidence. |
| `hash/README.sha256` | `4ee69e637732ab02b4623d8cdabc2b82815a9b4bac4e70d1df9bb046f55c9aba  records/verified/README.md` | Not part of the three migrated records. |

The current archived record content digests match the digest values in the three historical manifests when recalculated against the archived files:

| Archived record | Current content digest | Legacy manifest digest | Content digest match |
| --- | --- | --- | --- |
| `records/archived/HC-TEST-2026-0001.md` | `10a252de2f70d8890bc71007c21194a0023f1e3322ef1c127f599966ad3499c5` | `10a252de2f70d8890bc71007c21194a0023f1e3322ef1c127f599966ad3499c5` | Yes |
| `records/archived/HC-CHATGPT-2026-0001.md` | `e76cd39fbd8dca4368a7f6ae84a69fe51850ded16e8aaebbbcaa2e34bd986e0f` | `e76cd39fbd8dca4368a7f6ae84a69fe51850ded16e8aaebbbcaa2e34bd986e0f` | Yes |
| `records/archived/HC-CHATGPT-2026-0002.md` | `8a849d5e7f3a4eac8138d6e71afdb5727fba6e18be7b8ad23625493dee78c56d` | `8a849d5e7f3a4eac8138d6e71afdb5727fba6e18be7b8ad23625493dee78c56d` | Yes |

## 2. Path-bound hash references

The three migrated record hash manifests remain path-bound to `records/verified/`:

- `hash/HC-TEST-2026-0001.sha256` references `records/verified/HC-TEST-2026-0001.md`.
- `hash/HC-CHATGPT-2026-0001.sha256` references `records/verified/HC-CHATGPT-2026-0001.md`.
- `hash/HC-CHATGPT-2026-0002.sha256` references `records/verified/HC-CHATGPT-2026-0002.md`.

The corresponding records now exist at:

- `records/archived/HC-TEST-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0002.md`

The pre-migration `records/verified/` target files are not present in the current tree for these three records. This means a standard `sha256sum -c` verification using the existing manifests would fail on path lookup even though the archived file contents currently produce the same digest values.

Additional record-internal references observed during this review:

- `records/archived/HC-TEST-2026-0001.md` points to `/hash/HC-TEST-2026-0001.sha256`.
- `records/archived/HC-CHATGPT-2026-0001.md` contains an `Archive Path` value of `records/verified/HC-CHATGPT-2026-0001.md` and states that SHA-256 hash generation is pending.
- `records/archived/HC-CHATGPT-2026-0002.md` points to `hash/HC-CHATGPT-2026-0002.sha256`.

## 3. Migration impact

PR #610 changed the record locations but did not change the hash manifests. The practical result is a split between:

- **content integrity evidence**, where the archived files currently hash to the same digest values recorded in the legacy manifests; and
- **path-bound manifest evidence**, where the `.sha256` file lines still identify the former `records/verified/` paths.

This is not automatically a content-integrity failure. It is a path reconciliation issue caused by preserving legacy hash artifacts after moving the records.

The current state preserves historical evidence but creates ambiguity for tools or reviewers that interpret the path column in `.sha256` files as the current repository location.

## 4. Legacy evidence considerations

The existing manifests are historical evidence of the original path bindings. They should not be silently overwritten because the filename component of a standard SHA-256 manifest line is part of the reviewable evidence context.

Preserving legacy manifests supports auditability by retaining:

- the original digest values;
- the original `records/verified/` path references;
- evidence that the migration did not alter hash artifacts; and
- a clear boundary between historical path evidence and any future archived-path evidence.

Any future reconciliation should explicitly distinguish legacy path-bound evidence from current archived-path evidence.

## 5. Risks of leaving hashes unchanged

Leaving the hash manifests unchanged has review and tooling risks:

- `sha256sum -c hash/HC-TEST-2026-0001.sha256` and equivalent checks for the migrated ChatGPT records will look for files under `records/verified/` and fail because those paths no longer exist.
- Reviewers may misread the unchanged manifests as stale or broken if the legacy path-binding purpose is not documented.
- Automated tooling may report false negatives if it expects every `.sha256` path to resolve in the current tree.
- Future contributors may attempt ad hoc repair without preserving legacy evidence.
- The repository may retain conflicting interpretations unless governance clearly states that unchanged manifests are legacy path-bound evidence, not current archived-path manifests.

## 6. Risks of regenerating hashes

Regenerating or replacing the existing manifests also carries risk:

- Overwriting existing `.sha256` files would erase the original `records/verified/` path bindings.
- A path-only manifest update could look like evidence mutation even if the digest stays unchanged.
- New manifests without old-path linkage may obscure the PR #610 migration history.
- Regeneration without a recorded command, reviewer, rationale, and migration context could weaken auditability.
- Any automated regeneration that touches broader hash, QR, generated, release evidence, schema, validator, workflow, runtime, signing, federation, policy, or canonical surfaces would exceed this report-only scope.

## 7. Recommended approach

Recommended approach: **preserve the existing hash manifests unchanged as legacy path-bound evidence, and add separate reviewed archived-path reconciliation evidence in a future scoped PR if maintainers decide current-path verification should be supported.**

The future reconciliation should be documentation-first and human-supervised. It should not overwrite legacy manifests unless maintainers explicitly approve replacement and record the rationale.

A safe future pattern would be:

1. Keep the existing `hash/HC-TEST-2026-0001.sha256`, `hash/HC-CHATGPT-2026-0001.sha256`, and `hash/HC-CHATGPT-2026-0002.sha256` files unchanged as legacy evidence.
2. Add a small migration-specific reconciliation note or manifest that records old path, new path, digest, exact command, date of review, reviewer, and rationale.
3. If archived-path `.sha256` files are needed, issue them as clearly linked current-path evidence rather than silently replacing the historical files.
4. Update documentation so reviewers and tools can distinguish legacy path-bound manifests from current archived-path verification material.

## 8. Required future actions

Before any hash/path reconciliation is treated as accepted, maintainers should complete the following actions in a separate scoped PR:

1. Decide whether current archived-path manifests are required or whether documented legacy manifests are sufficient for v0.1.0 stabilization.
2. Define the target location and naming convention for any archived-path hash evidence.
3. Record exact commands for any generated hash evidence.
4. Preserve or explicitly link the legacy `records/verified/` path bindings.
5. Document how tooling should handle legacy path-bound manifests whose files no longer exist at the recorded path.
6. Review related QR references separately without modifying QR artifacts as part of this report.
7. Review release evidence and generated artifact implications separately without modifying those artifacts as part of this report.
8. Run terminology, docs drift, canonical artifact, and any future migration-specific checks.
9. Require human-supervised maintainer review before changing or replacing any hash artifact.

## 9. Go / No-Go recommendation

**Go for documentation-only merge of this review.**

Rationale:

- The report preserves the post-migration state without modifying protected or evidence-bearing artifacts.
- The current archived record content digests match the digest values in the legacy manifests.
- The remaining issue is path-bound manifest reconciliation, not evidence that the migrated record bytes changed.
- The report identifies the operational risk of unchanged paths and the evidence risk of overwriting hashes.

**No-Go for automatic hash regeneration or hash file modification in this PR.**

Any hash artifact update should be handled in a future small, scoped, human-reviewed PR with explicit approval, recorded commands, and clear linkage to the legacy path-bound evidence.
