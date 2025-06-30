import os
import pytest
from pathlib import Path
from sanic.utils import str_to_bool, load_module_from_file_location
from sanic.exceptions import LoadFileException, PyFileError
# Tests for str_to_bool function
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("y", True),
        ("yes", True),
        ("YES", True),
        ("yep", True),
        ("yup", True),
        ("t", True),
        ("true", True),
        ("TRUE", True),
        ("on", True),
        ("enable", True),
        ("enabled", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("NO", False),
        ("f", False),
        ("false", False),
        ("FALSE", False),
        ("off", False),
        ("disable", False),
        ("disabled", False),
        ("0", False),
    ],
)
def test_str_to_bool_valid_inputs(test_input, expected):
    assert str_to_bool(test_input) == expected
def test_str_to_bool_invalid_input():
    with pytest.raises(ValueError):
        str_to_bool("invalid")
def test_str_to_bool_empty_string():
    with pytest.raises(ValueError):
        str_to_bool("")
# Tests for load_module_from_file_location function
def test_load_module_with_env_vars(tmp_path, monkeypatch):
    # Set up environment variable
    monkeypatch.setenv('TEST_DIR', str(tmp_path))
    # Create a test file
    test_file = tmp_path / "test_config.py"
    test_file.write_text("CONFIG_VALUE = 42")
    # Test loading with environment variable
    module = load_module_from_file_location("${TEST_DIR}/test_config.py")
    assert module.CONFIG_VALUE == 42
def test_load_module_missing_env_var():
    with pytest.raises(LoadFileException):
        load_module_from_file_location("${NONEXISTENT_VAR}/config.py")
def test_load_module_from_path_object(tmp_path):
    # Test loading module using Path object
    test_file = tmp_path / "path_test.py"
    test_file.write_text("PATH_TEST = True")
    module = load_module_from_file_location(test_file)
    assert module.PATH_TEST is True