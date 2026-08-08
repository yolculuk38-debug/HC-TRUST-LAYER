# HC:// Advisory QR Payload Inspection Boundary

## Purpose

The current helper performs local QR payload structure, content-hash, and URL
allowlist checks while resisting misleading trust assumptions.

A QR scan is not automatic proof. It is only a transport mechanism for
verification metadata.

This layer does not resolve keys, cryptographically verify signatures,
authenticate issuers, prove QR authenticity, or establish truth.

---

## Security Principles

- QR payloads remain untrusted after these local checks.
- Only repository-defined HC verification URL shapes are accepted.
- Unknown domains are rejected.
- A present `content` value must match the declared SHA-256 digest.
- Signature presence is reported but never treated as signature verification.
- Unsafe redirects are rejected.
- Every result preserves the advisory and human-review boundary.

---

## Supported inspection status

- `SIGNATURE_UNVERIFIED`
- `HASH_MISMATCH`
- `INVALID_QR`
- `UNSAFE_URL`
- `UNSIGNED`

`SIGNATURE_UNVERIFIED` means only that local structure, content-hash, and URL
checks passed and a non-empty signature-shaped string was present. It does not
mean that the string was cryptographically checked.

Every result returns:

- `trusted: false`
- `signature_verified: false`
- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`

---

## Required QR Payload Fields

```json
{
  "record_id": "HC-QR-2026-0001",
  "content_hash": "SHA256",
  "verification_url": "https://github.com/...",
  "created_at": "2026-05-21T00:00:00Z",
  "signature": "OPTIONAL"
}
```

---

## Threat Model

This layer is designed to surface:

- QR spoofing
- malicious redirect abuse
- fake verification pages
- modified payload attacks
- trust confusion
- silent integrity failures

---

## Future Expansion

- Defined signed QR payload profile and key resolution
- Cryptographic signature verification
- Offline QR verification
- Multi-witness QR consensus
- Hardware-backed signatures
- Time-bound QR verification
