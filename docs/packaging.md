# Packaging and Manual Game Verification

## Build the Script Archive

Run:

```bash
poetry run python tools/build_ts4script.py
```

The default output is:

```text
dist/sim-origins.ts4script
```

The archive contains Python files from `src/sim_origins/` using paths that match
the package import name, such as `sim_origins/__init__.py`.

## Install in The Sims 4

1. Build `dist/sim-origins.ts4script`.
2. Create a folder such as:

   ```text
   Documents/Electronic Arts/The Sims 4/Mods/Sim Origins/
   ```

3. Copy `dist/sim-origins.ts4script` into that folder.
4. In game options, enable custom content and script mods.
5. Restart the game after changing script mod settings.

## Manual Verification for V0

V0 intentionally does not add a cheat command, pie-menu interaction, startup
hook, or gameplay behavior. Manual verification for V0 is therefore limited to
confirming that the game accepts the script archive without a Python load error.

Suggested verification:

1. Remove any previous Sim Origins script archives from the Mods folder.
2. Install the freshly built `dist/sim-origins.ts4script`.
3. Start the game with script mods enabled.
4. Load into the main menu or a save.
5. Confirm that no new Sim Origins-related `lastException.txt` or
   `lastUIException.txt` file is produced.

A visible in-game verification command belongs in V1, when the
`familytree.generate` cheat command is introduced.

## Custom Output

The build tool accepts explicit paths:

```bash
poetry run python tools/build_ts4script.py \
  --source-root src \
  --package sim_origins \
  --output dist/sim-origins.ts4script
```
