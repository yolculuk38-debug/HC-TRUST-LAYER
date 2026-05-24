# HC-TRUST-LAYER HC:// Trust Graph Viewer Foundation

## Status

- documentation-only foundation
- no runtime graph viewer implementation in this phase
- no production readiness claim

## Trust Graph Viewer Overview

The trust graph viewer is a planned visualization companion for the HC-TRUST-LAYER trust graph.

Its purpose is to make trust graph relationships inspectable for provenance interpretation, audit trail continuity, and reviewer routing.

## Node Visibility Concepts

Node visibility should support:

- canonical record nodes
- provenance event nodes
- validator nodes
- witness nodes
- verification package and snapshot reference nodes

Each node type should show explicit metadata boundaries and confidence context where available.

## Edge Visibility Concepts

Edge visibility should support:

- canonical lineage edges
- provenance progression edges
- validation result association edges
- supersession/revocation edges
- replay/dispute indicator edges

Edge states should preserve inspectability and avoid implicit authority inflation.

## Validator Relationship Visibility

Validator relationship visibility should include:

- validator-to-record verification edges
- validator-to-provenance event linkage
- validator status annotations
- unresolved validator conflict markers

## Provenance Relationship Visibility

Provenance relationship visibility should include:

- source-to-record lineage edges
- revision and branch edges
- continuity gap markers
- contradiction indicators for competing lineage claims

## Federation Relationship Visibility

Federation relationship visibility should include:

- federation-origin edge markers
- bridge/sync boundary edges
- staleness/freshness annotations
- cross-node conflict indicators

Federation visuals are advisory and do not imply consensus finality.

## Replay/Dispute Relationship Indicators

Replay/dispute relationship indicators should include:

- replay cluster edge highlighting
- disputed record edge markers
- challenge lifecycle state overlays
- escalation-required indicators for human-supervised validation

## Graph Filtering Concepts

Graph filtering concepts include:

- node-type filters (record/provenance/validator/witness/package)
- time-window filters
- dispute/replay-only filters
- federation-only filters

Filtering should reduce visual noise while preserving audit trail traceability.

## Graph Isolation Concepts

Graph isolation concepts include:

- isolate one canonical record neighborhood
- isolate one provenance branch
- isolate one validator influence slice
- isolate disputed subgraphs for reviewer focus

Isolation should preserve references back to full graph context.

## Public Visualization Considerations

Public visualization considerations:

- clear legends and confidence disclaimers
- no automatic trust decision signals
- explicit unknown/insufficient-evidence states
- privacy/redaction-aware rendering rules

Public trust graph visualization must remain evidence-oriented and human-supervised validation aware.
