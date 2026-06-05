# QR Reconciliation Decision Review

## Purpose

This report records the QR reconciliation decision for legacy HC:// QR artifacts before v0.1.0. It determines whether legacy QR artifacts should remain unchanged, whether archived-path QR artifacts should be issued, or whether no QR reconciliation is required before v0.1.0.

This is a REPORT ONLY governance decision review. It does not modify QR artifacts, records, hash files, release evidence, generated artifacts, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, GitHub Actions, or canonical artifacts.

## Inspected Inputs

- `qr/`
- `docs/governance/post-migration-qr-review.md`
- `docs/governance/v0.1.0-final-readiness-review.md`

## Current State

Current QR inventory findings are:

| Artifact | Current state | Review note |
| --- | --- | --- |
| `qr/HC-CHATGPT-2026-0001.txt` | Present | Text artifact containing a `QR Target` URL bound to the former `records/verified/HC-CHATGPT-2026-0001.md` path. |
| `qr/HC-CHATGPT-2026-0002.txt` | Not present | Referenced by the archived record, but no matching QR text artifact exists in the current QR inventory. |
| `qr/HC-TEST-2026-0001.txt` | Not present | No scoped text artifact exists for the test record; the archived record references `/qr/` generally. |
| `qr/README.md` | Present | QR layer documentation and demo policy. |
| `qr/qr-code.jpg` | Present | Binary JPEG artifact. The post-migration QR review did not decode or regenerate it. |

PR #610 moved historical records from `records/verified/` to `records/archived/` without modifying QR artifacts. PR #612 reviewed post-migration QR references and found that at least one existing QR text artifact remains legacy path-bound, while other scoped QR text artifacts are absent. PR #617 decided to preserve legacy hash manifests for v0.1.0, establishing a conservative precedent for preserving path-bound historical evidence rather than overwriting it during release stabilization.

The final readiness review identifies remaining archive-related downstream reconciliation items, including QR artifacts, as open release-disposition items. It also cautions that existing QR artifacts should not be treated as active v0.1.0 evidence unless decoded or regenerated through a reviewed process.

## Decision Categories

### Preserve Legacy QR Artifacts

**Decision:** Recommended for v0.1.0.

The existing QR artifacts should remain unchanged because they are historical access artifacts connected to the pre-migration record layout. Overwriting them would blur the boundary between legacy path-bound evidence and any post-migration archived-path evidence. Preservation keeps the v0.1.0 review boundary narrow and avoids implying that QR reconciliation has been completed by unreviewed artifact replacement.

Operational interpretation:

- Treat `qr/HC-CHATGPT-2026-0001.txt` as a legacy path-bound QR target artifact.
- Do not overwrite existing QR files before v0.1.0.
- Do not infer the target of `qr/qr-code.jpg` from filename, directory placement, or visual appearance.
- Treat missing scoped QR text artifacts as inventory findings, not as proof that no QR dependency exists.
- Use governance documentation to disclose the legacy path-bound QR state for v0.1.0.

### Issue Archived-Path QR Artifacts

**Decision:** Defer until after v0.1.0 unless maintainers explicitly require a separate reviewed reconciliation PR before release.

Archived-path QR artifacts could improve operator and reader experience by pointing directly to current `records/archived/` locations. However, issuing them before v0.1.0 would create new evidence-adjacent artifacts and would require clear naming, target documentation, review expectations, and validation guidance. Without that policy, new QR artifacts may be mistaken for replacements for legacy QR artifacts or for active release evidence.

If maintainers choose this path later, the work should be a small, dedicated, human-reviewed PR that:

- leaves existing legacy QR artifacts unchanged;
- creates clearly labeled archived-path QR text artifacts or a QR reconciliation index;
- documents every target URL in reviewable text;
- decodes and documents any binary QR artifact before relying on it;
- avoids committing generated binary QR images unless maintainers explicitly approve them;
- explains that new archived-path artifacts are post-migration access aids, not replacements for historical QR evidence; and
- runs terminology, docs drift, canonical artifact, and any QR-specific checks available at that time.

### No Action Required

**Decision:** Acceptable only as a v0.1.0 release disposition when paired with explicit disclosure.

No QR artifact action is required before v0.1.0 if the release remains advisory, early-stage, and human-supervised, and if release documentation acknowledges that legacy path-bound QR evidence remains. This does not mean QR reconciliation is complete. It means the known QR state is not a release blocker because the issue is path and access reconciliation, not a demonstrated content-integrity failure.

## Recommendation

Adopt **Preserve Legacy QR Artifacts** for v0.1.0, with **No Action Required before v0.1.0** as the release disposition.

Do not overwrite existing QR files. Do not modify QR artifacts in the v0.1.0 stabilization window unless maintainers explicitly decide that current archived-path QR targets are required before release. If archived-path QR artifacts are needed, issue them only in a future small, human-reviewed PR with explicit target documentation and without replacing legacy QR artifacts.

## Risks

- Users may follow a legacy QR target and land on a former `records/verified/` path instead of the current `records/archived/` path.
- Reviewers may confuse legacy path-bound QR artifacts with current active verification routes.
- Missing scoped QR text artifacts may be misread as evidence that no QR dependency exists.
- The binary QR image may be assumed to point to a target that has not been decoded or documented in this decision review.
- Issuing archived-path QR artifacts without clear labels may blur historical evidence and post-migration access aids.
- Leaving the issue only in governance documentation may require extra reviewer attention during v0.1.0 release review.

## v0.1.0 Impact

This decision should not block v0.1.0 if all of the following remain true:

1. v0.1.0 is presented as advisory, early-stage HC:// verification infrastructure, not production-ready infrastructure.
2. Existing QR artifacts remain unchanged and are described as legacy path-bound access evidence where applicable.
3. Release documentation acknowledges that archived-path QR artifacts were not issued before v0.1.0.
4. Existing QR artifacts are not relied on as active v0.1.0 evidence unless decoded or otherwise reviewed through a dedicated process.
5. Required terminology, docs drift, canonical artifact, and relevant validation checks pass or are explicitly dispositioned.
6. Human-supervised validation remains responsible for the final release decision.

This decision does not validate release readiness by itself. It only resolves the QR reconciliation strategy for the migrated historical records.

## Future Roadmap

After v0.1.0, maintainers should consider a dedicated QR reconciliation plan that:

1. Defines naming and placement rules for archived-path QR text artifacts.
2. Decides whether archived-path QR targets should be standalone files, a reconciliation index, or generated release evidence.
3. Documents every QR target in text before relying on any binary QR artifact.
4. Decodes and documents `qr/qr-code.jpg` before treating it as evidence.
5. Decides whether missing scoped QR text artifacts for archived historical records should be created, documented as absent, or left unbackfilled.
6. Clarifies user-facing guidance for legacy QR targets that point to former paths.
7. Preserves legacy QR artifacts and avoids replacing them with post-migration access aids.
8. Keeps any automation bounded, explainable, reversible, and human-reviewable.

## Final Decision

**Preserve Legacy QR Artifacts.**

No QR artifact reconciliation is required before v0.1.0 if release documentation records this disposition. Archived-path QR artifacts may be useful later, but they should be introduced only through a separate reviewed reconciliation PR after their status, target documentation, and review semantics are defined.
