# HC:// Visual Verification Signal Examples

This document defines first-pass, static visual verification signal examples for HC:// public-facing verification UX in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only examples.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator, guard, signing, federation, or policy behavior changes.
- No backend upload or storage.
- Human-supervised validation remains required.

## Purpose

Provide a standardized visual vocabulary for public verification previews that is mobile-readable, low-confusion, and aligned with anti-overclaim boundaries.

## Standard visual signal examples

Each signal below includes: example badge, example label, example mobile card, intended user interpretation, and misuse prevention note.

---

### 1) LOCAL PREVIEW

- **Example badge:** `LOCAL PREVIEW` (neutral outline badge, info icon).
- **Example label:** `Processed locally on this device.`
- **Example mobile card:**
  - **Header:** `Local preview completed`
  - **Body:** `This result was generated in-browser for preview use.`
  - **Footer note:** `No upload or registration happened in this step.`
- **Intended user interpretation:** Processing happened locally as a preview step.
- **Misuse prevention note:** Do not style this as authoritative registration or final verification.

### 2) HASH GENERATED

- **Example badge:** `HASH GENERATED` (neutral-confirmation badge, hash icon).
- **Example label:** `SHA-256 fingerprint generated.`
- **Example mobile card:**
  - **Header:** `Fingerprint ready`
  - **Body:** `A SHA-256 digest is available for comparison and review routing.`
  - **Footer note:** `Hash generation alone does not prove truth or authorship.`
- **Intended user interpretation:** A stable fingerprint is available for next-step review.
- **Misuse prevention note:** Do not frame digest creation as legal evidence or factual certainty.

### 3) NOT REGISTERED

- **Example badge:** `NOT REGISTERED` (caution-neutral badge, boundary icon).
- **Example label:** `No canonical record registration in this flow.`
- **Example mobile card:**
  - **Header:** `Registration not present`
  - **Body:** `This preview does not create or submit a canonical record.`
  - **Footer note:** `Registration is separate from local verification preview.`
- **Intended user interpretation:** Preview exists without canonical record registration.
- **Misuse prevention note:** Do not imply this equals falsity, abuse, or automatic failure.

### 4) ADVISORY ONLY

- **Example badge:** `ADVISORY ONLY` (high-visibility advisory badge, info boundary icon).
- **Example label:** `Supports review; does not decide.`
- **Example mobile card:**
  - **Header:** `Advisory verification`
  - **Body:** `This result supports evidence review and routing context.`
  - **Footer note:** `Consequential decisions require human-supervised validation.`
- **Intended user interpretation:** Output is guidance, not autonomous authority.
- **Misuse prevention note:** Do not use authority emblems, seals, or final-decision language.

### 5) REVIEW REQUIRED

- **Example badge:** `REVIEW REQUIRED` (attention badge, review icon).
- **Example label:** `Human-supervised validation required.`
- **Example mobile card:**
  - **Header:** `Review step required`
  - **Body:** `People must review scope, provenance, and context before consequential use.`
  - **Footer note:** `This is not an automatic approval or rejection signal.`
- **Intended user interpretation:** A human review step is mandatory.
- **Misuse prevention note:** Do not present this as punitive or as a final negative ruling.

### 6) CONTINUITY AVAILABLE

- **Example badge:** `CONTINUITY AVAILABLE` (positive-neutral badge, link-chain icon).
- **Example label:** `Continuity references can be inspected.`
- **Example mobile card:**
  - **Header:** `Continuity references found`
  - **Body:** `Expected provenance and audit trail pointers are available for review.`
  - **Footer note:** `Availability of references is not a universal truth guarantee.`
- **Intended user interpretation:** Supporting provenance continuity references are present.
- **Misuse prevention note:** Do not represent continuity presence as complete certainty.

### 7) CONTINUITY NOT AVAILABLE

- **Example badge:** `CONTINUITY NOT AVAILABLE` (caution badge, broken-link icon).
- **Example label:** `Expected continuity references are missing or incomplete.`
- **Example mobile card:**
  - **Header:** `Continuity gap detected`
  - **Body:** `Some expected provenance or audit trail continuity links are not available.`
  - **Footer note:** `Use caution and route to human-supervised validation.`
