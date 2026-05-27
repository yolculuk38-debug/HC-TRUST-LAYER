# Public Verification Walkthrough (HC:// Self-Service Prototype)

This walkthrough shows how a normal user can run the HC:// self-service verification prototype in HC-TRUST-LAYER from start to finish.

Boundary posture:

- advisory-only verification
- local-only SHA-256 processing
- no upload and no registration
- human-supervised validation required for consequential decisions

## Entry point

Open:

- `docs/self-service-verify.html`

This page is a local preview surface and does not create canonical records.

## End-to-end user flow

1. **Open self-service verification demo**
   - Load `docs/self-service-verify.html` in a mobile or desktop browser.
   - Confirm boundary messaging is visible (**No upload**, **Preview only, not registration**).

2. **Enter sample text**
   - Use text mode.
   - Paste or type a short sample string.

3. **Generate SHA-256**
   - Trigger hash generation.
   - The browser computes SHA-256 locally.

4. **Inspect verification result states**
   - Review visible state labels for this preview flow:
     - **LOCAL PREVIEW**
     - **HASH GENERATED**
     - **NOT REGISTERED**
     - **ADVISORY ONLY**
     - **REVIEW REQUIRED**

5. **Copy hash**
   - Use the copy action for the generated SHA-256 value.
   - Save it for later reviewer handoff or comparison.

6. **Inspect preview route**
   - Review the route-style preview shown by the prototype.
   - Treat it as a non-canonical preview reference, not a registration event.

7. **Understand advisory signal**
   - Treat the output as a verification signal for review routing.
   - Do not interpret the preview as a final trust decision.

8. **Understand no-upload/no-registration boundary**
   - Content remains local to the browser-side flow.
   - No backend upload, no account requirement, and no canonical record write occurs in this prototype step.

## Expected user-visible results

A successful run should visibly communicate all of the following:

- **LOCAL PREVIEW**
- **HASH GENERATED**
- **NOT REGISTERED**
- **ADVISORY ONLY**
- **REVIEW REQUIRED**

## What this proves / What this does not prove

### What this proves

- The user can generate a local SHA-256 digest from sample text in the HC:// self-service prototype.
- The user can view a preview route and copy the hash for later review workflows.
- The prototype can display advisory verification state messaging for human-supervised validation handoff.

### What this does not prove

- It does **not** prove objective truth.
- It does **not** prove authorship.
- It does **not** provide legal certification.
- It does **not** provide AI detection certainty.
- It does **not** register content into canonical records.
- It does **not** replace human-supervised validation.

## Related references

- `docs/public-self-service-verification-flow.md`
- `docs/self-service-smoke-test.md`
- `docs/verification-result-states.md`
- `docs/public-verification-boundaries.md`
- `docs/public/hc-public-trust-guide.md`
