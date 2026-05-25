# HC-TRUST-LAYER HC:// MVP-1 Demo Index

## MVP-1 Demo Overview

This index provides direct navigation for the HC:// MVP-1 static verification viewer so reviewers can quickly open demo packages from GitHub Pages.

- Static viewer page: [`docs/verification-viewer.html`](verification-viewer.html)
- Static viewer guide: [`docs/static-viewer.md`](static-viewer.md)
- CLI viewer documentation: [`docs/mvp-1-cli-viewer.md`](mvp-1-cli-viewer.md)

## MVP-1 Public Demo Quick Links

Use these shareable viewer hash links to open each bundled MVP-1 verification package state directly:

- [verified trace demo](verification-viewer.html#verified-trace)
- [partial trace demo](verification-viewer.html#partial-trace)
- [replay warning demo](verification-viewer.html#replay-warning)
- [disputed demo](verification-viewer.html#disputed)
- [unverified demo](verification-viewer.html#unverified)

## Available Demo Packages

The bundled MVP-1 demo package set includes:

- verified trace
- partial trace
- replay warning
- disputed
- unverified

These packages are loaded from `examples/verification-packages/` through the static viewer package selector.

Shareable hash links route only to bundled sample packages and are intended for quick demo handoff between reviewers.
Local uploaded packages are not stored in URL state and are not included in shared links.

The static viewer also supports shareable demo links via URL hash:

- `docs/verification-viewer.html#verified-trace`
- `docs/verification-viewer.html#partial-trace`
- `docs/verification-viewer.html#replay-warning`
- `docs/verification-viewer.html#disputed`
- `docs/verification-viewer.html#unverified`

Unknown hash values fail safely by loading a bundled default/selected example state.
Hash routing applies to bundled demo packages only.
Local uploaded JSON remains private, is not encoded into URL state, and is not written to local storage.

## Mobile-First Testing Note

The static viewer is optimized for mobile-readable demo review. Validate share links on phone-sized viewports before broader reviewer circulation.

## What Users Can Test

With the MVP-1 static viewer, users can test:

- trust result label rendering (`PASS`, `WARNING`, `FAIL`)
- provenance timeline continuity visibility
- replay warning and dispute indicator visibility
- validator review visibility and audit trail-linked context
- simple timeline-style grouping across provenance, validator reviews, replay indicators, dispute indicators, and audit snapshot context
- package-level interpretation boundaries before escalation

For terminal-based review of the same package set, use the CLI viewer documentation at `docs/mvp-1-cli-viewer.md`.

## Demo-Only Limitation

This demo index and the static viewer are documentation/demo surfaces only.
They do not introduce runtime verification behavior, schema contracts, validator logic, or workflow policy changes.

The MVP-1 demos do not provide production readiness guarantees, trust review guidance limitations, or forensic certainty claims.
The viewer layout improvements are interpretive UX polish only and do not change workflow policy, schema contracts, validator logic, or canonical record behavior.

## Human-Supervised Validation Note

MVP-1 viewer outputs are advisory verification signals.
Uncertain, disputed, replay-flagged, or high-impact outcomes require human-supervised validation before trust decisions.


## Report output quick test

From `docs/verification-viewer.html`, reviewers can additionally test:

- **Print report** for the currently loaded package.
- **Export report summary (.txt)** for the currently loaded package.

The export summary includes package identity, trust result, confidence, content hash, provenance summary, replay/dispute indicators, validator reviews, audit snapshot, human review required, and viewer warnings.

Demo-only/local-only note: these actions run in-browser with static HTML/JS only, use no backend services, and provide advisory outputs that still require human-supervised validation.

## Raw package fields quick test

From `docs/verification-viewer.html`, reviewers can test the MVP-1 raw field inspector:

- expand **Raw package fields** for any bundled demo package
- load a local `.json` package and expand **Raw package fields**
- verify pretty-printed JSON visibility on mobile-sized viewports
- use **Copy raw JSON** for local-only clipboard capture
- verify no-package safety messaging when no package is loaded

Local-only/demo-only reminder:

- raw package field inspection is static HTML/JS only
- no backend services or external dependencies are used
- package content is not uploaded and local uploaded package content is not stored
- viewer outputs remain advisory and require human-supervised validation
