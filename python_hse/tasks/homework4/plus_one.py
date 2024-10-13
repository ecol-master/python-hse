"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/plus-one
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ind = len(digits) - 1

        while ind >= 0:
            if digits[ind] != 9:
                digits[ind] += 1
                break

            digits[ind] = 0
            ind -= 1

        if ind == -1:
            digits.insert(0, 1)

        return digits
