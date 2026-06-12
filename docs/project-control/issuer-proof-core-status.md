# Issuer Proof Core Status

Status: completed local core slice

Completed reference:

- #847 added optional issuer proof evidence checks to the verification package core.

Current capability:

- package files are checked by SHA-256;
- `manifest.json` may include `issuer_proof`;
- issuer proof evidence is checked for file presence, SHA-256 match, and minimal JSON fields;
- output keeps `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.

Current states:

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`

Do-not-repeat:

- do not repeat #838, #839, #841, #843, #845, #846, or #847 unless new repository evidence appears.

Next safe action:

- update the sample package and quickstart so the example demonstrates issuer proof evidence.
