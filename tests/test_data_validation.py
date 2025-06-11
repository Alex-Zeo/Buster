import importlib


def test_data_validation_import():
    module = importlib.import_module('buster.validation.data_validation')
    assert hasattr(module, 'validate_report')
