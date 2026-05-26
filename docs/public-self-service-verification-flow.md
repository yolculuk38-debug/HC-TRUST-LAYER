# Public Self-Service Verification Flow (MVP)

This document defines the first minimal HC:// self-service verification flow for normal users in HC-TRUST-LAYER.

## Scope and constraints

- Documentation-only guidance.
- Non-canonical artifacts only.
- No canonical schema changes.
- No validator or guard weakening.
- No backend upload or storage in MVP.
- No private data collection in MVP.
- Advisory-only verification posture remains required.
- Human-supervised validation remains required for consequential decisions.

## MVP goal

Provide a mobile-readable, low-friction first public flow where a user can submit text or a file locally, generate a SHA-256 digest in the browser, and view an HC:// verification preview with clear advisory boundaries.

## MVP user flow

1. **Select input mode**
   - User chooses either:
     - enter text, or
     - select a local file.

2. **Local-only SHA-256 generation**
   - Browser computes SHA-256 locally on-device.
   - No upload is performed.
   - Input content does not leave the user device in this MVP stage.

3. **Hash visibility**
   - User sees the resulting SHA-256 hash clearly.
   - Copy action is available for manual review workflows.

4. **QR route and verification preview**
   - User sees an HC:// QR/verification preview route derived from local hash context.
   - Preview is explicitly marked advisory and non-registration.

5. **Advisory signal explanation**
   - User sees process-language signal guidance (for example: HC REVIEW / HC PARTIAL style advisory posture for preview-only context).
   - UI explains that this is verification assistance and not objective truth validation.

6. **Next-step boundary explanation**
   - User sees explicit note that registration and human review are separate steps.
   - UI points to optional follow-up paths without implying automatic canonical inclusion.

## What MVP does not do

This MVP flow must not claim or imply any of the following:

- no upload of user content
- no backend storage
- no legal certification
- no authorship proof
- no objective truth claim
- no AI certainty

Additional boundary clarifications:

- No canonical record is created by preview alone.
- No autonomous policy finality is provided.
- No consequential decision should rely on preview output without human-supervised validation.

## UX and messaging requirements (mobile-first)

- Keep text-first UI blocks for small screens.
- Show summary first: hash, preview route, advisory boundary.
- Keep boundary language always visible:
  - advisory-only verification
  - no truth guarantee
  - human-supervised validation required for consequential use
- Use concise wording and avoid institutional-authority tone.

## Suggested MVP UI sections

1. **Input** (text/file toggle)
2. **Local hash result** (SHA-256 output)
3. **HC:// preview route + QR** (preview only)
4. **Advisory meaning** (scope-bound process signal)
5. **Next steps** (optional draft/export/review paths)

## Future implementation stages (proposed)

### Stage 1 — Local-only hash preview

- Browser-only text/file hashing.
- Advisory preview route generation.
- No upload, no backend state.

### Stage 2 — Optional record draft export

- User can export a non-canonical draft package locally.
- Export supports later reviewer-assisted intake.
- Still no automatic canonical registration.

### Stage 3 — Optional human-reviewed registration

- Human-supervised intake path can review exported draft.
- Reviewers validate scope, provenance context, and policy fit before any canonical action.

### Stage 4 — Optional public explorer inclusion

- After approved registration workflow, record visibility can be included in explorer pathways.
- Explorer visibility remains advisory and evidence-linked.

## Trust-boundary reminders

- HC:// preview flow is a verification assistance interface, not a truth oracle.
- Hash equivalence indicates integrity match scope only.
- Human-supervised validation remains mandatory for consequential interpretation.

## Related references

- `docs/self-service-verify.html` (mobile-first step-by-step prototype with local-only advisory verification boundaries)
- `docs/public-onboarding-model.md`
- `docs/content-verification-signal-model.md`
- `docs/public-verification-boundaries.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/self-service-smoke-test.md`
