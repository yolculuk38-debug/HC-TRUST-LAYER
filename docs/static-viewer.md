# HC-TRUST-LAYER HC:// MVP-1 Static Verification Package Viewer

## Purpose

The MVP-1 static verification package viewer provides a browser-based, demo-only reading surface for HC:// verification package examples.

The viewer helps users inspect trust results, provenance timeline continuity, replay indicators, dispute indicators, validator reviews, and audit snapshot context without command-line usage.
The trust result card prioritizes mobile-readable labels and plain-language explanations to support non-technical interpretation boundaries.
The provenance, validator review, replay, and dispute sections use a simple timeline-style visual grouping with plain-text section labels (`[Timeline]`, `[Reviews]`, `[Replay]`, `[Dispute]`, `[Audit]`) so review flow is easier to scan on mobile-sized viewports.

## Open the viewer from GitHub Pages

After GitHub Pages publishes repository docs, open:

- `https://<org-or-user>.github.io/<repo>/docs/verification-viewer.html`
- `https://<org-or-user>.github.io/<repo>/docs/demo-index.md`

This page loads bundled examples from `examples/verification-packages/` and can also load local `.json` verification package files directly in-browser using a file input control.
All package processing is client-side local processing only with no server upload path.
The viewer validates required fields before rendering and shows explicit `WARNING` notices when local package data is incomplete, malformed, or advisory-only.
The layout remains mobile-readable and static-only.
UI labels include `Verified trace`, `Partial trace`, `Replay warning`, `Disputed`, `Unverified`, and `Human review required` for consistent MVP-1 trust interpretation.

Use the demo index as the quickest entry point for MVP-1 demo navigation:

- `docs/demo-index.md`
- `docs/verification-viewer.html`
- `docs/mvp-1-cli-viewer.md`

Before static rendering demos, run the fixture validation helper:

```bash
python3 scripts/validate_verification_package_examples.py
```

Expected behavior is `PASS` output per file for all bundled examples. This step checks required MVP-1 example fields only.

The viewer also performs content and shape checks used for advisory display boundaries:

- `content_hash` must match lowercase SHA-256 hex format (`64` hex characters).
- `trust_result` must be one of: `VERIFIED TRACE`, `PARTIAL TRACE`, `REPLAY WARNING`, `DISPUTED`, `UNVERIFIED`.
- `advisory trust summary` must be present and human-readable as trust interpretation review guidance.
- `provenance_timeline`, `validator_reviews`, `replay_indicators`, and `dispute_indicators` must each be arrays.

Terminology note: static viewer documentation should use **advisory trust summary** wording and avoid deprecated truth-guarantee phrasing.

When a package fails these checks, the viewer keeps rendering valid sections where possible and emits advisory `WARNING` messages instead of silently accepting malformed data.

## Demo permalink state (URL hash)

The static viewer supports demo permalink state using URL hash values for bundled examples only:

- `docs/verification-viewer.html#verified-trace`
- `docs/verification-viewer.html#partial-trace`
- `docs/verification-viewer.html#replay-warning`
- `docs/verification-viewer.html#disputed`
- `docs/verification-viewer.html#unverified`

These hash links are shareable for reviewer demo navigation and always resolve to bundled sample packages only.
Local uploaded packages are never serialized into URL state and are not shareable through these links.

When a bundled example is selected in the viewer, the URL hash is updated so reviewers can share the same demo state.
On page load, the viewer reads the hash and loads the matching bundled example when recognized.
If the hash value is unknown, the viewer falls back safely to the current/default bundled selection and shows advisory status.

Local upload privacy boundary:

- local uploaded JSON is never encoded in the URL hash
- local uploaded JSON is never stored in local storage
- reset returns to bundled demo state safely without sharing local upload contents

## Mobile-first demo testing note

