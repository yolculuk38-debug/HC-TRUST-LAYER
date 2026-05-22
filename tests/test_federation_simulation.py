from federation_simulation import simulate_federation_scenario



def test_stable_federation_simulation():
    result = simulate_federation_scenario(
        nodes=[
            {"weight": 50, "trusted": True},
            {"weight": 30, "trusted": True},
            {"weight": 20, "trusted": False},
        ],
        manipulation_pressure=10,
    )

    assert result["consensus"]["decision"] == "CONSENSUS_REACHED"



def test_degraded_federation_simulation():
    result = simulate_federation_scenario(
        nodes=[
            {"weight": 50, "trusted": True, "compromised": True},
            {"weight": 25, "trusted": True},
            {"weight": 25, "trusted": True},
        ],
        manipulation_pressure=75,
    )

    assert result["degraded_nodes"] == 1
