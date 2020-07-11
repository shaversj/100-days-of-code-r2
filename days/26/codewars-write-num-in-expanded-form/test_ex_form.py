import unittest
from ex_form import expanded_form


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
        self.assertEqual(expanded_form(3450), '3000 + 400 + 50')


if __name__ == '__main__':
    unittest.main()
