"""
Task info:
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/fraction-to-recurring-decimal
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
