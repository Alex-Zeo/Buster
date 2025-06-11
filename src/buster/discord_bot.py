"""Discord bot entry point and command registration."""

from __future__ import annotations

import logging
import os

import discord

logger = logging.getLogger(__name__)


def get_credentials() -> tuple[str, str]:
    """Return Discord token and application ID from environment."""
    token = os.getenv("DISCORD_TOKEN")
    app_id = os.getenv("DISCORD_APP_ID")
    missing = []
    if not token:
        missing.append("DISCORD_TOKEN")
    if not app_id:
        missing.append("DISCORD_APP_ID")
    if missing:
        logger.error(
            "missing environment variables",
            extra={"missing": missing},
        )
        raise RuntimeError(f"Missing credentials: {', '.join(missing)}")
    return token, app_id


class BusterBot(discord.Client):
    async def on_ready(self) -> None:  # type: ignore[override]
        logger.info("connected", extra={"user": str(self.user)})


def main() -> None:
    token, _app_id = get_credentials()
    intents = discord.Intents.default()
    client = BusterBot(intents=intents)
    try:
        client.run(token)
    except Exception:  # pragma: no cover - simple run wrapper
        logger.exception("bot run failed")


if __name__ == "__main__":
    main()
