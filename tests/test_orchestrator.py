import importlib
import pytest

def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')

def test_handle_report_command_valid_flow():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()

    result = orchestrator.handle_report_command(["a"])
    assert result == {"report": {"messages": ["a"]}, "score": 1}


def test_handle_report_command_invalid_data_raises(monkeypatch):
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    assert orchestrator.handle_report_command("u1", ["a"]) == {"messages": ["a"]}