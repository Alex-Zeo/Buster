import asyncio
import pytest
import discord
from unittest import mock

from buster.discord_bot import BusterBot, get_credentials
from buster.orchestrator import BusterOrchestrator


def test_get_credentials_missing_env_raises(monkeypatch):
    monkeypatch.delenv("DISCORD_TOKEN", raising=False)
    monkeypatch.delenv("DISCORD_APP_ID", raising=False)
    with pytest.raises(RuntimeError):
        get_credentials()


def test_get_credentials_returns_tuple(monkeypatch):
    monkeypatch.setenv("DISCORD_TOKEN", "tok")
    monkeypatch.setenv("DISCORD_APP_ID", "appid")
    token, app_id = get_credentials()
    assert (token, app_id) == ("tok", "appid")
    assert isinstance(token, str) and isinstance(app_id, str)


def test_report_command_invokes_orchestrator(monkeypatch):
    orchestrator = mock.MagicMock()
    orchestrator.handle_report_command.return_value = {"messages": ["a", "b"]}
    orchestrator.submit_report.return_value = True
    bot = BusterBot(orchestrator, intents=discord.Intents.none(), app_id="1")
    asyncio.run(bot.setup_hook())
    cmd = bot.tree.get_command("report")

    async def gen():
        class Msg:
            def __init__(self, content: str) -> None:
                self.content = content

        for text in ["a", "b"]:
            yield Msg(text)

    interaction = mock.MagicMock()
    interaction.channel.history = lambda limit=20: gen()
    interaction.response.send_message = mock.AsyncMock()

    asyncio.run(cmd.callback(interaction))
    orchestrator.handle_report_command.assert_called_with(["a", "b"])
    orchestrator.submit_report.assert_called_with({"messages": ["a", "b"]})
    interaction.response.send_message.assert_called()


def test_submit_report_posts(monkeypatch):
    orchestrator = BusterOrchestrator()
    monkeypatch.setenv("OFAC_API_URL", "http://example.com")
    post_mock = mock.MagicMock()
    response = mock.MagicMock(status_code=200)
    response.raise_for_status = mock.MagicMock()
    post_mock.return_value = response
    monkeypatch.setattr("buster.orchestrator.requests.post", post_mock)
    assert orchestrator.submit_report({"messages": []}) is True
    post_mock.assert_called_with("http://example.com", json={"messages": []}, timeout=10)
