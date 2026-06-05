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
