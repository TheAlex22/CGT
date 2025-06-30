import pytest
from utils import (
    curry, identity, increase, eq, curried_map, curried_filter,
    find, compose, pipe, cond, memoize
)

def test_identity():
    """Test identity function"""
    assert identity(1) == 1
    assert identity("test") == "test"
    assert identity(None) is None
    complex_obj = {"a": 1}
    assert identity(complex_obj) is complex_obj

def test_increase():
    """Test increase function"""
    assert increase(0) == 1
    assert increase(-1) == 0
    assert increase(999) == 1000

def test_curry():
    """Test curry function"""
    def add(a, b, c):
        return a + b + c
    
    curried_add = curry(add)
    assert curried_add(1)(2)(3) == 6
    assert curried_add(1, 2)(3) == 6
    assert curried_add(1)(2, 3) == 6
    assert curried_add(1, 2, 3) == 6

def test_eq():
    """Test eq function"""
    assert eq(1)(1) is True
    assert eq(1)(2) is False
    assert eq("test")("test") is True
    assert eq([1, 2])([1, 2]) is True

def test_curried_map():
    """Test curried_map function"""
    double = lambda x: x * 2
    assert curried_map(double)([1, 2, 3]) == [2, 4, 6]
    assert curried_map(str)([1, 2, 3]) == ["1", "2", "3"]
    assert curried_map(double)([]) == []

def test_curried_filter():
    """Test curried_filter function"""
    is_even = lambda x: x % 2 == 0
    assert curried_filter(is_even)([1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x > 2)([1, 2, 3, 4]) == [3, 4]
    assert curried_filter(is_even)([]) == []

def test_find():
    """Test find function"""
    numbers = [1, 2, 3, 4, 5]
    assert find(numbers, lambda x: x > 3) == 4
    assert find(numbers, lambda x: x > 5) is None
    assert find([], lambda x: True) is None

def test_pipe():
    """Test pipe function"""
    double = lambda x: x * 2
    add_one = lambda x: x + 1
    assert pipe(5, double, add_one) == 11
    assert pipe(5, add_one, double) == 12
    assert pipe(5) == 5

def test_cond():
    """Test cond function"""
    fn = cond([
        (lambda x: x > 10, lambda x: "big"),
        (lambda x: x < 5, lambda x: "small"),
        (lambda x: True, lambda x: "medium")
    ])
    
    assert fn(15) == "big"
    assert fn(3) == "small"
    assert fn(7) == "medium"

def test_memoize():
    """Test memoize function"""
    call_count = 0
    
    def expensive_fn(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    memoized_fn = memoize(expensive_fn)
    
    assert memoized_fn(5) == 10
    assert call_count == 1
    assert memoized_fn(5) == 10
    assert call_count == 1  # Should not increase due to caching
    assert memoized_fn(6) == 12
    assert call_count == 2

def test_memoize_with_custom_key():
    """Test memoize function with custom key function"""
    call_count = 0
    
    def expensive_fn(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    custom_key = lambda a, b: abs(a) == abs(b)
    memoized_fn = memoize(expensive_fn, key=custom_key)
    
    assert memoized_fn(5) == 10
    assert call_count == 1
    assert memoized_fn(-5) == 10  # Should use cached value
    assert call_count == 1