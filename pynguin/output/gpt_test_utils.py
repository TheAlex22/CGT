import pytest
from utils import (
    curry, identity, increase, eq, curried_map, curried_filter, find, compose, pipe, cond, memoize
)

# Test identity function
def test_identity():
    assert identity(5) == 5
    assert identity("test") == "test"
    assert identity([1, 2, 3]) == [1, 2, 3]

# Test increase function
def test_increase():
    assert increase(1) == 2
    assert increase(0) == 1
    assert increase(-1) == 0

# Test eq function (curried version)
def test_eq():
    eq_5 = eq(5)
    assert eq_5(5) is True
    assert eq_5(6) is False

# Test curried_map function
def test_curried_map():
    curried_double = curried_map(lambda x: x * 2)
    assert curried_double([1, 2, 3]) == [2, 4, 6]
    assert curried_double([0, -1, -2]) == [0, -2, -4]

# Test curried_filter function
def test_curried_filter():
    curried_even = curried_filter(lambda x: x % 2 == 0)
    assert curried_even([1, 2, 3, 4, 5]) == [2, 4]
    assert curried_even([1, 3, 5]) == []

# Test find function
def test_find():
    assert find([1, 2, 3, 4], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 5) is None

# Test pipe function
def test_pipe():
    assert pipe(2, lambda x: x + 1, lambda x: x * 2) == 6
    assert pipe(3, lambda x: x - 1, lambda x: x ** 2) == 4

# Test cond function
def test_cond():
    condition = cond([
        (lambda x: x > 0, lambda x: "positive"),
        (lambda x: x < 0, lambda x: "negative"),
    ])
    assert condition(5) == "positive"
    assert condition(-1) == "negative"
    assert condition(0) is None  # No condition matches

# Test memoize function
def test_memoize():
    # Memoization should return cached results on subsequent calls
    def slow_function(x):
        return x * 2

    memoized_function = memoize(slow_function)

    # First call will compute the result
    assert memoized_function(2) == 4
    # Second call with the same argument should return the cached result
    assert memoized_function(2) == 4
    # Calling with a different argument should compute again
    assert memoized_function(3) == 6
