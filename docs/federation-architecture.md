# Federation Architecture (Experimental)

Status:
- implemented: federation manifest schema and registry scaffolding exist.
- experimental: federation sync endpoints return normalized placeholder responses.
- planned: signed federation handshakes, dispute routing, and validator quorum rules.
- research: cross-network cryptographic attestation interoperability.

## Federation goals

HC-TRUST-LAYER federation aims to let independent nodes exchange verifiable record metadata without central narrative authority. The architecture keeps a strict boundary between transport and trust decisions.

## Trust limitations

- Node membership is currently static and placeholder-based.
- Public-key rotation and revocation workflows are not yet implemented.
- Federation responses are non-production and should not be used as sole evidence.

## Distributed verification vision

The long-term direction is a validator-network-compatible model where nodes publish capabilities, synchronize references, and contribute independent confirmations.

## Replay protection goals

Replay resistance is treated as a protocol requirement. Current code introduces timestamp skew concepts, nonce placeholders, and request-fingerprint normalization as foundations.

## Non-production warning

This architecture layer is a foundation only. It is suitable for interface alignment and integration planning, not for production security assertions.

> Trust the record, not the narrative.
