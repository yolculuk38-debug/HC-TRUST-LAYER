# HC-TRUST-LAYER HC:// Replay Warning Standard (MVP-1)

## Purpose

This document defines a documentation-only replay warning communication standard for HC-TRUST-LAYER and HC:// MVP-1 trust UX surfaces.

## Replay Warning Overview

A replay warning is a risk-oriented signal indicating potential suspicious reuse, duplicate propagation, or provenance continuity inconsistency.

Replay warnings are advisory and require human-supervised validation.

## Replay Severity Levels

Recommended documentation severity levels:

- **LOW**: minor anomaly requiring awareness
- **MEDIUM**: notable anomaly requiring reviewer follow-up
- **HIGH**: material anomaly requiring immediate human-supervised escalation

Severity levels communicate triage priority, not forensic certainty.

## Duplicate Propagation Concepts

Replay warning messaging should explain duplicate propagation in plain language:

- repeated appearance patterns
- scope of observed duplication
- whether context appears expected or suspicious

## Metadata Inconsistency Warnings

Replay warnings should highlight metadata inconsistency patterns such as mismatched fields or unexpected context shifts across linked records.

## Provenance Discontinuity Warnings

Replay warnings should identify provenance discontinuity signals where chronology or linkage context cannot be reliably followed in displayed scope.

## Human Review Escalation Guidance

Replay warning states should include clear escalation guidance:

- review affected timeline and provenance entries
- inspect validator context and rationale pointers
- document reviewer interpretation in audit trail
- route high-severity ambiguity to human-supervised validation workflow

## Related References

- `docs/trust-result-standard.md`
- `docs/verification-status-ux.md`
- `docs/provenance-timeline-format.md`
- `docs/public-verification-flow.md`
