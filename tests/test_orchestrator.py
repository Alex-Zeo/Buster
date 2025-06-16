import importlib
import pytest


def test_orchestrator_import():
    module = importlib.import_module("buster.orchestrator")
    assert hasattr(module, "BusterOrchestrator")


def test_handle_report_command_valid_flow(monkeypatch):
    orchestrator = importlib.import_module("buster.orchestrator").BusterOrchestrator()
    monkeypatch.setattr("buster.orchestrator.validate_report", lambda r: True)
    result = orchestrator.handle_report_command([
        {"content": "a", "author": "u", "timestamp": "t"}
    ])
    assert result == {
        "report": {"messages": [{"author": "u", "timestamp": "t", "content": "a", "evidence": []}]},
        "score": 1,
    }


def test_submit_report_invalid_data(monkeypatch):
    orchestrator = importlib.import_module("buster.orchestrator").BusterOrchestrator()
    monkeypatch.setenv("OFAC_API_URL", "http://example.com")
    with pytest.raises(ValueError):
        orchestrator.submit_report({"invalid": True})
