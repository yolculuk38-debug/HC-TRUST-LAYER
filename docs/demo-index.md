# HC-TRUST-LAYER HC:// MVP-1 Demo Index

## MVP-1 Demo Overview

This index provides direct navigation for the HC:// MVP-1 static verification viewer so reviewers can quickly open demo packages from GitHub Pages.

- Static viewer page: [`docs/verification-viewer.html`](verification-viewer.html)
- Static viewer guide: [`docs/static-viewer.md`](static-viewer.md)
- CLI viewer documentation: [`docs/mvp-1-cli-viewer.md`](mvp-1-cli-viewer.md)

## Available Demo Packages

The bundled MVP-1 demo package set includes:

- verified trace
- partial trace
- replay warning
- disputed
- unverified

These packages are loaded from `examples/verification-packages/` through the static viewer package selector.

## What Users Can Test

With the MVP-1 static viewer, users can test:

- trust result label rendering (`PASS`, `WARNING`, `FAIL`)
- provenance timeline continuity visibility
- replay warning and dispute indicator visibility
- validator review visibility and audit trail-linked context
- package-level interpretation boundaries before escalation

For terminal-based review of the same package set, use the CLI viewer documentation at `docs/mvp-1-cli-viewer.md`.

## Demo-Only Limitation

This demo index and the static viewer are documentation/demo surfaces only.
They do not introduce runtime verification behavior, schema contracts, validator logic, or workflow policy changes.

The MVP-1 demos do not provide production readiness guarantees, truth guarantees, or forensic certainty claims.

## Human-Supervised Validation Note

MVP-1 viewer outputs are advisory verification signals.
Uncertain, disputed, replay-flagged, or high-impact outcomes require human-supervised validation before trust decisions.
