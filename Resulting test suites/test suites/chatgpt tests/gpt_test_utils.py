import pytest
import os
from unittest.mock import patch
from utils import str_to_bool, load_module_from_file_location, LoadFileException, PyFileError


# Test suite for str_to_bool
@pytest.mark.parametrize(
    "input_val, expected_output",
    [
        ("y", True),
        ("yes", True),
        ("yep", True),
        ("yup", True),
        ("t", True),
        ("true", True),
        ("on", True),
        ("enable", True),
        ("enabled", True),
        ("1", True),
        ("n", False),
        ("no", False),
        ("f", False),
        ("false", False),
        ("off", False),
        ("disable", False),
        ("disabled", False),
        ("0", False),
    ],
)
def test_str_to_bool(input_val, expected_output):
    assert str_to_bool(input_val) == expected_output


def test_str_to_bool_invalid():
    # Test invalid values that should raise ValueError
    invalid_values = ["maybe", "unknown", "truefalse", "onoff"]
    for val in invalid_values:
        with pytest.raises(ValueError):
            str_to_bool(val)


# Test suite for load_module_from_file_location



@patch.dict(os.environ, {"some_env_var": "invalid_path"})
def test_load_module_from_file_location_with_missing_env_var():
    # Test if LoadFileException is raised when an environment variable is not defined
    location = "/some/path/${some_env_var}/module.py"
    with pytest.raises(LoadFileException):
        load_module_from_file_location(location)


@patch("builtins.open", side_effect=OSError("File not found"))
def test_load_module_from_file_location_with_os_error(mock_open):
    # Test if OSError is raised when the file cannot be loaded
    location = "/some/invalid/path/config.py"
    with pytest.raises(OSError):
        load_module_from_file_location(location)


def test_load_module_from_file_location_invalid_format():
    # Test invalid module location format
    location = "/invalid/path/to/module.txt"
    with pytest.raises(OSError):
        load_module_from_file_location(location)

