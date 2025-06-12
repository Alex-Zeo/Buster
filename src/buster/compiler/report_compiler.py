"""Build report data from messages and linked content."""

from __future__ import annotations

import re
from typing import Iterable

import httpx


class ReportCompiler:
    """Fetches evidence and assembles the report payload."""

    URL_RE = re.compile(r"https?://\S+")

    def fetch_url(self, url: str) -> str:
        """Return text content from a URL or an error message."""
        try:
            response = httpx.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except Exception as exc:  # pragma: no cover - network failures
            return f"ERROR: {exc}"  # pragma: no cover

    def compile(self, messages: Iterable[dict]) -> dict:
        """Return structured report data from message dictionaries."""
        compiled = []
        for msg in messages:
            content = msg.get("content", "")
            evidence = []
            for url in self.URL_RE.findall(content):
                evidence.append({"url": url, "content": self.fetch_url(url)})

            compiled.append(
                {
                    "author": msg.get("author"),
                    "timestamp": msg.get("timestamp"),
                    "content": content,
                    "evidence": evidence,
                }
            )

        return {"messages": compiled}
