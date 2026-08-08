# P0-4 Cryptographic Claim Inventory

Status: first bounded containment slice implemented; broader inventory remains
open for separate evidence-backed changes.

This note inventories executable names that can be read as cryptographic,
authenticity, immutability, or trust guarantees. A name is not implementation
evidence. SHA-256 consistency, field presence, or self-declared flags do not by
themselves prove signer identity, key ownership, issuer authority, immutable
storage, authenticity, or truth.

## First bounded slice: QR claim containment

| Surface | Repository evidence before this slice | Containment in this slice |
| --- | --- | --- |
| `src/qr_hardening.py` | A non-empty `signature` field could produce `VERIFIED` and `trusted: true`; no key resolution or cryptographic signature check existed. | The positive-looking result is replaced by `SIGNATURE_UNVERIFIED`; every result is fail-closed with `trusted: false`, `signature_verified: false`, advisory markers, and required human review. |
| `src/qr_orchestrator_integration.py` | The `VERIFIED` QR status could be promoted to an orchestrator trusted input. | QR trust now additionally requires an explicit `signature_verified: true`; the current inspector never emits that claim. |
| `src/hc_trust/qr_tools.py` | An unkeyed SHA-256 digest of public route fields was named `generate_signature` and exposed as `sig`. | It is relabeled as an advisory checksum with an explicit profile; generated links use `checksum` and `checksum_profile`. |
| `src/hc_trust/cli.py` and QR examples | Generated navigation images were described as `Secure QR`. | CLI and example wording now says `Advisory QR navigation helper`. |

No cryptography was added by this naming correction. The checksum remains an
unkeyed consistency value and must not be used as an authenticity signal.

## Remaining named surfaces

| Surface | Observed implementation boundary | Required follow-up before a stronger claim |
| --- | --- | --- |
| `src/cryptographic_identity.py` | Computes a SHA-256 fingerprint over supplied witness/key text; it does not prove key possession or identity. | Relabel as fingerprint consistency and return explicit ownership/identity-unverified markers. |
| `src/signed_export_package.py` | Computes an unkeyed SHA-256 digest from public signer text and payload. | Relabel as checksum packaging or implement a separately reviewed keyed/signature profile. |
| `src/immutable_snapshot.py`, `src/immutable_snapshot_core.py` | Provide local hashes/hash links or a declared `IMMUTABLE` state; they do not enforce immutable storage. | Relabel as hash-linked snapshot consistency and state the storage boundary. |
| `src/certificate_chain.py`, `src/certificate_verifier.py`, `src/verification_certificate.py` | Propagate certificate-shaped data and self-declared flags without cryptographic issuer validation. | Constrain to certificate-shape/advisory checks and make issuer/signature authority false unless separately verified. |
| `src/network_trust_proof.py`, `src/signed_bundle.py`, `src/witness_signature.py`, `src/exported_proof.py` | Build or validate shapes and caller-provided values without proving the named trust/signature/proof properties. | Relabel the outputs or add explicit unverified markers; do not infer authority from shape presence. |

## Evidence-backed cryptographic helpers

The following modules use keyed HMAC-SHA256 verification with
`hmac.compare_digest` and are therefore not part of the current renaming slice:

- `src/hc_trust/signed_payload.py`
- `src/signed_federation_exchange.py`
- `src/signed_witness.py`

Their cryptographic consistency checks still do not establish external signer
identity, legal authority, real-world truth, or production readiness. Existing
experimental/advisory boundaries remain required.

## Operating boundary

Future P0-4 changes must remain small, preserve compatibility deliberately,
add regression tests for the corrected claim boundary, and avoid introducing
new cryptography as a shortcut for a naming problem. Human maintainers retain
final authority.
