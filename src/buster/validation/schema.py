"""JSON schema definitions for report validation."""

from __future__ import annotations

import json
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[3] / "docs" / "ofac_schema.json"

with SCHEMA_PATH.open() as f:
    REPORT_SCHEMA: dict = json.load(f)
