"""Behavior tests for the V1 family-history application use case."""

from sim_origins.application.generate_family_history import GenerateFamilyHistory


def test_generate_family_history_acknowledges_target_without_generating_relatives():
    result = GenerateFamilyHistory().execute(target_sim_id=1234)

    assert result.accepted is True
    assert result.generated is False
    assert result.target_sim_id == 1234
    assert "1234" in result.message
    assert "not implemented in V1" in result.message
