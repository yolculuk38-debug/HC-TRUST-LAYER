# HC-TRUST-LAYER HC:// MVP-1 CLI Verification Package Viewer

## Purpose

This CLI viewer provides the first small working HC:// verification experience for MVP-1 by reading example verification package JSON files and rendering a concise, human-readable trust summary.

The viewer is interpretive and advisory. It preserves trust-kernel boundaries and does not modify canonical records.

## Usage Example

```bash
python3 scripts/view_verification_package.py examples/verification-packages/verified-trace-example.json
```

The command prints a fixed-order summary for MVP-1 fields:

- `package_id`
- `trust_result`
- `trust_confidence`
- `content_hash`
- `provenance_summary`
- `provenance_timeline`
- `validator_reviews`
- `replay_indicators`
- `dispute_indicators`
- `audit_snapshot`
- `human_review_required`

## Supported Example Files

The MVP-1 CLI viewer is currently scoped to the example fixtures in:

- `examples/verification-packages/verified-trace-example.json`
- `examples/verification-packages/partial-trace-example.json`
- `examples/verification-packages/replay-warning-example.json`
- `examples/verification-packages/disputed-example.json`
- `examples/verification-packages/unverified-example.json`

## Output Explanation

- `package_id`: example package identity.
- `trust_result`: top-level PASS/WARNING/FAIL trust signal.
- `trust_confidence`: confidence posture (`high`, `medium`, `low`).
- `content_hash`: content hash reference displayed for review context.
- `provenance_summary`: high-level provenance continuity summary.
- `provenance_timeline`: stage-by-stage provenance timeline entries.
- `validator_reviews`: validator and human reviewer decisions for the package.
- `replay_indicators`: replay warning status and detail indicators.
- `dispute_indicators`: dispute status summary and case identifiers when present.
- `audit_snapshot`: audit trail reference and current review boundary context.
- `human_review_required`: whether escalation to human review is required.

## Limitations

- This MVP-1 viewer reads local JSON files only.
- This viewer validates required MVP fields only and does not perform schema-level enforcement.
- This viewer is designed for example fixtures and does not imply support for all package variants.
- Output is advisory and should not be interpreted as an autonomous trust decision.

## Related Viewer Surfaces

- Static browser demo viewer: `docs/verification-viewer.html`
- Static viewer usage guide: `docs/static-viewer.md`

## Human-Supervised Validation Note

All non-trivial trust-kernel-impacting decisions require human-supervised validation. CLI viewer output is informational and must be reviewed within repository-defined verification and review workflows.
