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
- The viewer links, QR/link fixture entries, quickstart scenario commands, runner scenario names, and Record ID fixture matches align around the same demo keys: `banana`, `building`, `news`, and `qr-spoof`.
- The static viewer includes a Record ID input for bundled fixture matching only: `HC-DEMO-PV-FIXTURE-FOOD-0001` → `banana`, `HC-DEMO-PV-FIXTURE-CONCRETE-0001` → `building`, `HC-DEMO-PV-FIXTURE-NEWS-0001` → `news`, and `HC-DEMO-PV-FIXTURE-QR-0001` → `qr-spoof`. Unsupported IDs show a public-safe warning without backend, network, API, database, canonical lookup, truth verification, QR authenticity, signed payload verification, or production verification behavior.
- The README and START_HERE navigation point users to the static viewer, local runner, and quickstart without presenting the demo as production-ready.
- The local record lookup boundary spec defines the next-phase separation between fixture matching and future local canonical record lookup: [`public-validator-local-record-lookup-boundary.md`](public-validator-local-record-lookup-boundary.md).

## Demo-Only Boundaries

This checkpoint keeps the Public Validator demo bounded to local, public-safe review material.

The demo does not:

- claim production readiness;
- certify food safety, building safety, code compliance, news truth, legal status, issuer authority, product authenticity, or regulatory compliance;
- make a fraud finding, forensic determination, legal determination, QR authenticity certification, or truth verification claim;
- replace human reviewer judgment or grant autonomous governance authority;
- validate real signatures, verify live hashes, fetch remote URLs, call a backend, perform external network checks, or look up canonical records from Record ID input;
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

- The static viewer is a local static HTML page with bundled demo data. It does not load fixture JSON files, call a backend, fetch evidence, look up canonical records, or perform live HC:// validation.
- The QR/link fixture URLs are local static demo entry points for bundled scenario selection. They do not prove QR authenticity, payload integrity, issuer authority, or canonical HC:// binding.
- The demo result identifiers are fixture identifiers for public demo output and may be used by the static viewer for fixture matching only; they are not production records, signed payloads, legal certifications, database keys, lookup handles, or canonical records.
- The scenario evidence is intentionally incomplete or conflicting in places so public reviewers can see `missing_evidence`, `conflicting_evidence`, warnings, and human-review boundaries.
- The current demo remains suitable for checkpoint review and onboarding only; it should not be described as a production Public Validator, real Verification API, security workflow, or truth-verification system.

## Checkpoint Note

PR **#652 Public Validator Record ID input demo** keeps the work static/demo-only and documents bounded Record ID fixture matching as a viewer convenience layered on top of the existing scenario selection. It does not add backend calls, API calls, external network calls, QR crypto, signing changes, schema changes, validator changes, workflow changes, database/index lookup, canonical lookup, or production-readiness claims. Manual checks for this checkpoint are: query scenario links still work, scenario buttons still work, supported demo `record_id` values select the mapped scenarios, unsupported demo `record_id` values show a safe warning, and no backend/network/API calls are introduced.
