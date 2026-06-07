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

The application layer coordinates use cases. V1 introduces
`GenerateFamilyHistory`, which accepts a Sims-independent target Sim ID and
returns an explicit result. Its V1 result acknowledges the request while
confirming that no relatives were generated.

### Infrastructure

Location: `src/sim_origins/infrastructure/`

The infrastructure layer is reserved for technical implementation details such
as configuration, persistence, logging, and adapters that do not belong in the
domain model.

### Sims Integration

Location: `src/sim_origins/sims_integration/`

The Sims integration layer is the only package that imports Sims 4 runtime
APIs. The `familytree.generate` runtime command resolves the active Sim from the
invoking connection's client and delegates the Sim ID to the application use
case. Missing clients, active Sims, and Sim IDs are rejected before delegation.

`src/sim_origins_bootstrap.py` is the archive entrypoint loaded by The Sims 4.
It imports the Sims command module for registration and logs registration
failures. It contains no gameplay logic.

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

## V1 Boundary

V1 registers and dispatches `familytree.generate`. It intentionally does not
implement genealogy generation, create deceased relatives, add pie menus,
connect townies, or add automatic gameplay hooks.
