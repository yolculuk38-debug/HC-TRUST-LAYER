# HC-TRUST-LAYER HC:// MVP-1 Verification Package Viewer Implementation Plan

## Status

- documentation-only implementation plan
- no viewer implementation in this phase
- no backend required for MVP-1
- no production-readiness claims
- no automatic trust decisions

## Viewer Goal

Deliver the first small working HC:// viewer that can read example verification packages and display trust result, provenance timeline context, replay warnings, dispute status, validator reviews, and an audit snapshot in a simple human-readable format.

This MVP-1 viewer scope is interpretive and advisory. It must preserve canonical terminology and route uncertain or high-impact outcomes to human-supervised validation.

## Input Source

Primary input source for MVP-1:

- `examples/verification-packages/*.json`

The viewer should treat these files as example fixtures and should not imply that all package variants or external package formats are supported.

## MVP Output Sections

The MVP-1 viewer output should include the following sections in a stable, human-readable order:

1. trust result card
2. content hash
3. provenance summary
4. provenance timeline
5. validator reviews
6. replay indicators
7. dispute indicators
8. audit snapshot
9. human review status

## First Implementation Options

### Option 1: CLI viewer

A simple command-line viewer can render package sections as readable text blocks for quick local review.

- strengths: fast setup, low complexity, straightforward diffable output
- tradeoffs: less visual hierarchy for non-technical users, manual file handling

### Option 2: static HTML viewer

A static HTML viewer can render the same package sections in a mobile-readable layout with simple visual status indicators.

- strengths: accessible presentation, low deployment overhead, easy demo sharing
- tradeoffs: basic interactivity only, static asset constraints

### Option 3: GitHub Pages demo viewer

A GitHub Pages-hosted demo can publish a static viewer artifact for public review of MVP-1 behavior boundaries.

- strengths: easy sharing, reproducible documentation-aligned demos
- tradeoffs: public hosting constraints, must preserve non-production framing

## Recommended MVP Path

Recommended starting approach:

- start with a static HTML viewer or a simple CLI viewer
- keep the implementation local/static with no backend required
- preserve documentation-only boundaries and avoid production claims

## Planned File Surfaces

Potential MVP-1 implementation file surfaces:

- `scripts/view_verification_package.py`
- `docs/demo-viewer.html` or `docs/viewer.md`
- `examples/verification-packages/`

This plan documents intended surfaces only and does not implement them in this phase.

## UX Principles

The MVP-1 viewer should follow these UX principles:

- mobile-readable layout and typography
- simple `PASS` / `WARNING` / `FAIL` style for top-level trust interpretation
- clear limitations and advisory boundary language
- no forensic certainty framing
- no truth guarantee framing

## Validation Plan

The first implementation should include validation behavior that is transparent and non-destructive:

- validate JSON input before rendering
- check required fields for each MVP output section
- fail gracefully when fields are missing or incomplete
- never modify canonical records

## Constraints and Non-Goals

- documentation-first and implementation-scoped planning only
- no schema modifications
- no validator logic changes
- no workflow or governance control changes
- no trust-kernel behavior changes in this plan

## Related References

- `docs/mvp-1-verification-package-viewer.md`
- `docs/verification-package-examples.md`
- `docs/trust-result-standard.md`
- `docs/mvp-1-user-flow.md`
- `docs/implementation-transition-plan.md`
- `docs/mvp-1-cli-viewer.md`
