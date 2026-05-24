# HC-TRUST-LAYER HC:// Verification Status UX Standard

## Purpose

This document defines a documentation-only UX baseline for verification status communication in HC-TRUST-LAYER and HC:// MVP-1 surfaces.

## PASS / WARNING / FAIL Concepts

Verification status semantics should remain simple and bounded:

- **PASS**: visible checks within displayed scope are materially consistent
- **WARNING**: uncertainty, ambiguity, replay risk, or partial continuity signals are present
- **FAIL**: visible inconsistency or verification mismatch is present in displayed scope

Status labels are advisory and do not replace human-supervised validation.

## Confidence Communication

Confidence statements should:

- describe strength of visible evidence
- avoid certainty inflation
- declare scope limits clearly

Recommended confidence tiers may be shown as high/medium/low only when linked to visible evidence rationale.

## Risk Communication

Risk messaging should be plain-language and action-oriented:

- what risk was observed
- why it matters to trust interpretation
- what escalation action is recommended

## Provenance Visibility

Users should be able to see concise provenance context:

- origin and revision relationship pointers
- continuity indicators or gap markers
- canonical record linkage context

## Validator Visibility

Status views should show validator context in readable form:

- validator identity reference
- review time context
- summarized rationale pointer availability

## Replay Visibility

Status views should expose replay warnings prominently with:

- warning label
- short explanation
- escalation path to human-supervised review

## Dispute Visibility

Status views should clearly indicate when dispute state affects interpretation.

Dispute indicators should include a plain-language unresolved-state note.

## Audit Visibility

Status views should provide audit trail visibility cues:

- latest relevant review timestamp
- change continuity signals
- reviewer-action traceability pointers

## Trust Snapshot Visibility

Status views should expose trust snapshot context:

- snapshot timestamp
- scope boundary summary
- note when newer related evidence may exist

## Public Readability Goals

Public-facing verification status views should optimize for:

- non-technical comprehension
- short label consistency
- mobile-first readability
- explicit uncertainty boundaries

## Related References

- `docs/trust-result-standard.md`
- `docs/provenance-timeline-format.md`
- `docs/replay-warning-standard.md`
- `docs/mvp-1-user-flow.md`
