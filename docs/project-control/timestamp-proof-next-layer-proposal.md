# Timestamp Proof Next Layer Proposal

Status: proposal only

Context:

- The local verification package MVP is completed.
- The current local MVP checks package file integrity with SHA-256.
- The current local MVP checks optional issuer proof evidence.
- The current local MVP does not yet prove that a package existed at a given time.

Goal:

Add a later timestamp proof layer that can answer this limited question:

```text
Was this package or package hash known at or before a claimed time?
```

Important boundary:

- timestamp proof does not prove legal truth;
- timestamp proof does not prove identity authority;
- timestamp proof does not prove witness authority;
- timestamp proof does not make `truth_guarantee=true`;
- timestamp proof only strengthens time-existence evidence.

Simple open-source direction:

- start with a local `timestamp_proof` manifest entry;
- check only local file presence and SHA-256 digest first;
- report timestamp evidence as advisory evidence;
- keep external timestamp verification for a later separate implementation;
- use OpenTimestamps as the preferred future open timestamp reference.

Proposed later manifest shape:

```json
{
  "timestamp_proof": {
    "path": "timestamp-proof.json",
    "sha256": "..."
  }
}
```

Proposed local states:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `UNVERIFIED_EXTERNAL`

First implementation slice should only:

- parse optional `timestamp_proof` manifest entry;
- check timestamp proof file path stays inside the package;
- check timestamp proof file exists;
- check SHA-256 digest match;
- parse minimal JSON fields;
- add result to CLI JSON and summary;
- add tests for not provided, present, missing, mismatch, invalid.

First implementation slice should not:

- call external networks;
- verify OpenTimestamps remotely;
- change workflows;
- change public validator contract;
- change schema or records;
- claim production readiness.

Required output boundaries:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required` remains evidence-driven.

Real-world example:

A journalist publishes a package with a claim, source file, and issuer proof. Timestamp proof would not prove the claim is true. It would only help show that this package hash existed at or before a given time, similar to how a notary or bank receipt proves a record existed at a time without proving every statement inside is true.

Next safe action:

- implement only local timestamp proof presence and digest checks in a small test-backed PR.
