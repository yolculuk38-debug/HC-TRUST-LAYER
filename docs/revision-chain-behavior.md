# Immutable Revision Chain Behavior

## Revision Fields
Records may include:
- `version`
- `supersedes`
- `revision_reason`
- `previous_hash`
- `revision_timestamp`

## Behavior Rules
1. Revisions create new records; prior records are immutable.
2. `supersedes` points to prior `record_id`.
3. `previous_hash` must match the canonical hash of the superseded record payload.
4. Revision history is traversed as a directed chain for provenance and audit.
5. Any chain break or hash mismatch raises a verification anomaly.

## Verification Implications
- Trust and verification status are computed per revision and can be aggregated for lineage-level views.
- Consumers must not silently collapse revisions without preserving chain visibility.
