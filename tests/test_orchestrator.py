import importlib


def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')
