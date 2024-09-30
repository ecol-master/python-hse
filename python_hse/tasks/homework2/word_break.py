from typing import List

"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-break/description
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        table = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i):
                if table[j] and s[j:i] in wordDict:
                    table[i] = True

        return table[n]
