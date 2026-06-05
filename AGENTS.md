# Sim Origins - Agent Instructions

## Project Overview

Sim Origins is a Sims 4 script mod that generates believable family histories for Sims.

Development is tracked through GitHub issues:

- V0: Establish Modding Workspace and Project Architecture
- V1: Add familytree.generate Cheat Command
- V2: Generate Deceased Parents and Grandparents
- V3: Generate Optional Extended Family
- V4: Add Generate Family History Pie Menu Interaction
- V5: Connect Generated Sims to Existing Townies
- V6: Automatically Generate Family History for New Sims

Always align work with the relevant issue.

---

## Core Principles

### Clean Code

- Prefer readability over cleverness.
- Prefer explicit naming.
- Keep functions small and focused.
- Avoid deep nesting.
- Avoid unnecessary complexity.
- Leave the codebase cleaner than you found it.

### SOLID

Follow all SOLID principles.

Particularly:

- Domain logic must not depend directly on Sims 4 APIs.
- Use dependency inversion where appropriate.
- Prefer composition over inheritance.
- Keep responsibilities narrow and well-defined.

### DRY

Avoid duplication.

However:

- Do not introduce abstractions prematurely.
- A small amount of duplication is preferable to the wrong abstraction.

---

## Architecture Rules

The project should be organized around clear boundaries.

### Domain

Contains pure business logic.

Examples:

- Family generation rules
- Genealogy calculations
- Relationship validation

Domain code should:

- Be framework-independent
- Be Sims-independent where possible
- Be highly testable

### Application Layer

Coordinates use cases.

Examples:

- Generate family history
- Create ancestors
- Connect relatives

Application services should orchestrate domain logic.

### Infrastructure

Contains technical implementation details.

Examples:

- Persistence
- Configuration
- Logging

### Sims Integration

Contains Sims 4 specific code.

Examples:

- Cheat commands
- Pie menu interactions
- Sims API adapters

Keep Sims-specific code thin.

The majority of logic should live outside Sims integration modules.

---

## Testing Philosophy

### General Rules

Follow TDD.

Write tests for behavior rather than implementation.

Prefer high-value tests.

Avoid tests that exist only to increase coverage.

### Good Tests

Focus on:

- Business rules
- Edge cases
- Failure paths
- Regression protection
- Domain invariants

### Avoid

Avoid testing:

- Simple getters/setters
- Constants
- Framework boilerplate
- Internal implementation details

### Coverage

Coverage is a safety metric, not the goal.

Target:

- Excellent coverage of domain logic
- Strong coverage of application services
- Minimal mocking where possible

Do not add low-value tests solely to satisfy coverage metrics.

If achieving 100% coverage requires meaningless tests, explain the tradeoff.

---

## GitHub Workflow

Before starting work:

1. Identify the issue being worked on.
2. Limit changes to the scope of that issue.
3. Avoid implementing future issues unless explicitly requested.

When work is complete:

- Update documentation if necessary.
- Verify tests pass.
- Summarize changes clearly.

---

## Definition of Done

Work is complete only when:

- Relevant tests exist.
- Tests pass.
- Code follows SOLID principles.
- Code follows clean code principles.
- Documentation is updated where appropriate.
- No obvious duplication exists.
- Changes remain within the scope of the active issue.

---

## Agent Expectations

When making decisions:

1. Choose maintainability over speed.
2. Choose simplicity over cleverness.
3. Choose testability over convenience.
4. Choose explicitness over magic.
5. Prefer architecture that will support future versions V1–V6.

If uncertain, stop explain tradeoffs and ask for input!
