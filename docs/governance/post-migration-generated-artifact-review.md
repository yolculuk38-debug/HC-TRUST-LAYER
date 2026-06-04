# Post-Migration Generated Artifact Review

## Purpose

This report reviews generated artifact state after PR #610 moved three historical HC:// records from `records/verified/` to `records/archived/`.

This is a documentation-only governance review. It does not modify generated artifacts, records, hash files, QR artifacts, release evidence, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Scope

Inspected inputs:

- `generated/audit_snapshot.json`
- `docs/governance/generated-artifact-handling-plan.md`
- `records/archived/HC-TEST-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0002.md`

The review focuses only on post-migration generated artifact handling for `generated/audit_snapshot.json`. It does not assert maintainer approval, forensic certainty, production readiness, release verification, or autonomous governance finality.

## 1. Current generated artifact inventory

The current `generated/` directory contains the following generated JSON artifacts:

| Artifact | Current review relevance |
| --- | --- |
| `generated/audit_snapshot.json` | In scope. Path-sensitive audit snapshot that includes record IDs and source directory bindings relevant to the historical record migration. |
| `generated/example_federation_package.json` | Out of scope for this report. Present as generated advisory example material. |
| `generated/explorer_index.json` | Out of scope for this report. Present as generated advisory explorer index material. |
| `generated/first_working_audit_snapshot.json` | Out of scope for this report. Present as first-working-record demo snapshot material. |
| `generated/first_working_explorer_index.json` | Out of scope for this report. Present as first-working-record demo explorer index material. |

Current `generated/audit_snapshot.json` values:

| Field | Current value or binding |
| --- | --- |
| `file_count` | `9` |
| `record_ids` | `.gitkeep`, `HC-2026-0002`, `HC-CHATGPT-2026-0001`, `HC-CHATGPT-2026-0002`, `HC-EXAMPLE-2026-0001`, `HC-TEST-2026-0001`, `README` |
| `sha256_manifest_hash` | `7882c93453c3ed3f1b165b495621f3a17e51e035ee0e9d988e8f3b5914b0a5a4` |
| `snapshot_timestamp` | `2026-05-26T16:05:54Z` |
| `source_directories` | `records/pending/`, `records/verified/`, `records/archived/` |

The scoped historical record IDs remain present in the generated audit snapshot inventory. The snapshot also already lists both `records/verified/` and `records/archived/` as source directories.

## 2. Current path references

Current generated artifact bindings:

- `generated/audit_snapshot.json` does not list per-record paths for the scoped historical records.
- `generated/audit_snapshot.json` does list `records/verified/` and `records/archived/` in `source_directories`.
- The snapshot retains a `sha256_manifest_hash` value generated before this review and was not recalculated in this PR.

Current archived record references reviewed for generated-artifact context:

| Record | Current archived location | Internal path or artifact reference findings |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `records/archived/HC-TEST-2026-0001.md` | References `/hash/HC-TEST-2026-0001.sha256` and `/qr/`; no internal `records/verified/` path was found in the inspected file. |
| `HC-CHATGPT-2026-0001` | `records/archived/HC-CHATGPT-2026-0001.md` | Contains an `Archive Path` value of `records/verified/HC-CHATGPT-2026-0001.md`; hash and QR references remain pending text. |
| `HC-CHATGPT-2026-0002` | `records/archived/HC-CHATGPT-2026-0002.md` | References `hash/HC-CHATGPT-2026-0002.sha256`, `qr/HC-CHATGPT-2026-0002.txt`, and `timeline/2026-05-12-verification-system.md`; no internal `records/verified/` path was found in the inspected file. |

The generated artifact handling plan treats `generated/audit_snapshot.json` as historical generated evidence for the repository state at the time it was generated. It also warns that generated audit artifacts can be path-sensitive even when individual record IDs remain unchanged.

## 3. Migration impact

PR #610 changed the repository locations of the scoped historical records, but no generated artifacts were modified during the migration. The practical result is a split between:

- **record ID continuity**, where `HC-TEST-2026-0001`, `HC-CHATGPT-2026-0001`, and `HC-CHATGPT-2026-0002` remain listed in `generated/audit_snapshot.json`; and
- **path and generation-time continuity**, where `generated/audit_snapshot.json` remains a pre-review generated artifact with its original timestamp, manifest hash, file count, and source directory list.

Because `generated/audit_snapshot.json` does not include per-record paths, the migration did not create visible per-record stale paths inside that file. However, the snapshot's `file_count`, `sha256_manifest_hash`, and timestamp are still generated values from an earlier repository state and should not be interpreted as a fresh post-migration recalculation.

This state is not automatically a generated artifact failure. It is a documented post-migration reconciliation finding: the generated audit snapshot preserves historical generated evidence, while current record locations now live under `records/archived/`.

## 4. Risks of leaving generated artifacts unchanged

