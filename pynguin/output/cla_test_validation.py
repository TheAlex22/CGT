import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right
from pymonet.maybe import Maybe
from pymonet.box import Box
from pymonet.lazy import Lazy
from pymonet.monad_try import Try

def test_validation_creation():
    """Test basic Validation creation and attributes"""
    success = Validation.success(42)
    assert success.value == 42
    assert success.errors == []
    
    fail = Validation.fail(["error1"])
    assert fail.value is None
    assert fail.errors == ["error1"]

def test_validation_equality():
    """Test Validation equality comparison"""
    assert Validation.success(42) == Validation.success(42)
    assert Validation.fail(["error"]) == Validation.fail(["error"])
    assert Validation.success(42) != Validation.success(43)
    assert Validation.fail(["error1"]) != Validation.fail(["error2"])
    assert Validation.success(42) != Validation.fail(["error"])

def test_validation_state_checks():
    """Test is_success and is_fail methods"""
    success = Validation.success(42)
    assert success.is_success() is True
    assert success.is_fail() is False

    fail = Validation.fail(["error"])
    assert fail.is_success() is False
    assert fail.is_fail() is True

def test_validation_map():
    """Test map transformation"""
    success = Validation.success(42)
    mapped = success.map(lambda x: x * 2)
    assert mapped.value == 84
    assert mapped.errors == []

def test_validation_bind():
    """Test bind transformation"""
    def success_fn(x):
        return Validation.success(x * 2)
    
    success = Validation.success(42)
    bound = success.bind(success_fn)
    assert bound.value == 84
    assert bound.errors == []

def test_validation_ap():
    """Test ap method"""
    def validation_fn(x):
        return Validation.fail(["new_error"])
    
    success = Validation.success(42)
    result = success.ap(validation_fn)
    assert result.value == 42
    assert result.errors == ["new_error"]

def test_validation_to_either():
    """Test conversion to Either"""
    success = Validation.success(42)
    either_success = success.to_either()
    assert isinstance(either_success, Right)
    assert either_success.value == 42

    fail = Validation.fail(["error"])
    either_fail = fail.to_either()
    assert isinstance(either_fail, Left)
    assert either_fail.value == ["error"]

def test_validation_to_maybe():
    """Test conversion to Maybe"""
    success = Validation.success(42)
    maybe_success = success.to_maybe()
    assert maybe_success.value == 42


def test_validation_to_box():
    """Test conversion to Box"""
    success = Validation.success(42)
    box = success.to_box()
    assert isinstance(box, Box)
    assert box.value == 42


def test_validation_str_representation():
    """Test string representation"""
    success = Validation.success(42)
    assert str(success) == "Validation.success[42]"

    fail = Validation.fail(["error"])
    assert str(fail) == "Validation.fail[None, ['error']]"