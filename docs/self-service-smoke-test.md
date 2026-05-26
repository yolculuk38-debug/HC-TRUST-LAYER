# Self-Service Verification Smoke Test Plan (MVP)

This smoke test plan provides a repeatable manual check for the public HC:// self-service verification prototype in HC-TRUST-LAYER.

It is documentation-only and preserves current trust boundaries:

- advisory-only verification
- no canonical schema changes
- no validator or guard weakening
- no backend upload or storage
- human-supervised validation for consequential decisions

## Purpose

Use this plan to quickly confirm that the basic self-service verification user flow works on both mobile and desktop.

## Test environment

- Browser: any modern mobile or desktop browser
- Page under test: `docs/self-service-verify.html`
- Connectivity: optional (flow is local-only hashing)

## Manual smoke test steps

1. Open `docs/self-service-verify.html`.
2. Enter sample text in the text input mode.
3. Generate SHA-256 for the sample text.
4. Copy the generated text hash.
5. Inspect the preview route shown in the UI.
6. Select a small local file in file input mode.
7. Generate SHA-256 for the selected file.
8. Confirm the no-upload warning is visible.
9. Confirm the preview-only warning is visible.

## Expected results

- A SHA-256 hash appears after text hashing.
- A preview route appears in the verification preview area.
- An advisory signal appears and remains clearly visible.
- No canonical record is created by this preview flow.
- No upload occurs during text or file hashing.

## Validation notes

- This smoke test verifies UX continuity and trust-boundary messaging only.
- A successful smoke test does not imply production readiness or autonomous trust decisions.
- Consequential interpretation still requires human-supervised validation within HC-TRUST-LAYER workflows.

## Related guidance

- `docs/verification-result-states.md`
