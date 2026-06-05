# Public Validator MVP Specification

> **Mode:** DOCUMENTATION ONLY  
> **Scope:** Public Validator MVP contract, public-safe advisory result language, human-review boundary, QR/link safety fields, and first applied verification domains.  
> **Source review:** PR #637 Public Validator MVP Readiness Review concluded **PUBLIC VALIDATOR MVP CONDITIONALLY READY** and recommended this documentation-only specification.  
> **Boundary:** This document does not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy.

## Executive Summary

The Public Validator MVP is a narrow, public-facing verification aid for HC-TRUST-LAYER records and verification packages. It should help a public user quickly understand who made a record, who approved or reviewed it, what evidence supports it, what changed, whether a QR or link appears canonical, and whether the result requires human review.

The MVP must remain advisory, public-safe, and evidence-oriented. It must not claim truth finality, legal authority, food safety certification, ministry approval, security certification, autonomous authority, live federation guarantees, or production readiness. Every result must preserve `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and `human_review_required=true`.

The MVP should be small enough to run locally or from a static/public interface when possible. It should avoid backend dependency unless explicitly approved in a later implementation plan.

## MVP Purpose

The Public Validator MVP exists to answer six public verification questions in a consistent, mobile-readable way:

1. Who made this?
2. Who approved, reviewed, or accepted responsibility for it?
3. What evidence supports it?
4. What changed or is missing?
5. Is the QR/link canonical for this record or payload?
6. Does this require human review?

The MVP result is a review aid. It surfaces record structure, declared hash state, provenance signals, source chain, responsible entities, QR/link integrity signals, and warnings without converting those signals into truth finality.

## Non-Goals

The Public Validator MVP does not:

- certify food safety, legal compliance, security, roadworthiness, journalistic truth, ministry approval, or official enforcement status;
- provide production readiness guarantees;
- create, modify, approve, archive, sign, federate, or delete HC:// records;
- replace schema, validator, signing, federation, policy, or governance controls;
- bypass human-supervised validation;
- infer real-world truth from a passing schema, hash, or QR check;
- treat a marketing page, brand sustainability page, or generic QR landing page as equivalent to a verifiable provenance record;
- claim autonomous authority over verification outcomes.

## User Journey

A public MVP journey should be short and conservative:

1. The user opens a public validator page, local demo, or approved CLI/API wrapper.
2. The user provides a record identifier, canonical URL, QR payload, verification package, or structured evidence payload.
3. The validator normalizes the input enough to identify the candidate record or payload boundary.
4. The validator checks available public-safe signals: schema status, hash status, provenance status, source chain, responsible entities, QR/link integrity, and warnings.
5. The validator returns a compact result with required contract fields.
6. The user reads the advisory result and warnings.
7. The user escalates consequential, incomplete, disputed, or ambiguous outcomes to human review.

The MVP should prefer clear language over expert-only terminology. A mobile user should be able to distinguish `PASS`, `WARNING`, `FAIL`, `PARTIAL`, `MISSING`, and `NEEDS_REVIEW` without assuming final truth.

## Required Input

The MVP should accept at least one of the following public-safe inputs when implemented:

- `record_id`: an HC:// record identifier or repository-recognized public record ID;
- `canonical_url`: a repository-declared canonical URL or approved public validator link;
- `qr_payload`: decoded QR text or structured QR payload;
- `verification_package`: a local or public-safe verification package reference;
- `evidence_payload`: a structured public-safe object containing declared schema, hash, provenance, source, or QR fields.

Inputs should be treated as untrusted until checked. Missing optional inputs should produce warnings rather than silent success.

## Required Output Contract

Every Public Validator MVP result must include the following fields:

```yaml
record_id: string | null
status: PASS | WARNING | FAIL | PARTIAL | MISSING | NEEDS_REVIEW | UNKNOWN
schema: PASS | WARNING | FAIL | PARTIAL | MISSING | UNKNOWN
hash: PASS | WARNING | FAIL | PARTIAL | MISSING | UNKNOWN
provenance: PASS | WARNING | FAIL | PARTIAL | MISSING | UNKNOWN
source_chain: list
responsible_entities: list
qr_integrity: PASS | WARNING | FAIL | PARTIAL | MISSING | NOT_PROVIDED | UNKNOWN
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
warnings: list
```

Required semantics:

- `advisory_only` must always be `true`.
- `public_safe` must always be `true`.
- `truth_guarantee` must always be `false`.
- `human_review_required` must always be `true`.
- `warnings` must always exist as a list, including when empty.
- `status` must not imply truth finality.
- `source_chain` may be empty but must exist.
- `responsible_entities` may be empty but must exist.
- `qr_integrity` must exist even when a QR input is not provided.

Recommended status interpretation:

- `PASS`: the available public-safe check passed within its implemented scope only.
- `WARNING`: one or more concerns require attention.
- `FAIL`: a supplied value conflicts with the implemented check.
- `PARTIAL`: some required or expected evidence exists, but the chain is incomplete.
- `MISSING`: the expected input or evidence is not available.
- `NEEDS_REVIEW`: the result requires explicit human interpretation before reliance.
- `UNKNOWN`: the MVP cannot determine this signal from the supplied public-safe input.

## Advisory / Public-Safe Contract

Public validator output must be written for public readers without exposing protected material, private review notes, sensitive signing secrets, or non-public governance details.

The public-safe contract is:

- display evidence availability, not private evidence contents when those contents are not public;
- display declared source and responsibility fields where available;
- display warnings for missing, stale, copied, moved, non-canonical, disputed, or incomplete signals;
- avoid production, legal, forensic, food safety, ministry approval, or security certification language;
- keep AI assistance advisory only;
- preserve human final authority.

## Human Review Boundary

Human review is required for every MVP result because public checks cannot establish truth finality, legal authority, physical safety, journalistic accuracy, or real-world custody by themselves.

Human reviewers remain responsible for:

- interpreting whether evidence is sufficient for the use case;
- contacting official authorities, labs, publishers, contractors, or record owners when necessary;
- resolving disputed records, ambiguous source chains, or conflicting evidence;
- approving governance-sensitive interpretations;
- determining whether additional protected-path validation is required.

The MVP should make the human-review boundary visible in every result by returning `human_review_required=true`.

## Source / Provenance Fields

The MVP should support public-safe source and provenance fields where available:

- `record_id`;
- `schema` or schema identifier;
- `hash` or content-hash check status;
- `provenance` status;
- `created_by` or declared originator;
- `approved_by`, `reviewed_by`, or declared reviewing authority when present;
- `source_chain` as an ordered list of source, custody, transport, editorial, or review steps;
- `responsible_entities` as an ordered or grouped list of entities with declared responsibility;
- `evidence_references` as public-safe references to documents, lab results, inspections, complaints, corrections, or packages;
- `change_summary` where available;
- `warnings` for missing, conflicting, unverifiable, or non-public evidence.

A missing source chain is not a pass. It should be represented as an empty `source_chain` list plus a warning when source-chain evidence is expected.

## QR / Link Safety Fields

The MVP should treat QR and link inputs as untrusted routing hints until checked. A QR can be copied, moved, reprinted, replaced, or pointed to a non-canonical destination.

Recommended QR/link fields:

- `qr_integrity`;
- `canonical_url`;
- `observed_url`;
- `canonical_domain_check`;
- `issuer_check`;
- `record_id_check`;
- `payload_hash_check`;
- `signed_payload_check` when available;
- `stale_qr_warning`;
- `non_canonical_url_warning`;
- `copied_or_moved_label_warning`;
- `warnings`.

A QR integrity pass should never mean that the physical item, label, article, asset, or food product is true or safe. It only means the implemented QR/link checks passed within their limited scope.

## Applied Verification Domains

The first applied verification domains are examples for public MVP shaping. They are not production deployments, legal programs, food safety certifications, ministry approvals, security certifications, or live federation guarantees.

These domains are useful because they test different verification questions:

1. imported food and banana provenance test batch, lab, authority, shipment, and retailer responsibility signals;
2. municipal road and traffic sign maintenance tests asset, contractor, authority, inspection, and complaint signals;
3. news source provenance tests publisher, editorial, primary evidence, independent confirmation, and correction signals;
4. QR spoof and non-canonical link warning tests canonical URL, issuer, record ID, payload hash, signed payload, stale QR, and copied-label warnings.

## Example Domain 1: Imported Food / Banana Provenance

This is an example domain only. It describes how the Public Validator MVP could model imported food provenance, using bananas as a concrete public-readable scenario.

The validator should be able to model:

- product category;
- batch / lot identifier;
- country of origin;
- producer / exporter;
- importer;
- transport or shipment reference;
- origin-side inspection or lab result reference;
- destination-side inspection or lab result reference;
- pesticide / residue test reference where applicable;
- ministry / authority review reference where applicable;
- independent lab review reference where applicable;
- market / retailer responsibility where applicable;
- `source_chain`;
- `responsible_entities`;
- `warnings`.

HC does not prove the food is safe by itself. HC shows what evidence exists, who provided it, whether records align, and what still requires human / official review.

A brand sustainability page or marketing QR is not the same as a verifiable provenance record. A QR can be copied or moved, so QR integrity must be checked against batch, issuer, canonical URL, and signed payload when available.

Example banana result shape:

```yaml
record_id: HC-FOOD-BANANA-2026-0001
status: NEEDS_REVIEW
schema: PASS
hash: PASS
provenance: PARTIAL
source_chain:
  - Producer
  - Exporter
  - Origin inspection authority
  - Transport / shipment
  - Importer
  - Destination inspection authority
  - Retailer
