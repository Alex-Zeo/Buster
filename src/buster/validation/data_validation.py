"""Utilities for checking report data against the schema."""

from .schema import REPORT_SCHEMA


def validate_report(data: dict) -> bool:
    """Placeholder validation that ensures required fields exist."""
    for field in REPORT_SCHEMA["required"]:
        if field not in data:
            return False
    return True
