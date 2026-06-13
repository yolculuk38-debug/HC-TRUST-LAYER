# Test Inventory Search Anchor Status

Status: advisory checkpoint.

This note records connector-search and direct-file evidence for selected test anchors after the outside-review coverage concern.

This is not a full test inventory output. It records evidence found through repository search and targeted file reads.

## Confirmed test anchors

- `tests/test_verification_package_hash_core.py` imports `verify_verification_package` from `hc_trust.verification_package` and covers valid package verification, tamper detection, advisory flags, public-safe output, `truth_guarantee=false`, and unsafe manifest path rejection.
- `tests/test_trust_graph.py` imports `trust_graph` functions and covers valid graph behavior, tamper detection, unknown-edge review, and self-reference review.
- `tests/test_certificate_chain.py` imports certificate-chain functions and covers valid and invalid certificate-chain behavior.
- Repository search also shows verification-package sample, witness-proof, timestamp-proof, source-inventory, and integration-test status references.

## Decision

Do not treat the current test layer as absent. There are direct test anchors for multiple source areas.

This does not prove complete coverage for every source file.

## Remaining work

- Run or produce a full test inventory before rewriting tests.
- Map source files without direct test anchors to review-needed status.
- Keep test rewrites blocked until inventory evidence is reviewed.
