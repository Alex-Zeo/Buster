# Buster Agent

Buster is a Discord agent that collects user messages and referenced content to
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
src/    - bot source code
tests/  - automated tests
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
The high-level design is documented in [docs/architecture.md](docs/architecture.md),
and the placeholder OFAC schema can be found at [docs/ofac_schema.json](docs/ofac_schema.json).

## Environment Variables

The bot reads its configuration from environment variables:

- `DISCORD_TOKEN` – Discord bot token used for authentication.
- `DISCORD_APP_ID` – Application ID for registering slash commands.
- `BUSTER_LOG_LEVEL` – Optional logging level for JSON logs (defaults to `INFO`).
- `OFAC_API_URL` – HTTP endpoint used to submit validated reports.

## Discord Commands

The bot exposes multiple slash commands:
- `/active` – print selected active report
- `/rename` – rename the selected active report
- `/list` – list all active reports
- `/switch` – select a different active OFAC report
- `/find` – OpenAI deep research query used to gather evidence and add data to the OFAC report.
- `/add` – user prompt or browse links to gather evidence for the
- `/print` – curates and stores the content from the latest messages in selected report including deep research results, user messages, Buster messages, user links and their related content to compile the OFAC report.
- `/adjust` – tweak, rewrite, or reword a section of the OFAC report
- `/optimize` – rewrites the OFAC report prioritizing the best practices guidelines with all the relevant available data (messages, deep research, links, context) 
- `/submitreport` – collects the latest messages in selected report including the deep research results and submits the most relevant 
- `/stats` – count of number of reports submitted, count of pieces of evidence, count of individuals or entities

After report submission dont make specifics of 


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


## Container Usage

Build the Docker image:

```bash
docker build -t buster .
```

Run the bot from the image (set your credentials as environment variables):

```bash
docker run --rm -e DISCORD_TOKEN=TOKEN -e DISCORD_APP_ID=APPID buster
```

To execute the test suite inside the container use:

```bash
docker run --rm --entrypoint pytest buster
```
