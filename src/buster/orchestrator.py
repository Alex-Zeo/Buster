"""Core logic for coordinating report compilation and submission."""

from __future__ import annotations

import logging
import os
from typing import Any

import requests

from .compiler.report_compiler import ReportCompiler
from .validation.data_validation import validate_report


logger = logging.getLogger(__name__)


class BusterOrchestrator:
    """Coordinates message intake and dispatches work to other agents."""

    def __init__(self) -> None:
        self.compiler = ReportCompiler()

    def handle_report_command(self, messages: list[str]) -> dict:
        """Compile a report from messages and return structured data."""
        logger.info("received report command", extra={"message_count": len(messages)})
        result = self.compiler.compile(messages)
        logger.info("report command compiled", extra={"return_value": result})
        return result

    def submit_report(self, report: dict[str, Any]) -> bool:
        """Send the validated report to the configured OFAC endpoint."""
        if not validate_report(report):
            raise ValueError("invalid report")
        endpoint = os.getenv("OFAC_API_URL")
        if not endpoint:
            raise RuntimeError("Missing OFAC_API_URL")
        logger.info("submitting report", extra={"endpoint": endpoint})
        response = requests.post(endpoint, json=report, timeout=10)
        response.raise_for_status()
        logger.info("report submitted", extra={"status": response.status_code})
        return response.status_code == 200
