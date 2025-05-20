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

