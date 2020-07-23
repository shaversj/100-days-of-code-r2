def jolly_jumpers(numbers):
    diffs = []
    jolly_list = [jolly for jolly in range(1, len(numbers))]
    for idx in range(0, len(numbers) - 1):
        diffs.append(abs(numbers[idx] - numbers[idx + 1]))

    if sorted(diffs) != jolly_list:
        return False

    return True


print(jolly_jumpers([1, 4, 2, 3]))
print(jolly_jumpers([3, 7, 6, 8]))
print(jolly_jumpers([9, 8, 9, 7, 10, 6, 12, 17, 24, 38]))