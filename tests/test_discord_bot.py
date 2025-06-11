import pytest

from buster.discord_bot import get_credentials


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
