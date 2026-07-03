# Post-Migration QR/Path Reconciliation Review

## Purpose

This report reviews the QR/path state after PR #610 moved three historical HC:// records from `records/verified/` to `records/archived/` without modifying QR artifacts. It follows PR #611's hash/path impact review and focuses on whether existing QR references remain path-bound after the migration.

This is a documentation-only governance review. It does not modify QR artifacts, records, hash files, release evidence, generated artifacts, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Scope

Inspected inputs:

- `qr/`
- `qr/HC-CHATGPT-2026-0001.txt`
- `qr/HC-CHATGPT-2026-0002.txt` if present
- `qr/HC-TEST-2026-0001.txt` if present
- `qr/qr-code.jpg`
- `records/archived/HC-TEST-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0001.md`
- `records/archived/HC-CHATGPT-2026-0002.md`

The review focuses on path-bound QR references and migration impact. It does not assert maintainer approval, forensic certainty, production readiness, autonomous governance finality, or live public verification guarantees.

## 1. Current QR inventory

Current files under `qr/`:

| File | Current state | Notes |
| --- | --- | --- |
| `qr/HC-CHATGPT-2026-0001.txt` | Present, 115 bytes | Text artifact containing a `QR Target` URL bound to the former `records/verified/HC-CHATGPT-2026-0001.md` path. |
| `qr/HC-CHATGPT-2026-0002.txt` | Not present | Referenced by `records/archived/HC-CHATGPT-2026-0002.md`, but no matching QR text artifact exists in the current inventory. |
| `qr/HC-TEST-2026-0001.txt` | Not present | No scoped text artifact exists for the test record; `records/archived/HC-TEST-2026-0001.md` references `/qr/` generally. |
| `qr/README.md` | Present, 1,379 bytes | QR layer documentation and demo policy. |
| `qr/qr-code.jpg` | Present, 42,303 bytes | Binary JPEG artifact. Local byte inspection identifies it as a 300 x 300 JPEG image; this review did not decode or regenerate it. |

## 2. Path-bound QR references

The confirmed path-bound QR text artifact is:

```text
qr/HC-CHATGPT-2026-0001.txt
QR Target:
https://github.com/yolculuk38-debug/legacy-archive-repo/blob/main/records/verified/HC-CHATGPT-2026-0001.md
```

This target remains bound to the pre-migration `records/verified/` path. The corresponding record now exists at:

```text
records/archived/HC-CHATGPT-2026-0001.md
```

Additional record-internal QR references observed during this review:

- `records/archived/HC-TEST-2026-0001.md` contains `QR Reference: See /qr/`.
- `records/archived/HC-CHATGPT-2026-0001.md` states `Pending QR verification link`.
- `records/archived/HC-CHATGPT-2026-0002.md` references `qr/HC-CHATGPT-2026-0002.txt`, but that file is not present.

No archived-path QR text artifact for any of the three migrated records was found in `qr/`.

## 3. Missing QR artifacts

Missing scoped QR text artifacts are inventory findings:

| Record ID | Referenced or expected artifact | Current finding |
| --- | --- | --- |
| `HC-TEST-2026-0001` | `qr/HC-TEST-2026-0001.txt` | Not present. The archived record references `/qr/` generally rather than naming a specific file. |
| `HC-CHATGPT-2026-0001` | Current archived-path QR artifact | Not present. The existing text artifact points to the former `records/verified/` path. |
| `HC-CHATGPT-2026-0002` | `qr/HC-CHATGPT-2026-0002.txt` | Not present despite the archived record referencing this path. |

These missing files must not be interpreted as proof that the migration had no QR impact. They show that the QR inventory is incomplete for the scoped historical records and that at least one existing QR artifact remains legacy path-bound.

## 4. Migration impact

PR #610 changed the repository locations of the scoped historical records but did not change QR artifacts. The practical result is a split between:

- **legacy QR evidence**, where `qr/HC-CHATGPT-2026-0001.txt` preserves a pre-migration target under `records/verified/`; and
- **current record location**, where the migrated record now lives under `records/archived/`.

This is not automatically a content-integrity failure and does not prove QR tampering. It is a path reconciliation issue caused by preserving existing QR material after moving records.

The migration also leaves two inventory gaps unresolved:

