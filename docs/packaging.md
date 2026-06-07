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
the package import name, such as `sim_origins/__init__.py`. It also contains the
top-level `sim_origins_bootstrap.py` module, which imports the Sims integration
command module so The Sims 4 registers `familytree.generate`.

## Install in The Sims 4

1. Build `dist/sim-origins.ts4script`.
2. Create a folder such as:

   ```text
   Documents/Electronic Arts/The Sims 4/Mods/Sim Origins/
   ```

3. Copy `dist/sim-origins.ts4script` into that folder.
4. In game options, enable custom content and script mods.
5. Restart the game after changing script mod settings.

## Manual Verification for V1

Suggested verification:

1. Remove any previous Sim Origins script archives from the Mods folder.
2. Install the freshly built `dist/sim-origins.ts4script`.
3. Start the game with script mods enabled.
4. Load a household and select a Sim.
5. Open the cheat console and run:

   ```text
   familytree.generate
   ```

6. Confirm the console reports that the command was dispatched for the selected
   Sim and that family generation is not implemented in V1.
7. Confirm that no parents, grandparents, or other relatives were created.
8. Where the game permits invoking the command without an active Sim, confirm
   the console reports that no active Sim is selected and the game continues
   normally.
9. Confirm that no new Sim Origins-related `lastException.txt` or
   `lastUIException.txt` file is produced.

The command is registered as a live command and does not require
`testingcheats true`.

## Custom Output

The build tool accepts explicit paths:

```bash
poetry run python tools/build_ts4script.py \
  --source-root src \
  --package sim_origins \
  --output dist/sim-origins.ts4script
```
