import unittest
from hackercup import calculate_beauty_of_string


class MyTestCase(unittest.TestCase):
    def test_given_test_cases(self):
        self.assertEqual(152, calculate_beauty_of_string("ABbCcc"))
        self.assertEqual(754, calculate_beauty_of_string("Good luck in the Facebook Hacker Cup this year!"))
        self.assertEqual(491, calculate_beauty_of_string("Ignore punctuation, please 🙂"))
        self.assertEqual(729, calculate_beauty_of_string("Sometimes test cases are hard to make up."))
        self.assertEqual(646, calculate_beauty_of_string("So I just go consult Professor Dalves"))


if __name__ == '__main__':
    unittest.main()
