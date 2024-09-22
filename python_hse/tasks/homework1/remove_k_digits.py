"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/remove-k-digits/description/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        if k == 0:
            return num

        i = 0
        while k != 0 and i < len(num) - 1:
            if num[i] > num[i + 1]:
                num = num[:i] + num[i + 1 :]
                k -= 1
                i = max(0, i - 1)
                continue

            i += 1

        j = len(num) - 1
        while k != 0 and j != -1:
            if num[j] == "0":
                j -= 1
                continue

            num = num[:j] + num[j + 1 :]
            k -= 1
            j -= 1

        if len(num) == 1:
            return num

        num = num[: len(num) - k]
        c = 0
        for n in num:
            if n != "0":
                break
            c += 1

        if len(num) == c:
            return "0"

        return num[c:]
