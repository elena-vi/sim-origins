# Architecture

Sim Origins is structured around clear dependency boundaries so genealogy logic
can be developed and tested outside the Sims 4 runtime.

## Layers

### Domain

Location: `src/sim_origins/domain/`

The domain layer will hold pure business rules such as genealogy constraints,
family-history generation rules, relationship validation, and invariants. Domain
code must not import Sims 4 APIs, Sims integration modules, infrastructure
adapters, or framework-specific services.

### Application

Location: `src/sim_origins/application/`

The application layer will coordinate use cases. Future services belong here
when they orchestrate domain logic, request technical capabilities through
interfaces, and return simple results to callers.

### Infrastructure

Location: `src/sim_origins/infrastructure/`

The infrastructure layer is reserved for technical implementation details such
as configuration, persistence, logging, and adapters that do not belong in the
domain model.

### Sims Integration

Location: `src/sim_origins/sims_integration/`

The Sims integration layer is the only place where future code should import
Sims 4 runtime APIs. These modules should stay thin and delegate meaningful work
to application services.

## Dependency Direction

Dependencies should flow inward:

```text
Sims integration -> application -> domain
Infrastructure -> application/domain contracts
Domain -> standard library only unless deliberately justified
```

The domain layer must remain importable in a normal Python environment without
The Sims 4 installed. Tests enforce this architectural contract.

## Future Version Support

- V1 can add a cheat-command adapter in `sims_integration/` that calls an
  application service.
- V2 can add ancestor-generation rules in `domain/` and orchestration in
  `application/`.
- V3 can extend domain rules for optional relatives without changing Sims
  adapters.
- V4 can add pie-menu integration as another thin adapter.
- V5 can add ports for townie lookup and relationship persistence, with Sims
  implementations outside the domain layer.
- V6 can add new-Sim event integration while reusing the same application
  services.

## V0 Boundary

V0 establishes the workspace and architecture only. It intentionally does not
implement genealogy generation, cheat commands, pie menus, townie connections,
or automatic gameplay hooks.
