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

    def bad_compile(_: list[str]) -> dict:
        return {"bad": True}

    monkeypatch.setattr(orchestrator.compiler, "compile", bad_compile)
    with pytest.raises(ValueError):
        orchestrator.handle_report_command(["bad"])