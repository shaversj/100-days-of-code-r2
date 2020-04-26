import unittest
import parse_football


class MyTestCase(unittest.TestCase):
    def test_read_invalid_path_throws_exception(self):
        with self.assertRaises(FileNotFoundError):
            parse_football.read_csv_file("jgfjgfygjgj")

    def test_read_skips_header(self):
        expected_output = [["Arsenal", "38", "26", "9", "3", "79", "36", "87"],
                           ["Liverpool", "38", "24", "8", "6", "67", "30", "80"]]

        self.assertEqual(parse_football.read_csv_file("../test-football-data.csv"), expected_output)

    def test_get_team_with_smallest_difference(self):
        parsed_data = [["Arsenal", "38", "26", "9", "3", "79", "36", "87"],
                       ["Liverpool", "38", "24", "8", "6", "67", "30", "80"]]
        results = parse_football.find_team_with_smallest_difference(parsed_data)

        self.assertEqual(results, ["Liverpool", 37])


if __name__ == '__main__':
    unittest.main()
