# HC-TRUST-LAYER C2PA Bridge Considerations

## Purpose

This document describes architecture considerations for a future HC-TRUST-LAYER bridge layer related to C2PA and Content Credentials ecosystems.

It does not claim full C2PA compatibility, production interoperability, cryptographic guarantees, or automatic authenticity determination.

## C2PA Overview

C2PA is an industry provenance specification oriented around signed assertions and content metadata integrity.

Within HC:// planning, C2PA is an external provenance system that may provide useful interoperability signals.

## Content Credentials Relationship

Content Credentials is commonly used to present provenance metadata derived from C2PA-aligned workflows.

For HC-TRUST-LAYER, this relationship is informative input, not a replacement for HC:// verification infrastructure boundaries.

## Provenance Interoperability Concepts

Interoperability goals include:
- mapping external provenance references into HC:// canonical record context
- preserving source system attribution
- retaining uncertainty markers where mappings are partial
- avoiding semantic overstatement when fields do not align exactly

## Metadata Signature Relationship

External metadata signatures and HC:// verification signals may coexist.

Concepts:
- verify external signature artifacts as provenance inputs
- keep HC:// validator outputs as separate verification statements
- represent signature scope boundaries so consumers know what was actually signed

## Bridge-Layer Concepts

A bridge layer may include:
- parser/normalizer for external provenance manifests
- mapping registry from external fields to HC:// fields
- conflict annotation rules
- replay and stripping risk annotations

Bridge behavior should remain deterministic, auditable, and human-supervised.

## Limitations of External Provenance Systems

Potential limitations in external systems may include:
- ecosystem-specific field semantics
- uneven platform support
- missing-chain visibility after redistribution
- partial lifecycle visibility for revocation/status changes

These limits require conservative interpretation in HC-TRUST-LAYER outputs.

## Metadata Stripping Risks

Metadata stripping can remove or alter external provenance signals during reposting, conversion, or capture.

HC:// should represent stripping indicators explicitly when provenance continuity is broken.

## Replay Risks

External provenance artifacts can be replayed in new contexts.

Bridge-layer logic should preserve replay detection markers and compare canonical record linkage before accepting derived claims.

## Trust-Layer Inconsistency Risks

Inconsistency can occur when:
- external provenance appears valid but HC:// canonical linkage fails
- revocation state differs across ecosystems
- identity semantics do not map cleanly between systems

These inconsistencies should be surfaced as auditable warnings, not silently resolved.

## Interoperability Considerations

Practical considerations:
- explicit profile/version negotiation
- unsupported-field reporting
- deterministic import/export behavior
- audit trail records for bridge transformations
- policy controls for when cross-ecosystem provenance is accepted, flagged, or quarantined

## Terminology Alignment

This document aligns with:
- HC-TRUST-LAYER
- HC://
- provenance
- verification infrastructure
- verification package
- audit trail
- trust graph
- canonical record
- replay detection
- human-supervised validation
