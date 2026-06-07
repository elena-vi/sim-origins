# Sim Origins

Sim Origins is a Sims 4 script mod project that will generate believable family
histories for Sims. V1 adds the `familytree.generate` cheat command as the
entry point for future family generation.

V1 does not create parents, grandparents, or any other relatives.

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

## Use the Cheat Command

1. Load a household and select the Sim to target.
2. Open the cheat console.
3. Run:

   ```text
   familytree.generate
   ```

The command does not require `testingcheats true`. It resolves the active Sim
from the client connection that invoked the command, logs the result, and
prints an acknowledgement in the cheat console. V1 intentionally stops there
without generating family members.

If no valid active Sim can be resolved, the command prints a safe error message
and does not call the application use case. See
[Packaging and Manual Game Verification](docs/packaging.md) for the full manual
verification workflow.

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