Leaving `generated/audit_snapshot.json` unchanged preserves evidence continuity, but it has risks:

- Reviewers or tools may misread the snapshot timestamp and manifest hash as current post-migration generated values.
- The snapshot may appear stale if future checks expect every generated value to be regenerated after record movement.
- The `file_count` and `sha256_manifest_hash` may not represent the current tree if the generator is path-sensitive or content-sensitive beyond record IDs.
- The presence of both `records/verified/` and `records/archived/` in `source_directories` may hide the fact that scoped historical records now live only under `records/archived/`.
- Future contributors may attempt ad hoc regeneration without recording source inputs, tooling, reviewer context, or rationale.
- Coordination with hash, QR, release evidence, and documentation reference reconciliation may remain incomplete if generated artifact disposition is deferred indefinitely.

These risks are manageable if the repository treats the unchanged snapshot as historical generated evidence and documents that it is not a fresh post-migration artifact.

## 5. Risks of regenerating generated artifacts

Regenerating or replacing `generated/audit_snapshot.json` also carries risk:

- Replacing the file would erase the currently preserved generated snapshot unless legacy context is retained elsewhere.
- A regenerated `sha256_manifest_hash`, `file_count`, or timestamp could be mistaken for migration approval or release evidence validation.
- Regeneration without a documented command, source inputs, reviewer, rationale, and validation result would weaken auditability.
- A broad generator run could modify additional generated artifacts outside the intended review boundary.
- Generated diffs may include unrelated changes if the generator reads directories or files beyond the migration scope.
- Regeneration could obscure whether differences were caused by PR #610, later repository changes, tooling changes, or source input changes.
- Any generated artifact update touching records, hashes, QR artifacts, release evidence, schemas, validators, workflows, runtime, signing, federation, policy, or canonical surfaces would exceed this report-only scope.

Generated artifact regeneration should therefore be small, explicit, reproducible, and human-supervised.

## 6. Recommended regeneration approach

Recommended approach: **do not regenerate generated artifacts in this report-only PR. Preserve `generated/audit_snapshot.json` unchanged as historical generated evidence, and prepare any future regeneration as a separate scoped PR.**

A safe future regeneration pattern would be:

1. Identify and document the approved repository command or tooling path for generating `generated/audit_snapshot.json`.
2. Record the exact source inputs and expected source directories before running the generator.
3. Preserve the current snapshot values in a review note or legacy context before replacement.
4. Run only the approved generator needed for `generated/audit_snapshot.json`; avoid broad generated artifact rewrites.
5. Review the generated diff manually for unexpected changes to `file_count`, `record_ids`, `sha256_manifest_hash`, `snapshot_timestamp`, and `source_directories`.
6. Coordinate the regenerated artifact review with hash, QR, release evidence, and documentation reference disposition.
7. Record the command, reviewer, rationale, date, and validation results in the future PR.
8. Keep generated artifacts clearly non-canonical and advisory; do not present regeneration as proof of forensic certainty, truth finality, live federation guarantees, production readiness, or maintainer acceptance by itself.

## 7. Required future actions

Before any generated artifact regeneration or replacement is treated as accepted, maintainers should complete the following actions in a separate scoped PR:

1. Decide whether v0.1.0 stabilization requires a fresh post-migration `generated/audit_snapshot.json` or whether documented historical generated evidence is sufficient.
2. Identify the approved generator command or tooling path for `generated/audit_snapshot.json`.
3. Define generator source inputs and confirm whether `records/verified/`, `records/archived/`, and `records/pending/` should remain in scope.
4. Preserve or explicitly cite the current generated values before replacement.
5. Confirm that regeneration will not modify records, hash files, QR artifacts, release evidence, schemas, validators, workflows, runtime, signing, federation, policy, or canonical artifacts.
6. Review the `records/verified/` path retained inside `records/archived/HC-CHATGPT-2026-0001.md` separately from generated artifact regeneration.
7. Coordinate with post-migration hash, QR, release evidence, and documentation reference reviews.
8. Run terminology, docs drift, canonical artifact, and any future migration-specific checks.
9. Require human-supervised maintainer review before replacing or reissuing generated audit evidence.

## 8. Go / No-Go recommendation

**Go for documentation-only merge of this review.**

Rationale:

- The report preserves the post-migration state without modifying generated artifacts or other evidence-bearing artifacts.
- `generated/audit_snapshot.json` already includes the scoped historical record IDs and lists both `records/verified/` and `records/archived/` as source directories.
- No per-record stale path is visible inside `generated/audit_snapshot.json` for the scoped records.
- The remaining issue is generated artifact disposition and regeneration timing, not evidence that generated artifacts were modified during migration.

**No-Go for automatic generated artifact regeneration or generated artifact modification in this PR.**

Any regeneration should be handled in a future small, scoped, human-reviewed PR with explicit approval, recorded source inputs, exact commands, validation results, and clear separation between historical generated evidence and post-migration generated output.
