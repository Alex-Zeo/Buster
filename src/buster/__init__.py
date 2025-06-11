"""Buster package for automating OFAC report submissions."""

import logging
import os


def setup_logging() -> None:
    """Configure root logger with level and format."""
    level_name = os.getenv("BUSTER_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(level=level, format="%(asctime)s %(name)s [%(levelname)s] %(message)s")


setup_logging()

__all__ = [
    "BusterOrchestrator",
    "ReportCompiler",
]
