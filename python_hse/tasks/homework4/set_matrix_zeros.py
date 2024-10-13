"""
Task info:
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/set-matrix-zeroes
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix)
        m: int = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            for j in range(m):
                matrix[i][j] = 0

        for j in cols:
            for i in range(n):
                matrix[i][j] = 0
