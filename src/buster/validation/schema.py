"""JSON schema definitions for report validation."""

from __future__ import annotations

REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "messages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "author": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "content": {"type": "string"},
                    "evidence": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "url": {"type": "string"},
                                "content": {"type": "string"},
                            },
                            "required": ["url", "content"],
                        },
                    },
                },
                "required": ["author", "timestamp", "content", "evidence"],
            },
        },
    },
    "required": ["messages"],
}
