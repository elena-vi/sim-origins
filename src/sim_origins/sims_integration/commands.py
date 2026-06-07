"""Sims 4 cheat-command registration and runtime composition."""

import services
import sims4.commands
import sims4.log

from sim_origins.application.generate_family_history import GenerateFamilyHistory
from sim_origins.sims_integration.familytree_command import (
    FamilyTreeGenerateCommand,
)

LOGGER = sims4.log.Logger("SimOrigins", default_owner="Sim Origins")
GENERATE_FAMILY_HISTORY = GenerateFamilyHistory()


@sims4.commands.Command(
    "familytree.generate",
    command_type=sims4.commands.CommandType.Live,
)
def familytree_generate(_connection=None):
    """Dispatch a generation request for the invoking client's active Sim."""

    command = FamilyTreeGenerateCommand(
        client_manager=services.client_manager(),
        use_case=GENERATE_FAMILY_HISTORY,
        output=sims4.commands.CheatOutput(_connection),
        logger=LOGGER,
    )
    return command.execute(connection=_connection)
