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
- check local file presence and SHA-256 digest first;
- parse minimal JSON fields;
- require explicit subject binding before reporting `PRESENT`;
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

Subject binding requirement:

- `subject_sha256` must bind to the package, record, content hash, or another explicit manifest subject before witness proof can return `PRESENT`;
- if the witness proof file is digest-valid but the subject is unrelated or cannot be matched to an explicit local subject, the result must not be `PRESENT`;
- unrelated or unmatched subject evidence should be reported as `INVALID` or a dedicated subject-mismatch state in the implementation slice;
- this prevents treating any valid witness file as evidence for the current package.

Proposed local states:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `SUBJECT_MISMATCH`
- `UNVERIFIED_SIGNATURE`

First implementation slice should only:

- parse optional `witness_proof` manifest entry;
- check witness proof file path stays inside the package;
- check witness proof file exists;
- check SHA-256 digest match;
- parse minimal JSON fields;
- validate `subject_sha256` against the package hash, record/content hash, or another explicit manifest subject before returning `PRESENT`;
- add result to CLI JSON and summary;
- add tests for not provided, present, missing, mismatch, invalid, and subject mismatch.

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

A journalist publishes a package with a claim, source file, issuer proof, and timestamp proof. A witness proof would not prove the claim is true. It would only show that a named human, institution, AI system, or local witness record attested to the package hash or record under a visible statement. If the witness proof points to a different hash, HC must show that mismatch instead of reporting the witness as present for this package.

Next safe action:

- implement only local witness proof presence, digest checks, and subject binding checks in a small test-backed PR.