Before sharing MVP-1 links broadly, test bundled demo hash links on mobile-sized viewports to confirm readable trust labels, warning text, and audit trail context.
The timeline cards use larger spacing and stacked metadata to keep provenance and validator review details readable without horizontal scrolling.

## Demo-only limitations

- The viewer is static HTML/JS with no backend and no external dependencies.
- The viewer supports bundled fixtures and local `.json` package uploads, but both remain static interpretation surfaces.
- Validation helper coverage is demo-only and does not introduce schema, validator, or workflow changes.
- The viewer does not provide production readiness guarantees.
- The viewer does not provide verification advisory band guidance.
- The viewer does not provide forensic certainty claims.
- The viewer is advisory and does not replace human-supervised validation.
- The viewer includes explanation text for what the result means, why review may be needed, what users should not assume, and demo-only limitations.
- The viewer includes warnings for demo-only behavior, local-only processing, no server upload, no verification state guidance, and human review recommendation.

## Relation to CLI viewer

The static viewer and CLI viewer cover the same MVP-1 field set and both remain interpretation surfaces for documentation and demo usage.

For terminal-based review, use `scripts/view_verification_package.py` as documented in `docs/mvp-1-cli-viewer.md`.

## Future improvements

- Add richer timeline filtering and section collapse controls.
- Add deeper accessibility tuning and keyboard navigation polish.
- Add linked explanations for verification map and protocol graph context.
- Expand explicit UI notices for additional malformed nested structures beyond MVP-1 required field checks.


## Package copy and download controls

The static viewer in `docs/verification-viewer.html` includes two local-only package actions:

- **Copy current package JSON** copies the currently displayed package JSON to the local clipboard.
- **Download current package JSON** downloads the currently displayed package JSON as a local `.json` file using a safe filename derived from `package_id`.

These controls work for both bundled example packages and locally uploaded JSON packages. They do not modify package content, do not upload data to any server, and require no backend services.

If no package is currently loaded, the viewer fails safely by showing a status message instead of attempting copy/download. Status messages are cleared automatically after action feedback to keep controls mobile-readable.

This behavior is demo-only and local-only, and does not alter HC:// trust-kernel behavior or canonical record semantics. Human-supervised validation remains required for consequential trust decisions.


## Print report and export summary

The static viewer includes two report actions for the currently loaded HC:// verification package:

- **Print report** opens the browser print dialog for a human-readable report view of the currently loaded package.
- **Export report summary (.txt)** downloads a local text summary report.

The report summary includes: `package_id`, `trust_result`, `advisory trust summary`, `content_hash`, provenance summary, replay indicators, dispute indicators, validator reviews, audit snapshot, human review required, and viewer warnings.

Both actions fail safely when no package is loaded by showing a viewer status message instead of producing output.

Demo-only limitation and local-only processing note:

- this is a static HTML/JS viewer with no backend and no external dependencies
- report generation and export run in-browser only with no server upload path
- outputs remain advisory and require human-supervised validation for consequential trust decisions

## Raw package fields inspector

The static viewer includes a collapsible **Raw package fields** section that displays pretty-printed package JSON for the currently loaded package.

How to inspect raw fields:

1. Open a bundled example or load a local `.json` package.
2. Expand **Raw package fields**.
3. Use **Copy raw JSON** to copy the currently loaded JSON for local review.

When raw fields are useful:

- validating exact field names and nested structure shown by the viewer
- reviewing values that are summarized in higher-level cards
- preparing reviewer notes about provenance, replay indicators, dispute indicators, and audit trail context

Safety boundaries and limitations:

- local-only processing: raw JSON rendering and copy actions run in-browser only
- no upload path: the viewer does not upload package content to any server
- no storage path: local uploaded package content is not written to local storage
- no mutation path: the viewer does not modify package content
- fail-safe no-package behavior: when no package is loaded, the section shows a clear safe message instead of rendering content
- demo-only limitation: this is still a static MVP-1 demo interpretation surface
- human-supervised validation remains required for consequential trust decisions
