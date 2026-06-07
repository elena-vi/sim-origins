"""Load Sim Origins runtime integrations when The Sims 4 imports the archive."""

try:
    import sim_origins.sims_integration.commands  # noqa: F401
except Exception as exc:
    import sims4.log

    logger = sims4.log.Logger("SimOrigins", default_owner="Sim Origins")
    logger.exception("Failed to register Sim Origins commands.", exc=exc)
