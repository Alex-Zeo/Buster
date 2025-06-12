"""Core logic for coordinating report compilation and submission."""

import logging

from .compiler.report_compiler import ReportCompiler


logger = logging.getLogger(__name__)


class BusterOrchestrator:
    """Coordinates message intake and dispatches work to other agents."""

    def __init__(self) -> None:
        self.compiler = ReportCompiler()

    def handle_report_command(self, messages: list[dict]) -> dict:
        """Compile a report from messages and return structured data."""
        logger.info("received report command", extra={"message_count": len(messages)})
        result = self.compiler.compile(messages)
        logger.info("report command compiled", extra={"return_value": result})
        return result
