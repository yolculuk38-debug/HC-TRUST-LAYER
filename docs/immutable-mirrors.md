# Immutable Mirror Strategy

## Objective
Define a multi-target immutable publication strategy for verification evidence and release snapshots.

## Mirror Targets
- **IPFS snapshots**: content-addressed packaging for deterministic retrieval.
- **Arweave mirrors**: permanent archival persistence for long-term auditability.
- **OpenTimestamps**: timestamp anchoring for independent temporal proof.

## Release Snapshot Policy
1. Produce deterministic release package.
2. Compute canonical hash manifest.
3. Publish to IPFS and record CID.
4. Publish mirror payload to Arweave and record transaction ID.
5. Submit hash manifest digest to OpenTimestamps.
6. Store mirror references in release metadata and audit chain.

## Federation Mirror Strategy
- Federation nodes may host independent mirrors while preserving canonical hash equivalence.
- Mirror metadata must include source node, publication timestamp, and integrity references.
- Nodes should periodically verify cross-mirror consistency.

## Backup Verification Policy
- Perform scheduled hash checks across all mirror targets.
- Escalate mismatches to `quarantined` state for affected records/releases.
- Retain prior successful checks as audit evidence.
