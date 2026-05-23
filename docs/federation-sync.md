# Federation Sync Specification

## Sync Model
Federation synchronization exchanges signed verification events and trust metadata between nodes.

## Conflict Handling
- Conflicts are recorded, not dropped.
- Divergent states are represented as parallel branches until adjudication.

## Replay Handling
- Event deduplication based on event hash and signer identity.
- Late or replayed events trigger anomaly checks before acceptance.

## Validator Trust
- Incoming validator events are weighted by current federation trust policy.
- Low-trust validators may be accepted with reduced influence pending corroboration.

## Federation Recovery
- Recovery mode rehydrates from immutable snapshots and signed event logs.
- Missing segments are requested from peers and verified by hash.

## Mirror Reconciliation
- Nodes reconcile IPFS/Arweave references against canonical release manifests.
- Any mismatch produces a reconciliation alert and temporary quarantine scope.

## Trust Propagation
- Trust changes propagate as signed events.
- Downstream nodes recompute local trust projections using local policy weights.
