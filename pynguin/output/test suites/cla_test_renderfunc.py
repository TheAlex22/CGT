import pytest
from sty.renderfunc import sgr, eightbit_fg, eightbit_bg, rgb_fg, rgb_bg

def test_sgr():
    """Test SGR escape sequence generation"""
    assert sgr(0) == "\033[0m"
    assert sgr(1) == "\033[1m"
    assert sgr(31) == "\033[31m"

def test_eightbit_fg():
    """Test 8-bit foreground color escape sequences"""
    assert eightbit_fg(0) == "\033[38;5;0m"
    assert eightbit_fg(255) == "\033[38;5;255m"
    assert eightbit_fg(128) == "\033[38;5;128m"

def test_eightbit_bg():
    """Test 8-bit background color escape sequences"""
    assert eightbit_bg(0) == "\033[48;5;0m"
    assert eightbit_bg(255) == "\033[48;5;255m"
    assert eightbit_bg(128) == "\033[48;5;128m"

def test_rgb_fg():
    """Test RGB foreground color escape sequences"""
    assert rgb_fg(0, 0, 0) == "\x1b[38;2;0;0;0m"
    assert rgb_fg(255, 255, 255) == "\x1b[38;2;255;255;255m"
    assert rgb_fg(128, 64, 32) == "\x1b[38;2;128;64;32m"

def test_rgb_bg():
    """Test RGB background color escape sequences"""
    assert rgb_bg(0, 0, 0) == "\x1b[48;2;0;0;0m"
    assert rgb_bg(255, 255, 255) == "\x1b[48;2;255;255;255m"
    assert rgb_bg(128, 64, 32) == "\x1b[48;2;128;64;32m"
    