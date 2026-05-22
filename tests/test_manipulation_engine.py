from manipulation_engine import (
    ManipulationRisk,
    evaluate_manipulation_signals,
)


def test_low_manipulation_risk():
    result = evaluate_manipulation_signals(
        {
            "repost_clusters": 0,
            "self_reference_loops": 0,
            "coordinated_signals": 0,
            "contamination_links": 0,
        }
    )

    assert result["risk"] == ManipulationRisk.LOW


def test_critical_manipulation_risk():
    result = evaluate_manipulation_signals(
        {
            "repost_clusters": 3,
            "self_reference_loops": 2,
            "coordinated_signals": 2,
            "contamination_links": 1,
        }
    )

    assert result["risk"] == ManipulationRisk.CRITICAL
