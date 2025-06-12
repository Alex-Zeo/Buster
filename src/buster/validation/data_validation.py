"""Utilities for checking report data against the schema."""

from jsonschema import ValidationError, validate

from .schema import REPORT_SCHEMA


def validate_report(data: dict) -> bool:
    """Return True when the report dictionary conforms to the OFAC schema."""
    try:
        validate(instance=data, schema=REPORT_SCHEMA)
    except ValidationError:
        return False
    return True
