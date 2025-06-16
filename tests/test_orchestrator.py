import importlib
import pytest


def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')


def test_handle_report_command_valid_flow():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    messages = [{"content": "a", "author": "u", "timestamp": "t"}]
    result = orchestrator.handle_report_command(messages)
    assert result == {
        "report": {
            "messages": [{"author": "u", "timestamp": "t", "content": "a", "evidence": []}]
        },
        "score": 1,
    }


def test_handle_report_command_invalid_data_raises():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    messages = [{"content": "a", "timestamp": "t"}]  # missing author
    with pytest.raises(ValueError):
        orchestrator.handle_report_command(messages)
