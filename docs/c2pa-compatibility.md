# HC-TRUST-LAYER C2PA Compatibility Foundation

## Scope

This document defines how HC-TRUST-LAYER interoperates with C2PA-compatible provenance systems.
HC-TRUST-LAYER does not replace C2PA. It operates as a complementary verification layer.

## Positioning

C2PA provides a standardized media provenance manifest model.
HC-TRUST-LAYER provides an `HC://` verification layer for integrity checks, signed witness records, audit context, and machine-readable verification outcomes.

In this model:

- C2PA remains the source of media assertion and manifest semantics.
- `HC://` adds independently verifiable trust and witness evidence.
- Both systems can be evaluated in parallel during verification.

## Core Mapping: C2PA Concepts to HC:// Layer

| C2PA concept | HC-TRUST-LAYER compatible element | Notes |
| --- | --- | --- |
| content hash | `content_hash` in HC evidence record | Hash of the verified media object used for integrity matching. |
| manifest | `source_manifest_ref` and normalized manifest metadata | Reference to original C2PA manifest plus extracted fields used for cross-check. |
| signed record | `signed_hc_record` | HC-signed attestation object linked to hash and provenance metadata. |
| witness report | `witness_report` | Structured witness/audit output bound to verification event and media hash. |
| provenance chain | `provenance_chain` | Ordered chain linking source assertions, transformations, and verification checkpoints. |
| verification URL | `hc_verification_url` (`HC://...`) | Resolver endpoint or URI for retrieval of verification package and status. |

## Future Bridge Model

HC-TRUST-LAYER bridge support is planned as a compatibility profile with the following components:

1. **C2PA manifest import**
   - Parse C2PA manifest assertions and signature metadata into a normalized intermediate form.
2. **HC verification package export**
   - Emit an HC package containing integrity results, signed records, witness reports, and resolver references.
3. **Provenance cross-check**
   - Compare C2PA manifest lineage with HC provenance chain checkpoints and flag divergence.
4. **Signed media mapping**
   - Bind media digest + signer identity metadata to both C2PA signature context and HC signed record context.

## Limitations and Security Boundaries

HC-TRUST-LAYER has explicit limits and should be interpreted accordingly:

- HC does not prove that media claims are true.
- HC verifies integrity, provenance linkage, and witness/audit context.
- HC verification outcomes indicate consistency and evidence availability, not factual correctness of depicted events.

## Implementation Guidance

- Keep C2PA parsing and HC verification modules logically separate.
- Preserve raw C2PA manifest references when creating HC records to support deterministic re-verification.
- Require explicit versioning for mapping schemas to prevent silent compatibility drift.
- Return machine-readable mismatch codes for provenance cross-check failures.
