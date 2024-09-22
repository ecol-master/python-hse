"""
Task info:
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator-ii/
"""

from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.ops = ["+", "-", "*", "/"]
        self.stack_numbers = deque()
        self.stack_operations = deque()

    def calculate(self, s: str) -> int:
        symbols: List[str] = self.__parse_sequence(s)
        for symb in symbols:
            if symb.isdecimal():
                self.stack_numbers.append(int(symb))
                continue

            self.__process_add_operation(symb)

        while len(self.stack_operations) != 0:
            self.do_op(self.stack_operations.pop())

        return self.stack_numbers[-1]

    def __parse_sequence(self, s: str) -> List[str]:
        res: List[str] = list(s)
        i = 0
        while i < len(res) - 1:
            if res[i] == "" or res[i] == " ":
                res = res[:i] + res[i + 1 :]
                continue

            if res[i] in self.ops:
                i += 1
                continue

            if res[i].isdecimal() and res[i + 1].isdecimal():
                res[i] += res[i + 1]
                res = res[: i + 1] + res[i + 2 :]
                continue

            i += 1

        return res

    def __op_level(self, op: str) -> int:
        low_ops = ["+", "-"]
        high_ops = ["*", "/"]

        if op in low_ops:
            return 1
        if op in high_ops:
            return 2
        return 0

    def do_op(self, op: str) -> None:
        match op:
            case "+":
                self.stack_numbers.append(
                    self.stack_numbers.pop() + self.stack_numbers.pop()
                )
            case "-":
                first = self.stack_numbers.pop()
                second = self.stack_numbers.pop()
                self.stack_numbers.append(second - first)
            case "*":
                self.stack_numbers.append(
                    self.stack_numbers.pop() * self.stack_numbers.pop()
                )

            case "/":
                first = self.stack_numbers.pop()
                second = self.stack_numbers.pop()
                self.stack_numbers.append(int(second / first))
            case _:
                ...

    def __process_add_operation(self, new_op: str) -> None:
        if len(self.stack_operations) == 0:
            self.stack_operations.append(new_op)
            return

        if self.__op_level(new_op) <= self.__op_level(self.stack_operations[-1]):
            self.do_op(self.stack_operations.pop())
            self.__process_add_operation(new_op)
        else:
            self.stack_operations.append(new_op)
