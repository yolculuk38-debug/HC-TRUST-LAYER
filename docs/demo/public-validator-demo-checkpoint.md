# Public Validator Demo Checkpoint

> **Status:** checkpoint review for the completed #640-#649 demo flow
> **Scope:** public-safe HC:// Public Validator demo documentation, static viewer, local runner, and demo fixtures
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## What Currently Works

- The static viewer at [`public-validator-static-viewer.html`](public-validator-static-viewer.html) displays the four demo scenarios: `banana`, `building`, `news`, and `qr-spoof`.
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
- The QR/link fixture URLs document intended local demo entry points. They do not prove QR authenticity, payload integrity, issuer authority, or canonical HC:// binding.
- The demo result identifiers are fixture identifiers for public demo output; they are not production records, signed payloads, legal certifications, or canonical records.
- The scenario evidence is intentionally incomplete or conflicting in places so public reviewers can see `missing_evidence`, `conflicting_evidence`, warnings, and human-review boundaries.
- The current demo remains suitable for checkpoint review and onboarding only; it should not be described as a production Public Validator, real Verification API, security workflow, or truth-verification system.

## Recommended Next PR

Recommended next PR: **#651 Public Validator demo navigation polish**.

Suggested scope for #651: keep the work documentation/demo-only and consider a small navigation polish pass for public demo entry points, such as clarifying whether local query-string scenario selection should remain a documented fixture convention or become a bounded static-viewer convenience. Do not add backend calls, QR crypto, signing changes, schema changes, validator changes, workflow changes, or production-readiness claims.
