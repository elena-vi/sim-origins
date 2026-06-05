# Sim Origins

Sim Origins is a Sims 4 script mod project that will generate believable family
histories for Sims. The current repository state is focused on V0: establishing
the modding workspace, project architecture, packaging workflow, and contributor
documentation.

No genealogy generation or game-specific behavior is implemented in V0.

## Development Quick Start

Prerequisites:

- Python 3.7 target compatibility for Sims 4 runtime code.
- Poetry for dependency management.

Install dependencies:

```bash
poetry install
```

Run the default local workflow:

```bash
make
```

This runs Ruff fixes, tests with coverage, the Python package build, and the
Sims 4 script archive build.

Common Make targets:

```bash
make fix    # Apply Ruff lint fixes and formatting
make test   # Run pytest with configured coverage reporting
make build  # Build the Python package and .ts4script archive
make check  # Run Ruff checks without modifying files
```

Run linting and formatting checks:

```bash
poetry run ruff check .
poetry run ruff format --check .
```

Run tests with coverage:

```bash
poetry run pytest
```

Build the Python package:

```bash
poetry build
```

Build the Sims 4 script archive:

```bash
poetry run python tools/build_ts4script.py
```

The script archive is written to `dist/sim-origins.ts4script`.

## Install the Mod

1. Build the Sims 4 script archive:

   ```bash
   make build
   ```

2. Create a Sims 4 Mods subfolder for the project:

   ```text
   Documents/Electronic Arts/The Sims 4/Mods/Sim Origins/
   ```

3. Copy `dist/sim-origins.ts4script` into that folder.
4. Open The Sims 4 and enable custom content and script mods in game options.
5. Restart the game after changing script mod settings.

## Manual Sims 4 Archive Verification

V0 does not add a cheat command, pie-menu interaction, startup hook, or gameplay
behavior. Manual verification is limited to confirming that The Sims 4 accepts
the archive without a Python load error.

Suggested V0 verification:

1. Remove any previous Sim Origins `.ts4script` files from the Mods folder.
2. Install the freshly built `dist/sim-origins.ts4script`.
3. Start The Sims 4 with script mods enabled.
4. Load into the main menu or a save.
5. Confirm that no new Sim Origins-related `lastException.txt` or
   `lastUIException.txt` file is produced.

A visible in-game verification command belongs in V1, when the
`familytree.generate` cheat command is introduced. See
[Packaging and Manual Game Verification](docs/packaging.md) for the fuller
workflow and custom build options.

## Project Layout

- `.github/workflows/` contains CI for linting, tests, coverage, and builds.
- `src/sim_origins/domain/` is reserved for pure Sims-independent business logic.
- `src/sim_origins/application/` is reserved for use-case orchestration.
- `src/sim_origins/infrastructure/` is reserved for technical adapters.
- `src/sim_origins/sims_integration/` is reserved for thin Sims 4 API adapters.
- `tests/` contains behavior and architecture tests.
- `tools/` contains repository tooling, including `.ts4script` packaging.
- `docs/` contains architecture, development, packaging, and resume notes.

## Documentation

- [Architecture](docs/architecture.md)
- [Development Workflow](docs/development.md)
- [Packaging and Manual Game Verification](docs/packaging.md)
- [Resuming Work](docs/resuming-work.md)
