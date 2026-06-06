# Public Validator Demo Checkpoint

> **Status:** checkpoint review for the completed #640-#651 demo flow
> **Scope:** public-safe HC:// Public Validator demo documentation, static viewer, local runner, and demo fixtures
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## What Currently Works

- The static viewer at [`public-validator-static-viewer.html`](public-validator-static-viewer.html) displays the four demo scenarios: `banana`, `building`, `news`, and `qr-spoof`. It also supports static query-string scenario selection for demo links such as `public-validator-static-viewer.html?scenario=banana`, with unsupported or missing values falling back to `banana`.
- The local runner at [`../../scripts/run_public_validator_demo.py`](../../scripts/run_public_validator_demo.py) accepts the same four scenario commands and prints deterministic JSON from [`fixtures/results/`](fixtures/results/).
- The result fixtures expose consistent safety markers across scenarios:
  - `advisory_only: true`
  - `public_safe: true`
  - `truth_guarantee: false`
  - `human_review_required: true`
- The viewer links, QR/link fixture entries, quickstart scenario commands, and runner scenario names align around the same demo keys: `banana`, `building`, `news`, and `qr-spoof`.
- The README and START_HERE navigation point users to the static viewer, local runner, and quickstart without presenting the demo as production-ready.

## Demo-Only Boundaries

This checkpoint keeps the Public Validator demo bounded to local, public-safe review material.

The demo does not:

- claim production readiness;
- certify food safety, building safety, code compliance, news truth, legal status, issuer authority, product authenticity, or regulatory compliance;
- make a fraud finding, forensic determination, legal determination, QR authenticity certification, or truth verification claim;
- replace human reviewer judgment or grant autonomous governance authority;
- validate real signatures, verify live hashes, fetch remote URLs, call a backend, or perform external network checks;
- generate real QR artifacts, provide QR crypto, or prove scanned-link authenticity;
- define canonical records, mutate canonical record boundaries, or describe fixture files as canonical records.

The fixture files remain demo-only exports for reviewer discussion. They are not schemas, validators, records, generated artifacts, signed payloads, production validator output, certifications, legal authority, or canonical HC:// records.

## Checked Files

This checkpoint reviewed the public validator demo surface across:

- [`public-validator-demo-quickstart.md`](public-validator-demo-quickstart.md)
- [`public-validator-static-viewer.html`](public-validator-static-viewer.html)
- [`public-validator-demo-qr-entry.md`](public-validator-demo-qr-entry.md)
- [`fixtures/results/`](fixtures/results/)
- [`fixtures/demo-qr-links.json`](fixtures/demo-qr-links.json)
- [`../../README.md`](../../README.md)
- [`../START_HERE.md`](../START_HERE.md)
- [`../../scripts/run_public_validator_demo.py`](../../scripts/run_public_validator_demo.py)
- [`../../tests/test_public_validator_demo_runner.py`](../../tests/test_public_validator_demo_runner.py)

## Known Limitations

- The static viewer is a local static HTML page with bundled demo data. It does not load fixture JSON files, call a backend, fetch evidence, or perform live HC:// validation.
- The QR/link fixture URLs are local static demo entry points for bundled scenario selection. They do not prove QR authenticity, payload integrity, issuer authority, or canonical HC:// binding.
- The demo result identifiers are fixture identifiers for public demo output; they are not production records, signed payloads, legal certifications, or canonical records.
- The scenario evidence is intentionally incomplete or conflicting in places so public reviewers can see `missing_evidence`, `conflicting_evidence`, warnings, and human-review boundaries.
- The current demo remains suitable for checkpoint review and onboarding only; it should not be described as a production Public Validator, real Verification API, security workflow, or truth-verification system.

## Checkpoint Note

PR **#651 Public Validator demo navigation polish** keeps the work static/demo-only and documents bounded query-string scenario selection as a viewer convenience. It does not add backend calls, QR crypto, signing changes, schema changes, validator changes, workflow changes, canonical lookup, or production-readiness claims.
