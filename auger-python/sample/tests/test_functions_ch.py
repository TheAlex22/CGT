import functions
import os
from random import Random
import unittest


class TestFunctions:
    def test_func_one(self):
        assert functions.func_one() == \
            False


    def test_func_three(self):
        assert functions.func_three(a='C:/temp') == \
            False


    def test_func_two(self):
        assert functions.func_two(a='C:/temp') == \
            False


    def test_main(self):
        assert functions.main() == \
            None


if __name__ == "__main__":
    unittest.main()
