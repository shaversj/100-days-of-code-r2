from typing import List


def find_duplicate(values: List) -> int:
    return sum(values) - sum(set(values))
