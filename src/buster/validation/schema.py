"""JSON schema definitions for report validation."""
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

from __future__ import annotations

import json
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[3] / "docs" / "ofac_schema.json"

with SCHEMA_PATH.open() as f:
    REPORT_SCHEMA: dict = json.load(f)
