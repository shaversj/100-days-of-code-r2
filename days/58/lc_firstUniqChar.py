class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1

        for key, value in counts.items():
            if value == 1:
                return s.index(key)

        return -1
