def find_longest_lines(file):
    # Write a program which reads a file and prints to stdout the specified number of the longest lines
    # that are sorted based on their length in descending order.

    results = []
    num_of_results = 0
    with open(file) as f:
        num_of_results = int(f.readline())
        for line in f.readlines():
            line = line.strip()
            results.append([line, len(line)])

    sorted_results = sorted(results, reverse=True, key=lambda x: x[1])

    for num in range(0, num_of_results):
        print(sorted_results[num][0])


find_longest_lines("input_file.txt")

# 2
# Hello World
# CodeEval
# Quick Fox
# A
# San Francisco
