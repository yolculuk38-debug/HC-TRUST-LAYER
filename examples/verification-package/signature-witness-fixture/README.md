# Signature/Witness Fixture Package

Status: non-canonical example package.

This package demonstrates an opaque signature-like fixture file and a locally parsed witness note. The local verifier hashes the signature-like bytes but does not parse or validate a signature, signer identity, or witness authority.

It is demo evidence only. It does not verify a real cryptographic signature, witness authority, identity finality, legal truth, C2PA assertion, OpenTimestamps attestation, W3C Verifiable Credential, federation state, or production readiness.

Expected local verifier behavior:

- `metadata/source-info.txt` is checked by SHA-256.
- `signature-proof.json` is included as a manifest-listed fixture file and is checked by SHA-256 as generic local package evidence.
- `witness-proof.json` is checked by the existing local `witness_proof` slice.
- `witness_proof.subject_sha256` binds to the local source evidence.
- `signatures_verified` remains `false`.
- `witnesses_verified` remains `false`.
- `truth_guarantee` remains `false`.

Suggested local command:

```bash
python -m hc_trust.cli verify-package examples/verification-package/signature-witness-fixture --summary
```
