import pytest
from app.core.parser import parse_logs


def test_detects_info_level():
    result = parse_logs("2026-01-05 10:32:10 INFO User logged in")
    assert result[0]["level"] == "INFO"


def test_detects_error_level():
    result = parse_logs("2026-01-05 10:32:10 ERROR Database failed")
    assert result[0]["level"] == "ERROR"


def test_detects_warning_level():
    result = parse_logs("2026-01-05 10:32:10 WARNING Disk space low")
    assert result[0]["level"] == "WARNING"


def test_removes_timestamp():
    result = parse_logs("2026-01-05 10:32:10 INFO User logged in")
    assert result[0]["message"] == "User logged in"


def test_unknown_level_for_unrecognized_lines():
    result = parse_logs("something weird happened")
    assert result[0]["level"] == "UNKNOWN"


def test_ignores_empty_lines():
    result = parse_logs("INFO User logged in\n\nERROR Something broke")
    assert len(result) == 2


def test_raw_preserves_original_line():
    line = "2026-01-05 10:32:10 INFO User logged in"
    result = parse_logs(line)
    assert result[0]["raw"] == line
