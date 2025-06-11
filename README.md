# Buster

Buster is a Discord bot that collects user messages and referenced content to
build and submit sanction violation reports to the Office of Foreign Assets
Control (OFAC). This repository contains a lightweight prototype of that service
along with documentation outlining the intended architecture.

## Design Goals

- Automate data collection from Discord conversations
- Validate user-provided links and fetch related evidence
- Compile reports in a consistent JSON format for OFAC
- Provide clear logging and audit trails

## Architecture Overview

The system is composed of several cooperating agents:

### BusterOrchestrator
Coordinates message intake, dispatches work to other agents and manages user
interactions.

### ReportCompiler
Converts messages and linked media into a structured report payload.

### DataValidation
Ensures required fields are present and correctly formatted.

### BestPractices
Applies policy guidelines, scores report completeness and suggests improvements.

The agents run in sequence when a user invokes the reporting command. Messages
are processed, validated and scored before the final report is filed with OFAC
and logged for auditing.

## Repository Layout

```
src/    - bot source code (not yet included)
tests/  - automated tests (empty for now)
docs/   - additional documentation
```

## Requirements

- Python 3.11+
- Access to the Discord API
- Internet access for OFAC submissions

Install the dependencies with:

```bash
pip install -r requirements.txt
```

See [docs/usage.md](docs/usage.md) for setup instructions and more details on running the bot.

## Environment Variables

The bot reads its configuration from environment variables:

- `DISCORD_TOKEN` – Discord bot token used for authentication.
- `DISCORD_APP_ID` – Application ID for registering slash commands.
- `BUSTER_LOG_LEVEL` – Optional logging level (defaults to `INFO`).

## Running Checks

Before submitting changes, run the linters and tests:

```bash
flake8
pytest
```

The project follows PEP8 with a 100 character line limit.

## Contribution Workflow

1. Fork the repository and create a feature branch.
2. Ensure `flake8` and `pytest` pass with no errors.
3. Submit a pull request for review.

## Security & Compliance

- Sanitize all user input.
- Store credentials securely and avoid committing secrets to the repo.
- Log report submissions for audit purposes.

## Deployment

The production bot is intended to run in a containerized environment. CI/CD is
handled through GitHub Actions. The workflow defined in
`.github/workflows/ci.yml` runs `flake8` and `pytest` on every push and pull
request.

