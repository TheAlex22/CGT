import pytest
import operator
from typing import List
from iterator import (
    chunk, take, drop, drop_until, split_by,
    scanl, scanr, LazyList, Range, MapList
)

def test_chunk():
    """Test chunk function with various inputs"""
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(chunk(2, [1, 2, 3, 4, 5])) == [[1, 2], [3, 4], [5]]
    assert list(chunk(1, [1, 2, 3])) == [[1], [2], [3]]
    
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))
    with pytest.raises(ValueError):
        list(chunk(-1, range(10)))

def test_take():
    """Test take function"""
    assert list(take(3, range(10))) == [0, 1, 2]
    assert list(take(5, [1, 2, 3])) == [1, 2, 3]  # Less elements than requested
    assert list(take(0, range(10))) == []
    
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

def test_drop():
    """Test drop function"""
    assert list(drop(3, range(5))) == [3, 4]
    assert list(drop(5, [1, 2, 3])) == []  # Drop more than available
    assert list(drop(0, range(3))) == [0, 1, 2]
    
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))

def test_drop_until():
    """Test drop_until function"""
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 3, [1, 2, 3, 4])) == [3, 4]
    assert list(drop_until(lambda x: True, [1, 2, 3])) == [1, 2, 3]
    assert list(drop_until(lambda x: False, [1, 2, 3])) == []

def test_split_by_criterion():
    """Test split_by function with criterion"""
    assert list(split_by(range(10), criterion=lambda x: x % 3 == 0)) == [[1, 2], [4, 5], [7, 8]]
    assert list(split_by([1, 2, 3], criterion=lambda x: x == 2)) == [[1], [3]]
    
    # Test with empty_segments=True
    assert list(split_by([1, 2, 2, 3], empty_segments=True, criterion=lambda x: x == 2)) == [[1], [], [3]]

def test_split_by_separator():
    """Test split_by function with separator"""
    assert list(split_by("a.b.c", separator='.')) == [['a'], ['b'], ['c']]
    assert list(split_by("a..b", empty_segments=True, separator='.')) == [['a'], [], ['b']]

def test_scanl():
    """Test scanl function"""
    assert list(scanl(operator.add, [1, 2, 3, 4], 0)) == [0, 1, 3, 6, 10]
    assert list(scanl(lambda s, x: x + s, ['a', 'b', 'c'])) == ['a', 'ba', 'cba']
    
    with pytest.raises(ValueError):
        list(scanl(operator.add, [1, 2, 3], 0, 1))  # Too many arguments

def test_scanr():
    """Test scanr function"""
    assert scanr(operator.add, [1, 2, 3, 4], 0) == [10, 9, 7, 4, 0]
    assert scanr(lambda s, x: x + s, ['a', 'b', 'c']) == ['abc', 'bc', 'c']

def test_lazy_list():
    """Test LazyList class"""
    lazy = LazyList(range(5))
    assert lazy[0] == 0
    assert lazy[4] == 4
    assert lazy[1:4] == [1, 2, 3]
    
    with pytest.raises(TypeError):
        len(lazy)  # Length not available before exhaustion
    
    # Test iteration
    assert list(lazy) == [0, 1, 2, 3, 4]
    assert len(lazy) == 5  # Now length should be available

def test_map_list():
    """Test MapList class"""
    base_list = [1, 2, 3, 4, 5]
    mapped = MapList(lambda x: x * 2, base_list)
    
    assert mapped[0] == 2
    assert mapped[-1] == 10
    assert mapped[1:4] == [4, 6, 8]
    assert len(mapped) == 5
    assert list(mapped) == [2, 4, 6, 8, 10]