- `HC-CHATGPT-2026-0002` has a record-level QR reference to a text artifact that is not present.
- `HC-TEST-2026-0001` has only a general `/qr/` reference and no scoped text artifact.

## 5. Legacy QR evidence considerations

Existing QR artifacts should be treated as reviewable historical evidence. They can preserve useful context about the pre-migration public access path, even when the target is no longer the current repository path.

For auditability, legacy QR evidence should retain a clear boundary between:

- the original path-bound target;
- the post-migration archived record path;
- any future replacement, superseding, or archived-path QR artifact; and
- any future reviewer decision to deprecate, redirect, or preserve the old target.

The binary `qr/qr-code.jpg` should also be treated cautiously. Because this review did not decode or regenerate it, its target should not be assumed from filename, directory placement, or visual appearance alone.

## 6. Risks of leaving QR artifacts unchanged

Leaving QR artifacts unchanged has review and user-experience risks:

- A user following the `qr/HC-CHATGPT-2026-0001.txt` target may land on a former `records/verified/` path instead of the current `records/archived/` path.
- Reviewers may confuse a legacy path-bound access artifact with a current verification route.
- Missing QR text artifacts may be mistaken for evidence that no QR dependency exists.
- Automated or manual inventory checks may report inconsistent state between archived records and QR references.
- If `qr/qr-code.jpg` is used without decoding, reviewers may infer a target that has not been validated in this report.

These risks are manageable if the repository labels the state as legacy path-bound evidence and avoids representing existing QR artifacts as current archived-path verification links.

## 7. Risks of regenerating QR artifacts

Regenerating or overwriting QR artifacts also has risks:

- Silent overwrite would erase historical path-bound evidence and weaken auditability.
- A regenerated QR artifact could imply reviewer approval, current verification status, or active public verifier availability that has not been established.
- New QR files could diverge from existing hash, release evidence, generated artifact, or documentation state if introduced without a coordinated review.
- Binary QR artifacts are harder to review than text targets and can obscure changes unless accompanied by explicit decoded target documentation.
- Backfilling missing QR files without a reviewable decision could create fabricated or misleading QR evidence.

Any future QR generation should be explicit, minimal, reviewed, and accompanied by text-level target documentation.

## 8. Recommended approach

Recommended approach:

1. Preserve existing QR artifacts as legacy path-bound evidence.
2. Do not overwrite QR files silently.
3. Treat missing QR files as inventory findings, not proof of no QR impact.
4. If archived-path QR artifacts are needed, create them in a future small reviewed PR.
5. Prefer text-first QR target documentation before committing any binary QR output.
6. If binary QR artifacts are retained or added, include a decoded target or equivalent reviewable target record in the same small PR.

This approach preserves evidence, keeps the migration review bounded, and avoids uncontrolled architecture expansion or unsupported public-verification claims.

## 9. Required future actions

Required future actions before treating QR/path reconciliation as complete:

1. Decide whether `qr/HC-CHATGPT-2026-0001.txt` should remain only as legacy path-bound evidence, be accompanied by a new archived-path text artifact, or be formally deprecated.
2. Decode and document the target of `qr/qr-code.jpg` before relying on it as QR evidence.
3. Decide whether to create `qr/HC-CHATGPT-2026-0002.txt` for the archived path or update documentation to mark the current record-level reference as a missing historical artifact.
4. Decide whether `HC-TEST-2026-0001` needs a scoped QR text artifact or whether its general `/qr/` reference should remain historical context.
5. Keep any new archived-path QR work in a separate, small, reviewed PR.
6. Avoid modifying records, hash files, generated artifacts, release evidence, schemas, validators, workflows, or runtime code unless a future PR explicitly requests and justifies those changes.
7. Run the repository's documentation and governance checks after any future QR documentation or artifact change.

## 10. Go / No-Go recommendation

Recommendation: **Go for documentation-only merge of this review; No-Go for QR artifact regeneration in this PR.**

Rationale:

- The current report documents the post-migration QR/path state without modifying protected or evidence-bearing artifacts.
- Existing QR artifacts should remain preserved as legacy path-bound evidence unless maintainers approve a separate disposition.
- Missing QR artifacts should remain recorded as inventory findings, not backfilled silently.
- Archived-path QR artifacts, if needed, should be created only in a future small reviewed PR with explicit target documentation and human-supervised validation.
