# Release Evidence Lifecycle

## Purpose

Release evidence records document repository-backed release evidence for HC-TRUST-LAYER releases. They help maintainers and reviewers preserve release context, validation references, reviewer evidence, limitations, and audit trail continuity for HC:// verification infrastructure.

Release evidence records are advisory evidence artifacts. They do not create production readiness, security certification, truth finality, forensic certainty, autonomous governance, or live public verifier guarantees.

## Record Lifecycle

Release evidence records move through reviewable states that preserve uncertainty until sufficient evidence and human-supervised validation are available.

1. **pending**
   - Use when a release evidence record has been drafted but required evidence is incomplete, unknown, or still under maintainer review.
   - Pending records may contain allowed unknown markers while release candidate evidence, checklist references, validation outcomes, or reviewer evidence are being collected.
2. **reviewed**
   - Use when maintainers or reviewers have inspected the record for completeness, consistency, and scope, but the record is not yet accepted as verified release evidence.
   - Reviewed records should identify remaining blockers, unresolved unknowns, and required follow-up before verification.
3. **verified**
   - Use only after required evidence is present, checks and outcomes are recorded, protected-path and trust-kernel impact are evaluated, and human-supervised validation is complete.
   - Verified release evidence remains subject to challenge, correction, and audit review; it does not create production guarantees or forensic certainty.
4. **archived**
   - Use when a release evidence record is superseded, retained for historical reference, or moved out of active release review.
   - Archived records should preserve provenance, reason for archival, and links to any successor or correction records when applicable.

## Current v0.1.0 Release Record

The current v0.1.0 release evidence record is `HC-RELEASE-2026-0001`.

- Current location: `records/pending/HC-RELEASE-2026-0001.json`
- Current status: `pending`
- Purpose: initial v0.1.0 release evidence record
- Validation boundary: human-supervised validation remains required before the record can move to verified release evidence.

## Required Evidence Before Verification

Before a release evidence record can move to `verified`, it should include or reference the following evidence:

- Release candidate commit.
- Tag name.
- Release notes path.
- Release checklist path.
- Checks run and outcomes.
- Protected-path status.
- Trust-kernel impact status.
- Human-supervised validation status.
- Reviewer or approver evidence.
- Known limitations.

## Allowed Unknown Markers

The following unknown markers are allowed while a release evidence record remains `pending`:

- `pending`
- `not_recorded`
- `null`

These markers are temporary review aids. They should not remain in fields required for verification after a record leaves `pending` unless a future schema or protocol rule explicitly allows that use and human-supervised validation accepts the limitation.

## Record Type Constraint

The current `record-v1` schema does not yet support `record_type = release_evidence`.

Release evidence records currently use the following schema-compatible representation:

- `record_type = protocol_note`
- `witness_type = human`

Adding `release_evidence` as a first-class schema type requires a future schema or protocol change and human-supervised validation. Until then, release evidence records should remain schema-compatible and should clearly state their release evidence purpose in record content and documentation.

## QR / Public Verifier Boundary

Release records may become QR targets after validation. QR target generation or regeneration should occur only after the release record has sufficient evidence, review status, and human-supervised validation for the intended release context.

`docs/verify.html` is demo-only. v0.1.0 does not provide a hosted general public verifier. Non-demo `/verify/{record_id}` routes are advisory or navigation placeholders unless they are separately deployed, validated, and documented with their operational boundaries.

## Historical Records

Historical records must be preserved for provenance and should not be deleted or rewritten. This includes historical records such as:

- `HC-TEST-2026-0001`
- `HC-CHATGPT-2026-0001`
- `HC-CHATGPT-2026-0002`

These records may later be marked historical, test, or demo records, or archived through a separate maintainer-approved process. Any such process should preserve provenance, audit trail continuity, and review context.

## Correction Policy

Release evidence corrections must preserve history rather than erase it.

- Do not erase history.
- Preserve the audit trail.
- State the reason for each correction.
- Use human-supervised validation for sensitive release evidence corrections.

Corrections should be reviewable, attributable, and scoped to the specific issue being corrected. When a correction affects release interpretation, reviewer evidence, protected-path status, trust-kernel impact, or public verification expectations, maintainers should document the validation boundary and any remaining uncertainty.

## Future Work

Future release evidence lifecycle work may include:

- First-class `release_evidence` schema type.
- Release evidence checklist automation.
- QR target regeneration after a verified release record.
- Public Explorer integration.
