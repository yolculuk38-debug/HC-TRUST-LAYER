# Content Verification Signal and Media Provenance Model

This document defines an advisory-only HC:// content verification signal and media provenance model for HC-TRUST-LAYER.

## Scope and constraints

- Documentation-only guidance.
- Non-canonical artifacts only.
- No canonical schema changes.
- No validator or guard weakening.
- No blockchain, token, identity-authority, or truth-guarantee claims.
- No AI detection certainty claims.
- Human-supervised validation remains required.

## Supported content classes

HC:// verification signals can be rendered for these content classes:

- quote/text
- image
- video
- document
- social media post
- archived record

## Verification questions

Each content verification view should answer these questions explicitly:

1. Who first submitted or registered the content (as currently recorded in repository-visible provenance context)?
2. When was the content registered?
3. Does the current content hash match the registered hash?
4. Does the content appear modified relative to the registered reference?
5. Does provenance context exist and remain inspectable?
6. Is AI-generation risk present as an advisory/probabilistic indicator?
7. Is human-supervised review required before consequential use?

## Visible signal states

Use these text-first HC:// states for consistent mobile-readable rendering:

- **HC VERIFIED** — hash and required continuity checks match for the declared scope.
- **HC PROVENANCE** — provenance links are present and inspectable for the declared scope.
- **HC MODIFIED** — visible content differs from the registered hash/reference scope.
- **HC AI-RISK** — probabilistic advisory signal indicates possible AI-generation or manipulation risk.
- **HC PARTIAL** — some expected checks or continuity links are missing/incomplete.
- **HC REVIEW** — human-supervised validation is required before consequential interpretation.
- **HC UNKNOWN** — verification inputs are missing, unavailable, or not yet evaluable.

## Badge, color, and QR behavior

### QR behavior

- QR scan opens the HC:// verification page for the specific record/hash context.
- QR is a routing mechanism, not trust proof or truth proof.
- Verification page must keep canonical record link and evidence links visible.

### Badge behavior

- Badge summarizes current advisory verification state using the visible signal states.
- Badge must remain text-forward (not icon-only) and include human-review-required language when relevant.
- Badge must include or link to inspectable evidence: record ID, hash status, provenance references, and audit trail context.

### Color behavior

- Color may support scannability but must not imply objective certainty, institutional authority, or autonomous certainty.
- Do not rely on color alone; pair every color state with explicit text.
- Warning/partial/unknown states must remain high-visibility and accessible.

## Public inspection requirements

Users must be able to inspect:

- canonical record reference
- hash and comparison inputs
- provenance references
- audit trail evidence
- advisory boundary language

## Social media integration concept

For social distribution and public verification visibility:

1. A social media post can render an HC:// badge beside post text.
2. Shared image/video/document cards can render an HC:// badge beside media preview.
3. Each badge routes to a public HC:// verification link.
4. Verification view exposes a source/canonical record link for direct inspection.
5. Advisory warning text remains visible: process evidence only, human-supervised validation required for consequential decisions.

## Limitations and boundary statements

- Hash match does not prove truth.
- AI-generation detection is probabilistic and advisory.
- First registration does not prove original authorship.
- Human-supervised validation remains required.

## Non-canonical artifact guidance

Any generated signal packages, previews, exports, or social-card outputs are non-canonical artifacts.

Canonical record boundaries and repository-defined validation controls remain authoritative.

## Related references

- `docs/verification-signal-model.md`
- `docs/public-verification-boundaries.md`
- `docs/anti-spoof-verification-signals.md`
- `docs/qr-verification-security-model.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/public-onboarding-model.md`
- `docs/media-verification-showcase.md`
- `docs/public-self-service-verification-flow.md`
