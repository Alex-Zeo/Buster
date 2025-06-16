import importlib


def _get_validate():
    return importlib.import_module("buster.validation.data_validation").validate_report


def test_data_validation_import():
    module = importlib.import_module("buster.validation.data_validation")
    assert hasattr(module, "validate_report")


def test_validate_report_returns_true_for_valid_data():
    validate_report = importlib.import_module(
        "buster.validation.data_validation"
    ).validate_report
    data = {
        "reporter_id": "u",
        "messages": ["hi"],
        "evidence_urls": ["http://example.com"],
        "timestamp": "2024-01-01T00:00:00Z",
        "scores": {},
        "cover_letter": "",
        "executive_summary": "",
        "reporting_entity_information": "",
        "apparent_violations": "",
        "root_cause_and_risk_assessment": "",
        "internal_investigation_methodology": "",
        "compliance_program": "",
        "corrective_and_remedial_actions": "",
        "cooperation_and_mitigating_factors": "",
        "certification_and_attestation": "",
        "index_of_exhibits": "",
        "exhibits": "",
    }
    assert validate_report(data) is True


def test_validate_report_returns_false_for_wrong_type():
    validate_report = _get_validate()
    assert validate_report({"messages": "m"}) is False


def test_validate_report_returns_false_for_missing_field():
    validate_report = _get_validate()
    assert validate_report({"other": "x"}) is False
