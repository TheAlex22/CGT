import functions
import os
from random import Random
import unittest


class FunctionsTest(unittest.TestCase):
    def test_func_one(self):
        self.assertEqual(
            functions.func_one(),
            False
        )


    def test_func_three(self):
        self.assertEqual(
            functions.func_three(a='C:/temp'),
            False
        )


    def test_func_two(self):
        self.assertEqual(
            functions.func_two(a='C:/temp'),
            False
        )


    def test_main(self):
        self.assertEqual(
            functions.main(),
            None
        )


if __name__ == "__main__":
    unittest.main()
