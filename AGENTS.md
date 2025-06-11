# AGENTS.md – Buster

*Spec for OpenAI Codex & human contributors*

## 1  Overview

### Purpose
Buster is a Discord bot that collects user messages and linked content to automatically compile and submit sanction violation reports to the Office of Foreign Assets Control (OFAC).

### Design Goals
- Automate data collection from Discord conversations
- Validate user-provided links and extract relevant evidence
- Generate consistent OFAC reports and file them automatically
- Provide clear logging and audit trails

### Execution Environment
- Python 3.11 or newer
- Discord API credentials
- Internet access to submit reports

#### Buster Agent Service Goals
1. Accurately gather all reportable content from chat
2. Ensure reports meet OFAC formatting and compliance rules
3. Deliver reliable notifications when reports are filed or errors occur

## 2  Agent Taxonomy, Sub-Tasks & Dependencies

### BusterOrchestrator
Coordinates message intake, report compilation, and submission flows.
*Sub-tasks*
- Dispatch messages to the ReportCompiler
- Manage user interactions and status updates

### ReportCompiler
Converts messages and link content into structured OFAC reports.
*Sub-tasks*
- Fetch and validate all linked media
- Aggregate user details and conversation history
- Produce standardized report JSON for DataValidation

### DataValidation
Ensures all required fields are present and formatted correctly.
*Sub-tasks*
- Run schema checks on compiled report data
- Flag missing or malformed information for remediation

### BestPractices
Captures policy guidelines for high-quality submissions.
*Sub-tasks*
- Apply scoring rules to evaluate completeness
- Recommend improvements before final filing

### 2.1 Buster Report Builder & Scoring Catalogue
- **Report Compiler** – builds the report payload
- **Report Scoring** – rates report completeness
- **Best Practices** – maintains OFAC compliance tips
- **Final OFAC Score** – combined quality metric

## 3  Agent Interface & Runtime Guarantees
The agent exposes a Discord slash command interface. All actions provide deterministic responses with clear error messages. Reports are persisted for audit.

## 4 Specification & Result Objects
Report objects follow an internal JSON schema containing message text, user identifiers, evidence URLs, timestamps, and scoring metadata.

## 5 Lifecycle & Orchestration Flow
1. User issues a report command
2. BusterOrchestrator gathers conversation context
3. ReportCompiler fetches and assembles data
4. DataValidation verifies schema compliance
5. BestPractices scores the report
6. Final report is filed with OFAC and logged

## 6 Coding, Testing & Deployment Standards
- Code style: PEP8 with 100 character lines
- Use `pytest` for automated tests
- Validate code with `flake8`
- Deploy via GitHub Actions to a containerized runtime

## 7 Continuous Intelligence & Self-Improvement (Learning Loop)
### 7.1 Data Flow
All filed reports and outcomes are logged for future training.
### 7.2 OFAC Best Practices Engine
Guides report improvements from past data.
### 7.3 ML Optimiser
Suggests new scoring rules based on historical success.
### 7.4 Planner Integration
Orchestrates advanced workflows if additional evidence is needed.
### 7.5 Auto-A/B & Drift Guard
Monitors performance changes over time and rolls back when needed.
### 7.6 Outcome Metric
Primary metric is successful OFAC report acceptance rate.

## 8 Security & Compliance Guardrails
- Sanitize all user input
- Store sensitive tokens securely
- Log access and report submissions for auditing

## 9 Deployment & Architecture Dependencies
- Docker image with Python runtime
- Access to Discord API and OFAC submission endpoint
- GitHub Actions for CI/CD

## 10 Contribution Workflow
1. Fork and create feature branch
2. Ensure `flake8` and `pytest` pass
3. Submit pull request for review

## 11 Leveraging System Intelligence to Transform Any Custom Prompt into a High-Success OFAC Violation Report
### 11.1 Data Assets We Exploit
Conversation logs, external links, and previous report outcomes.
### 11.2 Tactic Retrieval & Ranking Workflow
Retrieve evidence, rank by relevance, and compile.
### 11.3 End-to-End Prompt-to-Report Pipeline
From user command to final OFAC submission with scoring feedback.
### 11.4 Iterative Optimisation Loop (per request)
Refine reporting approach using scoring metrics and user feedback.
### 11.5 API Entry Points & Integration Hooks
Discord commands and HTTP endpoints for internal tools.
### 11.6 Security & Ethical Safeguards
Prevent abuse by enforcing content validation and access controls.
### 11.7 Outcome Guarantee
Aim for consistent, properly formatted submissions accepted by OFAC.

## 12 Repository Organization & Governance
### 12.1 Canonical Directory Layout
- `src/` – bot source code
- `tests/` – automated tests
- `docs/` – documentation
### 12.2 Logging & Observability Standards
Use structured logging with log levels for troubleshooting.
### 12.3 Separation of Concerns Rules
Keep orchestrator, compiler, validation, and best-practice logic modular.
### 12.5 File & Folder Hygiene
No large binaries in repo; use Git LFS if needed.
### 12.6 Governance Workflow
PR reviews required for all changes.
### 12.7 Automated Enforcement
CI pipeline runs `flake8` and `pytest` on each commit.

## 13 Detailed System Architecture

Below is the recommended file and module layout for a full Buster deployment. Each component maps
directly to one of the agents or support utilities described above.

```
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
tests/
  test_orchestrator.py
  test_compiler.py
  test_data_validation.py
  test_best_practices.py
docs/
  architecture.md         # high level diagrams and design notes
  usage.md                # instructions for running the bot
  ofac_schema.json        # canonical OFAC report schema
AGENTS.md
README.md
requirements.txt
```

This layout keeps orchestrator, compiler, validation logic and best-practice rules in separate
modules while grouping them under a single package for clarity. Tests live alongside the code they
exercise, and all documentation resides in the `docs/` directory.

# Buster Agent Service Documentation
