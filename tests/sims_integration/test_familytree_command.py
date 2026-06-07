"""Behavior tests for the familytree.generate command adapter."""

from dataclasses import dataclass

import pytest

from sim_origins.application.generate_family_history import (
    GenerateFamilyHistoryResult,
)
from sim_origins.sims_integration.familytree_command import (
    FamilyTreeGenerateCommand,
)


@dataclass
class SimStub:
    id: int


@dataclass
class ClientStub:
    active_sim: object


class ClientManagerStub:
    def __init__(self, client):
        self.client = client
        self.requested_connections = []

    def get(self, connection):
        self.requested_connections.append(connection)
        return self.client


class GenerateFamilyHistorySpy:
    def __init__(self):
        self.target_sim_ids = []

    def execute(self, target_sim_id):
        self.target_sim_ids.append(target_sim_id)
        return GenerateFamilyHistoryResult(
            accepted=True,
            generated=False,
            target_sim_id=target_sim_id,
            message="Application use case dispatched.",
        )


class OutputSpy:
    def __init__(self):
        self.messages = []

    def __call__(self, message):
        self.messages.append(message)


class LoggerSpy:
    def __init__(self):
        self.info_messages = []
        self.warning_messages = []

    def info(self, message):
        self.info_messages.append(message)

    def warn(self, message):
        self.warning_messages.append(message)


def test_command_dispatches_selected_sim_to_application_use_case():
    connection = object()
    client_manager = ClientManagerStub(ClientStub(active_sim=SimStub(id=1234)))
    use_case = GenerateFamilyHistorySpy()
    output = OutputSpy()
    logger = LoggerSpy()
    command = FamilyTreeGenerateCommand(
        client_manager=client_manager,
        use_case=use_case,
        output=output,
        logger=logger,
    )

    result = command.execute(connection)

    assert result is True
    assert client_manager.requested_connections == [connection]
    assert use_case.target_sim_ids == [1234]
    assert output.messages == ["Application use case dispatched."]
    assert logger.info_messages == [
        "familytree.generate dispatched for selected Sim 1234."
    ]
    assert logger.warning_messages == []


@pytest.mark.parametrize(
    "client_manager",
    [
        None,
        ClientManagerStub(None),
        ClientManagerStub(ClientStub(active_sim=None)),
        ClientManagerStub(ClientStub(active_sim=object())),
    ],
)
def test_command_handles_missing_or_invalid_selected_sim_without_delegating(
    client_manager,
):
    use_case = GenerateFamilyHistorySpy()
    output = OutputSpy()
    logger = LoggerSpy()
    command = FamilyTreeGenerateCommand(
        client_manager=client_manager,
        use_case=use_case,
        output=output,
        logger=logger,
    )

    result = command.execute(connection=object())

    expected_message = (
        "Sim Origins: no active Sim is selected. Select a Sim and try again."
    )
    assert result is False
    assert use_case.target_sim_ids == []
    assert output.messages == [expected_message]
    assert logger.warning_messages == [expected_message]
    assert logger.info_messages == []
