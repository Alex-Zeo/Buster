"""Discord bot entry point and command registration."""

from __future__ import annotations

import logging
import os

import discord
from discord.ext import commands

from .orchestrator import BusterOrchestrator

logging.basicConfig(
    level=getattr(logging, os.getenv("BUSTER_LOG_LEVEL", "INFO").upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(message)s",
)

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


class BusterBot(commands.Bot):
    def __init__(self, orchestrator: BusterOrchestrator, *, app_id: str, **kwargs) -> None:
        intents = kwargs.pop("intents", discord.Intents.default())
        super().__init__(command_prefix="!", intents=intents, application_id=app_id)
        self.orchestrator = orchestrator

    async def setup_hook(self) -> None:  # type: ignore[override]
        @self.tree.command(name="report", description="Compile an OFAC report")
        async def report(interaction: discord.Interaction) -> None:
            messages: list[str] = []

            async for msg in interaction.channel.history(limit=20):
                messages.append(msg.content)

            result = self.orchestrator.handle_report_command(messages)
            try:
                self.orchestrator.submit_report(result)
                await interaction.response.send_message(str(result))
            except Exception as exc:  # pragma: no cover - errors returned to user
                await interaction.response.send_message(
                    f"submission failed: {exc}", ephemeral=True
                )

    async def on_ready(self) -> None:  # type: ignore[override]
        logger.info("connected", extra={"user": str(self.user)})


def main() -> None:
    token, app_id = get_credentials()
    intents = discord.Intents.default()
    orchestrator = BusterOrchestrator()
    client = BusterBot(orchestrator, intents=intents, app_id=app_id)
    try:
        client.run(token)
    except Exception:  # pragma: no cover - simple run wrapper
        logger.exception("bot run failed")


if __name__ == "__main__":
    main()
