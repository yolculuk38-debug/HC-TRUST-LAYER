# HC:// Verification Package Examples (MVP-1)

## Purpose of these examples

This document introduces canonical example verification packages for MVP-1 review, documentation, and UI alignment.

These examples are **demo data only**. They do not represent production readiness, forensic certainty, or live federation guarantees.

The examples are intended to make HC:// verification output human-readable for both desktop and mobile surfaces while preserving trust-kernel boundary semantics.

## How MVP-1 uses these examples

MVP-1 can use these files as reference fixtures for:

- verification map walkthroughs
- provenance continuity UI previews
- validator review state rendering
- replay warning and dispute status messaging
- trust result presentation and human-supervised validation routing

Files are located in `examples/verification-packages/`.

## PASS / WARNING / FAIL interpretation

Use the following interpretation pattern in MVP-1 review surfaces.

- **PASS**: verification checks and provenance continuity are sufficient for current review boundaries.
- **WARNING**: non-blocking issues exist (for example partial provenance continuity or replay indicators); human review should be prioritized.
- **FAIL**: blocking concerns prevent trust acceptance in the current decision path.

These labels are review states, not final certainty guarantees.

## Trust result interpretation

`trust_result` is a concise outcome signal for MVP-1 consumption.

- `PASS`: aligns with validator and provenance evidence for current scope.
- `WARNING`: indicates caution, follow-up, or uncertainty conditions.
- `FAIL`: indicates unresolved trust concerns, missing continuity, or active dispute impact.

`trust_confidence` communicates confidence posture (`high`, `medium`, `low`) for the current package context.

## Provenance continuity examples

- `verified-trace-example.json` shows intact provenance continuity across capture, canonical linkage, and validator confirmation.
- `partial-trace-example.json` shows a partial continuity path with a missing handoff stage that requires follow-up.
- `unverified-example.json` shows continuity failure where canonical linkage evidence is not found.

## Replay warning examples

- `replay-warning-example.json` demonstrates repeated submission indicators that produce a warning state.
- Replay warnings indicate elevated review attention, not automatic malicious attribution.

## Dispute examples

- `disputed-example.json` demonstrates divergent validator outcomes and an active dispute marker.
- Active disputes should preserve audit trail continuity and route to human-supervised validation before closure.

## Mobile readability considerations

To support mobile readability in MVP-1:

- keep top-level fields concise and consistently ordered
- avoid deeply nested structures when summary fields are sufficient
- pair machine-readable indicators with human-readable summaries
- preserve stable keys across PASS/WARNING/FAIL example variants

## Related References

- `docs/mvp-1-viewer-implementation-plan.md`
- `docs/mvp-1-cli-viewer.md`
