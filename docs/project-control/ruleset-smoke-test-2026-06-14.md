# Ruleset Smoke Test — 2026-06-14

This document records a small docs-only pull request used to validate the current `main` branch ruleset behavior.

## Purpose

Confirm that the repository ruleset and branch protection behavior remain aligned with HC-TRUST-LAYER governance expectations for a low-risk docs-only pull request.

## Expected checks

The pull request is expected to exercise the current required checks that apply to this docs-only scope without touching trust-critical implementation surfaces.

Required baseline under test:

- governance-preflight
- gate
- Advisory PR scope boundary guard
- docs-drift
- validate-verification-package-example

Note: the path-filtered `HC-TRUST-LAYER Validation` workflow is not expected to run for this docs-only change unless its configured paths are touched. This smoke test uses the required check context selected in the repository ruleset rather than treating every validation workflow as applicable to every docs-only PR.

## Expected repository behavior

- Pull request targets `main`.
- Merge method remains squash-only.
- Conversations must be resolved before merge.
- Existing automation may add or remove non-merge risk labels according to repository policy.
- No autonomous approval, rejection, merge, close, reviewer request, or auto-merge enablement is introduced by this test.

## Scope boundary

This is a docs-only project-control note. It does not modify:

- runtime code
- schemas
- validators
- records
- signatures
- QR logic
- workflows
- governance policy

## HC boundary

AI assists.
CI checks.
Governance constrains.
Audit records.
Human final authority remains.
