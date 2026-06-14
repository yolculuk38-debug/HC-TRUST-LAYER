# Ruleset Smoke Test — 2026-06-14

This document records a small docs-only pull request used to validate the current `main` branch ruleset behavior.

## Purpose

Confirm that the repository ruleset and branch protection behavior remain aligned with HC-TRUST-LAYER governance expectations.

## Expected checks

The pull request is expected to exercise the current required checks without touching trust-critical implementation surfaces.

Required baseline under test:

- Validation
- governance-preflight
- Automation Gate
- Advisory PR scope boundary guard
- Docs Drift

## Expected repository behavior

- Pull request targets `main`.
- Merge method remains squash-only.
- Conversations must be resolved before merge.
- No autonomous approval, rejection, merge, close, label write, or reviewer request is introduced by this test.

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
