import importlib
import pytest


def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')


def test_handle_report_command_valid_flow():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    result = orchestrator.handle_report_command(["a"])
    assert result['report']['messages'][0]['content'] == 'a'
    assert result['score'] == 1


def test_handle_report_command_invalid_data_raises():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    with pytest.raises(ValueError):
        orchestrator.handle_report_command([1])
