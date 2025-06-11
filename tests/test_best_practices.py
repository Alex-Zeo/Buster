import importlib


def test_best_practices_import():
    module = importlib.import_module('buster.best_practices.scoring')
    assert hasattr(module, 'score_report')
