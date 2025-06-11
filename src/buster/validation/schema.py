"""JSON schema definitions for report validation."""

REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "messages": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["messages"],
}