- **Intended user interpretation:** Continuity evidence is incomplete for this preview context.
- **Misuse prevention note:** Do not equate missing continuity with automatic fraud determination.

### 8) GENERATED ARTIFACT

- **Example badge:** `GENERATED ARTIFACT` (secondary badge, document icon).
- **Example label:** `Non-canonical support output.`
- **Example mobile card:**
  - **Header:** `Generated support artifact`
  - **Body:** `This item supports review and navigation only.`
  - **Footer note:** `It does not replace canonical record boundaries.`
- **Intended user interpretation:** Output is supportive, non-canonical material.
- **Misuse prevention note:** Do not present generated artifacts as canonical records.

### 9) CANONICAL RECORD

- **Example badge:** `CANONICAL RECORD` (distinct boundary badge, record icon).
- **Example label:** `Canonical record reference (scope-bound).`
- **Example mobile card:**
  - **Header:** `Canonical record reference`
  - **Body:** `This view references a canonical record boundary when explicitly linked.`
  - **Footer note:** `Canonical reference does not imply universal truth, legal certification, or authorship certainty.`
- **Intended user interpretation:** A scoped canonical record reference is present.
- **Misuse prevention note:** Do not attach institutional authority styling or legal-certification implications.

### 10) PREVIEW ROUTE

- **Example badge:** `PREVIEW ROUTE` (route/status badge, route icon).
- **Example label:** `Non-canonical preview link generated.`
- **Example mobile card:**
  - **Header:** `Preview route available`
  - **Body:** `A local verification preview route is available for demo-safe linking.`
  - **Footer note:** `Route generation is not registration or backend persistence.`
- **Intended user interpretation:** A preview-only link can be shared for demo flow.
- **Misuse prevention note:** Do not label preview routes as final verification endpoints.

## Example panel layouts

These are lightweight, static/demo-safe layout references.

### A) QR verification result panel

- **Top row:** `ADVISORY ONLY` + `REVIEW REQUIRED`
- **Middle row:** primary result text, hash excerpt, and continuity state
- **Bottom row:** `PREVIEW ROUTE` action and provenance/audit trail links
- **Persistent note:** `Advisory-only verification; human-supervised validation required for consequential decisions.`

### B) Social-post verification panel

- **Top row:** `LOCAL PREVIEW` + `HASH GENERATED`
- **Middle row:** post reference summary and continuity state (`CONTINUITY AVAILABLE` or `CONTINUITY NOT AVAILABLE`)
- **Bottom row:** non-canonical artifact notice and reviewer handoff copy
- **Persistent note:** clarify distribution context changes and advisory interpretation boundaries.

### C) Document verification panel

- **Top row:** `HASH GENERATED` + `NOT REGISTERED`
- **Middle row:** document fingerprint block, provenance pointer summary, and review instruction
- **Bottom row:** `GENERATED ARTIFACT` marker and optional canonical reference slot
- **Persistent note:** no truth certification or legal-certification implication.

### D) Image verification panel

- **Top row:** `LOCAL PREVIEW` + `ADVISORY ONLY`
- **Middle row:** image fingerprint summary and continuity state
- **Bottom row:** preview-route copy action and review-required reminder
- **Persistent note:** authorship and AI-detection certainty are out of scope.

## Anti-overclaim guidance

To preserve public trust and boundary clarity:

- Avoid authority styling (for example: medals, seals, government-like insignia, courtroom-like verdict motifs).
- Avoid wording such as `truth certified`, `officially true`, `forensically proven`, or equivalent certainty framing.
- Avoid fake government-style semantics or pseudo-regulatory language.
- Preserve advisory framing in every panel with a visible, persistent notice.

## Accessibility guidance

- Ensure readable contrast between text, background, and badges.
- Optimize for mobile readability with short labels, stacked sections, and tap-safe controls.
- Pair icon + text for every state signal.
- Ensure color-independent meaning by using explicit text and consistent symbols.

## Implementation notes

- These examples are design guidance only and remain non-canonical artifacts.
- This document does not change schemas, validators, policy evaluator behavior, signing logic, federation behavior, or canonical records.
- Human-supervised validation remains required for consequential decisions.

## Related documents

- `docs/verification-result-states.md`
- `docs/public-onboarding-model.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/verified-ai-validator-model.md`
- `docs/self-service-verify.html`
