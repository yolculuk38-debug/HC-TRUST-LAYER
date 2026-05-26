# Verification Signal Model

This document defines a safe, advisory-only visible verification signal model for HC:// in HC-TRUST-LAYER.

## Scope and constraints

- Documentation-only guidance.
- Non-canonical artifacts only.
- No canonical schema changes.
- No validator or guard weakening.
- No autonomous trust guarantees.
- Human-supervised validation remains required.

## Definitions

### verification signal

A **verification signal** is a visible indicator that one or more documented HC:// verification processes completed for a given review scope.

A verification signal is process evidence, not truth authority.

### advisory verification badge

An **advisory verification badge** is a compact visual label that communicates advisory verification status to operators and reviewers.

The badge is informational and must not be presented as institutional certification, legal authorization, or objective truth proof.

### integrity signal

An **integrity signal** indicates that integrity-oriented checks (for example hash and byte-consistency checks) completed successfully for the stated scope.

### provenance continuity signal

A **provenance continuity signal** indicates that expected provenance links were observed across referenced records and non-canonical continuity artifacts for the stated scope.

### audit continuity signal

An **audit continuity signal** indicates that expected audit trail references were present and traceable for the stated scope.

### generated artifact warning

A **generated artifact warning** is an explicit marker that references include generated, non-canonical artifacts that support visibility but do not replace canonical record boundaries.

### human-review-required signal

A **human-review-required signal** is an explicit marker that consequential trust decisions still require human-supervised validation, even when process checks complete.

## Boundary clarifications

Verification signals are constrained and must be interpreted narrowly:

- Verification signal is **NOT proof of truth**.
- Verification signal is **NOT identity authority**.
- Verification signal is **NOT legal certification**.
- Signals indicate completed verification processes only within their declared scope.

## Example signal states

Use clear, small, text-forward state labels:

- **integrity verified**
- **advisory verified**
- **continuity incomplete**
- **generated artifact**
- **human review required**
- **verification partial**

## Recommended display model

1. Show a primary advisory verification badge.
2. Show a compact list of subordinate signals (integrity, provenance continuity, audit continuity).
3. Always show generated artifact warning when generated references are included.
4. Always show human-review-required signal for consequential decisions.
5. Keep language concise, explicit, and non-authoritative.

## Lightweight text-only UI mock (mobile-friendly, static-site compatible)

```text
HC:// Verification Summary
--------------------------
Status: Advisory Verified
Signals:
- Integrity: Verified
- Provenance Continuity: Incomplete
- Audit Continuity: Verified
Warnings:
- Generated Artifact
- Human Review Required

Interpretation:
Completed process checks were detected for listed signals.
This summary is advisory-only and is not proof of truth,
identity authority, or legal certification.
```

## Implementation boundary guidance

- Keep signal artifacts outside canonical record paths.
- Keep signal rendering deterministic and text-first for mobile readability.
- Keep signal language aligned with HC-TRUST-LAYER advisory-only verification posture.
- Do not convert advisory signals into autonomous decision gates.

## Related documents

- `docs/public-verification-boundaries.md`
- `docs/federation-readiness-model.md`
- `docs/HC_CONTROL_PANEL.md`

For anti-spoof signal presentation patterns, unofficial/fake signal risks, and accessibility-oriented rendering guidance, see `docs/anti-spoof-verification-signals.md`.

For content-class-specific signals (text, quote, image, video, document, social media, and archived record) with badge/color/QR semantics and provenance inspection boundaries, see `docs/content-verification-signal-model.md`.
