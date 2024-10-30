# TODO: Add comments explaining this

import unittest

from src.main import add
from src.main import subtract
from src.main import multiply
from src.main import divide
from src.main import power


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(subtract(4, 1), 3)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_power(self):
        self.assertEqual(power(3, 2), 9)

if __name__ == "__main__":
    unittest.main()