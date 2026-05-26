# Public Verification Onboarding Model

This document defines a lightweight, mobile-first HC:// public verification onboarding experience for HC-TRUST-LAYER.

## Scope and constraints

- Documentation-only guidance.
- Non-canonical artifacts only.
- No canonical schema changes.
- No validator or guard weakening.
- No blockchain, token, or truth-guarantee claims.
- Advisory-only verification posture remains required.
- Human-supervised validation remains required.

## Onboarding goal

Enable normal users to understand HC:// verification outcomes quickly while preserving strict verification boundaries, provenance visibility, and audit trail continuity.

## Public self-service entry point

Try local verification preview at `docs/self-service-verify.html`.

- **No upload**
- **Browser-side SHA-256**
- **Preview only, not registration**

This entry point is mobile-friendly and supports local-only, advisory verification preview before human-supervised validation.

## Public onboarding flow (lightweight)

1. **QR scan**
   - User scans an HC:// QR code from content, packaging, or a shared verification card.
   - QR routes the user to a verification page for a specific record/hash context.

2. **Verification page**
   - Page opens with a concise summary first, then expandable details.
   - The page remains text-forward, mobile-readable, and static-site compatible.

3. **Visible verification signal**
   - User sees a clear state label (for example: HC VERIFIED, HC PARTIAL, HC REVIEW).
   - Signal communicates process status only, not objective truth authority.

4. **Continuity result**
   - User sees whether expected continuity links are complete, partial, or missing.
   - Continuity state must be explicit and separated from integrity status.

5. **Provenance visibility**
   - User can inspect provenance references in plain language.
   - Record link, hash comparison result, and audit trail context remain visible.

6. **Advisory explanation**
   - Page explains that verification is advisory-only and scope-bound.
   - Page clarifies that passing checks do not prove truth, intent, or full context.

7. **Human review notice**
   - Page displays a persistent human-supervised validation notice for consequential decisions.
   - Notice is always visible in partial/unknown/risk states and recommended in all states.

## Simplified public-facing language

Use direct, non-technical wording while preserving HC:// boundary semantics.

### Plain-language integrity explanation

- Preferred: "Integrity means the file we checked still matches the recorded fingerprint."
- Avoid: deeply technical wording as the primary explanation.

### Plain-language provenance explanation

- Preferred: "Provenance shows where this item came from and how it connects to earlier records."
- Avoid: abstract graph terms without a short plain-language bridge.

### Plain-language advisory verification explanation

- Preferred: "This result is advisory. It helps review process evidence, but people still need to review important decisions."
- Avoid: certainty language that implies automatic truth, legal proof, or institutional authority.

## Lightweight example user journeys

### 1) Image verification

- User scans QR on an image card.
- Verification page shows image hash match status and provenance references.
- User sees: HC VERIFIED + HC REVIEW.
- User can open audit trail links and continuity summary.

### 2) Video verification

- User opens an HC:// link from a video post.
- Verification page shows declared video reference, hash check status, and continuity result.
- If links are missing, page shows HC PARTIAL and asks for human-supervised validation.

### 3) Quote/text verification

- User scans QR beside a quote snippet.
- Page shows whether quote text matches the registered reference scope.
- Provenance context explains when/where the quote reference entered the verification map.

### 4) Document verification

- User opens verification page from a document footer QR.
- Page displays document fingerprint match result and provenance chain pointers.
- User reads a concise advisory message before using the document in consequential review.

### 5) Social media verification

- User taps HC:// badge on a social media card.
- Page shows current signal state, continuity result, and provenance references.
- Page warns that social distribution context can change and still requires human-supervised validation.

## What HC:// can and cannot verify

### HC:// can verify (within declared scope)

- Whether checked content matches a recorded hash/reference input.
- Whether listed provenance links are present and inspectable.
- Whether continuity evidence appears complete, partial, or missing.
- Whether audit trail references are available for review.

### HC:// cannot verify

- Complete certainty about all claims related to the content.
- Full intent, motive, or real-world context.
- Legal authority or institutional certification.
- Original authorship certainty from registration timing alone.
- Final consequential decisions without human-supervised validation.

## Accessibility and mobile-first guidance

### Readable signal states

- Use high-contrast text-forward labels.
- Keep state names short and consistent.
- Pair color with text; do not rely on color alone.

### Simple wording

- Use short sentences and familiar words.
- Prefer "what this means" language next to each signal.
- Keep advisory and boundary notes always visible.

### Low-friction navigation

- Present summary first, details second.
- Keep one primary action per step (open details, open record, open audit trail).
- Minimize taps between signal view and evidence view.

### Static-site compatible rendering

- Keep a no-JavaScript readable baseline.
- Prefer deterministic text sections and expandable details blocks.
- Ensure all critical boundary language renders in static export modes.

## Implementation alignment notes (non-runtime)

- Keep onboarding assets outside canonical record paths.
- Preserve existing validator, terminology, docs drift, and canonical artifact guards.
- Keep onboarding language aligned with advisory-only verification and trust kernel boundaries.

## Related documents

- `docs/verification-signal-model.md`
- `docs/content-verification-signal-model.md`
- `docs/public-verification-boundaries.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/media-verification-showcase.md`
- `docs/public-self-service-verification-flow.md`
- `docs/self-service-verify.html`

## Prototype reference

For an HC:// self-service, local-only verification prototype with step-by-step mobile UX guidance, see `docs/self-service-verify.html`.
