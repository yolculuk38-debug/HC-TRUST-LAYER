# HC-TRUST-LAYER Privacy and Redaction Model

## Purpose

This document defines privacy and redaction foundations for HC-TRUST-LAYER verification infrastructure.

It is architecture guidance only and does not claim full anonymity guarantees.

## Selective Disclosure Concepts

Selective disclosure allows verification participants to reveal only the minimum metadata needed for a given verification objective.

Principles:
- least disclosure
- purpose-limited visibility
- policy-traceable disclosure decisions
- reversible disclosure where legal/policy frameworks permit

## Redacted Metadata Concepts

Redacted metadata preserves verification utility while withholding sensitive fields.

Concepts:
- field-level redaction markers
- reason class for each redaction
- redaction integrity marker so omission is explicit
- scope-limited redaction views for public vs restricted consumers

## Private Witness Concepts

Private witness workflows allow witness identity or evidence details to remain restricted.

Concepts:
- pseudonymous witness references
- escrow or delegated reveal pathways
- policy-gated witness detail access
- audit trail markers proving private witness contribution existed

## Encrypted Package Concepts

Verification package segments may be encrypted for restricted audiences.

Concepts:
- split package: public envelope + protected section
- key-access policy metadata
- encrypted witness/dispute attachments
- explicit indicator that package contains protected sections

## Public/Private Verification Separation

HC-TRUST-LAYER should separate:
- public verification summary visibility
- private evidence review channels

Public outputs should remain reproducible for visible fields while clearly signaling hidden/private components.

## Privacy vs Provenance Tradeoffs

More provenance detail can improve auditability but increase privacy risk.

Tradeoff management concepts:
- metadata minimization by default
- bounded retention windows for sensitive provenance fields
- risk-based escalation for additional disclosure
- policy documentation for disclosure thresholds

## Institutional Verification Considerations

Institutional participants may require restricted evidence handling.

Considerations:
- role-based access separation
- legal hold and retention obligations
- independent oversight for high-impact verification decisions
- cross-institution verification package exchange with privacy policy compatibility checks

## Metadata Minimization Concepts

Metadata minimization should define what is essential for canonical record verification vs optional enrichment.

Concepts:
- required minimum fields per verification level
- prohibited over-collection categories
- privacy impact review for new metadata fields
- periodic minimization audits linked to audit trail records

## Terminology Alignment

This document aligns with:
- HC-TRUST-LAYER
- HC://
- provenance
- verification infrastructure
- verification package
- audit trail
- canonical record
- human-supervised validation
