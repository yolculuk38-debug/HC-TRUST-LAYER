# HC:// Public QR Verification Gateway Model

This document defines the first operational public QR verification gateway flow for HC:// in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only gateway model.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No canonical schema changes.
- No validator or guard weakening.
- Conditional federation routing is preserved.
- No truth-guarantee, legal-certification, or production-readiness claims.
- Static-site compatibility is preserved.

## Purpose

Define a mobile-readable, static-site-compatible QR entry flow that routes users to a public verification page with record identity, hash state, trust state, continuity state, advisory warning visibility, and public audit/history links.

## Gateway flow

1. **QR scanned**
   - User scans an HC:// verification QR from a public context.
2. **verification gateway opened**
   - Browser opens a static verification gateway route on an official HC:// domain.
3. **record identifier parsed**
   - Gateway parses record identifier parameters and prepares a public verification lookup context.
4. **hash parameter checked**
   - Gateway compares provided hash parameter state with available verification context and labels match/mismatch visibility.
5. **trust state displayed**
   - Gateway displays advisory trust state labels and related review-state context.
6. **continuity state displayed**
   - Gateway displays continuity state signals and continuity warning visibility when present.
7. **advisory warning displayed**
   - Gateway displays explicit advisory warning language and human-supervised validation reminders.
8. **audit/history links exposed**
   - Gateway exposes public audit/history links for traceability and challengeability.

## Supported public QR use cases

- **TV broadcast QR**
  - Broadcast overlays that route viewers to a public HC:// verification page.
- **store/campaign QR**
  - Retail and campaign surfaces that provide public verification entry links.
- **document QR**
  - Printed or digital document QR markers that point to public verification context.
- **public notice QR**
  - Noticeboard or municipal-style public notices that route to advisory verification state.
- **media verification QR**
  - News/media context QR links for public verification routing and continuity visibility.

## Warning and state labels

The public QR verification gateway should support clear user-visible state labels:

- `RECORD FOUND`
- `HASH MATCH`
- `HASH MISMATCH`
- `NOT REGISTERED`
- `CONTINUITY WARNING`
- `DISPUTED`
- `ADVISORY ONLY`

State interpretation boundaries:

- Labels are advisory visibility states, not autonomous final judgments.
- Warning states must remain attributable, challengeable, and linked to public traceability surfaces.
- Consequential interpretation must remain human-supervised.

## Public-safety clarifications

### QR is an entry point, not proof

An HC:// QR code is a routing entry point into verification context. A QR scan alone does not prove truth, authorship, or legal validity.

### Fake QR risks remain

Lookalike or manipulated QR placements can misroute users. Public messaging should explicitly preserve spoofing awareness and user caution.

### Users must verify official domain

The gateway should clearly instruct users to verify the official HC:// domain before relying on displayed advisory verification signals.

### Public gateway must expose traceability

Public verification pages should expose traceability paths, including record identity context, continuity visibility, and public audit/history links that support challenge and reviewer escalation.

## Static-site compatibility expectations

- Gateway model should remain compatible with static-site hosting and simple route/parameter parsing.
- Public verification rendering should prioritize mobile-readable UX.
- No backend dependency is required by this documentation model.

## Human-supervised validation reminder

The public QR verification gateway remains an advisory verification surface. Human-supervised validation is required for consequential decisions, dispute handling, and final trust interpretation.

## Implementation and boundary reminder

This model is documentation guidance only. It does not modify canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.

## Related references

- `docs/core/runtime-state-model.md`
- `docs/core/autonomous-validator-runtime-architecture.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/public-verification-walkthrough.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`
