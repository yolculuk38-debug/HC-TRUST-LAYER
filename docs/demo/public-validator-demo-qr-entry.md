# Public Validator Demo QR Entry Point

> **Status:** demo documentation and optional link fixture only
> **Scope:** public-safe QR/link entry flow for HC:// Public Validator demos
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Overview

This document defines the first demo-level QR/link entry flow for the HC:// Public Validator static viewer.

The entry flow is intentionally small and public-safe. A demo QR or ordinary link points a user toward the static viewer, the viewer displays one of the existing demo scenarios, and the result highlights warnings, missing evidence, source-chain context, and the need for human review.

No real QR artifacts are generated here. The links are fixture-level examples only and do not assert signed QR verification, production QR security, legal authority, certification authority, truth finality, or forensic certainty.

## Purpose

The purpose of this entry point is to show how a future public-facing HC:// validation experience could begin from a QR scan or link click without expanding the protocol, changing validator logic, or claiming production readiness.

This PR keeps the work documentation/demo-fixture only so reviewers can evaluate the user flow before any runtime, security, signing, federation, governance, or record-boundary changes are considered.

## Demo QR / Link Flow

The demo flow is:

```text
demo QR or link
→ static viewer
→ scenario result
→ warnings / missing evidence / source chain
→ human review reminder
```

In this demo posture, the QR or link is only an entry point. It does not prove that the QR label is authentic, that a scanned URL is canonical, that a payload is signed, or that a real-world claim is true. The Record ID input follows the same boundary: fixture matching only, not canonical lookup or security verification.

The static viewer remains the visible public demo surface. The scenario result remains advisory-only and public-safe, with `truth_guarantee: false` and `human_review_required: true`.

The viewer also includes a Record ID fixture input for demo convenience. It maps only the bundled demo IDs to bundled scenarios and must not be treated as canonical record lookup, database lookup, production verification, truth verification, QR authenticity proof, or signed payload verification.

## Demo Link Fixtures

The optional JSON fixture is available at [`fixtures/demo-qr-links.json`](fixtures/demo-qr-links.json).

Each fixture entry includes:

- `scenario`
- `record_id`
- `demo_url`
- `canonical_demo_path`
- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`
- `warnings`

The fixture is not a generated artifact, canonical record, schema, validator input, signed payload, production QR manifest, or security control. It is a public-safe list of demo entry links for reviewer discussion.

## Scenario Entry Points

| Demo key | Scenario | Record ID | Demo URL | Canonical demo path |
| --- | --- | --- | --- | --- |
| `banana` | `imported_banana_food_provenance` | `HC-DEMO-PV-FIXTURE-FOOD-0001` | `public-validator-static-viewer.html?scenario=banana` | `docs/demo/public-validator-static-viewer.html` |
| `building` | `building_concrete_provenance` | `HC-DEMO-PV-FIXTURE-CONCRETE-0001` | `public-validator-static-viewer.html?scenario=building` | `docs/demo/public-validator-static-viewer.html` |
| `news` | `news_source_provenance` | `HC-DEMO-PV-FIXTURE-NEWS-0001` | `public-validator-static-viewer.html?scenario=news` | `docs/demo/public-validator-static-viewer.html` |
| `qr-spoof` | `qr_spoof_non_canonical_link` | `HC-DEMO-PV-FIXTURE-QR-0001` | `public-validator-static-viewer.html?scenario=qr-spoof` | `docs/demo/public-validator-static-viewer.html` |

The `demo_url` values are static viewer entry points. When opened in a browser, the `scenario` query-string value selects the matching bundled demo scenario automatically. Unsupported or missing scenario values fall back to the `banana` demo scenario. The current static viewer remains a local static demo surface and does not provide production routing, backend lookup, remote fetching, QR authenticity checks, or signed QR validation.

## How to Use

1. Open [`public-validator-static-viewer.html`](public-validator-static-viewer.html) locally in a browser, or open a demo entry URL such as `public-validator-static-viewer.html?scenario=banana`.
2. Use one of the demo links from the fixture or the scenario table as the intended QR/link entry target.
3. Confirm the selected scenario in the static viewer; the page also keeps manual scenario buttons for reviewer comparison.
4. Review the displayed `record_id`, `scenario`, evidence list, missing evidence, conflicts, source chain, responsibility chain, and warnings.
5. Treat the result as advisory-only and require human review before relying on any displayed claim.

## What This Does

This demo entry point:

- documents a QR/link-style entry flow for the HC:// Public Validator demo;
- points users toward the existing static viewer and demo scenario results;
- keeps all scenario outputs public-safe and advisory-only;
- preserves `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true` posture;
- surfaces warnings, missing evidence, source-chain context, and review reminders;
- stays limited to documentation and a small demo fixture.

## What This Does NOT Do

This demo entry point does not:

- generate real QR artifacts;
- modify QR production code;
- modify records, schemas, validators, runtime endpoints, workflows, governance rules, signing, federation, policy, canonical artifacts, or generated artifacts;
- verify signed QR payloads;
- claim production QR security;
- fetch remote URLs or perform backend validation;
- certify food safety, building safety, news truth, legal status, regulatory compliance, issuer authority, or product authenticity;
- provide legal, certification, forensic, or autonomous governance authority;
- guarantee truth.

## QR Safety Notes

Demo QR/link entry points should be treated as untrusted until reviewed. A visible link can help a user reach a demo viewer, but it does not establish authenticity, issuer authority, payload integrity, or canonical HC:// binding.

The `qr-spoof` scenario exists to keep that limitation visible. It demonstrates that a scanned URL may differ from an expected HC:// canonical reference and that the mismatch should trigger warnings and human review rather than automatic trust.

Future QR work should keep scanned targets, expected HC:// references, payload signatures, issuer metadata, and verification results clearly separated so reviewers can inspect each boundary without confusing demo convenience with production security.

## Human Review Reminder

HC-TRUST-LAYER supports evidence-preserving, human-supervised validation. Demo QR/link entry points are advisory-only and should not be treated as final determinations.

Every scenario in this entry flow keeps:

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

A human reviewer remains responsible for evaluating evidence, missing evidence, conflicts, source-chain context, issuer authority, and any real-world reliance decision.

## Recommended Next PR

#651 Public Validator demo navigation polish
