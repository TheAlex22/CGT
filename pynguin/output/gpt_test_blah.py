import pytest
from blah import is_big_number, is_middling_number, is_both, start_with_a, some_other

# Test cases for is_big_number
def test_is_big_number():
    assert is_big_number(101) == True  # Number greater than 100
    assert is_big_number(100) == False  # Number equal to 100
    assert is_big_number(50) == False  # Number less than 100

# Test cases for is_middling_number
def test_is_middling_number():
    assert is_middling_number(51) == True  # Number between 50 and 2000
    assert is_middling_number(2000) == False  # Number equal to 2000
    assert is_middling_number(49) == False  # Number less than 50
    assert is_middling_number(2001) == False  # Number greater than 2000

# Test cases for is_both
def test_is_both():
    assert is_both(101) == True  # Number is both big and middling
    assert is_both(51) == False  # Number is middling but not big
    assert is_both(100) == False  # Number is not big and not middling
    assert is_both(2001) == False  # Number is not big and not middling

# Test cases for start_with_a
def test_start_with_a():
    assert start_with_a("Apple") == "Yeah"  # Word starts with 'A'
    assert start_with_a("apple") == "Yeah"  # Word starts with 'a' (case insensitive)
    assert start_with_a("Banana") == "Nah"  # Word starts with 'B'
    assert start_with_a("Zebra") == "Nah"  # Word starts with 'Z'

# Test cases for some_other
def test_some_other():
    assert some_other(101, "Apple") == 10  # Number is big or word starts with 'A'
    assert some_other(50, "Banana") == 5  # Number is not big and word does not start with 'A'
    #assert some_other(2001, "Zebra") == 5  # Number is not big and word does not start with 'A'
    assert some_other(101, "Banana") == 10  # Number is big or word starts with 'A'

