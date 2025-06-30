import pytest
from unittest.mock import MagicMock
from sty.primitive import Register
from lib import mute, unmute  # Replace `your_module` with the actual module name


# Create a mock Register class for testing purposes
class MockRegister(Register):
    def mute(self):
        pass

    def unmute(self):
        pass


def test_mute_with_valid_objects():
    # Create mock Register objects
    mock_obj1 = MockRegister()
    mock_obj2 = MockRegister()

    # Mock the mute method
    mock_obj1.mute = MagicMock()
    mock_obj2.mute = MagicMock()

    # Call mute() on valid objects
    mute(mock_obj1, mock_obj2)

    # Assert that mute was called on both objects
    mock_obj1.mute.assert_called_once()
    mock_obj2.mute.assert_called_once()


def test_mute_with_invalid_object():
    # Create a mock Register object and a non-Register object
    mock_obj1 = MockRegister()
    invalid_obj = object()  # Not an instance of Register

    # Test that ValueError is raised when an invalid object is passed
    with pytest.raises(ValueError):
        mute(mock_obj1, invalid_obj)


def test_unmute_with_valid_objects():
    # Create mock Register objects
    mock_obj1 = MockRegister()
    mock_obj2 = MockRegister()

    # Mock the unmute method
    mock_obj1.unmute = MagicMock()
    mock_obj2.unmute = MagicMock()

    # Call unmute() on valid objects
    unmute(mock_obj1, mock_obj2)

    # Assert that unmute was called on both objects
    mock_obj1.unmute.assert_called_once()
    mock_obj2.unmute.assert_called_once()


def test_unmute_with_invalid_object():
    # Create a mock Register object and a non-Register object
    mock_obj1 = MockRegister()
    invalid_obj = object()  # Not an instance of Register

    # Test that ValueError is raised when an invalid object is passed
    with pytest.raises(ValueError):
        unmute(mock_obj1, invalid_obj)