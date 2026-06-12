# Attestation Core Status

Status: completed local core slice

Completed reference:

- #867 added local attestation checks to the verification package core.

Current capability:

- `manifest.json` may include `witness_proof`;
- the referenced local evidence file is checked for presence;
- the referenced local evidence file is checked with SHA-256;
- minimal JSON fields are checked;
- `subject_sha256` must bind to an explicit local package subject before `PRESENT`;
- unmatched subject evidence returns `SUBJECT_MISMATCH`;
- CLI summary includes the local evidence status.

Current states:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `SUBJECT_MISMATCH`

Boundaries:

- no external network call;
- no signature verification;
- no legal truth claim;
- no identity authority claim;
- `truth_guarantee=false` remains required.

Do-not-repeat:

- do not repeat #867 unless new repository evidence appears.

Next safe action:

- update the sample verification package with local attestation evidence and quickstart coverage.
