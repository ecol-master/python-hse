"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/description
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(
            [w.strip() for w in s.strip().split(" ")[::-1] if w.strip() != ""]
        )