responsible_entities:
  - Producer
  - Exporter
  - Importer
  - Retailer
qr_integrity: WARNING
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
warnings:
  - Marketing QR does not provide batch-level verification.
  - Destination-side lab evidence unavailable.
  - Independent confirmation unavailable.
```

## Example Domain 2: Municipal Road / Traffic Sign Maintenance

This is an example domain only. It describes how the Public Validator MVP could model public maintenance evidence for a municipal road sign or traffic sign asset.

The validator should be able to model:

- `asset_id`;
- installation date;
- maintenance date;
- contractor;
- supervising authority;
- inspection record;
- public complaint / review reference;
- `warnings`.

The MVP can help a resident or reviewer see whether a sign has a declared maintenance record, who performed the work, who supervised it, whether inspection evidence exists, and whether public complaints or reviews are linked. It must not claim that the road is safe, that the sign is legally compliant, or that the municipality has issued a final approval unless those claims are separately established by official human review.

Potential warnings include missing inspection records, stale maintenance dates, contractor/authority mismatch, unresolved public complaints, or non-canonical asset links.

## Example Domain 3: News Source Provenance

This is an example domain only. It describes how the Public Validator MVP could model source provenance for a news article, report, or public claim.

The validator should be able to model:

- publisher;
- reporter;
- editor;
- original source;
- referenced sources;
- primary evidence;
- independent confirmation count;
- opinion / analysis marker;
- correction history;
- `warnings`.

The MVP can show whether an article declares its publisher, reporter, editor, original source, referenced sources, primary evidence, independent confirmations, opinion/analysis status, and correction history. It must not claim that the article is true, unbiased, legally approved, or free of misinformation. Public output should distinguish evidence availability from truth finality.

Potential warnings include missing original source, low independent confirmation count, unlabeled opinion/analysis, unresolved correction history, inaccessible primary evidence, or conflicting referenced sources.

## Example Domain 4: QR Spoof / Non-Canonical Link Warning

This is an example domain only. It describes how the Public Validator MVP could warn users when a QR code or link appears non-canonical, stale, copied, moved, or inconsistent with the declared record.

The validator should be able to model:

- canonical domain check;
- issuer check;
- record ID check;
- payload hash check;
- signed payload check when available;
- stale QR warning;
- non-canonical URL warning;
- copied/moved label warning.

A QR or link result should not be treated as proof of truth. QR/link safety only helps identify whether the observed route appears aligned with a declared canonical record, issuer, payload hash, and signed payload when available.

Potential warnings include observed URL not matching the canonical domain, issuer mismatch, record ID mismatch, payload hash mismatch, missing signed payload, stale QR metadata, or a physical label that may have been copied or moved.

## Error and Warning Behavior

The MVP should prefer explicit warnings over silent assumptions. Warnings should be public-readable, concise, and specific.

Required behavior:

- return `warnings` as a list for every result;
- warn when source-chain or responsible-entity fields are empty but expected;
- warn when QR/link input is not canonical, cannot be checked, is stale, lacks a signed payload, or mismatches the record ID;
- warn when schema, hash, provenance, or evidence checks are partial, missing, unknown, or failed;
- use `NEEDS_REVIEW` for consequential ambiguity;
- avoid converting warnings into truth finality claims.

Errors should not expose private repository material, secrets, signing keys, private review notes, or internal infrastructure details.

## Deferred Components

The following components are deferred to later PRs unless explicitly approved:

- runtime implementation changes;
- API contract changes;
- CLI contract changes;
- schema changes;
- validator changes;
- workflow changes;
- signing or signature-profile changes;
- federation support;
- policy changes;
- generated artifact updates;
- QR artifact generation;
- canonical record changes;
- automated trust scoring changes;
- backend service deployment.

## Security Boundaries

The Public Validator MVP must preserve security and trust-kernel boundaries:

- do not expose private keys, signing secrets, protected review material, or sensitive governance details;
- do not modify protected paths as part of public validation output;
- do not fabricate hashes, signatures, approvals, lab results, ministry reviews, publisher confirmations, or inspection evidence;
- do not auto-merge, auto-approve, or auto-certify any result;
- treat QR/link input as untrusted;
- keep all output advisory and public-safe;
- require human review for interpretation and consequential use.

## Implementation Readiness

This specification defines the expected MVP contract and applied domain shapes only. It does not assert that every field is already implemented across runtime, CLI, API, or demo surfaces.

Readiness position:

- documentation scope is ready for review;
- output contract is defined for a future implementation or contract-test PR;
- applied domains are defined as examples only;
- protected paths remain unchanged;
- implementation, validators, schemas, records, signing, federation, policy, workflows, QR artifacts, and generated artifacts remain deferred.

A future implementation should compare existing public validator, runtime, CLI, and package outputs against this contract before claiming MVP completeness.

## Recommended Next PR

Recommended next PR: **#639 Public Validator MVP contract tests or implementation plan**.

PR #639 should either:

1. add contract tests that verify existing public validator result shapes include the required advisory/public-safe fields; or
2. provide a documentation-only implementation plan that maps existing runtime, CLI, API, demo, and package surfaces to this MVP contract before code changes begin.

Either path should preserve `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, `human_review_required=true`, human final authority, public-safe language, and protected path boundaries.
