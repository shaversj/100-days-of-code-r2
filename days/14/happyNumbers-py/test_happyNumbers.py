import unittest
import happyNumbers as hn


class MyTestCase(unittest.TestCase):
    def test_sum_square_of_digits(self):
        self.assertEqual(hn.sum_square_of_digits(19), 82)
        self.assertEqual(hn.sum_square_of_digits(100), 1)

    def test_is_happy_number(self):
        self.assertEqual(hn.is_happy_number(19), True)
        self.assertEqual(hn.is_happy_number(12), False)


if __name__ == '__main__':
    unittest.main()
