"""Build report data from messages and linked content."""


class ReportCompiler:
    """Fetches evidence and assembles the report payload."""

    def compile(self, messages: list[str]) -> dict:
        """Return a minimal report structure from the provided messages."""
        return {"messages": messages}
