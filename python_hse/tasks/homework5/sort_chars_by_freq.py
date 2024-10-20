"""
Task info:
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/sort-characters-by-frequency
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map: dict[str, int] = dict()

        for ch in s:
            if ch in frequency_map.keys():
                frequency_map[ch] += 1
            else:
                frequency_map[ch] = 1

        itms = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        return "".join([item[0] * item[1] for item in itms])
