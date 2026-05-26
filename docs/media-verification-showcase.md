# Media Verification Showcase (Image Example)

This document provides the first realistic HC:// media verification showcase flow for HC-TRUST-LAYER using the existing advisory verification architecture.

## Scope and constraints

- Documentation-only guidance.
- Non-canonical artifacts only.
- No canonical schema changes.
- No validator or guard weakening.
- Advisory-only verification posture remains required.
- Human-supervised validation remains required.

## Showcase scenario

An image titled `city-council-briefing-photo.jpg` is submitted for verification with a public HC:// QR route on a media card.

### Verification references (example)

- **Canonical record ID:** `HC-MEDIA2026-IMG-0001`
- **Canonical record path:** `records/canonical-media-demo/HC-MEDIA2026-IMG-0001.json` (illustrative reference)
- **Original registration timestamp:** `2026-05-14T18:22:09Z`
- **Declared media hash (SHA-256):** `4f4a9d878bf3ef8dd8763ab6be6f3f0901c5e5f63076f0a2f882f266d8a36a11`
- **HC:// QR verification route:** `https://<owner>.github.io/HC-TRUST-LAYER/docs/verify.html?record=HC-MEDIA2026-IMG-0001&hash=4f4a9d878bf3ef8dd8763ab6be6f3f0901c5e5f63076f0a2f882f266d8a36a11`
- **Explorer continuity artifact (non-canonical):** `generated/media_showcase_explorer_index.json`
- **Audit continuity artifact (non-canonical):** `generated/media_showcase_audit_snapshot.json`

## End-to-end verification flow

1. **Original registration**
   - A submitter registers image metadata and fingerprint under canonical record `HC-MEDIA2026-IMG-0001` with timestamp `2026-05-14T18:22:09Z`.
   - Record linkage is retained for verification map and protocol graph navigation.

2. **QR verification route**
   - A viewer scans the HC:// QR route on the image card.
   - The static verification page loads `record` and `hash` query values for advisory comparison.

3. **Hash continuity check**
   - The verification view compares the presented image fingerprint to the hash in the canonical record context.
   - If bytes match: integrity state renders as match for declared scope.
   - If bytes differ or inputs are incomplete: integrity state renders as modified/unknown.

4. **Explorer continuity check**
   - The non-canonical explorer continuity artifact is inspected for matching `record_id` and `record_hash`.
   - Missing explorer linkage is shown as continuity partial, not as definitive failure.

5. **Audit continuity check**
   - The non-canonical audit snapshot is inspected for continuity of event references (registration, verification lookup, review handoff).
   - Continuity gaps are surfaced as advisory review signals.

6. **Verification signal rendering**
   - The page renders text-first status outputs for integrity, provenance continuity, advisory posture, and human review requirement.

## Example verification states (rendered)

For this showcase run, the view can render:

- **Original registration timestamp:** `2026-05-14T18:22:09Z`
- **Integrity verification state:** `HC VERIFIED` (hash match for declared scope)
- **Provenance continuity state:** `HC PROVENANCE` (continuity references present and inspectable)
- **Advisory verification state:** `HC PARTIAL` (one continuity source temporarily unavailable)
- **Human-review-required state:** `HC REVIEW` (human-supervised validation required before consequential use)

## Lightweight example UI sections (static-site compatible)

### 1) Verification badge

**HC VERIFIED · HC PROVENANCE · HC REVIEW**

- Text-first badge with plain language.
- Mobile-readable line wrapping.
- No backend dependency.

### 2) Continuity result

- **Canonical record continuity:** match
- **Hash continuity:** match
- **Explorer continuity:** partial (artifact fetch unavailable)
- **Audit continuity:** present

### 3) Generated artifact warning

> Generated explorer and audit artifacts are non-canonical verification aids. Canonical record boundaries remain authoritative.

### 4) Provenance summary

- First registered record: `HC-MEDIA2026-IMG-0001`
- Registration time: `2026-05-14T18:22:09Z`
- Hash status: match for declared image scope
- Audit trail references: available for reviewer inspection
- Consequential-use note: human-supervised validation required

## Limitations and boundary clarity

- Integrity match does not prove objective truth.
- First registration does not prove original authorship.
- AI-risk analysis remains advisory and probabilistic.
- Human-supervised validation remains required.

## Rendering and implementation notes

- Static-site compatible (no runtime backend required).
- Mobile-friendly, text-first layout prioritized.
- Advisories remain visible in both matched and partial states.
- This showcase does not change canonical schema, validators, policy evaluation, or trust-kernel behavior.

## Related references

- `docs/public-onboarding-model.md`
- `docs/content-verification-signal-model.md`
- `docs/FIRST_WORKING_RECORD.md`
- `docs/public-verification-boundaries.md`
- `docs/qr-verification-security-model.md`
