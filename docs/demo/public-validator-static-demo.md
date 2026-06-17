# Public Validator Static Demo

> **Status:** documentation-only static demo
> **Scope:** public-safe user-facing result screen examples
> **Authority:** advisory-only; human review remains required
> **Production readiness:** not claimed

## Overview

This page shows how an HC:// Public Validator result could appear to an end user on a mobile-friendly static page.

The examples are based on fictional demo fixtures. They are not canonical HC:// records, not live validator output, not signed payloads, not generated artifacts, and not proof that any real-world product, building, article, QR label, issuer, or claim is true.

Each result is intentionally written like a public result screen: short labels, visible evidence status, clear warnings, and a direct reminder that HC-TRUST-LAYER supports human-supervised validation rather than replacing reviewer judgment.

For static viewer scenario-link and demo `record_id` boundaries, see the [Public Validator Demo Links](public-validator-demo-links.md) guide.

## Demo Navigation

Use these demo result cards to compare common public validation scenarios:

1. [Imported Banana](#example-1-imported-banana) — food provenance with partial custody evidence and a carton-count conflict.
2. [Building / Concrete](#example-2-building--concrete) — construction material provenance with partial field sample evidence.
3. [News Source](#example-3-news-source) — news provenance with source-chain visibility and incomplete confirmation.
4. [QR Spoof Warning](#example-4-qr-spoof-warning) — QR/link review where the scanned URL differs from the expected HC:// canonical reference.

## Example 1: Imported Banana

### Record Summary

**Result:** Needs human review
**Record:** `HC-DEMO-PV-FIXTURE-FOOD-0001`
**Scenario:** Imported banana / food provenance
**Batch:** `DEMO-BANANA-BATCH-2026-04`
**Lot:** `DEMO-LOT-0187`
**Sample:** `DEMO-SAMPLE-FOOD-44A`

Visible provenance signals are available for the demo lot record, origin inspection summary, and lab method summary. The result does not certify food safety, origin truth, freshness, import legality, regulatory compliance, or fitness for consumption.

### Source Chain

- Demo grower cooperative harvest note
- Demo packhouse lot record
- Demo export inspection note
- Demo carrier handoff note
- Demo destination intake note
- Demo lab method summary

### Responsibility Chain

- Demo grower cooperative
- Demo packhouse operator
- Demo export broker
- Demo carrier
- Demo destination intake reviewer
- Demo human review approver

### Evidence

- Demo lot record: `DEMO-LOT-0187-RECORD` — present
- Demo origin inspection summary: `DEMO-ORIGIN-INSPECTION-REF` — present
- Demo lab method summary: `DEMO-LAB-METHOD-FOOD-01` — present
- Demo chromatography device reference: `DEMO-DEVICE-GC-001` — calibration reference visible

### Missing Evidence

- Independent confirmation of origin inspection issuer authority
- Destination intake image evidence
- Complete transport temperature log

### Conflicting Evidence

- Destination intake count differs from export count by two cartons.

### Warnings

- Advisory demo result only; not a food safety certification.
- Visible provenance is incomplete and requires human review.
- Conflicting carton count should be reviewed before relying on this demo result.

### Review Posture

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

## Example 2: Building / Concrete

### Record Summary

**Result:** Needs human review
**Record:** `HC-DEMO-PV-FIXTURE-CONCRETE-0001`
**Scenario:** Building / concrete provenance
**Project:** `DEMO-PROJECT-27`
**Building asset:** `DEMO-BUILDING-ASSET-A12`
**Concrete batch:** `DEMO-CONCRETE-BATCH-5509`
**Sample:** `DEMO-SAMPLE-CONCRETE-CYL-03`

Visible provenance signals are available for the batch ticket, sample collection note, and 28-day test result reference. The result does not certify building safety, structural integrity, code compliance, occupancy readiness, contractor performance, or legal approval.

### Source Chain

- Demo concrete plant batch ticket
- Demo mixer truck dispatch note
- Demo field sample collection note
- Demo lab receipt note
- Demo test result reference

### Responsibility Chain

- Demo concrete plant
- Demo mixer truck operator
- Demo field technician
- Demo concrete lab reviewer
- Demo supervising authority reviewer

### Evidence

- Demo batch ticket: `DEMO-CONCRETE-BATCH-5509-TICKET` — present
- Demo sample collection note: `DEMO-SAMPLE-CONCRETE-CYL-03` — partial
- Demo test result reference: `DEMO-CONCRETE-RESULT-28DAY-03` — present
- Demo compressive strength method reference: `DEMO-CONCRETE-METHOD-01` — present

### Missing Evidence

- Independent confirmation of sample collection witness
- Complete curing condition log
- Signed supervising authority review note

### Conflicting Evidence

- Field sample timestamp is later than one dispatch note timestamp and requires human review.

### Warnings

- Advisory demo result only; not a building safety or code compliance certification.
- Demo result references must not be treated as proof of structural integrity.
- Chain-of-custody contains partial field sample evidence.

### Review Posture

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

## Example 3: News Source

### Record Summary

**Result:** Needs human review
**Record:** `HC-DEMO-PV-FIXTURE-NEWS-0001`
**Scenario:** News source provenance
**Publisher:** Demo Daily Ledger
**Reporter role:** Demo staff reporter
**Editor role:** Demo assigning editor
**Label:** news analysis labeled

Visible provenance signals are available for the original source note, press statement reference, correction history, and partial public dataset summary. The result does not certify article truth, publisher reliability, legal status, journalistic quality, editorial independence, or absence of misinformation.

### Source Chain

- Demo public meeting note
- Demo reporter interview note
- Demo press statement
- Demo public dataset summary
- Demo correction note

### Responsibility Chain

- Demo staff reporter
- Demo assigning editor
- Demo publisher review desk
- Demo human reviewer

### Evidence

- Demo original source note: `DEMO-MEETING-NOTE-2026-05-02` — present
- Demo press statement: `DEMO-PRESS-STATEMENT-01` — present
- Demo public dataset summary: `DEMO-DATASET-SUMMARY-04` — partial
- Demo correction history: `DEMO-CORRECTION-NOTE-01` — present

### Missing Evidence

- Final independent confirmation response
- Full context for the public dataset summary

### Conflicting Evidence

- Demo press statement and demo meeting note use different date wording for the same event.

### Warnings

- Advisory demo result only; not a truth rating or news certification.
- Source provenance is partial and requires human editorial review.
- Opinion or analysis marker should remain visible to public reviewers.

### Review Posture

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

## Example 4: QR Spoof Warning

### Record Summary

**Result:** Warning: non-canonical link condition
**Record:** `HC-DEMO-PV-FIXTURE-QR-0001`
**Scenario:** QR spoof / non-canonical link review
**Scanned URL:** `https://demo.example.invalid/public-validator/banana-batch-0187`
**Expected HC:// reference:** `hc://demo/public-validator/banana-batch-0187`
**Issuer:** Demo Label Issuer

The scanned URL differs from the expected HC:// canonical reference in this fictional demo input. The result does not claim fraud, malicious intent, legal liability, signature validity, issuer authority, or forensic certainty.

### Source Chain

- Demo QR label scan observation
- Demo expected HC:// canonical reference
- Demo issuer reference note

### Responsibility Chain

- Demo label issuer
- Demo scanner operator
- Demo human reviewer

### Evidence

- Demo scanned URL observation: `DEMO-SCANNED-URL-OBSERVATION-01` — present
- Demo canonical HC:// reference: `DEMO-CANONICAL-HC-REFERENCE-01` — present
- Demo issuer reference: `DEMO-ISSUER-QR-01` — partial

### Missing Evidence

- Independently verified issuer authority
- Signed payload evidence
- Real payload hash verification
- Original QR artifact image

### Conflicting Evidence

- Scanned URL differs from the expected HC:// canonical URL in this demo fixture.

### Warnings

- Advisory demo result only; not a fraud finding or forensic determination.
- Non-canonical link condition requires human review before any reliance.
- This demo does not validate signatures, generate QR artifacts, or fetch remote URLs.

### Review Posture

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

## Human Review Reminder

HC-TRUST-LAYER helps expose record identity, source-chain, responsibility-chain, evidence, missing evidence, conflicting evidence, and warning signals for review.

A public result screen is not the final decision-maker. A human reviewer must decide whether the visible evidence, gaps, conflicts, custody context, and intended use support any next step. High-impact, disputed, incomplete, ambiguous, safety-related, legal, regulatory, or public-interest uses should be escalated through appropriate human-supervised review.

## What HC Does

- Shows a public-safe summary of an HC:// review target.
- Makes source-chain and responsibility-chain information easier to inspect.
- Separates visible evidence from missing or conflicting evidence.
- Surfaces warnings in plain language.
- Preserves `advisory_only: true` and `human_review_required: true` as public review boundaries.
- Supports reviewable, evidence-preserving workflows for future Public Validator UX planning.

## What HC Does NOT Do

- Does not guarantee objective truth.
- Does not certify food safety, building safety, news truth, QR authenticity, legal status, regulatory compliance, or production readiness.
- Does not replace human judgment, editorial review, engineering review, legal review, safety review, or governance review.
- Does not assert signature validity, federation status, issuer authority, policy approval, or canonical record status for these demo examples.
- Does not create or modify records, hashes, QR artifacts, generated artifacts, schemas, validators, signing logic, federation logic, policy files, runtime behavior, tests, workflows, or governance controls.

## Future Directions

A later reviewed PR could decide whether and how to connect this static demo to Public Validator navigation. That follow-up should remain scoped, public-safe, mobile-readable, and human-supervised.

Recommended next PR: **#644 Public Validator navigation integration review**.
