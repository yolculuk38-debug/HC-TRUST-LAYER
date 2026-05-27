# HC:// Verification Result States (Self-Service Prototype)

This document standardizes public-facing HC:// verification result states for the self-service verification prototype in HC-TRUST-LAYER.

Scope boundaries:

- Advisory-only verification output.
- No canonical schema changes.
- No validator or guard weakening.
- No backend upload or storage.
- Human-supervised validation remains required for consequential decisions.

## Purpose

Use these states to keep verification UX consistent, mobile-readable, and low-confusion while preserving trust-kernel boundaries, provenance clarity, and audit trail continuity.

## Standardized result states

### 1) LOCAL PREVIEW

- **Meaning:** Processing happened locally in-browser for preview purposes.
- **User interpretation:** "This check ran on my device as a preview step."
- **Does NOT mean:** registration, canonical record creation, or institutional certification.
- **Recommended UI wording:** "Local preview completed on this device."
- **Badge style guidance:** Neutral info badge (outline), medium emphasis, always paired with helper text.

### 2) HASH GENERATED

- **Meaning:** A SHA-256 digest was generated from provided text/file input.
- **User interpretation:** "I now have a fingerprint for comparison or next-step review."
- **Does NOT mean:** truth verification, authorship proof, or legal evidence by itself.
- **Recommended UI wording:** "SHA-256 fingerprint generated."
- **Badge style guidance:** Neutral-confirmation badge with monospace hash display nearby.

### 3) NOT REGISTERED

- **Meaning:** No canonical record registration happened in this flow.
- **User interpretation:** "This is not registered in canonical records yet."
- **Does NOT mean:** invalid content, false content, or failed integrity.
- **Recommended UI wording:** "Not registered in canonical records (preview route only)."
- **Badge style guidance:** Caution-neutral badge, persistent visibility in result summary.

### 4) ADVISORY ONLY

- **Meaning:** The result is guidance for review, not an autonomous decision.
- **User interpretation:** "This supports review but does not decide truth or authority."
- **Does NOT mean:** final verification authority or autonomous governance finality.
- **Recommended UI wording:** "Advisory result: human review remains required."
- **Badge style guidance:** High-visibility advisory badge with boundary icon/text.

### 5) REVIEW REQUIRED

- **Meaning:** Human-supervised validation is required before consequential use.
- **User interpretation:** "People must review this before important decisions."
- **Does NOT mean:** immediate rejection or definitive failure.
- **Recommended UI wording:** "Review required before consequential interpretation."
- **Badge style guidance:** Attention badge (amber/orange) with always-visible explanation.

### 6) CONTINUITY AVAILABLE

- **Meaning:** Expected provenance or audit trail continuity references are available.
- **User interpretation:** "Continuity evidence can be inspected."
- **Does NOT mean:** full truth certainty or complete ecosystem coverage.
- **Recommended UI wording:** "Continuity references available for review."
- **Badge style guidance:** Positive-neutral continuity badge plus link to provenance details.

### 7) CONTINUITY NOT AVAILABLE

- **Meaning:** Expected continuity links are currently missing or incomplete.
- **User interpretation:** "Continuity evidence is missing here; use caution."
- **Does NOT mean:** automatic fraud, guilt, or content falsity.
- **Recommended UI wording:** "Continuity not available in this preview."
- **Badge style guidance:** Caution badge with direct "what to do next" guidance.

### 8) GENERATED ARTIFACT

- **Meaning:** Output is generated/non-canonical support material.
- **User interpretation:** "This artifact helps review but is not the canonical record."
- **Does NOT mean:** canonical record authority.
- **Recommended UI wording:** "Generated artifact (non-canonical support output)."
- **Badge style guidance:** Secondary badge with explicit non-canonical label.

### 9) CANONICAL RECORD

- **Meaning:** Label reserved for verified canonical record surfaces only.
- **User interpretation:** "This references canonical record boundaries when explicitly linked."
- **Does NOT mean:** universal truth guarantee, legal certification, or authorship certainty.
- **Recommended UI wording:** "Canonical record reference (scope-bound)."
- **Badge style guidance:** Distinct boundary badge; use only when canonical record pointer is present.

### 10) PREVIEW ROUTE

- **Meaning:** The route is a non-canonical preview path for local verification UX.
- **User interpretation:** "This link is for preview flow, not final registration."
- **Does NOT mean:** submission, registration completion, or backend persistence.
- **Recommended UI wording:** "Preview route generated (non-canonical)."
- **Badge style guidance:** Route/status badge with copy affordance and boundary note.

## Mobile readability guidance

- Keep state labels uppercase and short.
- Show one primary state row, then expandable details.
- Use readable spacing and tap-safe controls.
- Keep hash and route text in wrap-safe monospace blocks.
- Avoid long banner stacks; group related signals into one compact panel.

## Accessibility guidance

- Never rely on color alone; pair badges with explicit state text.
- Maintain high-contrast text/background combinations.
- Use semantic headings and clear reading order.
- Use `aria-live` only for dynamic result outputs that change after user action.
- Keep warning language plain and concise for screen-reader clarity.

## Low-confusion wording guidance

- Prefer "verification preview" instead of "verification complete."
- Prefer "supports review" instead of "proves."
- Always separate integrity signal, continuity signal, and review requirement.
- Keep one sentence for meaning and one sentence for limitation.

## Anti-authority overclaim prevention guidance

Never present these states as:

- truth verification
- authorship proof
- legal certification
- AI detection certainty
- autonomous final decision

Always include a persistent notice:

"HC:// self-service verification is advisory-only and requires human-supervised validation for consequential decisions."

## Lightweight example result panels

### A) Text verification panel

- **Primary state:** HASH GENERATED
- **Supporting states:** LOCAL PREVIEW, PREVIEW ROUTE, ADVISORY ONLY, REVIEW REQUIRED
- **Example copy:** "SHA-256 fingerprint generated from text input. Advisory-only preview; review required before consequential interpretation."

### B) Image verification panel

- **Primary state:** HASH GENERATED
- **Supporting states:** LOCAL PREVIEW, NOT REGISTERED, CONTINUITY AVAILABLE or CONTINUITY NOT AVAILABLE, ADVISORY ONLY
- **Example copy:** "Image fingerprint generated locally. Registration is separate. Continuity status shown for review context."

### C) Document verification panel

- **Primary state:** HASH GENERATED
- **Supporting states:** LOCAL PREVIEW, NOT REGISTERED, GENERATED ARTIFACT, REVIEW REQUIRED
- **Example copy:** "Document fingerprint generated for advisory review. This preview output is non-canonical and requires human-supervised validation."

## Implementation note

These states are UX-standardization guidance for the self-service prototype and do not alter canonical records, validator behavior, signing semantics, federation behavior, or policy evaluator behavior.


## Related visual examples

- `docs/visual-verification-signals.md`
- `docs/verified-ai-validator-model.md`
- `docs/authenticated-ai-validator-access.md`
- `docs/accountability-defense-layer.md`
- `docs/federated-oversight-model.md`
- `docs/public-verification-disputes.md`
- `docs/immutable-state-history-model.md`
- `docs/foundation/trust-taxonomy-and-terminology.md`
