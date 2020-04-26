from pathlib import Path
import sys


def read_csv_file(file_location):
    file = Path(file_location)
    results = []

    if file.exists():
        with open(file, 'r') as f:
            f.readline()
            for line in f:
                results.append(line.strip().split(','))
    else:
        raise FileNotFoundError

    return results


def find_team_with_smallest_difference(data):
    smallest_difference = sys.maxsize
    team_with_smallest_difference = ""

    for entry in data:
        current_team_name = entry[0]
        goals = int(entry[5])
        goals_allowed = int(entry[6])
        current_difference = abs(goals - goals_allowed)

        if current_difference < smallest_difference:
            smallest_difference = current_difference
            team_with_smallest_difference = current_team_name

    return [team_with_smallest_difference, smallest_difference]


if __name__ == '__main__':
    parsed_data = read_csv_file("../football.csv")
    print(find_team_with_smallest_difference(parsed_data))
