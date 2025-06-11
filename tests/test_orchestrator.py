import importlib


def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')


def test_handle_report_command_returns_messages_dict():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    assert orchestrator.handle_report_command(["a"]) == {"messages": ["a"]}
