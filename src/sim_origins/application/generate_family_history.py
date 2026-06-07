"""Application entry point for family-history generation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class GenerateFamilyHistoryResult:
    """Outcome returned to adapters that request family-history generation."""

    accepted: bool
    generated: bool
    target_sim_id: int
    message: str


class GenerateFamilyHistory:
    """Acknowledge a generation request without creating relatives in V1."""

    def execute(self, target_sim_id: int) -> GenerateFamilyHistoryResult:
        return GenerateFamilyHistoryResult(
            accepted=True,
            generated=False,
            target_sim_id=target_sim_id,
            message=(
                "Sim Origins: familytree.generate dispatched for selected Sim "
                f"{target_sim_id}; family generation is not implemented in V1."
            ),
        )
