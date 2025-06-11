import importlib

from buster.best_practices.scoring import score_report


def test_best_practices_import():
    module = importlib.import_module('buster.best_practices.scoring')
    assert hasattr(module, 'score_report')


def test_score_report_counts_messages():
    assert score_report({"messages": ["x", "y"]}) == 2
