import pytest
from collections import UserDict
from _timers import Timers  # Replace with the correct module name

@pytest.fixture
def timers():
    """Fixture to create a fresh Timers object before each test."""
    return Timers()

def test_add_timer(timers):
    """Test the add method of the Timers class."""
    timers.add('timer1', 1.5)
    timers.add('timer1', 2.5)

    # Check the total value in the dictionary
    assert timers.data['timer1'] == 4.0
    # Check the timings list
    assert timers._timings['timer1'] == [1.5, 2.5]

def test_clear(timers):
    """Test the clear method of the Timers class."""
    timers.add('timer1', 1.5)
    timers.add('timer2', 2.5)
    
    timers.clear()
    
    # After clear, data and _timings should be empty
    assert len(timers.data) == 0
    assert len(timers._timings) == 0

def test_disallow_setitem(timers):
    """Test that setting an item via __setitem__ raises a TypeError."""
    with pytest.raises(TypeError):
        timers['timer1'] = 3.0

def test_count(timers):
    """Test the count method of the Timers class."""
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    
    assert timers.count('timer1') == 2

def test_total(timers):
    """Test the total method of the Timers class."""
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    
    assert timers.total('timer1') == 3.0

def test_min(timers):
    """Test the min method of the Timers class."""
    timers.add('timer1', 3.0)
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    
    assert timers.min('timer1') == 1.0

def test_max(timers):
    """Test the max method of the Timers class."""
    timers.add('timer1', 3.0)
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    
    assert timers.max('timer1') == 3.0

def test_mean(timers):
    """Test the mean method of the Timers class."""
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    
    assert timers.mean('timer1') == 2.0

def test_median(timers):
    """Test the median method of the Timers class."""
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    
    assert timers.median('timer1') == 2.0

def test_apply(timers):
    """Test the apply method with a custom function."""
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    
    result = timers.apply(sum, 'timer1')
    assert result == 3.0
