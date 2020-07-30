from typing import List


class LenCustom:

    @staticmethod
    def find_length(string: str):
        count = 0

        for char in string:
            count += 1

        return count


print(LenCustom.find_length("test"))
print(LenCustom.find_length([1, 2, 3, 4]))