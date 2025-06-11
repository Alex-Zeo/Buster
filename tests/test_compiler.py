import importlib


def test_compiler_import():
    module = importlib.import_module('buster.compiler.report_compiler')
    assert hasattr(module, 'ReportCompiler')
