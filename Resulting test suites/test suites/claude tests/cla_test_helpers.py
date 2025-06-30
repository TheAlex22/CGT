import sys
from unittest.mock import MagicMock, patch
import pytest
import json
from helpers import (
    STATUS_CODES,
    json_dumps,
    has_message_body,
    is_entity_header,
    is_hop_by_hop_header,
    import_string,
    is_atty,
    Default,
    _default,
)
def test_status_codes():
    """Test STATUS_CODES dictionary contains correct values"""
    assert STATUS_CODES[200] == b"OK"
    assert STATUS_CODES[404] == b"Not Found"
    assert STATUS_CODES[500] == b"Internal Server Error"
    assert isinstance(STATUS_CODES[200], bytes)
def test_json_dumps():
    """Test json_dumps functionality"""
    data = {"key": "value", "number": 42}
    result = json_dumps(data)
    # Verify the result is valid JSON and maintains expected format
    parsed = json.loads(result)
    assert parsed == data
    assert '"key":"value"' in result  # Check compact formatting
def test_has_message_body():
    """Test has_message_body function"""
    assert has_message_body(200) is True
    assert has_message_body(204) is False
    assert has_message_body(304) is False
    assert has_message_body(100) is False
    assert has_message_body(199) is False
    assert has_message_body(301) is True
def test_is_entity_header():
    """Test is_entity_header function"""
    assert is_entity_header("content-type") is True
    assert is_entity_header("Content-Type") is True
    assert is_entity_header("x-custom-header") is False
    assert is_entity_header("") is False
def test_is_hop_by_hop_header():
    """Test is_hop_by_hop_header function"""
    assert is_hop_by_hop_header("connection") is True
    assert is_hop_by_hop_header("Connection") is True
    assert is_hop_by_hop_header("content-type") is False
    assert is_hop_by_hop_header("") is False
class TestModule:
    """Test module for import_string testing"""
    pass
def test_import_string():
    """Test import_string function"""
    # Test importing a module
    result = import_string("json.encoder")
    assert result.__name__ == "json.encoder"
    # Test importing a class
    result = import_string("unittest.mock.MagicMock")
    assert isinstance(result, MagicMock)
def test_import_string_invalid():
    """Test import_string with invalid inputs"""
    with pytest.raises(ImportError):
        import_string("nonexistent.module")
    with pytest.raises(AttributeError):
        import_string("json.nonexistent")
def test_default_class():
    """Test Default class"""
    default = Default()
    assert str(default) == "<Default>"
    assert repr(default) == "<Default>"
    # Test singleton _default instance
    assert isinstance(_default, Default)
    assert str(_default) == "<Default>"
    
import pytest
import sys
from helpers import (
    has_message_body, 
    is_entity_header, 
    is_hop_by_hop_header,
    import_string,
    is_atty,
    Default,
)

# Test cases for has_message_body
def test_has_message_body():
    assert has_message_body(200) == True  # 200 is not 1XX, 204, or 304, so has a message body
    assert has_message_body(204) == False  # 204 has no message body
    assert has_message_body(304) == False  # 304 has no message body
    assert has_message_body(100) == False  # 1XX has no message body

# Test cases for is_entity_header
def test_is_entity_header():
    assert is_entity_header("content-type") == True  # 'content-type' is in _ENTITY_HEADERS
    assert is_entity_header("content-length") == True  # 'content-length' is in _ENTITY_HEADERS
    assert is_entity_header("connection") == False  # 'connection' is not in _ENTITY_HEADERS

# Test cases for is_hop_by_hop_header
def test_is_hop_by_hop_header():
    assert is_hop_by_hop_header("connection") == True  # 'connection' is in _HOP_BY_HOP_HEADERS
    assert is_hop_by_hop_header("upgrade") == True  # 'upgrade' is in _HOP_BY_HOP_HEADERS
    assert is_hop_by_hop_header("content-type") == False  # 'content-type' is not in _HOP_BY_HOP_HEADERS

# Test cases for import_string
# def test_import_string():
#     # Assuming we have a module `your_module` with a class `YourClass` defined as:
#     # class YourClass:
#     #     def __init__(self):
#     #         self.value = 42
#     #     def get_value(self):
#     #         return self.value

#     # Test importing the module (replace `your_module.YourClass` with your actual module/class name)
#     obj = import_string("your_module.YourClass")
#     assert obj.get_value() == 42  # Test if the class was imported and initialized properly

#     # Test importing a module object
#     module = import_string("your_module")
#     assert module is not None  # Ensure the module is loaded

# Test cases for is_atty
def test_is_atty(monkeypatch):
    # Mock sys.stdout to simulate an interactive terminal (isatty will return True)
    monkeypatch.setattr(sys.stdout, 'isatty', lambda: True)
    assert is_atty() == True  # Should return True since it's mocked to be interactive

    # Mock sys.stdout to simulate non-interactive (isatty will return False)
    monkeypatch.setattr(sys.stdout, 'isatty', lambda: False)
    assert is_atty() == False  # Should return False since it's mocked to be non-interactive

# # Test cases for Default class
# def test_default_class():
#     # Test the representation of Default object
#     default_obj = Default()
#     assert repr(default_obj) == "<Default>"
#     assert str(default_obj) == "<Default>"

#     # Ensure _default is an instance of Default
#     assert isinstance(_default, Default)

