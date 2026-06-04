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

An image titled `city-council-briefing-photo.jpg` is submitted for advisory review with a public HC:// QR navigation route on a media card.

### Verification references (example)

- **Canonical record ID:** `HC-MEDIA2026-IMG-0001`
- **Canonical record path:** `records/canonical-media-demo/HC-MEDIA2026-IMG-0001.json` (illustrative reference)
- **Original registration timestamp:** `2026-05-14T18:22:09Z`
- **Declared media hash (SHA-256):** `4f4a9d878bf3ef8dd8763ab6be6f3f0901c5e5f63076f0a2f882f266d8a36a11`
- **HC:// QR navigation route:** `https://<owner>.github.io/HC-TRUST-LAYER/verify/HC-MEDIA2026-IMG-0001?record=HC-MEDIA2026-IMG-0001&hash=4f4a9d878bf3ef8dd8763ab6be6f3f0901c5e5f63076f0a2f882f266d8a36a11&ref=media_showcase&sig=...` (advisory placeholder unless separately deployed and validated)
- **Explorer continuity artifact (non-canonical):** `generated/media_showcase_explorer_index.json`
- **Audit continuity artifact (non-canonical):** `generated/media_showcase_audit_snapshot.json`

## End-to-end verification flow

1. **Original registration**
   - A submitter registers image metadata and fingerprint under canonical record `HC-MEDIA2026-IMG-0001` with timestamp `2026-05-14T18:22:09Z`.
   - Record linkage is retained for verification map and protocol graph navigation.

2. **QR navigation route**
   - A viewer scans the HC:// QR route on the image card.
   - For media and other non-demo records, the `/verify/{record_id}` route is an advisory/navigation placeholder unless separately deployed and validated.
   - `docs/verify.html` is limited to the first-flow/demo static QR verification page and does not verify arbitrary records.

3. **Hash continuity check**
   - A separately validated review flow may compare the presented image fingerprint to the hash in the canonical record context.
   - If bytes match: integrity state may be documented as a match for the declared scope.
   - If bytes differ or inputs are incomplete: integrity state should remain modified/unknown.

4. **Explorer continuity check**
   - The non-canonical explorer continuity artifact is inspected for matching `record_id` and `record_hash`.
   - Missing explorer linkage is shown as continuity partial, not as definitive failure.

5. **Audit continuity check**
   - The non-canonical audit snapshot is inspected for continuity of event references (registration, verification lookup, review handoff).
   - Continuity gaps are surfaced as advisory review signals.

6. **Verification signal rendering**
   - Any page or report renders text-first status outputs for integrity, provenance continuity, advisory posture, and human review requirement only after the relevant route or review flow is separately deployed and validated.

## Example verification states (rendered)

For this illustrative showcase, a separately validated review view could render:

- **Original registration timestamp:** `2026-05-14T18:22:09Z`
- **Integrity verification state:** `HC VERIFIED` (illustrative hash match for declared scope; not active v0.1.0 evidence from `docs/verify.html`)
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

- Static-site compatible examples are possible, but v0.1.0 does not provide a hosted general public verifier for arbitrary records.
- Mobile-friendly, text-first layout prioritized.
- Advisories remain visible in both matched and partial states.
- This showcase does not change canonical schema, validators, policy evaluation, or trust-kernel behavior.
- Existing QR artifacts should not be treated as active v0.1.0 evidence unless decoded or regenerated after PR #592.
- Public QR verification remains advisory-only and human-supervised.
- Do not claim production readiness, security certification, truth finality, forensic certainty, or live public verifier guarantees.

## Related references

- `docs/public-onboarding-model.md`
- `docs/content-verification-signal-model.md`
- `docs/FIRST_WORKING_RECORD.md`
- `docs/public-verification-boundaries.md`
- `docs/qr-verification-security-model.md`
