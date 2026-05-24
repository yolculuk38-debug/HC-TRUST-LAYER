# HC-TRUST-LAYER Verification Routing Model (Foundation)

## Status

- documentation-only architecture foundation
- no production routing implementation in this phase
- no automatic trust decisions

## Verification Routing Overview

Verification routing in HC-TRUST-LAYER defines how verification requests can be directed across local, federation, and offline contexts while preserving provenance and audit trail visibility.

Routing decisions are policy-guided and human-supervised.

## Local Verification Routing

Local verification routing handles first-pass checks within a single operator boundary.

Concepts:

- local validator capability matching
- deterministic canonical record lookup
- local provenance cache usage boundaries
- local dispute and revocation pre-check gates

## Federation Verification Routing

Federation verification routing extends requests to interoperable HC:// participants.

Concepts:

- policy-constrained federation target selection
- capability and trust anchor compatibility checks
- federated evidence import with audit trail tagging
- explicit handling for partial or conflicting federation responses

## Offline Verification Routing

Offline verification routing supports disconnected verification workflows.

Concepts:

- routing to locally available validator capability
- use of local verification snapshot references
- missing-reference warnings when external lookup is unavailable
- deferred federation reconciliation once connectivity returns

## Validator Selection Concepts

Validator selection in routing should remain transparent and inspectable.

Concepts:

- match request type to declared validator capability
- prefer diversity of validators for sensitive workflows
- weight dispute state and revocation freshness in selection context
- preserve rationale in audit trail records

## Trust Graph Query Routing

Trust graph query routing resolves graph-linked evidence paths for verification.

Concepts:

- canonical-record-first graph traversal
- provenance and witness branch retrieval
- validator and dispute edge retrieval
- continuity checks for broken chain-of-reference segments

## Dispute-Aware Routing

Dispute-aware routing escalates contested records for stricter handling.

Concepts:

- detect dispute linkage before final result presentation
- prioritize validators with dispute review capability
- route to human-supervised validation checkpoints
- include supersession and revocation context in outputs

## Provenance Lookup Routing

Provenance lookup routing targets lineage sources needed for verification explanations.

Concepts:

- source and derivative lineage resolution
- federation-aware provenance reconciliation
- ambiguous lineage flagging
- preservation of lookup trace in audit trail

## Public Verification Routing Concepts

Public verification routing concepts define how HC-TRUST-LAYER may expose routing outcomes to public verification interfaces.

Concepts:

- bounded public result summaries
- clear distinction between evidence status and truth claims
- disclosure of routing scope (local/federated/offline)
- references to canonical record and supporting provenance context

## Terminology Alignment

This foundation aligns with:

- HC-TRUST-LAYER
- HC://
- verification routing
- trust graph
- provenance
- validator capability
- evidence continuity
- audit trail
- federation
- canonical record
- human-supervised validation
