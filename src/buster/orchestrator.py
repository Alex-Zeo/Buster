"""Core logic for coordinating report compilation and submission."""

from .compiler.report_compiler import ReportCompiler


class BusterOrchestrator:
    """Coordinates message intake and dispatches work to other agents."""

    def __init__(self) -> None:
        self.compiler = ReportCompiler()

    def handle_report_command(self, messages: list[str]) -> dict:
        """Compile a report from messages and return structured data."""
        return self.compiler.compile(messages)
