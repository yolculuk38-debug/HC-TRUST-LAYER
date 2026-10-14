"""Caller declarations cannot substitute for authenticated evidence."""

from copy import deepcopy

import pytest

from consensus_rules import evaluate_consensus
from consensus_status_integration import consensus_to_status
from evidence_engine import evaluate_evidence_bundle
from status_passport_integration import build_status_passport
from trust_orchestrator import orchestrate_trust_pipeline
from trust_passport import build_trust_passport
from verification_status_engine import determine_verification_status
from witness_consensus_integration import evaluate_witness_consensus
from witness_standard import create_witness_record


def complete_signals():
    return {"hash_verified": True, "witness_count": 100, "provenance_locked": True,
            "federated_verified": True, "trust_score": 100}


def asserted_response():
    return {"decision": "VERIFIED", "trusted": True,
            "signals": {"trust_score": 100, "hash": True, "signature": True}}


def assert_unverified(result):
    for field in ("trusted", "verified", "source_claims_verified", "content_hash_checked",
                  "signatures_verified", "identity_verified", "truth_guarantee", "public_safe"):
        assert result[field] is False, field
    assert result["content_hash_valid"] is None
    assert result["advisory_only"] is True
    assert result["human_review_required"] is True


def test_all_claims_cannot_authorize_orchestrator():
    bundle = dict.fromkeys(("hash", "provenance", "witness", "registry", "federation", "audit", "qr"), True)
    bundle["extension"] = {"reviewer": "claimed"}
    before = deepcopy(bundle)
    result = orchestrate_trust_pipeline(evidence_bundle=bundle, manipulation_signals={},
        registry_trusted=True, federation_trusted=True, revoked=False)
    assert_unverified(result["evidence"])
    assert result["evidence"]["decision"] == "REVIEW_REQUIRED"
    assert result["evidence"]["evidence_score"] == 0
    assert result["evidence"]["declaration_score"] == 115
    assert result["policy"]["decision"] == "REVIEW_REQUIRED"
    assert result["verified"] is result["trusted"] is False
    assert result["evidence"]["source_claims"] == before == bundle
    result["evidence"]["source_claims"]["extension"]["reviewer"] = "changed"
    assert bundle == before


@pytest.mark.parametrize("bundle", [None, [], "claims", {"hash": "true"}, {"audit": 1}, {"qr": []}])
def test_malformed_evidence_fails_closed(bundle):
    result = evaluate_evidence_bundle(bundle)
    assert result["decision"] == "INVALID"
    assert_unverified(result)


@pytest.mark.parametrize("signals", [None, [], {"hash_verified": "true"}, {"invalid": "false"},
    {"witness_count": True}, {"witness_count": -1}, {"witness_count": "3"},
    {"trust_score": 101}, {"trust_score": float("nan")}, {"risk_flags": "risk"},
    {"risk_flags": [{}]}, {"provenance_locked": []}, {"federated_verified": 1}, {"invalid": True}])
def test_malformed_or_invalid_status_signals_fail_closed(signals):
    result = determine_verification_status(signals)
    assert result["state"] == "INVALID"
    assert result["level"] == "LEVEL_0_UNVERIFIED"
    assert_unverified(result)


def test_complete_status_claims_remain_unverified_and_independent():
    signals = complete_signals()
    signals["extension"] = {"authority": True}
    before = deepcopy(signals)
    result = determine_verification_status(signals)
    assert result["state"] == "REVIEW_REQUIRED"
    assert result["level"] == "LEVEL_0_UNVERIFIED"
    assert result["trust_score"] == result["witness_count"] == 0
    assert result["source_claims"] == before == signals
    assert_unverified(result)
    result["source_claims"]["extension"]["authority"] = False
    assert signals == before


def test_witness_majority_and_caller_overrides_cannot_verify_passport():
    witnesses = [{"witness_id": f"claimed-{i}", "verdict": "PASS", "content_hash": "same"} for i in range(100)]
    consensus = evaluate_consensus(witnesses)
    assert consensus["consensus_reached"] is True  # agreement diagnostic only
    assert consensus["witness_independence_verified"] is False
    assert_unverified(consensus)
    status = consensus_to_status(consensus, base_signals=complete_signals())
    assert status["source_claims"]["consensus_result"] == consensus
    assert_unverified(status["status_result"])
    passport = build_status_passport("HC-1", complete_signals(),
        verification_response=asserted_response(), evidence_summary={"verified": True},
        federation_summary={"verified": True}, provenance_summary={"verified": True})
    assert passport["status"] == "REVIEW_REQUIRED"
    assert passport["verification_level"] == "LEVEL_0_UNVERIFIED"
    assert not any(passport["summary"].values())
    assert passport["source_claims"]["verification_response"] == asserted_response()
    assert_unverified(passport)
    assert_unverified(passport["status_engine"])


@pytest.mark.parametrize("consensus", [None, [], {"status": []}, {"status": "VERIFIED"},
    {"status": "CONFLICT"}, {"status": "INVALID_INPUT"},
    {"status": "CONSENSUS_REACHED", "witness_count": "3"}])
def test_invalid_consensus_never_promotes_base_flags(consensus):
    result = consensus_to_status(consensus, base_signals=complete_signals())
    assert result["status_result"]["state"] == "INVALID"
    assert_unverified(result["status_result"])


@pytest.mark.parametrize("witnesses,options", [(None, {}), ([], {"min_witnesses": "3"}),
    ([], {"min_witnesses": True}), ([], {"threshold": "0.5"}), ([], {"threshold": float("nan")})])
def test_invalid_consensus_parameters_have_explicit_boundary(witnesses, options):
    result = evaluate_consensus(witnesses, **options)
    assert result["status"] == "INVALID_INPUT"
    assert_unverified(result)


@pytest.mark.parametrize("response,summary", [(None, None), ({"signals": []}, None),
    ({"trusted": "true"}, None), ({"signals": {"trust_score": "100"}}, None),
    (asserted_response(), []), (asserted_response(), {"risk_flags": [{}]})])
def test_invalid_passport_inputs_fail_without_coercion(response, summary):
    result = build_trust_passport("HC-1", response, evidence_summary=summary)
    assert result["status"] == "INVALID"
    assert_unverified(result)


def test_invalid_status_cannot_be_overridden_by_verified_response():
    result = build_status_passport("HC-1", {"invalid": True}, verification_response=asserted_response())
    assert result["status"] == result["status_engine"]["state"] == "INVALID"
    assert_unverified(result)


def test_shape_valid_witness_signatures_do_not_prove_identity():
    records = [create_witness_record(f"claimed-{i}", "AI", "PASS", "2026-10-12T00:00:00Z",
        verification_method="claimed", confidence_score=100, provenance_reference="same",
        model_name="claimed", witness_signature="not-a-signature") for i in range(3)]
    result = evaluate_witness_consensus(records)
    assert result["valid_witness_count"] == 3  # legacy shape validator only
    assert result["consensus"]["consensus_reached"] is True
    assert result["signatures_verified"] is result["identity_verified"] is False
    assert_unverified(result["consensus"])


@pytest.mark.parametrize("field", ["witness_standard_version", "witness_type", "verdict"])
def test_malformed_witness_enums_are_rejected_before_consensus(field):
    record = create_witness_record("w1", "AI", "PASS", "2026-10-12T00:00:00Z",
        verification_method="claimed", confidence_score=100)
    record[field] = []
    result = evaluate_witness_consensus([record])
    assert result["validation_results"][0]["validation"]["status"] == "INVALID"
    assert result["valid_witness_count"] == 0
    assert_unverified(result["consensus"])
