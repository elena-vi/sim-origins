"""Runtime wiring tests using small Sims 4 API substitutes."""

import importlib
import sys
from types import ModuleType, SimpleNamespace


def test_familytree_generate_registers_as_a_live_command(monkeypatch):
    registered_commands = {}
    live_command_type = object()

    commands_module = ModuleType("sims4.commands")
    commands_module.CommandType = SimpleNamespace(Live=live_command_type)

    def register_command(name, command_type):
        def decorator(command):
            registered_commands[name] = {
                "command": command,
                "command_type": command_type,
            }
            return command

        return decorator

    commands_module.Command = register_command
    commands_module.CheatOutput = lambda connection: lambda message: None

    log_module = ModuleType("sims4.log")
    log_module.Logger = lambda *args, **kwargs: SimpleNamespace(
        info=lambda message: None,
        warn=lambda message: None,
    )

    sims4_module = ModuleType("sims4")
    sims4_module.__path__ = []
    sims4_module.commands = commands_module
    sims4_module.log = log_module

    services_module = ModuleType("services")
    services_module.client_manager = lambda: None

    monkeypatch.setitem(sys.modules, "services", services_module)
    monkeypatch.setitem(sys.modules, "sims4", sims4_module)
    monkeypatch.setitem(sys.modules, "sims4.commands", commands_module)
    monkeypatch.setitem(sys.modules, "sims4.log", log_module)
    monkeypatch.delitem(
        sys.modules,
        "sim_origins.sims_integration.commands",
        raising=False,
    )

    importlib.import_module("sim_origins.sims_integration.commands")

    assert set(registered_commands) == {"familytree.generate"}
    assert registered_commands["familytree.generate"]["command_type"] is (
        live_command_type
    )
