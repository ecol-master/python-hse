"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        result: str = "M" * (num // 1000)
        num = num % 1000

        if num // 100 == 9:
            result += "CM"
        elif num // 100 == 4:
            result += "CD"
        else:
            result += "D" * (num // 500) + "C" * (num // 100 - (num // 500) * 5)

        num = num % 100

        if num // 10 == 9:
            result += "XC"
        elif num // 10 == 4:
            result += "XL"
        else:
            result += "L" * (num // 50) + "X" * (num // 10 - (num // 50) * 5)

        num = num % 10

        if num == 9:
            result += "IX"
        elif num == 4:
            result += "IV"
        else:
            result += "V" * (num // 5) + "I" * (num - (num // 5) * 5)

        return result
