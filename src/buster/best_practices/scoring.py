"""Apply scoring rules to evaluate report completeness."""


def score_report(data: dict) -> int:
    """Return a placeholder score for the report data."""
    return len(data.get("messages", []))
