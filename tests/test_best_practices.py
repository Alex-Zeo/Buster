import importlib

from buster.best_practices.scoring import score_report


def test_best_practices_import():
    module = importlib.import_module('buster.best_practices.scoring')
    assert hasattr(module, 'score_report')


def test_score_report_counts_messages():
    messages = [
        {"content": "x", "author": "a", "timestamp": "t", "evidence": []},
        {"content": "y", "author": "b", "timestamp": "t", "evidence": []},
    ]
    assert score_report({"messages": messages}) == 2
