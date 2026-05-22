from adaptive_risk_engine import (
    AdaptiveRiskLevel,
    evaluate_adaptive_risk,
)



def test_stable_adaptive_risk():
    result = evaluate_adaptive_risk(
        propagation_growth=0,
        federation_degradation=0,
        anomaly_signals=0,
        trust_decay=0,
    )

    assert result["adaptive_risk_level"] == AdaptiveRiskLevel.STABLE



def test_critical_adaptive_risk():
    result = evaluate_adaptive_risk(
        propagation_growth=3,
        federation_degradation=2,
        anomaly_signals=2,
        trust_decay=2,
    )

    assert result["adaptive_risk_level"] == AdaptiveRiskLevel.CRITICAL
