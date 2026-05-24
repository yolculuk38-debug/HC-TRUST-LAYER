# HC-TRUST-LAYER Validator Capability Model (Foundation)

## Status

- documentation-only architecture foundation
- no production validator auto-selection in this phase
- no autonomous governance claims

## Validator Capability Declaration

A validator capability declaration is a structured statement of what a validator can verify under HC:// constraints.

Declaration concepts:

- validator identity and version metadata
- supported verification types
- signing and key-management scope
- federation participation scope
- dispute review scope
- snapshot compatibility scope

Declarations are evidence artifacts for human-supervised validation, not self-validating trust claims.

## Supported Verification Types

Capability declarations should enumerate verification types explicitly.

Examples:

- canonical record integrity checks
- provenance consistency checks
- witness envelope verification
- revocation and supersession checks
- verification package checks

Unsupported verification types should be explicit to prevent over-interpretation.

## Signing Capability Concepts

Signing capability indicates whether and how a validator can sign outputs.

Concepts:

- signing profiles and key lineage references
- signature timestamp and validity windows
- key rotation and revocation visibility
- signing scope boundaries (what is signed vs. referenced)

## Federation Participation Capability

Federation participation capability describes interoperability posture.

Concepts:

- accepted federation exchange formats
- trust anchor compatibility declarations
- replay and duplicate handling behavior
- policy constraints for inbound/outbound exchange

Capability presence does not imply blanket federation trust.

## Offline Verification Capability

Offline verification capability describes validator operation under disconnected conditions.

Concepts:

- minimum local artifacts required for verification
- cached policy/profile snapshot behavior
- missing-reference reporting behavior
- delayed synchronization expectations

## Dispute Review Capability

Dispute review capability indicates whether validator workflows include dispute-aware checks.

Concepts:

- ability to surface dispute status with verification outputs
- support for supersession and revocation references
- policy hook points for escalation to human reviewers
- traceable dispute evidence pointers in audit trail outputs

## Snapshot Support Concepts

Snapshot support indicates compatibility with verification snapshot workflows.

Concepts:

- snapshot schema/version support matrix
- historical snapshot replay support declarations
- snapshot integrity and linkage checks
- snapshot export/import compatibility notes

## Future Compatibility Declarations

Future compatibility declarations help HC-TRUST-LAYER plan validator interoperability evolution.

Concepts:

- forward-compatible field handling policy
- deprecation and migration signaling
- extension namespace support
- compatibility testing statement references

## Terminology Alignment

This foundation aligns with:

- HC-TRUST-LAYER
- HC://
- validator capability
- provenance
- verification routing
- evidence continuity
- audit trail
- federation
- canonical record
- human-supervised validation
