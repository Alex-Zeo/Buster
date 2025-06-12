"""Buster package for automating OFAC report submissions."""

from __future__ import annotations

import json
import logging
import os
from typing import Any


DEFAULT_ATTRS = set(logging.LogRecord(None, 0, "", 0, "", (), None).__dict__).union(
    {"message", "asctime"}
)


class JsonFormatter(logging.Formatter):
    """Format log records as JSON strings."""

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401 - short method
        base: dict[str, Any] = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        for key, value in record.__dict__.items():
            if key not in DEFAULT_ATTRS:
                base[key] = value
        return json.dumps(base)


def setup_logging() -> None:
    """Configure root logger with JSON output."""
    level_name = os.getenv("BUSTER_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(level)


setup_logging()

__all__ = [
    "BusterOrchestrator",
    "ReportCompiler",
]
