from security_gate_layer import (
    SecurityDecision,
    evaluate_security_gate,
)



def test_allow_security_gate():
    result = evaluate_security_gate(
        risk_level="LOW",
        adaptive_risk="STABLE",
        compromised_nodes=0,
    )

    assert result["decision"] == SecurityDecision.ALLOW



def test_critical_lock_security_gate():
    result = evaluate_security_gate(
        risk_level="CRITICAL",
        adaptive_risk="CRITICAL",
        compromised_nodes=3,
    )

    assert result["decision"] == SecurityDecision.CRITICAL_LOCK
