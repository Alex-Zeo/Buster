# Architecture Overview

This repository follows the canonical layout described in `AGENTS.md`.
The structure keeps orchestrator, compiler, validation and best practice
logic modular while grouping them under a single package.

```text
src/
  buster/
    __init__.py
    discord_bot.py        # entrypoint, Discord command registration
    orchestrator.py       # implements BusterOrchestrator logic
    compiler/
      __init__.py
      report_compiler.py  # fetch messages and links, build report data
    validation/
      __init__.py
      schema.py           # JSON schema definitions
      data_validation.py  # DataValidation checks
    best_practices/
      __init__.py
      scoring.py          # scoring and compliance advice
      guidelines.py       # reference best-practices documentation
```

Additional directories provide testing and documentation:

```text
tests/
  test_orchestrator.py
  test_compiler.py
  test_data_validation.py
  test_best_practices.py
docs/
  architecture.md
  usage.md
  ofac_schema.json
```
