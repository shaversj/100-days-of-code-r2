import unittest
from delete_n_num import delete_nth


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        self.assertEqual(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
