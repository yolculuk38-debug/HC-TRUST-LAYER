from federation_consensus import (
    ConsensusDecision,
    evaluate_federation_consensus,
)



def test_consensus_reached():
    result = evaluate_federation_consensus(
        [
            {"approved": True, "weight": 50},
            {"approved": True, "weight": 30},
            {"approved": False, "weight": 20},
        ]
    )

    assert result["decision"] == ConsensusDecision.CONSENSUS_REACHED



def test_federation_conflict():
    result = evaluate_federation_consensus(
        [
            {"approved": False, "weight": 60},
            {"approved": True, "weight": 40},
        ]
    )

    assert result["decision"] == ConsensusDecision.CONFLICT
