import unittest
from find_s import is_square


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_square((1, 6), (6, 7), (2, 7), (9, 1)), False)
        self.assertEqual(is_square((4, 1), (3, 4), (0, 5), (1, 2)), False)
        self.assertEqual(is_square((4, 6), (5, 5), (5, 6), (4, 5)), True)


if __name__ == '__main__':
    unittest.main()
