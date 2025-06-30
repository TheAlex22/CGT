import pytest
from validation import Validation  # Replace with the actual import path if needed

# Test initialization of Validation class
def test_validation_initialization():
    validation = Validation.success(5)
    assert validation.value == 5
    assert validation.errors == []

    validation = Validation.fail(["error1", "error2"])
    assert validation.value is None
    assert validation.errors == ["error1", "error2"]

# Test success and fail methods
def test_success_fail_methods():
    success = Validation.success(10)
    assert success.is_success() is True
    assert success.is_fail() is False

    fail = Validation.fail(["invalid_value"])
    assert fail.is_success() is False
    assert fail.is_fail() is True

# Test equality comparison (__eq__)
def test_validation_equality():
    success1 = Validation.success(5)
    success2 = Validation.success(5)
    fail1 = Validation.fail(["error1"])
    fail2 = Validation.fail(["error1"])

    assert success1 == success2
    assert fail1 == fail2
    assert success1 != fail1

# Test the str method (__str__)
def test_str_method():
    success = Validation.success(10)
    fail = Validation.fail(["error1", "error2"])

    assert str(success) == "Validation.success[10]"
    assert str(fail) == "Validation.fail[None, ['error1', 'error2']]"

# Test to_either method
def test_to_either_method():
    success = Validation.success(5)
    fail = Validation.fail(["error"])

    either_success = success.to_either()
    either_fail = fail.to_either()

    assert either_success.is_right() is True
    assert either_fail.is_left() is True

# Test to_lazy method
def test_to_lazy_method():
    success = Validation.success(5)
    lazy = success.to_lazy()

    assert lazy.get() == 5

