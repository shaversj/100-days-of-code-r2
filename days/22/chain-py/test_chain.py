import unittest
from chain import is_valid


class MyTestCase(unittest.TestCase):
    def test_good_chain(self):
        self.assertEqual(is_valid("BEGIN-3;4-2;3-4;2-END"), True)

    def test_bad_chain(self):
        self.assertEqual(is_valid("77-END;BEGIN-8;8-77;11-11"), False)

    def test_bad_chain_2(self):
        self.assertEqual(is_valid("BEGIN-3;4-3;3-4;2-END"), False)

if __name__ == '__main__':
    unittest.main()
