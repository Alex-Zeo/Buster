import importlib


def test_compiler_import():
    module = importlib.import_module('buster.compiler.report_compiler')
    assert hasattr(module, 'ReportCompiler')


def test_compile_returns_messages_dict():
    compiler = importlib.import_module(
        'buster.compiler.report_compiler'
    ).ReportCompiler()
    assert compiler.compile(["msg"]) == {"messages": ["msg"]}
