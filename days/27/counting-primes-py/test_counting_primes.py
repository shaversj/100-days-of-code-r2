import unittest
from counting_primes import count_primes


class MyTestCase(unittest.TestCase):
    def test_basic_test(self):
        self.assertEqual(count_primes(2, 10), 4)
        self.assertEqual(count_primes(20, 30), 2)


if __name__ == '__main__':
    unittest.main()
