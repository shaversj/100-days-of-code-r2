import unittest
from decimal_to_binary import convert_decimal_to_binary


class MyTestCase(unittest.TestCase):
    def test_basic_test(self):
        self.assertEqual(convert_decimal_to_binary(2), "10")
        self.assertEqual(convert_decimal_to_binary(10), "1010")
        self.assertEqual(convert_decimal_to_binary(67), "1000011")


if __name__ == '__main__':
    unittest.main()
