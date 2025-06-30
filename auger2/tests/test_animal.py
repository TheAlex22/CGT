import animal
from animal import Animal
import random
from random import Random
import unittest


class TestAnimal:
    def test___set_age(self):
        assert Animal("Cat",10,)._Animal__set_age(age=10) == \
            None


    def test___str__(self):
        assert Animal("Cat",10,).__str__() == \
            'Cat:10'


    def test_get_species(self):
        assert Animal("Cat",10,).get_species() == \
            'Cat'


    def test_main(self):
        assert animal.main() == \
            None


if __name__ == "__main__":
    unittest.main()
