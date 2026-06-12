# Witness Proof Next Layer Proposal

Status: proposal only

Context:

- The local verification package MVP is completed.
- The package core supports file integrity checks, issuer proof evidence, and local timestamp proof evidence.
- The package core does not yet include a witness proof layer.

Goal:

Add a later witness proof layer that can answer this limited question:

```text
Who or what attested to this package, record, or hash as a witness?
```

Important boundary:

- witness proof does not prove legal truth;
- witness proof does not prove identity authority by itself;
- witness proof does not prove timestamp authority;
- witness proof does not make `truth_guarantee=true`;
- witness proof only strengthens attestation evidence.

Simple open-source direction:

- start with a local `witness_proof` manifest entry;
- check only local file presence and SHA-256 digest first;
- parse minimal JSON fields;
- report witness evidence as advisory evidence;
- keep cryptographic signature, W3C VC, and federation validation for later separate implementations.

Proposed later manifest shape:

```json
{
  "witness_proof": {
    "path": "witness-proof.json",
    "sha256": "..."
  }
}
```

Proposed minimal witness proof JSON:

```json
{
  "witness_id": "HC-WITNESS-SAMPLE",
  "statement": "sample package witnessed",
  "subject_sha256": "..."
}
```

Proposed local states:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `UNVERIFIED_SIGNATURE`

First implementation slice should only:

- parse optional `witness_proof` manifest entry;
- check witness proof file path stays inside the package;
- check witness proof file exists;
- check SHA-256 digest match;
- parse minimal JSON fields;
- add result to CLI JSON and summary;
- add tests for not provided, present, missing, mismatch, invalid.

First implementation slice should not:

- call external networks;
- validate W3C Verifiable Credentials;
- verify C2PA credentials;
- verify cryptographic signatures;
- change workflows;
- change public validator contract;
- claim production readiness.

Required output boundaries:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required` remains evidence-driven.

Real-world example:

A journalist publishes a package with a claim, source file, issuer proof, and timestamp proof. A witness proof would not prove the claim is true. It would only show that a named human, institution, AI system, or local witness record attested to the package hash or record under a visible statement.

Next safe action:

- implement only local witness proof presence and digest checks in a small test-backed PR.
