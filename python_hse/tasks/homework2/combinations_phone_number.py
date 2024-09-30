from typing import List

"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def __init__(self):
        self.phone_table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        combinations: List[str] = []
        for d in digits:
            if not len(combinations):
                combinations = list(self.phone_table[d])
                continue
            symbols = self.phone_table[d]
            for _ in range(len(combinations)):
                comb: str = combinations.pop()
                for s in symbols:
                    combinations.insert(0, comb + s)

        return combinations
