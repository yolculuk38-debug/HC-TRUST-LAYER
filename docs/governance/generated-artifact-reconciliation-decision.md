# Generated Artifact Reconciliation Decision

## Purpose

This report records the generated artifact reconciliation decision for `generated/audit_snapshot.json` before v0.1.0.

It is a documentation-only governance decision. It does not modify generated artifacts, records, hash files, QR artifacts, release evidence, schemas, validators, workflows, runtime code, signing logic, federation logic, policy files, or canonical artifacts.

## Scope

Inspected inputs:

- `generated/audit_snapshot.json`
- `docs/governance/post-migration-generated-artifact-review.md`
- `docs/governance/v0.1.0-final-readiness-review.md`

Context considered:

- PR #610 moved historical HC:// records to `records/archived/`.
- PR #614 reviewed post-migration generated artifacts.
- PR #617 decided to preserve legacy hash manifests for v0.1.0.
- PR #618 decided to preserve legacy QR artifacts for v0.1.0.
- PR #619 decided to preserve legacy release evidence `related_records` for v0.1.0.

This report does not assert forensic certainty, production readiness, release approval, maintainer approval, or autonomous governance finality.

## Decision Categories

| Category | Decision | Rationale |
| --- | --- | --- |
| Preserve Current Generated Artifacts | **Recommended for v0.1.0** | Preserves historical generated evidence, avoids uncontrolled generated rewrites, and aligns with adjacent v0.1.0 preservation decisions for legacy hash manifests, QR artifacts, and release evidence references. |
| Regenerate Generated Artifacts | **Defer** | Regeneration may be appropriate later, but only through a small, human-reviewed PR using approved tooling and recorded command, inputs, reviewer, rationale, and validation results. |
| No Action Required | **Not selected** | A decision note is still useful because `generated/audit_snapshot.json` contains generation-time values that may be misread as fresh post-migration output. |

## Recommendation

**Preserve Current Generated Artifacts for v0.1.0.**

Do not regenerate `generated/audit_snapshot.json` before v0.1.0 release.

The current snapshot should remain unchanged and should be treated as historical generated evidence, not as a fresh post-migration recalculation. The inspected snapshot includes the scoped historical record IDs and lists `records/pending/`, `records/verified/`, and `records/archived/` as source directories. It does not list per-record paths for the scoped migrated historical records.

This recommendation follows the post-migration generated artifact review: the existing snapshot preserves generation-time context, while regeneration would require explicit tooling, input, and validation controls. It also aligns with the final readiness review, which allows generated artifacts to remain historical evidence unless maintainers require fresh post-migration regeneration for release evidence.

## Risks

Risks of preserving current generated artifacts:

- Reviewers or tools may mistake `generated/audit_snapshot.json` for a fresh post-migration recalculation.
- The snapshot timestamp, `file_count`, and `sha256_manifest_hash` may not represent the current repository tree after historical record migration.
- The presence of both `records/verified/` and `records/archived/` in `source_directories` may require explanation during review.
- Future contributors may attempt ad hoc regeneration without recording approved tooling, inputs, reviewer, rationale, or validation results.
- Generated artifact reconciliation may remain coupled to unresolved future decisions about archived metadata, hash manifests, QR artifacts, release evidence, and documentation references.

Risks of regenerating before v0.1.0:

- A regenerated file could overwrite preserved historical generated evidence without adequate legacy context.
- Regeneration could produce unrelated generated diffs if tooling reads more than the intended source scope.
- A new timestamp, manifest hash, or file count could be misread as release approval or as proof of current validation.
- Regeneration without a documented command, inputs, reviewer, rationale, and validation results would weaken auditability.
- Any generator-side change touching records, hash files, QR artifacts, release evidence, schemas, validators, workflows, runtime, signing, federation, policy, or canonical artifacts would exceed this decision scope.

## v0.1.0 Impact

This decision should not block a conservative v0.1.0 advisory release if maintainers accept the current generated snapshot as historical generated evidence and disclose the limitation.

For v0.1.0:

- `generated/audit_snapshot.json` remains unchanged.
- No generated artifact reconciliation is required before release.
- No generated artifact should be treated as a current post-migration recalculation unless regenerated through a separate reviewed process.
- Final release language should remain advisory, early-stage, and non-production.
- Required release checks and human-supervised validation evidence remain necessary for the release decision.

This decision is consistent with preserving legacy path-bound evidence for v0.1.0 rather than introducing late generated artifact churn.

## Future Roadmap

If maintainers later decide that fresh generated artifacts are needed, use a future small, scoped, human-reviewed PR.

That PR should:

1. Identify the approved command or tooling path for regenerating `generated/audit_snapshot.json`.
2. Record the exact source inputs and source directories used by the generator.
3. Preserve or cite the current snapshot values before replacement.
4. Run only the approved generator needed for the audit snapshot, avoiding broad generated artifact rewrites.
5. Review the generated diff for `file_count`, `record_ids`, `sha256_manifest_hash`, `snapshot_timestamp`, and `source_directories`.
6. Confirm that records, hash files, QR artifacts, release evidence, schemas, validators, workflows, runtime, signing logic, federation logic, policy files, and canonical artifacts remain unchanged unless separately approved.
7. Record the command, inputs, reviewer, rationale, date, and validation results.
8. Keep generated artifacts non-canonical and advisory unless repository governance explicitly changes their status.

Future reconciliation may also coordinate with archived metadata, legacy hash manifests, QR artifacts, release evidence `related_records`, and documentation reference reviews. That follow-up should remain evidence-preserving, human-reviewable, and scoped to HC:// and HC-TRUST-LAYER governance boundaries.

## Decision

**Decision: Preserve Current Generated Artifacts.**

`generated/audit_snapshot.json` should remain unchanged for v0.1.0. No generated artifact reconciliation is required before release. If regeneration is needed later, it should be performed only in a future small, human-reviewed PR using approved tooling and recorded command, inputs, reviewer, rationale, and validation results.
