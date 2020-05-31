import unittest
import alternateCase


class MyTestCase(unittest.TestCase):
    def test_empty_string_returns_empty_string(self):
        self.assertEqual(alternateCase.alternate_case(""), "")

    def test_word_alternates_case(self):
        self.assertEqual(alternateCase.alternate_case("The"), "ThE")

    def test_sentence(self):
        self.assertEqual(alternateCase.alternate_case("The quick brown fox."), "ThE qUiCk BrOwN fOx.")

    def test_sentence_with_comma(self):
        self.assertEqual(alternateCase.alternate_case("Four score, and seven years ago."), "FoUr ScOrE, aNd SeVeN yEaRs AgO.")

if __name__ == '__main__':
    unittest.main()
