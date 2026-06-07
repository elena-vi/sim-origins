"""Testable command adapter for familytree.generate."""

NO_ACTIVE_SIM_MESSAGE = (
    "Sim Origins: no active Sim is selected. Select a Sim and try again."
)


class FamilyTreeGenerateCommand:
    """Resolve the connection's active Sim and delegate to the application layer."""

    def __init__(self, client_manager, use_case, output, logger):
        self._client_manager = client_manager
        self._use_case = use_case
        self._output = output
        self._logger = logger

    def execute(self, connection):
        target_sim_id = self._resolve_target_sim_id(connection)
        if target_sim_id is None:
            self._output(NO_ACTIVE_SIM_MESSAGE)
            self._logger.warn(NO_ACTIVE_SIM_MESSAGE)
            return False

        result = self._use_case.execute(target_sim_id=target_sim_id)
        self._output(result.message)
        self._logger.info(
            f"familytree.generate dispatched for selected Sim {target_sim_id}."
        )
        return result.accepted

    def _resolve_target_sim_id(self, connection):
        if self._client_manager is None:
            return None

        client = self._client_manager.get(connection)
        if client is None:
            return None

        active_sim = getattr(client, "active_sim", None)
        if active_sim is None:
            return None

        return getattr(active_sim, "id", None)
