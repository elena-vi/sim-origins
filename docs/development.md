# Development Workflow

## Scope

Work is tracked through GitHub issues. V0 is issue #1: "Establish Modding
Workspace and Project Architecture." Do not implement V1-V6 behavior while
working on V0.

## Environment

The project uses Poetry and targets Python 3.7 compatibility because Sims 4
script mods run on a Python 3.7 runtime. Development can happen on a newer
Python version, but source code must remain compatible with Python 3.7.

Install dependencies:

```bash
poetry install
```

## Linting and Formatting

Ruff is the only configured linter and formatter tool for V0.

```bash
poetry run ruff check .
poetry run ruff format --check .
```

## Tests and Coverage

Run the test suite:

```bash
poetry run pytest
```

Pytest is configured to emit terminal coverage and `coverage.xml`. Coverage is
a safety signal, not the goal. Prefer valuable behavior, boundary, failure-path,
and regression tests over coverage-chasing tests.

## Builds

Build the Python package:

```bash
poetry build
```

Build the Sims 4 script package:

```bash
poetry run python tools/build_ts4script.py
```

## Before Opening a PR

Run:

```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run pytest
poetry build
poetry run python tools/build_ts4script.py
```

Keep each PR scoped to the active issue.
