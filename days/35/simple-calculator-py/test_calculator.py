import unittest
from calculator import main


class MyTestCase(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(main("250*14.3"), 3575)


if __name__ == '__main__':
    unittest.main()
