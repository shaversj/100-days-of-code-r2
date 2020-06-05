import unittest
from dash_insert import num_dash_insert

class MyTestCase(unittest.TestCase):
    def test_num_dash_insert(self):
        self.assertEqual("123-36*6", num_dash_insert(123366))


if __name__ == '__main__':
    unittest.main()
