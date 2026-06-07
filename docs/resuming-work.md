# Resuming Work

This document is a quick orientation point for future contributors and coding
agents returning after time away.

## Current V1 State

The repository contains the V0 project foundation and the V1
`familytree.generate` command. The command targets the invoking connection's
active Sim, delegates to the application layer, emits console and log output,
and handles missing selections safely.

The V1 application use case intentionally acknowledges the request without
generating relatives. Pie menu integration, townie connections, and automatic
new-Sim hooks are also not implemented.

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

## V1 Manual Validation Checklist

Before closing V1, confirm:

- The full automated verification workflow passes.
- The built archive loads without a Sim Origins-related exception.
- `familytree.generate` runs for the selected Sim without testing cheats.
- The console and game log contain the expected acknowledgement.
- No family members are created.
- Missing active-Sim behavior is verified where the game allows that state.
