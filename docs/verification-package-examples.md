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

Before rendering or using these fixtures in MVP-1 viewer flows, run:

```bash
python3 scripts/validate_verification_package_examples.py
```

Expected behavior is `PASS` output per file when JSON parsing succeeds and all required MVP-1 fields are present. Any `FAIL` output indicates fixture issues that should be resolved before demo review usage.

## PASS / WARNING / FAIL interpretation

Use the following interpretation pattern in MVP-1 review surfaces.

- **PASS**: verification checks and provenance continuity are sufficient for current review boundaries.
- **WARNING**: non-blocking issues exist (for example partial provenance continuity or replay indicators); human review should be prioritized.
- **FAIL**: blocking concerns prevent trust acceptance in the current decision path.

These labels are review states, not final certainty guarantees.

## Trust result interpretation

`trust_result` is a concise outcome signal for MVP-1 consumption.

- `VERIFIED TRACE`: aligns with validator and provenance evidence for current scope.
- `PARTIAL TRACE`: indicates caution, follow-up, or uncertainty conditions.
- `REPLAY WARNING`: indicates replay-related caution and review escalation need.
- `DISPUTED`: indicates active dispute context and unresolved review routing.
- `UNVERIFIED`: indicates unresolved trust concerns or missing continuity.

`trust_confidence` communicates confidence posture in human-readable form for the current package context.

## Hash and advisory warning validation

For MVP-1 static and CLI viewers, example rendering now includes advisory validation checks:

- `content_hash` should use lowercase SHA-256 hex formatting (`64` hex characters).
- `provenance_timeline`, `validator_reviews`, `replay_indicators`, and `dispute_indicators` should each be arrays.
- malformed or incomplete values should produce explicit `WARNING` output.

These warnings are advisory and do not change schema contracts, canonical records, or trust-kernel policy behavior.

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
- `docs/demo-index.md`
- `docs/mvp-1-cli-viewer.md`
- `docs/static-viewer.md`
- `docs/verification-viewer.html`


## Package copy and download controls

The static viewer in `docs/verification-viewer.html` includes two local-only package actions:

- **Copy current package JSON** copies the currently displayed package JSON to the local clipboard.
- **Download current package JSON** downloads the currently displayed package JSON as a local `.json` file using a safe filename derived from `package_id`.

These controls work for both bundled example packages and locally uploaded JSON packages. They do not modify package content, do not upload data to any server, and require no backend services.

If no package is currently loaded, the viewer fails safely by showing a status message instead of attempting copy/download. Status messages are cleared automatically after action feedback to keep controls mobile-readable.

This behavior is demo-only and local-only, and does not alter HC:// trust-kernel behavior or canonical record semantics. Human-supervised validation remains required for consequential trust decisions.
