# TODO: Write some comments in here

import unittest

from src.main import add
from src.main import subtract
from src.main import multiply
from src.main import divide

class TestMathIntegration(unittest.TestCase):

    def test_add_and_subtract(self):
        result = add(2, 3)
        result = subtract(result, 2)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main() 