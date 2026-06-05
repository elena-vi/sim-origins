# Resuming Work

This document is a quick orientation point for future contributors and coding
agents returning after time away.

## Current V0 State

The repository contains the initial project architecture, Poetry configuration,
tests, coverage reporting, Ruff configuration, CI, and a `.ts4script` packaging
tool.

The project intentionally does not contain genealogy generation, cheat commands,
pie menu integration, townie connections, or automatic new-Sim hooks yet.

## Start Here

1. Read `AGENTS.md`.
2. Check the open GitHub issue being worked on.
3. Confirm the current branch and working tree state:

   ```bash
   git status --short --branch
   ```

4. Install dependencies:

   ```bash
   poetry install
   ```

5. Run the verification commands:

   ```bash
   poetry run ruff check .
   poetry run pytest
   poetry build
   poetry run python tools/build_ts4script.py
   ```

## V1 Readiness Checklist

Before beginning V1, confirm:

- V0 CI is passing.
- Manual in-game archive verification has been performed by someone with Sims 4
  installed.
- The `familytree.generate` command design keeps Sims 4 API usage inside
  `sims_integration/`.
- Any domain rules introduced for V1 have behavior tests before implementation.
