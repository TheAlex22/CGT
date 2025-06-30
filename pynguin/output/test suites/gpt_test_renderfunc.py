import pytest
from renderfunc import sgr, eightbit_fg, eightbit_bg, rgb_fg, rgb_bg  # Replace `your_module` with the actual module name


def test_sgr():
    # Test for valid SGR sequences
    assert sgr(0) == "\033[0m"
    assert sgr(1) == "\033[1m"
    assert sgr(30) == "\033[30m"
    assert sgr(255) == "\033[255m"


def test_eightbit_fg():
    # Test for valid 8bit foreground color sequences
    assert eightbit_fg(0) == "\033[38;5;0m"
    assert eightbit_fg(255) == "\033[38;5;255m"
    assert eightbit_fg(128) == "\033[38;5;128m"


def test_eightbit_bg():
    # Test for valid 8bit background color sequences
    assert eightbit_bg(0) == "\033[48;5;0m"
    assert eightbit_bg(255) == "\033[48;5;255m"
    assert eightbit_bg(128) == "\033[48;5;128m"


def test_rgb_fg():
    # Test for valid RGB foreground color sequences
    assert rgb_fg(255, 0, 0) == "\x1b[38;2;255;0;0m"
    assert rgb_fg(0, 255, 0) == "\x1b[38;2;0;255;0m"
    assert rgb_fg(0, 0, 255) == "\x1b[38;2;0;0;255m"
    assert rgb_fg(128, 128, 128) == "\x1b[38;2;128;128;128m"


def test_rgb_bg():
    # Test for valid RGB background color sequences
    assert rgb_bg(255, 0, 0) == "\x1b[48;2;255;0;0m"
    assert rgb_bg(0, 255, 0) == "\x1b[48;2;0;255;0m"
    assert rgb_bg(0, 0, 255) == "\x1b[48;2;0;0;255m"
    assert rgb_bg(128, 128, 128) == "\x1b[48;2;128;128;128m"
