# Source Inventory Search Anchor Status

Status: advisory checkpoint.

This note records the first connector-search-based source anchor review after the non-mutating inventory checklist.

This is not a full source inventory output. The source inventory reporter still needs to be run locally or in a trusted execution environment for a complete JSON report.

## Search-confirmed anchors

- `src/hc_trust/verification_package.py` has direct verification-package test anchors, including `tests/test_verification_package_hash_core.py`, `tests/test_verification_package_sample.py`, `tests/test_verification_package_witness_proof.py`, and `tests/test_verification_package_timestamp_proof.py`.
- `src/hc_trust/cli.py` appears in verification-package search results and is linked to the local verifier CLI path.
- `src/trust_graph.py` has `tests/test_trust_graph.py`.
- `src/explainable_trust_graph.py` has `tests/test_explainable_trust_graph.py`.
- `src/trust_graph_passport_integration.py` has `tests/test_trust_graph_passport_integration.py`.
- `src/evidence_trust_graph_integration.py` has `tests/test_evidence_trust_graph_integration.py`.
- `src/manipulation_detection.py` has `tests/test_manipulation_detection.py` and additional test coverage.
- `src/certificate_chain.py` has `tests/test_certificate_chain.py`.

## Decision

Do not classify these files as cleanup targets from name alone. They have at least one search-visible source, test, or documentation anchor.

## Remaining work

- Run the full non-mutating source inventory reporter.
- Review files that appear without test, import, or documentation anchors.
- Keep all cleanup blocked until the source inventory review checklist conditions are met.
