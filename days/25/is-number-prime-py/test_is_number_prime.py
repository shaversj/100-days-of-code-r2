import unittest
from is_number_prime import is_prime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_prime(4), False)


if __name__ == '__main__':
    unittest.main()
