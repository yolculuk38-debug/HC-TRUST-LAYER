# HC-TRUST-LAYER HC:// MVP-1 User Flow (Verification Package Viewer)

## Status

- documentation-only user flow
- no frontend implementation in this phase
- no runtime package parsing in this phase

## Flow Overview

MVP-1 user flow focuses on a small and readable verification package inspection path.

### 1) Open Package

- user opens a verification package file or reference
- system shows package identity, version, and canonical record linkage summary
- system shows package scope note (what is covered vs what is not covered)

### 2) Inspect Verification

- user inspects hash and verification status summary
- user sees clear `PASS`, `WARNING`, `FAIL`, or `UNKNOWN` state labels
- user can inspect basic supporting evidence pointers

### 3) Inspect Provenance

- user reviews provenance continuity summary
- user sees origin/revision/supersession relationships when available
- user sees continuity gap or unknown lineage markers

### 4) Inspect Replay Warnings

- user sees replay warning indicator when suspicious reuse patterns exist
- user sees plain-language caution note about unresolved replay risk
- user is guided to human-supervised validation for uncertain outcomes

### 5) Inspect Validator Review

- user sees validator identity references
- user sees validator review timestamp context
- user sees validator outcome category and rationale pointer availability

### 6) Inspect Snapshot History

- user sees trust snapshot timestamp and scope
- user sees package-to-snapshot linkage context
- user sees drift note if newer provenance/audit trail entries exist

## Human-Readable Trust Result Concepts

MVP-1 trust result concepts should remain simple and non-absolute:

- `PASS`: available verification checks support continuity for displayed scope
- `WARNING`: potential issues, ambiguity, replay risk, or incomplete continuity signals
- `FAIL`: verification mismatch or explicit inconsistency in displayed scope
- `UNKNOWN`: not enough evidence in displayed scope for a stronger result

All states are advisory and require human-supervised validation for high-impact decisions.


## Related References
- `docs/mvp-1-viewer-implementation-plan.md`

- `docs/trust-result-standard.md`
- `docs/verification-status-ux.md`
- `docs/provenance-timeline-format.md`
- `docs/replay-warning-standard.md`
