# HC-TRUST-LAYER Trust Graph Data Model (Foundation)

## Status

- documentation-only architecture foundation
- no runtime trust graph implementation in this phase
- no automatic trust decisions

## Node Concepts

The HC-TRUST-LAYER trust graph models verification context using explicit node classes:

- canonical record node
- provenance event node
- witness attestation node
- validator assessment node
- dispute case node
- federation exchange node
- verification snapshot node
- audit trail event node

Each node is a documentation-level concept for HC:// interoperability planning and human-supervised validation.

## Edge Concepts

Edges describe relationships between nodes and preserve inspection paths.

Core edge categories:

- references
- attests
- validates
- supersedes
- revokes
- disputes
- federates-with
- snapshot-of
- derived-from

Edges should carry minimal metadata (time context, actor class, scope) without implying objective truth.

## Witness Linkage

Witness linkage binds witness attestations to canonical records and provenance context.

Concepts:

- one canonical record may have multiple witness edges
- witness classes (human/AI-assisted) are explicit labels
- witness edges include scope boundaries for what was observed
- witness linkage contributes evidence signals for audit trail review

## Validator Linkage

Validator linkage records how validators contribute verification outputs.

Concepts:

- validator edges reference specific verification runs or snapshots
- validator outputs are bounded by declared validator capability
- no single validator edge implies autonomous governance authority
- validator disagreement is represented as parallel, inspectable edges

## Provenance Linkage

Provenance linkage captures lineage and context transfer.

Concepts:

- parent/child or source/derivative edges
- custody and transformation markers
- missing provenance markers when lineage is incomplete
- explicit references to canonical record identifiers and hashes

## Dispute Linkage

Dispute linkage models contested evidence and review outcomes.

Concepts:

- dispute case node links claim/challenge artifacts
- dispute edges point to affected verification snapshots
- adjudication state is represented as evidence status, not truth finality
- supersession and revocation edges remain visible in the same lineage

## Federation Linkage

Federation linkage models cross-operator exchange paths in HC://.

Concepts:

- federation edges identify source node and receiving node context
- policy-bound routing constraints are represented as metadata signals
- federation imports remain reviewable through audit trail linkage
- federation linkage supports interoperability, not automatic trust transfer

## Verification Snapshot Linkage

Verification snapshot linkage preserves time-bound reproducibility.

Concepts:

- snapshot nodes reference validator outputs and policy version context
- snapshot edges link to evidence set used at verification time
- historical and current snapshot relationships can coexist
- snapshot lineage supports future verification routing decisions

## Graph Continuity Concepts

Graph continuity keeps evidence relationships interpretable over time.

Concepts:

- append-oriented growth of nodes and edges
- deterministic identifiers for canonical references
- continuity markers across archive migration and federation replay
- chain-of-reference linkage for long-term evidence continuity

## Graph Integrity Considerations

Integrity requires stable references and transparent change visibility.

Considerations:

- schema validation for graph artifacts
- deterministic node/edge identity policy
- revocation and supersession visibility
- orphan detection for broken lineage segments
- periodic integrity checks over graph partitions

## Graph Poisoning Risks

Graph poisoning risks include adversarial insertion of misleading nodes or edges.

Risk patterns:

- fabricated validator identities
- forged provenance branches
- replay injection designed to bias verification routing
- selective omission of adverse dispute linkage

Mitigation direction (future work):

- strict input validation and identity checks
- quarantine workflows for contested graph artifacts
- anomaly detection in edge creation patterns
- mandatory human-supervised validation for high-impact trust decisions

## Terminology Alignment

This foundation aligns with:

- HC-TRUST-LAYER
- HC://
- trust graph
- provenance
- verification routing
- validator capability
- evidence continuity
- audit trail
- federation
- canonical record
- human-supervised validation
