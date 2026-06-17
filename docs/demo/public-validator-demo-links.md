# HC:// Public Validator demo links

This page documents the current public-safe static demo link patterns for the HC:// Public Validator viewer.

The static viewer is a demo-only page. It does not call a backend, perform canonical lookup, verify truth, prove QR authenticity, validate signed payloads, or certify food, building, news, legal, or forensic claims.

Safety markers remain required:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`

## Scenario links

The current static viewer supports bundled scenario selection through the `scenario` query parameter:

```text
public-validator-static-viewer.html?scenario=banana
public-validator-static-viewer.html?scenario=building
public-validator-static-viewer.html?scenario=news
public-validator-static-viewer.html?scenario=qr-spoof
```

These links are useful for simple QR-style demo navigation. They select fixture scenarios only.

## Demo record IDs

The viewer also includes a local demo `record_id` form. A supported demo `record_id` can be pasted into the page to render the matching bundled fixture scenario.

Supported demo IDs:

```text
HC-DEMO-PV-FIXTURE-FOOD-0001       -> banana
HC-DEMO-PV-FIXTURE-CONCRETE-0001   -> building
HC-DEMO-PV-FIXTURE-NEWS-0001       -> news
HC-DEMO-PV-FIXTURE-QR-0001         -> qr-spoof
```

This is fixture matching only, not canonical record lookup.

## Current boundary

Current supported link behavior:

```text
scenario query parameter -> supported
record_id form input     -> supported
record_id query parameter -> not yet supported
```

A future implementation PR may add `record_id` query-string support so a QR/link can open a demo result directly by `record_id`. That future change must stay static, public-safe, advisory-only, and fixture-only unless a separate backend/canonical verification layer is explicitly added later.

## Non-goals

This demo page must not be represented as:

- production verification;
- QR authenticity verification;
- signed payload verification;
- canonical record lookup;
- truth certification;
- autonomous AI authority;
- food, building, news, legal, or forensic certification.
