# Witness Proof Next Layer Proposal

Status: proposal only

Context:

- The local verification package MVP is completed.
- The package core supports file integrity checks, issuer proof evidence, local timestamp proof evidence, and a first local witness proof evidence slice.
- The witness proof slice remains advisory-only and does not verify witness authority, cryptographic signatures, W3C Verifiable Credentials, C2PA credentials, external networks, or federation state.

Goal:

Add and evolve a later witness proof layer that can answer this limited question:

```text
Who or what attested to this package, record, or hash as a witness?
```

Important boundary:

- witness proof does not prove legal truth;
- witness proof does not prove identity authority by itself;
- witness proof does not prove timestamp authority;
- witness proof does not make `truth_guarantee=true`;
- witness proof only strengthens attestation evidence;
- manifest-only hash claims are not trusted as local subject evidence unless they are backed by verified local evidence.

Simple open-source direction:

- start with a local `witness_proof` manifest entry;
- check local file presence and SHA-256 digest first;
- parse minimal JSON fields;
- require explicit subject binding before reporting `PRESENT`;
- report witness evidence as advisory evidence;
- keep cryptographic signature, W3C VC, C2PA, and federation validation for later separate implementations.

Current local manifest shape:

```json
{
  "witness_proof": {
    "path": "witness-proof.json",
    "sha256": "..."
  }
}
```

Current minimal witness proof JSON:

```json
{
  "witness_id": "HC-WITNESS-SAMPLE",
  "statement": "sample package witnessed",
  "subject_sha256": "..."
}
```

Subject binding requirement:

- `subject_sha256` must bind to verified local package evidence before witness proof can return `PRESENT`;
- the current implementation treats matched local file digests as local subject evidence;
- top-level manifest fields such as `subject_sha256`, `content_hash`, or `record_hash` are claims and must not bind witness subjects by themselves;
- if package-level, record-level, or content-level subject binding is added later, the referenced hash must be derived from or otherwise validated against local evidence in a separate test-backed implementation slice;
- if the witness proof file is digest-valid but the subject is unrelated or cannot be matched to verified local subject evidence, the result must not be `PRESENT`;
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

Current implementation slice should only:

- parse optional `witness_proof` manifest entry;
- check witness proof file path stays inside the package;
- check witness proof file exists;
- check SHA-256 digest match;
- parse minimal JSON fields;
- validate `subject_sha256` against verified local subject evidence before returning `PRESENT`;
- reject manifest-only `content_hash` or `record_hash` claims unless backed by local subject evidence;
- add result to CLI JSON and summary;
- add tests for not provided, present, missing, mismatch, invalid, and subject mismatch.

Current implementation slice should not:

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

A journalist publishes a package with a claim, source file, issuer proof, and timestamp proof. A witness proof would not prove the claim is true. It would only show that a named human, institution, AI system, or local witness record attested to a subject hash that is bound to verified local package evidence. If the witness proof points to a different hash, or to a manifest-only hash claim that is not backed by local evidence, HC must show that mismatch instead of reporting the witness as present for this package.

Next safe action:

- keep the current local witness proof presence, digest checks, and verified-subject binding checks test-backed;
- only expand package-level or record/content-hash subject binding in a separate PR with explicit local-evidence derivation and regression tests.
