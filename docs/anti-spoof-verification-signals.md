# Anti-Spoof Verification Signals

This document defines anti-spoof guidance for visible HC:// verification signals in HC-TRUST-LAYER.

Verification rendering in this repository remains advisory-only and requires human-supervised validation for consequential decisions.

## Scope and constraints

- Documentation-only guidance.
- No canonical schema changes.
- No validator or guard weakening.
- No signing, federation, or policy boundary changes.
- No production-readiness, truth-guarantee, or institutional-certification claims.

## Signal definitions

### Official HC:// verification signal

An **official HC:// verification signal** is a repository-aligned, advisory display that:

- references the canonical record context,
- discloses generated artifact usage when present,
- discloses continuity state (including incomplete continuity), and
- displays human-review-required language.

Official signal rendering communicates process status, not autonomous authority.

### Unofficial or fake verification signal risk

An **unofficial/fake verification signal** is any copied, modified, or impersonated signal that appears to represent HC:// verification without repository-aligned boundary language and continuity context.

Risk includes misleading users into treating non-authoritative output as final authority.

### Generated artifact warning visibility

A **generated artifact warning** must be visibly rendered whenever non-canonical generated outputs are used in the view.

The warning should be close to the displayed signal state so users do not confuse generated artifacts with canonical records.

### Continuity incomplete visibility

A **continuity incomplete** state must be explicit and high-visibility when continuity references are missing, stale, or inconsistent.

Do not downgrade this state to decorative or low-contrast presentation.

### Advisory verification rendering rules

Advisory verification rendering must:

- preserve advisory-only interpretation,
- prevent certified-truth appearance,
- preserve human-supervised validation requirement,
- keep provenance and audit trail context inspectable.

## Verification rendering guidance

Every HC:// verification surface should make a clear distinction between:

1. **canonical record** (authoritative record boundary)
2. **generated artifact** (non-canonical derived output)
3. **advisory verification** (process evidence only)
4. **human review required** (required for consequential use)

Rendering guidance:

- Prefer text-first status labels over icon-only status communication.
- Avoid single green-check UX patterns that imply final authority.
- Avoid “certified truth” or equivalent visual posture.
- Keep warning language adjacent to status language.
- Ensure canonical record links are visible and reviewable.
- Preserve mobile-readable line length and hierarchy.

## Anti-spoof guidance

### Fake verification pages

- Confirm official domain and expected route before interpretation.
- Treat unfamiliar page framing or missing boundary language as suspicious.

### Copied screenshots

- Screenshots are non-authoritative snapshots and can be context-stripped.
- Re-open the canonical record and current verification view before relying on screenshot claims.

### Modified QR links

- Treat QR entry as routing only, not trust proof.
- Confirm destination domain, route, record identifier, and hash context.

### Fake explorer pages

- Validate that explorer-style pages map to repository-known continuity references.
- If references cannot be reconciled with repository evidence, treat as untrusted.

### Stale verification artifacts

- Generated artifacts can be outdated even when visually consistent.
- Re-check canonical record and current continuity references before consequential use.

## Lightweight example signal rendering

The following pattern is text-first, static-site compatible, mobile-friendly, and accessibility-friendly.

```text
HC:// Verification Signal
Status: Advisory Verification

Boundary:
- Canonical Record: Visible
- Generated Artifact: Present (non-canonical)
- Continuity: Incomplete
- Human Review: Required

Warning:
This view is advisory process evidence.
It is not certified truth, legal authority, or autonomous finality.
```

Accessibility notes:

- Do not rely on color alone for meaning.
- Use explicit text labels for all state transitions.
- Keep warning and boundary text available to screen readers.

## Related references

- `docs/verification-signal-model.md`
- `docs/public-verification-boundaries.md`
- `docs/qr-verification-security-model.md`
- `docs/anti-spoofing-foundations.md`
- `docs/HC_CONTROL_PANEL.md`
