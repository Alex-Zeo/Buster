import importlib


def test_orchestrator_import():
    module = importlib.import_module('buster.orchestrator')
    assert hasattr(module, 'BusterOrchestrator')


def test_handle_report_command_returns_messages_dict():
    orchestrator = importlib.import_module('buster.orchestrator').BusterOrchestrator()
    messages = [{
        'content': 'a',
        'author': 'user',
        'timestamp': 't',
    }]
    result = orchestrator.handle_report_command(messages)
    assert result['messages'][0]['content'] == 'a'
