import unittest
import array_abs

class MyTestCase(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(3, array_abs.find_duplicate([1, 4, 3, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
