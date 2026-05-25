# HC-TRUST-LAYER HC:// MVP-1 Static Verification Package Viewer

## Purpose

The MVP-1 static verification package viewer provides a browser-based, demo-only reading surface for HC:// verification package examples.

The viewer helps users inspect trust results, provenance timeline continuity, replay indicators, dispute indicators, validator reviews, and audit snapshot context without command-line usage.

## Open the viewer from GitHub Pages

After GitHub Pages publishes repository docs, open:

- `https://<org-or-user>.github.io/<repo>/docs/verification-viewer.html`

This page loads bundled examples from `examples/verification-packages/` and renders the selected package in a mobile-readable static layout.

Before static rendering demos, run the fixture validation helper:

```bash
python3 scripts/validate_verification_package_examples.py
```

Expected behavior is `PASS` output per file for all bundled examples. This step checks required MVP-1 example fields only.

## Demo-only limitations

- The viewer is static HTML/JS with no backend and no external dependencies.
- The viewer only targets bundled example fixtures in `examples/verification-packages/`.
- Validation helper coverage is demo-only and does not introduce schema, validator, or workflow changes.
- The viewer does not provide production readiness guarantees.
- The viewer does not provide truth guarantees.
- The viewer does not provide forensic certainty claims.
- The viewer is advisory and does not replace human-supervised validation.

## Relation to CLI viewer

The static viewer and CLI viewer cover the same MVP-1 field set and both remain interpretation surfaces for documentation and demo usage.

For terminal-based review, use `scripts/view_verification_package.py` as documented in `docs/mvp-1-cli-viewer.md`.

## Future improvements

- Add package upload support while preserving static-only boundaries.
- Add richer timeline filtering and section collapse controls.
- Add deeper accessibility tuning and keyboard navigation polish.
- Add linked explanations for verification map and protocol graph context.
- Add explicit UI notices when fields are missing or unknown.
