import pytest
import operator
from iterator import (
    chunk, take, drop, drop_until, split_by, scanl, scanr,
    LazyList, Range, MapList
)


def test_chunk_gpt():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    with pytest.raises(ValueError):
        list(chunk(0, range(5)))


def test_take_gpt():
    assert list(take(5, range(10))) == [0, 1, 2, 3, 4]
    assert list(take(0, range(10))) == []
    assert list(take(100, range(5))) == [0, 1, 2, 3, 4]
    with pytest.raises(ValueError):
        list(take(-1, range(10)))


def test_drop_gpt():
    assert list(drop(5, range(10))) == [5, 6, 7, 8, 9]
    assert list(drop(0, range(5))) == [0, 1, 2, 3, 4]
    assert list(drop(10, range(5))) == []
    with pytest.raises(ValueError):
        list(drop(-1, range(10)))


def test_drop_until_gpt():
    assert list(drop_until(lambda x: x > 5, range(10))) == [6, 7, 8, 9]
    assert list(drop_until(lambda x: x == 0, range(5))) == [0, 1, 2, 3, 4]
    assert list(drop_until(lambda x: x > 10, range(5))) == []


def test_split_by_criterion_gpt():
    data = list(range(10))
    result = list(split_by(data, criterion=lambda x: x % 3 == 0))
    assert result == [[1, 2], [4, 5], [7, 8]]


def test_split_by_separator_gpt():
    data = list(" Split by: ")
    result = list(split_by(data, empty_segments=True, separator=' '))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]


def test_split_by_invalid_args_gpt():
    with pytest.raises(ValueError):
        list(split_by(range(5)))  # Neither separator nor criterion
    with pytest.raises(ValueError):
        list(split_by(range(5), criterion=lambda x: x, separator=3))  # Both provided


def test_scanl_with_initial_gpt():
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]


def test_scanl_without_initial_gpt():
    result = list(scanl(lambda acc, x: x + acc, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']


def test_scanr_with_initial_gpt():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]



def test_lazylist_access_gpt():
    ll = LazyList(range(10))
    assert ll[0] == 0
    assert ll[5] == 5
    assert ll[:3] == [0, 1, 2]
    with pytest.raises(TypeError):
        len(ll)
    # Force exhaustion
    list(ll)
    assert len(ll) == 10


def test_lazylist_iteration_gpt():
    ll = LazyList(range(5))
    assert list(ll) == [0, 1, 2, 3, 4]


def test_range_gpt():
    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[-1] == 9
    assert r[:3] == [1, 3, 5]
    assert len(r) == 5
    assert list(r) == [1, 3, 5, 7, 9]


def test_maplist_basic_gpt():
    a = [1, 2, 3, 4, 5]
    ml = MapList(lambda x: x * x, a)
    assert ml[0] == 1
    assert ml[2] == 9
    assert ml[:3] == [1, 4, 9]
    assert list(ml) == [1, 4, 9, 16, 25]
    assert len(ml) == 5


def test_maplist_with_index_func_gpt():
    a = [1, 2, 3]
    b = [4, 5, 6]
    ml = MapList(lambda i: a[i] * b[i], Range(3))
    assert list(ml) == [4, 10, 18]
