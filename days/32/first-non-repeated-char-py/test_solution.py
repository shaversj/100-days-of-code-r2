import unittest
from solution import find_first_non_repeated_char


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_first_non_repeated_char("yellow"), "y")
        self.assertEqual(find_first_non_repeated_char("tooth"), "h")

if __name__ == '__main__':
    unittest.main()
